from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username="Demo",
        email="demo@aa.io",
        hashed_password="password",
        first_name="Demo",
        last_name="Last",
        bio="Demo Demo Demo",
        image_url="http://example.com/images/test.jpg",
    )
    marnie = User(
        username="marnie",
        email="marnie@aa.io",
        hashed_password="password",
        first_name="Marnie",
        last_name="Marston",
        bio="Music 4 Lyfe!",
        image_url="http://example.com/images/test.jpg",
    )
    bobbie = User(
        username="bobbie",
        email="bobbie@aa.io",
        hashed_password="password",
        first_name="Bobbie",
        last_name="Smith",
        bio="Rocker and Roller",
        image_url="http://example.com/images/test.jpg",
    )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
