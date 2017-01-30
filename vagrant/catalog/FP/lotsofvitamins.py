from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Vitamin, Base, FoodSource, User

engine = create_engine('sqlite:///vitaminCatalog.db')
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

User1 = User(name="Mickey Mouse", email="lisag@jnlcorp.com", picture="http://www.gettyimages.com/detail/157774730")
User2 = User(name="Lisa Guadagna", email="lisag@jnlcorp.com", picture="https://media.licdn.com/mpr/mpr/shrinknp_200_200/p/3/000/0f8/2b2/25fa838.jpg")
User3 = User(name="Sean Hamilton", email="lisag@jnlcorp.com", picture="http://www.gettyimages.com/detail/157774730")

#<div class="getty embed image" style="background-color:#fff;display:inline-block;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;color:#a7a7a7;font-size:11px;width:100%;max-width:341px;"><div style="padding:0;margin:0;text-align:left;"><a href="http://www.gettyimages.com/detail/157774730" target="_blank" style="color:#a7a7a7;text-decoration:none;font-weight:normal !important;border:none;display:inline-block;">Embed from Getty Images</a></div><div style="overflow:hidden;position:relative;height:0;padding:148.093842% 0 0 0;width:100%;"><iframe src="//embed.gettyimages.com/embed/157774730?et=hF7EEFLOT91ui6mNQmosMg&viewMoreLink=on&sig=Eam-JhsDWqnL2UTn_T-H2KMX-4lfs2-Ly46RRfxjM6A=&caption=true" width="341" height="505" scrolling="no" frameborder="0" style="display:inline-block;position:absolute;top:0;left:0;width:100%;height:100%;margin:0;"></iframe></div><p style="margin:0;"></p></div>

session.add(User1)


session.add(User2)


session.add(User3)


# Vitamin A Entry 
vitamin1 = Vitamin(name="Vitamin A", MinimumIntake="5000 IU")

session.add(vitamin1)


foodSource2 = foodSource(name="Beef Liver", description="Almost 3x the daily intake minimum",
                     serving="3 oz", amount="14,363 IU", vitamin=vitamin1)

session.add(foodSource2)



foodSource1 = foodSource(name="Carrots", description="over 100% DV",
                     serving="1 cup raw sliced", amount="21,384 IU", vitamin=vitamin1)

session.add(foodSource1)


foodSource2 = foodSource(name="Sweet Potato", description="over 100% DV",
                     serving="1 whole", amount="18,443 IU", vitamin=vitamin1)

session.add(foodSource2)
session.commit()

foodSource3 = foodSource(name="Kale", description="",
                     serving="1 cup", amount="6693 IU", vitamin=vitamin1)

session.add(foodSource3)


foodSource4 = foodSource(name="Spinach", description="",
                     serving="1 cup raw", amount="2813 IU", vitamin=vitamin1)

session.add(foodSource4)
session.commit()

foodSource5 = foodSource(name="Apricots", description="",
                     serving="1 fruit", amount="674 IU", vitamin=vitamin1)

session.add(foodSource5)
session.commit()

foodSource6 = foodSource(name="Brocolli", description="with Lemon",
                     serving="1 cpu raw", amount="567 IU", vitamin=vitamin1)

session.add(foodSource6)
session.commit()

foodSource7 = foodSource(name="Butter", description="On texas toast with American Cheese",
                     serving="$3.49", amount="355 IU", vitamin=vitamin1)

session.add(foodSource7)
session.commit()

foodSource8 = foodSource(name="Eggs", description="Made with freshest of ingredients and home grown spices",
                     serving="1 extra large", amount="302 IU", vitamin=vitamin1)

session.add(foodSource8)
session.commit()


# Menu for Super Stir Fry
vitamin2 = Vitamin(name="Antioxidants",  MinimumIntake="5000 IU")

session.add(vitamin2)
session.commit()


foodSource1 = foodSource(name="Goji Berries", description="With your choice of noodles vegetables and sauces",
                     serving="1/4 cup", amount="3290 ORAC", vitamin=vitamin2)

session.add(foodSource1)
session.commit()

foodSource2 = foodSource(
    name="Wild Blue Berries", description="about 1/2 cup", serving="14,000", amount="100 g", vitamin=vitamin2)

session.add(foodSource2)
session.commit()

foodSource3 = foodSource(name="Dark Chocolate", description="",
                     serving="12,000", amount="100 g", vitamin=vitamin2)

session.add(foodSource3)
session.commit()

foodSource4 = foodSource(name="Pecans", description="",
                     serving="21,000", amount="100 g", vitamin=vitamin2)

session.add(foodSource4)
session.commit()

foodSource5 = foodSource(name="Artichokes", description="",
                     serving="9,400", amount="100 g", vitamin=vitamin2)

session.add(foodSource5)
session.commit()

foodSource6 = foodSource(name="Elderberries", description="",
                     serving="14,000", amount="100 g", vitamin=vitamin2)

session.add(foodSource6)
session.commit()


# Menu for Panda Garden
vitamin1 = Vitamin(name="Vitamin C",  MinimumIntake="60 mg")

session.add(vitamin1)
session.commit()


foodSource1 = foodSource(name="Orange", description="",
                     serving="1 large", amount="82 mg", vitamin=vitamin1)

session.add(foodSource1)
session.commit()

