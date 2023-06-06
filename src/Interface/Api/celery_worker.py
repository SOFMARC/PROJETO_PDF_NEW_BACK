from src.Interface.Api.utils.clear import clear_folder_upload
from src.Interface.Api.works.work_controller import work_controller
from src.Infra.External.pyodbc.index import Database
from src.Infra.External.celery.index import Celery, current_task

celery = Celery('myapp', broker='redis://localhost:6379/0')

db = Database()

def update_status_in_database(task_id, status):

    db.connect()

    db.update_status_upload(2, task_id)

    db.close()

    print("ID da tarefa:", task_id, status)

    return

@celery.task
def process_pdf(filepath, filename, filepathimage, user_id):

    task_id = current_task.request.id

    print("ID da tarefa:", task_id)

    try:
        work_controller(filepath, filename, filepathimage, user_id, task_id)
        clear_folder_upload(filepath)

        update_status_in_database(task_id, 'completed')
        

    except Exception as e:
        update_status_in_database(task_id, 'faiuld')
    return

celery.conf.update(
    result_backend='redis://localhost:6379/0',
    task_track_started=True
)
