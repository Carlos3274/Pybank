from pybank_classes import Pybank
from tkinter.constants import HIDDEN
from PySimpleGUI import PySimpleGUI as sg

banco = Pybank()

# janelas
def janela_login():
    sg.theme('Reddit')
    layout = [
        
        [sg.Text('Nome'),sg.Input(key = 'nome',size=(20,1))],
        [sg.Text('Usuario'),sg.Input(key='usuario',size=(20,1))],
        [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(20,1))],
        [sg.Checkbox('Salvar o login')],
        [sg.Button('Entrar'),sg.Button('Cadastrar')]
        

    ]
    return sg.Window('Login',layout = layout,finalize = True)

def janela_cadastro():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome'),sg.Input(key='nome_cad',size=(20,1))],
        [sg.Text('Usuario'),sg.Input(key='user_cad',size=(20,1))],
        [sg.Text('Senha'),sg.Input(key='senha_cad',password_char='*',size=(20,1))],
        [sg.Text('Confirmar senha'),sg.Input(key='senha_confirm',password_char='*',size=(20,1))],
        [sg.Button('Salvar'),sg.Button('Voltar')]
        
    ]
    return sg.Window('Cadastro',layout = layout,finalize = True)

def janela_menu():
    sg.theme('Reddit')
    layout = [
        [sg.Button('Deposito')],
        [sg.Button('Saque')],
        [sg.Button('Transferência')],
        [sg.Button('Acessar Dados')],
        [sg.Button('Voltar')]

    ]
    return sg.Window('Menu',layout = layout,finalize = True)
def janela_deposito():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Valor'),sg.Input(key='Valor_deposito')],
        [sg.Button('Depositar')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Deposito',layout = layout,finalize = True)
def janela_saque():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Valor'),sg.Input(key='Valor_saque')],
        [sg.Button('Sacar')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Saque',layout = layout,finalize = True)
def janela_dados():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome:'),sg.Text(nome)],
        [sg.Text('Usuario'),sg.Text(usuario)],
        [sg.Text('Saldo:'),sg.Text(str(banco.saldo))],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Dados',layout = layout,finalize = True)
def janela_transferir():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Valor'),sg.Input(key='Valor_transferir')],
        [sg.Text('Usuario destino'),sg.Input(key='Usuario_destino')],
        [sg.Button('Voltar'),sg.Button('Transferir')]
    ]
    return sg.Window('Transferir',layout = layout,finalize = True)

 # Criação das janela inicial
janela1, janela2, janela3, janela4 , janela5, janela6, janela7 = janela_login(), None, None, None, None, None, None

# loop de leitura de eventos

while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela é fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == sg.WIN_CLOSED:
        break
    if window == janela5 and event == sg.WIN_CLOSED:
        break
    if window == janela6 and event == sg.WIN_CLOSED:
        break
    if window == janela7 and event == sg.WIN_CLOSED:
        break
    
    # Quando ir para a próxima janela
    

    if window == janela1 and event == 'Cadastrar':
        janela1.hide()
        janela2 = janela_cadastro()
    if window == janela1 and event == 'Entrar':
        nome = values['nome']
        usuario = values['usuario']
        senha = values['senha']
        banco.login(nome, usuario, senha)
        if banco.logado == True:
            janela1.hide()
            janela3 = janela_menu()
            
            
            
        else:
            sg.popup('Dados inválidos, digite novamente')
     
            
    if window == janela2 and event == 'Voltar':    
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Salvar':
        nome_cad = values['nome_cad']
        user_cad = values['user_cad']
        senha_cad = values['senha_cad']
        senha_confirm = values['senha_confirm']

        if senha_confirm == senha_cad:
            banco.cadastro(nome_cad,user_cad,senha_cad,100)
            sg.popup('Cadastro efetivado!')
        else:
            sg.popup('Dados inválidos')

    if window == janela3 and event == 'Deposito':
        janela3.hide()
        janela4 = janela_deposito()
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()
    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela3.un_hide()
    if window == janela4 and event == 'Depositar':
        nome_dep = banco.nome
        valor_depositado = int(values['Valor_deposito'])   
        banco.depositar(valor_depositado, nome_dep) 
        sg.popup(f'Foram depositados {valor_depositado} reais em sua conta!')
    if window == janela3 and event == 'Saque':
        janela3.hide()
        janela5 = janela_saque()
    if window == janela5 and event == 'Sacar':
        nome_saq = banco.nome
        valor_sacado = int(values['Valor_saque'])
        banco.sacar(valor_sacado,nome_saq)
        if banco.boolean_saq == True:
            sg.popup(f'Foi realizado o saque de {valor_sacado} reais!')
        else:
            sg.popup('Dados inválidos, digite novamente!')
    if window == janela5 and event == 'Voltar':
        janela5.hide()
        janela3.un_hide()
    if window == janela3 and event == 'Transferência':
        janela3.hide()
        janela7 = janela_transferir()
    if window == janela7 and event == 'Transferir':
        valor_transferido = int(values['Valor_transferir'])
        usuario_destinado = values['Usuario_destino']
        banco.transferir(valor_transferido,usuario_destinado)
        sg.popup(f'Foram transferidos {valor_transferido} para a conta de {usuario_destinado}')
    if window == janela7 and event == 'Voltar':
        janela7.hide()
        janela3.un_hide()
    if window == janela3 and event == 'Acessar Dados':
        janela3.hide()
        banco.atualizar_saldo()
        janela6 = janela_dados()
        
        
         
    if window == janela6 and event == 'Voltar':
        janela6.hide()
        janela3.un_hide()
        

        



            
            







    
    
