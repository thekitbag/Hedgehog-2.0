from flask import render_template
from webapp.main import bp


@bp.route('/')
@bp.route('/index')
def index():
	return render_template('main/index.html', title='Home')