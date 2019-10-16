#######################################
def main():
    """
    This contains all of the text data for the adventure. It is a json object structured as:
    scenarios (dict): contains all scenario data
    id (int): id for each scenario
    description (str): description for user to see about room
    options (list): available options for user in reponse to description
    outcome (list): outcome for each option
    result (bool): used to determine if option/outcome is successful and to move on
    """
    data = {}
    data['scenarios'] = [
        {
            "id": 1, 
            "description": "\nYou see a large golden orb sitting on top of a pedestal.\nSome sort of god-like statue looms above the room.\nA small door stands nearby.\n", 
            "options": [
                "Brazenly take the golden orb and dash towards the final door", 
                "Replace the orb with a similar looking adjacent rock", 
                "Dilligently inspect the alter for additional information"
            ],
            "outcome": [
                "A rolling boulder falls from a trapdoor above you and crushes you.",
                "You hear only silence and are able to escape out a nearby door.",
                "As you inspect the alter, you suddenly feel an arrow from a triggered trap pierce your side. Everything goes dark..."
            ],
            "result": [
                False,
                True,
                False,
            ]
        },
        {
            "id": 2, 
            "description": "\nYou open the door to a scene of carnage. Two male humans, a male elf, and a female dwarf lie in drying pools of their blood.\nIt seems that they might once have been wearing armor, except for the elf, who remains dressed in a blue robe. \nClearly they lost some battle and victors stripped them of their valuables.\n", 
            "options": [
                "Sidestep the carnage and continue moving to the next room", 
                "Inspect the scene to determine the cause of death", 
                "Loot whatever remains you can scavenge from the bodies",
            ],
            "outcome": [
                "As you near the door on the opposite side, you see glowing eyes staring at you from a dark corner.",
                "While inspecting the bodies, you feel an insidious jaw close around your torso.",
                "As you search the elf, you pull out a small potion from the corpse. Suddenly, a jaw closes around your torso..."
            ],
            "result": [
                True,
                False,
                False,
            ]
        }, 
        {
            "id": 3, 
            "description": "\nA cluster of low crates surrounds a barrel in the center of this chamber.\nAtop the barrel lies a stack of copper coins and two stacks of cards, one face up.\nMeanwhile, atop each crate rests a fan of five face-down playing cards.\nA thin layer of dust covers everything. Clearly someone meant to return to their game of cards.\n", 
            "options": [
                "Take the stack of copper coins and move towards the exit", 
                "Look to see the face up cards", 
                "Quickly move past the card game -- there's a good chance whomever was playing may be back soon."
            ],
            "outcome": [
                "The clattering of the coins appears to have drawn the attention of the card players. \nTheir swords glisten in the dim candlelight as they are drawn.",
                "it appears the winner had two aces -- a fortuitous hand. You continue to the next door.",
                "As you leave the room, you hear multiple voices barking laughter above clattering swords."
            ],
            "result": [
                False,
                True,
                True,
            ]
        },
        {
            "id": 4, 
            "description": "\nYou arrive at an empty room. Blocking the next door is a large stone slab with writing on it.\nThe writing reads:\n\"I have rivers without water,\nForests without trees,\nMountains without rocks,\nTowns without houses.\"\n",
            "options": [
                "A Map",
                "A City", 
                "A Planet", 
                "Ignore the riddle and push the block aside",
            ],
            "outcome": [
                "As you speak the answer, the stone slab moves aside and allows you to pass.",
                "As you speak the answer, you begin to feel light headed...",
                "As you speak the answer, you begin to feel light headed...",
                "As you begin pushing, the stone slab falls with inhuman force near you.\nWith quick reflexes you are able to avoid the slab and pass forward."
            ],
            "result": [
                True,
                False,
                False,
                True
            ]
        },
        {
            "id": 5, 
            "description": "The pathway continues down a corridor until, suddenly, it splits into two paths.", 
            "options": [
                "Take the left door", 
                "Take the right door", 
            ],
            "outcome": [
                "You go through the doorway and see the path immediately groups back up with the right doorway.\nWhat a waste of time.",
                "You go through the doorway and see the path immediately groups back up with the left doorway.\nWhat a waste of time."
            ],
            "result": [
                True,
                True
            ]
        },
        {
            "id": 6, 
            "description": "The pathway briefly moves until it is overlooking a deep chasm, too far to see the bottom.\nOnly an unsteady and dilapidated wooden slat bridge provides a way across.", 
            "options": [
                "Run quickly across the bridge, hoping it doesn\'t break on the way", 
                "Slowly but steadily move across the bridge, checking for weaknesses as you go"
            ],
            "outcome": [
                "As your foot touches the other side, you see the bridge collapse behind you. Good thing you went quickly...",
                "Although you find multiple weak slats as you go, you are able to make it across the bridge.\nYou likely would have stepped on a weak one and fallen to your death.\nGood thing you went slowly..."
            ],
            "result": [
                True,
                True,
            ]
        },
        {
            "id": 7, 
            "description": "A wide staircase steeply ascends to another level.\nAs you nearly reach the top, a pressure plate triggers a blast of jagged ice towards you.", 
            "options": [
                "Dodge to the left", 
                "Dodge to the right", 
                "Roll back down the stairs",
                "Push forward into the ice blast"
            ],
            "outcome": [
                "You narrowly escape the ice blast and are able to hide in a crevice in the wall until the trap completes its\' ice blast.",
                "You narrowly escape the ice blast and are able to hide in a crevice in the wall until the trap completes its\' ice blast.",
                "As you roll, your momentum is increased by the blast and you fall the entirety of the staircase.\nYou are unable to move your legs. In this dungeon, it\'s unlikely rescue is coming...",
                "You bravely face the ice blast head on. Unfortunately, this trap was designed for such bravery and you are frozen solid."
            ],
            "result": [
                True,
                True,
                False,
                False
            ]
        },
        {
            "id": 8, 
            "description": "An old witch sits next to a bubbling cauldron. She crooks a finger at you and screeches,\n\"You! Come here...I have a very special potion for you.\"\nShe looks at you expectedly, as if demanding an answer.",
            "options": [
                "Drink the old witch's potion", 
                "Politely refuse, mentioning you will drink it again if you pass her later", 
                "What\'s in the potion? Who\'s to say?"
            ],
            "outcome": [
                "You begin to feel...fuzzy. As if your body isn\'t entirely stable. After a few grueling moments pass, you begin to feel normal again.",
                "She looks disappointed, but not defeated. She returns to her bubbling brew and you are able to pass unhindered.",
                "The witch looks at you, confused by your response. In her confusion she begins to contemplate, allowing you to pass freely."
            ],
            "result": [
                True,
                True,
                True,
                True
            ]
        }
    ]
    data['flavor_text'] = [
        "You see another path open before you, as if the dungeon is mocking you.",
        "These rooms seem somewhat similar to the previous set...have you been here before?",
        "Are the rooms...moving as you move? It's as if this dungeon is alive.",
        "You continue onwards, deeper into the dungeon's secret passages.",
        "You pass a few more passages, they all look so similar; this whole place is a maze.",
        "You pass dozens of similar rooms and passages, most of which probably lead to other depths of this dungeon."
    ]

    return data
#######################################
if __name__ == '__main__':
    main()
#######################################
