import sqlite3

# Caminho do banco de dados
db_path = "projeto.db"

# Dados a serem inseridos
usuarios = [
    (532626, 74374374353, 50043432777, "João Silva", "joao.silva@example.com", 30, 3000, 12, 3, 290, 3480, 0),
    (256628, 85948502871, 50078272311, "Maria Souza", "maria.souza@example.com", 25, 1250, 6, 2, 241, 1450,5),
    (132111, 71773859930, 50029889889, "Carlos Santos", "carlos.santos@example.com", 40, 2900, 24, 24, 140, 3360, 10),
]

# Conexão com o banco de dados
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Inserir os dados
try:
    cursor.executemany("""
    INSERT INTO TbContratos (
        id_acordo, id_contrato, id_boleto, nome, email, idade, valor_emprestimo, total_parcelas, parcela_atual, valor_parcela, valor_total, dias_atraso
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, usuarios)
    conn.commit()
    print("Usuários adicionados com sucesso!")
except sqlite3.IntegrityError as e:
    print(f"Erro ao inserir dados: {e}")
finally:
    conn.close()