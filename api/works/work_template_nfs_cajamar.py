import re 
from utils.convert import pdf_to_text
from utils.clear import clear_blank_lines
from utils.string import empy_text_column

def work_template_nfs_cajamar(file, filename, filepathimage):
    print("############# work_template_nfs_cajamar cajamar ##############")
    try:
        removeCaracter = pdf_to_text(file)
        
        valor_total = re.compile("(?<=VALOR TOTAL DA NOTA =)(.*)")
        line_pretador_servico = re.compile("PRESTADOR DE SERVIÇOS((.*(\n|\r|\r\n)){7})")
        line_tomador_servico = re.compile("TOMADOR DE SERVIÇOS((.*(\n|\r|\r\n)){7})")
        line_table_value1 = re.compile("PIS((.*(\n|\r|\r\n)){2})")
        line_table_value2 = re.compile("VALOR TOTAL DAS DEDUÇÕES((.*(\n|\r|\r\n)){2})")
        line_descricao = re.compile("DESCRIÇÃO DOS SERVIÇOS((.*(\n|\r|\r\n)){3})")
        local_obra = re.compile("(?<=Local da Obra: )(.*)")
        cpf_cnpj_ptd = re.compile("(?<=CPF/CNPJ: )(.*)")
        inscricao_muni_ptd = re.compile("(?<=Inscrição Municipal: )(.*)")
        nome_razao_ptd = re.compile("(?<=Nome/Razão Social: )(.*)")
        endereco_ptd = re.compile("(?<=Endereço: )(.*)")
        municipio_ptd = re.compile("(?<=Município: )(.*)")
        cpf_cnpj_tdr = re.compile("(?<=CPF/CNPJ: )(.*)")
        inscricao_muni_tdr = re.compile("(?<=Inscrição Municipal: )(.*)")
        nome_razao_tdr = re.compile("(?<=Nome/Razão Social: )(.*)")
        endereco_tdr = re.compile("(?<=Endereço: )(.*)")
        municipio_tdr = re.compile("(?<=Município: )(.*)")

        line_descricao_servico = re.compile("(?<=DESCRIÇÃO DOS SERVIÇOS)((.|\n)*)(?=Local da Obra)")
        line_codigo_servico = re.compile("(?<=CÓDIGO DE SERVIÇO)((.|\n)*)(?=VALOR TOTAL DAS DEDUÇÕES)")
        
        line_valor_total_deducoes = re.compile("(?<=VALOR TOTAL DAS DEDUÇÕES  BASE DE CÁLCULO  ALÍQUOTA  VALOR DO ISS)((.*(\n|\r|\r\n)){2})")
        
        

        busca_codigo_servico = line_codigo_servico.search(removeCaracter)
        

        busca_total_deducoes = line_valor_total_deducoes.search(removeCaracter)

        line_valor_total = valor_total.search(removeCaracter)
        busca_pretador_servico = line_pretador_servico.search(removeCaracter)
        busca_tomador_servico = line_tomador_servico.search(removeCaracter)
        busca_table_value1 = line_table_value1.search(removeCaracter)
        busca_table_value2 = line_table_value2.search(removeCaracter)
        busca_local_obra = local_obra.search(removeCaracter)
        busca_descricao = line_descricao_servico.search(removeCaracter)
        busca_cpf_cnpj_ptd = cpf_cnpj_ptd.search(busca_pretador_servico.group())
        busca_inscricao_ptd = inscricao_muni_ptd.search(busca_pretador_servico.group())
        busca_endereco_ptd = endereco_ptd.search(busca_pretador_servico.group())
        busca_municipio_ptd = municipio_ptd.search(busca_pretador_servico.group())
        busca_razao_ptd = nome_razao_ptd.search(busca_pretador_servico.group())
        busca_cpf_cnpj_tdr = cpf_cnpj_tdr.search(busca_tomador_servico.group())
        busca_inscricao_tdr = inscricao_muni_tdr.search(busca_tomador_servico.group())
        busca_endereco_tdr = endereco_tdr.search(busca_tomador_servico.group())
        busca_municipio_tdr = municipio_tdr.search(busca_tomador_servico.group())
        busca_razao_tdr = nome_razao_tdr.search(busca_tomador_servico.group())
        
        text_to_array = re.split('\s', busca_table_value1.group())
        text_to_array2 = re.split('\s', busca_table_value2.group())

        array_clear_empty = [x for x in text_to_array if x != '']
        array_clear_empty_2 = [x for x in text_to_array2 if x != '']
    
        total = busca_total_deducoes.group()
        
        print("cnpj prestador: ", busca_cpf_cnpj_ptd.group())
        print("inscricao prestador: ", busca_inscricao_ptd.group())
        print("endereco prestador: ", busca_endereco_ptd.group())
        print("municipio prestador: ", busca_municipio_ptd.group())
        print("razao prestador: ", busca_razao_ptd.group())
        print("cnpj tomador: ", busca_cpf_cnpj_tdr.group())
        print("inscricao tomador: ", busca_inscricao_tdr.group())
        print("endereco tomador: ", busca_endereco_tdr.group())
        print("municipio tomador: ", busca_municipio_tdr.group())
        print("razao tomador: ", busca_razao_tdr.group())

        print('pis: ', array_clear_empty[5])
        print('cofins: ', array_clear_empty[6])
        print('csll: ', array_clear_empty[7])
        
        ##insert nota fiscal
        print(empy_text_column)
        print('descricao: ', clear_blank_lines(busca_descricao.group()))
        print(empy_text_column)
        print(empy_text_column)
        print(empy_text_column)
        print('base de calculo: ', array_clear_empty_2[12])
        print('inss: ', array_clear_empty[9])
        print(empy_text_column)
        print('local obra: ', busca_local_obra.group())
        print(empy_text_column)
        print('codigo do servico: ', clear_blank_lines(busca_codigo_servico.group()))
        print('busca valor total das deduções: ', total.split(' ')[1].replace('\n', ''))
        print('aliquota: ', array_clear_empty_2[13])
        print('valor total', line_valor_total.group())
        print('valor do iss: ', array_clear_empty_2[14])
        print('irrf: ', array_clear_empty[8])




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

        # base_de_calculo [x], 
        # inss [x],
        # endereco_obra [x],
        # valor_iss [x], 
        # ir [x] 
        # aliquota [x],
        # local_incidencia_imposto [nao], 
        # descricao_atividades [x], 
        # porcentagem [nao], 
        # servicos [nao], 
        # deducoes [nao], 
        # iss_retido [nao], 
        # cno [nao], 
        # codigo_servico [x], 
        # valor_total_deducoes [sim],  
        # valor_total_nota [sim], 

        data = [ 
            busca_cpf_cnpj_tdr.group(), 
            busca_razao_tdr.group(), 
            busca_inscricao_tdr.group(), 
            busca_endereco_tdr.group(), 
            busca_cpf_cnpj_ptd.group(), 
            busca_razao_ptd.group(), 
            busca_inscricao_ptd.group(),
            busca_endereco_ptd.group(),
            empy_text_column,
            clear_blank_lines(busca_descricao.group()),
            empy_text_column,
            empy_text_column,
            empy_text_column,
            array_clear_empty_2[12],
            array_clear_empty[9],
            empy_text_column,
            busca_local_obra.group(),
            empy_text_column,
            clear_blank_lines(busca_codigo_servico.group()),
            total.split(' ')[1].replace('\n', ''),
            array_clear_empty_2[13],
            line_valor_total.group(),
            array_clear_empty_2[14],
            array_clear_empty[8],
        ]
        

        return data
    except:
        
        return 400
        