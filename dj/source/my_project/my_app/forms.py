from django.forms import ModelForm
from .models import *

class default_template_form(ModelForm):
    class Meta:
        model = default_template
        fields = "__all__"