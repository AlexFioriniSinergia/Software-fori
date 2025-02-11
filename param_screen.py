import dearpygui.dearpygui as dpg
from image_screen import start_screen_image

x=370
y=250


def start_param_screen():
    dpg.create_context()
    dpg.create_viewport(width=x, height=y*2, resizable=False)
    dpg.setup_dearpygui()



    with dpg.window(label="Prima griglia",  width=x, height=y, no_collapse=True, autosize=True, no_close=True):
        param_options("g1")

    with dpg.window(label="Seconda griglia",  width=x, height=y, pos=[0,y*5/6], no_collapse=True, autosize=True, no_close=True):
        param_options("g2")

    with dpg.window(label="Salva", width=x/4, height=10, pos=[x / 4, y * 18/12], no_collapse=True, autosize=True, no_close=True):
        dpg.add_button(label="Crea immagine", callback=launch_image_screen)

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

def param_options(p):
    dpg.add_input_text(label="Dimensione x (mm)", tag=f"{p}_dim_x", decimal=True)
    dpg.add_input_text(label="Dimensione y (mm)", tag=f"{p}_dim_y", decimal=True)
    dpg.add_input_text(label="Numero fori x", tag=f"{p}_num_holes_x", decimal=True)
    dpg.add_input_text(label="Numero fori y", tag=f"{p}_num_holes_y", decimal=True)
    dpg.add_input_text(label="Ø fori (mm)", tag=f"{p}_hole_diameter", decimal=True)
    dpg.add_input_text(label="Passo (mm)", tag=f"{p}_step", decimal=True)

def get_params():
    g1_params = {
        "dim_x": dpg.get_value("g1_dim_x"),
        "dim_y": dpg.get_value("g1_dim_y"),
        "num_holes_x": dpg.get_value("g1_num_holes_x"),
        "num_holes_y": dpg.get_value("g1_num_holes_y"),
        "hole_diameter": dpg.get_value("g1_hole_diameter"),
        "step": dpg.get_value("g1_step")
    }

    g2_params = {
        "dim_x": dpg.get_value("g2_dim_x"),
        "dim_y": dpg.get_value("g2_dim_y"),
        "num_holes_x": dpg.get_value("g2_num_holes_x"),
        "num_holes_y": dpg.get_value("g2_num_holes_y"),
        "hole_diameter": dpg.get_value("g2_hole_diameter"),
        "step": dpg.get_value("g2_step")
    }

    params = [g1_params, g2_params]

    return params


def launch_image_screen():
    start_screen_image(get_params())
