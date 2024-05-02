""" 
This program is a hub for mini games and activites centered around classical mythology, specifically the Odyssey

Student 1: Mireya Martinez
eid: mam27549
Student 2: Christopher Chavez
eid: cac9354

"""

import random

class RPGGame:
    def __init__(self):
        # Define character traits and stories from the Odyssey
        self.characters = {
            "Odysseus": {"traits": "Cunning and resourceful", "story": "Odysseus, the hero of the Trojan War, embarks on a perilous journey home to Ithaca after years of wandering."},
            "Telemachus": {"traits": "Brave and determined", "story": "Telemachus, the son of Odysseus, sets out on a quest to find news of his father."}
        }

        # Define quests and challenges based on events from the Odyssey
        self.quests = {
            "Odysseus": [
                {"name": "Escape from Polyphemus", "description": "Odysseus encounters the Cyclops Polyphemus and must find a way to escape before being eaten.",
                 "decisions": [
                     {"description": "Attack Polyphemus", "outcome1": "Polyphemus kills Odysseus and his crew.", "outcome2": "Odysseus blinds Polyphemus and escapes with his men."},
                     {"description": "Conceal in the cave", "outcome1": "Polyphemus discovers Odysseus and eats him.", "outcome2": "Polyphemus falls asleep, allowing Odysseus to escape with his men."}
                 ]},
                {"name": "Navigating Scylla and Charybdis", "description": "Odysseus faces the deadly monsters Scylla and Charybdis and must navigate his ship safely through their treacherous waters.",
                 "decisions": [
                     {"description": "Sail closer to Scylla", "outcome1": "Scylla devours some of Odysseus' crew.", "outcome2": "Charybdis swallows the ship, but Odysseus and most of his crew survive."},
                     {"description": "Avoid Scylla and Charybdis", "outcome1": "The ship is destroyed by a whirlpool.", "outcome2": "Odysseus successfully navigates past Scylla and Charybdis with minimal losses."}
                 ]},
                {"name": "Defeating the Suitors", "description": "Odysseus returns to Ithaca to find his home overrun by suitors vying for the hand of his wife, Penelope. He must devise a plan to defeat them and reclaim his kingdom.",
                 "decisions": [
                     {"description": "Reveal his identity to the suitors", "outcome1": "The suitors plot to kill Odysseus.", "outcome2": "Odysseus reveals his identity and defeats the suitors in battle."},
                     {"description": "Stay in disguise", "outcome1": "The suitors discover Odysseus' identity and kill him.", "outcome2": "Odysseus successfully maintains his disguise and devises a plan to defeat the suitors."}
                 ]}
            ],
            "Telemachus": [
                {"name": "Searching for Odysseus", "description": "Telemachus sets out on a journey to find news of his father, Odysseus, and learn of his fate.",
                 "decisions": [
                     {"description": "Visit Nestor", "outcome1": "Nestor has no news of Odysseus.", "outcome2": "Nestor shares stories of Odysseus' exploits."},
                     {"description": "Visit Menelaus", "outcome1": "Menelaus has no news of Odysseus.", "outcome2": "Menelaus provides valuable information about Odysseus' whereabouts."}
                 ]},
                {"name": "Confrontation with the Suitors", "description": "Telemachus returns to Ithaca to find his home besieged by suitors. He must confront them and assert his authority as the rightful heir to the throne.",
                 "decisions": [
                     {"description": "Confront the suitors directly", "outcome1": "Telemachus is outnumbered and driven away.", "outcome2": "Telemachus gains the respect of the suitors and asserts his authority."},
                     {"description": "Seek help from allies", "outcome1": "The allies refuse to support Telemachus.", "outcome2": "The allies rally to Telemachus' aid and help him confront the suitors."}
                 ]}
            ]
        }

    def play_game(self):
        print("Welcome to the Odyssey RPG game!\n")
        print("Choose your character:")
        for i, character in enumerate(self.characters.keys(), 1):
            print(f"{i}. {character}")
        choice = input("\nEnter the number of your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.characters):
            character_name = list(self.characters.keys())[int(choice) - 1]
            character = self.characters[character_name]
            print(f"\nYou have chosen {character_name}.")
            print(f"Story: {character['story']}")
            print(f"Traits: {character['traits']}")
            print("\nLet's begin your journey!\n")
            self.begin_journey(character_name)
        else:
            print("Invalid choice. Please enter a number corresponding to the character.")

    def begin_journey(self, character_name):
        print("Your journey begins...\n")
        for index, quest in enumerate(self.quests[character_name]):
            print(f"Quest: {quest['name']}")
            print(f"Description: {quest['description']}\n")
            print("You face a critical decision...")
            for i, decision in enumerate(quest["decisions"], 1):
                print(f"{i}. {decision['description']}")
            choice = input("\nEnter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(quest["decisions"]):
                decision = quest["decisions"][int(choice) - 1]
                print("\nYou choose:", decision['description'])
                print("\nOutcome:")
                outcome = random.choice([decision['outcome1'], decision['outcome2']])
                print(outcome)
                if "kills" in outcome.lower():
                    print("\nYou have met a tragic end. Game Over.")
                    return
                if (index == len(self.quests[character_name]) - 1) and (character_name == "Odysseus"):
                    print("\nYour journey ends.\n")
                    return
                if (index == len(self.quests[character_name]) - 1) and (character_name == "Telemachus"):
                    print("\nYour journey ends.\n")
                    main_menu()
                    return
                print("\nYour journey continues...\n")
            else:
                print("Invalid choice. Please enter a number corresponding to the decision.")


class TriviaGame:
    def __init__(self):
        # Define trivia questions about the Odyssey with quotes and analysis
        self.trivia_questions = [
            {"question": "What is the name of Odysseus' wife?", "options": ["Helen", "Hera", "Athena", "Penelope"], "answer": "Penelope", "quote": "'Penelope, wise wife of Odysseus, sought out her own chamber, that was built deep within the stronghold of the house, high-roofed, and carved with the skill of the man, her lord, and the work of the cunning smiths, who with artifice of their craft had drawn it up with their tools, and built it over the echoing gallery, to be a chamber of her own.' (Od.19.56-61)\n"},

            {"question": "What is the name of the one-eyed giant encountered by Odysseus?", "options": ["Polyphemus", "Cyclops", "Cerberus", "Scylla"], "answer": "Polyphemus", "quote": "'He devoured them, lapping up their entrails and their flesh, and with horrible gulps he drank down the blood.' Od. 9.299-301)\n"},

            {"question": "Which goddess helps Odysseus throughout his journey?", "options": ["Hera", "Artemis", "Athena", "Aphrodite"], "answer": "Athena", "quote": "'But Athena came to my help and urged the Phaeacians to do me honour.' Od. 13.340\n"},

            {"question": "Who is the goddess that turns Odysseus' men into swine", "options": ["Athena", "Circe", "Calypso", "Hera"], "answer": "Circe", "quote": "'And she, with craft and cunning, drugged the meal she gave them—cheese and barley meal—adding her wicked drugs, and they lost their heads, their memories, and forgot the way home.' Od. 10.237-39\n"}
        ]

    def play_game(self):
        score = 0
        for question in self.trivia_questions:
            print(question["question"])
            for i, option in enumerate(question["options"], 1):
                print(f"{i}. {option}")
            answer = input("\nEnter your answer (1-4): ")
            if answer == str(question["options"].index(question["answer"]) + 1):
                print("\nCorrect!")
                print("Quote from the text: ", question["quote"])
                score += 1
            else:
                print("\nIncorrect!")
                print("Quote from the text: ", question["quote"])
        print("\nYour score:", score)

def main_menu():
    print("Welcome to the Odyssey Mini-Game Hub!\n")
    print("Choose an option:")
    print("1. Odyssey RPG game")
    print("2. The Odyssey trivia")
    print("3. Quit")

    choice = input("\nEnter your choice (1, 2, or 3): ")
    if choice == "1":
        game = RPGGame()
        game.play_game()
    elif choice == "2":
        game = TriviaGame()
        game.play_game()
    elif choice == "3":
        print("\nThanks for playing!")
        exit()
    else:
        print("\nInvalid choice. Please enter a number between 1 and 3.")

# Run the main menu
main_menu()