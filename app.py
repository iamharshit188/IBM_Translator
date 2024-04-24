#Importing Important Modules : ibm_watson , flask 
# From flask imported flask , render_template for rendering HTML code and imported request for HTTP request , basically for communicating with that Model
from flask import Flask, render_template, request 
from ibm_watson import LanguageTranslatorV3
# Here imported LanguageTranslatorV3 Service , i read about this in your docs
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# This IAMauthenticator as the name says for the authetication of your API keys

# Here app variable is an instance of Flask's class , which represents WSGI application
# WSGI --> (Web Server Gateway Interface) is a standard interface for web servers and web applications in Python. It defines a way for web servers to communicate with web frameworks like Flask, Django, and Pyramid.
app = Flask(__name__)

#IBM Credentials 
authenticator = IAMAuthenticator('your_api_key')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('your_service_url')
# These lines set up the IBM Cloud Language Translator credentials. The IAMAuthenticator object is created with the API key, and then passed to the LanguageTranslatorV3 object. The set_service_url method sets the URL of the Language Translator service.

@app.route('/')
def index():
    """
    This decorator defines a route for the root URL ("/") of the application.
    When a user navigates to this URL, the index function is called,
    which renders the index.html template.
    """
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    """
    This decorator defines a route for the "/translate" URL of the application,
    and specifies that it only responds to HTTP POST requests.
    When a user submits a form with text and a target language,
    the translate function is called.
    It extracts the text and target language from the form data,
    and then uses the IBM Cloud Language Translator to translate the text.
    The translated text is then passed to the index.html template as a variable.
    """
    text = request.form['text']
    target_language = request.form['target_language']

    translation = language_translator.translate(
        text=text,
        model_id=f'en-{target_language}'
    ).get_result()

    translated_text = translation['translations'][0]['translation']
    
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    """
    This block checks if the script is being run directly (not being imported as a module),
    and if so, it starts the Flask application in debug mode.
    Debug mode allows the application to automatically reload when changes are made to the code.
    """
    app.run(debug=True)