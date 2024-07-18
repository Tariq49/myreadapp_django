from django import forms
from apps.core.constants import BOOK_CATEGORY, BOOK_FORMAT, BOOK_LANGUAGES

from apps.book.models import Tag


class PostBookForm(forms.Form):
    isbn = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "isbn-input",
                "placeholder": "Enter isbn"
            }
        )
    )

    title  = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "title-input",
                "placeholder": "Enter text"
            }
        )
    )

    pages = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "pages-input",
                "placeholder": "Enter pages"
            }
        )
    )

    description = forms.CharField(
        required = False,
        widget=forms.Textarea(
            attrs={
                "class": "description-input",
                "placeholder": "Enter description"
            }
        )
    )


    categories = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                "class": "form-cat"
                
            }
        ),
        choices=BOOK_CATEGORY, 
        initial= 'pr'
    )

    published_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "published_date-input",
                "placeholder": "Enter published date"
                
            }
        )
    )

    publisher = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "publisher-input",
                "placeholder": "Enter publisher"
                
            }
        )
        
    )

    authors = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "authors-input",
                "placeholder": "Enter authors"
                
            }
        )
        
    )


    language = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                "class": "language-select"
                
            }

        ), choices=BOOK_LANGUAGES,
        initial='en'
    )

    book_format = forms.ChoiceField(
        required=True,
        widget = forms.Select(
            attrs={
                "class": "book_format-select",
                

            }
        ), choices=BOOK_FORMAT
    )



    lang = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "language-input",
                "placeholder": "Enter the language"
                
            }

        )
    )

    edition = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs= {
                "class": "edition-input",
                "placeholder":"Enter book edition"
            }
        )
    )

 
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "tags-input"
            }
        )
    )
