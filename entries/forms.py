from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
    # extra info about class
    class Meta:
        model = Entry
        fields = ('text', )

    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'textarea', 'placeholder': 'What\'s on your mind?'})
