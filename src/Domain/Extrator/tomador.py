class Tomador:
    def __init__(self, cnpj_tomador: str, razao_tomador: str, insc_mun_tomador: str, endereco_tomador: str):
        self._cnpj_tomador = cnpj_tomador
        self._razao_tomador = razao_tomador
        self._insc_mun_tomador = insc_mun_tomador
        self._endereco_tomador = endereco_tomador

    @property
    def cnpj_tomador(self):
        return self._cnpj_tomador
    
    @property
    def razao_tomador(self):
        return self._razao_tomador
    
    @property
    def insc_mun_tomador(self):
        return self._insc_mun_tomador
    
    @property
    def endereco_tomador(self):
        return self._endereco_tomador