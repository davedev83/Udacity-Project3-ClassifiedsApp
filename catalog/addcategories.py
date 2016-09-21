from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///classifieds.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create admin user for static categories
User1 = User(name="RoboAdmin", email="admin@admin.com",
             picture='http://informationtechnologysystems.com/wp-content/uploads/2016/01/cute-807306_960_720.png')
session.add(User1)
session.commit()

# list of fixed categories
categories = ("Autos", "Collectibles", "Housing", "Services", "Pets")

# Add categories
for category in categories:
    query = Category(user_id=1, name=category)
    session.add(query)
    session.commit()

#add listings
item1 = Item(user_id=1, name="2016 Tesla Model S", description="A five-door full-sized all-electric luxury liftback, the Tesla Model S is obviously produced by Tesla Motors. It was first introduced in June 2012",
                     price="$67,500", category_id=1, contact_name="David", contact_number="555-555-5555", image="https://8096-presscdn-0-43-pagely.netdna-ssl.com/wp-content/uploads/2016/03/Tesla-Model-S-Exterior.jpg")

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Upper Deck 1992 Baseball Edition", description="1992 Upper deck Baseball Edition \
Features Limited Edition Heroes still in wrap unopened",
                     price="$10", category_id=2, contact_name="David", contact_number="555-555-5555", image="https://pristineauction.s3.amazonaws.com/31/317906/main_1-Lot-of-3-Factory-Sealed-Boxes-of-Baseball-Cards-with-1992-Series-1-Leaf-Set-1992-Upper-Deck-Baseball-Edition-1991-Upper-Deck-Baseball-Heroes-Find-the-Nolan-PristineAuction.com.jpg")

session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Spacious 2 bd/1bath in S. RB", description="This is a beautiful and spacious 2bd/1 bath unit in South Redondo Beach. It features fresh custom paint, vaulted ceilings, granite countertops",
                     price="$2,900", category_id=3, contact_name="David", contact_number="555-555-5555", image="https://images.craigslist.org/01111_15VWpVRMKnb_600x450.jpg")

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="AUTO BODY REPAIR AND INNER STRUCTURE DAMAGE", description="THANK YOU FOR VIEWING OUR AD !!!\
1. NO PAINT WORK PRIMER ONLY.\
2. PROFESSIONAL WORK DONE. \
3. 37 PLUS YEARS EXPERIENCE.\
4. TOP QUALITY MATERIALS USED. ",
                     price="Call", category_id=4, contact_name="David", contact_number="555-555-5555", image="https://images.craigslist.org/00T0T_853ZaUGPgPr_600x450.jpg")

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="YORKIE POODLE PUPPIE", description="Male ready for his forever home he is beautifull with a beautifull personality. Fur does not an will not shed rehoming fee 200. Firm",
                     price="$200", category_id=5, contact_name="David", contact_number="555-555-5555", image="http://www.le-poodles-guide.com/images/YorkiePoo.jpg")

session.add(item5)
session.commit()


item6 = Item(user_id=1, name="2015 Lexus RC F", description='<h4>Up for sale is an <span style="color: #ff9900;"><strong>incredible</strong> </span>looking and highly customized 2015 Lexus RC F with just 10459 original miles. This Lexus is in absolutely fantastic cosmetic condition and you will have a hard time to find flaws, if any.</h4><p><iframe src="//www.youtube.com/embed/RXJm4DcbuXg" width="560" height="314" allowfullscreen="allowfullscreen"></iframe></p>',
                     price="$58,000", category_id=1, contact_name="David", contact_number="555-555-5555", image="http://o.aolcdn.com/dims-global/dims3/GLOB/legacy_thumbnail/750x422/quality/95/http://www.blogcdn.com/slideshows/images/slides/359/549/7/S3595497/slug/l/01-2015-lexus-rc-f-review-1.jpg")

session.add(item6)
session.commit()
