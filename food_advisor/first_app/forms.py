# forms.py
from django import forms
from .models import Person, Advisor, Item, Report,Favorite_list,Eaten,Target,Feedback

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'email', 'gender', 'phone_no','password']

class AdvisorForm(forms.ModelForm):
    class Meta:
        model = Advisor
        fields = ['name', 'email', 'specification','password']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'category', 'calories', 'vitamin', 'ingredient','image']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['pr_nm','date', 'total_calories', 'total_vitamins','consumed_items','total_ingredient']

class Favorite_listForm(forms.ModelForm):
    class Meta:
        model = Favorite_list
        fields = ['pr_name','item_id']

class EatenForm(forms.ModelForm):
    class Meta:
        model = Eaten
        fields = ['pr_name','item_id','date','quntity']

class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = ['pr_nm','tr_calories', 'tr_vitamins']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','email','message']