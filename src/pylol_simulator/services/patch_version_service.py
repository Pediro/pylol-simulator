import urllib.request
from ast import literal_eval

def get_version():
    with urllib.request.urlopen('https://ddragon.leagueoflegends.com/api/versions.json') as f:
        f_data = f.read().decode('utf-8')
        version_array = literal_eval(f_data)
        return version_array[0]