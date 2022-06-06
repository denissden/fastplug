import PySimpleGUI as sg
from .config import Config
from .loader import load_plugins

sg.theme('BrightColors')


conf = Config.load()
plugin_paths = conf.get_paths()
load_plugins(plugin_paths)

from .loader import UI

layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')],
            UI
        ]

from . import plugin
print('Commands', plugin.COMMANDS)
# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if handler := plugin.COMMANDS.get(event):
        handler(event, values)

window.close()