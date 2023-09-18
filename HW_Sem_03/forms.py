from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    login = StringField("Логин", validators=[DataRequired()])
    name = StringField(
        "Имя", validators=[DataRequired(), Regexp(regex=r"[a-zA-Za-яА-я]")]
    )
    surname = StringField(
        "Фамилия", validators=[DataRequired(), Regexp(regex=r"[a-zA-Za-яА-я]")]
    )
    date_birth = DateField("Дата рождения")
    email = StringField("Email", validators=[DataRequired(), Email()])
    consent_processing = BooleanField(
        "Согласие на обработку персональных данных", validators=[DataRequired()]
    )
    password = PasswordField(
        "Пароль",
        validators=[DataRequired(), Length(min=8), Regexp(regex=r"\d+[a-zA-Za-яА-я]+")],
    )
    confirm_password = PasswordField(
        "Повтор пароля", validators=[DataRequired(), EqualTo("password")]
    )
