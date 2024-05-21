from app.models import db, Review, User, Album, environment, SCHEMA
from sqlalchemy.sql import text


def seed_reviews():
    abbey_road_review = Review(
        user_id=User.query.filter_by(username="demo").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Amazing album!",
        album_id=1
    )

    dark_side_of_the_moon_review = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A masterpiece!",
        album_id=2
    )

    night_at_the_opera_review = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="An incredible work by Queen!",
        album_id=3
    )

    nevermind_review = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A defining album of its generation!",
        album_id=4
    )

    master_of_puppets_review = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="An iconic metal album!",
        album_id=5
    )

    let_it_bleed_review = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="A classic Rolling Stones album!",
        album_id=6
    )

    ok_computer_review = Review(
        user_id=User.query.filter_by(username="demo").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A revolutionary album by Radiohead!",
        album_id=7
    )

    led_zeppelin_iv_review = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A timeless classic!",
        album_id=8
    )

    london_calling_review = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="A must-listen punk album!",
        album_id=9
    )

    the_joshua_tree_review = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="An exceptional album by U2!",
        album_id=10
    )

    californication_review = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=4,
        comment="A great album with a unique sound!",
        album_id=11
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
