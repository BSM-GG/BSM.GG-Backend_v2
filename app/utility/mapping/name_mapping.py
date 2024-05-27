QUEUE_TYPE = {
    400: "일반",
    420: "솔로랭크",
    430: "일반",
    440: "자유랭크",
    450: "칼바람",
    490: "빠른대전",
    700: "격전",
    800: "AI대전",
    810: "AI대전",
    820: "AI대전",
    830: "AI대전",
    840: "AI대전",
    850: "AI대전",
    900: "URF",
    920: "포로왕",
    1020: "단일모드",
    1300: "돌격 넥서스",
    1400: "궁극기 주문서",
    1700: "아레나",
    2000: "튜토리얼",
    2010: "튜토리얼",
    2020: "튜토리얼",
}

TIER = {
    "CHALLENGER I":   2800,
    "GRAND MASTER I": 2800,
    "MASTER I":       2800,
    "DIAMOND I":      2700,
    "DIAMOND II":     2600,
    "DIAMOND III":    2500,
    "DIAMOND IV":     2400,
    "EMERALD I":      2300,
    "EMERALD II":     2200,
    "EMERALD III":    2100,
    "EMERALD IV":     2000,
    "PLATINUM I":     1900,
    "PLATINUM II":    1800,
    "PLATINUM III":   1700,
    "PLATINUM IV":    1600,
    "GOLD I":         1500,
    "GOLD II":        1400,
    "GOLD III":       1300,
    "GOLD IV":        1200,
    "SILVER I":       1100,
    "SILVER II":      1000,
    "SILVER III":      900,
    "SILVER IV":       800,
    "BRONZE I":        700,
    "BRONZE II":       600,
    "BRONZE III":      500,
    "BRONZE IV":       400,
    "IRON I":          300,
    "IRON II":         200,
    "IRON III":        100,
    "IRON IV":           0,
}

SPELL_NAME = {
    1: "SummonerBoost",
    3: "SummonerExhaust",
    4: "SummonerFlash",
    6: "SummonerHaste",
    7: "SummonerHeal",
    11: "SummonerSmite",
    12: "SummonerTeleport",
    13: "SummonerMana",
    14: "SummonerDot",
    21: "SummonerBarrier",
    30: "SummonerPoroRecall",
    31: "SummonerPoroThrow",
    32: "SummonerSnowball",
    39: "SummonerSnowURFSnowball_Mark",
    54: "Summoner_UltBookPlaceholder",
    55: "Summoner_UltBookSmitePlaceholder``",
    2201: "SummonerCherryHold",
    2202: "SummonerCherryFlash",
}

TEAM = {
    0: "BLUE",
    1: "RED",
}

