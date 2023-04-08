from pdf2image import convert_from_path
from PyPDF2 import PdfReader
from PIL import Image
from utils.convert import image_to_text
from utils.convert import pdf_to_text
from utils.clear import clear_blank_lines
from utils.clear import clear_folder_upload
from utils.clear import clear_array_empty
from utils.string import empy_text_column

import re

def work_template_nfs_trindade(file, filename, filepathimage):
    print("############# work_template_nfs_trindade trindade do sul ##############")
    try:
        filenameimage = filename.replace('.pdf', '')
        resultado = image_to_text(file, filenameimage)

        removeText = resultado.replace('(%)', '').replace('%', '').replace('(R$)', '').replace('R$', '').replace('RS', '').replace('^[\t ]*\n', '')

        text = pdf_to_text(file)

        lineAliqouta = re.compile("(?<=Aliquota  Valor do ISS  Valor do ISS Retido  Descontos Condicionais)((.*(\n|\r|\r\n)){2})")
        lineValor = re.compile("(?<=Valor dos Serviços  Valor Dedução  Descontos Incondicionais  Base de Calculo)((.*(\n|\r|\r\n)){2})")
        lineImposto = re.compile("(?<=Imposto de Renda  PIS  COFINS  CSLL  INSS  Outras Retenções )((.*(\n|\r|\r\n)){2})")
        lineValorTotal = re.compile("VALOR TOTAL DOS SERVIÇOS((.*(\n|\r|\r\n)){2})")
        endereco_obra = re.compile("(?<=ENDEREÇO DA OBRA:)(.*)")
        line_pretacao_tomador_servico = re.compile("Cpf / Cnpj((.|\n)*)Tomador de Serviços")
        line_cnpj_incricao = re.compile("Cpf / Cnpj Inscrição Municipal Inscrição Estadual((.*(\n|\r|\r\n)){2})")
        line_razao_tomador = re.compile("(?<=Razão Social )(.*)")
        line_endereco_tomador = re.compile("(?<=Endereço: )(.*)")        
        line_municipio_tomador = re.compile("(?<=Município: )(.*)")
        line_cnpj_incricao_prestador = re.compile("(?<=CPF / CNPJ Inscrição Municipal Telefone)((.*(\n|\r|\r\n)){2})")
        line_razao_prestador = re.compile("(?<=Nome/Razão Social)((.*(\n|\r|\r\n)){2})")
        line_endereco_prestador = re.compile("(?<=Prestador de Serviços : )(.*)")
        line_municipio_prestador = re.compile("(?<=Município Prestador UF CEP)((.*(\n|\r|\r\n)){2})")
        line_cnpj_pretacao = re.compile("(?<=Cnpj Inscrição Municipal Inscrição Estadual)((.*(\n|\r|\r\n)){2})")

        busca_cnpj_pretacao = line_cnpj_pretacao.search(text)
    
        line_endereco = re.compile("(?<=ENDEREÇO DA OBRA: )(.*)")
        cno = re.compile("(?<=CNO: )(.*)")

        array_cnpj_pretacao = clear_array_empty(clear_blank_lines(busca_cnpj_pretacao.group()).split(" "))

        busca_endereco_obra = line_endereco.search(text)
        busca_cno = cno.search(text)
        
        busca_line_aliquota = lineAliqouta.search(text)
        busca_line_valor = lineValor.search(text)
        busca_line_imposto = lineImposto.search(text)
        busca_valor_total = lineValorTotal.search(text)
        busca_pretacao_servico = line_pretacao_tomador_servico.search(text)

        busca_cnpj_incricao = line_cnpj_incricao.search(busca_pretacao_servico.group())
        busca_razao_tomador = line_razao_tomador.search(busca_pretacao_servico.group())
        busca_endereco_tomador = line_endereco_tomador.search(busca_pretacao_servico.group())
        busca_municipio_tomador = line_municipio_tomador.search(busca_pretacao_servico.group())
        
        busca_cnpj_incricao_prestador = line_cnpj_incricao_prestador.search(busca_pretacao_servico.group())
        busca_razao_prestador = line_razao_prestador.search(busca_pretacao_servico.group())
        busca_endereco_prestador = line_endereco_prestador.search(busca_pretacao_servico.group())
        busca_municipio_prestador = line_municipio_prestador.search(busca_pretacao_servico.group())
        array_cnpj_incricao = clear_blank_lines(busca_cnpj_incricao_prestador.group()).split(" ")
        
        array_line_aliquota = clear_array_empty(clear_blank_lines(busca_line_aliquota.group()).split(" "))
        array_line_valor = clear_array_empty(clear_blank_lines(busca_line_valor.group()).split(" "))
        array_line_imposto = clear_array_empty(clear_blank_lines(busca_line_imposto.group()).split(" "))


        print("Razao social tomador:", clear_blank_lines(busca_razao_tomador.group()))
        print('Endereco tomador:', clear_blank_lines(busca_endereco_tomador.group()))
        print("municipio tomador: ",clear_blank_lines(busca_municipio_tomador.group()))        
        print("CNPJ PRESTADOR TOMADOR: ", array_cnpj_incricao[0])
        print("INSCRIÇÃO MUNICIPAL TOMADOR : ", array_cnpj_incricao[1])
        print("CNPJ PRESTADOR", array_cnpj_pretacao[0])
        print("INSCRIÇÃO MUNICIPAL prestador", array_cnpj_pretacao[1])
        print("Razao social prestador:", clear_blank_lines(busca_razao_prestador.group()))
        print('Endereco prestador:', clear_blank_lines(busca_endereco_prestador.group()))
        print("municipio prestador: ",clear_blank_lines(busca_municipio_prestador.group()))


        
        print("Descontos Condicionais: ", array_line_aliquota[3])
        print("Descontos Incondicionais: ", array_line_valor[2])  
        print("PIS: ", array_line_imposto[1])  
        print("COFINS: ", array_line_imposto[2])  
        print("CSLL: ", array_line_imposto[3])
        print("Outras Retenções: ", array_line_imposto[5])


        print(empy_text_column)
        print(empy_text_column)
        print(empy_text_column)
        print("Valor dos Serviços: ", array_line_valor[0])
        print("Valor Dedução: ", array_line_valor[1])  
        print("Base de Calculo: ", array_line_valor[3])
        print("INSS: ", array_line_imposto[4])
        print("Valor do ISS Retido: ", array_line_aliquota[2])
        print("endereco obra:", busca_endereco_obra.group())
        print("cno:", busca_cno.group())
        print(empy_text_column)
        print(empy_text_column)
        print("Aliquota: ", array_line_aliquota[0])
        print(empy_text_column)
        print("Valor do ISS: ", array_line_aliquota[1])
        print("Imposto de Renda: ", array_line_imposto[0])



        # local_incidencia_imposto [sim], 
        # descricao_atividades [sim], 
        # porcentagem [nao], 
        # servicos [sim], 
        # deducoes [x], 
        # base_de_calculo [x], 
        # inss [x], 
        # iss_retido[x], 
        # endereco_obra [sim],
        # cno [sim], 
        # codigo_servico [sim], 
        # valor_total_deducoes [nao], 
        # aliquota [x], 
        # valor_total_nota [nao], 
        # valor_iss [x], 
        # ir [x]

        clear_folder_upload(filepathimage)
        
        return [
            clear_blank_lines(array_cnpj_pretacao[0]), 
            clear_blank_lines(busca_razao_tomador.group()), 
            clear_blank_lines(array_cnpj_pretacao[1]), 
            clear_blank_lines(busca_endereco_tomador.group()), 
            clear_blank_lines(array_cnpj_incricao[0]), 
            clear_blank_lines(busca_razao_prestador.group()),
            clear_blank_lines(array_cnpj_incricao[1]), 
            clear_blank_lines(busca_endereco_prestador.group()),
            clear_blank_lines(empy_text_column),
            clear_blank_lines(empy_text_column),
            clear_blank_lines(empy_text_column),
            clear_blank_lines(array_line_valor[0]),
            clear_blank_lines(array_line_valor[1]),  
            clear_blank_lines(array_line_valor[3]),
            clear_blank_lines(array_line_imposto[4]),
            clear_blank_lines(array_line_aliquota[2]),
            clear_blank_lines(busca_endereco_obra.group()),
            clear_blank_lines(busca_cno.group()),
            clear_blank_lines(empy_text_column),
            clear_blank_lines(empy_text_column),
            clear_blank_lines(array_line_aliquota[0]),
            clear_blank_lines(empy_text_column),
            clear_blank_lines(array_line_aliquota[1]),
            clear_blank_lines(array_line_imposto[0])
        ]
    
    except:
        return 400
        


