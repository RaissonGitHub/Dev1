from django.db.models import QuerySet
from .base_manager import BaseManager
from datetime import date


class ReporterManager(BaseManager):

    def find_by_name(self,nome: str) -> list['Reporter']:
        if isinstance(nome,str) and len(nome) > 0:
            consulta = self.filter(name__icontains=nome).order_by('name')[:2]
            return list(consulta)
        else:
            raise TypeError("O nome deve ser string e não pode ser nulo")
        

   # def find_by_publication_date_since(self, publication_date: date, date: date):
    #    if isinstance(publication_date, date):
     #       consulta = self.filter(article__pub_date__range=(publication_date))
      #      return consulta
       # else:
        #    raise TypeError