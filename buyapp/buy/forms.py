from django import forms
from .models import *

class DeptCreateForm(forms.ModelForm):

    def __init__(self,*args, **kwargs): 
        super().__init__(*args, **kwargs)
        for field in self.fields.values(): 
            field.widget.attrs["class"] = 'form-control'
    
    class Meta:
        model = DeptMaster
        fields = '__all__'

class PlaceCreateForm(forms.ModelForm):
    
    def __init__(self,*args, **kwargs): 
        super().__init__(*args, **kwargs)
        for field in self.fields.values(): 
            field.widget.attrs["class"] = 'form-control'
    
    class Meta:
        model = PurchaserMaster
        fields = '__all__'

class DeptEditForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dept_id'].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = DeptMaster
        fields = '__all__'
        widgets ={
            'dept_id':forms.TextInput(attrs={
                "class": "form-control",

            }),
            'dept':forms.TextInput(attrs={
                "class": "form-control",
            }),
            'note':forms.TextInput(attrs={
                "class": "form-control",
                }),
        }

class PlaceEditForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['store_id'].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = PurchaserMaster
        fields = '__all__'
        widgets ={
            'store_id':forms.TextInput(attrs={
                "class": "form-control",
            }),
            'place':forms.TextInput(attrs={
                "class": "form-control",
            }),
            'note':forms.TextInput(attrs={
                "class": "form-control",
            }),
        }

class AddListForm(forms.ModelForm):
    class Meta:
        model = ListOfPurchases
        fields = '__all__'
        widgets ={
            'order_day':forms.NumberInput(attrs={
                "type": "date",
            }),
            'item_name':forms.TextInput(attrs={
                'list':'item',
            })
        }

