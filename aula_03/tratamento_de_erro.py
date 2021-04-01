def funcao_que_lanca_excecao():
    return
    raise Exception('Erro da função')

if __name__ == '__main__':
    try:
        funcao_que_lanca_excecao()
    except Exception as error:
        print(error.args)
    else:
        print('Não ocorreu erro')
    finally:
        print('Sempre executa')
