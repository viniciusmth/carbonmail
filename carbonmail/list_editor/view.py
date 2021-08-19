import PySimpleGUI as sg

lista = ['Administradores', 'Alunos']

def get_layout():
    frame_list = [
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
            sg.Text(' ')
        ],
        [
            sg.Button('Deletar a Lista',
            key = '-Delete-',
            size=(15,1)
            ),
            sg.Button('Mostrar Contatos',
            key="-Show-",
            size=(15,1)
            ),
        ]

    ]

    frame_import = [
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
                size=(15,1)
            )
        ]
    ]
    
    layout = [
        [
            sg.Frame('Configurações da Lista',frame_list, element_justification='c')
        ],
        [
            sg.Frame('Importar Contatos', frame_import, element_justification='c')
        ]
    ]
    return layout


def get_window():
    return sg.Window('Editor de Lista', get_layout(), element_justification='c')