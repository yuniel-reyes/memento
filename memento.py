""" Here it's where the application instance is defined """
import os
from app import create_app, db 
from app.models import User, Post
from flask_migrate import Migrate, migrate

""" Creating an appplication using the app constructor """
app = create_app(os.getenv('MEMENTO_CONFIG') or 'default')
migrate = Migrate(app, db)