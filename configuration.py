from routes.home import home_route
from routes.costumer import costumer_route
from data_base.data_base import db
from data_base.models.costumer import Costumer

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(costumer_route, url_prefix = "/costumer")

def configure_db():
    db.connect()
    db.create_tables([Costumer])