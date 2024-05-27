from app.models import db, Album, User, environment, SCHEMA
from datetime import date
from sqlalchemy.sql import text


def seed_albums():
    abbey_road = Album(
        user_id=User.query.filter_by(name="The Beatles").first().id,
        title="Abbey Road",
        release_date=date(1969, 9, 26),
        description="One of the best albums by The Beatles.",
        image_url="https://upload.wikimedia.org/wikipedia/en/4/42/Beatles_-_Abbey_Road.jpg",
    )

    sgt_peppers = Album(
        user_id=User.query.filter_by(name="The Beatles").first().id,
        title="Sgt. Pepper's",
        release_date=date(1967, 6, 1),
        description="A landmark album by The Beatles.",
        image_url="https://upload.wikimedia.org/wikipedia/en/5/50/Sgt._Pepper%27s_Lonely_Hearts_Club_Band.jpg",
    )

    the_dark_side_of_the_moon = Album(
        user_id=User.query.filter_by(name="Pink Floyd").first().id,
        title="The Dark Side of the Moon",
        release_date=date(1973, 3, 1),
        description="A landmark album by Pink Floyd.",
        image_url="https://upload.wikimedia.org/wikipedia/en/3/3b/Dark_Side_of_the_Moon.png",
    )

    the_wall = Album(
        user_id=User.query.filter_by(name="Pink Floyd").first().id,
        title="The Wall",
        release_date=date(1979, 11, 30),
        description="A rock opera album by Pink Floyd.",
        image_url="https://i.scdn.co/image/ab67616d0000b2735d48e2f56d691f9a4e4b0bdf",
    )

    a_night_at_the_opera = Album(
        user_id=User.query.filter_by(name="Queen").first().id,
        title="A Night at the Opera",
        release_date=date(1975, 11, 21),
        description="One of Queen's most celebrated albums.",
        image_url="https://upload.wikimedia.org/wikipedia/en/4/4d/Queen_A_Night_At_The_Opera.png",
    )

    news_of_the_world = Album(
        user_id=User.query.filter_by(name="Queen").first().id,
        title="News of the World",
        release_date=date(1977, 10, 28),
        description="Another classic album by Queen.",
        image_url="https://upload.wikimedia.org/wikipedia/en/e/ea/Queen_News_Of_The_World.png",
    )

    nevermind = Album(
        user_id=User.query.filter_by(name="Nirvana").first().id,
        title="Nevermind",
        release_date=date(1991, 9, 24),
        description="The album that brought grunge to the mainstream.",
        image_url="https://upload.wikimedia.org/wikipedia/en/b/b7/NirvanaNevermindalbumcover.jpg",
    )

    in_utero = Album(
        user_id=User.query.filter_by(name="Nirvana").first().id,
        title="In Utero",
        release_date=date(1993, 9, 21),
        description="The third and final studio album by Nirvana.",
        image_url="https://upload.wikimedia.org/wikipedia/en/e/e5/In_Utero_%28Nirvana%29_album_cover.jpg",
    )

    master_of_puppets = Album(
        user_id=User.query.filter_by(name="Metallica").first().id,
        title="Master of Puppets",
        release_date=date(1986, 3, 3),
        description="One of Metallica's most influential albums.",
        image_url="https://upload.wikimedia.org/wikipedia/en/b/b2/Metallica_-_Master_of_Puppets_cover.jpg",
    )

    ride_the_lightning = Album(
        user_id=User.query.filter_by(name="Metallica").first().id,
        title="Ride the Lightning",
        release_date=date(1984, 7, 27),
        description="The second studio album by Metallica.",
        image_url="https://upload.wikimedia.org/wikipedia/en/f/f4/Ridetl.png",
    )

    let_it_bleed = Album(
        user_id=User.query.filter_by(name="The Rolling Stones").first().id,
        title="Let It Bleed",
        release_date=date(1969, 12, 5),
        description="A classic album by The Rolling Stones.",
        image_url="https://m.media-amazon.com/images/I/81Ut0SKKVhL._UF1000,1000_QL80_.jpg",
    )

    sticky_fingers = Album(
        user_id=User.query.filter_by(name="The Rolling Stones").first().id,
        title="Sticky Fingers",
        release_date=date(1971, 4, 23),
        description="Another classic album by The Rolling Stones.",
        image_url="https://m.media-amazon.com/images/I/813SPFc3RuL._UF1000,1000_QL80_.jpg",
    )

    ok_computer = Album(
        user_id=User.query.filter_by(name="Radiohead").first().id,
        title="OK Computer",
        release_date=date(1997, 5, 21),
        description="A critically acclaimed album by Radiohead.",
        image_url="https://upload.wikimedia.org/wikipedia/en/b/ba/Radioheadokcomputer.png",
    )

    kid_a = Album(
        user_id=User.query.filter_by(name="Radiohead").first().id,
        title="Kid A",
        release_date=date(2000, 10, 2),
        description="Another highly acclaimed album by Radiohead.",
        image_url="https://m.media-amazon.com/images/I/71I5kJS+dsL._UF1000,1000_QL80_.jpg",
    )

    led_zeppelin_iv = Album(
        user_id=User.query.filter_by(name="Led Zeppelin").first().id,
        title="Led Zeppelin IV",
        release_date=date(1971, 11, 8),
        description="Featuring the iconic 'Stairway to Heaven'.",
        image_url="https://upload.wikimedia.org/wikipedia/en/2/26/Led_Zeppelin_-_Led_Zeppelin_IV.jpg",
    )

    houses_of_the_holy = Album(
        user_id=User.query.filter_by(name="Led Zeppelin").first().id,
        title="Houses of the Holy",
        release_date=date(1973, 3, 28),
        description="Another classic album by Led Zeppelin.",
        image_url="https://m.media-amazon.com/images/I/81M17z91GwL._UF1000,1000_QL80_.jpg",
    )

    london_calling = Album(
        user_id=User.query.filter_by(name="The Clash").first().id,
        title="London Calling",
        release_date=date(1979, 12, 14),
        description="A double album by The Clash that became a classic.",
        image_url="https://upload.wikimedia.org/wikipedia/en/0/00/TheClashLondonCallingalbumcover.jpg",
    )

    combat_rock = Album(
        user_id=User.query.filter_by(name="The Clash").first().id,
        title="Combat Rock",
        release_date=date(1982, 5, 14),
        description="A commercially successful album by The Clash.",
        image_url="https://upload.wikimedia.org/wikipedia/en/0/07/The_Clash_-_Combat_Rock.jpg",
    )

    the_joshua_tree = Album(
        user_id=User.query.filter_by(name="U2").first().id,
        title="The Joshua Tree",
        release_date=date(1987, 3, 9),
        description="The album that brought U2 international fame.",
        image_url="https://upload.wikimedia.org/wikipedia/en/6/6b/The_Joshua_Tree.png",
    )

    achtung_baby = Album(
        user_id=User.query.filter_by(name="U2").first().id,
        title="Achtung Baby",
        release_date=date(1991, 11, 18),
        description="Another acclaimed album by U2.",
        image_url="https://m.media-amazon.com/images/I/71yC+dM15gL._UF1000,1000_QL80_.jpg",
    )

    californication = Album(
        user_id=User.query.filter_by(name="Red Hot Chili Peppers").first().id,
        title="Californication",
        release_date=date(1999, 6, 8),
        description="One of the band's most successful albums.",
        image_url="https://upload.wikimedia.org/wikipedia/en/d/df/RedHotChiliPeppersCalifornication.jpg",
    )

    by_the_way = Album(
        user_id=User.query.filter_by(name="Red Hot Chili Peppers").first().id,
        title="By the Way",
        release_date=date(2002, 7, 9),
        description="Another successful album by the Red Hot Chili Peppers.",
        image_url="https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Rhcp9.jpg/220px-Rhcp9.jpg",
    )

    fearless = Album(
        user_id=User.query.filter_by(name="Taylor Swift").first().id,
        title="Fearless",
        release_date=date(2008, 11, 11),
        description="Taylor Swift's second studio album, featuring hits like 'Love Story'.",
        image_url="https://upload.wikimedia.org/wikipedia/en/8/86/Taylor_Swift_-_Fearless.png",
    )

    ninteeneightynine = Album(
        user_id=User.query.filter_by(name="Taylor Swift").first().id,
        title="1989",
        release_date=date(2014, 10, 27),
        description="Taylor Swift's fifth studio album, a pop transformation.",
        image_url="https://i.scdn.co/image/ab67616d0000b273904445d70d04eb24d6bb79ac",
    )

    to_pimp_a_butterfly = Album(
        user_id=User.query.filter_by(name="Kendrick Lamar").first().id,
        title="To Pimp a Butterfly",
        release_date=date(2015, 3, 15),
        description="A critically acclaimed album by Kendrick Lamar.",
        image_url="https://upload.wikimedia.org/wikipedia/en/f/f6/Kendrick_Lamar_-_To_Pimp_a_Butterfly.png",
    )

    good_kid_maad_city = Album(
        user_id=User.query.filter_by(name="Kendrick Lamar").first().id,
        title="Good Kid, M.A.A.D City",
        release_date=date(2012, 10, 22),
        description="A major label debut album by Kendrick Lamar.",
        image_url="https://i.scdn.co/image/ab67616d0000b273d58e537cea05c2156792c53d",
    )

    twentyone = Album(
        user_id=User.query.filter_by(name="Adele").first().id,
        title="21",
        release_date=date(2011, 1, 24),
        description="Adele's second studio album featuring hit singles 'Rolling in the Deep' and 'Someone Like You'.",
        image_url="https://upload.wikimedia.org/wikipedia/en/1/1b/Adele_-_21.png",
    )

    twentyfive = Album(
        user_id=User.query.filter_by(name="Adele").first().id,
        title="25",
        release_date=date(2015, 11, 20),
        description="Adele's third studio album featuring the hit single 'Hello'.",
        image_url="https://upload.wikimedia.org/wikipedia/en/9/96/Adele_-_25_%28Official_Album_Cover%29.png",
    )

    lemonade = Album(
        user_id=User.query.filter_by(name="Beyoncé").first().id,
        title="Lemonade",
        release_date=date(2016, 4, 23),
        description="A visual album by Beyoncé that received widespread critical acclaim.",
        image_url="https://upload.wikimedia.org/wikipedia/en/5/53/Beyonce_-_Lemonade_%28Official_Album_Cover%29.png",
    )

    beyonce_album = Album(
        user_id=User.query.filter_by(name="Beyoncé").first().id,
        title="Beyoncé",
        release_date=date(2013, 12, 13),
        description="A self-titled visual album by Beyoncé.",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Beyonc%C3%A9_-_Beyonc%C3%A9.svg/1200px-Beyonc%C3%A9_-_Beyonc%C3%A9.svg.png",
    )

    divide = Album(
        user_id=User.query.filter_by(name="Ed Sheeran").first().id,
        title="÷ (Divide)",
        release_date=date(2017, 3, 3),
        description="Ed Sheeran's third studio album featuring hits like 'Shape of You' and 'Castle on the Hill'.",
        image_url="https://upload.wikimedia.org/wikipedia/en/4/45/Divide_cover.png",
    )

    multiply = Album(
        user_id=User.query.filter_by(name="Ed Sheeran").first().id,
        title="× (Multiply)",
        release_date=date(2014, 6, 20),
        description="Ed Sheeran's second studio album featuring hits like 'Sing' and 'Thinking Out Loud'.",
        image_url="https://upload.wikimedia.org/wikipedia/en/a/ad/X_cover.png",
    )

    twentyfourkmagic = Album(
        user_id=User.query.filter_by(name="Bruno Mars").first().id,
        title="24K Magic",
        release_date=date(2016, 11, 18),
        description="Bruno Mars' third studio album featuring the title track '24K Magic'.",
        image_url="https://upload.wikimedia.org/wikipedia/en/2/2b/Bruno_Mars_-_24K_Magic_%28Official_Album_Cover%29.png",
    )

    doo_wops_and_hooligans = Album(
        user_id=User.query.filter_by(name="Bruno Mars").first().id,
        title="Doo-Wops & Hooligans",
        release_date=date(2010, 10, 4),
        description="Bruno Mars' debut studio album.",
        image_url="https://m.media-amazon.com/images/I/71AJLmFQp+L._UF1000,1000_QL80_.jpg",
    )

    when_we_all_fall_asleep = Album(
        user_id=User.query.filter_by(name="Billie Eilish").first().id,
        title="When We All Fall Asleep",
        release_date=date(2019, 3, 29),
        description="Billie Eilish's debut studio album featuring the hit single 'Bad Guy'.",
        image_url="https://upload.wikimedia.org/wikipedia/en/3/38/When_We_All_Fall_Asleep%2C_Where_Do_We_Go%3F.png",
    )

    dont_smile_at_me = Album(
        user_id=User.query.filter_by(name="Billie Eilish").first().id,
        title="Don't Smile at Me",
        release_date=date(2017, 8, 11),
        description="Billie Eilish's debut extended play.",
        image_url="https://upload.wikimedia.org/wikipedia/en/2/2f/Billie_Eilish_-_Don%27t_Smile_at_Me.png",
    )

    thank_u_next = Album(
        user_id=User.query.filter_by(name="Ariana Grande").first().id,
        title="Thank U, Next",
        release_date=date(2019, 2, 8),
        description="Ariana Grande's fifth studio album featuring the title track 'Thank U, Next'.",
        image_url="https://upload.wikimedia.org/wikipedia/en/d/dd/Thank_U%2C_Next_album_cover.png",
    )

    sweetener = Album(
        user_id=User.query.filter_by(name="Ariana Grande").first().id,
        title="Sweetener",
        release_date=date(2018, 8, 17),
        description="Ariana Grande's fourth studio album.",
        image_url="https://m.media-amazon.com/images/I/81FH-xfuK5L._UF1000,1000_QL80_.jpg",
    )

    beerbongs_and_bentleys = Album(
        user_id=User.query.filter_by(name="Post Malone").first().id,
        title="Beerbongs & Bentleys",
        release_date=date(2018, 4, 27),
        description="Post Malone's second studio album featuring hit singles 'Rockstar' and 'Psycho'.",
        image_url="https://archive.org/services/img/post-malone-beersongs-and-bentleys/full/pct:300/0/default.jpg",
    )

    hollywoods_bleeding = Album(
        user_id=User.query.filter_by(name="Post Malone").first().id,
        title="Hollywood's Bleeding",
        release_date=date(2019, 9, 6),
        description="Post Malone's third studio album.",
        image_url="https://upload.wikimedia.org/wikipedia/en/5/58/Post_Malone_-_Hollywood%27s_Bleeding.png",
    )

    scorpion = Album(
        user_id=User.query.filter_by(name="Drake").first().id,
        title="Scorpion",
        release_date=date(2018, 6, 29),
        description="Drake's fifth studio album featuring the hit single 'In My Feelings'.",
        image_url="https://upload.wikimedia.org/wikipedia/en/9/90/Scorpion_by_Drake.jpg",
    )

    views = Album(
        user_id=User.query.filter_by(name="Drake").first().id,
        title="Views",
        release_date=date(2016, 4, 29),
        description="Another successful album by Drake.",
        image_url="https://upload.wikimedia.org/wikipedia/en/a/af/Drake_-_Views_cover.jpg",
    )

    db.session.add_all(
        [
            abbey_road,
            sgt_peppers,
            the_dark_side_of_the_moon,
            the_wall,
            a_night_at_the_opera,
            news_of_the_world,
            nevermind,
            in_utero,
            master_of_puppets,
            ride_the_lightning,
            let_it_bleed,
            sticky_fingers,
            ok_computer,
            kid_a,
            led_zeppelin_iv,
            houses_of_the_holy,
            london_calling,
            combat_rock,
            the_joshua_tree,
            achtung_baby,
            californication,
            by_the_way,
            fearless,
            ninteeneightynine,
            to_pimp_a_butterfly,
            good_kid_maad_city,
            twentyone,
            twentyfive,
            lemonade,
            beyonce_album,
            divide,
            multiply,
            twentyfourkmagic,
            doo_wops_and_hooligans,
            when_we_all_fall_asleep,
            dont_smile_at_me,
            thank_u_next,
            sweetener,
            beerbongs_and_bentleys,
            hollywoods_bleeding,
            scorpion,
            views,
        ]
    )
    db.session.commit()


def undo_albums():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.albums RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM albums"))

    db.session.commit()
