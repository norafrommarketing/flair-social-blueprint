#!/usr/bin/env python3
"""
Step 1: Process 25 airline TikTok JSON files into outliers.json
Per the PRD: calculate derived metrics, detect outliers, extract top 5 per airline.
"""

import json
import os
import statistics
from datetime import datetime

DATASETS_DIR = "/Users/nora/Flair WhiteSpace/Datasets"
OUTPUT_FILE = "/Users/nora/Flair WhiteSpace/flair-tiktok-outliers.json"

# Region mapping for sort order (North American first, then European, then rest)
REGION_MAP = {
    "Air Canada": "north_america",
    "Alaska Airlines": "north_america",
    "delta": "north_america",
    "Frontier Airlines": "north_america",
    "Hawaiian Airlines": "north_america",
    "JetBlue": "north_america",
    "Southwest Airlines": "north_america",
    "Spirit Airlines": "north_america",
    "United Airlines": "north_america",
    "WestJet": "north_america",
    "British Airways": "europe",
    "easyJet": "europe",
    "Icelandair": "europe",
    "Lufthansa": "europe",
    "VirginAtlantic": "europe",
    "Emirates": "middle_east",
    "Etihad": "middle_east",
    "Qatar Airways": "middle_east",
    "Cathay Pacific ✈️": "asia_pacific",
    "flyscoot": "asia_pacific",
    "Singapore Airlines": "asia_pacific",
    "Fly AirAsia": "asia_pacific",
    "LATAM Airlines": "latin_america",
    "SKY ✈️": "latin_america",
    "طيران أديل": "middle_east",  # Fly Deal / flyadeal
}

REGION_SORT_ORDER = {
    "north_america": 0,
    "europe": 1,
    "middle_east": 2,
    "asia_pacific": 3,
    "latin_america": 4,
}

# Clean display names
DISPLAY_NAMES = {
    "delta": "Delta Air Lines",
    "easyJet": "EasyJet",
    "VirginAtlantic": "Virgin Atlantic",
    "flyscoot": "Scoot",
    "Cathay Pacific ✈️": "Cathay Pacific",
    "SKY ✈️": "SKY Airline",
    "طيران أديل": "flyadeal",
}


def process_post(post, fans):
    """Calculate derived metrics for a single post."""
    play = post.get("playCount", 0) or 0
    digg = post.get("diggCount", 0) or 0
    share = post.get("shareCount", 0) or 0
    collect = post.get("collectCount", 0) or 0
    comment = post.get("commentCount", 0) or 0

    views_per_follower = play / fans if fans > 0 else 0
    engagement_rate = (digg + comment + share + collect) / play if play > 0 else 0
    share_rate = share / play if play > 0 else 0
    save_rate = collect / play if play > 0 else 0

    hashtags = [h.get("name", "") for h in post.get("hashtags", []) if h.get("name")]
    duration = post.get("videoMeta", {}).get("duration", 0) or 0
    cover_url = post.get("videoMeta", {}).get("coverUrl", "")
    date_str = post.get("createTimeISO", "")
    date_short = date_str[:10] if date_str else ""

    return {
        "id": post.get("id", ""),
        "text": (post.get("text", "") or "")[:300],
        "date": date_short,
        "dateISO": date_str,
        "views": play,
        "likes": digg,
        "shares": share,
        "saves": collect,
        "comments": comment,
        "duration": duration,
        "viewsPerFollower": round(views_per_follower, 2),
        "engagementRate": round(engagement_rate, 4),
        "shareRate": round(share_rate, 4),
        "saveRate": round(save_rate, 4),
        "thumbnailUrl": cover_url,
        "videoUrl": post.get("webVideoUrl", ""),
        "hashtags": hashtags,
        # Placeholders for manual/AI tagging
        "contentTheme": "",
        "repeatability": "",
        "flairRelevance": "",
        "flairTakeaway": "",
    }


