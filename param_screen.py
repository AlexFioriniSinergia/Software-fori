import dearpygui.dearpygui as dpg

x=370
y=250


def start_param_screen():
    dpg.create_context()
    dpg.create_viewport(width=x, height=y*2, resizable=False)
    dpg.setup_dearpygui()



    with dpg.window(label="Prima griglia",  width=x, height=y, no_collapse=True, autosize=True, no_close=True):
        param_options()

    with dpg.window(label="Seconda griglia",  width=x, height=y, pos=[0,y*5/6], no_collapse=True, autosize=True, no_close=True):
        param_options()

    with dpg.window(label="Salva", width=x/4, height=10, pos=[x / 4, y * 18/12], no_collapse=True, autosize=True, no_close=True):
        dpg.add_button(label="Crea immagine", onclick=)

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

def param_options():
    dpg.add_input_text(label="Dimensione x (mm)")
    dpg.add_input_text(label="Dimensione y (mm)")
    dpg.add_input_text(label="Numero fori x")
    dpg.add_input_text(label="Numero fori y")
    dpg.add_input_text(label="Ø fori (mm)")
    dpg.add_input_text(label="Passo (mm)")