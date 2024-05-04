from django import forms
from .models import CustomUser,Pet

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'phone_number', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'species', 'name', 'breed', 'age', 'gender', 'size', 'behavior',
            'description', 'photo', 'location', 'vaccinated', 'dewormed',
            'neutered_spayed', 'microchipped', 'friendly_with_kids',
            'friendly_with_dogs', 'friendly_with_cats', 'special_needs',
            'adoption_fee', 'color', 'coat_length', 'eye_color', 'weight',
            'health_status',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'special_needs': forms.Textarea(attrs={'rows': 2}),
        }