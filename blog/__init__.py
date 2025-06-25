import os
from flask import Flask
from flask_cors import CORS  # ✅ Import

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='development',
        DATABASE=os.path.join(app.instance_path, 'FLASKTECH.sqlite'),
    )

    # ✅ Apply CORS - Allow specific domains or all
    CORS(app, origins=["https://Pytechblog.com"])  # Replace with your frontend domain(s)
    # CORS(app)  # Use this to allow all origins (not safe for production)

    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)

    from . import tweet
    app.register_blueprint(tweet.bp)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
