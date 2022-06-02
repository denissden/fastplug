import PySimpleGUI as sg

sg.theme('BrightColors')
from .loader import main, PLUGINS, UI, PLUGIN_COMMANDS

main()

COMMANDS = {}

for name, commands in PLUGINS.items():
    COMMANDS = COMMANDS | commands


def run(name: str):
    command = COMMANDS.get(name.replace('-command-', ''))
    if command is not None:
        command()

c_buttons = [sg.Button(name, key="-command-"+name) for name in commands]

layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')],
            c_buttons,
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
    if handler := PLUGIN_COMMANDS.get(event):
        handler(event, values)
    run(event)
    print(event, values)

window.close()