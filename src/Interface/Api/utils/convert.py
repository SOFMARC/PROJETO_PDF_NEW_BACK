from src.Interface.Api.utils.config import path
from src.Infra.External.PyPDF2.index import PdfReaderFactory
from src.Infra.External.pillow.index import PillowImageFactory
from src.Infra.External.tesseract.index import TesseractFactory
from src.Infra.External.pdf2image.index import PdfToImageFactory

def image_to_text(file, name):
        print("image to text v2")
        
        images = PdfToImageFactory.convert_from_path(file)
        
        print("convert images", images)

        for i in range(len(images)):
            if i == 0: 
                images[i].save(path+'Api/uploads/image_pdf/'+name+'.jpg', 'JPEG')
                print('image convertida com sucesso')
                
        resultado = TesseractFactory.pytesseract().image_to_string( PillowImageFactory.Image().open(path+'Api/uploads/image_pdf/'+name+'.jpg'), lang='por')

        print("success convert images", resultado)

        return resultado
    
def pdf_to_text(file):
        print('text')
        reader = PdfReaderFactory.PdfReader(file)
        page = reader.pages[0]
        text = page.extract_text((0, 90))
        removeCaracter = text.replace('(%)', '').replace('%', '').replace('(R$)', '').replace('R$', '').replace('RS', '')
        print('text certo', removeCaracter)
        
        return removeCaracter 