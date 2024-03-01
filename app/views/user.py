from flask import Blueprint, render_template, url_for, request, redirect
from ..extensions import db

bp = Blueprint('users', __name__)

@bp.route('/register', methods=["GET", "POST"])
def register():
    return render_template('users/register.html')

@bp.route('/login', methods=["GET", "POST"])
def login():
    return render_template('users/login.html')

@bp.route('/logout')
def logout():
    return redirect(url_for('users.login'))