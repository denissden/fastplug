import PySimpleGUI as sg
import fastplugin.plugin as plugin

NAME = 'test'

@plugin.command('2args', ['click1', 'text_input'])
def two_args(a, b):
    print(a, b, '::2 args')

@plugin.command('Lol!')
def lol(a, _):
    print(a, 'lol')

# COMMANDS = {
#     "test": lambda a: print(a, 'test'),
#     "args": two_args
# }

COMMANDS = {
    "test": lambda: print("test"),
    "hello world": lambda: print("hello world")
}

UI = [
    [
        sg.Radio("Radio button sample", 1, key='-radio-', enable_events=True),
        sg.Radio("Another one", 1, key='-radio-', enable_events=True),
    ]
]


@plugin.command('-radio-')
def radio(event, values):
    print('RADIO:', event, values)

def init():
    pass