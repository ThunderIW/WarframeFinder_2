import requests



def get_planets():
    warframe_planets=[]


    planets = requests.get('https://drops.warframestat.us/data/missionRewards.json').json()

    for Planets_rewards in planets['missionRewards']:
        warframe_planets.append(Planets_rewards)

    for i in warframe_planets:
       rewards = planets['missionRewards'][i]
       for r in rewards:
           print(f"Planet: {i} Node : {r} ")
           print(planets['missionRewards'][i][r]['rewards'])




def get_available_prime():
    current_prime_part=set()

    response_2 = requests.get('https://drops.warframestat.us/data/all.json').json()
    for i in response_2['relics']:
        for r in i['rewards']:
            item_name = r['itemName']
            current_prime_part.add(item_name)

    sorted_prime_list = sorted(current_prime_part)



    for prime in sorted_prime_list:
        if "Prime" not in prime:
            sorted_prime_list.remove(prime)

    return sorted_prime_list

def get_prime_part_relic(item_to_find):
    item_list = {}

    response_2=requests.get('https://drops.warframestat.us/data/all.json').json()

    for i in response_2['relics']:


        relic_info=f"{i['tier']}_{i['relicName']}_{i['state']}"


        for r in i['rewards']:
            item_name = r['itemName']

            rarity_of_getting_item = r['rarity']
            chance_of_getting_item = r['chance']



            if item_name == item_to_find:

                if relic_info in item_list:
                    item_list[relic_info].append((rarity_of_getting_item, chance_of_getting_item))
                else:
                    item_list[relic_info]=[(rarity_of_getting_item, chance_of_getting_item)]



    #for info in relic_info_return_list:



    return item_list

