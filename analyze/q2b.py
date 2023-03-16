from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
from src.util import key_list
import pandas as pd
import matplotlib.pyplot as plt

POKEBALL = "pokeball"

def simulate() -> dict:
    factory = PokemonFactory("pokemon.json")
    ans = {}
    for pokemon_name in key_list("pokemon.json"):
        ans[pokemon_name.upper()] = {
            'hp': [],
            'catch_rate': []
        }
        for hp in range(0, 101, 10):
            pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, hp/100.0)
            ans[pokemon.name.upper()]['hp'].append(hp)
            ans[pokemon.name.upper()]['catch_rate'].append(attempt_catch(pokemon, POKEBALL)[1])
    return ans


def graph(base_name="figs/q2b"):
    ans = simulate()
    for pokemon_name in key_list("pokemon.json"):
        df = pd.DataFrame(ans[pokemon_name.upper()])
        plt.plot(df['hp'], df['catch_rate'], label='A')
        plt.title(f"{pokemon_name.upper()} (using {POKEBALL})")
        plt.xlabel('HP (%)')
        plt.ylabel('Catch rate')
        plt.savefig(base_name+'_'+ pokemon_name + '.png')
        plt.cla()
