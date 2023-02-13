import PySimpleGUI as sg
from Controle.classConexao import Conexao

con = Conexao()

tela1 = [[sg.Text("Nome: "), sg.Input(key='-Nome-')],
         [sg.Text("Cpf: "), sg.Input(key='-Cpf-')],
         [sg.Text("Salário: "), sg.Input(key='-Salario-')],
         [sg.Text("ID Departamento: "), sg.Input(key='-Id_Dept-')],
         [sg.Text("Cargo: "), sg.Input(key='-Cargo-')],
         [sg.Text("Login: "), sg.Input(key='-Login-')],
         [sg.Text("Senha: "), sg.Input(key='-Senha-', password_char='*')],
         [sg.Button("Enviar")]
         ]


funcionario = list()
signin = list()
print(funcionario)


window = sg.Window("Nova Janela", tela1)

while True:
    event, values = window.read()
    
    if event in ('Fechar', sg.WIN_CLOSED):
        break
    
    if event == 'Enviar':
        funcionario.append((values['-Nome-'], values['-Cpf-'], values['-Salario-'], values['-Id_Dept-'], values['-Cargo-']))
        signin.append((values['-Login-'], values['-Senha-']))
        window['-Nome-'].update('')        
        window['-Cpf-'].update('')        
        window['-Salario-'].update('')
        window['-Id_Dept-'].update('')        
        window['-Cargo-'].update('')
        window['-Login-'].update('')
        window['-Senha-'].update('')
        query = f'''
            INSERT INTO funcionarios (func_nome, func_cpf, func_salario, dept_id, func_cargo) VALUES (
	        '{funcionario[0][0]}', '{funcionario[0][1]}', {funcionario[0][2]}, {funcionario[0][3]}, '{funcionario[0][4]}');'''
        con.queryExecute(query)
        query = f'''SELECT func_id FROM funcionarios WHERE func_cpf = '{funcionario[0][1]}';'''
        id = con.querySelect(query)[0][0]
        query =  f'''INSERT INTO signin (func_id, login, senha) VALUES ('{id}', '{signin[0][0]}', '{signin[0][1]}');'''
        con.queryExecute(query)
        funcionario.clear()
        signin.clear()
        print(funcionario)       
               