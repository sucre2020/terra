from flask import Blueprint, render_template

horsefarming_bp = Blueprint('horsefarming', __name__)

@horsefarming_bp.route('/horsefarming')
def horsefarming():
    return render_template('horsefarming.html')