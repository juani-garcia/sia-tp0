import pandas as pd
from matplotlib import pyplot as plt

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
from src.util import key_list

SIMS = 20


def simulate():
    factory = PokemonFactory("pokemon.json")
    ans = {}
    for pokemon_name in key_list("pokemon.json"):
        ans[pokemon_name] = {}
        for status in StatusEffect:
            pokemon = factory.create(pokemon_name, 100, status, 1)
            accum = 0.0
            for _ in range(SIMS):
                attempt = attempt_catch(pokemon, "pokeball")
                accum += attempt[1]
            ans[pokemon_name][status.name] = accum / SIMS
    return ans


def graph(base_name="figs/q2a"):
    ans = simulate()
    for k, v in ans.items():
        series = pd.Series(v)
        ax = series.plot(kind='bar', figsize=(8, 6), rot=0)
        ax.set_xlabel('Status Effect')
        ax.set_ylabel('Average catch rate')
        ax.set_title(k + " catch rate with different status effects")
        plt.savefig(base_name + "_" + k + '.png')
        ax.cla()
