from flask import Blueprint, render_template

goatfarming_bp = Blueprint('goatfarming', __name__)

@goatfarming_bp.route('/goatfarming')
def goatfarming():
    return render_template("goatfarming.html")