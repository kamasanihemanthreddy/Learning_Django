from django import forms
from .models import Document, SalesData,EasycomData

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )

class SalesDataForm(forms.ModelForm):
	class Meta:
		model = SalesData
		fields = '__all__'

class EasycomForm(forms.ModelForm):
	class Meta:
		model = EasycomData
		fields = '__all__'