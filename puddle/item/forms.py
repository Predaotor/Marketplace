from django import forms 
from .models import Item 

INPUT_CLASSES="w-full py-6 rounded-xl border"

class NewItemform(forms.ModelForm):
    """
    NewItemform is a ModelForm for creating and updating Item instances.
    
    """
    class Meta:
        model=Item 
        fields=('category','name', 'description', 'price', 'image', )

        widgets={
         'category':forms.Select(attrs={
            'class':'w-full py-6 rounded-xl border'
         }),
         'name':forms.TextInput(attrs={
             'class':INPUT_CLASSES
         }),
         'description':forms.TextInput(attrs={
            'class':INPUT_CLASSES
         }),
         'price':forms.TextInput(attrs={
             'class':INPUT_CLASSES
         }
                                 ),
         'image':forms.FileInput(attrs={
             'class':INPUT_CLASSES
         })
    }
        

class EditItemform(forms.ModelForm):
    """
    EditItemform is a ModelForm for editing an Item instance.
    
            model (Item): The model that this form is associated with.
            fields (tuple): The fields to include in the form.
            widgets (dict): A dictionary specifying custom widgets for each field.
    """
    class Meta:
        model=Item 
        fields=('name', 'description', 'price', 'image', 'is_sold' )

        widgets={
         'name':forms.TextInput(attrs={
             'class':INPUT_CLASSES
         }),
         'description':forms.TextInput(attrs={
            'class':INPUT_CLASSES
         }),
         'price':forms.TextInput(attrs={
             'class':INPUT_CLASSES
         }
                                 ),
         'image':forms.FileInput(attrs={
             'class':INPUT_CLASSES
         })
    }