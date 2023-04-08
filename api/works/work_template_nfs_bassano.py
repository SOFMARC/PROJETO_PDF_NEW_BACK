from utils.convert import pdf_to_text
from utils.clear import clear_array_empty
from utils.clear import clear_blank_lines

import re
from utils.string import empy_text_column
from utils.clear import clear_folder_upload

def work_template_nfs_bassano(file, filename, filepathimage):
    print("############# work_template_nfs3_bassano Bassano ##############")
    try:
        removeCaracter = pdf_to_text(file)

        line_pretacao_servico = re.compile("Prestador do serviço((.*(\n|\r|\r\n)){15})")
        line_tomador_servico = re.compile("Tomador do serviço((.*(\n|\r|\r\n)){15})")
        line_values_liquido = re.compile("(?<=Liquido)((.*(\n|\r|\r\n)){8})")
        line_values_irrf = re.compile("(?<=IRRF)((.*(\n|\r|\r\n)){7})")
        line_values_nota = re.compile("(?<=Líquido da Nota)((.*(\n|\r|\r\n)){5})")
        endereco_obra = re.compile("(?<=Endereço da Obra: )(.*)")
        cno = re.compile("(?<=CNO: )(.*)")
        valor = re.compile("(?<=VALOR BRUTO DA NOTA = )(.*)")

        line_local_incidencia = re.compile("(?<=Número da Nota)((.*(\n|\r|\r\n)){2})")
        line_descricao_atividade = re.compile("(?<=Tributo)((.*(\n|\r|\r\n)){5})")
        line_porcetagem = re.compile("(?<=Tributo)((.|\n)*)(?=Detalhamento da Atividade)")

        
        busca_endereco_obra = endereco_obra.search(removeCaracter)
        busca_cno = cno.search(removeCaracter)
        valor_nota = valor.search(removeCaracter)

        busca_line_porcent = line_porcetagem.search(removeCaracter)

        busca_tomador = line_tomador_servico.search(removeCaracter)
        busca_prestador = line_pretacao_servico.search(removeCaracter)
        busca_line_values_liquido = line_values_liquido.search(removeCaracter)
        busca_line_values_irrf = line_values_irrf.search(removeCaracter)
        busca_line_values_nota = line_values_nota.search(removeCaracter)
        
        busca_local_incidencia = line_local_incidencia.search(removeCaracter)
        busca_decricao_atividade = line_descricao_atividade.search(removeCaracter)
        
        array_nota = re.split('\s', busca_line_values_nota.group())
        array_irrf = re.split('\s', busca_line_values_irrf.group())
        array_liquido = re.split('\s', busca_line_values_liquido.group())
        array_prestador = re.split('\n', busca_prestador.group())
        arra_tomador = re.split('\n', busca_tomador.group())
        
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
        print('Local de incidencia do imposto:', clear_blank_lines(busca_local_incidencia.group()))
        print('Descricao atividade:', clear_blank_lines(busca_decricao_atividade.group()))
        print(empy_text_column)
        print('serviços', clear_array_empty(array_liquido)[0])
        print('deduçoes:', clear_array_empty(array_liquido)[3])
        print('base de calculo', clear_array_empty(array_irrf)[0])
        print('inss: ', clear_array_empty(array_nota)[0])
        print('inss_retido: ', clear_array_empty(array_nota)[2])
        print("endereco da obra:", busca_endereco_obra.group())
        print("cno:", busca_cno.group())
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
        
        data = [
            clear_blank_lines(arra_tomador[3]),
            clear_blank_lines(arra_tomador[1]),
            clear_blank_lines(arra_tomador[12]),
            clear_blank_lines(arra_tomador[5]),
            clear_blank_lines(array_prestador[8]),
            clear_blank_lines(array_prestador[1]),
            clear_blank_lines(array_prestador[14]),
            clear_blank_lines(array_prestador[4]),
            clear_blank_lines(busca_local_incidencia.group()),
            clear_blank_lines(busca_decricao_atividade.group()),
            clear_blank_lines(empy_text_column),
            clear_array_empty(array_liquido)[0],
            clear_array_empty(array_liquido)[3],
            clear_array_empty(array_irrf)[0],
            clear_array_empty(array_nota)[0],
            clear_array_empty(array_nota)[2],
            clear_blank_lines(busca_endereco_obra.group()),
            clear_blank_lines(busca_cno.group()),
            clear_blank_lines(empy_text_column),
            clear_blank_lines(empy_text_column),
            clear_blank_lines(empy_text_column),
            clear_array_empty(array_nota)[3],
            clear_array_empty(array_liquido)[1],
            clear_array_empty(array_irrf)[4]
        ]

        print("dados", data)

        return data
        
    except:
        
        return 400
        
        