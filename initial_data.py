from main import app
from application.sec import datastore
from application.models import db, Role
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()
    datastore.find_or_create_role(name="admin", description="User is an Admin")
    datastore.find_or_create_role(name="creator", description="User is a Creator")
    datastore.find_or_create_role(name="user", description="User is a User")

    db.session.commit()
    if not datastore.find_user(email="admin@email.com"):
        datastore.create_user(email="admin@email.com", password=generate_password_hash("admin"), roles=["admin"])
    if not datastore.find_user(email="creator@email.com"):
        datastore.create_user(email="creator@email.com", password=generate_password_hash("creator"), roles=["creator"], active=False)
    if not datastore.find_user(email="user@email.com"):
        datastore.create_user(email="user@email.com", password=generate_password_hash("user"), roles=["user"])

    db.session.commit()