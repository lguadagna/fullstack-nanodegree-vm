from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Vitamin, Base, FoodSource

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


# start with a clean database by by deleting all rows


num_rows_deleted = session.query(Vitamin).delete()
print "rows deleted: %s" %num_rows_deleted
 
num_rows_deleted = session.query(FoodSource).delete()
print "rows deleted: %s" %num_rows_deleted
session.commit() 
Base.metadata.drop_all()
session.commit() 

Base.metadata.create_all(engine)

# Vitamin A Entry 
vitamin1 = Vitamin(name="Vitamin A", MinimumIntake="5000 IU", foodImageName="vitA.jpg")

session.add(vitamin1)
session.commit()

foodSource2 = FoodSource(name="Beef Liver", description="Almost 3x the daily intake minimum",
                     serving="3 oz", amount="14,363 IU", vitamin=vitamin1)

session.add(foodSource2)
session.commit()


foodSource1 = FoodSource(name="Carrots", description="over 100% DV",
                     serving="1 cup raw sliced", amount="21,384 IU", vitamin=vitamin1)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="Sweet Potato", description="over 100% DV",
                     serving="1 whole", amount="18,443 IU", vitamin=vitamin1)

session.add(foodSource2)
session.commit()

foodSource3 = FoodSource(name="Kale", description="",
                     serving="1 cup", amount="6693 IU", vitamin=vitamin1)

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name="Spinach", description="",
                     serving="1 cup raw", amount="2813 IU", vitamin=vitamin1)

session.add(foodSource4) 
session.commit()

foodSource5 = FoodSource(name="Apricots", description="",
                     serving="1 fruit", amount="674 IU", vitamin=vitamin1)

session.add(foodSource5)
session.commit()

foodSource6 = FoodSource(name="Brocolli", description="with Lemon",
                     serving="1 cpu raw", amount="567 IU", vitamin=vitamin1)

session.add(foodSource6)
session.commit()

foodSource7 = FoodSource(name="Butter", description="On texas toast with American Cheese",
                     serving="1 oz", amount="355 IU", vitamin=vitamin1)

session.add(foodSource7)
session.commit()

foodSource8 = FoodSource(name="Eggs", description="Made with freshest of ingredients and home grown spices",
                     serving="1 extra large", amount="302 IU", vitamin=vitamin1)

session.add(foodSource8)
session.commit()


# Menu for Super Stir Fry
vitamin2 = Vitamin(name="Antioxidants",  MinimumIntake="5000 IU", foodImageName="antioxidants.jpg")

session.add(vitamin2)
session.commit()


foodSource1 = FoodSource(name="Goji Berries", description="With your choice of noodles vegetables and sauces",
                     serving="1/4 cup", amount="3290 ORAC", vitamin=vitamin2)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(
    name="Wild Blue Berries", description="about 1/2 cup", serving="14,000", amount="100 g", vitamin=vitamin2)

session.add(foodSource2)
session.commit()

foodSource3 = FoodSource(name="Dark Chocolate", description="",
                     serving="12,000", amount="100 g", vitamin=vitamin2)

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name="Pecans", description="",
                     serving="21,000", amount="100 g", vitamin=vitamin2)

session.add(foodSource4)
session.commit()

foodSource5 = FoodSource(name="Artichokes", description="",
                     serving="9,400", amount="100 g", vitamin=vitamin2)

session.add(foodSource5)
session.commit()

foodSource6 = FoodSource(name="Elderberries", description="",
                     serving="14,000", amount="100 g", vitamin=vitamin2)

session.add(foodSource6)
session.commit()


# Menu for Panda Garden
vitamin1 = Vitamin(name="Vitamin C",  MinimumIntake="60 mg", foodImageName="vitC.jpg")

session.add(vitamin1)
session.commit()


foodSource1 = FoodSource(name="Orange", description="",
                     serving="1 large", amount="82 mg", vitamin=vitamin1)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="Red Peppers", description="",
                     serving="1/2 cup chopped raw", amount="95 mg", vitamin=vitamin1)

session.add(foodSource2)
session.commit()

foodSource3 = FoodSource(name="Kale", description="",
                     serving="1 cup", amount="80 mg", vitamin=vitamin1)

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name="Brussels Sprouts", description="",
                     serving="1/2 cup cooked", amount="48 mg", vitamin=vitamin1)

session.add(foodSource4)
session.commit()

foodSource2 = FoodSource(name="Broccoli", description="",
                     serving="1/2 cup cooked", amount="51 mg", vitamin=vitamin1)

session.add(foodSource2)
session.commit()


# Menu for Thyme for that
vitamin1 = Vitamin(name="Zinc",  MinimumIntake="xx" , foodImageName="zinc.jpg")
# 15 mg/day Daily Value 

session.add(vitamin1)
session.commit()


