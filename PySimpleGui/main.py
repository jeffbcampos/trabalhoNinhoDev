import PySimpleGUI as sg

tela1 = [[sg.Text("Digite o seu nome: "), sg.Input(key=("-Nome-"))], [sg.Button("Entrar")]]

tela2 = [[sg.MLine(size=(50,20), key=("-ChatBox-"))], [sg.Text("Chat: "), sg.Input(key=("-InputChat-"))], [sg.Button("Enviar")]]

layout = [[sg.Column(tela1, key="-Tela1-", visible=True)], [sg.Column(tela2, key=("-Tela2-"), visible=False)]]

window = sg.Window("Nova Janela", layout)

chatLog = ''
usuario = ''

while True:
    event, values = window.read()
    
    if event in ('Fechar', sg.WIN_CLOSED):
        break
    
    if event == "Entrar":
        usuario = values["-Nome-"] + ": "
        window["-Tela1-"].update(visible=False)
        window["-Tela2-"].update(visible=True)
    
    if event == "Enviar":
        texto = values["-InputChat-"]
        chatLog = chatLog + usuario + texto + '\n'
        window["-InputChat-"].update('')
        window["-ChatBox-"].update(chatLog)
    
window.close()