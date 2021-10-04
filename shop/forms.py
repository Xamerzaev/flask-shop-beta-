from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import email_validator
from shop.models import User

class RegForm(FlaskForm):
    email = StringField('Email',validators=[Email('Не правильно ввели свой email'), DataRequired('Это поле обязательно!')])
    password = PasswordField('Пароль', validators=[DataRequired('Это поле обязательно!')])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired('Это поле обязательно!'), EqualTo('password')])
    submit = SubmitField ('Регистрация')

    def validate_email (self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError ('Пользователь с таким email уже существует!')