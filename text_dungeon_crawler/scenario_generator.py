#######################################
import json 
#######################################
def main():
    data = {}
    data['scenarios'] = [
        {
            "id": 1, 
            "description": "You see a large golden orb sitting on top of a pedestal. Some sort of god-like statue looms above the room.\n A small door stands nearby.", 
            "options": [
                "Brazenly take the golden orb", 
                "Replace the orb with a similar looking adjacent rock", 
                "Dilligently inspect the alter"
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
            "description": "Scenario 2", 
            "options": [
                "Opt 1", 
                "Opt 2", 
                "Opt 3"
            ],
            "outcome": [
                "Out 1",
                "Out 2",
                "Out 3"
            ],
            "result": [
                False,
                True,
                False,
            ]
        }, 
        {
            "id": 3, 
            "description": "Scenario 3", 
            "options": [
                "Opt 1", 
                "Opt 2", 
                "Opt 3"
            ],
            "outcome": [
                "Out 1",
                "Out 2",
                "Out 3"
            ],
            "result": [
                False,
                True,
                False,
            ]
        },
        {
            "id": 4, 
            "description": "Scenario 3", 
            "options": [
                "Opt 1", 
                "Opt 2", 
                "Opt 3"
            ],
            "outcome": [
                "Out 1",
                "Out 2",
                "Out 3"
            ],
            "result": [
                False,
                True,
                False,
            ]
        },
        {
            "id": 5, 
            "description": "Scenario 3", 
            "options": [
                "Opt 1", 
                "Opt 2", 
                "Opt 3"
            ],
            "outcome": [
                "Out 1",
                "Out 2",
                "Out 3"
            ],
            "result": [
                False,
                True,
                False,
            ]
        },
        {
            "id": 6, 
            "description": "Scenario 3", 
            "options": [
                "Opt 1", 
                "Opt 2", 
                "Opt 3"
            ],
            "outcome": [
                "Out 1",
                "Out 2",
                "Out 3"
            ],
            "result": [
                False,
                True,
                False,
            ]
        },
        {
            "id": 7, 
            "description": "Scenario 3", 
            "options": [
                "Opt 1", 
                "Opt 2", 
                "Opt 3"
            ],
            "outcome": [
                "Out 1",
                "Out 2",
                "Out 3"
            ],
            "result": [
                False,
                True,
                False,
            ]
        },
        {
            "id": 8, 
            "description": "Scenario 3", 
            "options": [
                "Opt 1", 
                "Opt 2", 
                "Opt 3"
            ],
            "outcome": [
                "Out 1",
                "Out 2",
                "Out 3"
            ],
            "result": [
                False,
                True,
                False,
            ]
        },
        {
            "id": 9, 
            "description": "Scenario 3", 
            "options": [
                "Opt 1", 
                "Opt 2", 
                "Opt 3"
            ],
            "outcome": [
                "Out 1",
                "Out 2",
                "Out 3"
            ],
            "result": [
                False,
                True,
                False,
            ]
        },
        {
            "id": 10, 
            "description": "Scenario 3", 
            "options": [
                "Opt 1", 
                "Opt 2", 
                "Opt 3"
            ],
            "outcome": [
                "Out 1",
                "Out 2",
                "Out 3"
            ],
            "result": [
                False,
                True,
                False,
            ]
        },
        {
            "id": 11, 
            "description": "Scenario 3", 
            "options": [
                "Opt 1", 
                "Opt 2", 
                "Opt 3"
            ],
            "outcome": [
                "Out 1",
                "Out 2",
                "Out 3"
            ],
            "result": [
                False,
                True,
                False,
            ]
        },
        {
            "id": 12, 
            "description": "Scenario 3", 
            "options": [
                "Opt 1", 
                "Opt 2", 
                "Opt 3"
            ],
            "outcome": [
                "Out 1",
                "Out 2",
                "Out 3"
            ],
            "result": [
                False,
                True,
                False,
            ]
        },
        {
            "id": 13, 
            "description": "Scenario 3", 
            "options": [
                "Opt 1", 
                "Opt 2", 
                "Opt 3"
            ],
            "outcome": [
                "Out 1",
                "Out 2",
                "Out 3"
            ],
            "result": [
                False,
                True,
                False,
            ]
        }
    ]
    data['flavor_moving'] = [
        "You see another path open before you, as if the dungeon is mocking you.",
        "These rooms seem somewhat similar to the previous set...have you been here before?",
        "Are the rooms...moving as you move? It's as if this dungeon is alive.",
        "You continue onwards, deeper into the dungeon's secret passages.",
        "You pass a few more passages, they all look so similar, this whole place is a maze.",
        "You pass dozens of similar rooms and passages, most of which probably lead to other depths of this dungeon."
    ]

    return data
#######################################
if __name__ == '__main__':
    main()
#######################################
