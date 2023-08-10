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


    def insert_user(self, name: str, email:str, password:str):
        
        commando = f"""insert into usuarios(name, email, password) values ('{name}', '{email}', '{password}')"""
        self.cursor.execute(commando)
        self.cnxn.commit()

    def get_user(self, email):
        print('get user')
        self.cursor.execute('select u.id, tp2.per_nome, u.email from usuarios u inner join tab_perfil tp2 on u.id_perfil = tp2.per_id where u.email = ?', email)

        return self.cursor.fetchall()

    
    def relatorio(self, id):
        print('relatorio')
        self.cursor.execute('EXEC REL_NOTAFISCAL @id_cliente = ?', id)

        return self.cursor.fetchall()
    

    def get_user_v2(self, email):

        try:
            self.cursor.execute('select u.id , u.nome_usuario, u.email, u.per_id, u.id_cliente, c.empresa  from usuarios u inner join clientes c on c.id = u.id_cliente where u.email = ?', email)
            result = self.cursor.fetchone()
            print("result user", result)
            return result
        
        finally:
            print("hello")

    def get_user_upload(self, user_id):
        try:
            self.cursor.execute('select * from uploads u inner join status s on u.status_id = s.id where u.id_usuario = ?', (user_id))
            res = self.cursor.fetchall()
            return res
        
        finally:
            print("fim")

    def update_status_upload(self, status_id, task_id):
        sql = "UPDATE uploads SET status_id = ? WHERE task_id = ?"
        params = (status_id, task_id)
        self.cursor.execute(sql, params)
        self.cnxn.commit()
    
    def get_upload(self, task_id):

        try:
            self.cursor.execute('select id from uploads u where task_id = ?', (task_id))
        finally:
            print("hello")

        return  self.cursor.fetchall()

    def check_user_login(self, email: str, password:str):
        try:
            self.cursor.execute('SELECT * FROM usuarios where email = ?', (email))
            res = self.cursor.fetchall()
            return res
        finally:
            print("hello")

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
        
        print("insere prestador", commando)

        self.cursor.execute(commando)
        self.cnxn.commit()

    def insert_data_tomador(self, user_id, id_nota, cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomado):
        commando = f"""INSERT INTO SQL_DATA_PDF.dbo.tomadores
                        (id_usuario, id_nota, cnpj_tomador, razao_tomador, insc_mun_tomador, endereco_tomador)
                        VALUES({user_id}, '{id_nota}', '{cnpj_tomador}', '{razao_tomador}', '{insc_mun_tomador}', '{endereco_tomado}')"""


        print("insere tomador", commando)

        self.cursor.execute(commando)
        self.cnxn.commit()

    def insert_nota_fiscal(self, user_id, id_nota, local_incidencia_imposto, descricao_atividades, porcentagem, servicos, deducoes, base_de_calculo, inss, iss_retido, endereco_obra, cno, codigo_servico, valor_total_deducoes, aliquota, valor_total_nota, valor_iss, ir):
        
        commando = f"""
                EXEC INSERT_NOTASFISCAIS 
                @id_usuario = {user_id}, 
                @id_nota = '{id_nota}', 
                @local_incidencia_imposto = '{local_incidencia_imposto}', 
                @descricao_atividades = '{descricao_atividades}',
                @porcentagem = '{porcentagem}', 
                @servicos = '{servicos}',
                @deducoes = '{deducoes}',
                @base_de_calculo = '{base_de_calculo}',
                @inss = '{inss}', 
                @iss_retido = '{iss_retido}',
                @endereco_obra = '{endereco_obra}', 
                @cno = '{cno}',
                @codigo_servico = '{codigo_servico}',
                @valor_total_deducoes = '{valor_total_deducoes}',
                @aliquota = '{aliquota}',
                @valor_total_nota = '{valor_total_nota}', 
                @valor_iss = '{valor_iss}',
                @ir = '{ir}';
        """


        print("####### meu commando ###########", commando)


        self.cursor.execute(commando)
        self.cnxn.commit()
        
        # Recuperar o ID retornado pela procedure
        self.cursor.execute("SELECT @@IDENTITY AS InsertedID;")
        inserted_id = self.cursor.fetchone()[0]

        print("####### meu id ###########", inserted_id)

        return inserted_id
        
        

    def insert_uploads(self, id_usuario, data_upload, nome_arquivo , sucesso, status_id, task_id):

        commando = f"""INSERT INTO SQL_DATA_PDF.dbo.uploads
                        (id_usuario, data_upload, nome_arquivo , sucesso, status_id, task_id)
                        VALUES('{id_usuario}', '{data_upload}', '{nome_arquivo}', '{sucesso}', '{status_id}', '{task_id}')"""

        self.cursor.execute(commando)
        self.cnxn.commit()

        # Recuperar o ID do último registro inserido
        select_command = "SELECT SCOPE_IDENTITY() AS InsertedID"
        self.cursor.execute(select_command)
        inserted_id = self.cursor.fetchone()[0]

        return inserted_id

        

    def insert_uploads_logs(self, id_upload, data_log, descricao):


        commando = f"""INSERT INTO SQL_DATA_PDF.dbo.upload_logs
                        (id_upload, data_log, descricao)
                        VALUES('{id_upload}', '{data_log}', '{descricao}')"""

        print("insert uploads lpgs", commando)

        self.cursor.execute(commando)
        self.cnxn.commit()


    def insert_client(self, empresa):
        commando = f"""insert into clientes (empresa) values ('{empresa}')"""
        self.cursor.execute(commando)
        self.cnxn.commit()

        select_command = "SELECT SCOPE_IDENTITY() AS InsertedID"
        self.cursor.execute(select_command)
        id_cliente = self.cursor.fetchone()[0]

        return id_cliente
    
    
    def insert_tab_perfil(self, per_nome, per_ativo, per_dt_cadastro, per_home):
        commando = f"""insert into tab_perfil (per_nome, per_ativo, per_dt_cadastro, per_home) values ('{per_nome}', '{per_ativo}', '{per_dt_cadastro}', '{per_home}')"""
        self.cursor.execute(commando)
        self.cnxn.commit()

        select_command = "SELECT SCOPE_IDENTITY() AS InsertedID"
        self.cursor.execute(select_command)
        id_perfil = self.cursor.fetchone()[0]

        return id_perfil

    def insert_usuarios(self, id_cliente, per_id, nome_usuario, email, password):

        commando = f"""INSERT INTO usuarios (id_cliente, per_id, nome_usuario, email, password) 
                    VALUES ('{id_cliente}', '{per_id}', '{nome_usuario}', '{email}', '{password}')"""
        
        try:
            self.cursor.execute(commando)
            self.cnxn.commit()

            select_command = "SELECT SCOPE_IDENTITY() AS InsertedID"
            self.cursor.execute(select_command)
            id_user = self.cursor.fetchone()[0]

            return id_user
    
        except Exception as e:
            print('Erro ao inserir na tabela usuarios:', e)
        
        return


    def check_users_inseridos(self, id_cliente):
        try:
            self.cursor.execute('SELECT u.id, u.nome_usuario, u.email from usuarios u  where u.id_cliente = ?', (id_cliente))
            res = self.cursor.fetchall()
            return res
        finally:
            print("hello")



    def delete_users(self, id_usuario):        
        self.cursor.execute('DELETE FROM usuarios WHERE id = ?', (id_usuario))
        self.cnxn.commit()


    def get_logs_uploads(self, id_upload):
        try:
            self.cursor.execute('select * from upload_logs ul where id_upload = ?', (id_upload))
            res = self.cursor.fetchall()
            return res
        finally:
            print("hello")




    