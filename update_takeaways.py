import json

with open("/Users/nora/Flair WhiteSpace/flair-tiktok-outliers.json") as f:
    data = json.load(f)

FLAIR_VERSIONS = {
    "Audio trends with brand overlay require minimal production and deliver outsized reach":
        "Flair's version: trending audio + crew dancing at the gate, or a 737 engine spool-up synced to a viral sound. Zero budget, maximum algorithm.",

    "Aviation geek content has a massive built-in audience — aircraft and operations content performs reliably":
        "Flair's version: 737 MAX walkarounds, cockpit prep sequences, de-icing in Canadian winter. Flair's fleet is newer than most Canadians realize.",

    "Behind-the-scenes operations content satisfies curiosity and builds trust":
        "Flair's version: show the turnaround operation. 99% completion factor is invisible to passengers — BTS content makes it real.",

    "Brand culture content works when tied to a specific, concrete action or change":
        "Flair's version: the ULCC-to-value-carrier rebrand is a concrete story. New CEO, new routes, new standards. Show it, don't just announce it.",

    "Budget carriers that own their identity through humor build cult followings on TikTok":
        "Flair's version: own the price gap. \"They charge $800, we charge $89. Same sky.\" Self-aware budget humor is Flair's unfair advantage.",

    "Cinematic destination content can be adapted to Flair's Canadian and warm-weather routes":
        "Flair's version: Cancun from Edmonton for $149, Montego Bay from Toronto. Pair the destination beauty with the price shock.",

    "Corporate announcements with human-centered visuals outperform press release formats":
        "Flair's version: new route to Jamaica? Film the crew celebrating, not a graphic. New CEO? Show him walking the cabin, not a headshot.",

    "Creator collabs amplify reach but need to feel organic — Canadian creators in Flair's demo would work":
        "Flair's version: partner with Canadian travel creators who fly budget. Their audience IS Flair's customer. Authentic > aspirational.",

    "Crew content with trending audio is a proven formula for budget carriers":
        "Flair's version: Flair crew + trending audio = the single fastest path to TikTok growth. Give 3 crew members phones and a loose brief this week.",

    "Crew personality content consistently outperforms polished brand content — Flair should launch a recurring crew series":
        "Flair's version: weekly crew spotlight series. Day-in-the-life from Edmonton, Toronto, or Cancun layover. Let the crew be the brand.",

    "Destination content works but Flair should focus on Canadian domestic and sun destinations":
        "Flair's version: Kelowna wine country, Halifax waterfront, Montego Bay beaches — all from cities other airlines overcharge for.",

    "Destination showcase content with route-specific hooks drives saves and shares":
        "Flair's version: \"Vancouver to Cancun, $149\" over gorgeous beach footage. The price IS the hook. Saves = future bookings.",

    "Emotional passenger stories drive the highest share rates in airline TikTok":
        "Flair's version: the family flying together for the first time because they could finally afford it. That's Flair's brand story in a single clip.",

    "Flash deal content with urgency mechanics drives both engagement and conversion signals":
        "Flair's version: \"$49 flights dropping in 3... 2... 1...\" with a countdown format. Flair's price advantage is made for this.",

    "Flight attendant-led content drives massive engagement; Flair crew could be the brand's TikTok voice":
        "Flair's version: pick 2-3 charismatic crew members. Make them recurring characters. Flair's TikTok voice should be crew-first, brand-second.",

    "Inclusive policy announcements generate massive goodwill and shareability":
        "Flair's version: accessibility as an airline for everyone is a values story waiting to be told. Show what affordable travel changes for real people.",

    "Jumping on trends with airline-specific twists is high-ROI content — fast turnaround matters more than polish":
        "Flair's version: empower the social team to post within 48 hours of a trend emerging. A rough crew TikTok today beats a polished one next week.",

    "New aircraft or fleet content generates excitement even for budget carriers":
        "Flair's version: 737 MAX delivery content. Most Canadians don't know Flair flies brand-new planes. Show them.",

    "New route announcements are content gold — plan capture strategy for every inaugural":
        "Flair's version: Jamaica and Montreal launches should have been 5-10 content pieces each. Build a capture checklist for every future route launch.",

    "Playful self-deprecation turns brand perception into content advantage":
        "Flair's version: lean into the complaints. \"You said we'd never be on time. We just hit 99% completion. Anyway, here's a $49 flight.\"",

    "Policy and values announcements delivered through people (not graphics) generate outsized engagement":
        "Flair's version: operational milestones told through crew pride, not press releases. The people who turned this airline around are the story.",

    "Premium/brand-specific content not transferable to Flair's budget positioning — observe the format, not the execution":
        "Flair's version: ignore the first-class suites. Watch HOW they film — the pacing, the reveals, the audio choices. Steal the format, not the lifestyle.",

    "Price-led content works when it feels native to TikTok — avoid traditional ad formats":
        "Flair's version: \"POV: your friend says flights to Mexico are too expensive\" [cuts to Flair booking at $129]. Price as punchline, not banner ad.",

    "Product announcements succeed when they feel like content, not ads":
        "Flair's version: Flair Express priority boarding? Show a passenger breezing past the line with trending audio. Feature, not ad.",

    "Promotional content needs TikTok-native execution — Flair deals with personality would perform":
        "Flair's version: seat sales announced by crew, not graphics. Trend audio over the booking screen. Make the deal feel like content.",

    "Route announcement content performs well — adapt the format to Flair's network expansion":
        "Flair's version: every new route = a content event. Film crew reactions, first passengers, destination reveals. Flair is expanding — show it.",

    "Short-form BTS of operations humanizes the brand and feeds aviation enthusiasm":
        "Flair's version: pre-dawn crew briefing, pushback in Canadian winter, cockpit views over the Rockies. Flair's operation has stories to tell.",

    "Speed-to-trend matters more than production value on TikTok":
        "Flair's version: build a rapid-response content process. Trending audio today, Flair version posted tomorrow. That's how you grow on TikTok.",

    "Staff-led content builds brand affinity without production budget":
        "Flair's version: phone + crew member + 30 seconds = Flair's most effective content format. No agency, no studio, no excuse not to start.",

    "Surprising passengers with in-flight moments creates highly shareable content":
        "Flair's version: surprise upgrades, milestone flights (100th flight, birthday, honeymoon). Equip crew to spot and capture these moments.",

    "This creator collab content pattern is directly replicable for Flair":
        "Flair's version: partner with mid-tier Canadian creators (50K-200K) who match Flair's audience. Send them on a route, let them create.",

    "This milestone content pattern is directly replicable for Flair":
        "Flair's version: new route launches, fleet milestones, operational records. Flair has a steady stream of firsts — each one is content.",

    "Travel aspiration content paired with route announcements amplifies reach":
        "Flair's version: pair dreamy destination footage with Flair's actual price. The aspiration + affordability combo is unique to Flair.",

    "Trend-jacking with brand personality drives outsized engagement at zero production cost":
        "Flair's version: \"Don't be ultra basic\" energy applied to every trending format. Flair's competitive personality is a content engine.",

    "UGC-style passenger content drives both shares and saves, signaling high value":
        "Flair's version: build #FlyFlair into a UGC engine. Repost passenger content weekly. 4.5M annual passengers = massive untapped content library.",

    "Value propositions delivered with personality outperform corporate promotional posts":
        "Flair's version: free snacks announcement? Film the crew taste-testing. TravelFlex launch? Show a passenger changing their trip last-minute. Features through people.",

    "Influencer partnerships drive reach when they feel like content, not sponsorship":
        "Flair's version: skip the polished #ad. Send a creator on a Flair trip and let them post raw. Authenticity > production value.",

    "This behind-the-scenes format works but needs Flair voice and Canadian context":
        "Flair's version: same format, Canadian setting. De-icing in -30°C, flying over the Rockies, turnarounds at YEG. Canadian operations content.",

    "This destination format works but needs Flair voice and Canadian context":
        "Flair's version: same format, Flair routes. Cancun, Puerto Vallarta, Halifax, Kelowna — destinations Flair actually flies to, at prices that shock.",

    "Operations content performs well; adapt with Flair's fleet and Canadian context":
        "Flair's version: 737 MAX content with a Canadian twist. Winter ops, cross-country flights, new route prep. Flair's operation is the content.",

    "Milestone moments are powerful but time-limited — Flair should plan content around route launches and fleet milestones":
        "Flair's version: build a content capture checklist for every milestone. Jamaica launch, Montreal resumption, fleet additions. Plan the content before the moment.",

    "Humanizing the crew creates emotional connection that polished production can't match":
        "Flair's version: Flair crew are young, diverse, bilingual. That's a casting advantage. Let them be themselves on camera.",

    "Meme-format content drives shares; short, punchy humor outperforms longer narratives":
        "Flair's version: meme the price difference. \"Me booking a $79 Flair flight while my friend pays $400 on [redacted].\" Short, shareable, on-brand.",

    "Trend participation shows platform fluency and keeps the brand culturally relevant":
        "Flair's version: consistent trend participation signals to TikTok audiences that Flair is a modern, culturally aware brand — not a legacy carrier.",

    "Self-aware humor about budget travel resonates deeply — Flair should lean into its value positioning with wit":
        "Flair's version: \"No free checked bag. But your flight was $59. You're welcome.\" Own every criticism with humor and a price drop.",

    "Real passenger moments generate authentic engagement — Flair should empower crew to capture these":
        "Flair's version: create a crew content capture guide. What to film, how to ask permission, where to send it. Make it easy for moments to reach the social team.",
}

updated = 0
for airline in data["airlines"]:
    for o in airline["outliers"]:
        old = o.get("flairTakeaway", "")
        if old in FLAIR_VERSIONS:
            o["flairTakeaway"] = old + " " + FLAIR_VERSIONS[old]
            updated += 1
        elif old and "Flair's version:" not in old:
            # Generic fallback for any we missed
            o["flairTakeaway"] = old + " Flair's version: adapt this format with Flair crew, Canadian routes, and budget-airline personality."
            updated += 1

with open("/Users/nora/Flair WhiteSpace/flair-tiktok-outliers.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated {updated} takeaways with Flair-specific versions")
