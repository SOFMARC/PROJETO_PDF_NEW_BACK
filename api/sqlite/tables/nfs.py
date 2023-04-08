import sqlite3

connection_database = sqlite3.connect('api/sqlite/database/nfs_database.db')

cursor = connection_database.cursor()

cursor.execute("CREATE TABLE nfs (cnpj_tomador text, razao_tomador text, insc_mun_tomador text, endereco_tomador text, cnpj_prestador text, razao_prestador text, insc_mun_prestador text, endereco_prestador text, inss text, base_calculo text, aliquota text)")

connection_database.commit()
