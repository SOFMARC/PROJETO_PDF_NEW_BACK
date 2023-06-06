import json
from datetime import date

from src.Interface.Api.utils.uuid import Id
from src.Infra.External.pyodbc.index import Database
from src.Interface.Api.works.work_template_nfs_sp import work_template_nfs_sp
from src.Interface.Api.works.work_template_nfs_cajamar import work_template_nfs_cajamar
from src.Interface.Api.works.work_template_nfs_trindade import work_template_nfs_trindade
from src.Interface.Api.works.work_template_nfs_bassano import work_template_nfs_bassano
from src.Interface.Api.works.work_template_nfs_osasco import work_template_nfs_osasco
from src.Interface.Api.works.work_template_nfs_biguacu import work_template_nfs_biguacu
from src.Interface.Api.works.work_template_nfs_suzanu import work_template_nfs_suzanu
from src.Infra.Database.NotaFiscalRepository import NotaFiscalRepositoryInfra


works = [
        work_template_nfs_osasco,
        work_template_nfs_cajamar, 
        work_template_nfs_trindade, 
        work_template_nfs_bassano,
        work_template_nfs_sp,
        work_template_nfs_biguacu,
        work_template_nfs_suzanu 
]

def work_controller(filepath, filename, filepathimage, user_id, task_id):
    i = 0
    while(i < len(works)):
        res = works[i](filepath, filename, filepathimage)
        
        print( "########## fim da extração ########", res != 400 and 200 or 400 )
        
        if res != 400:
            data = insert_nfs(res, user_id, task_id)
            
            return data
        
        i += 1  
        

def insert_nfs(data, user_id, task_id):
    print("####################### dados chegouu  #######################")
    try:
        
        ("####################### dados chegouu v222  #######################")
        
        info = json.loads(data)

        print("CNPJ Tomador:", info['cnpj_tomador'])
        print("Razão Tomador:", info['razao_tomador'])
        print("Inscrição Municipal Tomador:", info['insc_mun_tomador'])
        print("Endereço Tomador:", info['endereco_tomador'])
        print("CNPJ Prestador:", info['cnpj_prestador'])
        print("Razão Prestador:", info['razao_prestador'])
        print("Inscrição Municipal Prestador:", info['insc_mun_prestador'])
        print("Endereço Prestador:", info['endereco_prestador'])
        print("Local de Incidência do Imposto:", info['local_incidencia_imposto'])
        print("Descrição das Atividades:", info['descricao_atividades'])
        print("Porcentagem:", info['porcentagem'])
        print("Serviços:", info['servicos'])
        print("Deduções:", info['deducoes'])
        print("Base de Cálculo:", info['base_de_calculo'])
        print("INSS:", info['inss'])
        print("ISS Retido:", info['iss_retido'])
        print("Endereço da Obra:", info['endereco_obra'])
        print("CNO:", info['cno'])
        print("Código do Serviço:", info['codigo_servico'])
        print("Valor Total de Deduções:", info['valor_total_deducoes'])
        print("Alíquota:", info['aliquota'])
        print("Valor Total da Nota:", info['valor_total_nota'])
        print("Valor do ISS:", info['valor_iss'])
        print("IR:", info['ir'])

        unique_id:int = Id()

        user_id = user_id

        database = Database()

        db = NotaFiscalRepositoryInfra(database)

        database.connect()

        id_nota = db.save(user_id, unique_id, info['local_incidencia_imposto'], info['descricao_atividades'], info['porcentagem'], info['servicos'], info['deducoes'], info['base_de_calculo'], info['inss'], info['iss_retido'], info['endereco_obra'], info['cno'], info['codigo_servico'],info['valor_total_deducoes'], info['aliquota'], info['valor_total_nota'],  info['valor_iss'], info['ir'])
        
        print("##################################### resultado ##################################### ", id_nota)

        database.close()

        database.connect()

        db.insert_data_tomador(user_id, id_nota,  info['cnpj_tomador'], info['razao_tomador'], info['insc_mun_tomador'], info['endereco_tomador'])
        
        database.close()

        database.connect()

        db.insert_data_prestacao(user_id, id_nota, info['cnpj_prestador'], info['razao_prestador'], info['insc_mun_prestador'], info['endereco_prestador'])

        database.close()

        for key, value in info.items():
            if value == "nao informado":
                print("######################Valor não informado para a propriedade:######################", key)
                db_v2 = Database()

                db_v2.connect()

                id = db_v2.get_upload(task_id)

                print("id", id[0][0])

                db_v2.close()

                db_v2.connect()

                res = f"Não foi possivel extrair o valor da propriedade: {key}"
                print(res)

                db_v2.insert_uploads_logs(id[0][0], date.today(), res)
                
                db_v2.close()
            else:
                db_v2 = Database()

                db_v2.connect()

                id = db_v2.get_upload(task_id)

                print("id", id[0][0])

                db_v2.close()

                db_v2.connect()

                res = f"Extraido com sucesso: {key}"
                print(res)

                db_v2.insert_uploads_logs(id[0][0], date.today(), res)
                
                db_v2.close()

        return 200
        
    except:
        print("error nao foi posiivel")
        
        return 400