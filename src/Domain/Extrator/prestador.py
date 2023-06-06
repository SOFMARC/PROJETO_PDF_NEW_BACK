class Prestador:
    def __init__(self, cnpj_prestador: str, razao_prestador: str, insc_mun_prestador: str, endereco_prestador: str):
        self._cnpj_prestador = cnpj_prestador
        self._razao_prestador = razao_prestador
        self._insc_mun_prestador = insc_mun_prestador
        self._endereco_prestador = endereco_prestador

    @property
    def cnpj_prestador(self):
        return self._cnpj_prestador
    
    @property
    def razao_prestador(self):
        return self._razao_prestador
    
    @property
    def insc_mun_prestador(self):
        return self._insc_mun_prestador
    
    @property
    def endereco_prestador(self):
        return self._endereco_prestador