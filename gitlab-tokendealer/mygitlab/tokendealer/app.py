import os
from flakon import create_app as _create
from mygitlab.tokendealer.views import blueprints


_HERE = os.path.dirname(__file__)
print(_HERE)
_SETTINGS = os.path.join(_HERE, 'settings.ini')


def create_app(settings=_SETTINGS):
    app = _create(blueprints=blueprints, settings=settings)
    print(app.config['pub_key'])
    # reading key files
    with open(app.config['priv_key']) as f:
        app.config['priv_key'] = f.read()

    with open(app.config['pub_key']) as f:
        app.config['pub_key'] = f.read()

    return app
