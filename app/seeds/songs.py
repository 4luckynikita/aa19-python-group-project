from app.models import db, Song, Album, environment, SCHEMA
from sqlalchemy.sql import text


def seed_songs():
    songs = [
        # Abbey Road
        Song(album_id=Album.query.filter_by(title="Abbey Road").first().id, title="Come Together", duration=259),
        Song(album_id=Album.query.filter_by(title="Abbey Road").first().id, title="Something", duration=182),
        Song(album_id=Album.query.filter_by(title="Abbey Road").first().id, title="Here Comes the Sun", duration=185),

        # Sgt. Pepper's
        Song(album_id=Album.query.filter_by(title="Sgt. Pepper's").first().id, title="Lucy in the Sky with Diamonds", duration=207),
        Song(album_id=Album.query.filter_by(title="Sgt. Pepper's").first().id, title="A Day in the Life", duration=337),
        Song(album_id=Album.query.filter_by(title="Sgt. Pepper's").first().id, title="With a Little Help from My Friends", duration=165),

        # The Dark Side of the Moon
        Song(album_id=Album.query.filter_by(title="The Dark Side of the Moon").first().id, title="Money", duration=382),
        Song(album_id=Album.query.filter_by(title="The Dark Side of the Moon").first().id, title="Time", duration=414),
        Song(album_id=Album.query.filter_by(title="The Dark Side of the Moon").first().id, title="Us and Them", duration=462),

        # The Wall
        Song(album_id=Album.query.filter_by(title="The Wall").first().id, title="Another Brick in the Wall, Part 2", duration=240),
        Song(album_id=Album.query.filter_by(title="The Wall").first().id, title="Comfortably Numb", duration=384),
        Song(album_id=Album.query.filter_by(title="The Wall").first().id, title="Hey You", duration=279),

        # A Night at the Opera
        Song(album_id=Album.query.filter_by(title="A Night at the Opera").first().id, title="Bohemian Rhapsody", duration=354),
        Song(album_id=Album.query.filter_by(title="A Night at the Opera").first().id, title="You're My Best Friend", duration=168),
        Song(album_id=Album.query.filter_by(title="A Night at the Opera").first().id, title="Love of My Life", duration=209),

        # News of the World
        Song(album_id=Album.query.filter_by(title="News of the World").first().id, title="We Will Rock You", duration=121),
        Song(album_id=Album.query.filter_by(title="News of the World").first().id, title="We Are the Champions", duration=179),
        Song(album_id=Album.query.filter_by(title="News of the World").first().id, title="Spread Your Wings", duration=246),

        # Nevermind
        Song(album_id=Album.query.filter_by(title="Nevermind").first().id, title="Smells Like Teen Spirit", duration=301),
        Song(album_id=Album.query.filter_by(title="Nevermind").first().id, title="In Bloom", duration=255),
        Song(album_id=Album.query.filter_by(title="Nevermind").first().id, title="Come as You Are", duration=218),

        # In Utero
        Song(album_id=Album.query.filter_by(title="In Utero").first().id, title="Heart-Shaped Box", duration=284),
        Song(album_id=Album.query.filter_by(title="In Utero").first().id, title="Rape Me", duration=153),
        Song(album_id=Album.query.filter_by(title="In Utero").first().id, title="All Apologies", duration=230),

        # Master of Puppets
        Song(album_id=Album.query.filter_by(title="Master of Puppets").first().id, title="Master of Puppets", duration=515),
        Song(album_id=Album.query.filter_by(title="Master of Puppets").first().id, title="Battery", duration=312),
        Song(album_id=Album.query.filter_by(title="Master of Puppets").first().id, title="Welcome Home (Sanitarium)", duration=388),

        # Ride the Lightning
        Song(album_id=Album.query.filter_by(title="Ride the Lightning").first().id, title="Fight Fire with Fire", duration=283),
        Song(album_id=Album.query.filter_by(title="Ride the Lightning").first().id, title="Ride the Lightning", duration=396),
        Song(album_id=Album.query.filter_by(title="Ride the Lightning").first().id, title="Fade to Black", duration=418),

        # Let It Bleed
        Song(album_id=Album.query.filter_by(title="Let It Bleed").first().id, title="Gimme Shelter", duration=272),
        Song(album_id=Album.query.filter_by(title="Let It Bleed").first().id, title="You Can't Always Get What You Want", duration=432),
        Song(album_id=Album.query.filter_by(title="Let It Bleed").first().id, title="Midnight Rambler", duration=413),

        # Sticky Fingers
        Song(album_id=Album.query.filter_by(title="Sticky Fingers").first().id, title="Brown Sugar", duration=223),
        Song(album_id=Album.query.filter_by(title="Sticky Fingers").first().id, title="Wild Horses", duration=325),
        Song(album_id=Album.query.filter_by(title="Sticky Fingers").first().id, title="Can't You Hear Me Knocking", duration=437),

        # OK Computer
        Song(album_id=Album.query.filter_by(title="OK Computer").first().id, title="Paranoid Android", duration=387),
        Song(album_id=Album.query.filter_by(title="OK Computer").first().id, title="Karma Police", duration=263),
        Song(album_id=Album.query.filter_by(title="OK Computer").first().id, title="No Surprises", duration=229),

        # Kid A
        Song(album_id=Album.query.filter_by(title="Kid A").first().id, title="Everything in Its Right Place", duration=255),
        Song(album_id=Album.query.filter_by(title="Kid A").first().id, title="Kid A", duration=274),
        Song(album_id=Album.query.filter_by(title="Kid A").first().id, title="Idioteque", duration=312),

        # Led Zeppelin IV
        Song(album_id=Album.query.filter_by(title="Led Zeppelin IV").first().id, title="Stairway to Heaven", duration=482),
        Song(album_id=Album.query.filter_by(title="Led Zeppelin IV").first().id, title="Black Dog", duration=296),
        Song(album_id=Album.query.filter_by(title="Led Zeppelin IV").first().id, title="Rock and Roll", duration=223),

        # Houses of the Holy
        Song(album_id=Album.query.filter_by(title="Houses of the Holy").first().id, title="The Song Remains the Same", duration=329),
        Song(album_id=Album.query.filter_by(title="Houses of the Holy").first().id, title="No Quarter", duration=417),
        Song(album_id=Album.query.filter_by(title="Houses of the Holy").first().id, title="Over the Hills and Far Away", duration=284),

        # London Calling
        Song(album_id=Album.query.filter_by(title="London Calling").first().id, title="London Calling", duration=202),
        Song(album_id=Album.query.filter_by(title="London Calling").first().id, title="Brand New Cadillac", duration=129),
        Song(album_id=Album.query.filter_by(title="London Calling").first().id, title="Jimmy Jazz", duration=192),

        # Combat Rock
        Song(album_id=Album.query.filter_by(title="Combat Rock").first().id, title="Should I Stay or Should I Go", duration=215),
        Song(album_id=Album.query.filter_by(title="Combat Rock").first().id, title="Rock the Casbah", duration=228),
        Song(album_id=Album.query.filter_by(title="Combat Rock").first().id, title="Straight to Hell", duration=344),

        # The Joshua Tree
        Song(album_id=Album.query.filter_by(title="The Joshua Tree").first().id, title="With or Without You", duration=296),
        Song(album_id=Album.query.filter_by(title="The Joshua Tree").first().id, title="Where the Streets Have No Name", duration=336),
        Song(album_id=Album.query.filter_by(title="The Joshua Tree").first().id, title="I Still Haven't Found What I'm Looking For", duration=277),

        # Achtung Baby
        Song(album_id=Album.query.filter_by(title="Achtung Baby").first().id, title="One", duration=272),
        Song(album_id=Album.query.filter_by(title="Achtung Baby").first().id, title="Mysterious Ways", duration=254),
        Song(album_id=Album.query.filter_by(title="Achtung Baby").first().id, title="The Fly", duration=277),

        # Californication
        Song(album_id=Album.query.filter_by(title="Californication").first().id, title="Californication", duration=329),
        Song(album_id=Album.query.filter_by(title="Californication").first().id, title="Scar Tissue", duration=216),
        Song(album_id=Album.query.filter_by(title="Californication").first().id, title="Otherside", duration=255),

        # By the Way
        Song(album_id=Album.query.filter_by(title="By the Way").first().id, title="By the Way", duration=213),
        Song(album_id=Album.query.filter_by(title="By the Way").first().id, title="Can't Stop", duration=269),
        Song(album_id=Album.query.filter_by(title="By the Way").first().id, title="The Zephyr Song", duration=231),

        # Fearless
        Song(album_id=Album.query.filter_by(title="Fearless").first().id, title="Love Story", duration=231),
        Song(album_id=Album.query.filter_by(title="Fearless").first().id, title="You Belong with Me", duration=230),
        Song(album_id=Album.query.filter_by(title="Fearless").first().id, title="White Horse", duration=237),

        # 1989
        Song(album_id=Album.query.filter_by(title="1989").first().id, title="Shake It Off", duration=231),
        Song(album_id=Album.query.filter_by(title="1989").first().id, title="Blank Space", duration=231),
        Song(album_id=Album.query.filter_by(title="1989").first().id, title="Style", duration=231),

        # To Pimp a Butterfly
        Song(album_id=Album.query.filter_by(title="To Pimp a Butterfly").first().id, title="Alright", duration=210),
        Song(album_id=Album.query.filter_by(title="To Pimp a Butterfly").first().id, title="King Kunta", duration=238),
        Song(album_id=Album.query.filter_by(title="To Pimp a Butterfly").first().id, title="The Blacker the Berry", duration=324),

        # Good Kid, M.A.A.D City
        Song(album_id=Album.query.filter_by(title="Good Kid, M.A.A.D City").first().id, title="Swimming Pools (Drank)", duration=236),
        Song(album_id=Album.query.filter_by(title="Good Kid, M.A.A.D City").first().id, title="Bitch, Don't Kill My Vibe", duration=297),
        Song(album_id=Album.query.filter_by(title="Good Kid, M.A.A.D City").first().id, title="Poetic Justice", duration=304),

        # 21
        Song(album_id=Album.query.filter_by(title="21").first().id, title="Rolling in the Deep", duration=228),
        Song(album_id=Album.query.filter_by(title="21").first().id, title="Someone Like You", duration=285),
        Song(album_id=Album.query.filter_by(title="21").first().id, title="Set Fire to the Rain", duration=241),

        # 25
        Song(album_id=Album.query.filter_by(title="25").first().id, title="Hello", duration=295),
        Song(album_id=Album.query.filter_by(title="25").first().id, title="When We Were Young", duration=285),
        Song(album_id=Album.query.filter_by(title="25").first().id, title="Send My Love (To Your New Lover)", duration=225),

        # Lemonade
        Song(album_id=Album.query.filter_by(title="Lemonade").first().id, title="Formation", duration=229),
        Song(album_id=Album.query.filter_by(title="Lemonade").first().id, title="Sorry", duration=230),
        Song(album_id=Album.query.filter_by(title="Lemonade").first().id, title="Hold Up", duration=215),

        # Beyoncé
        Song(album_id=Album.query.filter_by(title="Beyoncé").first().id, title="Drunk in Love", duration=331),
        Song(album_id=Album.query.filter_by(title="Beyoncé").first().id, title="Partition", duration=205),
        Song(album_id=Album.query.filter_by(title="Beyoncé").first().id, title="XO", duration=210),

        # ÷ (Divide)
        Song(album_id=Album.query.filter_by(title="÷ (Divide)").first().id, title="Shape of You", duration=234),
        Song(album_id=Album.query.filter_by(title="÷ (Divide)").first().id, title="Castle on the Hill", duration=261),
        Song(album_id=Album.query.filter_by(title="÷ (Divide)").first().id, title="Perfect", duration=263),

        # × (Multiply)
        Song(album_id=Album.query.filter_by(title="× (Multiply)").first().id, title="Sing", duration=225),
        Song(album_id=Album.query.filter_by(title="× (Multiply)").first().id, title="Don't", duration=210),
        Song(album_id=Album.query.filter_by(title="× (Multiply)").first().id, title="Thinking Out Loud", duration=281),

        # 24K Magic
        Song(album_id=Album.query.filter_by(title="24K Magic").first().id, title="24K Magic", duration=227),
        Song(album_id=Album.query.filter_by(title="24K Magic").first().id, title="That's What I Like", duration=187),
        Song(album_id=Album.query.filter_by(title="24K Magic").first().id, title="Versace on the Floor", duration=280),

        # Doo-Wops & Hooligans
        Song(album_id=Album.query.filter_by(title="Doo-Wops & Hooligans").first().id, title="Just the Way You Are", duration=223),
        Song(album_id=Album.query.filter_by(title="Doo-Wops & Hooligans").first().id, title="Grenade", duration=227),
        Song(album_id=Album.query.filter_by(title="Doo-Wops & Hooligans").first().id, title="The Lazy Song", duration=187),

        # When We All Fall Asleep
        Song(album_id=Album.query.filter_by(title="When We All Fall Asleep").first().id, title="Bad Guy", duration=194),
        Song(album_id=Album.query.filter_by(title="When We All Fall Asleep").first().id, title="Bury a Friend", duration=193),
        Song(album_id=Album.query.filter_by(title="When We All Fall Asleep").first().id, title="When the Party's Over", duration=196),

        # Don't Smile at Me
        Song(album_id=Album.query.filter_by(title="Don't Smile at Me").first().id, title="Ocean Eyes", duration=200),
        Song(album_id=Album.query.filter_by(title="Don't Smile at Me").first().id, title="Bellyache", duration=174),
        Song(album_id=Album.query.filter_by(title="Don't Smile at Me").first().id, title="Copycat", duration=182),

        # Thank U, Next
        Song(album_id=Album.query.filter_by(title="Thank U, Next").first().id, title="Thank U, Next", duration=207),
        Song(album_id=Album.query.filter_by(title="Thank U, Next").first().id, title="7 rings", duration=178),
        Song(album_id=Album.query.filter_by(title="Thank U, Next").first().id, title="Break Up with Your Girlfriend, I'm Bored", duration=190),

        # Sweetener
        Song(album_id=Album.query.filter_by(title="Sweetener").first().id, title="No Tears Left to Cry", duration=221),
        Song(album_id=Album.query.filter_by(title="Sweetener").first().id, title="God is a woman", duration=231),
        Song(album_id=Album.query.filter_by(title="Sweetener").first().id, title="Breathin", duration=218),

        # Beerbongs & Bentleys
        Song(album_id=Album.query.filter_by(title="Beerbongs & Bentleys").first().id, title="Rockstar", duration=218),
        Song(album_id=Album.query.filter_by(title="Beerbongs & Bentleys").first().id, title="Psycho", duration=222),
        Song(album_id=Album.query.filter_by(title="Beerbongs & Bentleys").first().id, title="Better Now", duration=232),

        # Hollywood's Bleeding
        Song(album_id=Album.query.filter_by(title="Hollywood's Bleeding").first().id, title="Circles", duration=215),
        Song(album_id=Album.query.filter_by(title="Hollywood's Bleeding").first().id, title="Wow.", duration=168),
        Song(album_id=Album.query.filter_by(title="Hollywood's Bleeding").first().id, title="Goodbyes", duration=176),

        # Scorpion
        Song(album_id=Album.query.filter_by(title="Scorpion").first().id, title="In My Feelings", duration=217),
        Song(album_id=Album.query.filter_by(title="Scorpion").first().id, title="God's Plan", duration=198),
        Song(album_id=Album.query.filter_by(title="Scorpion").first().id, title="Nice for What", duration=211),

        # Views
        Song(album_id=Album.query.filter_by(title="Views").first().id, title="Hotline Bling", duration=267),
        Song(album_id=Album.query.filter_by(title="Views").first().id, title="One Dance", duration=173),
        Song(album_id=Album.query.filter_by(title="Views").first().id, title="Controlla", duration=245),
    ]

    db.session.add_all(songs)
    db.session.commit()


def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.songs RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))

    db.session.commit()
