from src.Interface.Api.utils.clear import clear_folder_image
from pdf2image import convert_from_path
from src.Interface.Api.utils.convert import image_to_text
from src.Interface.Api.utils.clear import clear_blank_lines
from src.Interface.Api.utils.clear import clear_array_empty
from src.Interface.Api.utils.convert import pdf_to_text
from src.Interface.Api.utils.clear import clear_folder_upload
from src.Interface.Api.utils.string import empy_text_column
from numpy import loadtxt
import re
import json

def work_template_nfs_suzanu(file, filename, filepathimage):
    print("############# work_template_nfs_suzanu suzano ##############")

    filenameimage = filename.replace('.pdf', '')

    text = image_to_text(file, filenameimage)
    
    text2 = pdf_to_text(file)

    removeCaracter = text.replace('(%)', '').replace('%', '').replace('(R$)', '').replace('R$', '').replace('-', '').replace('RS', '').replace('^[\t ]*\n', '').replace('\n\n', '\n').replace(r"\n{2,}","\n").replace("|","")
      
    try:

      lines = removeCaracter.split("\n")
      non_empty_lines = [line for line in lines if line.strip() != ""]

      string_without_empty_lines = ""
      for line in non_empty_lines:
            string_without_empty_lines += line + "\n"
      
      line_cnpj_prestador = re.compile("(CNPJ/CPF)((.|\n)*)(?=CNPJ/CPF)")
      cnpj_prestador = re.compile("(?<=CNPJ/CPF)((.|\n)*)(?=Inscrição Municipal)")
      line_endereco_tomador = re.compile("(?<=Endereço e Cep )((.|\n)*)(?=CEP)")
      line_aliquota = re.compile("(?<=Alíquota )(.*)")
      line_base_calculo = re.compile("(?<=Base de Cálculo )(.*)")
      line_valor_iss = re.compile("(?<=Valordo ISS:)(.*)")
      line_valor_liquido = re.compile("(?<=Valor Líquido  )((.|\n)*)(?=SE)")
      line_endereco = re.compile("(?<=ENDEREÇO: )(.*)")
      line_cno = re.compile("(?<=CNO:)(.*)")
      line_endereco_prestador = re.compile("(?<=Local da Prestação)((.*(\n|\r|\r\n)){2})")
      line_razao_tomador = re.compile("(?<=Razão Social/Nome)(.*)")
      table_razao_tomador = re.compile("(?<=Razão Social/Nome)(.*)")
      line_incricao_tomador = re.compile("(?<=Inscrição Municipal )(.*)(?=Município)")
      line_cnpj_tomador = re.compile("(?<=CNPJ/CPF)(.*)(?=Inscrição Municipal Município)")
      line_iss_retido = re.compile("(?<=ISS Retido )(.*)(?= SS a reter)")
      line_valor_servico = re.compile("(?<=Valor dos Serviços )(.*)(?= Natureza)")

      line_local_pretacao = re.compile("(?<=Local da Prestação)(.*)")
      line_local_obra = re.compile("(?<=ENDEREÇO:)(.*)")
      line_cno = re.compile("(?<=CNO:)(.*)")
      
      line_valor_servico = re.compile("(?<=Local da Prestação)((.*(\n|\r|\r\n)){2})")

      table_cnpj_prestador = line_cnpj_prestador.search(string_without_empty_lines)
      busca_razao_prestador = line_endereco_prestador.search(string_without_empty_lines)
      busca_cnpj = cnpj_prestador.search(table_cnpj_prestador.group())
      busca_cnpj_tomador = line_cnpj_tomador.search(string_without_empty_lines) 
      busca_municipal_tomador = line_incricao_tomador.search(string_without_empty_lines)
      busca_endereco = line_endereco_tomador.search(table_cnpj_prestador.group())
      busca_razao_tomador = line_razao_tomador.search(string_without_empty_lines)
      busca_razao = table_razao_tomador.findall(string_without_empty_lines)
      busca_aliquota = line_aliquota.search(removeCaracter)
      busca_base_calculo = line_base_calculo.search(removeCaracter)
      
      busca_valor_iss = line_valor_iss.search(string_without_empty_lines)

      busca_valor_liquido = line_valor_liquido.search(removeCaracter)
      busca_endereco_tomador = line_endereco.search(removeCaracter)
      
      busca_obra = line_local_obra.search(text2)
      busca_cno = line_cno.search(text2)
    
      busca_iss_retido = line_iss_retido.search(string_without_empty_lines)
      busca_valor_servico = line_valor_servico.search(string_without_empty_lines)
      
      busca_local_prestacao = line_local_pretacao.search(string_without_empty_lines)

      print("cnpj prestador:", busca_cnpj.group())
      print("razao/social prestador:", clear_blank_lines(busca_razao_tomador.group()))
      print("endereco prestador:", busca_endereco.group())
      print("cnpj tomador:", clear_blank_lines(busca_cnpj_tomador.group()))
      print("inscrição municipal tomador:", busca_municipal_tomador.group())
      print("razao/social tomador:", busca_razao[1])
      print("endereco tomador:", busca_endereco_tomador.group())


      
      print("valor liquido:", busca_valor_liquido.group())
      
      #print("descricao_atividades:")
      #print("servicos:")
      


      print("local_incidencia_imposto:", busca_local_prestacao.group())
      print(empy_text_column)
      print(empy_text_column)
      print("valor do serviço:", busca_valor_servico.group())
      print(empy_text_column)
      print("base de calculo:", busca_base_calculo.group())
      print(empy_text_column)
      print("iss retido", busca_iss_retido.group())
      print("endereco_obra:", busca_obra.group())
      print("cno:", busca_cno.group())
      print(empy_text_column)
      print(empy_text_column)
      print("aliquota:", busca_aliquota.group())
      print(empy_text_column)
      print("valor do ISS:", busca_valor_iss.group())
      print(empy_text_column)


      

      # local_incidencia_imposto [x], 
      # descricao_atividades [nao], 
      # porcentagem [nao], 
      # servicos [x], 
      # deducoes [nao], 
      # base_de_calculo [x], 
      # inss [nao], 
      # iss_retido [x], 
      # endereco_obra [x],
      # cno [x], 
      # codigo_servico [nao], 
      # valor_total_deducoes [nao], 
      # aliquota [x], 
      # valor_total_nota [nao], 
      # valor_iss [x], 
      # ir [nao]
      
      
      clear_folder_upload(filepathimage)

      # return [
      #   clear_blank_lines(busca_cnpj_tomador.group()),
      #   clear_blank_lines(busca_razao[1]),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(busca_endereco_tomador.group()),
      #   clear_blank_lines(busca_cnpj.group()),
      #   clear_blank_lines(clear_blank_lines(busca_razao_tomador.group())),
      #   clear_blank_lines(busca_municipal_tomador.group()),
      #   clear_blank_lines(busca_endereco.group()),
      #   clear_blank_lines(busca_local_prestacao.group()),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(busca_valor_servico.group()),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(busca_base_calculo.group()),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(busca_iss_retido.group()),
      #   clear_blank_lines(busca_obra.group()),
      #   clear_blank_lines(busca_cno.group()),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(busca_aliquota.group()),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(busca_valor_iss.group()),
      #   clear_blank_lines(empy_text_column),
      #   ]
      

      data = {
          "cnpj_tomador": clear_blank_lines(busca_cnpj_tomador.group()),
          "razao_tomador": clear_blank_lines(busca_razao[1]),
          "insc_mun_tomador": clear_blank_lines(empy_text_column),
          "endereco_tomador": clear_blank_lines(busca_endereco_tomador.group()),
          "cnpj_prestador": clear_blank_lines(busca_cnpj.group()),
          "razao_prestador": clear_blank_lines(clear_blank_lines(busca_razao_tomador.group())),
          "insc_mun_prestador": clear_blank_lines(busca_municipal_tomador.group()),
          "endereco_prestador": clear_blank_lines(busca_endereco.group()),
          "local_incidencia_imposto": clear_blank_lines(busca_local_prestacao.group()),
          "descricao_atividades": clear_blank_lines(empy_text_column),
          "porcentagem": clear_blank_lines(empy_text_column),
          "servicos": clear_blank_lines(busca_valor_servico.group()),
          "deducoes": clear_blank_lines(empy_text_column),
          "base_de_calculo": clear_blank_lines(busca_base_calculo.group()),
          "inss": clear_blank_lines(empy_text_column),
          "iss_retido": clear_blank_lines(busca_iss_retido.group()),
          "endereco_obra": clear_blank_lines(busca_obra.group()),
          "cno": clear_blank_lines(busca_cno.group()),
          "codigo_servico": clear_blank_lines(empy_text_column),
          "valor_total_deducoes": clear_blank_lines(empy_text_column),
          "aliquota": clear_blank_lines(busca_aliquota.group()),
          "valor_total_nota": clear_blank_lines(empy_text_column),
          "valor_iss": clear_blank_lines(busca_valor_iss.group()),
          "ir": clear_blank_lines(empy_text_column)
      }


      json_data = json.dumps(data)

      return json_data


    except:
                    
      return 400






