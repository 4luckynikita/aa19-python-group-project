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
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/SmileyFace.png",
    )
    marnie = User(
        username="marnie",
        is_musician=False,
        email="marnie@aa.io",
        password="password",
        first_name="Marnie",
        last_name="Marston",
        description="Music 4 Lyfe!",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/SmileyFace.png",
    )
    bobbie = User(
        username="bobbie",
        is_musician=False,
        email="bobbie@aa.io",
        password="password",
        first_name="Bobbie",
        last_name="Smith",
        description="My favorite genre is METALLICA!",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/SmileyFace.png",
    )
    nikita = User(
        username="nikita",
        is_musician=False,
        email="nikita@aa.io",
        password="password",
        first_name="Nikita",
        last_name="Kastyshyn",
        description="I'm down with whatever you got!",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/SmileyFace.png",
    )
    erik = User(
        username="erik",
        is_musician=False,
        email="erik@aa.io",
        password="password",
        first_name="Erik",
        last_name="Hervall",
        description="Rocker and Roller!!!",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/SmileyFace.png",
    )
    cece = User(
        username="cece",
        is_musician=False,
        email="cece@aa.io",
        password="password",
        first_name="Cece",
        last_name="Potakey",
        description="Let's hear some KPOP!",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/SmileyFace.png",
    )
    the_beatles = User(
        name="The Beatles",
        is_musician=True,
        email="thebeatles@music.com",
        password="password",
        genre="Classic Rock",
        description="Legendary rock band.",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/The_Beatles_members_at_New_York_City_in_1964.jpg/800px-The_Beatles_members_at_New_York_City_in_1964.jpg",
    )

    pink_floyd = User(
        name="Pink Floyd",
        is_musician=True,
        email="pinkfloyd@music.com",
        password="password",
        genre="Progressive Rock",
        description="Pioneers of psychedelic music.",
        image_url="https://img.apmcdn.org/0f423154792e8a69e98ba69cb9718417e6cb5aa6/square/ed84b0-20180105-pink-floyd-with-syd-barrett.jpg",
    )

    queen = User(
        name="Queen",
        is_musician=True,
        email="queen@music.com",
        password="password",
        genre="Rock",
        description="Iconic British rock band.",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Queen_%E2%80%93_montagem_%E2%80%93_new.png/220px-Queen_%E2%80%93_montagem_%E2%80%93_new.png",
    )

    nirvana = User(
        name="Nirvana",
        is_musician=True,
        email="nirvana@music.com",
        password="password",
        genre="Grunge",
        description="Key band in the Seattle grunge scene.",
        image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCtkrCP0PCSudDwLkkjXDeuUoDOIQV_qqjxrbVGij_9A&s",
    )

    metallica = User(
        name="Metallica",
        is_musician=True,
        email="metallica@music.com",
        password="password",
        genre="Heavy Metal",
        description="One of the most influential heavy metal bands.",
        image_url="https://upload.wikimedia.org/wikipedia/en/7/7b/Metallica_-_The_%245.98_E.P.-Garage_Days_Re-Revisited_cover.jpg",
    )

    the_rolling_stones = User(
        name="The Rolling Stones",
        is_musician=True,
        email="therollingstones@music.com",
        password="password",
        genre="Rock",
        description="Long-standing British rock band.",
        image_url="https://lh3.googleusercontent.com/VayRnJfZC6MAdZZEkGa_O8Zegu9qoyhlwcYA73fFqRAr5C8no_DLdMqGY3LXtdDQFX91V4GMWrtnjmk=w544-h544-p-l90-rj",
    )

    radiohead = User(
        name="Radiohead",
        is_musician=True,
        email="radiohead@music.com",
        password="password",
        genre="Alternative Rock",
        description="Known for their experimental approach.",
        image_url="https://i.guim.co.uk/img/media/c174daa9a205ff9ad68c155bad9003fd946bbf85/0_178_2048_1228/master/2048.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=d0ec33bb206217ddc78f8701fe6a32c4",
    )

    led_zeppelin = User(
        name="Led Zeppelin",
        is_musician=True,
        email="ledzeppelin@music.com",
        password="password",
        genre="Hard Rock",
        description="Pioneers of hard rock and heavy metal.",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/49/LedZeppelinmontage.jpg",
    )

    the_clash = User(
        name="The Clash",
        is_musician=True,
        email="theclash@music.com",
        password="password",
        genre="Punk Rock",
        description="Influential punk rock band.",
        image_url="https://i.discogs.com/1gn6P_tkUM7E75yrF4lH7aYNfYIaDmu6xJ15l6xpp14/rs:fit/g:sm/q:90/h:531/w:531/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTI5ODkw/LTE3MDY2NjIzOTQt/MTA2Mi5qcGVn.jpeg",
    )

    u2 = User(
        name="U2",
        is_musician=True,
        email="u2@music.com",
        password="password",
        genre="Rock",
        description="Irish rock band known for their anthemic sound.",
        image_url="https://artist1.cdn107.com/0be/0bedc3953dbb5af368a6d186f0c4fe77_xl.jpg",
    )

    red_hot_chili_peppers = User(
        name="Red Hot Chili Peppers",
        is_musician=True,
        email="rhcp@music.com",
        password="password",
        genre="Funk Rock",
        description="Band known for their fusion of rock, funk, and punk.",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Red_Hot_Chili_Peppers_logo.svg/200px-Red_Hot_Chili_Peppers_logo.svg.png",
    )
    
    demo_musician = User(
        name="Demo Musician",
        is_musician=True,
        email="demo@musician.com",
        password="password",
        genre="Rock",
        description="I am a demo musician",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/SmileyFace.png",
    )

    taylor_swift = User(
        name="Taylor Swift",
        is_musician=True,
        email="taylorswift@music.com",
        password="password",
        genre="Pop",
        description="Award-winning pop artist and songwriter.",
        image_url="https://media.newyorker.com/photos/647a206eb7642d9e0771ebe6/1:1/w_1652,h_1652,c_limit/Foggatt-Taylor-Swift-Eras.jpg",
    )

    kendrick_lamar = User(
        name="Kendrick Lamar",
        is_musician=True,
        email="kendricklamar@music.com",
        password="password",
        genre="Hip Hop",
        description="Renowned rapper and lyricist.",
        image_url="https://yt3.googleusercontent.com/V4FqOieQ9y9dnErXPUZNWl1hyLafxIK7F55n5M8LVhPBmEou8kAbNuMlUZx23DoJHvH1sWG56No=s900-c-k-c0x00ffffff-no-rj",
    )

    adele = User(
        name="Adele",
        is_musician=True,
        email="adele@music.com",
        password="password",
        genre="Soul",
        description="Soulful singer with powerful vocals.",
        image_url="https://hips.hearstapps.com/hmg-prod/images/adele-makeup-1632125637.png?crop=0.9803921568627451xw:1xh;center,top&resize=640:*",
    )

    beyonce = User(
        name="Beyoncé",
        is_musician=True,
        email="beyonce@music.com",
        password="password",
        genre="R&B",
        description="Iconic R&B artist and performer.",
        image_url="https://media.glamour.com/photos/66268d8a8aefb9b182da343a/1:1/w_354%2Cc_limit/Beyonce%25CC%2581%2520Just%2520Dropped%2520Her%2520Hair%2520Care%2520Routine%2520and%2520Shut%2520Down%2520Wig%2520%2520%25E2%2580%2598Misconceptions%25E2%2580%2599.jpg",
    )

    ed_sheeran = User(
        name="Ed Sheeran",
        is_musician=True,
        email="edsheeran@music.com",
        password="password",
        genre="Pop",
        description="Popular singer-songwriter and musician.",
        image_url="https://i.iheart.com/v3/catalog/artist/396790?ops=fit(720%2C720)",
    )

    bruno_mars = User(
        name="Bruno Mars",
        is_musician=True,
        email="brunomars@music.com",
        password="password",
        genre="Pop",
        description="Versatile singer known for his catchy hits.",
        image_url="https://i.scdn.co/image/ab6761610000e5ebc36dd9eb55fb0db4911f25dd",
    )

    billie_eilish = User(
        name="Billie Eilish",
        is_musician=True,
        email="billieeilish@music.com",
        password="password",
        genre="Electropop",
        description="Innovative electropop artist.",
        image_url="https://i.guim.co.uk/img/media/67944850a1b5ebd6a0fba9e3528d448ebe360c60/359_0_2469_1482/master/2469.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=03f3e07a7f367f36a738f1ad8132b3bb",
    )

    ariana_grande = User(
        name="Ariana Grande",
        is_musician=True,
        email="arianagrande@music.com",
        password="password",
        genre="Pop",
        description="Pop sensation with a powerful voice.",
        image_url="https://d.newsweek.com/en/full/2356120/ariana-grande-2018.png?w=1600&h=1600&q=88&f=ca74f80d593339aa3e3f5f9cd7ddb901",
    )

    post_malone = User(
        name="Post Malone",
        is_musician=True,
        email="postmalone@music.com",
        password="password",
        genre="Hip Hop",
        description="Hip hop artist known for his unique style.",
        image_url="https://m.media-amazon.com/images/M/MV5BODg4N2I0NmEtNTIyMS00MzVjLThjYzgtODAwMzcwYThkMTVkXkEyXkFqcGdeQXVyMTI2Nzk3NzI4._V1_FMjpg_UX1000_.jpg",
    )

    drake = User(
        name="Drake",
        is_musician=True,
        email="drake@music.com",
        password="password",
        genre="Hip Hop",
        description="Top-selling rapper and entertainer.",
        image_url="https://i.guim.co.uk/img/media/26bd84ad34111920d6eebf52de3ee1b098b4a3e6/0_47_1472_883/master/1472.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=75dfdb3554b9610d5baacb8d7e44b74a",
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
            taylor_swift,
            kendrick_lamar,
            adele,
            beyonce,
            ed_sheeran,
            bruno_mars,
            billie_eilish,
            ariana_grande,
            post_malone,
            drake,
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
