#forms.py

from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField("Id Number of puppy to remove: ")
    submit = SubmitField("Remove puppy")



class AddOwnerForm(FlaskForm):
    name = StringField('name of owner: ')
    pup_id = IntegerField("Id of Puppy: ")
    submit = SubmitField("Add Owner")