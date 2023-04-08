import sqlite3
from provider.index import database_connection

def insert_nfs_database(cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomador, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador, inss, base_calculo, aliquota):
    connection_database = database_connection()
    cursor = connection_database.cursor()

    cursor.execute("""
    INSERT INTO nfs (cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomador, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador, inss, base_calculo, aliquota)
    VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, (cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomador, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador, inss, base_calculo, aliquota ))    
    connection_database.commit()

    return 200

def insert_user_database(name, email, password):
    print("vou inserir", name, email, password)
    connection_database = database_connection()
    cursor = connection_database.cursor()
    cursor.execute("""
    INSERT INTO users (name, email, password)
    VALUES (?,?,?)
    """, (name, email, password))
    connection_database.commit()
    
    return 200
    
def get_user_database():
    connection_database = database_connection()
    cursor = connection_database.cursor()
    cursor.execute("SELECT email FROM users")
    connection_database.commit()
    
    return cursor.fetchall()

def check_user_login(email, password):
    connection_database = database_connection()
    cursor = connection_database.cursor()
    cursor.execute('SELECT * FROM users where email == ? and password == ?', (email, password))
    connection_database.commit()
    
    return cursor.fetchone()