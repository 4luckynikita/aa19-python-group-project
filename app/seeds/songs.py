from app.models import db, Song, Album, environment, SCHEMA
from sqlalchemy.sql import text


def seed_songs():
    come_together = Song(
        album_id=Album.query.filter_by(title="Abbey Road").first().id,
        title="Come Together",
        duration=259,
        image_url="http://example.com/images/cometogether.jpg",
    )

    money = Song(
        album_id=Album.query.filter_by(title="The Dark Side of the Moon").first().id,
        title="Money",
        duration=382,
        image_url="http://example.com/images/money.jpg",
    )

    bohemian_rhapsody = Song(
        album_id=Album.query.filter_by(title="A Night at the Opera").first().id,
        title="Bohemian Rhapsody",
        duration=354,
        image_url="http://example.com/images/bohemianrhapsody.jpg",
    )

    smells_like_teen_spirit = Song(
        album_id=Album.query.filter_by(title="Nevermind").first().id,
        title="Smells Like Teen Spirit",
        duration=301,
        image_url="http://example.com/images/smellsliketeenspirit.jpg",
    )

    master_of_puppets_song = Song(
        album_id=Album.query.filter_by(title="Master of Puppets").first().id,
        title="Master of Puppets",
        duration=515,
        image_url="http://example.com/images/masterofpuppets_song.jpg",
    )

    gimme_shelter = Song(
        album_id=Album.query.filter_by(title="Let It Bleed").first().id,
        title="Gimme Shelter",
        duration=272,
        image_url="http://example.com/images/gimmeshelter.jpg",
    )

    paranoid_android = Song(
        album_id=Album.query.filter_by(title="OK Computer").first().id,
        title="Paranoid Android",
        duration=387,
        image_url="http://example.com/images/paranoidandroid.jpg",
    )

    stairway_to_heaven = Song(
        album_id=Album.query.filter_by(title="Led Zeppelin IV").first().id,
        title="Stairway to Heaven",
        duration=482,
        image_url="http://example.com/images/stairwaytoheaven.jpg",
    )

    london_calling_song = Song(
        album_id=Album.query.filter_by(title="London Calling").first().id,
        title="London Calling",
        duration=202,
        image_url="http://example.com/images/londoncalling_song.jpg",
    )

    with_or_without_you = Song(
        album_id=Album.query.filter_by(title="The Joshua Tree").first().id,
        title="With or Without You",
        duration=296,
        image_url="http://example.com/images/withorwithoutyou.jpg",
    )

    californication_song = Song(
        album_id=Album.query.filter_by(title="Californication").first().id,
        title="Californication",
        duration=329,
        image_url="http://example.com/images/californication_song.jpg",
    )

    db.session.add_all(
        [
            come_together,
            money,
            bohemian_rhapsody,
            smells_like_teen_spirit,
            master_of_puppets_song,
            gimme_shelter,
            paranoid_android,
            stairway_to_heaven,
            london_calling_song,
            with_or_without_you,
            californication_song,
        ]
    )
    db.session.commit()


def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.songs RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))

    db.session.commit()
