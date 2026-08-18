import json
from pathlib import Path
from random import choice

_TRICKS_PATH = Path(__file__).parent / "tricks.json"

with _TRICKS_PATH.open(encoding="utf-8") as _file:
    _tricks = json.load(_file)

_aliases = _tricks["aliases"]

stance = _tricks["stance"]
direction = _tricks["direction"]
spin = _tricks["spin"]
highpop = _tricks["highpop"]
midpop = _tricks["midpop"]
lowpop = _tricks["lowpop"]
pressure = _tricks["pressure"]
grind = _tricks["grind"]
flat = _tricks["flat"]

flips = highpop[:2]

def _combo_pools():
    easy = [
        [stance, midpop],
        [stance, "to", grind],
        [stance, direction, spin],
        [stance, direction, highpop],
    ]

    medium = [
        [stance, lowpop],
        [stance, pressure],
        [stance, direction, midpop],
        [stance, flips, "to", flat],
        [stance, direction, pressure],
        [grind, "to", direction, spin],
        [stance, direction, spin, highpop],
        [stance, direction, spin, "to", flat],
        [stance, direction, spin, "to", grind],
        [stance, direction, highpop, "to", grind],
    ]

    hard = [
        [grind, "to", highpop],
        [stance, direction, midpop],
        [stance, direction, lowpop],
        [stance, direction, spin, highpop],
        [stance, direction, spin, pressure],
        [stance, direction, spin, "to", grind],
        [stance, direction, midpop, "to", grind],
        [stance, direction, lowpop, "to", grind],
        [stance, direction, spin, highpop, "to", grind],
        [stance, direction, flips, "to", flat, "to", flips],
        [stance, direction, lowpop, "to", flat, "to", flips],
        [stance, direction, midpop, "to", flat, "to", midpop],
        [stance, direction, midpop, "to", grind, "to", highpop],
        [stance, direction, spin, midpop, "to", flat, "to", midpop],
        [stance, direction, spin, midpop, "to", flat, "to", highpop],
        [stance, direction, flips, "to", flat, "to", direction, spin],
        [stance, direction, flips, "to", flat, "to", direction, flips],
        [stance, direction, spin, highpop, "to", grind, "to", highpop],
        [stance, direction, midpop, "to", flat, "to", direction, spin],
        [stance, direction, midpop, "to", grind, "to", direction, spin],
        [stance, direction, spin, midpop, "to", flat, "to", direction, flips],
        [stance, direction, spin, midpop, "to", flat, "to", direction, midpop],
    ]

    return {
        "easy": easy,
        "medium": medium,
        "hard": hard,
    }

def _resolve_combo(combo):
    resolved = []
    for item in combo:
        if isinstance(item, list):
            resolved.append(choice(item))
        else:
            resolved.append(item)
    return resolved

def _format(trick_list):
    output = " ".join(str(x) for x in trick_list).strip()
    if output.startswith("to"):
        output = "Ollie " + output
    return output

def _apply_aliases(combo):
    for original in sorted(_aliases, key=len, reverse=True):
        combo = combo.replace(original, _aliases[original])
    combo = combo.replace("Modern Ghetto Bird 360", "Backside Hardflip 360")
    return combo

def generate_trick(difficulty="random"):
    pools = _combo_pools()

    if difficulty == "random":
        difficulty = choice(list(pools))

    combo = choice(pools[difficulty])
    combo = _resolve_combo(combo)
    combo = _format(combo)
    combo = _apply_aliases(combo)

    return combo.replace(" to ", "\n↓\n")
