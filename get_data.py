
import psycopg2
import requests
import urllib
import fandom
from bs4 import BeautifulSoup


def get_prime_part_image(item_to_find):

    possible_image=[]
    global t, ImageToDownload
    fandom.set_wiki('warframe')

    # Search for a page (Mirage Prime in this case)
    search_results = fandom.search(item_to_find, results=1)

    # Check if there are search results
    if search_results:
        # Get the page ID from the search results
        page_id = search_results[0][1]

        # Create a FandomPage object
        fandom_page = fandom.FandomPage(wiki='warframe', language='en', pageid=page_id)

        # Create a BeautifulSoup object using the HTML content of the page
        soup = BeautifulSoup(fandom_page.html, 'html.parser')

        # Find all image tags in the HTML
        images = soup.find_all('img')

        # Extract and print the image URLs
        for img in images:
            src = img.get('src')
            if src:
                if f"{item_to_find.replace(" ","")}" in src:
                    possible_image.append(src)
        print(possible_image)
        if len(possible_image)>1:
            ImageToDownload=possible_image[1]

        if len(possible_image)<=1:
            ImageToDownload=possible_image[0]



    else:
        print("No search results found for 'Mirage Prime'.")

    urllib.request.urlretrieve(ImageToDownload, "image.png")





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

#get_prime_part_image('Octavia Prime')