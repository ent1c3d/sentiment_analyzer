from flask import Flask
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from commands import Seeder
from commands import ClassifierGenerator

import config
from models import db

server = Flask(__name__)

server.debug = config.DEBUG
server.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db.init_app(server)

migrate = Migrate(server, db)
manager = Manager(server)
manager.add_command('db', MigrateCommand)
manager.add_command('seed', Seeder())
manager.add_command('gc', ClassifierGenerator())

if __name__ == '__main__':
    manager.run()
