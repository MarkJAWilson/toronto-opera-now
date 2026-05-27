import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# We compile data for all 15 companies in alphabetical order.
data = {
    "companies": [
        {
            "name": "Against the Grain Theatre",
            "abbreviation": "AtG",
            "website": "https://atgtheatre.com/",
            "status": "Active",
            "description": "Against the Grain Theatre is a Canadian opera company dedicated to presenting genre-bending, boundary-breaking operatic and vocal works, making opera accessible in relaxed, friendly venues.",
            "socials": {
                "twitter": "http://www.twitter.com/AtGtheatre",
                "facebook": "http://www.facebook.com/AtGtheatre",
                "instagram": "http://www.instagram.com/AtGtheatre",
                "youtube": "http://www.youtube.com/AtGtheatre"
            },
            "productions": [
                {
                    "title": "Opera Pub (Pride Edition)",
                    "composer": "Various / Operatic Highlights",
                    "date": "June 22, 2026",
                    "time": "7:00 PM",
                    "isoStart": "2026-06-22T19:00:00",
                    "isoEnd": "2026-06-22T21:00:00",
                    "venue": "TRANZAC Club",
                    "address": "292 Brunswick Ave, Toronto, ON M5S 2M6",
                    "ticketLink": "https://atgtheatre.com/upcoming/opera-pub/",
                    "imageLink": "https://atgtheatre.com/wp-content/uploads/2025/10/Opera-Pub-Logo-AtG-Red-300x300.png",
                    "price": "Free Admission (Pay what you can / Buy a beer)",
                    "description": "Against the Grain Theatre's signature Opera Pub returns to the TRANZAC for the Pride Edition! Experience live opera with a beer in hand, featuring talented singers in a relaxed, friendly environment. Perfect introduction for newcomers and a welcome break for opera veterans.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "Amplified Opera",
            "abbreviation": "Amplified",
            "website": "https://www.amplifiedopera.com/",
            "status": "Inactive/No Upcoming Shows",
            "description": "Amplified Opera is a Toronto-based collective that places artists at the center of public discourse. They foster equity, inclusivity, and representation in classical music, creating a space for marginalized and equity-seeking creators to push the boundaries of the art form.",
            "socials": {
                "twitter": "https://x.com/AmplifiedOpera",
                "facebook": "https://www.facebook.com/AmplifiedOpera",
                "instagram": "https://www.instagram.com/amplifiedopera/"
            },
            "productions": []
        },
        {
            "name": "Apocryphonia",
            "abbreviation": "Apocryphonia",
            "website": "https://apocryphonia.com/",
            "status": "Active",
            "description": "Apocryphonia Concert Series explores forgotten, neglected, and contemporary musical works, presenting unique, immersive chamber music experiences in Toronto.",
            "socials": {
                "instagram": "https://www.instagram.com/apocryphonia/",
                "facebook": "https://www.facebook.com/Apocryphonia/"
            },
            "productions": [
                {
                    "title": "Of Whales and Willpower: The Jamaican Jonah, Pt. 1",
                    "composer": "Samuel Felsted / Various Heritage Composers",
                    "date": "June 12, 2026",
                    "time": "7:00 PM - 9:00 PM",
                    "isoStart": "2026-06-12T19:00:00",
                    "isoEnd": "2026-06-12T21:00:00",
                    "venue": "Christ Church Deer Park",
                    "address": "1570 Yonge Street, Toronto, ON M4T 1Z8",
                    "ticketLink": "https://www.eventbrite.ca/e/of-whales-and-willpower-the-jamaican-jonah-pt-1-tickets-1501714882639",
                    "imageLink": "https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F1185050450%2F404331086101%2F1%2Foriginal.20260520-160123?crop=focalpoint&fit=crop&w=600&auto=format%2Ccompress&q=75&sharp=10&fp-x=0.843&fp-y=0.221&s=bbabd7d36acfa5960f501f145c5b713a",
                    "price": "Paid Tickets ($20 - $35)",
                    "description": "A journey through classical organ works by composers of Jamaican and West Indian heritage, spanning from the Baroque era to the present day. Emerging Jamaican-Canadian organist Joshua Duncan-Lee premieres works by Jamaica's first classical composer, Samuel Felsted, including excerpts of the 1775 oratorio 'Jonah'—the first oratorio written in the Western Hemisphere.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "Benevolence Opera Project",
            "abbreviation": "BOP",
            "website": "https://theredwoodtheatre.com/",
            "status": "Inactive/No Upcoming Shows",
            "description": "Founded by Artistic Director Ryan Hofman, the Benevolence Opera Project is dedicated to producing high-quality opera performances that combine artistic excellence with community engagement and support for meaningful causes.",
            "socials": {
                "facebook": "https://www.facebook.com/theredwoodtheatre"
            },
            "productions": [
                {
                    "title": "Don Giovanni",
                    "composer": "Wolfgang Amadeus Mozart",
                    "date": "May 22, 2026",
                    "time": "7:30 PM",
                    "isoStart": "2026-05-22T19:30:00",
                    "isoEnd": "2026-05-22T22:30:00",
                    "venue": "The Redwood Theatre",
                    "address": "1300 Gerrard St E, Toronto, ON M4L 1Y7",
                    "ticketLink": "https://www.theredwoodtheatre.com/event-details/don-giovanni",
                    "imageLink": "assets/images/don_giovanni.jpg",
                    "price": "Tickets from $30 (Redwood Shelter Fundraiser)",
                    "description": "Mozart's masterpiece presented as a one-night-only community fundraiser. Partnering with the Redwood Theatre to raise funds and awareness for the Redwood Women's Shelter.",
                    "status": "Passed"
                }
            ]
        },
        {
            "name": "Canadian Children's Opera Company",
            "abbreviation": "CCOC",
            "website": "https://www.canadianchildrensopera.com/",
            "status": "Active",
            "description": "The CCOC provides unique operatic training and performance opportunities for children and youth, producing professional-level staged operas and collaborating regularly with the Canadian Opera Company.",
            "socials": {
                "twitter": "https://twitter.com/operakidscanada?lang=en",
                "facebook": "https://www.facebook.com/canadianchildrensopera",
                "instagram": "https://www.instagram.com/canadianchildrensopera/",
                "youtube": "https://www.youtube.com/channel/UCZABBXZt36AqIWJufaxg6ww"
            },
            "productions": [
                {
                    "title": "Phantom of the Music Room",
                    "composer": "Janet Gardner",
                    "date": "May 31, 2026",
                    "time": "Afternoon Performance",
                    "isoStart": "2026-05-31T14:00:00",
                    "isoEnd": "2026-05-31T15:30:00",
                    "venue": "Canadian Children's Opera Company",
                    "address": "227 Front St. E. Toronto, ON M5A 1E8",
                    "ticketLink": "https://www.eventbrite.ca/e/the-phantom-of-the-music-room-tickets-1988832553706?aff=oddtdtcreator",
                    "imageLink": "https://www.canadianchildrensopera.com/wp-content/uploads/2022/11/CCOC_Full_NoDate.png",
                    "price": "Paid Tickets ($15 - $25)",
                    "description": "Presented by the CCOC Junior Division, this is a 30-minute musical mystery filled with clever songs set to classical melodies by Chopin, Dvořák, Sousa, and more. Join the young choristers as they solve the mysteries hidden in their school music room in this imaginative, family-friendly staging.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "Canadian Opera Company",
            "abbreviation": "COC",
            "website": "https://www.coc.ca/",
            "status": "Active",
            "description": "Based in Toronto, the Canadian Opera Company is the largest opera company in Canada and one of the largest producers of opera in North America, performing in the state-of-the-art Four Seasons Centre.",
            "socials": {
                "twitter": "https://twitter.com/CanadianOpera",
                "facebook": "https://www.facebook.com/CanadianOperaCompany",
                "instagram": "https://www.instagram.com/canadianopera/",
                "youtube": "https://www.youtube.com/user/CanadianOperaCompany"
            },
            "productions": [
                {
                    "title": "La Traviata",
                    "composer": "Giuseppe Verdi",
                    "date": "September 18 - October 17, 2026",
                    "time": "7:30 PM (Sundays at 2:00 PM)",
                    "isoStart": "2026-09-18T19:30:00",
                    "isoEnd": "2026-10-17T22:30:00",
                    "venue": "Four Seasons Centre for the Performing Arts",
                    "address": "145 Queen St W, Toronto, ON M5H 4G1",
                    "ticketLink": "https://www.coc.ca/tickets/2627-season/la-traviata",
                    "imageLink": "https://res.cloudinary.com/dpaedgweb/image/upload/c_fill,g_auto,h_342,w_410/f_auto/q_auto/v1770227736/COC2627_Social_LaTraviata_1920x1080?_a=BAAASyDQ",
                    "price": "Tickets from $35",
                    "description": "One of opera's most beloved tragedies. Verdi's exquisite portrait of a glamorous courtesan sacrifice in Paris. Led by an international cast and spectacular staging at the Four Seasons Centre.",
                    "status": "Upcoming"
                },
                {
                    "title": "Così fan tutte",
                    "composer": "Wolfgang Amadeus Mozart",
                    "date": "October 3 - 18, 2026",
                    "time": "7:30 PM (Sundays at 2:00 PM)",
                    "isoStart": "2026-10-03T19:30:00",
                    "isoEnd": "2026-10-18T22:30:00",
                    "venue": "Four Seasons Centre for the Performing Arts",
                    "address": "145 Queen St W, Toronto, ON M5H 4G1",
                    "ticketLink": "https://www.coc.ca/tickets/2627-season/cosi-fan-tutte",
                    "imageLink": "https://res.cloudinary.com/dpaedgweb/image/upload/c_fill,g_auto,h_342,w_410/f_auto/q_auto/v1770227736/COC2627_Social_CosiFanTutte_1920x1080?_a=BAAASyDQ",
                    "price": "Tickets from $35",
                    "description": "Mozart's sparkling, witty comedy exploring fidelity, deception, and human relationships in a stunning classical production filled with unforgettable ensembles.",
                    "status": "Upcoming"
                },
                {
                    "title": "The Turn of the Screw",
                    "composer": "Benjamin Britten",
                    "date": "January 23 - February 17, 2027",
                    "time": "7:30 PM (Sundays at 2:00 PM)",
                    "isoStart": "2027-01-23T19:30:00",
                    "isoEnd": "2027-02-17T22:00:00",
                    "venue": "Four Seasons Centre for the Performing Arts",
                    "address": "145 Queen St W, Toronto, ON M5H 4G1",
                    "ticketLink": "https://www.coc.ca/tickets/2627-season/the-turn-of-the-screw",
                    "imageLink": "https://res.cloudinary.com/dpaedgweb/image/upload/c_fill,g_auto,h_342,w_410/f_auto/q_auto/v1770227736/COC2627_Social_TurnOfTheScrew_1920x1080?_a=BAAASyDQ",
                    "price": "Tickets from $35",
                    "description": "Britten's spine-chilling chamber masterpiece based on Henry James's classic ghost story. A tense psychological thriller exploring isolation and the corruption of innocence.",
                    "status": "Upcoming"
                },
                {
                    "title": "Ariadne auf Naxos",
                    "composer": "Richard Strauss",
                    "date": "February 4 - 20, 2027",
                    "time": "7:30 PM (Sundays at 2:00 PM)",
                    "isoStart": "2027-02-04T19:30:00",
                    "isoEnd": "2027-02-20T22:00:00",
                    "venue": "Four Seasons Centre for the Performing Arts",
                    "address": "145 Queen St W, Toronto, ON M5H 4G1",
                    "ticketLink": "https://www.coc.ca/tickets/2627-season/ariadne-auf-naxos",
                    "imageLink": "https://res.cloudinary.com/dpaedgweb/image/upload/c_fill,g_auto,h_342,w_410/f_auto/q_auto/v1770227736/COC2627_Social_AriadneAufNaxos_1920x1080?_a=BAAASyDQ",
                    "price": "Tickets from $35",
                    "description": "A delightful mash-up of high art opera and low-brow commedia dell'arte comedy, featuring one of the most vocally demanding soprano roles in the entire repertoire.",
                    "status": "Upcoming"
                },
                {
                    "title": "Empire of Wild",
                    "composer": "Ian Cusson / Cherie Dimaline",
                    "date": "May 1 - 21, 2027",
                    "time": "7:30 PM (Sundays at 2:00 PM)",
                    "isoStart": "2027-05-01T19:30:00",
                    "isoEnd": "2027-05-21T22:00:00",
                    "venue": "Four Seasons Centre for the Performing Arts",
                    "address": "145 Queen St W, Toronto, ON M5H 4G1",
                    "ticketLink": "https://www.coc.ca/tickets/2627-season/empire-of-wild",
                    "imageLink": "https://res.cloudinary.com/dpaedgweb/image/upload/c_fill,g_auto,h_342,w_410/f_auto/q_auto/v1770227736/COC2627_Social_EmpireOfWild_1920x1080?_a=BAAASyDQ",
                    "price": "Tickets from $35",
                    "description": "World Premiere. A powerful new Canadian opera based on Cherie Dimaline's bestselling novel, weaving Métis folklore of the Rogarou with a story of love, loss, and community resilience.",
                    "status": "Upcoming"
                },
                {
                    "title": "The Elixir of Love",
                    "composer": "Gaetano Donizetti",
                    "date": "May 8 - 29, 2027",
                    "time": "7:30 PM (Sundays at 2:00 PM)",
                    "isoStart": "2027-05-08T19:30:00",
                    "isoEnd": "2027-05-29T22:00:00",
                    "venue": "Four Seasons Centre for the Performing Arts",
                    "address": "145 Queen St W, Toronto, ON M5H 4G1",
                    "ticketLink": "https://www.coc.ca/tickets/2627-season/the-elixir-of-love",
                    "imageLink": "https://res.cloudinary.com/dpaedgweb/image/upload/c_fill,g_auto,h_342,w_410/f_auto/q_auto/v1770227736/COC2627_Social_ElixirOfLove_1920x1080?_a=BAAASyDQ",
                    "price": "Tickets from $35",
                    "description": "Donizetti's charming and funny romantic comedy, boasting some of the composer's most famous tunes including 'Una furtiva lagrima'. Perfect for opera beginners.",
                    "status": "Upcoming"
                },
                {
                    "title": "Come Closer",
                    "composer": "Ryan Trew / Rachel Krehm",
                    "date": "June 18 - 20, 2027",
                    "time": "8:00 PM",
                    "isoStart": "2027-06-18T20:00:00",
                    "isoEnd": "2027-06-20T22:00:00",
                    "venue": "Canadian Opera Company Theatre",
                    "address": "227 Front St E, Toronto, ON M5A 1E8",
                    "ticketLink": "https://www.coc.ca/tickets/2627-season/come-closer",
                    "imageLink": "https://res.cloudinary.com/dpaedgweb/image/upload/c_fill,g_auto,h_342,w_410/f_auto/q_auto/v1770227737/COC2627_Social_ComeCloser_1920x1080?_a=BAAASyDQ",
                    "price": "Tickets from $40",
                    "description": "An intimate, contemporary production staged at the COC Theatre, exploring memory, connection, and the spaces between us in a modern operatic language.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "Fawn Chamber Creative",
            "abbreviation": "FAWN",
            "website": "https://www.fawnchambercreative.com/",
            "status": "Inactive/No Upcoming Shows",
            "description": "Exploring new directions in music, theater, and opera, FAWN Chamber Creative is a Toronto-based collective that produces multidisciplinary works, workshops, and immersive performance experiences.",
            "socials": {
                "facebook": "https://www.facebook.com/fawnchambercreative",
                "instagram": "https://www.instagram.com/fawnchambercreative/"
            },
            "productions": []  # Album release focus currently
        },
        {
            "name": "Opera 5",
            "abbreviation": "Opera 5",
            "website": "https://www.opera5.ca/",
            "status": "Active",
            "description": "Opera 5 is a Toronto-based opera company dedicated to producing funny, fast-paced, and engaging operatic experiences, bridging the gap between traditional theater and modern audiences.",
            "socials": {
                "twitter": "https://twitter.com/Opera5Opera",
                "facebook": "https://www.facebook.com/OperaFive",
                "instagram": "https://www.instagram.com/operafive/"
            },
            "productions": [
                {
                    "title": "Suor Angelica & Gianni Schicchi",
                    "composer": "Giacomo Puccini",
                    "date": "June 3 - 7, 2026",
                    "time": "7:30 PM (Sunday matinee at 2:00 PM)",
                    "isoStart": "2026-06-03T19:30:00",
                    "isoEnd": "2026-06-07T22:00:00",
                    "venue": "Toronto Opera Festival",
                    "address": "Toronto, ON (Venues TBA)",
                    "ticketLink": "https://www.opera5.ca/season2026",
                    "imageLink": "https://images.squarespace-cdn.com/content/v1/66900b857cbcd75ecec7aebb/73f7a236-661c-4538-9b6b-c035aa17cb7f/3.png",
                    "price": "Tickets from $25",
                    "description": "An intimate, fresh double bill of Puccini's masterworks Suor Angelica and Gianni Schicchi, featuring a new chamber reduction by Music Director Evan Mitchell. Directed by Jessica Derventzis, this production weaves rising talents with Canadian opera stars like Krisztina Szabó and Rachel Krehm.",
                    "status": "Upcoming"
                },
                {
                    "title": "Parḗlios",
                    "composer": "Cecilia Livingston / Duncan McFarlane",
                    "date": "June 12 - 14, 2026",
                    "time": "7:30 PM",
                    "isoStart": "2026-06-12T19:30:00",
                    "isoEnd": "2026-06-14T21:00:00",
                    "venue": "Toronto Opera Festival",
                    "address": "Toronto, ON (Venues TBA)",
                    "ticketLink": "https://www.opera5.ca/season2026",
                    "imageLink": "https://images.squarespace-cdn.com/content/v1/66900b857cbcd75ecec7aebb/414072b8-af94-4fa8-b885-1eaf3a3bf86a/Season+Announcement+Posters+Final.png",
                    "price": "Tickets from $25",
                    "description": "World Premiere of a bold new Canadian opera. Cecilia Livingston's haunting score merges opera, installation, and oratorio, featuring the TorQ Percussion Ensemble. Exploring themes of survival, light, and mathematical symmetry.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "Opera Atelier",
            "abbreviation": "OA",
            "website": "https://www.operaatelier.com/",
            "status": "Active",
            "description": "Opera Atelier is Canada's premier baroque opera company, specializing in historically informed, spectacular productions featuring period dancing, acting, and music in Toronto.",
            "socials": {
                "twitter": "https://twitter.com/operaatelier",
                "facebook": "https://www.facebook.com/OperaAtelier",
                "instagram": "https://www.instagram.com/operaatelier/"
            },
            "productions": [
                {
                    "title": "The Descent of Orpheus",
                    "composer": "Marc-Antoine Charpentier",
                    "date": "October 22 - 25, 2026",
                    "time": "7:30 PM (Sunday matinee at 2:30 PM)",
                    "isoStart": "2026-10-22T19:30:00",
                    "isoEnd": "2026-10-25T21:30:00",
                    "venue": "Koerner Hall",
                    "address": "273 Bloor St W, Toronto, ON M5S 1W2",
                    "ticketLink": "https://www.operaatelier.com/",
                    "imageLink": "https://www.operaatelier.com/wp-content/uploads/2026/02/OA-Cover-Page-1-ChestTONE-e1770842437615-636x405.jpg",
                    "price": "Tickets from $45",
                    "description": "Fully staged Canadian Premiere of Charpentier's baroque masterwork 'La descente d'Orphée aux enfers'. Converted into a rich period experience featuring American tenor Daniel McGrew in his Opera Atelier debut as Orpheus and soprano Mireille Asselin as Eurydice. Conducted by Christopher Bagan and choreographed by Jeannette Lajeunesse Zingg.",
                    "status": "Upcoming"
                },
                {
                    "title": "The Resurrection",
                    "composer": "George Frideric Handel",
                    "date": "April 15 - 18, 2027",
                    "time": "7:30 PM (Sunday matinee at 2:30 PM)",
                    "isoStart": "2027-04-15T19:30:00",
                    "isoEnd": "2027-04-18T21:30:00",
                    "venue": "Koerner Hall",
                    "address": "273 Bloor St W, Toronto, ON M5S 1W2",
                    "ticketLink": "https://www.operaatelier.com/",
                    "imageLink": "https://www.operaatelier.com/wp-content/uploads/2026/02/Resurrection-Image-1-636x405.png",
                    "price": "Tickets from $45",
                    "description": "A welcome remount of Opera Atelier's critically acclaimed, multi-layered production of Handel's early Italian masterpiece 'La Resurrezione'. Led by music director David Fallis, featuring stunning scenery, dramatic period dance choreography, and an all-star Canadian cast.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "Opera by the Glass",
            "abbreviation": "OBTG",
            "website": "https://www.instagram.com/operabytheglass/",
            "status": "Inactive/No Upcoming Shows",
            "description": "Opera by the Glass is an active chamber opera company in the Greater Toronto Area, bringing classical vocal music to intimate, unconventional spaces.",
            "socials": {
                "instagram": "https://www.instagram.com/operabytheglass/"
            },
            "productions": []
        },
        {
            "name": "Opera Revue",
            "abbreviation": "Opera Revue",
            "website": "https://operarevue.com/",
            "status": "Active",
            "description": "Opera Revue makes opera accessible, fun, and casual by performing high-quality opera in neighborhood bars, breweries, and lounges. They are known for their regular series at the Granite Brewery, themed events like Drag Me to the Opera, and cross-over mashups like OperaMANIA.",
            "socials": {
                "facebook": "https://www.facebook.com/operarevue",
                "instagram": "https://www.instagram.com/operarevue/"
            },
            "productions": [
                {
                    "title": "Drag Me to the Opera",
                    "composer": "Various / Cabaret Highlights",
                    "date": "June 25, 2026",
                    "time": "7:30 PM",
                    "isoStart": "2026-06-25T19:30:00",
                    "isoEnd": "2026-06-25T22:00:00",
                    "venue": "Granite Brewery",
                    "address": "245 Eglinton Ave E, Toronto, ON M4P 3B7",
                    "ticketLink": "https://operarevue.com/upcoming",
                    "imageLink": "assets/images/opera_revue.jpg",
                    "price": "Tickets: $25 (Early Bird)",
                    "description": "Opera Revue presents their hit show 'Drag Me to the Opera' at the Granite Brewery! Experience an incredible, high-energy collaboration blending classical opera arias with fabulous drag performances, hosted by Gregory Finney and starring drag sensation Selena Vyle.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "Opera York",
            "abbreviation": "Opera York",
            "website": "http://www.operayork.com/",
            "status": "Inactive/No Upcoming Shows",
            "description": "Serving York Region and northern Toronto, Opera York provides professional staged performance opportunities for emerging Canadian classical artists, presenting accessible and beautiful standard repertoire.",
            "socials": {
                "facebook": "https://www.facebook.com/OperaYork"
            },
            "productions": []
        },
        {
            "name": "Southern Ontario Lyric Opera",
            "abbreviation": "SOLO",
            "website": "https://southernontariolyricopera.com/",
            "status": "Active",
            "description": "Southern Ontario Lyric Opera (SOLO) is a professional opera company based in Burlington and Hamilton, dedicated to presenting classic operatic works, highlighting local talents and educational programs.",
            "socials": {
                "facebook": "https://www.facebook.com/southernontariolyricopera/",
                "instagram": "https://www.instagram.com/southernontariolyricopera/"
            },
            "productions": [
                {
                    "title": "An outdoor Concert under the Stars",
                    "composer": "Various / Operatic Highlights",
                    "date": "June 12, 2026",
                    "time": "8:30 PM - 10:00 PM",
                    "isoStart": "2026-06-12T20:30:00",
                    "isoEnd": "2026-06-12T22:00:00",
                    "venue": "Hamilton Italian Heritage Month",
                    "address": "420 Crerar Dr, Hamilton, ON L9A 5K3, Canada",
                    "ticketLink": "https://southernontariolyricopera.com/event/an-outdoor-concert-under-the-stars/",
                    "imageLink": "https://southernontariolyricopera.com/wp-content/uploads/2024/10/cropped-solo_red_banner.png",
                    "price": "Free / Community Event",
                    "description": "Celebrate Italian Heritage Month with Southern Ontario Lyric Opera! An outdoor summer evening concert under the stars featuring beloved operatic selections, aria favorites, and classic ensembles. (Rain date scheduled for Friday, June 19th).",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "Summer Opera Lyric Theatre",
            "abbreviation": "SOLT",
            "website": "https://www.solt.ca/",
            "status": "Active",
            "description": "For over 40 years, Summer Opera Lyric Theatre has provided intensive professional training for emerging singer-actors, presenting staged productions in an intimate summer festival setting.",
            "socials": {
                "twitter": "https://twitter.com/OperaSOLT",
                "facebook": "https://www.facebook.com/summeroperalyrictheatre",
                "instagram": "https://www.instagram.com/summeroperatoronto/"
            },
            "productions": [
                {
                    "title": "The Medium",
                    "composer": "Gian Carlo Menotti",
                    "date": "July 24 - August 1, 2026",
                    "time": "July 24 @ 8:00pm, July 29 @ 2:00pm, July 30 @ 8:00pm, August 1 @ 8:00pm",
                    "isoStart": "2026-07-24T20:00:00",
                    "isoEnd": "2026-08-01T22:00:00",
                    "venue": "Alumnae Theatre",
                    "address": "70 Berkeley Street, Toronto, ON M5A 2W6",
                    "ticketLink": "https://www.solt.ca/performances",
                    "imageLink": "assets/images/the_medium.png",
                    "price": "Tickets: $28 (Seniors/Students $22)",
                    "description": "A gripping two-act dramatic chamber opera exploring the supernatural, fraud, and psychological breakdown. Conducted by Vlad Soloviev and featuring SOLT's new generation of operatic talents.",
                    "status": "Upcoming"
                },
                {
                    "title": "The Importance of Being Earnest",
                    "composer": "Victor Davies / Eugene Benson (after Oscar Wilde)",
                    "date": "July 25 - 31, 2026",
                    "time": "July 25 @ 2:00pm, July 26 @ 2:00pm, July 29 @ 8:00pm, July 31 @ 8:00pm",
                    "isoStart": "2026-07-25T14:00:00",
                    "isoEnd": "2026-07-31T22:00:00",
                    "venue": "Alumnae Theatre",
                    "address": "70 Berkeley Street, Toronto, ON M5A 2W6",
                    "ticketLink": "https://www.solt.ca/performances",
                    "imageLink": "assets/images/earnest.png",
                    "price": "Tickets: $28 (Seniors/Students $22)",
                    "description": "Oscar Wilde's legendary comedy of manners is brilliantly adapted into a witty, melodic opera by Victor Davies and Eugene Benson. A delightful musical romp through high-society double lives.",
                    "status": "Upcoming"
                },
                {
                    "title": "Katya Kabanova",
                    "composer": "Leoš Janáček",
                    "date": "July 25 - August 2, 2026",
                    "time": "July 25 @ 8:00pm, July 28 @ 8:00pm, August 1 @ 2:00pm, August 2 @ 2:00pm",
                    "isoStart": "2026-07-25T20:00:00",
                    "isoEnd": "2026-08-02T16:00:00",
                    "venue": "Alumnae Theatre",
                    "address": "70 Berkeley Street, Toronto, ON M5A 2W6",
                    "ticketLink": "https://www.solt.ca/performances",
                    "imageLink": "assets/images/katya_kabanova.png",
                    "price": "Tickets: $28 (Seniors/Students $22)",
                    "description": "Janáček's heartbreaking masterwork of oppression, forbidden passion, and tragic fate on the Volga River. Presented in an intimate, powerful staging under music director Minira Najafzade.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "Tapestry Opera",
            "abbreviation": "Tapestry",
            "website": "https://tapestryopera.com/",
            "status": "Active",
            "description": "Tapestry Opera is an award-winning Canadian opera company based in Toronto, dedicated to creating, developing, and producing modern, boundary-pushing contemporary operas.",
            "socials": {
                "twitter": "https://twitter.com/TapestryOpera",
                "facebook": "https://www.facebook.com/TapestryOpera",
                "instagram": "https://www.instagram.com/tapestryopera/"
            },
            "productions": [
                {
                    "title": "10 Days in a Madhouse",
                    "composer": "Rene Orth / Hannah Moscovitch",
                    "date": "June 16, 18, 20, & 21, 2026",
                    "time": "June 16 & 18 at 7:30 PM, June 20 at 3:30 PM, June 21 at 1:30 PM",
                    "isoStart": "2026-06-16T19:30:00",
                    "isoEnd": "2026-06-21T15:00:00",
                    "venue": "Bluma Appel Theatre",
                    "address": "St. Lawrence Centre for the Arts, 27 Front St E, Toronto, ON M5E 1B4",
                    "ticketLink": "https://www.luminatofestival.com/10-days-in-a-madhouse",
                    "imageLink": "https://tapestryopera.com/wp-content/uploads/2025/11/2025-Luminato_10-Days-in-Madhouse_A3_1080x1080.jpg",
                    "price": "Tickets from $30",
                    "description": "Co-presented with the Luminato Festival. A groundbreaking contemporary chamber opera exposing Nellie Bly's heroic, undercover exploration of a women's asylum. Written by librettist Hannah Moscovitch and composer Rene Orth.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "The Glenn Gould School",
            "abbreviation": "GGS",
            "website": "https://www.rcmusic.com/",
            "status": "Active",
            "description": "The vocal program of the Royal Conservatory's Glenn Gould School is an elite training ground for emerging opera artists, presenting fully staged operas accompanied by the Royal Conservatory Orchestra.",
            "socials": {
                "facebook": "https://www.facebook.com/royalconservatoryofmusic",
                "instagram": "https://www.instagram.com/theroyalconservatory/"
            },
            "productions": [
                {
                    "title": "The Glenn Gould School Spring Opera",
                    "composer": "TBA / Directed Performance",
                    "date": "March 17 & 19, 2027",
                    "time": "7:30 PM",
                    "isoStart": "2027-03-17T19:30:00",
                    "isoEnd": "2027-03-19T22:00:00",
                    "venue": "Koerner Hall",
                    "address": "273 Bloor St W, Toronto, ON M5S 1W2",
                    "ticketLink": "https://www.rcmusic.com/events/the-glenn-gould-school-spring-opera-430803",
                    "imageLink": "https://rcmusic-production-strapi-media.s3.ca-central-1.amazonaws.com/ggs_spring_opera_440x400_3_8114ae7aa3.png",
                    "price": "Tickets from $25",
                    "description": "Students from The Glenn Gould School’s vocal program present their fully staged annual opera in Koerner Hall, conducted by Judith Yan. Experience future classical stars supported by the prestigious Royal Conservatory Orchestra.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "Toronto City Opera",
            "abbreviation": "TCO",
            "website": "https://www.torontocityopera.com/",
            "status": "Active",
            "description": "Toronto City Opera (TCO) is a community-focused opera company in downtown Toronto, providing staged performances of standard and modern operatic works while engaging amateur and emerging singers.",
            "socials": {
                "facebook": "https://www.facebook.com/TorontoCityOpera",
                "instagram": "https://www.instagram.com/torontocityopera/",
                "youtube": "https://www.youtube.com/user/TorontoCityOpera"
            },
            "productions": [
                {
                    "title": "Orpheus in the Underworld",
                    "composer": "Jacques Offenbach",
                    "date": "June 27 & 28, 2026",
                    "time": "7:30 PM (Sunday matinee at 2:30 PM)",
                    "isoStart": "2026-06-27T19:30:00",
                    "isoEnd": "2026-06-28T22:00:00",
                    "venue": "Trinity St. Paul's Centre",
                    "address": "427 Bloor St W, Toronto, ON M5S 1X7",
                    "ticketLink": "https://www.torontocityopera.com/copy-of-2024-25-season",
                    "imageLink": "https://static.wixstatic.com/media/cad2c4_5c9551ef17bf4d4286a1eb5e9f5d2362~mv2.jpg/v1/fill/w_515,h_670,al_c,q_80,usm_0.66_1.00_0.01,enc_avif,quality_auto/4.jpg",
                    "price": "Tickets from $25",
                    "description": "Offenbach's sparkling, satirical operetta turns classic Greek myths on their head in a witty comedy. Featuring the famous 'Can-Can' melody, fully staged in English with the North York Concert Orchestra in the pit.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "Toronto Summer Music",
            "abbreviation": "TSM",
            "website": "https://torontosummermusic.com/",
            "status": "Active",
            "description": "Toronto Summer Music is an annual summer festival and academy presenting world-class chamber music and art song performances in Toronto's prestigious Koerner Hall.",
            "socials": {
                "facebook": "https://www.facebook.com/torontosummermusic/",
                "instagram": "https://www.instagram.com/torontosummermusic/",
                "twitter": "https://twitter.com/tosummermusic"
            },
            "productions": [
                {
                    "title": "La descente d'Orphée aux enfers & Les arts florissants",
                    "composer": "Marc-Antoine Charpentier",
                    "date": "July 9, 2026",
                    "time": "7:30 PM (includes post-show reception)",
                    "isoStart": "2026-07-09T19:30:00",
                    "isoEnd": "2026-07-09T22:30:00",
                    "venue": "Koerner Hall",
                    "address": "273 Bloor St W, Toronto, ON M5S 1W2",
                    "ticketLink": "https://torontosummermusic.com/event/opening-night-les-arts-florissants/",
                    "imageLink": "assets/images/les_arts_florissants.jpg",
                    "price": "Tickets: $30 - $120",
                    "description": "Toronto Summer Music Opening Night. Under the direction of William Christie, the legendary early music ensemble Les Arts Florissants performs a staged double-bill of Charpentier's baroque masterpieces: 'La descente d'Orphée aux enfers' and the chamber opera 'Les arts florissants'. Followed by a celebratory champagne reception.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "University of Toronto Opera",
            "abbreviation": "UofT Opera",
            "website": "https://uoftopera.ca",
            "status": "Active",
            "description": "The University of Toronto Faculty of Music's Opera division is one of Canada's premier training grounds for opera, offering comprehensive graduate performance training and presenting fully staged productions accompanied by the U of T Symphony Orchestra.",
            "socials": {
                "twitter": "https://twitter.com/uoftopera",
                "facebook": "https://www.facebook.com/UofTOpera",
                "instagram": "https://www.instagram.com/uoftopera/"
            },
            "productions": [
                {
                    "title": "Fall River, the legend of Lizzie Borden",
                    "composer": "Cecilia Livingston",
                    "date": "November 2026",
                    "time": "TBA (Reopening of MacMillan Theatre)",
                    "isoStart": "2026-11-19T19:30:00",
                    "isoEnd": "2026-11-22T22:00:00",
                    "venue": "MacMillan Theatre",
                    "address": "Edward Johnson Building, 80 Queen's Park, Toronto, ON M5S 2C5",
                    "ticketLink": "https://uoftopera.ca",
                    "imageLink": "assets/images/fall_river.png",
                    "price": "Tickets TBA",
                    "description": "The world premiere of Fall River, the legend of Lizzie Borden, with music by Cecilia Livingston and libretto/direction by Michael Patrick Albano. This major new commission marks the U of T Opera division's first commissioned work in twenty-five years, celebrating the reopening of the MacMillan Theatre.",
                    "status": "Upcoming"
                }
            ]
        },
        {
            "name": "Voicebox: Opera in Concert",
            "abbreviation": "Voicebox",
            "website": "http://www.operainconcert.com/",
            "status": "Inactive/No Upcoming Shows",
            "description": "Founded in 1974 by Stuart Hamilton, VOICEBOX: Opera in Concert is Canada's oldest voice-only opera company. It is dedicated to presenting rarely performed operatic masterpieces in a concert format, focusing on musical expression and emerging Canadian vocal talent.",
            "socials": {
                "facebook": "https://www.facebook.com/VOICEBOXOperainConcert/",
                "twitter": "https://x.com/operainconcert",
                "instagram": "https://www.instagram.com/voiceboxoperainconcert/"
            },
            "productions": []
        }
    ]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully compiled and wrote data.json!")
