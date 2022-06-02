import PySimpleGUI as sg
import fastplugin.plugin as plugin

"""
doc dodc doc
"""
NAME = 'foo'
COMMANDS = {}

UI = [
    [sg.Text("Some test text"), sg.Button("Some button", key='-test-')],
    [sg.Input(key='-INPUT-'),]
    ]

def init():
    print()

@plugin.command("-test-")
def test_command(_, __):
    print("test_command")