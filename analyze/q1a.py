from src.catching import attempt_catch
from src.pokemon import PokemonFactory
from src.util import key_list
import pandas as pd
import matplotlib.pyplot as plt

SIMS = 100


def simulate() -> dict:
    factory = PokemonFactory("pokemon.json")
    ans = {}
    for pokeball_name in key_list("pokeball.json"):
        ans[pokeball_name] = {}
        for pokemon_name in key_list("pokemon.json"):
            pokemon = factory.create_basic(pokemon_name)
            accum = 0.0
            caught = 0
            for _ in range(SIMS):
                att = attempt_catch(pokemon, pokeball_name)
                accum += att[1]
                caught += 1 if att[0] else 0
            ans[pokeball_name][pokemon_name.upper()] = accum/SIMS
    return ans


def graph(ans, base_name="figs/q1a"):
    for pokeball_name in key_list("pokeball.json"):
        series = pd.Series(ans[pokeball_name])
        ax = series.plot(kind='bar', figsize=(8, 6), rot=0)
        ax.set_xlabel('Pokemon')
        ax.set_ylabel('Average catch rate')
        ax.set_title(pokeball_name.upper())
        plt.savefig(base_name+'_'+pokeball_name+'.png')
        ax.cla()
