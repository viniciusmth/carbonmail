# interface gráfica
# pysimplegui
from calendar import c
import PySimpleGUI as sg

lista = ["Administradores", "Alunos"]

sg.theme('DarkPurple4')

def get_layout():
    layout = [
        
        [
            sg.Text("Selecione seu código: "),
            sg.In(),
            sg.FileBrowse("Selecione", 
            file_types=(("Arquivos Python", "*.py"),)
            ),   
        ],
        [   sg.Text('Selecione a lista de destinatários'),
            sg.Combo(lista, default_value=lista[1]),
        ],
        [
            sg.Text("Insira um título: "),
            sg.In(key='-Title-'),

        ],
        [
            sg.Text("Insira o conteúdo do E-mail: "),
            sg.In(key="-Content-"),
        ],
        [
            sg.Button("Enviar", key="-Send-"),
            sg.Button("Gerenciar Listas", key="-ListEditor-"),
        ],
    ]
    return layout

def get_window():
    return sg.Window("Teste de Janela", get_layout())