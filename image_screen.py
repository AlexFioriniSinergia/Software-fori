import dearpygui.dearpygui as dpg
from image import create_image


def start_screen_image(params):
    texture = create_image(params)

    dpg.delete_item("Prima griglia")
    dpg.delete_item("Seconda griglia")
    dpg.delete_item("Salva")