import folium

# Key locations and their coordinates
locations = {
    "Troy": (40.1536, 26.4062),
    "Land of the Cicones": (40.1817, 26.2401),
    "Land of the Lotus Eaters": (33.9223, 18.4241),
    "Land of the Cyclopes": (37.0078, 25.2637),
    "Aeolia": (38.3983, 15.0895),
    "Laestrygonia": (38.1167, 15.6500),
    "Land of the Sirens": (38.7331, 15.4144),
    "Scylla and Charybdis": (38.1929, 15.3866),
    "Ithaca": (38.3623, 20.7183),
    "Aeaea": (38.3894, 14.9414), 
    "Thrinacia": (37.0179, 14.2915), 
    "Ogygia": (34.9734, 25.9543), 
    "Phaeacia": (37.3148, 20.5903)  
}

# Quotes, analysis, and importance for each location
location_info = {
    "Troy": {
        "quote": "'Now I have left the light of day, and am not there to help, as on the plains of Troy when I was killing the best Trojans, to help the Greeks.' (Od. 11-498-501)",
        "analysis": "The beginning of the epic, Troy marks the start of Odysseus' journey. Odysseus spent 10 years fighting on the side of the Greeks, eventually becoming one of their greatest warriors.",
        "importance": "Highlights the harships and challenges faced byOdysseus before the story of The Odyssey starts. Serves as a reminder of the epics theme of nostos (homecoming)."
    },
    "Land of the Cicones": {
        "quote": "'We reached the land of the Cicones, allied with Troy. We fought and sacked their city, killed the men, but as for all the wives and plunder, we took them, to divide them equally among us all.' (Od. 9.39-42)",
        "analysis": "AKA Ismarus. Odysseus and his men reach the Land of the Cicones, where they encounter a fierce battle and leave victorious. They ransack the city, kill the men, and enslave the women. While celebrating their victory, nearby Cicones retaliate and kill several of Odysseus' men.",
        "importance": "Marks one of the first encounters in Odysseus' journey, showcasing the challenges and consequences of his actions."
    },
    "Land of the Lotus Eaters": {
        "quote": "'The scouts encountered humans, Lotus-Eaters, who did not hurt them. They just shared with them their sweet delicious fruit. But as they ate it, they lost the will to come back and bring news to me. They wanted only to stay there, feeding on lotus with the Lotus-Eaters. They had forgotten home. I dragged them back. in tears, forced them on board the hollow ships, pushed them below the decks, and tied them up.' Od. 9.91-99",
        "analysis": "Upon reaching the land of the Lotus Eaters, Odysseus' crew encounters an enticing land where the inhabitants consume a plant called the lotus. They sample the plant and succumb to its effects, losing all desire to return home. Despite Odysseus' efforts to retrieve them and continue their journey, the men refuse to leave. He orders them back onto their ships and ties them up.",
        "importance": "Highlights the dangers of temptation and the importance of perseverance in Odysseus' journey."
    },
    "Land of the Cyclopes": {
        "quote": "'We reached the land of the Cyclopes, a fierce, lawless people who never lift a hand to plant or plow but trust in the immortal gods.' (Od.9.105-107)",
        "analysis": "Odysseus and his men reached teh Land of the Cyclopes, home of the giant cyclops Polyphemus. They entered Polyphemus' cave, and were trapped as he began to eat some of Odysseus' crew. Odysseys blinded Polyphemus and escaped with his men by hiding under the giant's sheep. As they were leaving, Odysseus taunted Polyphemus, revealing his real name and incurring the wrath of the god Poseidon.",
        "importance": "This encounter showcases his intelligence, recoucefullness, and cunningness. It also marks the beginning of Posiedon's grudge against Odysseus."
    },
    "Aeolia": {
        "quote": "'We reached the floating island of Aeolia, home of Aeolus, son of Hippotas, dear to the immortal gods.' (Od.10.1-3)",
        "analysis": "Odysseus and his men visited this island ruled by Aeolus, the god of winds, who gave them a bag of winds to help them return home. However, Odysseus' men opened the bag prematurely whilst he was sleeping, because they found it suspicious, causing them to be blown off course.",
        "importance": "This event represents a missed opportunity for a swift return home. It also highlights the theme of divine intervention and the consequences of human error in the face of temptation."
    },
    "Laestrygonia": {
        "quote": "'Hearing, the mighty Laestrygonians thronged from all sides, not humanlike, but giants. With boulders bigger than a man could lift they pelted at us from the cliffs. We heard the dreadful uproar of ships being broken and dying men.' (Od. 10.119-124).",
        "analysis": "When Odysseus and his men arrived in the land of the Lestrygonians, they encountered giant cannibals who attacked and destroyed most of the ships in Odysseus' fleet. Odysseus and a few survivors managed to escape, but the encounter was a significant setback in their journey home.",
        "importance": "The encounter with the Laestrygonians results in significant losses for Odysseus' fleet, emphasizing the dangers of the journey."
    },
    "Land of the Sirens": {
        "quote": "'Next you will come to the Sirens who beguile all men that approach them. Whoever encounters them unawares and listens to their singing will never joy at reaching home.' (Od.12.39-41)",
        "analysis": "When Odysseus and his men approached the island of the Sirens, whose enchanting voices lured sailors to their deaths, he had his men plug their ears with wax so they would not be tempted. However, Odysseus himself wanted to hear their song, so he had his men tie him to the mast of the ship and instructed them not to untie him, no matter how much he begged.",
        "importance": "Highlights his cunning intellect and his ability to overcome temptation and resist allurements that could potentially jeopardize his journey home."
    },
    "Scylla and Charybdis": {
        "quote": "'Beneath, divine Charybdis sucks black water down. Three times a day she spurts it up; three times she glugs it down. Avoid that place when she is swallowing the water. No one could save you from death then, even great Poseidon. Row fast, and steer your ship alongside Scylla, since it is better if you lose six men than all of them.' (Od. 12.103-111)",
        "analysis": "As Odysseus and his men sailed between Scylla, a six-headed monster, and Charybdis, a deadly whirlpool, Scylla snatched six of his men, one for each of her heads. Although Odysseus was powerless to stop Scylla's attack, he managed to steer his ship away from Charybdis' deadly vortex, narrowly avoiding total destruction.",
        "importance": "Represents a moment of decision-making under extreme pressure. It showcases Odysseus' leadership and strategic thinking as he makes the difficult choice to minimize losses and continue his journey home."
    },
    "Ithaca": {
        "quote": "'The land was visible. Odysseus, after so long a wait and so much pain, was filled with happiness at last. In joy he kissed the fertile earth of his own country, then lifted high his arms and prayed' (Od. 13.352-356)",
        "analysis": " Ithaca is Odysseus' homeland and the ultimate destination of his long and arduous journey. After ten years of fighting in the Trojan War and another ten years of wandering, Odysseus finally returns to Ithaca. However, upon his return, he finds that his palace has been overrun by suitors vying for the hand of his wife, Penelope, and attempting to claim his kingdom. Disguised as a beggar, Odysseus spends time observing the situation in Ithaca and planning his revenge against the suitors.",
        "importance": "Ithaca is the long-awaited goal of Odysseus' journey, symbolizing homecoming and reunion with his family."
    },
    "Aeaea": {
        "quote": "'We reached Aeaea, home of the beautiful, dreadful goddess Circe, who speaks in human languages—the sister of Aeetes whose mind is set on ruin.' (Od. 10.135-138)",
        "analysis": "When Odysseus and his men arrived at Aeaea, they encountered the witch-goddess Circe, who turned some of his men into pigs. With the help of the god Hermes, Odysseus was able to resist Circe's magic and force her to restore his men to human form. Odysseus and his men then stayed on Aeaea for a year, enjoying the luxurious hospitality of Circe, before continuing on their journey home. When it was time to leave Aeaea, Circe told the men they needed to go to the Underworld before going back to Ithaca.",
        "importance": "The encounter with Circe and the transformation of his crew underscores the dangers of magic and temptation on Odysseus' journey."
    },
    "Thrinacia": {
        "quote": "'My friends, we have supplies on board. Let us not touch the cattle, or we will regret it. Those cows and fat sheep are the property of Helius, the great Sun God, who sees all things, and hears all things.' (Od. 12.320-324)",
        "analysis": "When Odysseus and his men arrived on the island of Thrinacia, they were warned not to harm the sacred cattle of the sun god Helios. However, Odysseus' men ignored the warning and killed and ate some of the cattle. As punishment, Zeus sent a thunderbolt that destroyed their ship, killing all of Odysseus' men except for him.",
        "importance": "Thrinacia is where Odysseus' crew succumbs to temptation, leading to dire consequences and further delays in their journey."
    },
    "Ogygia": {
        "quote": "'On the tenth black night, the gods carried me till I reached Ogygia, home of the beautiful and mighty goddess Calypso. Lovingly she cared for me, vowing to set me free from death and time forever. But she never swayed my heart. I stayed for seven years; she gave me clothes like those of gods, but they were always wet with tears.' (Od. 7.253-261).",
        "analysis": "Where Odysseus is held captive by the nymph Calypso for seven years. Calypso offered Odysseus immortality and eternal youth if he stayed with her, but he longed to return to his wife and kingdom. He escapes with the help of the god Hermes.",
        "importance": "Ogygia represents a significant obstacle to Odysseus' journey, delaying his return home and testing his resilience and loyalty."
    },
    "Phaeacia": {
        "quote": "'Now, Odysseus, since you have been my guest, beneath my roof, you need not wander anymore. You have endured enough; you will get home again.' (Od. 13.3-6)",
        "analysis": "When Odysseus arrived in Phaeacia, he was welcomed by the princess Nausicaa, who showed him hospitality and kindness. The king of Phaeacia, Alcinous, offered to help Odysseus return home by providing him with a ship and crew. Odysseus recounted his epic journey and adventures to the Phaeacians, who were enthralled by his stories and sent him off to Ithaca, his home.",
        "importance": "Phaeacia serves as a pivotal point in Odysseus' journey, where he recounts his adventures and receives aid to finally return home."
    }
}

