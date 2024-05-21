from app.models import db, Album, User, environment, SCHEMA
from datetime import date
from sqlalchemy.sql import text


def seed_albums():
    abbey_road = Album(
        user_id=User.query.filter_by(name="The Beatles").first().id,
        title="Abbey Road",
        release_date=date(1969, 9, 26),
        description="One of the best albums by The Beatles.",
        image_url="http://example.com/images/abbeyroad.jpg",
    )

    the_dark_side_of_the_moon = Album(
        user_id=User.query.filter_by(name="Pink Floyd").first().id,
        title="The Dark Side of the Moon",
        release_date=date(1973, 3, 1),
        description="A landmark album by Pink Floyd.",
        image_url="http://example.com/images/darksideofmoon.jpg",
    )

    a_night_at_the_opera = Album(
        user_id=User.query.filter_by(name="Queen").first().id,
        title="A Night at the Opera",
        release_date=date(1975, 11, 21),
        description="One of Queen's most celebrated albums.",
        image_url="http://example.com/images/nightattheopera.jpg",
    )

    nevermind = Album(
        user_id=User.query.filter_by(name="Nirvana").first().id,
        title="Nevermind",
        release_date=date(1991, 9, 24),
        description="The album that brought grunge to the mainstream.",
        image_url="http://example.com/images/nevermind.jpg",
    )

    master_of_puppets = Album(
        user_id=User.query.filter_by(name="Metallica").first().id,
        title="Master of Puppets",
        release_date=date(1986, 3, 3),
        description="One of Metallica's most influential albums.",
        image_url="http://example.com/images/masterofpuppets.jpg",
    )

    let_it_bleed = Album(
        user_id=User.query.filter_by(name="The Rolling Stones").first().id,
        title="Let It Bleed",
        release_date=date(1969, 12, 5),
        description="A classic album by The Rolling Stones.",
        image_url="http://example.com/images/letitbleed.jpg",
    )

    ok_computer = Album(
        user_id=User.query.filter_by(name="Radiohead").first().id,
        title="OK Computer",
        release_date=date(1997, 5, 21),
        description="A critically acclaimed album by Radiohead.",
        image_url="http://example.com/images/okcomputer.jpg",
    )

    led_zeppelin_iv = Album(
        user_id=User.query.filter_by(name="Led Zeppelin").first().id,
        title="Led Zeppelin IV",
        release_date=date(1971, 11, 8),
        description="Featuring the iconic 'Stairway to Heaven'.",
        image_url="http://example.com/images/ledzeppeliniv.jpg",
    )

    london_calling = Album(
        user_id=User.query.filter_by(name="The Clash").first().id,
        title="London Calling",
        release_date=date(1979, 12, 14),
        description="A double album by The Clash that became a classic.",
        image_url="http://example.com/images/londoncalling.jpg",
    )

    the_joshua_tree = Album(
        user_id=User.query.filter_by(name="U2").first().id,
        title="The Joshua Tree",
        release_date=date(1987, 3, 9),
        description="The album that brought U2 international fame.",
        image_url="http://example.com/images/joshuatree.jpg",
    )

    californication = Album(
        user_id=User.query.filter_by(name="Red Hot Chili Peppers").first().id,
        title="Californication",
        release_date=date(1999, 6, 8),
        description="One of the band's most successful albums.",
        image_url="http://example.com/images/californication.jpg",
    )

    db.session.add_all(
        [
            abbey_road,
            the_dark_side_of_the_moon,
            a_night_at_the_opera,
            nevermind,
            master_of_puppets,
            let_it_bleed,
            ok_computer,
            led_zeppelin_iv,
            london_calling,
            the_joshua_tree,
            californication,
        ]
    )
    db.session.commit()


def undo_albums():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.albums RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM albums"))

    db.session.commit()