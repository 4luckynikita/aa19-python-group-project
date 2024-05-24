from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username="demo",
        is_musician=False,
        email="demo@aa.io",
        password="password",
        first_name="Demo",
        last_name="Last",
        description="Demo Demo Demo",
        image_url="http://example.com/images/demo_musician.jpg",
    )
    demo_musician = User(
        name="Demo Musician",
        is_musician=True,
        email="demo@musician.com",
        password="password",
        genre="Rock",
        description="I am a demo musician",
        image_url="http://example.com/images/demo_musician.jpg",
    )
    marnie = User(
        username="marnie",
        is_musician=False,
        email="marnie@aa.io",
        password="password",
        first_name="Marnie",
        last_name="Marston",
        description="Music 4 Lyfe!",
        image_url="http://example.com/images/test.jpg",
    )
    bobbie = User(
        username="bobbie",
        is_musician=False,
        email="bobbie@aa.io",
        password="password",
        first_name="Bobbie",
        last_name="Smith",
        description="My favorite genre is METALLICA!",
        image_url="http://example.com/images/test.jpg",
    )
    nikita = User(
        username="nikita",
        is_musician=False,
        email="nikita@aa.io",
        password="password",
        first_name="Nikita",
        last_name="Kastyshyn",
        description="I'm down with whatever you got!",
        image_url="http://example.com/images/test.jpg",
    )
    erik = User(
        username="erik",
        is_musician=False,
        email="erik@aa.io",
        password="password",
        first_name="Erik",
        last_name="Hervall",
        description="Rocker and Roller!!!",
        image_url="http://example.com/images/test.jpg",
    )
    cece = User(
        username="cece",
        is_musician=False,
        email="cece@aa.io",
        password="password",
        first_name="Cece",
        last_name="Potakey",
        description="Let's hear some KPOP!",
        image_url="http://example.com/images/test.jpg",
    )
    the_beatles = User(
        name="The Beatles",
        is_musician=True,
        email="thebeatles@music.com",
        password="password",
        genre="Classic Rock",
        description="Legendary rock band.",
        image_url="http://example.com/images/thebeatles.jpg",
    )

    pink_floyd = User(
        name="Pink Floyd",
        is_musician=True,
        email="pinkfloyd@music.com",
        password="password",
        genre="Progressive Rock",
        description="Pioneers of psychedelic music.",
        image_url="http://example.com/images/pinkfloyd.jpg",
    )

    queen = User(
        name="Queen",
        is_musician=True,
        email="queen@music.com",
        password="password",
        genre="Rock",
        description="Iconic British rock band.",
        image_url="http://example.com/images/queen.jpg",
    )

    nirvana = User(
        name="Nirvana",
        is_musician=True,
        email="nirvana@music.com",
        password="password",
        genre="Grunge",
        description="Key band in the Seattle grunge scene.",
        image_url="http://example.com/images/nirvana.jpg",
    )

    metallica = User(
        name="Metallica",
        is_musician=True,
        email="metallica@music.com",
        password="password",
        genre="Heavy Metal",
        description="One of the most influential heavy metal bands.",
        image_url="http://example.com/images/metallica.jpg",
    )

    the_rolling_stones = User(
        name="The Rolling Stones",
        is_musician=True,
        email="therollingstones@music.com",
        password="password",
        genre="Rock",
        description="Long-standing British rock band.",
        image_url="http://example.com/images/therollingstones.jpg",
    )

    radiohead = User(
        name="Radiohead",
        is_musician=True,
        email="radiohead@music.com",
        password="password",
        genre="Alternative Rock",
        description="Known for their experimental approach.",
        image_url="http://example.com/images/radiohead.jpg",
    )

    led_zeppelin = User(
        name="Led Zeppelin",
        is_musician=True,
        email="ledzeppelin@music.com",
        password="password",
        genre="Hard Rock",
        description="Pioneers of hard rock and heavy metal.",
        image_url="http://example.com/images/ledzeppelin.jpg",
    )

    the_clash = User(
        name="The Clash",
        is_musician=True,
        email="theclash@music.com",
        password="password",
        genre="Punk Rock",
        description="Influential punk rock band.",
        image_url="http://example.com/images/theclash.jpg",
    )

    u2 = User(
        name="U2",
        is_musician=True,
        email="u2@music.com",
        password="password",
        genre="Rock",
        description="Irish rock band known for their anthemic sound.",
        image_url="http://example.com/images/u2.jpg",
    )

    red_hot_chili_peppers = User(
        name="Red Hot Chili Peppers",
        is_musician=True,
        email="rhcp@music.com",
        password="password",
        genre="Funk Rock",
        description="Band known for their fusion of rock, funk, and punk.",
        image_url="http://example.com/images/rhcp.jpg",
    )

    db.session.add_all(
        [
            demo,
            demo_musician,
            marnie,
            bobbie,
            nikita,
            erik,
            cece,
            the_beatles,
            pink_floyd,
            queen,
            nirvana,
            metallica,
            the_rolling_stones,
            radiohead,
            led_zeppelin,
            the_clash,
            u2,
            red_hot_chili_peppers,
        ]
    )
    db.session.commit()


def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
