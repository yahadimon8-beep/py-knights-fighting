# app/main.py
KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": 15,
                "hp": -5,
                "protection": 10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": 10,
                "power": 5,
            }
        }
    }
}


def prepare_knight(knight: dict) -> dict:
    protection = sum(
        armour["protection"]
        for armour in knight["armour"]
    )

    power = knight["power"] + knight["weapon"]["power"]
    hp = knight["hp"]

    potion = knight["potion"]

    if potion:
        effects = potion["effect"]

        power += effects.get("power", 0)
        protection += effects.get("protection", 0)
        hp += effects.get("hp", 0)

    return {
        "name": knight["name"],
        "hp": hp,
        "power": power,
        "protection": protection,
    }


def fight(first_knight: dict, second_knight: dict) -> None:
    first_damage = max(
        0,
        second_knight["power"] - first_knight["protection"]
    )

    second_damage = max(
        0,
        first_knight["power"] - second_knight["protection"]
    )

    first_knight["hp"] = max(
        0,
        first_knight["hp"] - first_damage
    )

    second_knight["hp"] = max(
        0,
        second_knight["hp"] - second_damage
    )


def battle(knights_config: dict) -> dict:
    lancelot = prepare_knight(
        knights_config["lancelot"]
    )

    arthur = prepare_knight(
        knights_config["arthur"]
    )

    mordred = prepare_knight(
        knights_config["mordred"]
    )

    red_knight = prepare_knight(
        knights_config["red_knight"]
    )

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
