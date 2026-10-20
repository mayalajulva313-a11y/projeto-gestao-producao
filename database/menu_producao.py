import sqlite3

from banco import (
    atualizar_no_banco,
    carregar_dados,
    criar_tabela,
    excluir_do_banco,
    inserir_no_banco,
)
from interface import (
    confirmar,
    exibir_indicadores,
    exibir_menu,
    exibir_registro,
    exibir_registros,
    ler_dados_registro,
    ler_inteiro,
)
from regras import (
    buscar_por_id,
    calcular_indicadores,
    gerar_proximo_id,
    validar_registro,
)


def cadastrar_registro(registros):
    registro = ler_dados_registro()
    registro["id"] = gerar_proximo_id(registros)
    erro = validar_registro(registro)
    if erro:
        print(erro)
        return

    try:
        inserir_no_banco(registro)
    except sqlite3.Error as erro_banco:
        print(f"Não foi possível cadastrar o registro: {erro_banco}")
        return

    registros.append(registro)
    print(f"Registro cadastrado com ID {registro['id']}.")


def listar_registros(registros):
    exibir_registros(registros)


def consultar_registro(registros):
    identificador = ler_inteiro("ID do registro: ", minimo=1)
    registro = buscar_por_id(registros, identificador)
    if registro:
        exibir_registro(registro)
    else:
        print("Registro não encontrado.")


def atualizar_registro(registros):
    identificador = ler_inteiro("ID do registro a atualizar: ", minimo=1)
    registro_atual = buscar_por_id(registros, identificador)
    if not registro_atual:
        print("Registro não encontrado.")
        return

    novos_dados = ler_dados_registro()
    novo_registro = {"id": identificador, **novos_dados}
    erro = validar_registro(novo_registro)
    if erro:
        print(erro)
        return

    try:
        atualizado = atualizar_no_banco(novo_registro)
    except sqlite3.Error as erro_banco:
        print(f"Não foi possível atualizar o registro: {erro_banco}")
        return

    if not atualizado:
        print("O registro não foi encontrado no banco; a lista não foi alterada.")
        return

    registro_atual.update(novos_dados)
    print("Registro atualizado.")


def excluir_registro(registros):
    identificador = ler_inteiro("ID do registro a excluir: ", minimo=1)
    registro = buscar_por_id(registros, identificador)
    if not registro:
        print("Registro não encontrado.")
        return
    if not confirmar(f"Confirma a exclusão do registro {identificador}"):
        print("Exclusão cancelada.")
        return

    try:
        excluido = excluir_do_banco(identificador)
    except sqlite3.Error as erro_banco:
        print(f"Não foi possível excluir o registro: {erro_banco}")
        return

    if not excluido:
        print("O registro não foi encontrado no banco; a lista não foi alterada.")
        return

    registros.remove(registro)
    print("Registro excluído.")


def mostrar_indicadores(registros):
    exibir_indicadores(calcular_indicadores(registros))


def main():
    try:
        criar_tabela()
        registros = carregar_dados()
    except sqlite3.Error as erro_banco:
        print(f"Não foi possível iniciar o banco de dados: {erro_banco}")
        return

    while True:
        opcao = exibir_menu()
        if opcao == 0:
            print("Programa encerrado.")
            break
        elif opcao == 1:
            cadastrar_registro(registros)
        elif opcao == 2:
            listar_registros(registros)
        elif opcao == 3:
            consultar_registro(registros)
        elif opcao == 4:
            atualizar_registro(registros)
        elif opcao == 5:
            excluir_registro(registros)
        elif opcao == 6:
            mostrar_indicadores(registros)
        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()