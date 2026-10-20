from math import isfinite


def exibir_menu():
    print("\n===== Controle de produção =====")
    print("1. Cadastrar registro")
    print("2. Listar todos os registros")
    print("3. Consultar por ID")
    print("4. Atualizar registro")
    print("5. Excluir registro")
    print("6. Mostrar indicadores")
    print("0. Sair")
    return ler_inteiro("Opção: ", minimo=0)


def ler_inteiro(mensagem, minimo=0):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Informe um valor maior ou igual a {minimo}.")
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_decimal(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if isfinite(valor) and valor >= 0:
                return valor
            print("Informe um número finito e não negativo.")
        except ValueError:
            print("Digite um número válido, por exemplo 3,50.")


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("O campo não pode ficar vazio.")


def ler_dados_registro():
    return {
        "setor": ler_texto("Setor: "),
        "produzidas": ler_inteiro("Peças produzidas: "),
        "pecas_rejeitadas": ler_inteiro("Peças rejeitadas: "),
        "custo_unitario": ler_decimal("Custo unitário: "),
    }


def confirmar(mensagem):
    return input(f"{mensagem} (s/n): ").strip().lower() in ("s", "sim")


def exibir_registro(registro):
    print("ID | Setor | Produzidas | Rejeitadas | Custo unitário")
    print(
        f"{registro['id']} | {registro['setor']} | {registro['produzidas']} | "
        f"{registro['pecas_rejeitadas']} | R$ {registro['custo_unitario']:.2f}"
    )


def exibir_registros(registros):
    if not registros:
        print("Nenhum registro cadastrado.")
        return

    print("ID | Setor | Produzidas | Rejeitadas | Custo unitário")
    for registro in registros:
        print(
            f"{registro['id']} | {registro['setor']} | {registro['produzidas']} | "
            f"{registro['pecas_rejeitadas']} | R$ {registro['custo_unitario']:.2f}"
        )


def exibir_indicadores(indicadores):
    print(f"Registros: {indicadores['total_registros']}")
    print(f"Peças produzidas: {indicadores['produzidas']}")
    print(f"Peças rejeitadas: {indicadores['rejeitadas']}")
    print(f"Percentual rejeitado: {indicadores['percentual_rejeitadas']:.2f}%")
    print(f"Custo unitário médio: R$ {indicadores['custo_unitario_medio']:.2f}")