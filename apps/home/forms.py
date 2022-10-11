from django import forms
from apps.home.models import Person, Lga, Ward

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lga'].queryset = Lga.objects.none()
        
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['lga'].queryset = Lga.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Lga queryset
        elif self.instance.pk:
            self.fields['lga'].queryset = self.instance.state.lga_set.order_by('name')


            self.fields['ward'].queryset = Ward.objects.none()

            if 'ward' in self.data:
                try:
                    ward_id = int(self.data.get('ward'))
                    self.fields['ward'].queryset = Ward.objects.filter(ward_id=ward_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty ward queryset
            elif self.instance.pk:
                self.fields['ward'].queryset = self.instance.lga.ward_set.order_by('name')


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = "__all__"