PERKS = [
    {
        "id": 8369,
        "name": "First Strike",
        "majorChangePatchVersion": "11.23",
        "tooltip": "Attacks or abilities against an enemy champion within @GraceWindow.2@s of entering champion combat grants @GoldProcBonus@ gold and <b>First Strike</b> for @Duration@ seconds, causing you to deal <truedamage>@DamageAmp*100@%</truedamage> extra <truedamage>damage</truedamage> against champions, and granting <gold>{{ Item_Melee_Ranged_Split }}</gold> of that damage dealt as <gold>gold</gold>.<br><br>Cooldown: <scaleLevel>@Cooldown@</scaleLevel>s<br><hr><br>Damage Dealt: @f1@<br>Gold Gained: @f2@",
        "shortDesc": "When you initiate champion combat, deal 7% extra damage for 3 seconds and gain gold based on damage dealt.",
        "longDesc": "Attacks or abilities against an enemy champion within 0.25s of entering champion combat grants 5 gold and <b>First Strike</b> for 3 seconds, causing you to deal <truedamage>7%</truedamage> extra <truedamage> damage</truedamage> against champions, and granting <gold>100% (70% for ranged champions)</gold> of bonus damage dealt as <gold>gold</gold>.<br><br>Cooldown: <scaleLevel>25 - 15</scaleLevel>s",
        "recommendationDescriptor": "True Damage, Income",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/FirstStrike/FirstStrike.png",
        "endOfGameStatDescs": [
            "Damage Dealt: @eogvar1@",
            "Gold Gained: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8446,
        "name": "Demolish",
        "majorChangePatchVersion": "",
        "tooltip": "Charge up a powerful attack against a tower over 3s, while within 600 range of it. The charged attack deals <scaleAD>@f6@</scaleAD> bonus physical damage. <br><hr><br>Cooldown remaining: @f2@<br>Total bonus damage: <scaleAD>@f1@</scaleAD><br>Current Damage: 100 + 35% of your max health",
        "shortDesc": "Charge up a powerful attack against a tower while near it.",
        "longDesc": "Charge up a powerful attack against a tower over 3s, while within 600 range of it. The charged attack deals 100 (+35% of your max health) bonus physical damage. <br><br>Cooldown: 45s",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/Demolish/Demolish.png",
        "endOfGameStatDescs": [
            "Total Bonus Damage: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kUtility": 10
        }
    },
    {
        "id": 8126,
        "name": "Cheap Shot",
        "majorChangePatchVersion": "9.9",
        "tooltip": "Damaging champions with <b>impaired movement or actions</b> deals 10 - 45 bonus true damage (based on level).<br><br>Cooldown: 4s<br><rules>Activates on damage occurring after the impairment.</rules><br><hr><br>Current Damage: @f2@<br>Total bonus damage dealt: @f1@",
        "shortDesc": "Deal bonus true damage to enemy champions with <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_ImpairAct'>impaired movement or actions</lol-uikit-tooltipped-keyword>. ",
        "longDesc": "Damaging champions with <b>impaired movement or actions</b> deals 10 - 45 bonus true damage (based on level).<br><br>Cooldown: 4s<br><rules>Activates on damage occurring after the impairment.</rules>",
        "recommendationDescriptor": "Earned by winning ranked games in Season 2020 - Split 1.",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/CheapShot/CheapShot.png",
        "endOfGameStatDescs": [
            "Total damage: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kBurstDamage": 5,
            "kDamagePerSecond": 5
        }
    },
    {
        "id": 8321,
        "name": "Future's Market",
        "majorChangePatchVersion": "",
        "tooltip": "You can enter debt to buy items. The amount you can borrow increases over time. If you enter debt, you will be charged a lending fee of <attention>50</attention> gold.<br><br>Debt limit: <attention>Available at 2 minutes</attention><br>Future Purchases: <attention>@f3@</attention>",
        "shortDesc": "You can enter debt to buy items.",
        "longDesc": "You can enter debt to buy items. The amount you can borrow increases over time. If you enter debt, you will be charged a lending fee of <attention>50</attention> gold.<br>Debt limit: 100 + 8/min<br>(Debt doesn't become available until 2 minutes)",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/FuturesMarket/FuturesMarket.png",
        "endOfGameStatDescs": [
            "Future Purchases: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kGold": 15
        }
    },
    {
        "id": 8415,
        "name": "The Arcane Colossus",
        "majorChangePatchVersion": "",
        "tooltip": "<pathResolve>Resolve</pathResolve> + <pathSorcery>Sorcery</pathSorcery> <br>+0-0 Health based on level<br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD>",
        "shortDesc": "<pathBonus><pathResolve>Resolve</pathResolve> + <pathSorcery>Sorcery</pathSorcery> Set Bonus</pathBonus>",
        "longDesc": "+0-0 Health based on level<br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8410,
        "name": "Approach Velocity",
        "majorChangePatchVersion": "",
        "tooltip": "Gain <speed>7.5% Move Speed</speed> towards nearby enemy champions that are movement impaired. This bonus is increased to <speed>15% Move Speed</speed> for any enemy champion that you impair. <br><br>Activation Range for CC from allies: 1000<br><hr><br>Time Spent Hasted: @f1@s",
        "shortDesc": "Bonus <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_MS'>MS</lol-uikit-tooltipped-keyword> towards nearby enemy champions that are <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_ImpairMov'>movement impaired</lol-uikit-tooltipped-keyword>, increased for enemy champions that you impair.",
        "longDesc": "Gain <speed>7.5% Move Speed</speed> towards nearby enemy champions that are movement impaired. This bonus is increased to <speed>15% Move Speed</speed> for any enemy champion that you impair. <br><br>Activation Range for CC from allies: 1000",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/ApproachVelocity/ApproachVelocity.png",
        "endOfGameStatDescs": [
            "Time Spent Hasted: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kMoveSpeed": 10
        }
    },
    {
        "id": 8232,
        "name": "Waterwalking",
        "majorChangePatchVersion": "",
        "tooltip": "Gain <speed>10 Move Speed</speed> and an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of up to 18 Attack Damage or 30 Ability Power (based on level) when in the river.",
        "shortDesc": "Gain <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_MS'>MS</lol-uikit-tooltipped-keyword> and AP or AD, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'>adaptive</lol-uikit-tooltipped-keyword> in the river.",
        "longDesc": "Gain <speed>10 Move Speed</speed> and an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of up to 18 Attack Damage or 30 Ability Power (based on level) when in the river.<br><br><hr><br><i>May you be as swift as the rushing river and agile as a startled Rift Scuttler.</i><br>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/Waterwalking/Waterwalking.png",
        "endOfGameStatDescs": [
            "Total time active: @eogvar1@:@eogvar2@"
        ],
        "recommendationDescriptorAttributes": {
            "kBurstDamage": 2,
            "kDamagePerSecond": 2,
            "kMoveSpeed": 6
        }
    },
    {
        "id": 8299,
        "name": "Last Stand",
        "majorChangePatchVersion": "",
        "tooltip": "Deal 5% - 11% increased damage to champions while you are below 60% health. Max damage gained at 30% health.<br><br><rules>Minimum bonus is 5%.<br>Maximum bonus is granted while below 30% health.</rules><br><hr><br>Total bonus damage: <scaleAD>@f1@</scaleAD>",
        "shortDesc": "Deal more damage to champions while you are low on health.",
        "longDesc": "Deal 5% - 11% increased damage to champions while you are below 60% health. Max damage gained at 30% health.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/LastStand/LastStand.png",
        "endOfGameStatDescs": [
            "Total Bonus Damage: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kBurstDamage": 1,
            "kDamagePerSecond": 9
        }
    },
    {
        "id": 8112,
        "name": "Electrocute",
        "majorChangePatchVersion": "",
        "tooltip": "Hitting a champion with 3 <b>separate</b> attacks or abilities within 3s deals bonus <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'><font color='#48C4B7'>adaptive damage</font></lol-uikit-tooltipped-keyword>.<br>Cooldown: 25 - 20s<br><hr><br>Current damage: @f2@ (<scaleAP>+@f3@</scaleAP>) (<scaleAD>+@f4@</scaleAD>)<br>Total Damage Dealt: <scaleAD>@f1@</scaleAD>",
        "shortDesc": "Hitting a champion with 3 <b>separate</b> attacks or abilities in 3s deals bonus <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'>adaptive damage</lol-uikit-tooltipped-keyword>.",
        "longDesc": "Hitting a champion with 3 <b>separate</b> attacks or abilities within 3s deals bonus <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'><font color='#48C4B7'>adaptive damage</font></lol-uikit-tooltipped-keyword>.<br><br>Damage: 30 - 220 (+0.1 bonus AD, +0.05 AP) damage.<br><br>Cooldown: 25 - 20s<br><br><hr><i>'We called them the Thunderlords, for to speak of their lightning was to invite disaster.'</i>",
        "recommendationDescriptor": "Combo Damage",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/Electrocute/Electrocute.png",
        "endOfGameStatDescs": [
            "Total Damage Dealt: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8234,
        "name": "Celerity",
        "majorChangePatchVersion": "9.9",
        "tooltip": "All movement bonuses are 7% more effective on you and gain <speed>1% Move Speed</speed>.<br><br>Currently Granted: <speed>@f1@ Move Speed</speed><br>Extra Distance Traveled: @f2@",
        "shortDesc": "All <speed>Move Speed</speed> bonuses are 7% more effective on you and gain <speed>1% Move Speed</speed>.",
        "longDesc": "All movement bonuses are 7% more effective on you and gain <speed>1% Move Speed</speed>.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/Celerity/CelerityTemp.png",
        "endOfGameStatDescs": [
            "Extra Distance Travelled: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kMoveSpeed": 10
        }
    },
    {
        "id": 8453,
        "name": "Revitalize",
        "majorChangePatchVersion": "",
        "tooltip": "Gain 5% Heal and Shield Power.<br><br>Heals and shields you cast or receive are 10% stronger on targets below 40% health.<br><hr><br><scaleAD>Bonus healing</scaleAD>: @f1@<br><scaleAD>Bonus shielding</scaleAD>: @f2@<br><scaleAD>Total Heal and Shield power</scaleAD>: @f4@%",
        "shortDesc": "Gain 5% Heal and Shield Power.<br><br>Heals and shields you cast or receive are 10% stronger on targets below 40% health.",
        "longDesc": "Gain 5% Heal and Shield Power.<br><br>Heals and shields you cast or receive are 10% stronger on targets below 40% health.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/Revitalize/Revitalize.png",
        "endOfGameStatDescs": [
            "Bonus Healing: @eogvar1@",
            "Bonus Shielding: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {
            "kHealing": 10
        }
    },
    {
        "id": 8360,
        "name": "Unsealed Spellbook",
        "majorChangePatchVersion": "8.9",
        "tooltip": "Swap one of your equipped Summoner Spells to a new, single use Summoner Spell. Each unique Summoner Spell you swap to permanently decreases your swap cooldown by 25s (initial swap cooldown is at 5 mins). <br><br>Your first swap becomes available at 6 mins. <br><rules><br>Summoner Spells can only be swapped while out of combat. <br>After using a swapped Summoner Spell you must swap 3 more times before the first can be selected again.<br>Smite damage increases after two Summoner Spell swaps. </rules><hr><br>Unique Summoner Spells Used: @f4@/@f8@<br>Current Swap Cooldown: @f3@ seconds",
        "shortDesc": "Swap Summoner Spells while out of combat. Swapping to unique Summoner Spells will increase the rate at which you can make future swaps.",
        "longDesc": "Swap one of your equipped Summoner Spells to a new, single use Summoner Spell. Each unique Summoner Spell you swap to permanently decreases your swap cooldown by 25s (initial swap cooldown is at 5 mins). <br><br>Your first swap becomes available at 6 mins. <br><rules><br>Summoner Spells can only be swapped while out of combat. <br>After using a swapped Summoner Spell you must swap 3 more times before the first can be selected again.<br>Smite damage increases after two Summoner Spell swaps. </rules>",
        "recommendationDescriptor": "Cast more Summoners",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/UnsealedSpellbook/UnsealedSpellbook.png",
        "endOfGameStatDescs": [
            "Summoner Spells swapped: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8004,
        "name": "The Brazen Perfect",
        "majorChangePatchVersion": "",
        "tooltip": "<pathPrecision>Precision</pathPrecision> + <pathSorcery>Sorcery</pathSorcery><br>+0% Attack Speed<br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD>",
        "shortDesc": "<pathBonus><pathPrecision>Precision</pathPrecision> + <pathSorcery>Sorcery</pathSorcery> Set Bonus</pathBonus>",
        "longDesc": "+0% Attack Speed<br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8128,
        "name": "Dark Harvest",
        "majorChangePatchVersion": "8.23",
        "tooltip": "Damaging a champion below 50% health deals <scaleAD>@f8@ physical damage</scaleAD> and harvests their soul, permanently increasing Dark Harvest's damage by <font color='#fc314e'>@f12@</font>.<br><br>Cooldown: 45s (resets to 1.5s on takedown)<br><hr><br>Souls harvested: <font color='#fc314e'>@f5@</font><br>Current damage: <scaleLevel>@f7@</scaleLevel> <font color='#fc314e'>(+@f6@)</font> <scaleAD>(+@f10@)</scaleAD> <scaleAP>(+@f11@)</scaleAP> <br>Total damage dealt: @f9@",
        "shortDesc": "Damaging a low health champion inflicts <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'>adaptive damage</lol-uikit-tooltipped-keyword> and harvests a soul from the victim.",
        "longDesc": "Damaging a Champion below 50% health deals <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'>adaptive damage</lol-uikit-tooltipped-keyword> and harvests their soul, permanently increasing Dark Harvest's damage by 5.<br><br>Dark Harvest damage: 20-80 (based on level) (+5 damage per soul) (+0.1 bonus AD) (+0.05 AP)<br>Cooldown: 45s (resets to 1.5s on takedown)",
        "recommendationDescriptor": "Execute Enemies",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/DarkHarvest/DarkHarvest.png",
        "endOfGameStatDescs": [
            "Total Damage Dealt: @eogvar1@",
            "Total Souls Harvested: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8220,
        "name": "The Calamity",
        "majorChangePatchVersion": "",
        "tooltip": "<pathSorcery>Sorcery</pathSorcery> + <pathDomination>Domination</pathDomination><br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD>",
        "shortDesc": "<pathBonus><pathSorcery>Sorcery</pathSorcery> + <pathDomination>Domination</pathDomination> Set Bonus</pathBonus>",
        "longDesc": "+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8016,
        "name": "The Merciless Elite",
        "majorChangePatchVersion": "",
        "tooltip": "<pathPrecision>Precision</pathPrecision> + <pathDomination>Domination</pathDomination><br>+0% Attack Speed<br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD>",
        "shortDesc": "<pathBonus><pathPrecision>Precision</pathPrecision> + <pathDomination>Domination</pathDomination> Set Bonus</pathBonus>",
        "longDesc": "+0% Attack Speed<br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8473,
        "name": "Bone Plating",
        "majorChangePatchVersion": "9.9",
        "tooltip": "After taking damage from an enemy champion, the next 3 spells or attacks you receive from them deal <scaleLevel>@f2@</scaleLevel> less damage.<br><br>Duration: 1.5s<br>Cooldown: 55s<br><hr><br>Total Damage Reduced: <scaleLevel>@f1@</scaleLevel>",
        "shortDesc": "After taking damage from an enemy champion, the next 3 spells or attacks you receive from them deal 30-60 less damage.<br><br><br>Duration: 1.5s<br>Cooldown: 55s",
        "longDesc": "After taking damage from an enemy champion, the next 3 spells or attacks you receive from them deal 30-60 less damage.<br><br><br>Duration: 1.5s<br>Cooldown: 55s",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/BonePlating/BonePlating.png",
        "endOfGameStatDescs": [
            "Total Damage Blocked: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kDurability": 10
        }
    },
    {
        "id": 8339,
        "name": "Celestial Body",
        "majorChangePatchVersion": "",
        "tooltip": "+100 Health permanently<br>-10% damage to champions and monsters until 10 min",
        "shortDesc": "+100 Health permanently<br>-10% damage to champions and monsters until 10 min",
        "longDesc": "+100 Health permanently<br>-10% damage to champions and monsters until 10 min<br><br><hr><br><i>'The greatest legends live on in the stars.' <br>—Daphna the Dreamer</i>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/CelestialBody/CelestialBody.png",
        "endOfGameStatDescs": [
            "--"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8214,
        "name": "Summon Aery",
        "majorChangePatchVersion": "",
        "tooltip": "Damaging enemy champions with basic attacks or abilities sends Aery to them, dealing <font color='#FFFFFF'>@f5@</font> (+<scaleAP>@f6@</scaleAP>) (+<scaleAD>@f7@</scaleAD>).<br><br>Empower or protecting allies with abilities sends Aery to them, shielding them for <font color='#FFFFFF'>@f8@</font> (+<scaleAP>@f9@</scaleAP>) (+<scaleAD>@f10@</scaleAD>).<br><br>Aery cannot be sent out again until she returns to you.<br><br><hr><br>Aery has attacked enemies <font color='#FFFFFF'>@f1@</font> times for a total of <font color='#FFFFFF'>@f3@</font> damage.<br>Aery has helped allies <font color='#FFFFFF'>@f2@</font> times, shielding a total of <font color='#FFFFFF'>@f4@</font> damage.",
        "shortDesc": "Your attacks and abilities send Aery to a target, damaging enemies or shielding allies.",
        "longDesc": "Damaging enemy champions with basic attacks or abilities sends Aery to them, dealing 10 - 50 based on level (+<scaleAP>0.05 AP</scaleAP>) (+<scaleAD>0.1 bonus AD</scaleAD>).<br><br>Empower or protecting allies with abilities sends Aery to them, shielding them for 30 - 100 based on level (+<scaleAP>0.05 AP</scaleAP>) (+<scaleAD>0.1 bonus AD</scaleAD>).<br><br>Aery cannot be sent out again until she returns to you.",
        "recommendationDescriptor": "Poke Damage",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/SummonAery/SummonAery.png",
        "endOfGameStatDescs": [
            "Damage Dealt: @eogvar1@",
            "Damage Shielded: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8237,
        "name": "Scorch",
        "majorChangePatchVersion": "9.9",
        "tooltip": "Your next damaging ability hit sets champions on fire dealing 20 - 40 bonus magic damage based on level after 1s.<br><br>Cooldown: 10s<br><hr><br>Current Damage: @f2@<br>Total Damage Dealt: @f1@",
        "shortDesc": "Your first damaging ability hit every 10s burns champions.",
        "longDesc": "Your next damaging ability hit sets champions on fire dealing 20 - 40 bonus magic damage based on level after 1s.<br><br>Cooldown: 10s",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/Scorch/Scorch.png",
        "endOfGameStatDescs": [
            "Total Bonus Damage: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kBurstDamage": 7,
            "kDamagePerSecond": 3
        }
    },
    {
        "id": 8139,
        "name": "Taste of Blood",
        "majorChangePatchVersion": "",
        "tooltip": "Heal when you damage an enemy champion.<br><br>Healing: <font color='#ffffff'>@f2@</font> (+<scaleAD>@f3@</scaleAD>) (+<scaleAP>@f4@</scaleAP>)<br><br>Cooldown: 20s<br><hr><br>Total Healing: @f1@",
        "shortDesc": "Heal when you damage an enemy champion.",
        "longDesc": "Heal when you damage an enemy champion.<br><br>Healing: 16-40 (+0.1 bonus AD, +0.05 AP) health (based on level)<br><br>Cooldown: 20s",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/TasteOfBlood/GreenTerror_TasteOfBlood.png",
        "endOfGameStatDescs": [
            "Total Healing: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kHealing": 10
        }
    },
    {
        "id": 8008,
        "name": "Lethal Tempo",
        "majorChangePatchVersion": "",
        "tooltip": "Gain %i:scaleAS% (%i:meleeActive% @ASMelee@ || %i:rangedActive% @ASRanged@) Attack Speed for 6 seconds when you attack an enemy champion. This effect stacks up to 6 times.<br><br>While this effect is fully stacked, your Attack Speed can exceed 2.5 and you also gain 50 Attack Range.<br><hr><br>Capstone Uptime: @f1@s",
        "shortDesc": "Gain Attack Speed when attacking an enemy champion, stacking up to 6 times. At max stacks, gain Attack Range and remove your Attack Speed limit.",
        "longDesc": "Gain [30% - 96%] (Melee) or [21% - 48%] (Ranged) Attack Speed for 6 seconds when you attack an enemy champion. This effect stacks up to 6 times.<br><br>While this effect fully stacked, your Attack Speed can exceed 2.5 and you gain 50 Attack Range.",
        "recommendationDescriptor": "Ramping Attack Speed",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png",
        "endOfGameStatDescs": [
            "Max Attack Speed Uptime: @eogvar1@:@eogvar2@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 9105,
        "name": "Legend: Tenacity",
        "majorChangePatchVersion": "",
        "tooltip": "Gain 5% tenacity plus an additional 1.5% for every <i>Legend</i> stack (<statGood>max 10 stacks</statGood>).<br><br>Earn progress toward <i>Legend</i> stacks for every champion takedown, epic monster takedown, large monster kill, and minion kill.<br><hr><br>Total tenacity granted: <scaleAD>@f1*100@%</scaleAD> (<statGood>@f3@ of 10</statGood>)<br>Progress Towards Next Stack: @f2@%",
        "shortDesc": "<lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>Takedowns</lol-uikit-tooltipped-keyword> on enemies grant permanent <b>Tenacity</b>. ",
        "longDesc": "Gain 5% tenacity plus an additional 1.5% for every <i>Legend</i> stack (<statGood>max 10 stacks</statGood>).<br><br>Earn progress toward <i>Legend</i> stacks for every champion takedown, epic monster takedown, large monster kill, and minion kill.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Precision/LegendTenacity/LegendTenacity.png",
        "endOfGameStatDescs": [
            "Time Completed: @eogvar1@:@eogvar2@"
        ],
        "recommendationDescriptorAttributes": {
            "kDurability": 4,
            "kUtility": 6
        }
    },
    {
        "id": 8010,
        "name": "Conqueror",
        "majorChangePatchVersion": "9.4",
        "tooltip": "Basic attacks or spells that deal damage to an enemy champion grant 2 stacks of Conqueror for 5s, gaining <scaleLevel>@f5.1@</scaleLevel> <scaleAD>Attack Damage</scaleAD> per stack. Stacks up to 12 times. Ranged champions gain only 1 stack per basic attack.<br><br>When fully stacked, heal for 8% of the damage you deal to champions (5% for ranged champions).<br><br>Total Healing: @f1@",
        "shortDesc": "Gain stacks of adaptive force when attacking enemy champions. After reaching 12 stacks, heal for a portion of damage you deal to champions.",
        "longDesc": "Basic attacks or spells that deal damage to an enemy champion grant 2 stacks of Conqueror for 5s, gaining 1.8-4 <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive Force</font></lol-uikit-tooltipped-keyword> per stack. Stacks up to 12 times. Ranged champions gain only 1 stack per basic attack.<br><br>When fully stacked, heal for 8% of the damage you deal to champions (5% for ranged champions).",
        "recommendationDescriptor": "Bonus Damage, Sustain",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Precision/Conqueror/Conqueror.png",
        "endOfGameStatDescs": [
            "Total healing: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8106,
        "name": "Ultimate Hunter",
        "majorChangePatchVersion": "9.9",
        "tooltip": "Your ultimate gains <attention>6</attention> Ability Haste, plus an additional <attention>5</attention> Ability Haste per <i>Bounty Hunter</i> stack.<br><br><i>Bounty Hunter</i> stacks are earned the first time you get a takedown on each enemy champion.<br><hr><br><u>No Claimable Bounties</u>",
        "shortDesc": "<b>Unique</b> <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>takedowns</lol-uikit-tooltipped-keyword> grant permanent cooldown reduction on your Ultimate. ",
        "longDesc": "Your ultimate gains <attention>6</attention> Ability Haste, plus an additional <attention>5</attention> Ability Haste per <i>Bounty Hunter</i> stack.<br><br><i>Bounty Hunter</i> stacks are earned the first time you get a takedown on each enemy champion.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/UltimateHunter/UltimateHunter.png",
        "endOfGameStatDescs": [
            "Total Stacks: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kCooldown": 10
        }
    },
    {
        "id": 8017,
        "name": "Cut Down",
        "majorChangePatchVersion": "",
        "tooltip": "Deal 5% to 15% more damage to champions, based on how much more max health they have than you.<br><br><rules>Bonus damage scales up linearly against enemies with 10% to 100% more max health than you.</rules><br><hr><br>Total bonus damage: <scaleAD>@f1@</scaleAD>",
        "shortDesc": "Deal more damage to champions with more max health than you.",
        "longDesc": "Deal 5% to 15% more damage to champions, based on how much more max health they have than you.<br><br><rules>Bonus damage scales up linearly against enemies with 10% to 100% more max health than you.</rules>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Precision/CutDown/CutDown.png",
        "endOfGameStatDescs": [
            "Total Bonus Damage: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kBurstDamage": 1,
            "kDamagePerSecond": 9
        }
    },
    {
        "id": 8224,
        "name": "Nullifying Orb",
        "majorChangePatchVersion": "",
        "tooltip": "When you take magic damage that would reduce your Health below 30%, gain a shield that absorbs @NullifyingShieldSize@ magic damage for 4s.<br><br>Cooldown: 60s<br><hr><br>Total Magic Damage Blocked: @f1@",
        "shortDesc": "Gain a magic damage shield when taken to low health by magic damage.",
        "longDesc": "When you take magic damage that would reduce your health below 30%, first gain a shield that absorbs 35 to 110 (+14% bonus attack damage) + (9% ability power) magic damage based on level for 4s.<br><br>Cooldown: 60s",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/NullifyingOrb/Pokeshield.png",
        "endOfGameStatDescs": [
            "Total shield granted: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kDurability": 10
        }
    },
    {
        "id": 8210,
        "name": "Transcendence",
        "majorChangePatchVersion": "",
        "tooltip": "Gain bonuses upon reaching the following levels:<br>Level 5: +5 <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_CDR'>Ability Haste</lol-uikit-tooltipped-keyword> <br>Level 8: +5 <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_CDR'>Ability Haste</lol-uikit-tooltipped-keyword> <br>Level 11: On Champion takedown, reduce the remaining cooldown of basic abilities by 20%.<br><br><hr><br>Bonus Ability Haste: +@f4*100@<br>Seconds Refunded: @f3@",
        "shortDesc": "Gain bonuses upon reaching the following levels:<br>Level 5: +5 <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_CDR'>Ability Haste</lol-uikit-tooltipped-keyword> <br>Level 8: +5 <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_CDR'>Ability Haste</lol-uikit-tooltipped-keyword> <br>Level 11: On Champion takedown, reduce the remaining cooldown of basic abilities by 20%.",
        "longDesc": "Gain bonuses upon reaching the following levels:<br>Level 5: +5 <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_CDR'>Ability Haste</lol-uikit-tooltipped-keyword> <br>Level 8: +5 <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_CDR'>Ability Haste</lol-uikit-tooltipped-keyword> <br>Level 11: On Champion takedown, reduce the remaining cooldown of basic abilities by 20%.<br>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/Transcendence/Transcendence.png",
        "endOfGameStatDescs": [
            "Seconds refunded: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kCooldown": 10
        }
    },
    {
        "id": 8005,
        "name": "Press the Attack",
        "majorChangePatchVersion": "",
        "tooltip": "Hitting an enemy champion with 3 consecutive basic attacks deals <scaleLevel>@f4@</scaleLevel> bonus <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'><font color='#48C4B7'>adaptive damage</font></lol-uikit-tooltipped-keyword> (based on level) and makes them vulnerable, increasing the damage they take by <scaleLevel>@f7@%</scaleLevel> from all sources for 6s.<br><hr><br>Bonus Damage Dealt: <scaleAD>@f2@</scaleAD><br>Total Exposure Damage: <scaleAD>@f3@</scaleAD>",
        "shortDesc": "Hitting an enemy champion 3 consecutive times makes them vulnerable, dealing bonus damage and causing them to take more damage from all sources for 6s.",
        "longDesc": "Hitting an enemy champion with 3 consecutive basic attacks deals 40 - 180 bonus <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'><font color='#48C4B7'>adaptive damage</font></lol-uikit-tooltipped-keyword> (based on level) and makes them vulnerable, increasing the damage they take by 8% from all sources for 6s.",
        "recommendationDescriptor": "Single Target Damage",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Precision/PressTheAttack/PressTheAttack.png",
        "endOfGameStatDescs": [
            "Total Damage: @eogvar1@",
            "Bonus Damage: @eogvar2@",
            "Expose Damage: @eogvar3@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8435,
        "name": "Mirror Shell",
        "majorChangePatchVersion": "",
        "tooltip": "Gain +6 Magic Resist. <br><br>Heal effects from consumables, heals for at least 20 health and shields increase your Magic Resist by 5% for 3s.",
        "shortDesc": "Gain +6 Magic Resist. <br>Heals, including consumables, increase your Magic Resist by 5% temporarily.<br>",
        "longDesc": "Gain +6 Magic Resist. <br><br>Heal effects from consumables, heals for at least 20 health and shields increase your Magic Resist by 5% for 3s.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/MirrorShell/MirrorShell.png",
        "endOfGameStatDescs": [
            "Bonus Magic Resist: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8115,
        "name": "The Aether Blade",
        "majorChangePatchVersion": "",
        "tooltip": "<pathDomination>Domination</pathDomination> + <pathSorcery>Sorcery</pathSorcery><br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD>",
        "shortDesc": "<pathBonus><pathDomination>Domination</pathDomination> + <pathSorcery>Sorcery</pathSorcery> Set Bonus</pathBonus>",
        "longDesc": "+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8359,
        "name": "Kleptomancy",
        "majorChangePatchVersion": "8.23",
        "tooltip": "After using an ability, each of your next 2 attacks can grant 5 gold... or something nicer.<br><br>Only attacks against champions grant you a reward.<br><hr><br>Gold Gained: @f1@<br>Items Looted: @f3@",
        "shortDesc": "Loot gold and items from enemy champions by casting spells and auto attacking them.",
        "longDesc": "After using an ability, each of your next 2 attacks can grant 5 gold... or something nicer.<br><br>Only attacks against champions grant you a reward.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/Kleptomancy/Kleptomancy.png",
        "endOfGameStatDescs": [
            "Gold Granted: @eogvar1@",
            "Items Looted: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8352,
        "name": "Time Warp Tonic",
        "majorChangePatchVersion": "8.22",
        "tooltip": "Consuming a potion or biscuit grants 30% of its health or mana restoration immediately. In addition, gain <speed>2% Move Speed</speed> while under their effects.<br><br><br><hr><br>Time Spent hasted: @f1@s<br>Total health instantly restored: @f2@<br>Total mana instantly restored: @f3@",
        "shortDesc": "Potions and biscuits grant some restoration immediately. Gain <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_MS'>MS</lol-uikit-tooltipped-keyword>  while under their effects.",
        "longDesc": "Consuming a potion or biscuit grants 30% of its health or mana restoration immediately. In addition, gain <speed>2% Move Speed</speed> while under their effects.<br><br>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/TimeWarpTonic/TimeWarpTonic.png",
        "endOfGameStatDescs": [
            "Time Spent Hasted: @eogvar1@",
            "Total Immediate Health Restored: @eogvar2@",
            "Total Immediate Mana Restored: @eogvar3@"
        ],
        "recommendationDescriptorAttributes": {
            "kHealing": 5,
            "kMoveSpeed": 5
        }
    },
    {
        "id": 5003,
        "name": "Magic Resist",
        "majorChangePatchVersion": "",
        "tooltip": "+8 Magic Resist",
        "shortDesc": "+8 Magic Resist",
        "longDesc": "+8 Magic Resist",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/StatMods/StatModsMagicResIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8135,
        "name": "Treasure Hunter",
        "majorChangePatchVersion": "",
        "tooltip": "Gain an additional <gold>50 gold</gold> the next time you collect a <i>Bounty Hunter</i> stack. Increase the gold gained by <gold>20 gold</gold> for each <i>Bounty Hunter</i> stack, up to <gold>130 gold</gold>.<br><br><i>Bounty Hunter</i> stacks are earned the first time you get a takedown on each enemy champion.<br><br>Current Bounty Available: <gold>@f15@ gold</gold><br>Bonus Gold Collected: <gold>@f3@ gold</gold><br><hr><br><u>No Claimable Bounties</u>",
        "shortDesc": "<b>Unique</b> <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>takedowns</lol-uikit-tooltipped-keyword> grant additional gold the first time they are collected. ",
        "longDesc": "Gain an additional <gold>50 gold</gold> the next time you collect a <i>Bounty Hunter</i> stack. Increase the gold gained by <gold>20 gold</gold> for each <i>Bounty Hunter</i> stack, up to <gold>130 gold</gold>.<br><br><i>Bounty Hunter</i> stacks are earned the first time you get a takedown on each enemy champion.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/TreasureHunter/TreasureHunter.png",
        "endOfGameStatDescs": [
            "Gold Collected: @eogvar1@",
            "Total Stacks: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {
            "kGold": 15
        }
    },
    {
        "id": 8120,
        "name": "Ghost Poro",
        "majorChangePatchVersion": "9.9",
        "tooltip": "When your wards expire, they leave behind a Ghost Poro, which grants vision for 90s. Nearby enemy champions scare the Ghost Poro away.<br><br>Gain an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 1.2 Attack Damage or 2 Ability Power for every Ghost Poro spawned and when your Ghost Poro spots an enemy champion up to 10 stacks. <br><br>After gaining 10 stacks, additionally gain 10 adaptive force.<br><hr><br>Stats Gained: <scaleAD>+@f2@ Attack Damage</scaleAD><br>Poros Spawned: @f3@<br>Enemies Spotted: @f5@",
        "shortDesc": "When your wards expire, they leave behind a Ghost Poro. The Ghost Poro grants vision until discovered. Gain permanent AD or AP, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'>adaptive</lol-uikit-tooltipped-keyword> for each Ghost Poro and when your Ghost Poro spots an enemy champion, plus bonus upon completion.",
        "longDesc": "When your wards expire, they leave behind a Ghost Poro, which grants vision for 90s. Nearby enemy champions scare the Ghost Poro away.<br><br>Gain an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 1.2 Attack Damage or 2 Ability Power for every Ghost Poro spawned and when your Ghost Poro spots an enemy champion up to 10 stacks. <br><br>After gaining 10 stacks, additionally gain 10 adaptive force.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/GhostPoro/GhostPoro.png",
        "endOfGameStatDescs": [
            "Ghost Poros Spawned: @eogvar3@",
            "Enemies Spotted: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kUtility": 10
        }
    },
    {
        "id": 8134,
        "name": "Ingenious Hunter",
        "majorChangePatchVersion": "",
        "tooltip": "Gain <attention>20</attention> <b>Item Haste</b> plus an additional <attention>6</attention> <b>Item Haste</b> per <i>Bounty Hunter</i> stack (includes Trinkets).<br><br><i>Bounty Hunter</i> stacks are earned the first time you get a takedown on each enemy champion.<br><br><rules>Item Haste affects all items with cooldowns. </rules><br><br>Total item activations (including Trinkets): @f3@<br><hr><br><u>No Claimable Bounties</u>",
        "shortDesc": "<b>Unique</b> <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>takedowns</lol-uikit-tooltipped-keyword> grant permanent Item <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_CDR'>Haste</lol-uikit-tooltipped-keyword> (includes Trinkets).",
        "longDesc": "Gain <attention>20</attention> <b>Item Haste</b> plus an additional <attention>6</attention> <b>Item Haste</b> per <i>Bounty Hunter</i> stack (includes Trinkets).<br><br><i>Bounty Hunter</i> stacks are earned the first time you get a takedown on each enemy champion.<br><br><rules>Item Haste affects all items with cooldowns. </rules>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/IngeniousHunter/IngeniousHunter.png",
        "endOfGameStatDescs": [
            "Total Stacks: @eogvar2@",
            "Total Item Activations (Including Trinkets): @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kCooldown": 8,
            "kUtility": 2
        }
    },
    {
        "id": 8351,
        "name": "Glacial Augment",
        "majorChangePatchVersion": "",
        "tooltip": "Immobilizing an enemy champion will cause 3 glacial rays to emanate from them towards you and other nearby champions, creating frozen zones for 3 (+ 100% of the immobilizing effect's duration) seconds that slow enemies and reduce their damage by 15% against your allies (not including yourself). <br><br>Cooldown: 25s<br>Slow Amount: @f3@% = 20% <healing>+@f4@% (%i:scaleHealShield%)</healing> <scaleAP>+@f5@% (%i:scaleAP%)</scaleAP> <scaleAD>+@f6@% (%i:scaleAD%)</scaleAD> <br>Duration Enemy Champs Slowed: @f1@s<br>Damage Reduced: @f2@",
        "shortDesc": "Immobilizing an enemy champion will cause 3 glacial rays that slow nearby enemies and reduce their damage to your allies.",
        "longDesc": "Immobilizing an enemy champion will cause 3 glacial rays to emanate from them towards you and other nearby champions, creating frozen zones for 3 (+ 100% of the immobilizing effect's duration) seconds that slow enemies for 20% (+9% per 10% Heal and Shield Power) (+6% per 100 Ability Power) (+7% per 100 bonus Attack Damage) and reduce their damage by 15% against your allies (not including yourself). <br><br>Cooldown: 25s",
        "recommendationDescriptor": "Slow Enemies",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/GlacialAugment/GlacialAugment.png",
        "endOfGameStatDescs": [
            "Duration Enemy Champs Slowed: @eogvar1@s",
            "Damage Reduced: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8242,
        "name": "Unflinching",
        "majorChangePatchVersion": "",
        "tooltip": "Gain <scaleLevel>@f1@</scaleLevel> <scaleArmor>Armor</scaleArmor> and <scaleMR>Magic Resist</scaleMR> while crowd controlled and for 2s after.<br><br>Total combat time with increased resistances: @f6@s.",
        "shortDesc": "Gain Armor and Magic Resist when receiving crowd control.",
        "longDesc": "Gain 2 - 10 (level scaling) Armor and Magic Resist when crowd controlled and for 2 seconds after.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/Unflinching/Unflinching.png",
        "endOfGameStatDescs": [
            "Seconds in combat with bonus resistances: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kDurability": 4,
            "kUtility": 6
        }
    },
    {
        "id": 8401,
        "name": "Shield Bash",
        "majorChangePatchVersion": "8.23",
        "tooltip": "While shielded, gain <scaleLevel>@f6@</scaleLevel> bonus Armor and Magic Resist.<br><br>Whenever you gain a new shield, your next basic attack against a champion deals <scaleLevel>@f4@</scaleLevel> <scaleHealth>(+@f2@)</scaleHealth> <scaleMana>(+8.5% New Shield Amount)</scaleMana> bonus magic damage.<br><br>You have up to 2s after the shield expires to use this effect.<br><hr><br>Total Damage Dealt: @f1@",
        "shortDesc": "Whenever you gain a shield, your next basic attack against a champion deals bonus <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> damage.",
        "longDesc": "While shielded, gain <scaleLevel>1 - 10</scaleLevel> Armor and Magic Resist based on Level.<br><br>Whenever you gain a new shield,  your next basic attack against a champion deals <scaleLevel>5 - 30</scaleLevel> <scaleHealth>(+1.5% Bonus Health)</scaleHealth> <scaleMana>(+8.5% New Shield Amount)</scaleMana> bonus <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> damage.<br><br>You have up to 2s after the shield expires to use this effect.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/MirrorShell/MirrorShell.png",
        "endOfGameStatDescs": [
            "Total Damage: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kBurstDamage": 5,
            "kDurability": 5
        }
    },
    {
        "id": 9111,
        "name": "Triumph",
        "majorChangePatchVersion": "",
        "tooltip": "Takedowns restore 5% of your missing health, 2.5% of your max health, and grant an additional 20 gold. <br><hr><br>Total health restored: <scaleAD>@f1@</scaleAD><br>Total bonus gold granted: <scaleAD>@f2@</scaleAD>",
        "shortDesc": "<lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>Takedowns</lol-uikit-tooltipped-keyword> restore 5% of your missing health and grant an additional 20 gold. ",
        "longDesc": "Takedowns restore 5% of your missing health, 2.5% of your max health, and grant an additional 20 gold. <br><br><hr><br><i>'The most dangerous game brings the greatest glory.' <br>—Noxian Reckoner</i>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Precision/Triumph.png",
        "endOfGameStatDescs": [
            "Total Health Restored: @eogvar1@",
            "Total bonus gold granted: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {
            "kDurability": 2,
            "kHealing": 8
        }
    },
    {
        "id": 8105,
        "name": "Relentless Hunter",
        "majorChangePatchVersion": "9.9",
        "tooltip": "Gain <speed>5 Move Speed</speed> out of combat plus <speed>8</speed> per <i>Bounty Hunter</i> stack.<br><br><i>Bounty Hunter</i> stacks are earned the first time you get a takedown on each enemy champion.<br><br>Current Relentless Hunter increase: <speed>@f3.2@% Move Speed</speed><br><hr><br><u>No Claimable Bounties</u>",
        "shortDesc": "<b>Unique</b> <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>takedowns</lol-uikit-tooltipped-keyword> grant permanent <b>out of combat <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_MS'>MS</lol-uikit-tooltipped-keyword></b>. ",
        "longDesc": "Gain <speed>5 Move Speed</speed> out of combat plus <speed>8</speed> per <i>Bounty Hunter</i> stack.<br><br><i>Bounty Hunter</i> stacks are earned the first time you get a takedown on each enemy champion.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/RelentlessHunter/RelentlessHunter.png",
        "endOfGameStatDescs": [
            "Total Stacks: @eogvar2@",
            "<speed>@eogvar1@% Move Speed</speed> increase"
        ],
        "recommendationDescriptorAttributes": {
            "kMoveSpeed": 10
        }
    },
    {
        "id": 8454,
        "name": "The Leviathan",
        "majorChangePatchVersion": "",
        "tooltip": "<pathResolve>Resolve</pathResolve> + <pathDomination>Domination</pathDomination> <br>+0-0 Health based on level<br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD>",
        "shortDesc": "<pathBonus><pathResolve>Resolve</pathResolve> + <pathDomination>Domination</pathDomination> Set Bonus</pathBonus>",
        "longDesc": "+0-0 Health based on level<br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8275,
        "name": "Nimbus Cloak",
        "majorChangePatchVersion": "8.11",
        "tooltip": "After casting a Summoner Spell, gain a <speed>Move Speed</speed> increase that lasts for 2s and allows you to pass through units.<br><hr><br>Increase: <speed>5% - 25% Move Speed</speed> based on the Summoner Spell's cooldown. (Higher cooldown Summoner Spells grant more <speed>Move Speed</speed>). <br><hr><br>Times activated: @f1@",
        "shortDesc": "After casting a Summoner Spell, gain a short <speed>Move Speed</speed> increase that allows you to pass through units.",
        "longDesc": "After casting a Summoner Spell, gain a <speed>Move Speed</speed> increase that lasts for 2s and allows you to pass through units.<br><br>Increase: <speed>5% - 25% Move Speed</speed> based on the Summoner Spell's cooldown. (Higher cooldown Summoner Spells grant more <speed>Move Speed</speed>). ",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/NimbusCloak/6361.png",
        "endOfGameStatDescs": [
            "Times activated: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kMoveSpeed": 10
        }
    },
    {
        "id": 8207,
        "name": "The Cryptic",
        "majorChangePatchVersion": "",
        "tooltip": "<pathSorcery>Sorcery</pathSorcery> + <pathInspiration>Inspiration</pathInspiration><br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD>",
        "shortDesc": "<pathBonus><pathSorcery>Sorcery</pathSorcery> + <pathInspiration>Inspiration</pathInspiration> Set Bonus</pathBonus>",
        "longDesc": "+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 5012,
        "name": "Resist Scaling",
        "majorChangePatchVersion": "",
        "tooltip": "+@f1@ Armor and Magic Resist (based on level)",
        "shortDesc": "+1-8 Armor and Magic Resist (based on level)",
        "longDesc": "+1-8 Armor and Magic Resist (based on level)",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/StatMods/StatModsAdaptiveForceScalingIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8439,
        "name": "Aftershock",
        "majorChangePatchVersion": "9.9",
        "tooltip": "After immobilizing an enemy champion, increase your Armor and Magic Resist for 2.5s. Then explode, dealing magic damage to nearby enemies.<br><br>Damage: <scaleLevel>@f4@</scaleLevel> <scaleHealth>(+@f5@)</scaleHealth> <br>Armor buff: @f8@<scaleArmor> (+@f2@)</scaleArmor><br>Magic Resist buff: @f8@<scaleMR> (+@f3@)</scaleMR><br>Cooldown: 20s<br><hr><br>Total damage dealt: <scaleAD>@f1@</scaleAD><br>Total damage mitigated: <scaleHealth>@f9@</scaleHealth>",
        "shortDesc": "After <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Immobilize'>immobilizing</lol-uikit-tooltipped-keyword> an enemy champion gain defenses and later deal a burst of magic damage around you.",
        "longDesc": "After immobilizing an enemy champion, increase your Armor and Magic Resist by 35 + 80% of your Bonus Resists for 2.5s. Then explode, dealing magic damage to nearby enemies.<br><br>Damage: 25 - 120 (+8% of your bonus health)<br>Cooldown: 20s<br><br>Resistance bonus from Aftershock capped at: 80-150 (based on level)<br>",
        "recommendationDescriptor": "Burst Defenses",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/VeteranAftershock/VeteranAftershock.png",
        "endOfGameStatDescs": [
            "Total Damage Dealt: @eogvar1@",
            "Total Damage Mitigated: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8109,
        "name": "The Wicked Maestro ",
        "majorChangePatchVersion": "",
        "tooltip": "<pathDomination>Domination</pathDomination> + <pathInspiration>Inspiration</pathInspiration><br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD>",
        "shortDesc": "<pathBonus><pathDomination>Domination</pathDomination> + <pathInspiration>Inspiration</pathInspiration> Set Bonus</pathBonus>",
        "longDesc": "+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 5002,
        "name": "Armor",
        "majorChangePatchVersion": "",
        "tooltip": "+6 Armor",
        "shortDesc": "+6 Armor",
        "longDesc": "+6 Armor",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/StatMods/StatModsArmorIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 5011,
        "name": "Health",
        "majorChangePatchVersion": "",
        "tooltip": "<scaleHealth>+65 Health</scaleHealth>",
        "shortDesc": "+65 Health",
        "longDesc": "+65 Health",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/StatMods/StatModsHealthScalingIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 5013,
        "name": "Tenacity and Slow Resist",
        "majorChangePatchVersion": "",
        "tooltip": "+10% Tenacity and Slow Resist",
        "shortDesc": "+10% Tenacity and Slow Resist",
        "longDesc": "+10% Tenacity and Slow Resist",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/StatMods/StatModsTenacityIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8414,
        "name": "The Behemoth",
        "majorChangePatchVersion": "",
        "tooltip": "<pathResolve>Resolve</pathResolve> + <pathPrecision>Precision</pathPrecision> <br>+0-0 Health based on level<br>+0% Attack Speed",
        "shortDesc": "<pathBonus><pathResolve>Resolve</pathResolve> + <pathPrecision>Precision</pathPrecision> Set Bonus</pathBonus>",
        "longDesc": "+0-0 Health based on level<br>+0% Attack Speed",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 5008,
        "name": "Adaptive Force",
        "majorChangePatchVersion": "",
        "tooltip": "<scaleAD>+@f2@ Attack Damage</scaleAD>",
        "shortDesc": "+9 <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive Force</font></lol-uikit-tooltipped-keyword>",
        "longDesc": "+9 <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive Force</font></lol-uikit-tooltipped-keyword>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/StatMods/StatModsAdaptiveForceIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8320,
        "name": "The Timeless",
        "majorChangePatchVersion": "",
        "tooltip": "<pathInspiration>Inspiration</pathInspiration> + <pathResolve>Resolve</pathResolve><br>+0-0 Health based on level",
        "shortDesc": "<pathBonus><pathInspiration>Inspiration</pathInspiration> + <pathResolve>Resolve</pathResolve> Set Bonus</pathBonus>",
        "longDesc": "+0-0 Health based on level",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8319,
        "name": "The Stargazer",
        "majorChangePatchVersion": "",
        "tooltip": "<pathInspiration>Inspiration</pathInspiration> + <pathSorcery>Sorcery</pathSorcery><br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD>",
        "shortDesc": "<pathBonus><pathInspiration>Inspiration</pathInspiration> + <pathSorcery>Sorcery</pathSorcery> Set Bonus</pathBonus>",
        "longDesc": "+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 5001,
        "name": "Health Scaling",
        "majorChangePatchVersion": "",
        "tooltip": "<scaleHealth>+@f1@ Health</scaleHealth> (based on level)",
        "shortDesc": "+10-180 Health (based on level)",
        "longDesc": "+10-180 Health (based on level)",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/StatMods/StatModsHealthPlusIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8430,
        "name": "Iron Skin",
        "majorChangePatchVersion": "",
        "tooltip": "Gain +5 Armor. <br><br>Heal effects from consumables, heals for at least 20 health and shields increase your Armor by 5% for 3s.",
        "shortDesc": "Gain +5 Armor. <br>Heals, including consumables, increase your Armor by 5% temporarily.",
        "longDesc": "Gain +5 Armor. <br><br>Heal effects from consumables, heals for at least 20 health and shields increase your Armor by 5% for 3s.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/IronSkin/IronSkin.png",
        "endOfGameStatDescs": [
            "Percent of game active: @eogvar1@%"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8014,
        "name": "Coup de Grace",
        "majorChangePatchVersion": "",
        "tooltip": "Deal 8% more damage to champions who have less than 40% health.<br><hr><br>Total bonus damage dealt: <scaleAD>@f1@</scaleAD>",
        "shortDesc": "Deal more damage to low health enemy champions.",
        "longDesc": "Deal 8% more damage to champions who have less than 40% health.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Precision/CoupDeGrace/CoupDeGrace.png",
        "endOfGameStatDescs": [
            "Total Bonus Damage: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kBurstDamage": 8,
            "kDamagePerSecond": 2
        }
    },
    {
        "id": 5007,
        "name": "Ability Haste",
        "majorChangePatchVersion": "",
        "tooltip": "+@f1@ Ability Haste",
        "shortDesc": "+8 <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_CDR'>Ability Haste</lol-uikit-tooltipped-keyword> ",
        "longDesc": "+8 <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_CDR'>Ability Haste</lol-uikit-tooltipped-keyword> ",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/StatMods/StatModsCDRScalingIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8021,
        "name": "Fleet Footwork",
        "majorChangePatchVersion": "",
        "tooltip": "Attacking and moving builds Energy stacks. At 100 stacks, your next attack is Energized.<br><br>Energized attacks heal you for <font color='#ffffff'>@f2@</font> <scaleAD>(+@f3@)</scaleAD> <scaleAP>(+@f4@)</scaleAP> and grant <speed>@f5*100@% Move Speed</speed> for 1 second.<br><rules><br>Healing from minions is 10% effective for Ranged Champions, and 20% effective for Melee Champions.<br></rules><hr><br>Total Healing: @f1@",
        "shortDesc": "Attacking and moving builds Energy stacks. At 100 stacks, your next attack heals you and grants increased <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_MS'>MS</lol-uikit-tooltipped-keyword>.",
        "longDesc": "Attacking and moving builds Energy stacks. At 100 stacks, your next attack is Energized<br><br>Energized attacks heal you for 10 - 130 (+0.1 Bonus AD, +0.05 AP) and grant <speed>20% Move Speed</speed> for 1s.<br><br>Healing from minions is 10% effective for Ranged Champions, and 20% effective for Melee Champions.",
        "recommendationDescriptor": "Movement, Health Recovery",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Precision/FleetFootwork/FleetFootwork.png",
        "endOfGameStatDescs": [
            "Total Healing: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8226,
        "name": "Manaflow Band",
        "majorChangePatchVersion": "8.7",
        "tooltip": "Hitting an enemy champion with an ability permanently increases your maximum mana by 25, up to 250 mana.<br><br>After reaching 250 bonus mana, restore 1% of your missing mana every 5 seconds.<br><br>Cooldown: 15 seconds<br><hr><br>Total bonus mana: @f1@<br>Total mana restored: @f2@",
        "shortDesc": "Hitting an enemy champion with an ability permanently increases your maximum mana by 25, up to 250 mana.<br><br>After reaching 250 bonus mana, restore 1% of your missing mana every 5 seconds.",
        "longDesc": "Hitting an enemy champion with an ability permanently increases your maximum mana by 25, up to 250 mana.<br><br>After reaching 250 bonus mana, restore 1% of your missing mana every 5 seconds.<br><br>Cooldown: 15 seconds",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/ManaflowBand/ManaflowBand.png",
        "endOfGameStatDescs": [
            "Total bonus mana: @eogvar1@",
            "Total mana restored: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {
            "kMana": 15
        }
    },
    {
        "id": 8451,
        "name": "Overgrowth",
        "majorChangePatchVersion": "8.23",
        "tooltip": "Absorb life essence from monsters or enemy minions that die near you, permanently gaining 3 maximum health for every 8.<br><br>When you've absorbed 120 monsters or enemy minions, gain an additional 3.5% maximum health.<br><hr><br>Total Max Health Earned: <scaleHealth>@f1@</scaleHealth><br>Enemies Absorbed: <passiveText>@f2@</passiveText>",
        "shortDesc": "Gain permanent max health when minions or monsters die near you.",
        "longDesc": "Absorb life essence from monsters or enemy minions that die near you, permanently gaining 3 maximum health for every 8.<br><br>When you've absorbed 120 monsters or enemy minions, gain an additional 3.5% maximum health.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/Overgrowth/Overgrowth.png",
        "endOfGameStatDescs": [
            "Total Bonus Max Health: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kDurability": 10
        }
    },
    {
        "id": 8313,
        "name": "Triple Tonic",
        "majorChangePatchVersion": "",
        "tooltip": "Upon reaching level 3, gain an Elixir of Avarice.<br>Upon reaching level 6, gain an Elixir of Force.<br>Upon reaching level 9, gain an Elixir of Skill. <br><br>Items Gained: @f1@",
        "shortDesc": "Upon reaching level 3, gain an Elixir of Avarice.<br>Upon reaching level 6, gain an Elixir of Force.<br>Upon reaching level 9, gain an Elixir of Skill. ",
        "longDesc": "Upon reaching level 3, gain an Elixir of Avarice.<br>Upon reaching level 6, gain an Elixir of Force.<br>Upon reaching level 9, gain an Elixir of Skill. ",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/PerfectTiming/AlchemistCabinet.png",
        "endOfGameStatDescs": [
            "Items Gained: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kUtility": 10
        }
    },
    {
        "id": 9103,
        "name": "Legend: Bloodline",
        "majorChangePatchVersion": "",
        "tooltip": "Gain <scaleAD>0.35% Life Steal</scaleAD> for every <i>Legend</i> stack (<statGood>max 15 stacks</statGood>). At maximum <i>Legend</i> stacks, gain <scaleHealth>85 max health</scaleHealth>.<br><br>Earn progress toward <i>Legend</i> stacks for every champion takedown, epic monster takedown, large monster kill, and minion kill.<br><hr><br>Total Life Steal Granted: <scaleAD>@f1*100@%</scaleAD> (<statGood>@f3@ of 15</statGood>)<br>Progress Towards Next Stack: @f2@%<br>",
        "shortDesc": "<lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>Takedowns</lol-uikit-tooltipped-keyword> on enemies grant permanent<b> Life Steal</b>, up to a cap. Once the cap is reached, increase your max health. Weaker earlier but stronger later game than other Legend Runes.",
        "longDesc": "Gain <scaleAD>0.35% Life Steal</scaleAD> for every <i>Legend</i> stack (<statGood>max 15 stacks</statGood>). At maximum <i>Legend</i> stacks, gain <scaleHealth>85 max health</scaleHealth>.<br><br>Earn progress toward <i>Legend</i> stacks for every champion takedown, epic monster takedown, large monster kill, and minion kill.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Precision/LegendBloodline/LegendBloodline.png",
        "endOfGameStatDescs": [
            "Time Completed: @eogvar1@:@eogvar2@"
        ],
        "recommendationDescriptorAttributes": {
            "kHealing": 10
        }
    },
    {
        "id": 8114,
        "name": "The Immortal Butcher",
        "majorChangePatchVersion": "",
        "tooltip": "<pathDomination>Domination</pathDomination> + <pathResolve>Resolve</pathResolve><br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD><br>+0-0 Health based on level",
        "shortDesc": "<pathBonus><pathDomination>Domination</pathDomination> + <pathResolve>Resolve</pathResolve> Set Bonus</pathBonus>",
        "longDesc": "+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>+0-0 Health based on level",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8230,
        "name": "Phase Rush",
        "majorChangePatchVersion": "",
        "tooltip": "Hitting an enemy champion with 3 attacks or <b>separate</b> abilities within 4s grants <speed>15 - 40% Move Speed</speed> based on level and 75% Slow Resistance. <hr>This is increased to <speed>25 - 50% Move Speed</speed> for Melee champions.<hr>Duration: 3s<br>Cooldown: @f4@s<br>Haste Bonus: @f2@%",
        "shortDesc": "Hitting an enemy champion with 3 <b>separate</b> attacks or abilities grants a burst of <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_MS'>MS</lol-uikit-tooltipped-keyword>. ",
        "longDesc": "Hitting an enemy champion with 3 attacks or <b>separate</b> abilities within 4s grants <speed>15 - 40% Move Speed</speed> based on level and 75% Slow Resistance. <hr>This is increased to <speed>25 - 50% Move Speed</speed> for Melee champions.<hr>Duration: 3s<br>Cooldown: 30s - 10s",
        "recommendationDescriptor": "Rush of Movement",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/PhaseRush/PhaseRush.png",
        "endOfGameStatDescs": [
            "Total activations: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8318,
        "name": "The Ruthless Visionary",
        "majorChangePatchVersion": "",
        "tooltip": "<pathInspiration>Inspiration</pathInspiration> + <pathDomination>Domination</pathDomination><br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD>",
        "shortDesc": "<pathBonus><pathInspiration>Inspiration</pathInspiration> + <pathDomination>Domination</pathDomination> Set Bonus</pathBonus>",
        "longDesc": "+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8316,
        "name": "Minion Dematerializer",
        "majorChangePatchVersion": "9.6",
        "tooltip": "Start the game with 3 Minion Dematerializers that kill and absorb lane minions instantly. Minion Dematerializers are on cooldown for the first 180s of the game.<br><br>Absorbing a minion increases your damage by +6% against that type of minion permanently, and an extra +3% for each additional minion of that type absorbed.<br><br><hr><br>Melee Bonus Damage: +@f1@%<br>Caster Bonus Damage: +@f2@%<br>Siege Bonus Damage: +@f3@%",
        "shortDesc": "Start the game with 3 Minion Dematerializers. Killing minions with the item gives permanent bonus damage vs. that minion type.",
        "longDesc": "Start the game with 3 Minion Dematerializers that kill and absorb lane minions instantly. Minion Dematerializers are on cooldown for the first 180s of the game.<br><br>Absorbing a minion increases your damage by +6% against that type of minion permanently, and an extra +3% for each additional minion of that type absorbed.<br>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/MinionDematerializer/MinionDematerializer.png",
        "endOfGameStatDescs": [
            "Bonus Minion Damage Dealt: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kUtility": 10
        }
    },
    {
        "id": 8463,
        "name": "Font of Life",
        "majorChangePatchVersion": "",
        "tooltip": "Impairing the movement of an enemy champion marks them for 4s.<br><br>Ally champions who attack marked enemies heal for 5 + 0.9% of your max health over 2s. ",
        "shortDesc": "<lol-uikit-tooltipped-keyword key='LinkTooltip_Description_ImpairMov'>Impairing</lol-uikit-tooltipped-keyword> the movement of an enemy champion marks them. Your allies heal when attacking champions you've marked. ",
        "longDesc": "Impairing the movement of an enemy champion marks them for 4s.<br><br>Ally champions who attack marked enemies heal for 5 + 0.9% of your max health over 2s. ",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/FontOfLife/FontOfLife.png",
        "endOfGameStatDescs": [
            "Total Ally Healing: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kHealing": 5,
            "kUtility": 5
        }
    },
    {
        "id": 7000,
        "name": "Template",
        "majorChangePatchVersion": "",
        "tooltip": "",
        "shortDesc": "",
        "longDesc": "",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Template/7000.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8304,
        "name": "Magical Footwear",
        "majorChangePatchVersion": "9.9",
        "tooltip": "You get free Slightly Magical Footwear at 12 min, but you cannot buy boots before then. For each takedown you acquire the boots 45s sooner.<br><br>Slightly Magical Footwear grants you an additional <speed>10 Move Speed</speed>.<br><hr><br><scaleAD>Boots arrival time:</scaleAD> @f1@:@f2@@f3@",
        "shortDesc": "You get free boots at 12 min but you cannot buy boots before then. Each <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>takedown</lol-uikit-tooltipped-keyword> you get makes your boots come 45s sooner.",
        "longDesc": "You get free Slightly Magical Footwear at 12 min, but you cannot buy boots before then. For each takedown you acquire the boots 45s sooner.<br><br>Slightly Magical Footwear grants you an additional <speed>10 Move Speed</speed>.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/MagicalFootwear/MagicalFootwear.png",
        "endOfGameStatDescs": [
            "Boots Arrival Time: @eogvar1@:@eogvar2@@eogvar3@"
        ],
        "recommendationDescriptorAttributes": {
            "kGold": 10,
            "kMoveSpeed": 3
        }
    },
    {
        "id": 8236,
        "name": "Gathering Storm",
        "majorChangePatchVersion": "",
        "tooltip": "Every 10 min gain AP or AD, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword>.<br><br><i>10 min</i>: + 8 AP or 5 AD <br><i>20 min</i>: + 24 AP or 14 AD<br><i>30 min</i>: + 48 AP or 29 AD<br><i>40 min</i>: + 80 AP or 48 AD<br><i>50 min</i>: + 120 AP or 72 AD<br><i>60 min</i>: + 168 AP or 101 AD<br>etc...<br><hr><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD>",
        "shortDesc": "Gain increasing amounts of AD or AP, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'>adaptive</lol-uikit-tooltipped-keyword> over the course of the game.",
        "longDesc": "Every 10 min gain AP or AD, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword>.<br><br><i>10 min</i>: + 8 AP or 5 AD <br><i>20 min</i>: + 24 AP or 14 AD<br><i>30 min</i>: + 48 AP or 29 AD<br><i>40 min</i>: + 80 AP or 48 AD<br><i>50 min</i>: + 120 AP or 72 AD<br><i>60 min</i>: + 168 AP or 101 AD<br>etc...",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/GatheringStorm/GatheringStorm.png",
        "endOfGameStatDescs": [
            "Total Bonus AD/AP: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kBurstDamage": 5,
            "kDamagePerSecond": 5
        }
    },
    {
        "id": 8009,
        "name": "Presence of Mind",
        "majorChangePatchVersion": "8.7",
        "tooltip": "Damaging an enemy champion increases your mana regeneration by @RegenAmount@ (80% for ranged) mana per second for 4 seconds. All energy users gain 1.5 energy per second, instead.<br><br>Takedowns restore 15% of your maximum mana or energy. <br><hr><br>Resource Restored: @f1@<br>",
        "shortDesc": "Increase your mana or energy regeneration when damaging an enemy champion. Takedowns restore mana or energy.",
        "longDesc": "Damaging an enemy champion increases your mana regeneration by 1.5-11 (80% for ranged) mana per second for 4 seconds. All energy users gain 1.5 energy per second, instead.<br><br>Takedowns restore 15% of your maximum mana or energy. ",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Precision/PresenceOfMind/PresenceOfMind.png",
        "endOfGameStatDescs": [
            "Resource Restored: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kMana": 15
        }
    },
    {
        "id": 8006,
        "name": "The Eternal Champion",
        "majorChangePatchVersion": "",
        "tooltip": "<pathPrecision>Precision</pathPrecision> + <pathResolve>Resolve</pathResolve><br>+0% Attack Speed<br>+0-0 Health based on level",
        "shortDesc": "<pathBonus><pathPrecision>Precision</pathPrecision> + <pathResolve>Resolve</pathResolve> Set Bonus</pathBonus>",
        "longDesc": "+0% Attack Speed<br>+0-0 Health based on level",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 9104,
        "name": "Legend: Alacrity",
        "majorChangePatchVersion": "",
        "tooltip": "Gain 3% attack speed plus an additional 1.5% for every <i>Legend</i> stack (<statGood>max 10 stacks</statGood>).<br><br>Earn progress toward <i>Legend</i> stacks for every champion takedown, epic monster takedown, large monster kill, and minion kill.<br><hr><br>Total Attack Speed added: <scaleAD>@f1*100@%</scaleAD> (<statGood>@f3@ of 10</statGood>)<br>Progress Towards Next Stack: @f2@%",
        "shortDesc": "<lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>Takedowns</lol-uikit-tooltipped-keyword> on enemies grant permanent <b>Attack Speed</b>. ",
        "longDesc": "Gain 3% attack speed plus an additional 1.5% for every <i>Legend</i> stack (<statGood>max 10 stacks</statGood>).<br><br>Earn progress toward <i>Legend</i> stacks for every champion takedown, epic monster takedown, large monster kill, and minion kill.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Precision/LegendAlacrity/LegendAlacrity.png",
        "endOfGameStatDescs": [
            "Time Completed: @eogvar1@:@eogvar2@"
        ],
        "recommendationDescriptorAttributes": {
            "kDamagePerSecond": 10
        }
    },
    {
        "id": 8416,
        "name": "The Enlightened Titan",
        "majorChangePatchVersion": "",
        "tooltip": "<pathResolve>Resolve</pathResolve> + <pathInspiration>Inspiration</pathInspiration><br>+0-0 Health based on level",
        "shortDesc": "<pathBonus><pathResolve>Resolve</pathResolve> + <pathInspiration>Inspiration</pathInspiration> Set Bonus</pathBonus>",
        "longDesc": "+0-0 Health based on level",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 5005,
        "name": "Attack Speed",
        "majorChangePatchVersion": "",
        "tooltip": "+10% Attack Speed",
        "shortDesc": "+10% Attack Speed",
        "longDesc": "+10% Attack Speed",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/StatMods/StatModsAttackSpeedIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8306,
        "name": "Hextech Flashtraption",
        "majorChangePatchVersion": "",
        "tooltip": "While Flash is on cooldown it is replaced by <i>Hexflash</i>.<br><br><i>Hexflash</i>: Channel for 2s to blink to a new location.<br><br>Cooldown: 20s. Goes on a 10s cooldown when you enter champion combat.",
        "shortDesc": "While Flash is on cooldown it is replaced by <i>Hexflash</i>.<br><br><i>Hexflash</i>: Channel, then blink to a new location.",
        "longDesc": "While Flash is on cooldown it is replaced by <i>Hexflash</i>.<br><br><i>Hexflash</i>: Channel for 2s to blink to a new location.<br><br>Cooldown: 20s. Goes on a 10s cooldown when you enter champion combat.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/HextechFlashtraption/HextechFlashtraption.png",
        "endOfGameStatDescs": [
            "Times Hexflashed: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kUtility": 10
        }
    },
    {
        "id": 8465,
        "name": "Guardian",
        "majorChangePatchVersion": "",
        "tooltip": "<i>Guard</i> allies within 350 units of you, and allies you target with spells for 2.5s. While <i>Guarding</i>, if you or the ally take more than a small amount of damage over the duration of the <i>Guard</i>, both of you gain a shield for 1.5s.<br><hr><br>Cooldown: <scaleLevel>@f5@</scaleLevel> seconds<br>Current shield strength: <scaleLevel>@f2@</scaleLevel> <scaleAP>(+@f3@)</scaleAP> <scaleHealth>(+@f4@)</scaleHealth>.",
        "shortDesc": "Guard allies you cast spells on and those that are very nearby. If you or a guarded ally would take damage based on level, you're both granted a shield.",
        "longDesc": "<i>Guard</i> allies within 350 units of you, and allies you target with spells for 2.5s. While <i>Guarding</i>, if you or the ally take more than a small amount of damage over the duration of the <i>Guard</i>, both of you gain a shield for 1.5s.<br><br>Cooldown: <scaleLevel>90 - 40</scaleLevel> seconds<br>Shield: <scaleLevel>45 - 120</scaleLevel> + <scaleAP>12.5%</scaleAP> of your ability power + <scalehealth>8%</scalehealth> of your bonus health<br>Proc Threshold: <scaleLevel>90 - 250</scaleLevel> postmitigation damage",
        "recommendationDescriptor": "Shield Allies",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/Guardian/Guardian.png",
        "endOfGameStatDescs": [
            "Total Shield Strength: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8138,
        "name": "Eyeball Collection",
        "majorChangePatchVersion": "",
        "tooltip": "Collect eyeballs for champion takedowns. Gain an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 1.2 Attack Damage or 2 Ability Power, per eyeball collected. <br><br>Upon completing your collection at 10 eyeballs, additionally gain an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 6 Attack Damage, or 10 Ability Power.<br><br>Collect 1 eyeball per champion takedown.<br><hr><br>Stats Gained: <scaleAD>+@f2@ Attack Damage</scaleAD><br>Eyeballs Collected: @f3@/10",
        "shortDesc": "Collect eyeballs for champion <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>takedowns</lol-uikit-tooltipped-keyword>. Gain permanent AD or AP, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'>adaptive</lol-uikit-tooltipped-keyword> for each eyeball plus bonus upon collection completion.",
        "longDesc": "Collect eyeballs for champion takedowns. Gain an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 1.2 Attack Damage or 2 Ability Power, per eyeball collected. <br><br>Upon completing your collection at 10 eyeballs, additionally gain an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 6 Attack Damage, or 10 Ability Power.<br><br>Collect 1 eyeball per champion takedown.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/EyeballCollection/EyeballCollection.png",
        "endOfGameStatDescs": [
            "Total Bonus AD/AP: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kBurstDamage": 5,
            "kDamagePerSecond": 5
        }
    },
    {
        "id": 5010,
        "name": "Move Speed",
        "majorChangePatchVersion": "",
        "tooltip": "<speed>+2% Move Speed</speed>",
        "shortDesc": "+2% <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_MS'>Move Speed</lol-uikit-tooltipped-keyword>",
        "longDesc": "+2% <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_MS'>Move Speed</lol-uikit-tooltipped-keyword>",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/StatMods/StatModsMovementSpeedIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8127,
        "name": "The Twisted Surgeon",
        "majorChangePatchVersion": "",
        "tooltip": "<pathDomination>Domination</pathDomination> + <pathPrecision>Precision</pathPrecision><br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD><br>+0% Attack Speed",
        "shortDesc": "<pathBonus><pathDomination>Domination</pathDomination> + <pathPrecision>Precision</pathPrecision> Set Bonus</pathBonus>",
        "longDesc": "+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>+0% Attack Speed",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8143,
        "name": "Sudden Impact",
        "majorChangePatchVersion": "",
        "tooltip": "After exiting stealth or using a dash, leap, blink, or teleport, dealing any damage to a champion grants you 9 Lethality and 7 Magic Penetration for 5s.<br><br>Cooldown: 4s<br><hr><br>Bonus champion damage: @f1@",
        "shortDesc": "Gain a burst of Lethality and Magic Penetration after using a dash, leap, blink, teleport, or when leaving stealth.",
        "longDesc": "After exiting stealth or using a dash, leap, blink, or teleport, dealing any damage to a champion grants you 9 Lethality and 7 Magic Penetration for 5s.<br><br>Cooldown: 4s",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/SuddenImpact/SuddenImpact.png",
        "endOfGameStatDescs": [
            "Bonus Damage: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kBurstDamage": 8,
            "kDamagePerSecond": 2
        }
    },
    {
        "id": 8345,
        "name": "Biscuit Delivery",
        "majorChangePatchVersion": "",
        "tooltip": "Biscuit Delivery: Gain a Total Biscuit of Everlasting Will every 2 mins, until 6 min.<br><br>Biscuits restore 8% of your missing health and mana. Consuming or selling a Biscuit permanently increases your mana cap by 40. <br><br><i>Manaless:</i> Champions without mana restore 12% missing health instead.<br><hr><br>Biscuits Gained: @f1@/@f2@",
        "shortDesc": "Gain a free Biscuit every 2 min, until 6 min. Consuming or selling a Biscuit permanently increases your max mana and restores health and mana.",
        "longDesc": "Biscuit Delivery: Gain a Total Biscuit of Everlasting Will every 2 mins, until 6 min.<br><br>Biscuits restore 8% of your missing health and mana. Consuming or selling a Biscuit permanently increases your mana cap by 40. <br><br><i>Manaless:</i> Champions without mana restore 12% missing health instead.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/BiscuitDelivery/BiscuitDelivery.png",
        "endOfGameStatDescs": [
            "Biscuits Received: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kHealing": 5,
            "kMana": 10
        }
    },
    {
        "id": 8444,
        "name": "Second Wind",
        "majorChangePatchVersion": "",
        "tooltip": "After taking damage from an enemy champion, heal for 4% of your missing health +3 over 10s.<br><hr><br><scaleAD>Total healing: @f1@</scaleAD>",
        "shortDesc": "After taking damage from an enemy champion heal back some missing health over time. ",
        "longDesc": "After taking damage from an enemy champion, heal for 4% of your missing health +3 over 10s.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/SecondWind/SecondWind.png",
        "endOfGameStatDescs": [
            "Total Healing: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {
            "kHealing": 10
        }
    },
    {
        "id": 8205,
        "name": "The Incontestable Spellslinger",
        "majorChangePatchVersion": "",
        "tooltip": "<pathSorcery>Sorcery</pathSorcery> + <pathPrecision>Precision</pathPrecision><br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD><br>+0% Attack Speed",
        "shortDesc": "<pathBonus><pathSorcery>Sorcery</pathSorcery> + <pathPrecision>Precision</pathPrecision> Set Bonus</pathBonus>",
        "longDesc": "+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>+0% Attack Speed",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8437,
        "name": "Grasp of the Undying",
        "majorChangePatchVersion": "",
        "tooltip": "Every 4s in combat, your next basic attack on a champion will:<li>Deal bonus magic damage equal to 3.5% of your max health</li><li>Heals you for 3 + 1.2% of your max health</li><li>Permanently increase your health by 7</li><br><rules><i>Ranged Champions:</i> Damage, healing, and permanent health gained reduced by 40%.</rules><br><br>Max Health gained: <scaleHealth>@f4@</scaleHealth><br>Damage to Champions: <scaleHealth>@f1@</scaleHealth><br>Total Healing: <scaleHealth>@f2@</scaleHealth><br>Times Used: @f3@",
        "shortDesc": "Every 4s your next attack on a champion deals bonus magic damage, heals you, and permanently increases your health.",
        "longDesc": "Every 4s in combat, your next basic attack on a champion will:<li>Deal bonus magic damage equal to 3.5% of your max health</li><li>Heals you for 3 + 1.2% of your max health</li><li>Permanently increase your health by 7</li><br><rules><i>Ranged Champions:</i> Damage, healing, and permanent health gained reduced by 40%.</rules><br>",
        "recommendationDescriptor": "Drain Opponents",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/GraspOfTheUndying/GraspOfTheUndying.png",
        "endOfGameStatDescs": [
            "Total damage: @eogvar1@",
            "Total Healing: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 9923,
        "name": "Hail of Blades",
        "majorChangePatchVersion": "8.11",
        "tooltip": "Gain @f3@% Attack Speed when you attack an enemy champion for up to 3 attacks. <br><br>Cooldown: 12s.<br><hr><br>Hail of Blades attacks: @f1@<br>Percentage of Hail attacks landed: @f2@%<br><br><rules>Basic Attack resets increase the attack limit by 1.<br>Allows you to temporarily exceed the attack speed limit.</rules>",
        "shortDesc": "Gain a large amount of Attack Speed for the first 3 attacks made against enemy champions.",
        "longDesc": "Gain 110% Attack Speed when you attack an enemy champion for up to 3 attacks.<br><br>No more than 3s can elapse between attacks or this effect will end.<br><br>Cooldown: 12s.<br><br><rules>Attack resets increase the attack limit by 1.<br>Allows you to temporarily exceed the attack speed limit.</rules>",
        "recommendationDescriptor": "Flurry of Attacks",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/HailOfBlades/HailOfBlades.png",
        "endOfGameStatDescs": [
            "Attacks made with extra attack speed: @eogvar1@",
            "Percentage of Hail attacks landed: @eogvar2@%"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8429,
        "name": "Conditioning",
        "majorChangePatchVersion": "9.9",
        "tooltip": "After 12 min gain +8 Armor and +8 Magic Resist and increase your bonus Armor and Magic Resist by 3%.<br><br>Armor Gained: @f3@ <scaleArmor>(+@f4@)</scaleArmor><br>Resist Gained: @f5@ <scaleMR>(+@f6@)</scaleMR>",
        "shortDesc": "After 12 min gain +8 Armor and +8 Magic Resist and increase your bonus Armor and Magic Resist by 3%.",
        "longDesc": "After 12 min gain +8 Armor and +8 Magic Resist and increase your bonus Armor and Magic Resist by 3%.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/Conditioning/Conditioning.png",
        "endOfGameStatDescs": [
            "Percent of game active: @eogvar1@%",
            "Total Bonus Armor: @eogvar2@",
            "Total Bonus Magic Resist: @eogvar3@"
        ],
        "recommendationDescriptorAttributes": {
            "kDurability": 10
        }
    },
    {
        "id": 8124,
        "name": "Predator",
        "majorChangePatchVersion": "",
        "tooltip": "Enchants your boots with the active effect <font color='#c60300'>Predator</font>.<br><br>Gain increased <speed>Move Speed</speed>, ramping up to <speed>@MaxMSLevelCalc@ Move Speed</speed> over 1.5 seconds, while chasing enemy champions. Damaging attacks or abilities to champions end this effect, dealing <scaleLevel>@f3@</scaleLevel> <scaleAP>(+@f5@)</scaleAP> <scaleAD>(+@f4@)</scaleAD> bonus damage. <br><br>Cooldown: <scaleLevel>@f7@</scaleLevel>s<br><hr><br>Damage Dealt To Champions: @f1@",
        "shortDesc": "Add an active effect to your boots that grants a large boost of <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_MS'>MS</lol-uikit-tooltipped-keyword> and causes your next attack or ability to deal bonus <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'>adaptive damage</lol-uikit-tooltipped-keyword>.",
        "longDesc": "Enchants your boots with the active effect '<font color='#c60300'>Predator</font>.'<br><br>Gain increased Move Speed, ramping up to 25-50% Move Speed over 1 second, while chasing enemy champions. After ramping up, damaging attacks or abilities to champions end this effect, dealing 20-180 (+<scaleAD>0.25</scaleAD> bonus AD)(+<scaleAP>0.15</scaleAP> AP) bonus <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'><font color='#48C4B7'>adaptive damage</font></lol-uikit-tooltipped-keyword>.<br><br>Cooldown: 120s-60s.",
        "recommendationDescriptor": "Out of Combat Movement",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/Predator/Predator.png",
        "endOfGameStatDescs": [
            "Total Damage to Champions: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8233,
        "name": "Absolute Focus",
        "majorChangePatchVersion": "",
        "tooltip": "While above 70% health, gain an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of up to 18 Attack Damage or 30 Ability Power (based on level). <br><br>Grants 1.8 Attack Damage or 3 Ability Power at level 1. <br><hr><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD>",
        "shortDesc": "While above 70% health, gain extra <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'>adaptive damage</lol-uikit-tooltipped-keyword>.",
        "longDesc": "While above 70% health, gain an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of up to 18 Attack Damage or 30 Ability Power (based on level). <br><br>Grants 1.8 Attack Damage or 3 Ability Power at level 1. ",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/AbsoluteFocus/AbsoluteFocus.png",
        "endOfGameStatDescs": [
            "Total time active: @eogvar1@:@eogvar2@"
        ],
        "recommendationDescriptorAttributes": {
            "kBurstDamage": 5,
            "kDamagePerSecond": 5
        }
    },
    {
        "id": 8007,
        "name": "The Savant",
        "majorChangePatchVersion": "",
        "tooltip": "<pathPrecision>Precision</pathPrecision> + <pathInspiration>Inspiration</pathInspiration><br>+0% Attack Speed",
        "shortDesc": "<pathBonus><pathPrecision>Precision</pathPrecision> + <pathInspiration>Inspiration</pathInspiration> Set Bonus</pathBonus>",
        "longDesc": "+0% Attack Speed",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8136,
        "name": "Zombie Ward",
        "majorChangePatchVersion": "8.14",
        "tooltip": "<lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>Takedowns</lol-uikit-tooltipped-keyword> on enemy Wards cause friendly Zombie Wards to sprout from their corpses.<br><br>Gain an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 1.2 Attack Damage or 2 Ability Power for every Zombie Ward spawned, up to 10. <br><br>After spawning 10 Zombie Wards, additionally gain 10 adaptive force.<br><br>Zombie Wards are visible, last for 120s and do not count towards your ward limit.<br><hr><br>Stats Gained: <scaleAD>+@f2@ Attack Damage</scaleAD><br>Zombie Wards raised: @f1@",
        "shortDesc": "<lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>Takedowns</lol-uikit-tooltipped-keyword> on enemy Wards cause friendly Zombie Wards to sprout from their corpses. Gain permanent AD or AP, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'>adaptive</lol-uikit-tooltipped-keyword> for each Zombie Ward spawned plus bonus upon completion.",
        "longDesc": "<lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Takedown'>Takedowns</lol-uikit-tooltipped-keyword> on enemy Wards cause friendly Zombie Wards to sprout from their corpses.<br><br>Gain an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 1.2 Attack Damage or 2 Ability Power for every Zombie Ward spawned, up to 10. <br><br>After spawning 10 Zombie Wards, additionally gain 10 adaptive force.<br><br>Zombie Wards are visible, last for 120s and do not count towards your ward limit.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Domination/ZombieWard/ZombieWard.png",
        "endOfGameStatDescs": [
            "Wards spawned: @eogvar1@",
            "Adaptive Force Gained: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {
            "kUtility": 10
        }
    },
    {
        "id": 8208,
        "name": "The Ancient One",
        "majorChangePatchVersion": "",
        "tooltip": "<pathSorcery>Sorcery</pathSorcery> + <pathResolve>Resolve</pathResolve><br>+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>Current Bonus: <scaleAD>+@f1@ <scaleAD>Attack Damage</scaleAD></scaleAD><br>+0-0 Health based on level",
        "shortDesc": "<pathBonus><pathSorcery>Sorcery</pathSorcery> + <pathResolve>Resolve</pathResolve> Set Bonus</pathBonus>",
        "longDesc": "+0 Attack Damage or +0 Ability Power, <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>Adaptive</font></lol-uikit-tooltipped-keyword><br>+0-0 Health based on level",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8347,
        "name": "Cosmic Insight",
        "majorChangePatchVersion": "",
        "tooltip": "+<attention>18</attention> Summoner Spell Haste<br>+<attention>10</attention> Item Haste",
        "shortDesc": "+<attention>18</attention> Summoner Spell Haste<br>+<attention>10</attention> Item Haste",
        "longDesc": "+<attention>18</attention> Summoner Spell Haste<br>+<attention>10</attention> Item Haste",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Inspiration/CosmicInsight/CosmicInsight.png",
        "endOfGameStatDescs": [
            "--"
        ],
        "recommendationDescriptorAttributes": {
            "kCooldown": 10
        }
    },
    {
        "id": 8472,
        "name": "Chrysalis",
        "majorChangePatchVersion": "8.6",
        "tooltip": "Start the game with 40 bonus health. When you get 4 takedowns, convert that health for an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 6 Attack Damage or 10 Ability Power.<br><hr><br>Takedowns: @f1@/@f2@<br>Health Given: @f3@<br>Bonus <scaleAD>Attack Damage</scaleAD> Given: @f4@",
        "shortDesc": "Start the game with 40 bonus health. When you get 4 takedowns, convert that health for an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 6 Attack Damage or 10 Ability Power.",
        "longDesc": "Start the game with 40 bonus health. When you get 4 takedowns, convert that health for an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 6 Attack Damage or 10 Ability Power.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Resolve/Chrysalis/Chrysalis.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8229,
        "name": "Arcane Comet",
        "majorChangePatchVersion": "",
        "tooltip": "Damaging a champion with an ability hurls a comet at their location, or, if Arcane Comet is on cooldown, reduces its remaining cooldown.<br><rules><br>Cooldown Reduction:<br>Single Target: 20%.<br>Area of Effect: 10%.<br>Damage over Time: 5%.<br></rules><br>Damage: <font color='#FFFFFF'>@f5@</font> (+<scaleAP>@f6@</scaleAP>) (+<scaleAD>@f7@</scaleAD>)<br>Cooldown: @f2@s<br><hr><br>You have hit with @f3@% of comets fired, for a total of @f1@ damage to champions.",
        "shortDesc": "Damaging a champion with an ability hurls a damaging comet at their location.",
        "longDesc": "Damaging a champion with an ability hurls a comet at their location, or, if Arcane Comet is on cooldown, reduces its remaining cooldown.<br><br><lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'><font color='#48C4B7'>Adaptive Damage</font></lol-uikit-tooltipped-keyword>: 30 - 130 based on level (<scaleAP>+0.05 AP</scaleAP> and <scaleAD>+0.1 bonus AD</scaleAD>)<br>Cooldown: 20 - 8s<br><rules><br>Cooldown Reduction:<br>Single Target: 20%.<br>Area of Effect: 10%.<br>Damage over Time: 5%.<br></rules>",
        "recommendationDescriptor": "Ability Damage",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Sorcery/ArcaneComet/ArcaneComet.png",
        "endOfGameStatDescs": [
            "Total Damage Dealt: @eogvar1@"
        ],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 8344,
        "name": "The Elegant Duelist ",
        "majorChangePatchVersion": "",
        "tooltip": "<pathInspiration>Inspiration</pathInspiration> + <pathPrecision>Precision</pathPrecision><br>+0% Attack Speed",
        "shortDesc": "<pathBonus><pathInspiration>Inspiration</pathInspiration> + <pathPrecision>Precision</pathPrecision> Set Bonus</pathBonus>",
        "longDesc": "+0% Attack Speed",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/RunesIcon.png",
        "endOfGameStatDescs": [],
        "recommendationDescriptorAttributes": {}
    },
    {
        "id": 9101,
        "name": "Overheal",
        "majorChangePatchVersion": "",
        "tooltip": "Excess healing on you becomes a shield for up to <scaleLevel>@OverhealShieldCap@</scaleLevel> Health.<br><br>Shield is built up from <scaleLevel>@f6@%</scaleLevel> of excess healing from yourself or any ally.<br><hr><br><b>Total damage blocked: <scaleAD>@f1@</scaleAD></b>",
        "shortDesc": "Excess healing on you becomes a shield.",
        "longDesc": "Excess healing on you becomes a shield for 11% of your max Health.<br><br>Shield is built up from 20 to 100% of excess healing from yourself or any ally.",
        "recommendationDescriptor": "",
        "iconPath": "/lol-game-data/assets/v1/perk-images/Styles/Precision/Overheal.png",
        "endOfGameStatDescs": [
            "Total Shielding: @eogvar2@"
        ],
        "recommendationDescriptorAttributes": {
            "kDurability": 7,
            "kHealing": 3
        }
    }
]