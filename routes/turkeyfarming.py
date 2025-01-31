from flask import Blueprint, render_template

turkeyfarming_bp = Blueprint('turkeyfarming', __name__)

@turkeyfarming_bp.route('/turkeyfarming')
def turkeyfarming():
    return render_template('turkeyfarming.html')