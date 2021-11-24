from django.forms import ModelForm
from models import order


class orderForm(ModelForm):
    class Meta:
        model = order
        exclude = ()