
import psycopg2
import requests



#response = requests.get('https://api.warframe.market/v1/items').json()
response_2=requests.get('https://drops.warframestat.us/data/all.json').json()
relic_name=set()


for i in response_2['relics']:
    relic_info=f"{i['tier']}_{i['relicName']}"
    print(i['rewards'])
    relic_name.add(relic_info)









#items_name=[i for i in response['payload']['items']['item_name']]
#relic_name_list=[]




# Set your environment variables
PGHOST= 'ep-crimson-term-61485968.us-east-2.aws.neon.tech'
PGDATABASE = 'tableOfInfo'
PGUSER = 'ThunderIW'
PGPASSWORD = 'Bgds0ALIbE1O'

# Establish a connection using environment variables
connection = psycopg2.connect(
    host=PGHOST,
    database=PGDATABASE,
    user=PGUSER,
    password=PGPASSWORD
)
'''
# Create a cursor
cursor = connection.cursor()
cursor.execute("""SELECT * 
FROM Warframe_relic""")
print(cursor.fetchone())

# Now you can use the 'cursor' object to execute SQL queries

# Remember to close the cursor and connection when you're done
cursor.close()
connection.close()
'''