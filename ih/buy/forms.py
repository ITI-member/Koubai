from dataclasses import field
from sqlite3 import SQLITE_DROP_TEMP_INDEX
from tkinter import Widget
from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget

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
        self.fields['place_id'].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = PurchaserMaster
        fields = '__all__'
        widgets ={
            'place_id':forms.TextInput(attrs={
                "class": "form-control",
            }),
            'place':forms.TextInput(attrs={
                "class": "form-control",
            }),
            'note':forms.TextInput(attrs={
                "class": "form-control",
                }),
        
        }




class CustomModelDeptChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj): # label_from_instance 関数をオーバーライド
         return obj.dept # 表示したいカラム名を return

class CustomModelStoreChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj): # label_from_instance 関数をオーバーライド
         return obj.place # 表示したいカラム名を return

class AddListForm(forms.ModelForm):
    deploy_id = CustomModelDeptChoiceField(queryset=DeptMaster.objects.all(),) # 上記のクラスを参照する様変更
    store_id = CustomModelStoreChoiceField(queryset=PurchaserMaster.objects.all())
    item_name = forms.TextInput()
    user_id = forms.TextInput()
    unit_prise = forms.IntegerField()
    quantity = forms.IntegerField()
    total_due = forms.IntegerField()
    remarks = forms.TextInput()
    
    class Meta:
        model = ListOfPurchases
        fields = '__all__'
