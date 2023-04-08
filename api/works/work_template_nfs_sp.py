from utils.convert import image_to_text
from utils.clear import clear_blank_lines
from utils.clear import clear_array_empty
from utils.clear import clear_jump_lines
from utils.clear import clear_folder_upload
from utils.string import empy_text_column
import re

def work_template_nfs_sp(file, filename, filepathimage):
    print("############# work_template_nfs_sp são paulo ##############")
    
    filenameimage = filename.replace('.pdf', '')

    text = image_to_text(file, filenameimage)

    removeCaracter = text.replace('(%)', '').replace('%', '').replace('(R$)', '').replace('R$', '').replace('RS', '').replace('^[\t ]*\n', '') 
      
    texto_sem_espacos = re.sub(r'\n\s*\n', '\n', removeCaracter)
    #print(texto_sem_espacos)

    try:
      
      line_pretacao_servico = re.compile("PRESTADOR DE SERVIÇOS((.*(\n|\r|\r\n)){6})")
      line_tomador_servico = re.compile("TOMADOR DE SERVIÇOS((.*(\n|\r|\r\n)){6})")
        
      busca_tomador = line_tomador_servico.search(removeCaracter)
      busca_prestador = line_pretacao_servico.search(removeCaracter)

      line_nome = re.compile("(?<=Nome/Razão Social: )(.*)")
      line_cpf_cnpj = re.compile("CPF/CNPJ: (.*)")
      line_endereco = re.compile("(?<=Endereço: )(.*)")
      line_municipio = re.compile("(?<=Município: )(.*)")
      line_incricao = re.compile("(?<=Inscrição Municipal: )(.*)")
      line_cpf_cnpj_v2 = re.compile("(?<=CPF/CNPJ: )((.|\n)*)(?=Inscrição Municipal)")
      line_valor_liquido = re.compile("(?<=VALOR TOTAL DO SERVIÇO = )(.*)")
      line_inss = re.compile("(?<=INSS  IRRF  CSLL  COFINS  PIS/PASEP)((.*(\n|\r|\r\n)){2})")
      line_aliquota = re.compile("(?<=Valor Total das Deduções  Base de Cálculo  Alíquota  Valor do ISS  Crédito )((.*(\n|\r|\r\n)){2})")
      line_endereco_obra = re.compile("(?<=Endereço da Obra: )(.*)")
      local = re.compile("(?<=LOCAL:)(.*)")
      local_obra = re.compile("(?<=Endereço da Obra:)(.*)")
      cno = re.compile("(?<=CNO:)(.*)")
      codigo_serivo = re.compile("(?<=Código do Serviço)((.|\n)*)(?=Valor Total das Deduções)")

      busca_tomador_nome = line_nome.search(busca_tomador.group())
      busca_tomador_cpf_cnpj = line_cpf_cnpj.search(busca_tomador.group())
      busca_tomador_endereco = line_endereco.search(busca_tomador.group())
      busca_tomador_municipio = line_municipio.search(busca_tomador.group())
      busca_tomador_inscricao = line_incricao.search(busca_tomador.group())


      busca_prestador_nome = line_nome.search(busca_prestador.group())
      busca_prestador_cpf_cnpj = line_cpf_cnpj.search(busca_prestador.group())
      busca_prestador_endereco = line_endereco.search(busca_prestador.group())
      busca_prestador_incricao = line_incricao.search(busca_prestador.group())
      
      busca_prestadwor_municipio = line_municipio.search(busca_prestador.group())
      
      busca_endereco_obra = line_endereco_obra.search(removeCaracter)
      busca_valor_liquido = line_valor_liquido.search(clear_jump_lines(removeCaracter))
      busca_line_inss = line_inss.search(clear_jump_lines(removeCaracter))
      busca_line_aliquota = line_aliquota.search(clear_jump_lines(removeCaracter))
      
      array_line_inss = clear_array_empty(clear_blank_lines(busca_line_inss.group()).split(" "))
      array_line_aliquota = clear_array_empty(clear_blank_lines(busca_line_aliquota.group()).split(" "))
      
      
      busca_tomador_cpf_cnpj_v2 = line_cpf_cnpj_v2.search(clear_blank_lines(busca_tomador_cpf_cnpj.group()))
      busca_prestador_cpf_cnpj_v2 = line_cpf_cnpj_v2.search(clear_blank_lines(busca_prestador_cpf_cnpj.group()))
      busca_local = local.search(texto_sem_espacos)

      busca_local_obra = local_obra.search(texto_sem_espacos)
      busca_cno = cno.search(texto_sem_espacos)
      busca_codigo_serico = codigo_serivo.search(texto_sem_espacos)

      print("cnpj v2", busca_tomador_cpf_cnpj_v2.group())
                                                             
      if len(array_line_aliquota) < 4:
        valor_total_deducoes = empy_text_column
        base_calculo = empy_text_column
        aliquota = empy_text_column
        valor_iss = empy_text_column
        credito = empy_text_column
      else:
        valor_total_deducoes = array_line_aliquota[0] == '-' and empy_text_column or array_line_aliquota[0]
        base_calculo = array_line_aliquota[1] == '-' and empy_text_column or array_line_aliquota[1]
        aliquota = array_line_aliquota[2] == '-' and empy_text_column or array_line_aliquota[2]
        valor_iss =  array_line_aliquota[3] == '-' and empy_text_column or array_line_aliquota[3]
        credito = array_line_aliquota[4] == '-' and empy_text_column or array_line_aliquota[4]
        
      if len(array_line_inss) < 4:
        irrf = empy_text_column
        csll  = empy_text_column
        cofins = empy_text_column
        pis_pasep = empy_text_column

      else:
        irrf = array_line_inss[0] == '-' and empy_text_column or array_line_inss[0]
        csll  = array_line_inss[1] == '-' and empy_text_column or array_line_inss[1]
        cofins = array_line_inss[2] == '-' and empy_text_column or array_line_inss[2]
        pis_pasep = array_line_inss[3] == '-' and empy_text_column or array_line_inss[3]
      
      print("nome tomador:", clear_blank_lines(busca_tomador_nome.group()))
      print("cnpj tomador:", clear_blank_lines(busca_tomador_cpf_cnpj_v2.group()))
      print("endereço tomador:", clear_blank_lines(busca_tomador_endereco.group()))
      print("municipi tomador:", clear_blank_lines(busca_tomador_municipio.group()))
      print("nome prestador:", clear_blank_lines(busca_prestador_nome.group()))
      print("cnpj prestador:", clear_blank_lines(busca_prestador_cpf_cnpj_v2.group()))
      print("endereço prestador:", clear_blank_lines(busca_prestador_endereco.group()))
      print("incricao tomador:", busca_tomador_inscricao.group())
      print("incricao prestador:", busca_prestador_incricao.group())

      print("Crédito",credito)
      print("CSLL:", csll)
      print("COFINS:", cofins)
      print("PIS/PASEP:", pis_pasep)
      print("valor liquido:", busca_valor_liquido.group())


      ##insert nota fiscal
      print("local imposto:", busca_local.group() if busca_local else empy_text_column )
      print(empy_text_column)
      print(empy_text_column)
      print(empy_text_column)
      print(empy_text_column)
      print("Base de Cálculo:", base_calculo)
      print(empy_text_column)
      print(empy_text_column)
      print("endereco obra:", busca_local_obra.group() if busca_local_obra else empy_text_column )
      print("cno:", busca_cno.group() if busca_cno else empy_text_column)
      print("codigo serivo:", clear_blank_lines(busca_codigo_serico.group()))
      print("Valor Total das Deduções:",valor_total_deducoes)
      print("Alíquota:",aliquota)
      print(empy_text_column)
      print("Valor do ISS:",valor_iss)
      print("IRRF:", irrf)


      # local_incidencia_imposto [sim], 
      # descricao_atividades [nao], 
      # porcentagem [nao], 
      # servicos [nao],
      # deducoes, [nao], 
      # base_de_calculo [x], 
      # inss [nao], 
      # iss_retido [nao], 
      # endereco_obra [sim],
      # cno [sim], 
      # codigo_servico [sim], 
      # valor_total_deducoes [sim], 
      # aliquota [x], 
      # valor_total_nota[nao], 
      # valor_iss [x], 
      # ir [x]
      
      
      clear_folder_upload(filepathimage)
      
      return [
        clear_blank_lines(clear_blank_lines(busca_tomador_cpf_cnpj_v2.group())),
        clear_blank_lines(busca_tomador_nome.group()),
        clear_blank_lines(busca_tomador_inscricao.group()),
        clear_blank_lines(busca_tomador_endereco.group()),
        clear_blank_lines(clear_blank_lines(busca_prestador_cpf_cnpj_v2.group())),
        clear_blank_lines(busca_prestador_nome.group()),
        clear_blank_lines(busca_prestador_incricao.group()),
        clear_blank_lines(busca_prestador_endereco.group()),
        clear_blank_lines(busca_local.group() if busca_local else empy_text_column),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(base_calculo),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(busca_local_obra.group() if busca_local_obra else empy_text_column),
        clear_blank_lines(busca_cno.group() if busca_cno else empy_text_column),
        clear_blank_lines(clear_blank_lines(busca_codigo_serico.group())),
        clear_blank_lines(valor_total_deducoes),
        clear_blank_lines(aliquota),
        clear_blank_lines(empy_text_column),
        clear_blank_lines(valor_iss),
        clear_blank_lines(irrf),
        ]
        
    except:
      return 400






