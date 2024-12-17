import sqlite3

db_path = "projeto.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS TbContratos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_acordo INTEGER NOT NULL,
    id_contrato INTEGER NOT NULL,
    id_boleto INTEGER NOT NULL,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    idade INTEGER,
    valor_emprestimo TEXT,
    total_parcelas INTEGER,
    parcela_atual INTEGER NOT NULL,
    valor_parcela TEXT,
    valor_total  TEXT,
    dias_atraso INTEGER
)
""")

conn.commit()
conn.close()

print(f"Banco de dados criado em: {db_path}")
