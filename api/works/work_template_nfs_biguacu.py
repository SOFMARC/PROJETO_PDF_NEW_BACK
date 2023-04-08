from utils.convert import image_to_text
from utils.clear import clear_blank_lines
from utils.clear import clear_array_empty
from utils.clear import clear_folder_upload
from utils.string import empy_text_column
from utils.getvalue import get_value

import re

def work_template_nfs_biguacu(file, filename, filepathimage):
    print("############# work_template_nfs_biguacu biguaçu ##############")
    filenameimage = filename.replace('.pdf', '')
    text = image_to_text(file, filenameimage) 

    removeCaracter = text.replace('(%)', '').replace('%', '').replace('(R$)', '').replace('R$', '').replace('-', '').replace('RS', '').replace('^[\t ]*\n', '').replace('\n\n', '\n').replace(r"\n{2,}","\n").replace("|","")
      
    try:
      line_pretacao_servico = re.compile("PRESTADOR DE SERVIÇOS((.*(\n|\r|\r\n)){8})")
      line_tomador_servico = re.compile("TOMADOR DE SERVIÇOS((.*(\n|\r|\r\n)){15})")
        
      busca_tomador = line_tomador_servico.search(removeCaracter)
      busca_prestador = line_pretacao_servico.search(removeCaracter)

      line_nome = re.compile("(?<=Nome/Razão social:)(.*)")
      line_cpf_cnpj = re.compile("(?<=CNPJ:)((.|\n)*)(?=Inscrição municipal)")
      line_endereco = re.compile("(?<=Endereço: )(.*)")
      line_municipio = re.compile("(?<=Município: )(.*)")
      line_nome_prestador = re.compile("(?<=Nome/Razão social:)(.*)")
      line_cpf_cnpj_prestador = re.compile("(?<=CNPJ:)((.|\n)*)(?=Inscrição municipal)")
      line_endereco_prestador = re.compile("(?<=Endereço:)(.*)")
      line_municipio_prestador = re.compile("(?<=Município:)(.*)")
      line_inscricao_prestador = re.compile("(?<=Inscrição municipal:)((.|\n)*)(?=Telefone)")
      line_endereco_obra = re.compile("(?<=Endereço da obra:)((.|\n)*)(?=Cep)")
      line_pis = re.compile("(?<=PIS/PASEP COFINS INSS IR CSLL Outras retenções)((.*(\n|\r|\r\n)){2})")
      line_desc = re.compile("(?<=Desc. condicionado Desc. incondicionado Deduções Base de cálculo Valor ISS)((.*(\n|\r|\r\n)){2})")

      line_descricao_atividade = re.compile("(?<=Valor unitário Qtd Valor do serviço Base de cálculo  ISS)((.*(\n|\r|\r\n)){2})")
      busca_descricao_atividade = line_descricao_atividade.search(busca_tomador.group())
      
      line_cno = re.compile("(?<=Cno)(.*)(?=Periodo)")
      line_codigo_servico = re.compile("(?<=Códigos dos serviços:)((.|\n)*)(?=Desc. condicionado)")
      line_total_bruto = re.compile("(?<=Valor bruto =)(.*)(?=Valor líquido)")


      busca_tomador_nome = line_nome.search(busca_tomador.group())
      busca_tomador_cpf_cnpj = line_cpf_cnpj.search(busca_tomador.group())
      busca_tomador_endereco = line_endereco.search(busca_tomador.group())
      busca_tomador_municipio = line_municipio.search(busca_tomador.group())
      busca_prestador_nome = line_nome_prestador.search(busca_prestador.group())
      busca_prestador_cpf_cnpj = line_cpf_cnpj_prestador.search(busca_prestador.group())
      busca_prestador_endereco = line_endereco_prestador.search(busca_prestador.group())
      busca_prestador_municipio = line_municipio_prestador.search(busca_prestador.group())
      busca_inscricao_prestador = line_inscricao_prestador.search(busca_prestador.group())

      busca_endereco_obra = line_endereco_obra.search(removeCaracter)
      busca_line_pis = line_pis.search(removeCaracter)
      busca_line_desc = line_desc.search(removeCaracter)
      busca_total_bruto = line_total_bruto.search(removeCaracter)
      

      busca_line_cno = line_cno.search(removeCaracter)
      busca_line_servico = line_codigo_servico.search(removeCaracter)
      
      array_line_pis = clear_array_empty(clear_blank_lines(busca_line_pis.group()).split(" "))
      array_line_desc = clear_array_empty(clear_blank_lines(busca_line_desc.group()).split(" "))

      numeros = re.findall(r'\d+[\.\,\d]*', busca_descricao_atividade.group()) # Encontra todos os números com ponto ou vírgula
      numeros_x = re.findall(r'x\d+[\.\,\d]*', busca_descricao_atividade.group()) # Encontra todos os números com x e ponto ou vírgula

      for n in numeros_x:
          numeros.append(n[1:]) # Remove o x do começo dos números com x
      
      texto_sem_numeros = re.sub(r'[\d\.\,x]+', '', busca_descricao_atividade.group()) # Substitui números com ponto ou vírgula e x por vazio
      texto_sem_numeros = texto_sem_numeros.strip() # Remove espaços no começo e fim da string

      print("nome tomador:", clear_blank_lines(busca_tomador_nome.group()))
      print("cnpj tomador:", clear_blank_lines(busca_tomador_cpf_cnpj.group()))
      print("endereço tomador:", clear_blank_lines(busca_tomador_endereco.group()))
      print("municipio tomador:", clear_blank_lines(busca_tomador_municipio.group()))
      print("nome prestador:", clear_blank_lines(busca_prestador_nome.group()))
      print("cnpj prestador:", clear_blank_lines(busca_prestador_cpf_cnpj.group()))
      print("endereço prestador:", clear_blank_lines(busca_prestador_endereco.group()))
      print("municipio prestador:", busca_prestador_municipio.group())
      print("incricao prestador:", busca_inscricao_prestador.group())


      
      print("PIS/PASEP:", array_line_pis[0])
      print("CONFINS:", array_line_pis[1])      
      print("CSLL:", array_line_pis[4])
      

      
      ##insert nota fiscal
      print(empy_text_column)
      print("atividade:", clear_blank_lines(texto_sem_numeros))
      print("porcentagem:", numeros[4])
      print(empy_text_column)
      print("deduções:", array_line_desc[2])
      print("Base de cálculo:", array_line_desc[3])
      print("INSS:", array_line_pis[2])
      print(empy_text_column)
      print("endereço obra:", busca_endereco_obra.group())
      print("cno:", busca_line_cno.group())
      print("codigo do serviço:", clear_blank_lines(busca_line_servico.group()))
      print(empy_text_column)
      print(empy_text_column)
      print("busca total bruto:", clear_blank_lines(busca_total_bruto.group()))
      print("Valor ISS:", array_line_desc[4])
      print("IR:", array_line_pis[3])


      clear_folder_upload(filepathimage)

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
      # local_incidencia_imposto [nao], 
      # descricao_atividades [x], 
      # porcentagem [x], 
      # servicos [nao], 
      # deducoes [x], 
      # iss_retido [nao],  
      # cno [x], 
      # codigo_servico [x], 
      # valor_total_deducoes [nao], 
      # aliquota [nao], 
      # valor_total_nota [x], 


      return [
        clear_blank_lines(busca_tomador_cpf_cnpj.group()),
        clear_blank_lines(busca_tomador_nome.group()),
        clear_blank_lines(busca_inscricao_prestador.group()),
        clear_blank_lines(busca_tomador_endereco.group()),
        clear_blank_lines(busca_prestador_cpf_cnpj.group()),
        clear_blank_lines(busca_prestador_nome.group()),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(busca_prestador_endereco.group()),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(texto_sem_numeros),
        clear_blank_lines(numeros[4]),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(array_line_desc[2]),
        clear_blank_lines(array_line_desc[3]),
        clear_blank_lines(array_line_pis[2]),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(busca_endereco_obra.group()),
        clear_blank_lines(busca_line_cno.group()),
        clear_blank_lines(busca_line_servico.group()),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(busca_total_bruto.group()),
        clear_blank_lines(array_line_desc[4]),
        clear_blank_lines(array_line_pis[3])
      ]
         
    except:
         
      return 400






