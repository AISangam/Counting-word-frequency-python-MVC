from app import *
from app.views import home_page, register_view, login_view, nlp_freq_occurence, logout_view


@app.route('/', methods=['GET', 'POST'])
def home():
    return home_page()

@app.route('/login/', methods=['GET', 'POST'])
def login():
    return login_view()

@app.route('/register/', methods=['GET', 'POST'])
def register():
    return register_view()    


@app.route('/frequency_occurency', methods=['GET', 'POST'])
def frequency():
	return nlp_freq_occurence()


# @app.route('/frequency_occurrency', methods=['GET', 'POST'])
# def frequency_occurence_values():
# 	return frequency()



@app.route('/logout/')
def logout():
    return logout_view()