from app.models import db, Review, User, Album, environment, SCHEMA
from sqlalchemy.sql import text


def seed_reviews():
    

    abbey_road_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Great album, loved every track!",
        album_id=1
    )

    abbey_road_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Classic Beatles at their best!",
        album_id=1
    )

    sgt_peppers_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A groundbreaking album!",
        album_id=2
    )

    sgt_peppers_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A timeless classic by The Beatles.",
        album_id=2
    )

    sgt_peppers_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Innovative and influential.",
        album_id=2
    )

    dark_side_of_the_moon_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A phenomenal album from start to finish.",
        album_id=3
    )

    dark_side_of_the_moon_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="An incredible journey through sound!",
        album_id=3
    )

    the_wall_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A rock opera like no other!",
        album_id=4
    )

    the_wall_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A powerful and emotional album.",
        album_id=4
    )

    the_wall_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="An essential album for any music lover.",
        album_id=4
    )

    

    night_at_the_opera_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Bohemian Rhapsody is a masterpiece.",
        album_id=5
    )

    night_at_the_opera_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Queen's creativity shines in this album!",
        album_id=5
    )

    news_of_the_world_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="We Will Rock You and We Are the Champions are iconic!",
        album_id=6
    )

    news_of_the_world_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Queen delivers another classic.",
        album_id=6
    )

    news_of_the_world_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="A must-listen for any Queen fan.",
        album_id=6
    )

    

    nevermind_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every track is a hit!",
        album_id=7
    )

    nevermind_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Nirvana at their best.",
        album_id=7
    )

    in_utero_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Raw and powerful!",
        album_id=8
    )

    in_utero_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="An intense and emotional album.",
        album_id=8
    )

    in_utero_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Nirvana's last and greatest album.",
        album_id=8
    )

    

    master_of_puppets_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A true masterpiece in metal.",
        album_id=9
    )

    master_of_puppets_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Metallica's best work!",
        album_id=9
    )

    ride_the_lightning_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A metal classic!",
        album_id=10
    )

    ride_the_lightning_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="An essential album for any metal fan.",
        album_id=10
    )

    ride_the_lightning_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Metallica's raw energy at its best.",
        album_id=10
    )

    

    let_it_bleed_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Timeless music.",
        album_id=11
    )

    let_it_bleed_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Rolling Stones never disappoint!",
        album_id=11
    )

    sticky_fingers_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A rock and roll classic!",
        album_id=12
    )

    sticky_fingers_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every track is fantastic.",
        album_id=12
    )

    sticky_fingers_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="The Rolling Stones at their peak.",
        album_id=12
    )

    

    ok_computer_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Innovative and groundbreaking.",
        album_id=13
    )

    ok_computer_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A must-listen!",
        album_id=13
    )

    kid_a_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Experimental and groundbreaking!",
        album_id=14
    )

    kid_a_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A transformative album.",
        album_id=14
    )

    kid_a_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Radiohead at their most innovative.",
        album_id=14
    )

    

    led_zeppelin_iv_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every track is fantastic.",
        album_id=15
    )

    led_zeppelin_iv_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Led Zeppelin at their best.",
        album_id=15
    )

    houses_of_the_holy_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="An amazing follow-up to Led Zeppelin IV!",
        album_id=16
    )

    houses_of_the_holy_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Led Zeppelin's versatility shines.",
        album_id=16
    )

    houses_of_the_holy_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="A diverse and powerful album.",
        album_id=16
    )

    

    london_calling_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Punk rock perfection.",
        album_id=17
    )

    london_calling_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="The Clash's best work.",
        album_id=17
    )

    combat_rock_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A solid album with great tracks!",
        album_id=18
    )

    combat_rock_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="The Clash at their peak.",
        album_id=18
    )

    combat_rock_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Another classic by The Clash.",
        album_id=18
    )

    

    the_joshua_tree_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Incredible sound and lyrics.",
        album_id=19
    )

    the_joshua_tree_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="U2 at their best.",
        album_id=19
    )

    achtung_baby_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="U2's reinvention and one of their best albums!",
        album_id=20
    )

    achtung_baby_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A bold and brilliant album.",
        album_id=20
    )

    achtung_baby_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="U2's creativity shines.",
        album_id=20
    )

    

    californication_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Funky and fresh!",
        album_id=21
    )

    californication_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Red Hot Chili Peppers' best work.",
        album_id=21
    )

    by_the_way_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A fantastic follow-up to Californication!",
        album_id=22
    )

    by_the_way_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Red Hot Chili Peppers continue to innovate.",
        album_id=22
    )

    by_the_way_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Another great album by RHCP.",
        album_id=22
    )

    

    fearless_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Great songwriting and production.",
        album_id=23
    )

    fearless_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Taylor Swift's breakout album.",
        album_id=23
    )

    ninteeneightynine_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Taylor Swift's pop transformation is perfect!",
        album_id=24
    )

    ninteeneightynine_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every song is a hit.",
        album_id=24
    )

    ninteeneightynine_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Taylor Swift's best album.",
        album_id=24
    )

    

    to_pimp_a_butterfly_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Kendrick Lamar at his best.",
        album_id=25
    )

    to_pimp_a_butterfly_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A modern classic.",
        album_id=25
    )

    good_kid_maad_city_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A storytelling masterpiece!",
        album_id=26
    )

    good_kid_maad_city_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Kendrick's major label debut is flawless.",
        album_id=26
    )

    good_kid_maad_city_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="An essential album.",
        album_id=26
    )

    

    twentyone_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Adele's voice is amazing.",
        album_id=27
    )

    twentyone_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A modern classic.",
        album_id=27
    )

    twentyfive_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Adele's voice continues to amaze!",
        album_id=28
    )

    twentyfive_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every song is powerful.",
        album_id=28
    )

    twentyfive_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Adele at her best.",
        album_id=28
    )

    

    lemonade_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Beyoncé at her best.",
        album_id=29
    )

    lemonade_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A groundbreaking album.",
        album_id=29
    )

    beyonce_album_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Beyoncé's self-titled album is a triumph!",
        album_id=30
    )

    beyonce_album_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every track is a hit.",
        album_id=30
    )

    beyonce_album_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="A bold and innovative album.",
        album_id=30
    )

    divide_review1 = Review(
        user_id=User.query.filter_by(username="demo").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A fantastic pop album!",
        album_id=31
    )

    divide_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Ed Sheeran's best work.",
        album_id=31
    )

    divide_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every song is a hit.",
        album_id=31
    )

    multiply_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Ed Sheeran's songwriting is top-notch!",
        album_id=32
    )

    multiply_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A diverse and engaging album.",
        album_id=32
    )

    multiply_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="A solid album with great tracks.",
        album_id=32
    )

    twentyfourkmagic_review1 = Review(
        user_id=User.query.filter_by(username="demo").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A funky and fun album!",
        album_id=33
    )

    twentyfourkmagic_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Bruno Mars at his best.",
        album_id=33
    )

    twentyfourkmagic_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every track is a hit.",
        album_id=33
    )

    doo_wops_and_hooligans_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Bruno Mars' debut is a hit!",
        album_id=34
    )

    doo_wops_and_hooligans_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every song is catchy and fun.",
        album_id=34
    )

    doo_wops_and_hooligans_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="A great debut album.",
        album_id=34
    )

    when_we_all_fall_asleep_review1 = Review(
        user_id=User.query.filter_by(username="demo").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A unique and haunting album!",
        album_id=35
    )

    when_we_all_fall_asleep_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Billie Eilish's debut is amazing.",
        album_id=35
    )

    when_we_all_fall_asleep_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every track is innovative.",
        album_id=35
    )

    dont_smile_at_me_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A fantastic EP by Billie Eilish!",
        album_id=36
    )

    dont_smile_at_me_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every song is great.",
        album_id=36
    )

    dont_smile_at_me_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="A promising start for Billie Eilish.",
        album_id=36
    )

    thank_u_next_review1 = Review(
        user_id=User.query.filter_by(username="demo").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Ariana Grande's best work!",
        album_id=37
    )

    thank_u_next_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Great tracks throughout.",
        album_id=37
    )

    thank_u_next_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Ariana Grande at her best.",
        album_id=37
    )

    sweetener_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A fresh and exciting album!",
        album_id=38
    )

    sweetener_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every track is enjoyable.",
        album_id=38
    )

    sweetener_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Ariana Grande's creativity shines.",
        album_id=38
    )

    beerbongs_and_bentleys_review1 = Review(
        user_id=User.query.filter_by(username="demo").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A fantastic album by Post Malone!",
        album_id=39
    )

    beerbongs_and_bentleys_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Great tracks and production.",
        album_id=39
    )

    beerbongs_and_bentleys_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Post Malone at his best.",
        album_id=39
    )

    hollywoods_bleeding_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A solid follow-up album!",
        album_id=40
    )

    hollywoods_bleeding_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Post Malone continues to impress.",
        album_id=40
    )

    hollywoods_bleeding_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Another great album by Post Malone.",
        album_id=40
    )

    scorpion_review1 = Review(
        user_id=User.query.filter_by(username="demo").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A fantastic double album by Drake!",
        album_id=41
    )

    scorpion_review2 = Review(
        user_id=User.query.filter_by(username="marnie").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Great tracks throughout.",
        album_id=41
    )

    scorpion_review3 = Review(
        user_id=User.query.filter_by(username="bobbie").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Drake at his best.",
        album_id=41
    )

    views_review1 = Review(
        user_id=User.query.filter_by(username="nikita").first().id,
        reviewable_type="Album",
        rating=5,
        comment="A fantastic album by Drake!",
        album_id=42
    )

    views_review2 = Review(
        user_id=User.query.filter_by(username="erik").first().id,
        reviewable_type="Album",
        rating=5,
        comment="Every track is a hit.",
        album_id=42
    )

    views_review3 = Review(
        user_id=User.query.filter_by(username="cece").first().id,
        reviewable_type="Album",
        rating=4,
        comment="Drake's creativity shines.",
        album_id=42
    )

    db.session.add_all(
        [
            
            abbey_road_review2,
            abbey_road_review3,
            sgt_peppers_review1,
            sgt_peppers_review2,
            sgt_peppers_review3,
            
            dark_side_of_the_moon_review2,
            dark_side_of_the_moon_review3,
            the_wall_review1,
            the_wall_review2,
            the_wall_review3,
            
            night_at_the_opera_review2,
            night_at_the_opera_review3,
            news_of_the_world_review1,
            news_of_the_world_review2,
            news_of_the_world_review3,
            
            nevermind_review2,
            nevermind_review3,
            in_utero_review1,
            in_utero_review2,
            in_utero_review3,
            
            master_of_puppets_review2,
            master_of_puppets_review3,
            ride_the_lightning_review1,
            ride_the_lightning_review2,
            ride_the_lightning_review3,
            
            let_it_bleed_review2,
            let_it_bleed_review3,
            sticky_fingers_review1,
            sticky_fingers_review2,
            sticky_fingers_review3,
            
            ok_computer_review2,
            ok_computer_review3,
            kid_a_review1,
            kid_a_review2,
            kid_a_review3,
            
            led_zeppelin_iv_review2,
            led_zeppelin_iv_review3,
            houses_of_the_holy_review1,
            houses_of_the_holy_review2,
            houses_of_the_holy_review3,
            
            london_calling_review2,
            london_calling_review3,
            combat_rock_review1,
            combat_rock_review2,
            combat_rock_review3,
            
            the_joshua_tree_review2,
            the_joshua_tree_review3,
            achtung_baby_review1,
            achtung_baby_review2,
            achtung_baby_review3,
            
            californication_review2,
            californication_review3,
            by_the_way_review1,
            by_the_way_review2,
            by_the_way_review3,
            
            fearless_review2,
            fearless_review3,
            ninteeneightynine_review1,
            ninteeneightynine_review2,
            ninteeneightynine_review3,
            
            to_pimp_a_butterfly_review2,
            to_pimp_a_butterfly_review3,
            good_kid_maad_city_review1,
            good_kid_maad_city_review2,
            good_kid_maad_city_review3,
            
            twentyone_review2,
            twentyone_review3,
            twentyfive_review1,
            twentyfive_review2,
            twentyfive_review3,
            
            lemonade_review2,
            lemonade_review3,
            beyonce_album_review1,
            beyonce_album_review2,
            beyonce_album_review3,
            divide_review1,
            divide_review2,
            divide_review3,
            multiply_review1,
            multiply_review2,
            multiply_review3,
            twentyfourkmagic_review1,
            twentyfourkmagic_review2,
            twentyfourkmagic_review3,
            doo_wops_and_hooligans_review1,
            doo_wops_and_hooligans_review2,
            doo_wops_and_hooligans_review3,
            when_we_all_fall_asleep_review1,
            when_we_all_fall_asleep_review2,
            when_we_all_fall_asleep_review3,
            dont_smile_at_me_review1,
            dont_smile_at_me_review2,
            dont_smile_at_me_review3,
            thank_u_next_review1,
            thank_u_next_review2,
            thank_u_next_review3,
            sweetener_review1,
            sweetener_review2,
            sweetener_review3,
            beerbongs_and_bentleys_review1,
            beerbongs_and_bentleys_review2,
            beerbongs_and_bentleys_review3,
            hollywoods_bleeding_review1,
            hollywoods_bleeding_review2,
            hollywoods_bleeding_review3,
            scorpion_review1,
            scorpion_review2,
            scorpion_review3,
            views_review1,
            views_review2,
            views_review3,
        ]
    )
    db.session.commit()


def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
