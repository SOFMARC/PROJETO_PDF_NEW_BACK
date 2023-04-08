from pdf2image import convert_from_path
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract
from utils.config import path

def image_to_text(file, name):
        images = convert_from_path(file)

        for i in range(len(images)):
            if i == 0:
                        images[i].save(''+path+'/api/uploads/image_pdf/'+name+'.jpg', 'JPEG')
                
        resultado = pytesseract.image_to_string( Image.open(''+path+'/api/uploads/image_pdf/'+name+'.jpg'), lang='por')
        
        return resultado
    
def pdf_to_text(file):
        reader = PdfReader(file)
        page = reader.pages[0]
        text = page.extract_text((0, 90))
        removeCaracter = text.replace('(%)', '').replace('%', '').replace('(R$)', '').replace('R$', '').replace('RS', '')
        
        return removeCaracter