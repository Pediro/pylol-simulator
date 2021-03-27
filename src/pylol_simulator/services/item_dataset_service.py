import urllib.request
import json
from pylol_simulator.services.patch_version_service import get_version

def get_items_dataset():
    
    current_patch = get_version()

    with urllib.request.urlopen(f'http://ddragon.leagueoflegends.com/cdn/{current_patch}/data/en_US/item.json') as f:
        f_data = f.read().decode('utf-8')
        item_dataset = json.loads(f_data)

    item_stats_dataset = {}

    for item in item_dataset['data']:
        item_name = item_dataset['data'][item]['name']
        item_stats = item_dataset['data'][item]['stats']
        item_stats_dataset[item_name] = item_stats

    return item_stats_dataset