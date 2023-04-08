import pyodbc

class Database:
    def __init__(self):
        self.server =  'serverpdf.database.windows.net'
        self.database = 'SQL_DATA_PDF'
        self.username = 'tsilva'
        self.password = 'N78mN4ykxHuskgx'
        self.driver = '{ODBC Driver 18 for SQL Server}'

    def connect(self):
        cnxn_str = f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
        self.cnxn = pyodbc.connect(cnxn_str)
        self.cursor = self.cnxn.cursor()

    def close(self):
        self.cursor.close()
        self.cnxn.close()

    def insert_data(self, name: str, email:str, password:str):
        commando = f"""insert into users(name, email, password) values ('{name}', '{email}', '{password}')"""
        self.cursor.execute(commando)
        self.cnxn.commit()

    def get_user(self, email):
        self.cursor.execute('SELECT email FROM users where email = ?', (email))
    
        return  self.cursor.fetchall()

    def check_user_login(self, email: str, password:str):
        print(email, password)
        self.cursor.execute('SELECT * FROM users where email = ?', (email))

        return  self.cursor.fetchall()

    def insert_nfs_database(self, cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomador, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador, inss, base_calculo, aliquota):
        self.cursor.execute("""
        INSERT INTO nfs (cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomador, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador, inss, base_calculo, aliquota)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
        """, (cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomador, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador, inss, base_calculo, aliquota ))    
        
        self.cnxn.commit()

        return 200

    def insert_data_prestacao(self, user_id, id_nota, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador):
        commando = f"""INSERT INTO SQL_DATA_PDF.dbo.prestadores
                        (id_usuario, id_nota, cnpj_prestador, razao_prestador, insc_mun_prestador, endereco_prestador)
                        VALUES({user_id}, '{id_nota}', '{cnpj_prestador}', '{razao_prestador}', '{insc_mun_prestador}', '{endereco_prestador}')"""

        self.cursor.execute(commando)
        self.cnxn.commit()

    def insert_data_tomador(self, user_id, id_nota, cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomado):
        commando = f"""INSERT INTO SQL_DATA_PDF.dbo.tomadores
                        (id_usuario, id_nota, cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomador)
                        VALUES({user_id}, '{id_nota}', '{cnpj_tomador}', '{razao_tomador}', '{insc_mun_tomador}', '{endereco_tomado}')"""

        self.cursor.execute(commando)
        self.cnxn.commit()

    def insert_nota_fiscal(self, user_id, id_nota, local_incidencia_imposto, descricao_atividades, porcentagem, servicos, deducoes, base_de_calculo, inss, iss_retido, endereco_obra, cno, codigo_servico, valor_total_deducoes, aliquota, valor_total_nota, valor_iss, ir):
        print(user_id, id_nota, local_incidencia_imposto, descricao_atividades, porcentagem, servicos, deducoes, base_de_calculo, inss, iss_retido, endereco_obra, cno, codigo_servico, valor_total_deducoes, aliquota, valor_total_nota, valor_iss, ir)
        commando = f"""INSERT INTO SQL_DATA_PDF.dbo.notas_fiscais
                        (id_usuario, id_nota, local_incidencia_imposto, descricao_atividades, porcentagem, servicos, deducoes, base_de_calculo, inss, iss_retido, endereco_obra, cno, codigo_servico, valor_total_deducoes, aliquota, valor_total_nota, valor_iss, ir)  
                        VALUES({user_id}, '{id_nota}', '{local_incidencia_imposto}', '{descricao_atividades}', '{porcentagem}', '{servicos}', '{deducoes}', '{base_de_calculo}', '{inss}', '{iss_retido}', '{endereco_obra}', '{cno}', '{codigo_servico}', '{valor_total_deducoes}', '{aliquota}', '{valor_total_nota}', '{valor_iss}', '{ir}')"""
        
        self.cursor.execute(commando)
        self.cnxn.commit()


    