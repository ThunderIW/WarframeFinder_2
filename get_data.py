
import psycopg2
import requests

def get_available_prime():
    current_prime_part=[]
    response_2 = requests.get('https://drops.warframestat.us/data/all.json').json()
    for i in response_2['relics']:
        for r in i['rewards']:
            item_name = r['itemName']
            current_prime_part.append(item_name)


    print(f"There are {len(current_prime_part)} prime_parts  to get/farm ")
    return current_prime_part




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




query=get_prime_part_relic('Braton Prime Stock')
t=get_available_prime()






















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