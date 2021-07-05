from enum import unique
from .models import Users
from django import forms
from django.core import validators
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, HTML, Row, Column, Layout, Submit
from crispy_forms.bootstrap import PrependedText
from .models import CITY, COUNTRIES, TOPHY, YEAREXPERIENCE,GENDER,TITLE,QUALIFICATION



class RegistrationForm(forms.ModelForm):

    title = forms.ChoiceField(choices=TITLE)

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
        validators=[validators.MaxLengthValidator(20),
                    ]
    )

    second_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
                                  validators=[validators.MaxLengthValidator(15)
                                              ],
                                  )
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),
                               validators=[validators.MaxLengthValidator(20),
                               validators.RegexValidator(
                                   regex='^[a-zA-Z0-9]*$',
                                   message=['Username must be Alphanumeric','No Special Symbol Allowed',
                                   'user only lowercase latter'],
                                   code='invalid_username'
                               )
    ],)

    gender = forms.ChoiceField(choices=GENDER,
                               )
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                             validators=[validators.EmailValidator,validators.MaxLengthValidator(30)]
                             )
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Mobile No'}),
                                   validators=[validators.MaxLengthValidator(15)])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
                               validators=[validators.MaxLengthValidator(30),validators.MinLengthValidator(6)]
                               )
    address = forms.CharField(
        label='Address',
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter full address', 'rows': '3'})
    )

    country = forms.ChoiceField(choices=COUNTRIES)
    city = forms.ChoiceField(choices=CITY)
    zip_code = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': 'Pincode'}),validators=[validators.MaxLengthValidator(10)])
    date_of_Birth = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'Date of Birth'}))

    type_of_pharmacy = forms.ChoiceField(choices=TOPHY)

    Current_Address_of_Pharmacy = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter Current Store Address', 'rows': '3'}),
                                                  validators=[validators.MaxLengthValidator(120)])

    training_done_till_date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'Date of Birth'}))

    Work_experience = forms.ChoiceField(choices=YEAREXPERIENCE)
    qualification = forms.ChoiceField(choices=QUALIFICATION)
    # IdProof = forms.FileField(widget=forms.FileInput(attrs={'type': 'file',
    #                                                         'enctype':'multipart/form-data'
    #                                                         }))

    IdProofNumber = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Proof Id Unique No'}))

    check_me_out = forms.BooleanField(required=False)


    class Meta:
        model = Users
        fields = '__all__'
        get_latest_by = 'order_date'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False

        self.helper.layout = Layout(
            Fieldset(
                'Account Details',
                HTML('<hr>'),
                Row(
                    Column(
                        PrependedText('username', '@', active=True), css_class='form-group col-md-6 mb-0'),
                    Column('phone_number', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row',
                ),
                Row(
                    Column('email', css_class='form-group col-md-6 mb-0'),
                    Column('password', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row',
                )
            ),
            HTML('<br>'),
            Fieldset(
                'Basic Details',
                HTML("<hr>"),
                Row(
                    Column('title', css_class='form-group col-md-2 mb-0'),
                    Column('first_name', css_class='form-group col-md-5 mb-0'),
                    Column('second_name', css_class='form-group col-md-5 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('gender', css_class='form-group col-md-6 mb-0'),
                    Column(
                        PrependedText('date_of_Birth', 'DOB'), css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('address', css_class='form-group col-md-12 mb-0'),

                ),
                Row(
                    Column('country', css_class='form-group col-md-4 mb-0'),
                    Column('city', css_class='form-group col-md-4 mb-0'),
                    Column('zip_code', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    HTML(
                        '<span style="margin-left:5px">Upolad Any Government ID Proof (Adhar/PAN/Driving Licence)*</span>'),
                    # Column('IdProof', css_class='form-group col-md-12 mb-0'),
                    Column('IdProofNumber',
                           css_class='form-group col-md-12 mb-0'),
                    css_class='form-row'
                ),

                HTML("<br>"),
                Fieldset('Education/Work Details',
                         HTML("<hr>"),
                         Row(
                             Column('type_of_pharmacy',
                                    css_class='form-group col-md-6 mb-0'),
                             Column('Work_experience',
                                    css_class='form-group col-md-6 mb-0'),
                             css_class='form-row'
                         ),
                         Row(
                             Column('qualification',
                                    css_class='form-group col-md-6 mb-0'),
                             Column('training_done_till_date',
                                    css_class='form-group col-md-6 mb-0'),
                             css_class='form-row'
                         ),
                         Row(
                             Column('Current_Address_of_Pharmacy',
                                    css_class='form-group col-md-12 mb-0'),

                         ),

                         Row(
                             Column('check_me_out',
                                    css_class='form-group col-md-1 mb-0'),
                             Column(
                                 HTML('I accept the <a href="#">Terms of Use</a> & <a href="#">Privacy Policy</a>'), css_class='form-group col-md-11 mb-0'),

                         ),

                         Submit('submit', 'Sign In',
                                css_class='btn btn-success  btn-block')
                         )
            ))


class LoginForm(forms.Form):

    userLoginId = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username/Email/Mobile'}))
    userLoginPassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False

        self.helper.layout = Layout(
                Row(
                    Column('userLoginId', css_class='form-group col-md-12 mb-0'),
                    Column('userLoginPassword', css_class='form-group col-md-12 mb-0'),
                    css_class='form-row',
                ),
            Submit('submit', 'Log in',css_class='btn btn-success  btn-block')
            )

    