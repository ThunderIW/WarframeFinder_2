

import requests
import fandom
from bs4 import BeautifulSoup
import csv
import urllib.request


def get_prime_part_image(item_to_find):

    #word=str(item_to_find).split(" ")
    #modified_word=f"{word[0]} {word[1]}"
    #print(modified_word)
    fandom.set_wiki('warframe')

    # Search for a page (Mirage Prime in this case)
    search_results = fandom.search(item_to_find, results=1)

    # Check if there are search results
    if search_results:
        # Get the page ID from the search results
        id = search_results[0][1]
        print(id)
        page_to_use=fandom.page(pageid=id)
        fandom_url=page_to_use.url

        reponse=requests.get(fandom_url)
        soup=BeautifulSoup(reponse.text,'html.parser')

        image_tags=soup.find_all('img')

        for images in image_tags:
            img_url=images.get('src')
            #print(img_url)
            text=f"{item_to_find}Full.png"
            new_image=text.replace(" ","")

            if new_image in img_url:
                download_img=img_url

    urllib.request.urlretrieve(download_img,f"{item_to_find}.png")







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



    relic_info_return_list = []

    for i in response_2['relics']:


        relic_info=f"{i['tier']}_{i['relicName']}_{i["state"]}"


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










