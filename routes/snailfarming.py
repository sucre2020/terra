from flask import Blueprint, render_template

snailfarming_bp = Blueprint('snailfarming', __name__)

@snailfarming_bp.route('/snailfarming')
def snailfarming():
    return render_template('snailfarming.html')