def detect_outliers(processed_posts, top_n=5):
    """
    Flag posts where viewsPerFollower > 2x median OR > 1.5 std devs above mean.
    Return top N by viewsPerFollower.
    """
    if not processed_posts:
        return [], 0, 0

    vpf_values = [p["viewsPerFollower"] for p in processed_posts if p["viewsPerFollower"] > 0]
    if not vpf_values:
        return processed_posts[:top_n], 0, 0

    median_vpf = statistics.median(vpf_values)
    mean_vpf = statistics.mean(vpf_values)
    std_vpf = statistics.stdev(vpf_values) if len(vpf_values) > 1 else 0

    threshold_2x = median_vpf * 2
    threshold_std = mean_vpf + (1.5 * std_vpf)

    for p in processed_posts:
        is_outlier = p["viewsPerFollower"] > threshold_2x or p["viewsPerFollower"] > threshold_std
        p["isOutlier"] = is_outlier
        p["outlierScore"] = round(p["viewsPerFollower"] / median_vpf, 1) if median_vpf > 0 else 0

    # Sort by viewsPerFollower descending, take top N
    sorted_posts = sorted(processed_posts, key=lambda x: x["viewsPerFollower"], reverse=True)
    top_outliers = sorted_posts[:top_n]

    return top_outliers, median_vpf, mean_vpf


def process_airline(filepath):
    """Process one airline's JSON file."""
    with open(filepath) as f:
        posts = json.load(f)

    if not posts:
        return None

    # Get airline metadata from first post
    author = posts[0].get("authorMeta", {})
    fans = author.get("fans", 0) or 0
    nick = author.get("nickName", "Unknown")
    handle = author.get("name", "")
    display_name = DISPLAY_NAMES.get(nick, nick)
    region = REGION_MAP.get(nick, "other")

    # Process all posts
    processed = [process_post(p, fans) for p in posts]

    # Airline-level stats
    all_views = [p["views"] for p in processed if p["views"] > 0]
    all_vpf = [p["viewsPerFollower"] for p in processed if p["viewsPerFollower"] > 0]
    all_er = [p["engagementRate"] for p in processed if p["engagementRate"] > 0]

    median_views = statistics.median(all_views) if all_views else 0
    avg_views = statistics.mean(all_views) if all_views else 0
    median_vpf = statistics.median(all_vpf) if all_vpf else 0
    avg_er = statistics.mean(all_er) if all_er else 0

    # Detect outliers
    outliers, _, _ = detect_outliers(processed, top_n=5)

    return {
        "name": display_name,
        "handle": handle,
        "nickName": nick,
        "followers": fans,
        "region": region,
        "totalPosts": len(posts),
        "medianViews": round(median_views),
        "avgViews": round(avg_views),
        "medianViewsPerFollower": round(median_vpf, 2),
        "avgEngagementRate": round(avg_er, 4),
        "topContentThemes": [],  # Populated after tagging
        "outliers": outliers,
    }


def main():
    airlines = []
    total_posts = 0

    for filename in sorted(os.listdir(DATASETS_DIR)):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(DATASETS_DIR, filename)
        print(f"Processing {filename}...")
        airline = process_airline(filepath)
        if airline:
            airlines.append(airline)
            total_posts += airline["totalPosts"]
            print(f"  → {airline['name']}: {airline['totalPosts']} posts, "
                  f"{airline['followers']:,} followers, "
                  f"best outlier: {airline['outliers'][0]['outlierScore']}x" if airline['outliers'] else "  → No outliers")

    # Sort: North American first, then European, then rest
    airlines.sort(key=lambda a: (REGION_SORT_ORDER.get(a["region"], 99), a["name"]))

    total_outliers = sum(len(a["outliers"]) for a in airlines)

    dashboard_data = {
        "generated": datetime.now().isoformat(),
        "summary": {
            "totalAirlines": len(airlines),
            "totalPostsAnalyzed": total_posts,
            "totalOutliers": total_outliers,
            "patterns": [],  # Populated after tagging
            "flairRecommendations": [],  # Populated after tagging
        },
        "airlines": airlines,
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(dashboard_data, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"DONE: {len(airlines)} airlines, {total_posts} posts, {total_outliers} outliers")
    print(f"Output: {OUTPUT_FILE}")

    # Print quick summary
    print(f"\n{'='*60}")
    print("TOP 10 OUTLIERS ACROSS ALL AIRLINES:")
    print(f"{'='*60}")
    all_outliers = []
    for a in airlines:
        for o in a["outliers"]:
            all_outliers.append({**o, "airline": a["name"]})
    all_outliers.sort(key=lambda x: x["viewsPerFollower"], reverse=True)
    for i, o in enumerate(all_outliers[:10], 1):
        print(f"{i:2}. {o['airline']:20s} | {o['outlierScore']:5.1f}x | "
              f"{o['views']:>12,} views | {o['text'][:60]}")


if __name__ == "__main__":
    main()
