#ele é sempre executado ao importa-lo!
from tkinter import font
import PySimpleGUI as sg

def inner_element_space(width=100):
    return [sg.Text(' ' * width)]