# Create a map centered around the Mediterranean
m = folium.Map(location=[37.9838, 23.7275], zoom_start=5)

# Add markers for each location with popup information
for location, coord in locations.items():
    folium.Marker(location=coord, popup=folium.Popup(f"<div style='width: 300px; height: 200px;'><b>{location}</b><br>{location_info[location]['quote']}<br>{location_info[location]['analysis']}<br><br><b>Importance:</b> {location_info[location]['importance']}</div>", max_width=300)).add_to(m)

# Add custom icons for different types of locations
icon_colors = {
    "Troy": "blue",
    "Land of the Cicones": "green",
    "Land of the Lotus Eaters": "green",
    "Land of the Cyclopes": "red",
    "Aeolia": "orange",
    "Laestrygonia": "red",
    "Land of the Sirens": "pink",
    "Scylla and Charybdis": "purple",
    "Ithaca": "blue",
    "Aeaea": "purple",
    "Thrinacia": "red",
    "Ogygia": "pink",
    "Phaeacia": "green"
}

for location, coord in locations.items():
    folium.Marker(location=coord, popup=folium.Popup(f"<div style='width: 300px; height: 300px;'><b>{location}</b><br>{location_info[location]['quote']}<br>{location_info[location]['analysis']}<br><br><b>Importance:</b> {location_info[location]['importance']}</div>", max_width=300),
                  icon=folium.Icon(color=icon_colors[location])).add_to(m)

# Save the map to an HTML file
m.save("odyssey_map.html")