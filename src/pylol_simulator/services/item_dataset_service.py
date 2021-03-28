import urllib.request
import json
from pylol_simulator.types.stat import Stat
from pylol_simulator.types.item_stats import Item_Stat

def get_items_dataset():
    
    with urllib.request.urlopen("http://cdn.merakianalytics.com/riot/lol/resources/latest/en-US/items.json") as f:
        f_data = f.read().decode("utf-8")
        item_dataset = json.loads(f_data)

    item_stats_dataset = {}

    for item in item_dataset:
        item_name = item_dataset[item]["name"]
        init_stats(item_dataset[item]["stats"])

    #print(item_stats_dataset["dagger"])

    return item_stats_dataset

def init_stats(item_stats):
    print("\n")
    print(item_stats)
    print(item_stats["abilityPower"])
    print("\n")

    # return Item_Stat(init_stat(item_stats["abilityPower"]),\
    #                 init_stat(item_stats["armor"]),\
    #                 init_stat(item_stats["armorPenetration"]),\
    #                 init_stat(item_stats["attackDamage"]),\
    #                 init_stat(item_stats["attackSpeed"]),\
    #                 init_stat(item_stats["cooldownReduction"]),\
    #                 init_stat(item_stats["criticalStrikeChance"]),\
    #                 init_stat(item_stats["goldPer_10"]),\
    #                 init_stat(item_stats["healAndShieldPower"]),\
    #                 init_stat(item_stats["health"]),\
    #                 init_stat(item_stats["healthRegen"]),\
    #                 init_stat(item_stats["lethality"]),\
    #                 init_stat(item_stats["lifesteal"]),\
    #                 init_stat(item_stats["magicPenetration"]),\
    #                 init_stat(item_stats["magicResistance"]),\
    #                 init_stat(item_stats["mana"]),\
    #                 init_stat(item_stats["manaRegen"]),\
    #                 init_stat(item_stats["movespeed"]),\
    #                 init_stat(item_stats["abilityHaste"]),\
    #                 init_stat(item_stats["omnivamp"]),\
    #                 init_stat(item_stats["tenacity"]))

def init_stat(item_stat):
    return Stat(item_stat["flat"], \
                item_stat["percent"], \
                item_stat["perLevel"], \
                item_stat["percentPerLevel"], \
                item_stat["percentBase"], \
                item_stat["percentBonus"])