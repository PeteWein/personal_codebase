import json 

data = {}
data['scenarios'] = [
    {
        "id": 1, 
        "description": "Scenario 1", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    }, 
    {
        "id": 2, 
        "description": "Scenario 2", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    }, 
    {
        "id": 3, 
        "description": "Scenario 3", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    },
    {
        "id": 4, 
        "description": "Scenario 3", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    },
    {
        "id": 5, 
        "description": "Scenario 3", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    },
    {
        "id": 6, 
        "description": "Scenario 3", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    },
    {
        "id": 7, 
        "description": "Scenario 3", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    },
    {
        "id": 8, 
        "description": "Scenario 3", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    },
    {
        "id": 9, 
        "description": "Scenario 3", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    },
    {
        "id": 10, 
        "description": "Scenario 3", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    },
    {
        "id": 11, 
        "description": "Scenario 3", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    },
    {
        "id": 12, 
        "description": "Scenario 3", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    },
    {
        "id": 13, 
        "description": "Scenario 3", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    },
    {
        "id": 14, 
        "description": "Scenario 3", 
        "options": [
            "Opt 1", 
            "Opt 2", 
            "Opt 3"
        ]
    }
]



with open('scenarios.json', 'w') as outfile:
    json.dump(data, outfile)