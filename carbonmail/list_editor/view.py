import PySimpleGUI as sg
from carbonmail.utils import inner_element_space

lista = ['Administradores', 'Alunos']

def get_layout():
    frame_list = [
        inner_element_space(150),
        [
            sg.Text('Selecione a lista: '),
            sg.Combo(lista, default_value=lista[1], key = '-List-')
        ],
        [
            sg.Text('Criar uma lista:'),
            sg.In(key='-ListName-'),
            sg.Button('Criar', key='-Create-', size=(10,1)),
        ],
        [
            sg.Button('Deletar a Lista',
            key = '-Delete-',
            size=(15,1),
            pad=(5,(7,7))
            ),
            sg.Button('Mostrar Contatos',
            key="-Show-",
            size=(15,1),
            pad=(5, (7,7))
            ),
        ],
        inner_element_space(150),
    ]

    frame_add = [
        inner_element_space(150),
        [
            sg.Text('Insira o nome:  ', 
            pad=(0, (0, 7))
            ),
            sg.In(key='-Name-', 
            pad=(0, (0, 7))
            )
        ],
        [
            sg.Text('Insira o e-mail:', pad=((7, 0), (0, 0))),
            sg.In(key='-Email-')
        ],
        inner_element_space(150),
    ]

    frame_import = [
        inner_element_space(150),
        [
            sg.Text('Selecione o arquivo (CSV):', tooltip='Cabeçalhos: name e email'),
            sg.In(key='-CSV-'),
            sg.FileBrowse('Selecionar', file_types=(("CSV", "*.csv"),),
            tooltip='Cabeçalhos: name e email',
            ),
        ],
        [
            sg.Button(
                'Importar Contatos',
                key='-Import-',
                size=(15,1),
                pad=(5, (7, 7))
            )
        ],
        inner_element_space(150),
    ]
    
    layout = [
        [
            sg.Frame('Configurações da Lista',frame_list, element_justification='c')
        ],
        [
            sg.Frame('Importar Contatos', frame_import, element_justification='c')
        ],
        [
            sg.Frame('Adicionar Anfitrião', frame_add, element_justification='c')
        ]   
    ]
    return layout


def get_window():
    return sg.Window('Editor de Lista', get_layout(), element_justification='c')