foodSource1 = FoodSource(name="Grass Fed Beef", description="",
                     serving="3 oz", amount="33% daily value", vitamin=vitamin1)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="Kiefer or Yogurt", description="",
                     serving="1 cup", amount="15% daily value", vitamin=vitamin1)

session.add(foodSource2)
session.commit()

foodSource3 = FoodSource(name="Lamb", description="",
                     serving="4 oz", amount="30% daily value", vitamin=vitamin1)

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name="Chickpeas", description="",
                     serving="1 cup", amount="4% daily value", vitamin=vitamin1)

session.add(foodSource4)
session.commit()

foodSource5 = FoodSource(name="Pumpkin Seeds", description="",
                     serving="1/4 cup", amount="17% daily value", vitamin=vitamin1)

session.add(foodSource5)
session.commit()

foodSource2 = FoodSource(name="Cashews", description="",
                     serving="1 oz", amount="10% daily value", vitamin=vitamin1)

session.add(foodSource2)
session.commit()


# Menu for Tony's Bistro
vitamin1 = Vitamin(name="Vitamin E",  MinimumIntake="xx mg" , foodImageName="vitE.jpg")
# 27 mg daily value

session.add(vitamin1)
session.commit()


foodSource1 = FoodSource(name="Almonds", description="",
                     serving="1 oz", amount="27% daily value", vitamin=vitamin1)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="Spinach", description="",
                     serving="1 bunch", amount="26% daily value", vitamin=vitamin1)

session.add(foodSource2)
session.commit()

foodSource3 = FoodSource(name="Sweet Potato", description="",
                     serving="1 Tsb", amount="15% daily value", vitamin=vitamin1)

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name="Avocado",
                     description="1 whole", serving="2.7 mg (10% dv)", amount="", vitamin=vitamin1)

session.add(foodSource4)
session.commit()

foodSource5 = FoodSource(name="Wheat Germ", description="",
                     serving="1 oz", amount="4.5 mg (17% dv)", vitamin=vitamin1)

session.add(foodSource5)
session.commit()


# Menu for Andala's
vitamin1 = Vitamin(name="Folate",  MinimumIntake="xx mg")

session.add(vitamin1)
session.commit()


foodSource1 = FoodSource(name="Garbanzo Beans", description="",
                     serving="1/2 cup", amount="557 mcg", vitamin=vitamin1)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="Liver", description="",
                     serving="3 oz", amount="22  mcg (55% dv)", vitamin=vitamin1)

session.add(foodSource2)
session.commit()

foodSource3 = FoodSource(name="Pinto Beans", description="",
                     serving="1/2 cup", amount="146 mcg (37% dv)", vitamin=vitamin1) 

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name="Lentils", description="",
                     serving="1/2 cup", amount="179 mcg (45% dv)", vitamin=vitamin1)

session.add(foodSource4)
session.commit()

foodSource2 = FoodSource(name="Spinach", description="",
                     serving="1 cup", amount="56 mcg", vitamin=vitamin1)

session.add(foodSource2)
session.commit()


# Menu for Auntie Ann's
# vitamin1 = Vitamin(name="")
# 
# session.add(vitamin1)
# session.commit()
# 
# foodSource9 = FoodSource(name="", description="",
#                      serving="", amount="", vitamin=vitamin1)
# 
# session.add(foodSource9)
# session.commit()
# 
# 
# foodSource1 = FoodSource(name="", description="",
#                      serving="", amount="", vitamin=vitamin1)
# 
# session.add(foodSource1)
# session.commit()
# 
# foodSource2 = FoodSource(name="", description="",
#                      serving="", amount="", vitamin=vitamin1)
# 
# session.add(foodSource2)
# session.commit()
# 
# foodSource3 = FoodSource(name="", description="",
#                      serving="", amount="", vitamin=vitamin1)
# 
# session.add(foodSource3)
# session.commit()
# 
# foodSource4 = FoodSource(name=" ", description="",
#                      serving="", amount="", vitamin=vitamin1)
# 
# session.add(foodSource4)
# session.commit()
# 
# foodSource2 = FoodSource(name=" ", description="",
#                      serving="", amount="", vitamin=vitamin1)
# 
# session.add(foodSource2)
# session.commit()
# 
# foodSource10 = FoodSource(name="", description="",
#                       serving="", amount="", vitamin=vitamin1)
# 
# session.add(foodSource10)
# session.commit()


# Menu for Cocina Y Amor
vitamin1 = Vitamin(name="Omega-3" ,  MinimumIntake="xx mg", foodImageName="omega-3.jpg")

session.add(vitamin1)
session.commit()


foodSource1 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource2)
session.commit()


vitamin1 = Vitamin(name="Vitamin K", MinimumIntake= "xx mg")
session.add(vitamin1)
session.commit()

foodSource1 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource1)
session.commit

foodSource1 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource1)
session.commit()


foodSource1 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1)

session.add(foodSource1)
session.commit()


print "added menu items!"
