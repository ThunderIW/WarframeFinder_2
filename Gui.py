import os
import time
import urllib

import dearpygui.dearpygui as dpg
from get_data import get_available_prime,get_prime_part_relic,get_prime_part_image




def clear_table_rows(sender, app_data):
    print(relic_list)
    for relic_name in relic_list.keys():
        row_id = f"row_{relic_name}"
        dpg.delete_item(row_id)





def find_relic(sender,app_data):
    global relic_list

    chosen_prime_part=dpg.get_value('-I-')
    relic=set()

    relic_list=get_prime_part_relic(chosen_prime_part)
    print(relic_list)


    for r in relic_list.keys():
        name=r.split("_")
        relic_info=f"{name[0]}_{name[1]}"
        relic.add(relic_info)



    number_of_relic=len(list(relic))
    dpg.set_value("-number-",number_of_relic)
    dpg.configure_item("-N-",show=True)
    dpg.set_value("-relics-",list(relic))
    dpg.configure_item("-relics-",show=True)

    for relic_name in relic_list.keys():
        row_id = f"row_{relic_name}"
        with dpg.table_row(parent='-RELIC_TABLE-',id=row_id):
            dpg.add_text(relic_name)
            dpg.add_text(relic_list[relic_name][0])
            dpg.add_text(f"{relic_list[relic_name][1]} %")








    dpg.configure_item("-RELIC_TABLE-",show=True)









    #dpg.delete_item('-II-')
    #get_prime_part_image(chosen_prime_part)
    #width, height, channels, data = dpg.load_image("image.png")





dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)





with dpg.window(label="Example Window",tag='w'):




    with dpg.group(horizontal=True):
        dpg.add_text("Prime part to find:")
        dpg.add_combo(items=get_available_prime(),tag='-I-',width=200)
    with dpg.group(horizontal=True):
        dpg.add_button(label="Get relics to farm",callback=find_relic)
        dpg.add_button(label="clear",callback=clear_table_rows)

    with dpg.group(horizontal=True,show=False,tag='-N-'):
        dpg.add_text("Number of relic you need to farm are")
        dpg.add_input_text(tag="-number-",width=20)
    dpg.add_input_text(tag='-relics-',show=False)
    dpg.add_spacer(height=20)



    with dpg.table(header_row=True, resizable=True,policy=dpg.mvTable_SizingStretchProp, borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True
                   ,tag="-RELIC_TABLE-",show=False):
        dpg.add_table_column(label="Relic name",)
        dpg.add_table_column(label="Rarity")
        dpg.add_table_column(label="Chance(%)")









dpg.setup_dearpygui()
dpg.set_primary_window('w',True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()