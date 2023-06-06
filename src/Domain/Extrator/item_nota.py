class NotaFiscal:
    def __init__(self, local_incidencia_imposto: str, descricao_atividades: str, porcentagem: str, servicos: str, deducoes: str, base_de_calculo: str, inss: str, iss_retido: str, endereco_obra: str, cno: str, codigo_servico: str, valor_total_deducoes: str, aliquota: str, valor_total_nota: str, valor_iss: str, ir: str,):
        self._local_incidencia_imposto = local_incidencia_imposto
        self._descricao_atividades = descricao_atividades
        self._porcentagem = porcentagem
        self._servicos = servicos
        self._deducoes = deducoes
        self._base_de_calculo = base_de_calculo
        self._inss = inss
        self._iss_retido = iss_retido
        self._endereco_obra = endereco_obra
        self._cno = cno
        self._codigo_servico =  codigo_servico
        self._valor_total_deducoes =  valor_total_deducoes
        self._aliquota =  aliquota
        self._valor_total_nota = valor_total_nota 
        self._valor_iss =  valor_iss
        self._ir =  ir
            
    @property
    def local_incidencia_imposto(self):
        return self._local_incidencia_imposto
    
    @property
    def descricao_atividades(self):
        return self._descricao_atividades
    
    @property
    def porcentagem(self):
        return self._porcentagem
    
    @property
    def servicos(self):
        return self._servicos
    
    @property
    def deducoes(self):
        return self._deducoes
    
    @property
    def base_de_calculo(self):
        return self._base_de_calculo
    
    @property
    def inss(self):
        return self._inss
    
    @property
    def iss_retido(self):
        return self._iss_retido
    
    @property
    def endereco_obra(self):
        return self._endereco_obra
    
    @property
    def cno(self):
        return self._cno
    
    @property
    def codigo_servico(self):
        return self._codigo_servico
    
    @property
    def valor_total_deducoes(self):
        return self._valor_total_deducoes
    
    @property
    def aliquota(self):
        return self._aliquota
    
    @property
    def valor_total_nota(self):
        return self._valor_total_nota
    
    @property
    def valor_iss(self):
        return self._valor_iss
    
    @property
    def ir(self):
        return self._ir