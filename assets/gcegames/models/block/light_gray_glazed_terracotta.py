{
    "parent": "block/cube",
    "display": {
        "firstperson_righthand": {
            "rotation": [ 0, 135, 0 ],
            "translation": [ 0, 0, 0 ],
            "scale": [ 0.40, 0.40, 0.40 ]
        }
    },
    "elements": [
        {   "from": [ 0, 0, 0 ],
            "to": [ 16, 16, 16 ],
            "faces": {
                "down":  { "uv": [ 0,  0, 16, 16 ], "texture": "#bg", "cullface": "down"},
                "up":    { "uv": [ 0,  0, 16, 16 ], "texture": "#bg", "cullface": "up" },
                "north": { "uv": [ 0,  0, 16, 16 ], "texture": "#main", "cullface": "north"},
                "south": { "uv": [ 0,  0, 16, 16 ], "texture": "#main", "cullface": "south"},
                "west":  { "uv": [ 0,  0, 16, 16 ], "texture": "#main", "cullface": "west"},
                "east":  { "uv": [ 0,  0, 16, 16 ], "texture": "#main", "cullface": "east"}
            }
        }
    ],
    "textures": {
        "particle": "#main",
        "main": "gcegames:block/light_gray_gt",
        "bg": "gcegames:block/gt_background"
    }
}
