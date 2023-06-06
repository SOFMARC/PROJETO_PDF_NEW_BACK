class PdfToImageFactory:

    @staticmethod
    def convert_from_path(file):
        from pdf2image import convert_from_path
        return convert_from_path(file)
