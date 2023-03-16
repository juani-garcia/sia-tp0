import matplotlib.pyplot as plt
import pandas as pd

from src.catching import attempt_catch
from src.pokemon import PokemonFactory
from src.util import key_list

SIMS = 10000
COMPARE_TO = "POKEBALL"


def simulate() -> dict:
    factory = PokemonFactory("pokemon.json")
    ans = {}
    for pokemon_name in key_list("pokemon.json"):
        pokemon = factory.create_basic(pokemon_name)
        ans[pokemon.name.upper()] = {}
        for pokeball_name in key_list("pokeball.json"):
            caught = 0
            for _ in range(SIMS):
                att = attempt_catch(pokemon, pokeball_name)
                caught += 1 if att[0] else 0
            ans[pokemon.name.upper()][pokeball_name.upper()] = caught / SIMS
        base_effectiveness = ans[pokemon.name.upper()][COMPARE_TO]
        for ball in ans[pokemon.name.upper()].keys():
            ans[pokemon.name.upper()][ball] = ans[pokemon.name.upper()][ball] / base_effectiveness
    return ans


def graph(base_name="figs/q1b"):
    ans = simulate()
    for pokemon_name in key_list("pokemon.json"):
        series = pd.Series(ans[pokemon_name.upper()])
        ax = series.plot(kind='bar', figsize=(8, 6), rot=0)
        ax.set_xlabel('Pokeball')
        ax.set_ylabel('Average ball effectiveness')
        ax.set_title(pokemon_name.upper())
        plt.savefig(base_name + '_' + pokemon_name + '.png')
        ax.cla()
