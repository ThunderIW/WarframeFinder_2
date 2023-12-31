import streamlit as st
from getting_data import get_available_prime,get_prime_part_relic
import pandas as pd
from time import sleep
from stqdm import stqdm

# Initialize session_state
if "i" not in st.session_state:
    st.session_state.i = None


def set_data():
    relic_list=[]
    chance_info=[]
    number_list=[]
    choice=st.session_state.get("-i-")
    relics=get_prime_part_relic(choice)
    for relic in relics.keys():
        relic_list.append(relic)
        chance_info.append(relics[relic][0][0])
        number_list.append(relics[relic][0][1])
    relic_info=pd.DataFrame({
        "Relic name": relic_list,
        "Chance": chance_info,
        "Chance of getting item(%)": number_list
    })
    return  relic_info









primes = get_available_prime()

st.title("WarframeFinder")
st.text("You can select the item you want from the box below or type in the item\nyou want to find")
prime_part = st.selectbox(label="Choose the part you want to get", options=primes, key="-i-")
get_item=st.button(label="Get Relics")
if get_item:
    for _ in stqdm(range(50),desc=f"Getting relics for {prime_part}"):
        sleep(0.3)
    table=set_data()
    st.dataframe(table)


