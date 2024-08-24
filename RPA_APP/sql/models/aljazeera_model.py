from RPA_APP.extensions import db


class AljazeeraModel(db.Model):

    __tablename__ = "aljazeera"

    # >>>>>>>>>Aljazeera Model>>>>>>>>>
    id = db.Column(db.Integer, primary_key=True)
    id_aljazeera = db.Column(db.Integer, autoincrement=True)
    email = db.Column(db.String(100), nullable=True)
    search_phrase = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.Text, nullable=False)
    picture_filename = db.Column(db.String(255), nullable=False)
    picture_url = db.Column(db.Text, nullable=False)
    picture_saved = db.Column(db.Boolean, nullable=False)
    count_search_phrase = db.Column(db.Integer, nullable=False)
    money = db.Column(db.Boolean, nullable=True)
    dt_insert = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    dt_update = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    active = db.Column(db.Boolean, default=True)
    # <<<<<<<<<Aljazeera Model<<<<<<<<<
