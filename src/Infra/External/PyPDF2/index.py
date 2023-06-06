from PyPDF2 import PdfReader

class PdfReaderFactory:
    @staticmethod
    def PdfReader(file):
        return PdfReader(file)