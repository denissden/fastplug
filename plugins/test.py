import PySimpleGUI as sg
import fastplug.plugin as plugin

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
        rad := sg.Radio("Radio button sample", 1, key='-radio-'),
        rad2 := sg.Radio("Another one", 1, key='-radio2-'),
    ]
]

rad.ChangeSubmits = True
rad2.ChangeSubmits = True

@plugin.command('-radio-')
def radio(event, values):
    print('RADIO:', event, values)

def init():
    pass