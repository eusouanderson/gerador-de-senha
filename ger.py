from random import randint
import string
from tqdm import tqdm
import time


apresentação = ' \033[35m- Covid 2022 -\033[m'
apresentação_dois = 'Desenvolvido por \033[31mAnderson Rodrigues\033[m'

cont = 0
cont2 = 31
for i in range(0, 16):
    i = 'GERADOR DE SENHA'
    print(f'\033[{cont2}m--' * 12, f'{i[cont]}', '--' * 12)
    if cont2 >= 38:
        cont2 = 31
    cont2 += 1
    cont += 1
    time.sleep(0.30)

print(apresentação, apresentação_dois)


def randonozia():

    while True:

        link = input(
            'Escreva o título da sua senha ou [N] para [exit]: '
        ).upper()
        if link == 'N':
            break

        Todos = list()
        escolha_qtd_carac = int(
            input(
                'Escolha a quantidade de caracteres que deseja usar na sua senha: '
            )
        )
        if escolha_qtd_carac == type(int):
            print('Digite somente numeros nessa parte')
            break
        if escolha_qtd_carac < 8:
            print(
                '\033[7;31;47m[Msg do Sistema]\033[m',
                '\n\033[0;30;47mEscolher um numero de caracteres menor que 8 te dára uma senha fraca sem segurança\033[m',
            )
            perigo = str(input('Deseja continuar ?')).upper()
            if perigo == 'N':
                escolha_qtd_carac = int(
                    input(
                        f'{escolha_qtd_carac} era quantidade de caracteres que desejava usar, deseja alterar para qual valor? '
                    )
                )
                total = len(Todos)
            if perigo == 'S':
                ...
        escolha_do_tipo = int(
            input('Somente letras: [1]\nSomente numeros: [2]\nOs dois: [3]\n ')
        )
        if escolha_do_tipo == 1:
            opcao_de_formatacao = int(
                input(
                    'Digite [1]-Maiusculas [2]-Minusculas [3]-Mista [4]-Mista com caracteres especiais: '
                )
            )
            if opcao_de_formatacao == 1:
                letra_escolhida = string.ascii_uppercase
                print('1')
                msg = 'Maiusculas'
            if opcao_de_formatacao == 2:
                letra_escolhida = string.ascii_lowercase
                msg = 'Minusculas'
                print('2')
            if opcao_de_formatacao == 3:
                letra_escolhida = string.ascii_letters
                msg = 'Mistas'
                print('3')
            if opcao_de_formatacao == 4:
                letra_escolhida = str(string.punctuation * string.ascii_letters)
                msg = 'Letras Mistas com Caracteres especiais'
                print('4')
            cont1 = 0
            for i in range(0, escolha_qtd_carac):
                cont1 += 1
                if cont1 == len(letra_escolhida):
                    cont1 = 0
                C1 = letra_escolhida[randint(0, len(letra_escolhida) - 1)]

                Todos.append(C1)

                letra = "-Caracteres especiais- "
        if escolha_do_tipo == 2:

            for i in range(0, escolha_qtd_carac):
                C2 = randint(0, 9)
                Todos.append(C2)
                letra = 'Numeros'
                msg = ''
        if escolha_do_tipo == 3:
            for i in range(0, escolha_qtd_carac):
                C3 = string.punctuation[
                    randint(0, len(string.punctuation) - 1)
                ]
                C4 = string.digits[randint(0, len(string.digits) - 1)]
                C5 = C4 + C3
                Todos.append(C5)
                letra = 'Numeros com caracteres especiais'
                msg = ''
        total = len(Todos)
        print(
            f' Você selecionou \033[7m{total}\033[m caractéres \033[7m{letra}{msg}\033[m'
        )
        time.sleep(1)
        for i in tqdm(range(10)):
            time.sleep(0.10)
        escolha_segura = str(
            input('Deseja que eu mostre a senha aqui ? [S/N] ')
        ).upper()
        if escolha_segura == 'S':
            print(''.join(map(str, Todos)))
        else:
            print('Senha Gerada e arquivada no bloco de notas...')
        with open('senha.txt', 'a', encoding='utf-8') as txtfile:
            for i in range(1):
                print(
                    f"Local: {link} -- Senha:{''.join(map(str, Todos))} ",
                    file=txtfile,
                )


if __name__ == '__main__':
    randonozia()
