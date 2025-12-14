from .base_form import BaseForm
from ..models import Reporter

class ReporterForm(BaseForm):
    class Meta:
        model = Reporter
        fields = '__all__'