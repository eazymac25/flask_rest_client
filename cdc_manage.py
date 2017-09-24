from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from cdc_app import create_cdc_app, db

app = create_cdc_app()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
