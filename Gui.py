

import dearpygui.dearpygui as dpg
from get_data import get_available_prime,get_prime_part_relic


def find_relic(sender,app_data):
    chosen_prime_part=dpg.get_value('-I-')

    relic_list=get_prime_part_relic(chosen_prime_part)

    for relic_name in relic_list.keys():
        with dpg.table_row(parent='-RELIC_TABLE-'):
            dpg.add_text(relic_name)
            dpg.add_text(relic_list[relic_name][0])
            dpg.add_text(f"{relic_list[relic_name][1]} %")


    dpg.configure_item("-RELIC_TABLE-",show=True)






dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

with dpg.window(label="Example Window",tag='w'):
    with dpg.group(horizontal=True):
        dpg.add_text("Prime part to find:")
        dpg.add_combo(items=get_available_prime(),tag='-I-')

    dpg.add_button(label="Get relics to farm",callback=find_relic)
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