"""\
The Git Serve

The Github lottery.
"""

from flask import Flask

__version__ = '0.1'


# Flask application
app = Flask(__name__)
app.config.from_object('default_config')
app.config.from_envvar('SETTINGS_MODULE', silent=True)


#Views
@app.route('/')
def index():
    return 'The GitServe'


# Run development server
if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'], app.debug != False)
