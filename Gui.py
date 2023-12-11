

import dearpygui.dearpygui as dpg
from get_data import get_available_prime

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

with dpg.window(label="Example Window",tag='w'):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.setup_dearpygui()
dpg.set_primary_window('w',True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()