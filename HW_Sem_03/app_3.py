from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd41286730f6c3c4e9cd328a1b42c6eaff1131f3fc727a7fb8b12bda95e735c36'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///registered_users.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        login = form.login.data
        name = form.name.data
        surname = form.surname.data
        date_birth = form.date_birth.data
        email = form.email.data
        consent_processing = form.consent_processing.data
        password = form.password.data
        existing_user = User.query.filter((User.login == login) | (User.email == email)).first()
        if existing_user:
            error_msg = 'Login or email already exists.'
            form.name.errors.append(error_msg)
            return render_template('register.html', form=form)
        new_user = User(login=login, name=name, surname=surname, date_birth=date_birth, email=email,
                        consent_processing=consent_processing, password=password)
        new_user.encrypt_password(password)
        db.session.add(new_user)
        db.session.commit()
        # Выводим сообщение об успешной регистрации
        success_msg = 'Вы зарегистрированы!'
        return success_msg
    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
