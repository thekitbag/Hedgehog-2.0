from flask import render_template, url_for, request
from webapp.main import bp
from webapp.main.forms import SearchForm
from webapp.main.search import Search
from webapp import posthog


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
	form = SearchForm()
	if form.validate_on_submit():
		results = Search.getSearchResults(form.search_term.data)
		return render_template('main/results.html', title='Search Results', results=results)


	
	if posthog.feature_enabled('survey-landing-page', '123') == True:
		return render_template('main/survey-landing-page.html', title='Home')
	else:
		return render_template('main/index.html', title='Home', form=form)

