from app.models import db, Musician, environment, SCHEMA
from sqlalchemy.sql import text


def seed_musicians():
    the_beatles = Musician(
        name="The Beatles",
        email="thebeatles@music.com",
        hashed_password="password",
        genre="Classic Rock",
        description="Legendary rock band.",
        image_url="http://example.com/images/thebeatles.jpg",
    )

    pink_floyd = Musician(
        name="Pink Floyd",
        email="pinkfloyd@music.com",
        hashed_password="password",
        genre="Progressive Rock",
        description="Pioneers of psychedelic music.",
        image_url="http://example.com/images/pinkfloyd.jpg",
    )

    queen = Musician(
        name="Queen",
        email="queen@music.com",
        hashed_password="password",
        genre="Rock",
        description="Iconic British rock band.",
        image_url="http://example.com/images/queen.jpg",
    )

    nirvana = Musician(
        name="Nirvana",
        email="nirvana@music.com",
        hashed_password="password",
        genre="Grunge",
        description="Key band in the Seattle grunge scene.",
        image_url="http://example.com/images/nirvana.jpg",
    )

    metallica = Musician(
        name="Metallica",
        email="metallica@music.com",
        hashed_password="password",
        genre="Heavy Metal",
        description="One of the most influential heavy metal bands.",
        image_url="http://example.com/images/metallica.jpg",
    )

    the_rolling_stones = Musician(
        name="The Rolling Stones",
        email="therollingstones@music.com",
        hashed_password="password",
        genre="Rock",
        description="Long-standing British rock band.",
        image_url="http://example.com/images/therollingstones.jpg",
    )

    radiohead = Musician(
        name="Radiohead",
        email="radiohead@music.com",
        hashed_password="password",
        genre="Alternative Rock",
        description="Known for their experimental approach.",
        image_url="http://example.com/images/radiohead.jpg",
    )

    led_zeppelin = Musician(
        name="Led Zeppelin",
        email="ledzeppelin@music.com",
        hashed_password="password",
        genre="Hard Rock",
        description="Pioneers of hard rock and heavy metal.",
        image_url="http://example.com/images/ledzeppelin.jpg",
    )

    the_clash = Musician(
        name="The Clash",
        email="theclash@music.com",
        hashed_password="password",
        genre="Punk Rock",
        description="Influential punk rock band.",
        image_url="http://example.com/images/theclash.jpg",
    )

    u2 = Musician(
        name="U2",
        email="u2@music.com",
        hashed_password="password",
        genre="Rock",
        description="Irish rock band known for their anthemic sound.",
        image_url="http://example.com/images/u2.jpg",
    )

    red_hot_chili_peppers = Musician(
        name="Red Hot Chili Peppers",
        email="rhcp@music.com",
        hashed_password="password",
        genre="Funk Rock",
        description="Band known for their fusion of rock, funk, and punk.",
        image_url="http://example.com/images/rhcp.jpg",
    )

    db.session.add_all(
        [
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


def undo_musicians():
    db.session.execute("DELETE FROM musicians")
    db.session.commit()
