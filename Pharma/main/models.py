from enum import unique
from djongo import models
# Create your models here.

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)


COUNTRIES = (
    ('','Select Country'),
    ('1', 'Axis'),
    ('2', 'Nairobi'),
    ('3', 'Mombasa'),
    ('4', 'Kiambu'),

)

CITY = (
    ('','Select City'),
    ('1', 'Delhi'),
    ('2', 'Nairobi'),
    ('3', 'Mombasa'),
    ('4', 'Kiambu'),

)

GENDER = (
    ('', 'Choose Gender'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('TRNS','Transgender'),
    ('NSP','Not Specified')
)

TOPHY = (
    ('', 'Type of Pharmacy'),
    ('1', 'Community'),
    ('2', 'Hospital'),
    ('3', 'PHC'),
    ('4', 'Government'),
    ('5', 'Non-Government'),
    ('6', 'Other'),
    ('7', 'No Pharmacy')
)


YEAREXPERIENCE = (
    ('', 'Select Year of Experience'),
    ('1', '1 Year'),
    ('2', '2 Year'),
    ('3', '3 Year'),
    ('4', '4 Year'),
    ('5', '4+ years'),
    ('6', '10+ years'),
    ('7','None')
)

QUALIFICATION = (
    ('', 'Select Qualification'),
    ('1', 'B.Pharma'),
    ('2', 'MBBS'),
    ('3', 'B.Sc Biology'),
    ('4', 'M.Sc Biology'),
    ('5', 'M.Pharma'),
    ('6','Other'),
    ('7','None')
)

TITLE = (
    ('', 'Title'),
    ('1', 'Mr.'),
    ('2', 'Mrs.'),
    ('3', 'Ms'),
    ('4', 'Dr.'),
    ('5', 'Prof.')
)


class Users(models.Model):
    title = models.CharField(max_length=5)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20,unique=True)
    gender = models.CharField(max_length=5,choices=GENDER)
    email = models.EmailField(max_length=30,unique=True)
    phone_number =models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=4,choices=COUNTRIES)
    city = models.CharField(max_length=10,choices=CITY)
    zip_code = models.CharField(max_length=10)
    date_of_Birth = models.DateField()
    type_of_pharmacy = models.CharField(max_length=5,choices=TOPHY)
    Current_Address_of_Pharmacy = models.CharField(max_length=100)
    training_done_till_date = models.DateField()
    Work_experience = models.CharField(max_length=5,choices=YEAREXPERIENCE)
    qualification = models.CharField(max_length=5,choices=YEAREXPERIENCE)
    IdProofNumber = models.CharField(max_length=20)


    def __str__(self):
        return self.first_name
