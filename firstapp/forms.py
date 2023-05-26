from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from firstapp.models import Post,ListGroups,ListStudents,UserProfileInfo
from django.contrib.auth.forms import UserChangeForm



class UserFilterForm(forms.Form):
     

    
    experience_min = forms.IntegerField(label='Минимальный стаж(в месяцах)')
    experience_max = forms.IntegerField(label='Максимальный стаж(в месяцах)')

    age_min = forms.IntegerField(label='Минимальный возраст')
    age_max = forms.IntegerField(label='Максимальный возраст')

 
# class ExperienceForm(forms.Form):
#     EXPERIENCE_CHOICES = (
#         ('months', 'Месяцы'),
#         ('years', 'Годы'),
#     )

#     experience_type = forms.ChoiceField(choices=EXPERIENCE_CHOICES, label='Тип стажа')
#     experience_value = forms.IntegerField(label='Значение стажа')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class UserProfileInfoEditForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('direction', 'experience', 'education', 'age', 'place_education', 'atchievments')

class UserProfileInfoFormEdit(forms.ModelForm):


    class Meta:
        model = UserProfileInfo
        fields = ('direction', 'education', 'age', 'place_education', 'atchievments')


class UserProfileInfoForm(forms.ModelForm):
     

    class Meta:
        model = UserProfileInfo
        fields = ('direction', 'education', 'age','experience', 'place_education', 'atchievments')





class UserForm(UserCreationForm):
   

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name',
                   'password1', 'password2')

class UserFormProfile(UserChangeForm):
     

    class Meta():
        model = User
        fields = ('first_name', 'last_name',)
  


class AddGroupForm(forms.ModelForm):
    class Meta:
        model = ListGroups
        fields = ('name','description')

 



class AddStudentsForm(forms.ModelForm):
    class Meta:
        model = ListStudents
        fields = ('groups', 'fio', 'age', 'birsday', 'pol', 'place_learning', 'sertificat_pfdo', 'fio_parents', 'contact_data', 'atchievments')
        widgets = {
        'groups': forms.CheckboxSelectMultiple(),  
        }


class FilterStudentsForm(forms.Form):
    age_choices = (
        ('', 'Любой'),
        ('6-8', '6-8'),
        ('9-11', '9-11'),
        ('12-14', '12-14'),
        ('15-16', '15-16'),
        ('17-18', '17-18'),
      
    )
    
    gender_choices = (
        ('', 'Любой'),
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )

    age = forms.TypedChoiceField(label='Возраст', choices=age_choices, required=False, coerce=str)
    gender = forms.ChoiceField(label='Пол', choices=gender_choices, required=False)