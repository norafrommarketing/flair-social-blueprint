import json

with open("/Users/nora/Flair WhiteSpace/flair-tiktok-outliers.json") as f:
    data = json.load(f)

# For every outlier: read the caption, understand the video, write Flair's version of THAT video
# Format: "General insight. Flair's version: what Flair's version of this specific video would be."

VERSIONS = {
    # ═══ AIR CANADA ═══
    # 1. Destination showcase - nonstop from Vancouver to tropical destination
    "7482780770554203397": (
        "Cinematic destination content paired with a specific route drives massive reach.",
        "Short destination reel for Flair's Vancouver to Cancun or Edmonton to Puerto Vallarta. Beautiful footage, simple caption, let the destination do the talking."
    ),
    # 2. New route Montreal to Naples - dreamy Italy content
    "7505068070856084791": (
        "New route announcements wrapped in destination storytelling outperform plain announcements.",
        "Flair's Montreal to Jamaica or Toronto to Guadalajara announced the same way. Dreamy destination footage, bilingual caption, the route is the hook."
    ),
    # 3. Free beer wine and snacks announcement
    "7556261417515568401": (
        "Onboard experience upgrades announced as simple, shareable moments drive views.",
        "Any Flair onboard improvement announced the same way. Crew pouring drinks, passengers reacting, short and feel-good."
    ),
    # 4. FlyTheFlag teaser - something big coming
    "7559620746109029650": (
        "Teaser content with national pride builds anticipation and shares.",
        "Tease Flair's next big route launch or fleet milestone with Canadian flag energy. Build-up content before the reveal."
    ),
    # 5. Team Air Canada heading to Milano Cortina Olympics
    "7561088475907542279": (
        "National pride content with athletes and team moments drives massive reach.",
        "Flair crew cheering on Team Canada during major sporting events. Film crew watching hockey, reacting to Canadian wins. National pride, crew energy."
    ),

    # ═══ ALASKA AIRLINES ═══
    # 1. Star Wars Galaxy's Edge themed flight
    "7093888452785392942": (
        "Pop culture themed flights create scroll-stopping, highly shareable content.",
        "Flair themed flight for a Canadian cultural moment. Hockey playoff flight, holiday themed cabin, crew dressed up for Halloween. The event becomes the content."
    ),
    # 2. Porg (Star Wars character) on the plane - cute mascot content
    "7094765877891157294": (
        "Mascot and character content with humor generates massive engagement and shares.",
        "Flair crew interacting with a fun prop or mascot on board. Could be a stuffed moose, a hockey puck, anything distinctly Canadian and playful."
    ),
    # 3. AI bot writes a Big Game commercial - collab with Tan France
    "7194595177523318062": (
        "Timely cultural commentary with a celebrity cameo creates viral moments.",
        "Flair reacts to an AI-generated Flair ad or trending cultural moment. Crew watches and reacts. Low production, high personality."
    ),
    # 4. New plane smell - fleet reveal content
    "7140762175139810602": (
        "New aircraft content with enthusiasm and personality drives aviation audience engagement.",
        "Flair's brand-new 737 MAX walkthrough. Crew showing off the cabin, that new plane smell energy. Most Canadians don't know Flair flies new planes."
    ),
    # 5. Cheese platter available on more routes
    "7512147436459035934": (
        "Food and snack content framed with personality outperforms standard product announcements.",
        "Flair crew taste-testing onboard snacks or showing what you can buy on board. Make the in-flight experience feel fun, not transactional."
    ),

    # ═══ DELTA ═══
    # 1. New in-flight activities for SkyMiles members - gamification tease
    "7285423062609235246": (
        "Teasing new in-flight features as exclusive unlocks creates curiosity and massive views.",
        "Flair teasing a new onboard feature or experience. Short, mysterious, let the audience guess. Works even for small upgrades."
    ),
    # 2. Futurecore - Sustainable Skies Lab, cinematic sustainability content
    "7559224803299839262": (
        "Cinematic sustainability content with a cool aesthetic drives views beyond the usual audience.",
        "Flair's operational efficiency story told cinematically. 99% completion factor, newest fleet in Canada, reduced emissions. Make it look cool."
    ),
    # 3. Group Drop - SkyMiles Experiences access to events
    "7564416669913845022": (
        "Exclusive experience teasers create aspirational engagement and shares.",
        "Flair offering a unique experience tied to a destination. Win a trip to Cancun, backstage at a concert in Montreal. The experience is the content."
    ),
    # 4. Don't leave mom on read + free wifi announcement
    "7202667559999589678": (
        "Relatable humor paired with a product feature makes announcements feel native to TikTok.",
        "Flair crew or passengers in a relatable moment that naturally features something about the Flair experience. Humor first, feature second."
    ),
    # 5. Free wifi pinky promise
    "7195245073154575659": (
        "Simple, personality-driven product announcements with trending energy outperform corporate reveals.",
        "Any Flair improvement announced with crew energy and a simple visual. Pinky promise format, crew reacting, passengers celebrating. Keep it human."
    ),

    # ═══ FRONTIER ═══
    # 1. John Leonard Coca-Cola jet story - years-long dream fulfilled
    "7604656245215137038": (
        "Storytelling that ties into cultural moments and fulfills a passenger dream creates earned reach.",
        "Find the Flair passenger with a great story. The grandma flying for the first time, the kid who loves planes, the family reuniting. Real stories, real people."
    ),
    # 2. All-You-Can-Fly annual pass for $499
    "7451691022557416735": (
        "Bold, disruptive product announcements generate massive shares when the offer itself is the hook.",
        "Flair announcing a bold offer or new product with crew excitement. Film the team reacting to the announcement, not just a graphic."
    ),
    # 3. $19 flight with trending audio (Don't Put The Blame On Me)
    "7205994481445784878": (
        "Trending audio paired with a simple brand moment drives outsized reach through the algorithm.",
        "Flair crew vibing to trending audio at the gate, on the tarmac, or in the cabin. The audio carries the reach, the brand gets the exposure."
    ),
    # 4. Xavier's surprise kindergarten graduation on the flight
    "7374559496036764971": (
        "Surprise passenger celebrations captured in-flight drive the highest share rates in airline TikTok.",
        "Flair crew surprising a passenger with a birthday, anniversary, or milestone celebration mid-flight. Equip crew to spot and film these moments."
    ),
    # 5. Can you reach me - trending audio with plane footage
    "7226094100649463086": (
        "Trending audio layered over simple airline footage is high-ROI content with minimal production.",
        "Flair 737 taking off, landing, or cruising with a trending audio track. Phone filmed, 10 seconds, posted same day. The simplest format that works."
    ),

    # ═══ HAWAIIAN ═══
    # 1. They're Hawaiian Airlines flight attendants - crew pride reveal
    "7344880250016304426": (
        "Crew pride reveals with trending audio and uniform showcase drive massive engagement.",
        "They're Flair Airlines flight attendants. Same format, Flair crew, Flair green uniform, crew personality on full display."
    ),
    # 2. POV: you land in Hawaii - arrival POV
    "7337060520484343086": (
        "POV arrival content at a desirable destination is simple, repeatable, and high-performing.",
        "POV: you land in Cancun. POV: you land in Montego Bay. Window footage, crew greeting, first steps off the plane. Repeat for every destination."
    ),
    # 3. First class seat content - aspirational in-flight
    "7184188693866040622": (
        "In-flight experience content that shows the actual seat and cabin generates curiosity views.",
        "Flair cabin walkthrough. Show the actual seats, legroom, window views. Honest, unfiltered, this-is-what-you-get content."
    ),
    # 4. Followers' favorite local activities in Hawaii - community content
    "7283629869215288622": (
        "Crowdsourced destination tips from followers builds community and drives saves.",
        "Ask Flair followers: what's your favorite thing to do in Cancun? Montreal? Kelowna? Turn the answers into a video. Community builds content."
    ),
    # 5. Just being honest relatable travel humor
    "7194549809770958122": (
        "Relatable travel humor with a simple caption drives shares because everyone sees themselves in it.",
        "Flair crew or passengers in a universally relatable travel moment. Boarding chaos, overhead bin struggles, landing applause. Keep it honest and funny."
    ),

    # ═══ JETBLUE ═══
    # 1. TrueBlue customer Gurnaj first to finish 25for25 promotion
    "7525503457109789982": (
        "Spotlighting real loyal customers by name creates authentic engagement and community pride.",
        "Spotlight a real frequent Flair flyer. Name them, tell their story, celebrate their loyalty. Real passengers are more compelling than any campaign."
    ),
    # 2. GeoGuessr partnership - guess destinations game
    "7462856630070267166": (
        "Interactive game content tied to destinations drives engagement and time-on-post.",
        "Flair destination guessing game. Show clips from Cancun, Montreal, Vancouver, Jamaica. Can you guess where we fly? Interactive content drives comments."
    ),
    # 3. An islander born and raised - NYC pride content
    "7483301332774898974": (
        "City pride content with a bold, short caption drives local audience engagement and shares.",
        "Edmonton born and raised. Toronto through and through. Calgary to the core. City pride content for every Flair base city."
    ),
    # 4. Gave the Gen Z employee an opportunity and he flew with it
    "7503578491149995294": (
        "Gen Z crew content with humor and personality resonates with TikTok's core audience.",
        "Give a young Flair crew member the camera for a day. Let them create in their voice. Gen Z crew content is authentic by default."
    ),
    # 5. New snacks on the snack cart - cookie reveal
    "7499588915137924383": (
        "Snack and food reveals framed with personality and hype generate surprising engagement.",
        "Flair's onboard menu or new snack options revealed with crew energy. Taste test format, crew reactions, make the small things feel exciting."
    ),

    # ═══ SOUTHWEST ═══
    # 1. Kaya the service dog's final flight - emotional passenger story
    "7197534710090812715": (
        "Deeply emotional passenger stories are the highest-performing content format in all of airline TikTok.",
        "Find the emotional Flair stories. The service dog, the veteran, the family flying together for the first time. These stories exist on every flight."
    ),
    # 2. Precious cargo - pilot's daughter on the flight
    "7345894839289957663": (
        "Crew family moments captured on camera create instant emotional connection with audiences.",
        "Flair pilot flying with their kid on board. Crew member's parent taking their first Flair flight. Family moments from inside the operation."
    ),
    # 3. RJ the greeter - enthusiastic passenger/employee personality
    "7234591331652209963": (
        "Recurring character content with a standout personality builds audience loyalty and return viewers.",
        "Find Flair's RJ. The gate agent with personality, the crew member everyone loves, the ground crew with energy. Make them a recurring character."
    ),
    # 4. Official airline of the SEC - sports partnership
    "7390364544947735838": (
        "Sports partnership content taps into massive existing fan audiences for outsized reach.",
        "Flair partnering with a Canadian sports moment. CFL, hockey, local teams. Film crew wearing jerseys, passengers heading to the game."
    ),
    # 5. Feel-good crew video - dreams come true story
    "7258336605746793771": (
        "Feel-good crew stories told with emotion and a payoff ending drive shares and saves.",
        "A Flair crew member's personal story. Why they fly, where they came from, what this job means to them. Let crew tell their own stories."
    ),

    # ═══ SPIRIT ═══
    # 1. Major new plane alert - A321neo fleet addition with crew excitement
    "7241249157699145003": (
        "New aircraft reveals with genuine crew excitement drive massive aviation audience engagement.",
        "Flair welcoming a new 737 MAX to the fleet. Crew lined up, water cannon salute, first walkthrough. Fleet pride content with real energy."
    ),
    # 2. IYKYK - Holy Airball trending audio
    "7518397990176820493": (
        "Trending audio with a cryptic caption drives curiosity views and comment engagement.",
        "Flair crew or plane footage with a trending IYKYK audio. Let the audience fill in the meaning. Cryptic content drives comments."
    ),
    # 3. God forbid we have your back - self-aware trend
    "7494272772382936366": (
        "Self-aware humor that acknowledges the brand's reputation turns criticism into content.",
        "Flair owning its reputation with humor. God forbid we fly you there on time (99% completion rate). Turn the narrative with confidence."
    ),
    # 4. Stir the pot - comment why you like flying with us
    "7536214140482882871": (
        "Engagement bait that invites the audience to defend the brand drives comments and algorithmic push.",
        "Stir the pot: comment why you fly Flair. Let loyal passengers defend the brand in the comments. The community does the marketing."
    ),
    # 5. Yellow suits us - brand color pride with aviation footage
    "7439830291289607466": (
        "Brand color and identity pride content with simple aviation footage builds brand recognition.",
        "Green suits us. Flair's green livery on the tarmac, crew in uniform, the brand color everywhere. Simple, proud, brand-building."
    ),

    # ═══ UNITED ═══
    # 1. Two peas in a plane - best friend flight attendants
    "7098397999377829162": (
        "Crew friendship content with trending audio is simple, warm, and consistently high-performing.",
        "Two Flair crew members who are best friends. Film them together on a flight, at the gate, on layover. Crew friendship is relatable content."
    ),
    # 2. Airport personal assistant app - creator review
    "7368970980401728811": (
        "Creator-filmed product reviews feel more authentic than brand-produced content.",
        "Send a Canadian travel creator through the Flair experience. Let them film it their way. Their audience trusts their lens more than Flair's."
    ),
    # 3. Where we flying besties - this or that destinations
    "7134784264482213163": (
        "Interactive this-or-that destination content drives comments and repeat views.",
        "Where are we flying, Flair fam? Cancun or Montego Bay? Montreal or Halifax? This-or-that with Flair's actual routes. Let the audience pick."
    ),
    # 4. Think portrait not landscape - luggage packing hack
    "7353736977692347694": (
        "Practical packing and travel hack content drives saves and shares because it's genuinely useful.",
        "Flair-specific packing tips. How to maximize your personal item, what fits in Flair's dimensions, real crew showing real hacks."
    ),
    # 5. Flying with Aly and AJ - celebrity on board
    "7085460538574032174": (
        "Celebrity or creator surprise moments on board create viral, shareable content.",
        "A Canadian musician, athlete, or creator spotted on a Flair flight. Crew reaction, passenger reaction. The surprise is the content."
    ),

    # ═══ WESTJET ═══
    # 1. Plenty of reasons to travel - sale promo with travel montage
    "7410478126091865349": (
        "Travel montage content with an emotional pull outperforms standard sale announcements.",
        "Why Canadians travel with Flair. Montage of real destinations, real passengers, real moments. Emotion first, the booking link can wait."
    ),
    # 2. Can't tell a Seoul - Calgary to Seoul route announcement pun
    "7312498856837778693": (
        "Route announcements with personality and wordplay make corporate news feel human.",
        "Flair's Jamaica or Montreal route announced with a pun, crew excitement, destination reveal. Make the announcement feel like a moment."
    ),
    # 3. WestJetters jump into summer - crew summer energy
    "7382618431054449926": (
        "Seasonal crew energy content marks calendar moments and builds brand warmth.",
        "Flair crew jumping into summer. First day of summer content, crew at destinations, seasonal energy. Mark the moment with crew."
    ),
    # 4. Helpful tip for the long weekend - travel tip
    "7424517539650080006": (
        "Quick, practical travel tips timed to holidays drive saves and shares.",
        "Flair crew sharing a quick travel tip before a long weekend. Practical, helpful, 15 seconds. Builds trust and saves."
    ),
    # 5. Where are you headed on your next getaway - community question
    "7161444492657118469": (
        "Simple community questions drive comments and algorithmic distribution through engagement.",
        "Where are you flying with Flair this month? Simple question, crew asking on camera. Comments drive the algorithm."
    ),

    # ═══ BRITISH AIRWAYS ═══
    # 1. We've landed on TikTok - platform debut with new uniform reveal
    "7185569523230133510": (
        "Platform debut content paired with a visual reveal creates a strong first impression.",
        "If Flair relaunches its TikTok voice, make it a moment. New energy, new look, crew front and center. A voice debut, not just another post."
    ),
    # 2. Lewis Capaldi surprise performance on board
    "7215882133456293126": (
        "Surprise celebrity moments on board create massive earned media and shares.",
        "A Canadian artist performing or appearing on a Flair flight. Doesn't need to be A-list. A local musician, a comedian, a creator. The surprise is the format."
    ),
    # 3. Charles Leclerc comparison - plane vs F1 car race
    "7481309446065425686": (
        "Playful cross-brand comparisons with trending cultural figures drive curiosity clicks.",
        "Flair 737 vs something unexpected. A race, a comparison, a playful challenge. Plane content with a twist."
    ),
    # 4. Taylor Swift Super Bowl - special on-board announcement to Las Vegas
    "7334290396400438560": (
        "Tying crew moments to live cultural events creates timely, shareable content.",
        "Flair crew making a special announcement tied to a cultural moment. Concert weekend, playoff game, holiday. Tie the flight to the event."
    ),
    # 5. New A321neo seats reveal - next-gen aircraft product
    "7369609485431688481": (
        "New seat and cabin product reveals drive aviation audience engagement and curiosity.",
        "Flair's newest cabin configuration or seat upgrade revealed by crew. Walk through it, sit in it, show the details. Product content through people."
    ),

    # ═══ EASYJET ═══
    # 1. Eurovision Song Contest 2023 partnership
    "7224592419700886810": (
        "Major event partnerships create content moments that tap into existing massive audiences.",
        "Flair partnering with a Canadian cultural event. Stampede, Caribana, Jazz Fest, a music festival. The event's audience becomes Flair's audience."
    ),
    # 2. Are we nearly there yet - crew humor in cabin
    "7096877917103328518": (
        "Simple crew humor filmed in the cabin with a relatable caption is endlessly repeatable.",
        "Flair crew doing a quick relatable moment in the cabin. Short, funny, no script needed. Are we there yet energy."
    ),
    # 3. Game changer phone hack - crew sharing a travel tip
    "7135395974809160966": (
        "Crew-filmed travel hacks feel authentic and drive massive saves and shares.",
        "Flair crew sharing a phone hack, packing tip, or airport shortcut. Crew as the expert, filmed on their phone. Authentic and useful."
    ),
    # 4. Our office > your office - crew showing their view
    "7066093435626802437": (
        "Crew POV content showing their unique workplace view is simple, repeatable, and aspirational.",
        "Flair crew showing their office view. Cockpit over the Rockies, cabin at sunrise, tarmac in winter. Our office, your next destination."
    ),
    # 5. Jane Boulton hopecore - emotional crew member spotlight
    "7462841955710455072": (
        "Emotional crew spotlights with hopecore energy generate massive engagement and loyalty.",
        "Find the Flair crew member with a moving story. Long career, second career, dream job. Let them tell it in their own words. Hopecore with substance."
    ),

    # ═══ ICELANDAIR ═══
    # 1. Is Iceland real or conspiracy - playful brand humor
    "7571117722965216534": (
        "Playful, self-aware brand humor that leans into a meme creates viral destination content.",
        "Is affordable Canadian travel real, or just the world's best-kept secret? Playful, self-aware, leaning into the disbelief that good fares exist."
    ),
    # 2. Yule Cat tastes traditional Christmas food
    "7586805425362734358": (
        "Recurring character content tied to cultural traditions builds a loyal returning audience.",
        "A recurring Flair character exploring Canadian food, culture, or traditions at each destination. Build a series audiences come back for."
    ),
    # 3. Yule Cat backstory - folklore storytelling
    "7584857090582121750": (
        "Storytelling content that educates about culture and place builds deeper destination connection.",
        "Stories from Flair destinations. Montreal bagel history, Jamaica's Blue Mountains, Kelowna wine country origins. Destination storytelling, not just footage."
    ),
    # 4. Yule Cat asks for comfort and entertainment on board
    "7585685143797484822": (
        "Character-driven content that showcases onboard features in a narrative format keeps audiences engaged.",
        "A fun character or crew member reviewing the Flair onboard experience. Seats, snacks, entertainment. Make it a personality, not a product demo."
    ),
    # 5. Is Iceland real part 2 - puffin, unreal conspiracy continues
    "7576360070628281622": (
        "Series content that extends a viral concept keeps momentum and builds franchise value.",
        "If something works, make it a series. Same format, new angle, recurring theme. Flair's version of an ongoing joke or concept that audiences follow."
    ),

    # ═══ LUFTHANSA ═══
    # 1. Weekend mode on - simple beautiful aviation footage
    "7466079142652562721": (
        "Simple, beautiful aviation footage with a mood caption drives massive passive views.",
        "Flair 737 footage. Takeoff, landing, cruising over mountains. Weekend mode on, Friday mood, holiday energy. Beautiful footage, simple caption."
    ),
    # 2. Northern Lights adventure - aurora destination content
    "7463779392527846678": (
        "Spectacular natural phenomenon tied to destination creates aspirational, save-worthy content.",
        "Northern lights from Edmonton or Yellowknife, beach sunsets from Cancun, mountain views from Kelowna. Flair flies to spectacular places."
    ),
    # 3. Phonetics: 1, Plans: 0 - humorous mispronunciation travel content
    "7570014074814188832": (
        "Relatable travel humor about mispronouncing destinations is universally shareable.",
        "Flair passengers trying to pronounce Guadalajara, or debating how to say Montreal vs Montréal. Light, funny, universally relatable."
    ),
    # 4. Traveling with a baby - family-friendly content
    "7024480652653284613": (
        "Family travel content that normalizes flying with babies drives engagement from parent audiences.",
        "Flying with a baby on Flair. Real family, real flight, crew helping out. Family travel content reaches a huge parent audience."
    ),
    # 5. Allegris new cabin product reveal (German language)
    "7569196809550187798": (
        "Premium product reveals with cinematic production create aspirational brand content.",
        "Flair's newest cabin or service improvement shown cinematically. Walk through the experience. Even budget carriers can make product content look great."
    ),

    # ═══ VIRGIN ATLANTIC ═══
    # 1. See the world differently - brand values campaign
    "7086444322589035781": (
        "Brand values content with a clear, bold message creates identity-defining moments.",
        "Flair's version of a brand values statement. Travel is for everyone. Affordable doesn't mean less. A bold, visual brand moment."
    ),
    # 2. Travel without judgement - inclusivity message
    "7156641302359084294": (
        "Inclusivity messaging delivered visually and emotionally drives shares and brand loyalty.",
        "Flair is for everyone. Show the diversity of who flies Flair. Families, students, seniors, first-time flyers. Everyone belongs."
    ),
    # 3. Good vibes only - crew in heels, runway-style walk
    "7112493700403563781": (
        "Crew confidence and style content with trending audio builds brand personality and aspiration.",
        "Flair crew walking through the airport or cabin with confidence and energy. Trending audio, crew style, good vibes. Let the crew shine."
    ),
    # 4. Everyone's a VIP - cabin crew service showcase
    "7230914909419080986": (
        "Content showing equal treatment for all passengers builds brand warmth and shareability.",
        "Everyone gets the Flair experience. Show crew treating every passenger like they matter. Affordable travel with genuine hospitality."
    ),
    # 5. Tattoo policy change - crew can show tattoos with pride
    "7103802405078240518": (
        "Progressive policy changes announced through crew create massive positive engagement.",
        "Any positive crew or company policy change announced through the people it affects. Crew telling their own story about what it means to them."
    ),

    # ═══ EMIRATES ═══
    # 1. Captain Claus - Santa themed A380 Christmas content
    "7180347155746393345": (
        "Holiday themed aviation content with cinematic production creates annual viral moments.",
        "Flair's holiday content. Crew in holiday spirit, festive cabin, Christmas flight to a sun destination. Holiday energy, crew-filmed."
    ),
    # 2. Three aircraft formation flyover at Dubai Airshow
    "7574456161609452820": (
        "Spectacular aviation footage of rare operational moments drives massive avgeek engagement.",
        "Flair's version of a rare aviation moment. First landing at a new airport, fleet lineup, special livery reveal. The operational spectacle."
    ),
    # 3. Sleigh380 - Santa's going long-haul Christmas sequel
    "7587301326392970516": (
        "Sequel holiday content that builds on a previous viral hit sustains audience engagement year over year.",
        "If a Flair holiday post works, do it again next year with a twist. Build annual traditions in content. Audiences love returning formats."
    ),
    # 4. This trend but make it First Class - surround sound trend
    "7329911500640996609": (
        "Trending audio adapted to show the in-flight experience drives curiosity and aspirational engagement.",
        "This trend but make it Flair. Trending audio with the Flair cabin, Flair crew, Flair destinations. Same trend, Flair's world."
    ),
    # 5. Valentine's Day - passion for travel in full bloom, roses + A380
    "7471202121501658386": (
        "Holiday-specific content that ties the brand to an emotion creates shareable seasonal moments.",
        "Flair's Valentine's content. Couples traveling together, crew spreading love, romantic destinations. Tie the holiday to the travel emotion."
    ),

    # ═══ ETIHAD ═══
    # 1. I do - engagement/wedding themed content on plane
    "7102317808951856385": (
        "Life milestone content filmed on board creates deeply emotional, highly shareable moments.",
        "Flair passengers celebrating life milestones on board. Engagement, honeymoon trip, anniversary flight. Ask crew to spot and capture these."
    ),
    # 2. Welcome on board A321LR - crew greeting every passenger with flat beds
    "7590703357002550546": (
        "Crew greeting passengers warmly and personally creates aspirational hospitality content.",
        "Flair crew welcoming passengers on board. Every hello, every smile, every greeting. The warmth of Flair's crew is the content."
    ),
    # 3. Welcome on board - same crew greeting format, different video
    "7301945584569617665": (
        "Repeating a successful format with slight variation compounds audience and views.",
        "If the crew welcome video works, do it again from a different flight, different crew, different city. Same format, fresh content."
    ),
    # 4. Europe awaits - summer travel aspiration content
    "7386678652471151890": (
        "Seasonal aspiration content tied to a destination region drives saves and shares.",
        "Mexico awaits. The Caribbean is calling. Summer in BC. Flair's version of seasonal destination aspiration, tied to real routes."
    ),
    # 5. With a croissant - simple Paris lifestyle moment
    "7099772491698048257": (
        "Simple destination lifestyle moments with minimal caption drive massive views through mood and aesthetic.",
        "With a taco in Cancun. With a smoked meat sandwich in Montreal. Simple, beautiful destination moments. One line, one vibe."
    ),

    # ═══ QATAR ═══
    # 1. FIFA World Cup song
    "7166954065258138882": (
        "Official event soundtrack content taps into massive existing fan audiences.",
        "Flair content tied to a major Canadian sporting or music event. The energy of the event, crew celebrating, passengers heading there."
    ),
    # 2. Check - satisfying aviation pre-flight checklist
    "7461654490601557266": (
        "Satisfying aviation checklist content appeals to avgeeks and casual viewers alike.",
        "Flair pre-flight check. Cockpit prep, walk-around, systems check. Satisfying, methodical, trust-building aviation content."
    ),
    # 3. Tag your aviation friends - trivia question
    "7210313039365623042": (
        "Aviation trivia that invites tagging drives comments, shares, and algorithmic push.",
        "Flair aviation trivia. How fast does a 737 fly? How cold is it at cruising altitude? Tag a friend who would know. Engagement-first content."
    ),
    # 4. Champions League partnership announcement
    "7416326390586395922": (
        "Sports partnership content creates crossover audience reach beyond the airline's usual followers.",
        "Flair connected to a Canadian sports partnership. Local hockey team, CFL, university athletics. The sports audience discovers Flair."
    ),
    # 5. Of course we're award-winning cabin crew - ofcourse trend
    "7334675529288781074": (
        "Trending audio used to flex genuine brand achievements creates confident, shareable content.",
        "Of course Flair has 99% completion rate. Of course we're the most on-time airline in Canada. Trending audio + real flex."
    ),

    # ═══ FLYADEAL ═══
    # 1. Cairo destination showcase - diverse activities
    "7420004220704722182": (
        "Destination showcase with diverse activity highlights drives travel planning saves.",
        "Flair's version for Cancun, Jamaica, or Guadalajara. Show the range of what you can do there. Culture, food, nightlife, nature."
    ),
    # 2. Winter magic - seasonal travel content
    "7438234924685004088": (
        "Seasonal escape content drives saves from audiences dreaming of warmer destinations.",
        "Canadian winter outside, Cancun beach on the other end. The contrast between home and destination is Flair's content advantage."
    ),
    # 3. Nile boats and sunset - specific destination activity content
    "7391903032302177542": (
        "Specific activity content at a destination is more engaging than generic scenery.",
        "Snorkeling in Montego Bay, street food in Mexico City, wine tasting in Kelowna. Specific activities, not just skyline shots."
    ),
    # 4. Abha outdoor adventures - adventure destination content
    "7413289630167993605": (
        "Adventure and outdoor activity content at destinations drives saves from active travelers.",
        "Adventure content at Flair destinations. Hiking, water sports, exploring. Show what active travelers can do when they land."
    ),
    # 5. Summer is calling - multi-destination summer montage
    "7504277688681631031": (
        "Multi-destination summer montage content builds excitement across the whole network.",
        "Summer across Flair's network. Quick cuts between Vancouver, Montreal, Cancun, Jamaica, Kelowna. Every destination in 15 seconds."
    ),

    # ═══ CATHAY PACIFIC ═══
    # 1. Reminder you can breathe - calming cloud footage (158M views)
    "7472670745756224790": (
        "Ultra-simple calming aviation footage with a mindful caption drives massive passive views.",
        "Flair's calming content. Cloud footage from 35,000 feet, engine hum, window views. Peaceful, no sell, just the beauty of flying."
    ),
    # 2. Turbines = our kind of dopamine - engine close-up
    "7438554374894325024": (
        "Engine and aviation detail content satisfies the avgeek audience and drives saves.",
        "Flair's 737 engine spool-up, thrust reverser, or wing flex. Aviation detail content for the built-in avgeek audience."
    ),
    # 3. What's your favorite part about pre-takeoff - question + footage
    "7433776245852163361": (
        "Simple question captions over aviation footage drive comments and repeat engagement.",
        "What's your favorite part of flying? Window or aisle? Takeoff or landing? Simple question, beautiful footage, let the comments roll."
    ),
    # 4. Chasing views from 35,000 feet - window footage
    "7417036373405732128": (
        "Window view content from altitude is endlessly repeatable and universally appealing.",
        "Views from a Flair window seat. Rockies, prairies, coastline, city lights at night. Different route, same format, every week."
    ),
    # 5. Tag that bestie who chooses passport stamps over candles
    "7429344363618012449": (
        "Tag-a-friend content with a travel personality hook drives shares and comments.",
        "Tag a friend who would rather fly somewhere than get a gift. Travel personality content that invites sharing."
    ),

    # ═══ FLY AIRASIA ═══
    # 1. Baggage dimension education - don't be like this brother
    "7401077880010165522": (
        "Humorous baggage education content solves a real pain point while entertaining.",
        "Flair's baggage dimensions explained with humor. Don't be this person at the gate. Crew demonstrating what fits and what doesn't."
    ),
    # 2. They see us rollin - fleet/sale content with trending audio
    "7338259381420674306": (
        "Fleet footage with trending audio and a sale overlay reaches beyond the usual audience.",
        "Flair fleet on the tarmac with trending audio. They see us rollin energy. Fleet pride, crew confidence, brand personality."
    ),
    # 3. TICK-TOCK music video - branded artist collaboration
    "7484231343489027333": (
        "Brand-produced music content with an artist creates entertainment-first branded content.",
        "Flair collaborating with a Canadian artist on content. Music video on the plane, performance at the gate. Entertainment first, brand second."
    ),
    # 4. Hijab now official crew uniform - inclusive policy announcement
    "7580303742596041991": (
        "Inclusive uniform or policy changes announced through crew create massive positive engagement.",
        "Any Flair policy that celebrates crew individuality or inclusivity, announced by the crew it impacts. Let them tell their own story."
    ),
    # 5. Dance challenge with MimiFly creator
    "7486844728038804741": (
        "Dance challenge content with a creator at the brand's location drives fun, shareable content.",
        "Flair crew doing a dance challenge at the gate, on the tarmac, or in the cabin with a Canadian creator. Fun, shareable, personality-first."
    ),

    # ═══ SCOOT ═══
    # 1. Singapore Superfan Riz - fan contest winner content
    "7350493400547822866": (
        "Fan contest winner content that shows the fan's journey creates compelling, earned storytelling.",
        "Find Flair's biggest fan. Run a contest, feature the winner, let them experience something special. Fan-driven content is the most authentic."
    ),
    # 2. Join Singapore Superfans - contest call to action
    "7340848206013566226": (
        "UGC contest calls-to-action build community when the ask is fun and specific.",
        "Launch a #FlyFlair fan contest. Why do you love flying Flair? Best video wins a trip. Let the community create the content."
    ),
    # 3. Here's to more moments - new Embraer planes reveal
    "7342832613087825160": (
        "Year-in-review or forward-looking fleet content builds excitement about the brand's future.",
        "Flair's fleet growth story. New 737 MAXs arriving, routes expanding, the airline growing. Here's to what's next."
    ),
    # 4. Singapore top of your bucket list - destination aspiration CTA
    "7339013520266251528": (
        "Destination bucket list content with a call-to-action drives both engagement and conversion intent.",
        "Is Jamaica on your bucket list? Is Mexico City? Bucket list destination content tied to Flair's routes. Aspiration meets accessibility."
    ),
    # 5. Searching for the superest superfans - series continuation
    "7339400127972379911": (
        "Multi-part campaign content builds anticipation and keeps audiences returning for updates.",
        "If a Flair fan campaign gets traction, extend it. Part 2, part 3, the reveal. Multi-part content builds returning viewers."
    ),

    # ═══ SINGAPORE AIRLINES ═══
    # 1. Now that we've said hello, can we get a follow - TikTok debut
    "7481570187787947271": (
        "Confident, personality-forward TikTok debuts set the tone for everything that follows.",
        "If Flair relaunches its TikTok voice, lead with confidence. A crew-led hello, a bold ask for the follow. Set the tone from post one."
    ),
    # 2. Our experiences make us who we are - brand film
    "7291492084085689601": (
        "Short brand films that focus on the human experience of travel create emotional brand moments.",
        "Short film showing what travel means to Flair passengers. The first trip, the reunion, the adventure. Emotion over information."
    ),
    # 3. Inside Out partnership - core memories from first trip
    "7392882456329735442": (
        "Pop culture partnership content tied to a universal emotion drives shares across audiences.",
        "What core memories did you make on a Flair flight? Tie content to a cultural moment or universal emotion. Let passengers share their stories."
    ),
    # 4. Join our fan club and hit follow - community building CTA
    "7578796173536890130": (
        "Direct community building CTAs with crew energy convert viewers into followers.",
        "Flair crew asking for the follow. Direct, confident, crew-led. Build the community one ask at a time."
    ),
    # 5. World's Best Airline Skytrax award announcement
    "7249281700671327506": (
        "Award and recognition content validates brand quality and drives pride shares.",
        "Flair's operational achievements announced with crew pride. Best on-time in Canada, 99% completion. Let the crew celebrate the wins."
    ),

    # ═══ LATAM ═══
    # 1. Athletes' dreams - Olympics/sports emotional content
    "7284292321703775494": (
        "Emotional sports content that ties the airline to athletes' journeys drives massive reach.",
        "Flair flying Canadian athletes, teams, or sports fans to events. The journey to the game, the flight home after a win."
    ),
    # 2. Father's Day - special crew of dads flying together
    "7516190997265648952": (
        "Holiday content featuring crew families creates deep emotional connection.",
        "Father's Day, Mother's Day, Family Day on Flair. Crew who are parents, passengers traveling with family. Holiday emotion through real people."
    ),
    # 3. Sustainability content - most sustainable airline in LatAm
    "7397824209423994117": (
        "Sustainability claims backed by visual storytelling create credibility and shareability.",
        "Flair's sustainability story. Newest fleet in Canada means lower emissions. Tell it visually, not as a press release."
    ),
    # 4. Conservation and rare bird content - environmental storytelling
    "7301704541978840326": (
        "Environmental storytelling tied to destinations creates unique, save-worthy content.",
        "Wildlife and nature at Flair destinations. Jamaica's Blue Mountains, BC's old-growth forests, Mexican wildlife. Conservation meets travel."
    ),
    # 5. Mother's Day flowers - LATAM Cargo flying 600M stems from Colombia
    "7503187633179217207": (
        "Behind-the-scenes cargo and operations storytelling reveals the invisible side of air travel.",
        "What else flies on a Flair 737? The cargo story, the operations story, the invisible side of keeping flights running. Behind-the-scenes with substance."
    ),

    # ═══ SKY AIRLINE ═══
    # 1. SKY Plus loyalty program - why it's so good
    "7545129269437992248": (
        "Loyalty program content framed as a lifestyle rather than a feature list drives engagement.",
        "If Flair has loyalty perks, show them in action. A passenger using their benefits, crew recognizing a frequent flyer. Lifestyle, not features."
    ),
    # 2. Grab your wings - newest fleet in Americas, aspirational travel
    "7156950473130511622": (
        "Aspirational fleet pride content positions the airline as modern and forward-looking.",
        "Flair's newest fleet in Canada content. The planes are new, the experience is fresh. Show it with energy and pride."
    ),
    # 3. SKY Plus registration CTA - loyalty sign-up
    "7358851210712993030": (
        "Loyalty program CTAs work when they feel like an invitation, not an ad.",
        "Invite passengers into the Flair community. Not a signup form, but a crew member explaining why they love seeing regulars."
    ),
    # 4. Pack your bag - adventure montage across destinations
    "7065694478740262150": (
        "Adventure travel montage content with energetic pacing drives excitement and saves.",
        "Pack your bag and fly Flair. Quick-cut adventure montage across Cancun, Jamaica, Vancouver, Montreal. Energy, movement, excitement."
    ),
    # 5. Miami! We've arrived - new destination excitement
    "7106919788806540549": (
        "New destination arrival content with genuine excitement creates shareable celebration moments.",
        "Flair touches down in a new city. Jamaica! Montreal is back! Crew celebrating, first passengers, the energy of a new route. Capture the moment."
    ),
}

# Apply all versions
updated = 0
for a in data["airlines"]:
    for o in a["outliers"]:
        if o["id"] in VERSIONS:
            insight, flair = VERSIONS[o["id"]]
            o["flairTakeaway"] = f"{insight} Flair's version: {flair}"
            updated += 1

print(f"Updated {updated} of 125 outliers")

# Check for any we missed
missed = 0
for a in data["airlines"]:
    for o in a["outliers"]:
        if o["id"] not in VERSIONS:
            print(f"MISSED: {a['name']} - {o['id']} - {o['text'][:60]}")
            missed += 1
print(f"\n{missed} missed")

with open("/Users/nora/Flair WhiteSpace/flair-tiktok-outliers.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

