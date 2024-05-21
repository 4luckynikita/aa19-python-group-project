from app.models import db, Review, User, Album, environment, SCHEMA
from sqlalchemy.sql import text


def seed_reviews():
    abbey_road_review = Review(
        user_id=User.query.filter_by(username="demo").first().id,
        reviewable_type="Album",
        reviewable_id=Album.query.filter_by(title="Abbey Road").first().id,
        rating=5,
        comment="Amazing album!",
    )

    dark_side_of_the_moon_review = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        reviewable_id=Album.query.filter_by(title="The Dark Side of the Moon")
        .first()
        .id,
        rating=5,
        comment="A masterpiece!",
    )

    night_at_the_opera_review = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        reviewable_id=Album.query.filter_by(title="A Night at the Opera").first().id,
        rating=4,
        comment="An incredible work by Queen!",
    )

    nevermind_review = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        reviewable_id=Album.query.filter_by(title="Nevermind").first().id,
        rating=5,
        comment="A defining album of its generation!",
    )

    master_of_puppets_review = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        reviewable_id=Album.query.filter_by(title="Master of Puppets").first().id,
        rating=5,
        comment="An iconic metal album!",
    )

    let_it_bleed_review = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        reviewable_id=Album.query.filter_by(title="Let It Bleed").first().id,
        rating=4,
        comment="A classic Rolling Stones album!",
    )

    ok_computer_review = Review(
        user_id=User.query.filter_by(username="demo").first().id,
        reviewable_type="Album",
        reviewable_id=Album.query.filter_by(title="OK Computer").first().id,
        rating=5,
        comment="A revolutionary album by Radiohead!",
    )

    led_zeppelin_iv_review = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        reviewable_id=Album.query.filter_by(title="Led Zeppelin IV").first().id,
        rating=5,
        comment="A timeless classic!",
    )

    london_calling_review = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        reviewable_id=Album.query.filter_by(title="London Calling").first().id,
        rating=4,
        comment="A must-listen punk album!",
    )

    the_joshua_tree_review = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        reviewable_id=Album.query.filter_by(title="The Joshua Tree").first().id,
        rating=5,
        comment="An exceptional album by U2!",
    )

    californication_review = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        reviewable_id=Album.query.filter_by(title="Californication").first().id,
        rating=4,
        comment="A great album with a unique sound!",
    )

    db.session.add_all(
        [
            abbey_road_review,
            dark_side_of_the_moon_review,
            night_at_the_opera_review,
            nevermind_review,
            master_of_puppets_review,
            let_it_bleed_review,
            ok_computer_review,
            led_zeppelin_iv_review,
            london_calling_review,
            the_joshua_tree_review,
            californication_review,
        ]
    )
    db.session.commit()


def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()