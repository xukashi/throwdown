import json
from pathlib import Path
from random import choice

_TRICKS_PATH = Path(__file__).parent / 'tricks.json'

with open(_TRICKS_PATH, encoding='utf-8') as _file:
    _tricks = json.load(_file)

_aliases = _tricks['aliases']

def _random_elements():
    return {
        'stance': choice(_tricks['stance']),
        'direction': choice(_tricks['direction']),
        'spin': choice(_tricks['spin']),
        'highpop': choice(_tricks['highpop']),
        'flips': choice(_tricks['highpop'][:2]),
        'pops': choice(_tricks['highpop'][3:]),
        'midpop': choice(_tricks['midpop']),
        'lowpop': choice(_tricks['lowpop']),
        'pressure': choice(_tricks['pressure']),
        'grind': choice(_tricks['grind']),
        'flat': choice(_tricks['flat']),
    }

def _combo_pools(e):
    easy = [
        [e['stance'], e['midpop']],
        [e['stance'], "to", e['grind']],
        [e['stance'], e['direction'], e['spin']],
        [e['stance'], e['direction'], e['highpop']],
    ]

    medium = [
        [e['stance'], e['lowpop']],
        [e['stance'], e['pressure']],
        [e['stance'], e['direction'], e['midpop']],
        [e['stance'], e['flips'], "to", e['flat']],
        [e['stance'], e['direction'], e['pressure']],
        [e['grind'], "to", e['direction'], e['spin']],
        [e['stance'], e['direction'], e['spin'], e['highpop']],
        [e['stance'], e['direction'], e['spin'], "to", e['flat']],
        [e['stance'], e['direction'], e['spin'], "to", e['grind']],
        [e['stance'], e['direction'], e['highpop'], "to", e['grind']],
    ]

    hard = [
        [e['grind'], "to", e['highpop']],
        [e['stance'], e['direction'], e['midpop']],
        [e['stance'], e['direction'], e['lowpop']],
        [e['stance'], e['direction'], e['spin'], e['highpop']],
        [e['stance'], e['direction'], e['spin'], e['pressure']],
        [e['stance'], e['direction'], e['spin'], "to", e['grind']],
        [e['stance'], e['direction'], e['midpop'], "to", e['grind']],
        [e['stance'], e['direction'], e['lowpop'], "to", e['grind']],
        [e['stance'], e['direction'], e['spin'], e['highpop'], "to", e['grind']],
        [e['stance'], e['direction'], e['flips'], "to", e['flat'], "to", e['flips']],
        [e['stance'], e['direction'], e['lowpop'], "to", e['flat'], "to", e['flips']],
        [e['stance'], e['direction'], e['midpop'], "to", e['flat'], "to", e['midpop']],
        [e['stance'], e['direction'], e['midpop'], "to", e['grind'], "to", e['highpop']],
        [e['stance'], e['direction'], e['spin'], e['midpop'], "to", e['flat'], "to", e['midpop']],
        [e['stance'], e['direction'], e['spin'], e['midpop'], "to", e['flat'], "to", e['highpop']],
        [e['stance'], e['direction'], e['flips'], "to", e['flat'], "to", e['direction'], e['spin']],
        [e['stance'], e['direction'], e['flips'], "to", e['flat'], "to", e['direction'], e['flips']],
        [e['stance'], e['direction'], e['spin'], e['highpop'], "to", e['grind'], "to", e['highpop']],
        [e['stance'], e['direction'], e['midpop'], "to", e['flat'], "to", e['direction'], e['spin']],
        [e['stance'], e['direction'], e['midpop'], "to", e['grind'], "to", e['direction'], e['spin']],
        [e['stance'], e['direction'], e['spin'], e['midpop'], "to", e['flat'], "to", e["direction"], e['flips']],
        [e['stance'], e['direction'], e['spin'], e['midpop'], "to", e['flat'], "to", e["direction"], e['midpop']],
    ]

    return easy, medium, hard

def _format(trick_list):
    output = " ".join(str(x) for x in trick_list).strip()
    if output.startswith("to"):
        output = "Ollie " + output
    return output

def _apply_aliases(combo):
    for original in sorted(_aliases, key=len, reverse=True):
        combo = combo.replace(original, _aliases[original])
        if "Modern Ghetto Bird 360" in combo:
            combo = combo.replace("Modern Ghetto Bird 360", "Backside Hardflip 360")
    return combo

def generate_trick(difficulty):
    easy, medium, hard = _combo_pools(_random_elements())

    pools = {
        "easy": easy,
        "medium": medium,
        "hard": hard,
    }

    if difficulty == "random":
        pool = choice(list(pools.values()))
    else:
        pool = pools[difficulty]

    combo = _apply_aliases(_format(choice(pool)))
    return combo.replace(" to ", "\n↓\n")
