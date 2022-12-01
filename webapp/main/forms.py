from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class SearchForm(FlaskForm):
	search = StringField('Search for places to eat or drink', validators=[DataRequired()])
	submit = SubmitField('Search')