from src.Interface.Api.utils.convert import image_to_text
from src.Interface.Api.utils.clear import clear_blank_lines
from src.Interface.Api.utils.clear import clear_folder_upload
from src.Interface.Api.utils.string import empy_text_column
from src.Interface.Api.utils.sanetization import remove_number_to_text
import re
import json

def work_template_nfs_osasco(file, filename, filepathimage):
    print("############# work_template_nfs4_osasco osasco##############")
    filenameimage = filename.replace('.pdf', '')
    print('filename', filename)
    text = image_to_text(file, filenameimage)
  
    print('text', text)

    removeCaracter = text.replace('(%)', '').replace('%', '').replace('(R$)', '').replace('R$', '').replace('RS', '').replace('^[\t ]*\n', '') 

    try:
      line_pretacao_servico = re.compile("PRESTADOR DE SERVIÇOS((.*(\n|\r|\r\n)){10})")
      line_tomador_servico = re.compile("TOMADOR DO SERVIÇO((.*(\n|\r|\r\n)){10})")
      line_ir = re.compile("(?<=IR : )(.*)")
      line_cofins = re.compile("(?<=Cofins : )(.*)")
      line_csll = re.compile("(?<=CSLL : )(.*)")
      line_nome = re.compile("(?<=Razão Social/Nome: )(.*)")
      line_cnpj = re.compile("(?<=CNPJ/CPF: )(.*?\S\s)")
      line_inscricao_municipal = re.compile("(?<=Inscrição Municipal: )(.*?\S\s)")
      line_endereco = re.compile("(?<=Endereço: )(.*)")
      line_municipio = re.compile("(?<=Município: )(.*)")
      line_confins = re.compile("(?<=Cofins : )(.*?\S\s)")
      line_csll_1 = re.compile("(?<=CSLL: )(.*?\S\s)")
      line_pis = re.compile("(?<=Pis/Pasep : )(.*?\S\s)")
      line_ir_prop = re.compile("(?<=IR : )(.*?\S\s)")
      line_iss = re.compile("(?<=ISS (CAJAMAR 4): )(.*?\S\s)")
      line_valor_liquido = re.compile("(?<=Valor Líquido a Pagar: )(.*?\S\s)")
      line_atividade= re.compile("(?<=DESCRIÇÃO DOS SERVIÇOS E OUTRAS INFORMAÇÕES:)((.*(\n|\r|\r\n)){8})")
      line_valor_servico = re.compile("(?<=Valor Serviço)((.|\n)*)(?=Impostos Adicionais)")
      line_endereco_obra = re.compile("(?<=ENDEREÇO: )(.*)")
      line_cno = re.compile("(?<=CNO: )(.*)")
      line_codigo_servico = re.compile("(?<=ATIVIDADE: )((.|\n)*)(?=DESCRIÇÃO DOS SERVIÇOS)")

      busca_tomador = line_tomador_servico.search(removeCaracter)
      busca_prestador = line_pretacao_servico.search(removeCaracter)
      busca_ir = line_ir.search(removeCaracter)
      busca_cofins = line_cofins.search(removeCaracter)
      busca_csll = line_csll.search(removeCaracter)
      busca_tomador_nome = line_nome.search(busca_tomador.group())
      busca_tomador_cnpj = line_cnpj.search(busca_tomador.group())
      busca_tomador_endereco = line_endereco.search(busca_tomador.group())
      busca_tomador_municipio = line_municipio.search(busca_tomador.group())
      busca_tomador_inscricao = line_inscricao_municipal.search(busca_tomador_cnpj.group())
      busca_prestador_nome = line_nome.search(busca_prestador.group())
      busca_prestador_cnpj = line_cnpj.search(busca_prestador.group())
      busca_prestador_inscricao = line_inscricao_municipal.search(busca_prestador.group())
      busca_prestador_endereco = line_endereco.search(busca_prestador.group())
      busca_prestador_municipio = line_municipio.search(busca_prestador.group())
      busca_confins = line_confins.search(busca_ir.group())
      busca_csll = line_csll_1.search(busca_ir.group())
      busca_pis = line_pis.search(removeCaracter)
      busca_ir = line_ir_prop.search(removeCaracter)
      busca_iss = line_iss.search(removeCaracter)
      busca_valor_total = line_valor_liquido.search(removeCaracter)
      busca_atividade = line_atividade.search(removeCaracter)
      busca_valor_servico = line_valor_servico.search(removeCaracter)
      busca_endereco_obra = line_endereco_obra.search(removeCaracter)
      busca_cno = line_cno.search(removeCaracter)
      busca_codigo_servico = line_codigo_servico.search(removeCaracter)

      print("nome tomador:", clear_blank_lines(busca_tomador_nome.group()))
      print("cnpj tomador:", clear_blank_lines(busca_tomador_cnpj.group()))
      print("endereço tomador:", clear_blank_lines(busca_tomador_endereco.group()))
      print("municipio tomador:", clear_blank_lines(busca_tomador_municipio.group()))      
      print("nome prestador:", clear_blank_lines(busca_prestador_nome.group()))
      print("cnpj prestador:", clear_blank_lines(busca_prestador_cnpj.group()))
      print("endereço prestador:", clear_blank_lines(busca_prestador_endereco.group()))
      print("municipio prestador:", clear_blank_lines(busca_prestador_municipio.group()))
      print("inscricao municipal:", clear_blank_lines(busca_prestador_inscricao.group()))
      print("csll: ", clear_blank_lines(busca_csll.group()))
      print("Confins: ", clear_blank_lines(busca_confins.group()))
      print("pis/pasep:", clear_blank_lines(busca_pis.group()))
      ##insert nota fiscal
      print(empy_text_column)
      print("descricao das atividades:", clear_blank_lines(busca_atividade.group()))
      print(empy_text_column)
      print("valor servicos:", remove_number_to_text(busca_valor_servico.group())[0])
      print(empy_text_column)
      print("base calculo:", remove_number_to_text(busca_valor_servico.group())[1])
      print(empy_text_column)
      print(empy_text_column)
      print("endereco obra:", busca_endereco_obra.group())
      print("cno:", busca_cno.group())
      print("codigo servico:", clear_blank_lines(busca_codigo_servico.group()))
      print(empy_text_column)
      print("valor total:", clear_blank_lines(busca_valor_total.group()))
      print(empy_text_column)
      print("ir:", clear_blank_lines(busca_ir.group()))
      # local_incidencia_imposto [nao], 
      # descricao_atividades [x], 
      # porcentagem [nao], 
      # servicos [x], 
      # deducoes [nao], 
      # base_de_calculo [x], 
      # inss [nao], 
      # iss_retido [nao], 
      # endereco_obra [x],
      # cno [x], 
      # codigo_servico [x], 
      # valor_total_deducoes [nao], 
      # aliquota [nao], 
      # valor_total_nota[x], 
      # valor_iss [nao], 
      # ir [x]
      
      clear_folder_upload(filepathimage)
      
      # return [
      #   clear_blank_lines(busca_tomador_cnpj.group()),
      #   clear_blank_lines(busca_tomador_nome.group()),
      #   clear_blank_lines(busca_prestador_inscricao.group()),
      #   clear_blank_lines(busca_tomador_endereco.group()),
      #   clear_blank_lines(busca_prestador_cnpj.group()),
      #   clear_blank_lines(busca_prestador_nome.group()),
      #   clear_blank_lines(busca_prestador_inscricao.group()),
      #   clear_blank_lines(busca_prestador_endereco.group()),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(clear_blank_lines(busca_atividade.group())),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines( remove_number_to_text(busca_valor_servico.group())[0]),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(remove_number_to_text(busca_valor_servico.group())[1]),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(busca_endereco_obra.group()),
      #   clear_blank_lines(busca_cno.group()),
      #   clear_blank_lines(clear_blank_lines(busca_codigo_servico.group())),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(clear_blank_lines(busca_valor_total.group())),
      #   clear_blank_lines(empy_text_column),
      #   clear_blank_lines(clear_blank_lines(busca_ir.group()))
      #   ]

      data = {
        "cnpj_tomador": clear_blank_lines(busca_tomador_cnpj.group()),
        "razao_tomador": clear_blank_lines(busca_tomador_nome.group()),
        "insc_mun_tomador": clear_blank_lines(busca_prestador_inscricao.group()),
        "endereco_tomador": clear_blank_lines(busca_tomador_endereco.group()),
        "cnpj_prestador": clear_blank_lines(busca_prestador_cnpj.group()),
        "razao_prestador": clear_blank_lines(busca_prestador_nome.group()),
        "insc_mun_prestador": clear_blank_lines(busca_prestador_inscricao.group()),
        "endereco_prestador": clear_blank_lines(busca_prestador_endereco.group()),
        "local_incidencia_imposto": clear_blank_lines(empy_text_column),
        "descricao_atividades": clear_blank_lines(busca_atividade.group()),
        "porcentagem": clear_blank_lines(empy_text_column),
        "servicos": clear_blank_lines(remove_number_to_text(busca_valor_servico.group())[0]),
        "deducoes": clear_blank_lines(empy_text_column),
        "base_de_calculo": clear_blank_lines(remove_number_to_text(busca_valor_servico.group())[1]),
        "inss": clear_blank_lines(empy_text_column),
        "iss_retido": clear_blank_lines(empy_text_column),
        "endereco_obra": clear_blank_lines(busca_endereco_obra.group()),
        "cno": clear_blank_lines(busca_cno.group()),
        "codigo_servico": clear_blank_lines(busca_codigo_servico.group()),
        "valor_total_deducoes": clear_blank_lines(empy_text_column),
        "aliquota": clear_blank_lines(empy_text_column),
        "valor_total_nota": clear_blank_lines(busca_valor_total.group()),
        "valor_iss": clear_blank_lines(empy_text_column),
        "ir": clear_blank_lines(busca_ir.group())
      }

      json_data = json.dumps(data)

      return json_data

        
    except:
        
      return 400






