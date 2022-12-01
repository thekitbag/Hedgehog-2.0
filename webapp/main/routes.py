from flask import render_template, url_for, request
from webapp.main import bp
from webapp.main.forms import SearchForm
from webapp import posthog


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		return "Postymcpostyson"

	form = SearchForm()
	if posthog.feature_enabled('survey-landing-page', '123') == True:
		return render_template('main/survey-landing-page.html', title='Home')
	else:
		return render_template('main/index.html', title='Home', form=form)