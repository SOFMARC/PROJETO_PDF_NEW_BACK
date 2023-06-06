from celery import Celery, current_task


class CeleryFactory:
    @staticmethod
    def Celery(self):
        return Celery
    
    def current_task():
        return current_task

