import re
import json
from src.Interface.Api.utils.convert import pdf_to_text
from src.Interface.Api.utils.clear import clear_array_empty
from src.Interface.Api.utils.clear import clear_blank_lines
from src.Interface.Api.utils.string import empy_text_column
from src.Interface.Api.utils.clear import clear_folder_upload
from src.Interface.Api.utils.searchInformationText import searchInformationText

def work_template_nfs_bassano(file, filename, filepathimage):
    print("############# work_template_nfs3_bassano Bassano ##############")
    try:
        removeCaracter = pdf_to_text(file)

        busca_prestador = searchInformationText("Prestador do serviço((.*(\n|\r|\r\n)){15})", removeCaracter)
        busca_tomador = searchInformationText("Tomador do serviço((.*(\n|\r|\r\n)){15})", removeCaracter)
        busca_line_values_liquido = searchInformationText("(?<=Liquido)((.*(\n|\r|\r\n)){8})", removeCaracter)
        busca_line_values_irrf = searchInformationText("(?<=IRRF)((.*(\n|\r|\r\n)){7})", removeCaracter)
        busca_line_values_nota = searchInformationText("(?<=Líquido da Nota)((.*(\n|\r|\r\n)){5})", removeCaracter)
        busca_local_incidencia = searchInformationText("(?<=Número da Nota)((.*(\n|\r|\r\n)){2})", removeCaracter)
        busca_decricao_atividade = searchInformationText("(?<=Tributo)((.*(\n|\r|\r\n)){5})", removeCaracter)
        busca_endereco_obra = searchInformationText("(?<=Endereço da Obra: )(.*)", removeCaracter)
        busca_cno = searchInformationText("(?<=CNO: )(.*)", removeCaracter)

        array_nota = re.split('\s', busca_line_values_nota)
        array_irrf = re.split('\s', busca_line_values_irrf)
        array_liquido = re.split('\s', busca_line_values_liquido)
        array_prestador = re.split('\n', busca_prestador)
        arra_tomador = re.split('\n', busca_tomador)
        
        print('Razao social prestador:', array_prestador[1])
        print('cpf/cnpj prestador:', array_prestador[8])
        print('insc mun prestador:', array_prestador[14])
        print('Endereco prestador:', array_prestador[4])
        print('Razao social tomador:', arra_tomador[1])
        print('cpf/cnpj tomador:', arra_tomador[3])
        print('insc mun tomador:', arra_tomador[12])
        print('Endereco tomador:', arra_tomador[5])        
        print('pis:', clear_array_empty(array_irrf)[1])
        print('cofins:', clear_array_empty(array_irrf)[2])
        print('csll', clear_array_empty(array_irrf)[3])
        ##insert nota fiscal
        print('Local de incidencia do imposto:', clear_blank_lines(busca_local_incidencia))
        print('Descricao atividade:', clear_blank_lines(busca_decricao_atividade))
        print(empy_text_column)
        print('serviços', clear_array_empty(array_liquido)[0])
        print('deduçoes:', clear_array_empty(array_liquido)[3])
        print('base de calculo', clear_array_empty(array_irrf)[0])
        print('inss: ', clear_array_empty(array_nota)[0])
        print('inss_retido: ', clear_array_empty(array_nota)[2])
        print("endereco da obra:", busca_endereco_obra)
        print("cno:", busca_cno)
        print(empy_text_column)
        print(empy_text_column)
        print(empy_text_column)
        print('liquido da nota: ', clear_array_empty(array_nota)[3])
        print('valor do iss:', clear_array_empty(array_liquido)[1])
        print('irrf', clear_array_empty(array_irrf)[4])
        #clear_folder_upload(filepathimage)
        # local_incidencia_imposto, 
        # descricao_atividades, 
        # porcentagem, 
        # servicos, 
        # deducoes, 
        # base_de_calculo, 
        # inss, 
        # iss_retido, 
        # endereco_obra, 
        # cno, 
        # codigo_servico, 
        # valor_total_deducoes, 
        # aliquota, 
        # valor_total_nota, 
        # valor_iss,
        # ir
        # local_incidencia_imposto[x], 
        # descricao_atividades [x], 
        # porcentagem [nao], 
        # servicos [x],
        # deducoes [x], 
        # base_de_calculo [x], 
        # inss [x], 
        # iss_retido [x], 
        # endereco_obra [x],
        # cno [x], 
        # codigo_servico [nao], 
        # valor_total_deducoes [nao], 
        # aliquota [nao], 
        # valor_total_nota [sim], 
        # valor_iss [x], 
        # ir [x]
        
        # data = [
        #     clear_blank_lines(arra_tomador[3]),
        #     clear_blank_lines(arra_tomador[1]),
        #     clear_blank_lines(arra_tomador[12]),
        #     clear_blank_lines(arra_tomador[5]),
        #     clear_blank_lines(array_prestador[8]),
        #     clear_blank_lines(array_prestador[1]),
        #     clear_blank_lines(array_prestador[14]),
        #     clear_blank_lines(array_prestador[4]),
        #     clear_blank_lines(busca_local_incidencia),
        #     clear_blank_lines(busca_decricao_atividade),
        #     clear_blank_lines(empy_text_column),
        #     clear_array_empty(array_liquido)[0],
        #     clear_array_empty(array_liquido)[3],
        #     clear_array_empty(array_irrf)[0],
        #     clear_array_empty(array_nota)[0],
        #     clear_array_empty(array_nota)[2],
        #     clear_blank_lines(busca_endereco_obra),
        #     clear_blank_lines(busca_cno),
        #     clear_blank_lines(empy_text_column),
        #     clear_blank_lines(empy_text_column),
        #     clear_blank_lines(empy_text_column),
        #     clear_array_empty(array_nota)[3],
        #     clear_array_empty(array_liquido)[1],
        #     clear_array_empty(array_irrf)[4]
        # ]

        data = {
            "cnpj_tomador": clear_blank_lines(arra_tomador[3]),
            "razao_tomador": clear_blank_lines(arra_tomador[1]),
            "insc_mun_tomador": clear_blank_lines(arra_tomador[12]),
            "endereco_tomador": clear_blank_lines(arra_tomador[5]),
            "cnpj_prestador": clear_blank_lines(array_prestador[8]),
            "razao_prestador": clear_blank_lines(array_prestador[1]),
            "insc_mun_prestador": clear_blank_lines(array_prestador[14]),
            "endereco_prestador": clear_blank_lines(array_prestador[4]),
            "local_incidencia_imposto": clear_blank_lines(busca_local_incidencia),
            "descricao_atividades": clear_blank_lines(busca_decricao_atividade),
            "porcentagem": clear_blank_lines(empy_text_column),
            "servicos": clear_array_empty(array_liquido)[0],
            "deducoes": clear_array_empty(array_liquido)[3],
            "base_de_calculo": clear_array_empty(array_irrf)[0],
            "inss": clear_array_empty(array_nota)[0],
            "iss_retido": clear_array_empty(array_nota)[2],
            "endereco_obra": clear_blank_lines(busca_endereco_obra),
            "cno": clear_blank_lines(busca_cno),
            "codigo_servico": clear_blank_lines(empy_text_column),
            "valor_total_deducoes": clear_blank_lines(empy_text_column),
            "aliquota": clear_blank_lines(empy_text_column),
            "valor_total_nota": clear_array_empty(array_nota)[3],
            "valor_iss": clear_array_empty(array_liquido)[1],
            "ir": clear_array_empty(array_irrf)[4]
        }

        # Convertendo o dicionário em formato JSON
        json_data = json.dumps(data)

        print("dados", data)

        return json_data
        
    except:
        
        return 400
        
        