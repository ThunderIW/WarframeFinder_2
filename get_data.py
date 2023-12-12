
import psycopg2
import requests

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



    relic_info_return_dictonary = []

    for i in response_2['relics']:


        relic_info=f"{i['tier']}_{i['relicName']}_{i["state"]}"


        for r in i['rewards']:
            item_name = r['itemName']

            rarity_of_getting_item = r['rarity']
            chance_of_getting_item = r['chance']

            if item_name ==item_to_find:
                item_list[relic_info]=[rarity_of_getting_item,chance_of_getting_item]

    return item_list





























#cursor.execute(f"""INSERT INTO warframe_relic(relic_name) VALUES('{relic_info}')""")
        #connection.commit()

'''
# Create a cursor

cursor.execute("""SELECT * 
FROM Warframe_relic""")
print(cursor.fetchone())

# Now you can use the 'cursor' object to execute SQL queries

# Remember to close the cursor and connection when you're done

'''