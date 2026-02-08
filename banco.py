import sqlite3

# Nome do arquivo do banco de dados
DB_NAME = "clube.db"

def conectar():
    """Conecta ao banco de dados SQLite."""
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    """Cria a tabela se ela não existir."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            plano TEXT NOT NULL,
            ativo BOOLEAN NOT NULL DEFAULT 1
        )
    """)
    conn.commit()
    conn.close()

def adicionar_socio(nome, cpf, plano):
    try:
        conn = conectar()
        cursor = conn.cursor()
        # Usamos ? para evitar SQL Injection (Segurança)
        cursor.execute("INSERT INTO socios (nome, cpf, plano) VALUES (?, ?, ?)", (nome, cpf, plano))
        conn.commit()
        print(f"✅ Sócio {nome} cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print(f"❌ Erro: Já existe um sócio com o CPF {cpf}.")
    finally:
        conn.close()

def listar_socios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM socios")
    socios = cursor.fetchall()
    conn.close()
    return socios

def atualizar_status(id_socio, novo_status):
    """Ativa (1) ou Desativa (0) um sócio"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE socios SET ativo = ? WHERE id = ?", (novo_status, id_socio))
    conn.commit()
    conn.close()
    print("✅ Status atualizado.")

def deletar_socio(id_socio):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM socios WHERE id = ?", (id_socio,))
    conn.commit()
    conn.close()
    print("🗑️ Sócio removido.")