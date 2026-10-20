# projeto-gestao-producao

Sistema de controle de produção em Python com banco de dados SQLite.

## Como executar

Na raiz do projeto, execute:

```bash
python database/menu_producao.py
```

O banco `database/producao_db.sqlite` é criado automaticamente se ainda não existir.

O programa carrega os registros em uma lista de dicionários ao iniciar. Consultas e indicadores usam essa lista; cada inclusão, atualização ou exclusão é gravada primeiro no SQLite e só então refletida na memória.

## Organização

- `database/menu_producao.py`: inicialização e fluxo do menu
- `database/banco.py`: conexão, criação da tabela e operações SQLite
- `database/interface.py`: menu, entradas e exibição
- `database/regras.py`: validações, busca e cálculos

## Funções disponíveis

- Cadastrar registros de produção
- Listar todos os registros
- Consultar, atualizar e excluir por ID
- Exibir indicadores de produção e rejeição