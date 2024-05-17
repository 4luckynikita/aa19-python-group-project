# from models import (
#     db,
#     Musician,
#     Album,
#     Song,
#     Review,
#     User,
#     FollowedMusician,
#     Comment,
# )


# def seed_data():
#     with app.app_context():

#         ###############! USERS ###############
#         users = [
#             {
#                 "username": "johndoe",
#                 "email": "john@doe.com",
#                 "password_hash": "hashed_password",
#                 "first_name": "John",
#                 "last_name": "Doe",
#                 "bio": "Rocker and Roller",
#                 "image_url": "http://example.com/images/johndoe.jpg",
#             }
#         ]

#         for user_data in users:
#             user = User(**user_data)
#             db.session.add(user)
#         db.session.commit()

#         ###############! MUSICIANS ###############
#         musicians = [
#             {
#                 "name": "The Beatles",
#                 "email": "kpop@music.com",
#                 "password_hash": "hashed_password",
#                 "genre": "Classic Rock",
#                 "description": "Legendary rock band.",
#                 "image_url": "http://example.com/images/thebeatles.jpg",
#             }
#         ]

#         for musician_data in musicians:
#             musician = Musician(**musician_data)
#             db.session.add(musician)
#         db.session.commit()

#         ###############! ALBUMS ###############
#         albums = [
#             {
#                 "musician_id": Musician.query.filter_by(name="The Beatles").first().id,
#                 "title": "Abbey Road",
#                 "release_date": date(1969, 9, 26),
#                 "description": "One of the best albums by The Beatles.",
#                 "image_url": "http://example.com/images/abbeyroad.jpg",
#             }
#         ]

#         for album_data in albums:
#             album = Album(**album_data)
#             db.session.add(album)
#         db.session.commit()

#         ###############! SONGS ###############
#         songs = [
#             {
#                 "album_id": Album.query.filter_by(title="Abbey Road").first().id,
#                 "title": "Come Together",
#                 "duration": 259,
#                 "image_url": "http://example.com/images/cometogether.jpg",
#             }
#         ]

#         for song_data in songs:
#             song = Song(**song_data)
#             db.session.add(song)
#         db.session.commit()

#         ###############! REVIEWS ###############
#         reviews = [
#             {
#                 "user_id": User.query.filter_by(username="johndoe").first().id,
#                 "reviewable_type": "Album",
#                 "reviewable_id": Album.query.filter_by(title="Abbey Road").first().id,
#                 "rating": 5,
#                 "comment": "Amazing album!",
#             }
#         ]

#         for review_data in reviews:
#             review = Review(**review_data)
#             db.session.add(review)
#         db.session.commit()

#         ###############! FOLLOWED MUSICIANS ###############
#         follows = [
#             {
#                 "user_id": User.query.filter_by(username="johndoe").first().id,
#                 "musician_id": Musician.query.filter_by(name="The Beatles").first().id,
#             }
#         ]

#         for follow_data in follows:
#             follow = FollowedMusician(**follow_data)
#             db.session.add(follow)
#         db.session.commit()

#         ###############! COMMENTS ###############
#         comments = [
#             {
#                 "user_id": User.query.filter_by(username="johndoe").first().id,
#                 "review_id": Review.query.filter_by(comment="Amazing album!")
#                 .first()
#                 .id,
#                 "comment": "I totally agree!",
#             }
#         ]

#         for comment_data in comments:
#             comment = Comment(**comment_data)
#             db.session.add(comment)
#         db.session.commit()


# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#         seed_data()
