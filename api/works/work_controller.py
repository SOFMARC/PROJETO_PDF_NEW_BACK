from works.work_template_nfs_cajamar import work_template_nfs_cajamar
from works.work_template_nfs_trindade import work_template_nfs_trindade
from works.work_template_nfs_bassano import work_template_nfs_bassano
from works.work_template_nfs_osasco import work_template_nfs_osasco
from works.work_template_nfs_sp import work_template_nfs_sp
from works.work_template_nfs_biguacu import work_template_nfs_biguacu
from works.work_template_nfs_suzanu import work_template_nfs_suzanu
from provider.database import Database
from utils.uuid import Id

works = [
        work_template_nfs_osasco,
        work_template_nfs_cajamar, 
        work_template_nfs_trindade, 
        work_template_nfs_bassano,
        work_template_nfs_sp,
        work_template_nfs_biguacu,
        work_template_nfs_suzanu ]

def work_controller(filepath, filename, filepathimage):
    
    i = 0

    while(i < len(works)):
        res = works[i](filepath, filename, filepathimage)
        
        print("########## fim da extração ########", res != 400 and 200 or 400)
        
        if res != 400:
            data = insert_nfs(res)
            
            return data
        
        i += 1     
        

def insert_nfs(data):
    print("dados", data)
    try:

        unique_id:int = Id()
        user_id = 1

        db = Database()

        db.connect()
        
        db.insert_data_tomador(user_id, unique_id,  data[0], data[1], data[2], data[3])
        
        db.insert_data_prestacao(user_id, unique_id, data[4], data[5], data[6], data[7])

        print("infos:",  data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23])

        db.insert_nota_fiscal(user_id, unique_id, data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23])
        
        db.close()

        
        return 200
        
    except:
        
        return 400