foodSource2 = foodSource(name="Red Peppers", description="",
                     serving="1/2 cup chopped raw", amount="95 mg", vitamin=vitamin1)

session.add(foodSource2)
session.commit()

foodSource3 = foodSource(name="Kale", description="",
                     serving="1 cup", amount="80 mg", vitamin=vitamin1)

session.add(foodSource3)
session.commit()

foodSource4 = foodSource(name="Brussels Sprouts", description="",
                     serving="1/2 cup cooked", amount="48 mg", vitamin=vitamin1)

session.add(foodSource4)
session.commit()

foodSource2 = foodSource(name="Broccoli", description="",
                     serving="1/2 cup cooked", amount="51 mg", vitamin=vitamin1)

session.add(foodSource2)
session.commit()


# Menu for Thyme for that
vitamin1 = Vitamin(name="Zinc")
# 15 mg/day Daily Value 

session.add(vitamin1)
session.commit()


foodSource1 = foodSource(name="Grass Fed Beef", description="",
                     serving="3 oz", amount="33% daily value", vitamin=vitamin1)

session.add(foodSource1)
session.commit()

foodSource2 = foodSource(name="Kiefer or Yogurt", description="",
                     serving="1 cup", amount="15% daily value", vitamin=vitamin1)

session.add(foodSource2)
session.commit()

foodSource3 = foodSource(name="Lamb", description="",
                     serving="4 oz", amount="30% daily value", vitamin=vitamin1)

session.add(foodSource3)
session.commit()

foodSource4 = foodSource(name="Chickpeas", description="",
                     serving="1 cup", amount="4% daily value", vitamin=vitamin1)

session.add(foodSource4)
session.commit()

foodSource5 = foodSource(name="Pumpkin Seeds", description="",
                     serving="1/4 cup", amount="17% daily value", vitamin=vitamin1)

session.add(foodSource5)
session.commit()

foodSource2 = foodSource(name="Cashews", description="",
                     serving="1 oz", amount="10% daily value", vitamin=vitamin1)

session.add(foodSource2)
session.commit()


# Menu for Tony's Bistro
vitamin1 = Vitamin(name="Vitamin E")
# 27 mg daily value

session.add(vitamin1)
session.commit()


foodSource1 = foodSource(name="Almonds", description="",
                     serving="1 oz", amount="27% daily value", vitamin=vitamin1)

session.add(foodSource1)
session.commit()

foodSource2 = foodSource(name="Spinach", description="",
                     serving="1 bunch", amount="26% daily value", vitamin=vitamin1)

session.add(foodSource2)
session.commit()

foodSource3 = foodSource(name="Sweet Potato", description="",
                     serving="1 Tsb", amount="15% daily value", vitamin=vitamin1)

session.add(foodSource3)
session.commit()

foodSource4 = foodSource(name="Avocado",
                     description="1 whole", serving="2.7 mg (10% dv)", amount="", vitamin=vitamin1)

session.add(foodSource4)
session.commit()

foodSource5 = foodSource(name="Wheat Germ", description="",
                     serving="1 oz", amount="4.5 mg (17% dv)", vitamin=vitamin1)

session.add(foodSource5)
session.commit()


# Menu for Andala's
vitamin1 = Vitamin(name="Folate")

session.add(vitamin1)
session.commit()


foodSource1 = foodSource(name="Garbanzo Beans", description="",
                     serving="1/2 cup", amount="557 mcg", vitamin=vitamin1)

session.add(foodSource1)
session.commit()

foodSource2 = foodSource(name="Liver", description="",
                     serving="3 oz", amount="22  mcg (55% dv)", vitamin=vitamin1)

session.add(foodSource2)
session.commit()

foodSource3 = foodSource(name="Pinto Beans", description="",
                     serving="1/2 cup", amount="146 mcg (37% dv)", vitamin=vitamin1) 

session.add(foodSource3)
session.commit()

foodSource4 = foodSource(name="Lentils", description="",
                     serving="1/2 cup", amount="179 mcg (45% dv)", vitamin=vitamin1)

session.add(foodSource4)
session.commit()

foodSource2 = foodSource(name="Spinach", description="",
                     serving="1 cup", amount="56 mcg", vitamin=vitamin1)

session.add(foodSource2)
session.commit()


# New vitamin
vitamin1 = Vitamin(name="")

session.add(vitamin1)
session.commit()

foodSource9 = foodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource9)
session.commit()


foodSource1 = foodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource1)
session.commit()

foodSource2 = foodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource2)
session.commit()

foodSource3 = foodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource3)
session.commit()

foodSource4 = foodSource(name=" ", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource4)
session.commit()

foodSource2 = foodSource(name=" ", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource2)
session.commit()

foodSource10 = foodSource(name="", description="",
                      serving="", amount="", vitamin=vitamin1)

session.add(foodSource10)
session.commit()


# Omega-3
vitamin1 = Vitamin(name="Omega-3")

session.add(vitamin1)
session.commit()


foodSource1 = foodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource1)
session.commit()

foodSource2 = foodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource2)
session.commit()


vitamin1 = vitamin(name="Magnesium")
session.add(vitamin1)
session.commit()

foodSource1 = foodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource1)
session.commit

foodSource1 = foodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource1)
session.commit()


foodSource1 = foodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource1)
session.commit()


print "added menu items!"
