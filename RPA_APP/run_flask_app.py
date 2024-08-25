import os
from flask import Flask
from RPA_APP.extensions import db
from RPA_APP.sql.models import AljazeeraModel
from RPA_APP.rpa.procedures import RPAAljazeera
from RPA_APP.rpa.services.aljazeera_service import AljazeeraService
from RPA_APP.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from RPA_APP.payloads import EMAIL_ALJAZEERA, SERCH_PHRASE_ALJAZEERA, SHOW_MORE_ALJAZEERA


print("=-=" * 12)
print("Running 'run_flask_app.py'.........")
print("=-=" * 12)


def create_app(testing=False):
    """Application factory, used to create application"""

    # Basic Flask application settings
    app = Flask(__name__)

    # >>>>>>>>>Database Settings>>>>>>>>>
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    # <<<<<<<<<Database Settings<<<<<<<<<

    # Extensions configuration
    configure_extensions(app)

    return app

def configure_extensions(app):
    """Configure extensions"""
    # >>>>>>>>>Ensures that the database and tables are created within the context of the app>>>>>>>>>
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # <<<<<<<<<Ensures that the database and tables are created within the context of the app<<<<<<<<<

def rpa_procedures():
    """Function to init RPA's"""

    # >>>>>>>>>Aljazeeras's RPA>>>>>>>>>
    service_aljazeera = AljazeeraService()
    # >>>>>>>>>Setting Aljazeera's RPA variables>>>>>>>>>
    # print("=-=" * 24)
    # print("=-==-= Parameter's for Aljazeera's RPA =-==-=")
    email = EMAIL_ALJAZEERA
    search_phrase = SERCH_PHRASE_ALJAZEERA
    show_more = SHOW_MORE_ALJAZEERA
    # email = os.getenv("EMAIL_ALJAZEERA", "pincellihenrique9@gmail.com")
    # search_phrase = os.getenv("SEARCH_PHRASE_ALJAZEERA", "RPA")
    # show_more = os.getenv("SHOW_MORE_ALJAZEERA", 9)
    # send_email = service_aljazeera.get_valid_send_email()
    # if send_email:
    #     email = service_aljazeera.get_valid_email()
    # else:
    #     email = None
    # search_phrase = service_aljazeera.get_valid_search_phrase()
    # show_more = service_aljazeera.get_valid_show_more()
    # print("=-=" * 24)
    # <<<<<<<<<Setting Aljazeera's RPA variables<<<<<<<<<

    # >>>>>>>>>RPA's Procedure>>>>>>>>>
    print("=-=" * 24)
    print("Initiating Aljazeeras's RPA")
    result_aljazeera = RPAAljazeera.newest_news(email=email, search_phrase=search_phrase, show_more=show_more)
    print(">" * 45)
    print(result_aljazeera)
    print("<" * 45)
    print("=-=" * 24)
    # <<<<<<<<<RPA's Procedure<<<<<<<<<
    # <<<<<<<<<Aljazeeras's RPA<<<<<<<<<

if __name__ == "__main__":
    # Application creation and database configuration
    app = create_app(testing=False)

    # >>>>>>>>>Ensure that RPA procedures run within the application context>>>>>>>>>
    with app.app_context():
        rpa_procedures()
    # <<<<<<<<<Ensure that RPA procedures run within the application context<<<<<<<<<
