# Задание
# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан
# cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия, где будет
# отображаться имя пользователя. На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён
# cookie-файл с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'd41286730f6c3c4e9cd328a1b42c6eaff1131f3fc727a7fb8b12bda95e735c36'


@app.route("/", methods=["GET", "POST"])
def login():
    context = {"login": "Авторизоваться"}
    if request.method == "POST":
        session["name"] = request.form.get("name")
        session["email"] = request.form.get("email")
        return redirect(url_for("welcome_page"))
    return render_template("login.html", **context)


@app.route("/welcome_page", methods=["GET", "POST"])
def welcome_page():
    if "name" in session:
        context = {
            "name": session["name"],
            "email": session["email"],
            "title": "Страница приветствия",
        }
        if request.method == "POST":
            session.pop("name", None)
            session.pop("email", None)
            return redirect(url_for("login"))
        return render_template("welcome_page.html", **context)
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
