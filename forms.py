from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length

class CurrencyConverterForm(FlaskForm):
    from_currency = StringField('From Currency', validators=[DataRequired(), Length(min=3, max=3)])
    to_currency = StringField('To Currency', validators=[DataRequired(), Length(min=3, max=3)])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Convert')
