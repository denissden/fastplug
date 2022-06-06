import PySimpleGUI as sg
import fastplug.plugin as plugin

"""
doc dodc doc
"""
NAME = 'foo'
COMMANDS = {}

UI = [
    [sg.Text("Some test text"), s_b := sg.Button("Some button", key='-test-')],
    [sg.Input(key='-INPUT-'),]
    ]

def init():
    print()

@plugin.reg(s_b)
def test_command(_, __):
    print("test_command")