import PySimpleGUI as sg 

def start_gui():
    sg.ChangeLookAndFeel('Reds')
    sg.set_options(text_justification='left')
    layout = [[sg.Text('hej hej', font=('Helvetica', 35))]]


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    event, values = window.read()


start_gui()

