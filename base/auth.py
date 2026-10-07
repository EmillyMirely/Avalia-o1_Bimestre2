from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database


auth_bp = Blueprint("auth", __name__)


# Complete este arquivo durante a avaliação.
#
# O Blueprint já está criado, mas nenhuma rota foi vinculada ainda.
# Implemente aqui:

@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        flash("Implemente o cadastro com hash de senha.")
        return redirect(url_for("auth.registro"))

    return render_template("registro.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        flash("Implemente o login com session.")
        return redirect(url_for("auth.login"))

    if senha is True:
        senha = check_password_hash
        session["usuario_id"]
        session["usuario_nome"]

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    flash("Implemente o logout com session.")
    return redirect(url_for("auth.index"))

