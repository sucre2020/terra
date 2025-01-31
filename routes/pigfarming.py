from flask import Blueprint, render_template

pigfarming_bp = Blueprint('pigfarming', __name__)

@pigfarming_bp.route('/pigfarming')
def pigfarming():
    return render_template("pigfarming.html")