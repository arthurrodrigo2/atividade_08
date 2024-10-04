'''
Crie um programa que faça o cadastro de vários usuários dentro de uma única lista. Ao final, o programa deverá exibir na tela todos os dados de todos os usuários cadastrados. Os dados do usuário a serem cadastrados serão os seguintes:

- Nome
- Idade
- CPF
- E-mail
- Profissão
- Tipo Sanguíneo
- Peso
- Altura
'''

# Lista
usuarios = []

# dados do usuário
def cadastrar_usuario():
    # dicionário
    usuario = {}
    
    # dados do usuário
    usuario['Nome'] = input("Digite o nome: ").strip()
    usuario['Idade'] = int(input("Digite a idade: "))
    usuario['CPF'] = input("Digite o CPF: ").strip()
    usuario['E-mail'] = input("Digite o e-mail: ").strip()
    usuario['Profissão'] = input("Digite a profissão: ").strip()
    usuario['Tipo Sanguíneo'] = input("Digite o tipo sanguíneo: ").strip()
    usuario['Peso'] = float(input("Digite o peso (em kg): "))
    usuario['Altura'] = float(input("Digite a altura (em metros): "))
    
    # dicionário do usuário à lista de usuários
    usuarios.append(usuario)

# função para controle do programa
def main():
    # loop
    while True:
        cadastrar_usuario()
        
        # caso o usuário desejar continuar cadastrando
        continuar = input("Deseja cadastrar outro usuário? (s/n): ").strip().lower()
        # se a resposta não for 's', saímos do loop
        if continuar != 's':
            break
    
    # exibir os dados cadastrados
    print("\nUsuários cadastrados:")
    for usuario in usuarios:
        print("-" * 30)
        for chave, valor in usuario.items():
            print(f"{chave}: {valor}")
    print("-" * 30)

# Chamar a função para iniciar o programa
if __name__ == "__main__":
    main()