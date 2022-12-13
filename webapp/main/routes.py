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
		search_term = form.search_term.data
		results = Search.getSearchResults(search_term)
		return render_template('main/results.html', title='Search Results', results=results, search_term=search_term)


	
	if posthog.feature_enabled('survey-landing-page', '123') == True:
		return render_template('experiments/survey-landing-page.html', title='Home')
	else:
		return render_template('main/index.html', title='Home', form=form)

@bp.route('/place', methods=['GET'])
def place():
	place = {
		"name": "pubbypub",
		"place_type": "Pub",
		"location": "Bursledon",
		"address": "2 The High Street, Bursledon, Southampton, Hants, SO31 8AA",
		"score": 74,
		"reviews": "                             ",
	}
	return render_template('main/place.html', title='Search Results', place=place)

@bp.route('/interest', methods=['GET'])
def interest():
	return render_template('experiments/interest.html')

