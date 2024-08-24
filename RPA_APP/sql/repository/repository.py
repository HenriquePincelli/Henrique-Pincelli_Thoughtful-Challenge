from RPA_APP.extensions import db


class Repository:

    model: db.Model

    # >>>>>>>>>SQL Functions>>>>>>>>>
    def get_by_id(self, id):
        item = self.model
        return item.query.filter(item.ID==id).first()

    def get_all(self, paginate: bool = False, page: int = 1, per_page: int = 10):
        item = self.model
        if paginate:
            return item.query.order_by(item.ID.asc()).paginate(page, per_page)
        else:
            return item.query.order_by(item.ID.asc()).all()

    def add(self, model):
        try:
            db.session.add(model)
            db.session.flush()
        except ValueError as e:
            print(e)
            return None
        else:
            return model

    def delete(self, model):
        try:
            db.session.delete(model)
        except ValueError as e:
            print(e)
            return False
        else:
            return True

    def update(self, model, fields_update: dict):
        model.update().values(fields_update)

    def commit_changes(self):
        db.session.commit()
    # <<<<<<<<<SQL Functions<<<<<<<<<
