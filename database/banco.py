import sqlite3
from pathlib import Path


CAMINHO_BANCO = Path(__file__).with_name("producao_db.sqlite")


def conectar():
    return sqlite3.connect(CAMINHO_BANCO)


def criar_tabela():
    with conectar() as conexao:
        conexao.execute(
            """CREATE TABLE IF NOT EXISTS producao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                setor TEXT NOT NULL,
                produzidas INTEGER NOT NULL DEFAULT 0,
                pecas_rejeitadas INTEGER NOT NULL DEFAULT 0,
                custo_unitario REAL NOT NULL DEFAULT 0
            )"""
        )


def carregar_dados():
    with conectar() as conexao:
        conexao.row_factory = sqlite3.Row
        linhas = conexao.execute(
            """SELECT id, setor, produzidas, pecas_rejeitadas, custo_unitario
               FROM producao ORDER BY id"""
        ).fetchall()
    return [dict(linha) for linha in linhas]


def inserir_no_banco(registro):
    with conectar() as conexao:
        conexao.execute(
            """INSERT INTO producao
               (id, setor, produzidas, pecas_rejeitadas, custo_unitario)
               VALUES (?, ?, ?, ?, ?)""",
            (
                registro["id"],
                registro["setor"],
                registro["produzidas"],
                registro["pecas_rejeitadas"],
                registro["custo_unitario"],
            ),
        )
    return True


def atualizar_no_banco(registro):
    with conectar() as conexao:
        cursor = conexao.execute(
            """UPDATE producao
               SET setor = ?, produzidas = ?, pecas_rejeitadas = ?, custo_unitario = ?
               WHERE id = ?""",
            (
                registro["setor"],
                registro["produzidas"],
                registro["pecas_rejeitadas"],
                registro["custo_unitario"],
                registro["id"],
            ),
        )
    return cursor.rowcount > 0


def excluir_do_banco(identificador):
    with conectar() as conexao:
        cursor = conexao.execute(
            "DELETE FROM producao WHERE id = ?", (identificador,)
        )
    return cursor.rowcount > 0