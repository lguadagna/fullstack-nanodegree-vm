from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Vitamin, Base, FoodSource, User

engine = create_engine('sqlite:///vitaminCatalog.db', echo=True)
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
User2 = User(name="Lisa Guadagna", email="lisa.guadagna@gmail.com", picture="https://media.licdn.com/mpr/mpr/shrinknp_200_200/p/3/000/0f8/2b2/25fa838.jpg")
User3 = User(name="Sean Hamilton", email="sean.hamilton@gmail.com", picture="http://www.gettyimages.com/detail/157774730")

print User1.name
print User2.name
print User3.name

#<div class="getty embed image" style="background-color:#fff;display:inline-block;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;color:#a7a7a7;font-size:11px;width:100%;max-width:341px;"><div style="padding:0;margin:0;text-align:left;"><a href="http://www.gettyimages.com/detail/157774730" target="_blank" style="color:#a7a7a7;text-decoration:none;font-weight:normal !important;border:none;display:inline-block;">Embed from Getty Images</a></div><div style="overflow:hidden;position:relative;height:0;padding:148.093842% 0 0 0;width:100%;"><iframe src="//embed.gettyimages.com/embed/157774730?et=hF7EEFLOT91ui6mNQmosMg&viewMoreLink=on&sig=Eam-JhsDWqnL2UTn_T-H2KMX-4lfs2-Ly46RRfxjM6A=&caption=true" width="341" height="505" scrolling="no" frameborder="0" style="display:inline-block;position:absolute;top:0;left:0;width:100%;height:100%;margin:0;"></iframe></div><p style="margin:0;"></p></div>

session.add(User1)

session.add(User2)

session.add(User3)
session.commit()


# Vitamin A Entry 
vitamin1 = Vitamin(name="Vitamin A", MinimumIntake="5000 IU", user_id=User1.id, foodImageName="vitA.jpg", \
                   description="Shiny Eyes, Skin", longDescription="Vitamin A is a fat soluble vitamin that has \
                   a critical role in maintaining healthy vision, neurological function and healthy skin. \
                    A vitamin A deficiency will lead to night blindness and can eventually cause thickening \
                    of the cornea and blindness.")

session.add(vitamin1)
session.commit()

foodSource2 = FoodSource(name="Beef Liver", description="Almost 3x the daily intake minimum",
                     serving="3 oz", amount="14,363 IU", vitamin=vitamin1, user_id = User1.id  )

session.add(foodSource2)
session.commit()


foodSource1 = FoodSource(name="Carrots", description="over 100% DV",
                     serving="1 cup raw sliced", amount="21,384 IU", vitamin=vitamin1, user_id = User1.id  )

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="Sweet Potato", description="over 100% DV",
                     serving="1 whole", amount="18,443 IU", vitamin=vitamin1, user_id = User1.id  )

session.add(foodSource2)
session.commit()

foodSource3 = FoodSource(name="Kale", description="",
                     serving="1 cup", amount="6693 IU", vitamin=vitamin1,  user_id = User1.id )

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name="Spinach", description="",
                     serving="1 cup raw", amount="2813 IU", vitamin=vitamin1, user_id = User1.id  )

session.add(foodSource4)


foodSource5 = FoodSource(name="Apricots", description="",
                     serving="1 fruit", amount="674 IU", vitamin=vitamin1,  user_id = User1.id )

session.add(foodSource5)


foodSource6 = FoodSource(name="Brocolli", description="with Lemon",
                     serving="1 cpu raw", amount="567 IU", vitamin=vitamin1,  user_id = User1.id )

session.add(foodSource6)
session.commit()

foodSource7 = FoodSource(name="Butter", description="On texas toast with American Cheese",
                     serving="$3.49", amount="355 IU", vitamin=vitamin1,  user_id = User1.id )

session.add(foodSource7)
session.commit()

foodSource8 = FoodSource(name="Eggs", description="Free Range Hens in organic environment",
         serving="1 extra large", amount="302 IU", user_id = User1.id )

session.add(foodSource8)
session.commit()


# Menu for Super Stir Fry
vitamin2 = Vitamin(name="Antioxidants",  MinimumIntake="5000 IU", user_id = User1.id, foodImageName="antioxidants.jpg" ,
  description="Slow Aging", longDescription="Antioxidants are substances that help prevent certain types of cell damage, \
especially those caused by oxidation. Free radicals are very dangerous to the bodys \
tissues and have been connected to cancer and premature aging. \
Oxidative damage plays a major role in disease today and has been linked to health conditions like heart disease, cancer and dementia. \
Some of the benefits of consuming antioxidant rich foods include: Slower aging, Healthy glowing skin, Reduced cancer risk, Detoxification support, Longer life span ")

session.add(vitamin2)
session.commit()


foodSource1 = FoodSource(name="Goji Berries", description="From the Amazon",
                     serving="1/4 cup", amount="3290 ORAC", vitamin=vitamin2, user_id = User2.id)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(
    name="Wild Blue Berries", description="about 1/2 cup", serving="14,000", amount="100 g", vitamin=vitamin2, user_id = User2.id)

session.add(foodSource2)
session.commit()
foodSource3 = FoodSource(name="Dark Chocolate", description="",
                     serving="12,000", amount="100 g", vitamin=vitamin2, user_id = User2.id)

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name="Pecans", description="",
                     serving="21,000", amount="100 g", vitamin=vitamin2, user_id = User2.id)

session.add(foodSource4)
session.commit()

foodSource5 = FoodSource(name="Artichokes", description="",
                     serving="9,400", amount="100 g", vitamin=vitamin2, user_id = User2.id)

session.add(foodSource5)
session.commit()

foodSource6 = FoodSource(name="Elderberries", description="",
                     serving="14,000", amount="100 g", vitamin=vitamin2, user_id = User2.id)

session.add(foodSource6)
session.commit()


# Menu for Panda Garden
vitC_description = "Vitamin C is a water-soluble vitamin that plays a role in maintaining the health of the bodys \
connective tissue as well as acting as an antioxidant. A severe vitamin C deficiency will result in scurvy, a disease \
resulting from the breakdown of collagen. Scurvy is rarely seen today, as only a very small amount of vitamin C \
is needed to prevent it. But even mild vitamin C deficiency symptoms include: easy bruising, bleeding gums, slow wound healing, \
dry splitting hair, nosebleeds, and dry red spots on the skin, where blood has leaked out of the capillaries. \
Benefits of consuming vitamin C rich foods include: Promotes healthy glowing skin and collagen formation, Improves mineral absorption, \
Fights free radical damage, Boosts immunity fighting colds and flu, Improves health of gums and teeth, Vital for \
circulation and heart health" 

vitamin1 = Vitamin(name="Vitamin C",  MinimumIntake="60 mg", user_id = User3.id, foodImageName="vitC.jpg" , longDescription=vitC_description, description="Healthy Skin, Immunity")

session.add(vitamin1)
session.commit()


foodSource1 = FoodSource(name="Orange", description="",
                     serving="1 large", amount="82 mg", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource1)
session.commit()

# Menu for Panda Garden
vitamin1 = Vitamin(name="Vitamin C",  MinimumIntake="60 mg",user_id = User3.id )

session.add(vitamin1)
session.commit()


foodSource1 = FoodSource(name="Orange", description="",
                     serving="1 large", amount="82 mg", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="Red Peppers", description="",
                     serving="1/2 cup chopped raw", amount="95 mg", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource2)
session.commit()

foodSource3 = FoodSource(name="Kale", description="",
                     serving="1 cup", amount="80 mg", vitamin=vitamin1,user_id = User3.id )

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name="Brussels Sprouts", description="",
                     serving="1/2 cup cooked", amount="48 mg", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource4)
session.commit()

foodSource2 = FoodSource(name="Broccoli", description="",
                     serving="1/2 cup cooked", amount="51 mg", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource2)
session.commit()


# Menu for Thyme for that
zinc_description="Zinc is an essential trace mineral that plays a role in over a hundred enzymatic reactions in the body.\
                 It functions to protect against oxidative damage, helps with wound healing, makes DNA and helps with the \
                 formation of hemoglobin. Zinc deficiency symptoms include frequent colds, leaky gut, consistent diarrhea, \
                 poor vision, infertility, thinning hair, stunted growth in children and slow healing wounds."
vitamin1 = Vitamin(name="Zinc",  MinimumIntake="60 mg", user_id = User1.id, foodImageName="zinc.jpg" , longDescription=zinc_description, description="immunity")
# 15 mg/day Daily Value 

session.add(vitamin1)
session.commit()


foodSource1 = FoodSource(name="Grass Fed Beef", description="",
                     serving="3 oz", amount="33% daily value", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="Kiefer or Yogurt", description="",
                     serving="1 cup", amount="15% daily value", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource2)
session.commit()

foodSource3 = FoodSource(name="Lamb", description="",
                     serving="4 oz", amount="30% daily value", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name="Chickpeas", description="",
                     serving="1 cup", amount="4% daily value", vitamin=vitamin1,user_id = User3.id )

session.add(foodSource4)
session.commit()

foodSource5 = FoodSource(name="Pumpkin Seeds", description="",
                     serving="1/4 cup", amount="17% daily value", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource5)
session.commit()

foodSource2 = FoodSource(name="Cashews", description="",
                     serving="1 oz", amount="10% daily value", vitamin=vitamin1,user_id = User3.id )

session.add(foodSource2)
session.commit()


# Menu for Tony's Bistro
vitE_description="Vitamin E is a fat-soluble vitamin which plays a role as an antioxidant in the body. \
It also helps prevent damage to specific fats that are critical for health. \
Deficiency symptoms include loss of muscle coordination, impaired vision, and speech. \
Supplementing and consuming vitamin E rich foods can have the following benefits: Balance cholesterol, \
Repair damaged skin, Thicken hair, Balance hormones, Improve vision"



vitamin1 = Vitamin(name="Vitamin E", MinimumIntake="60 mg", user_id = User1.id, foodImageName="vitE.jpg" , longDescription=vitE_description, description="Vision, balanced hormones" )
# 27 mg daily value

session.add(vitamin1)
session.commit()


foodSource1 = FoodSource(name="Almonds", description="",
                     serving="1 oz", amount="27% daily value", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="Spinach", description="",
                     serving="1 bunch", amount="26% daily value", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource2)
session.commit()

foodSource3 = FoodSource(name="Sweet Potato", description="",
                     serving="1 Tsb", amount="15% daily value", vitamin=vitamin1,user_id = User3.id )

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name="Avocado",
                     description="1 whole", serving="2.7 mg (10% dv)", amount="", vitamin=vitamin1,user_id = User3.id )

session.add(foodSource4)
session.commit()

foodSource5 = FoodSource(name="Wheat Germ", description="",
                     serving="1 oz", amount="4.5 mg (17% dv)", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource5)
session.commit()


# Menu for Andala's
folate_description="Folate is also considered a B-vitamin and is water soluble, but plays a slightly different \
                   role from the other B-vitamins in that it doesnt participate in energy metabolism.\
Folate primarily helps the body make new cells, specifically by playing a role in copying and synthesizing DNA.\
It also helps the body utilize vitamin B12 and amino acids. A folate deficiency will cause anemia\
(poorly formed red blood cells), poor immune function, and poor digestion.\
For pregnant women a deficiency in folate can lead to neural tube defects such as spina bifida."


vitamin1 = Vitamin(name="Folate",  MinimumIntake="60 mg", user_id = User1.id, foodImageName="antioxidants.jpg", longDescription=folate_description, description="New Cells" )

session.add(vitamin1)
session.commit()


foodSource1 = FoodSource(name="Garbanzo Beans", description="",
                     serving="1/2 cup", amount="557 mcg", vitamin=vitamin1, user_id = User3.id)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="Liver", description="",
                     serving="3 oz", amount="22  mcg (55% dv)", vitamin=vitamin1,user_id = User3.id )

session.add(foodSource2)
session.commit()

foodSource3 = FoodSource(name="Pinto Beans", description="",
                     serving="1/2 cup", amount="146 mcg (37% dv)", vitamin=vitamin1, user_id = User3.id) 

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name="Lentils", description="",
                     serving="1/2 cup", amount="179 mcg (45% dv)", vitamin=vitamin1)

session.add(foodSource4)
session.commit()

foodSource2 = FoodSource(name="Spinach", description="",
                     serving="1 cup", amount="56 mcg", vitamin=vitamin1,user_id = User3.id )

session.add(foodSource2)
session.commit()


# New vitamin
vitamin1 = Vitamin(name="omega-3", MinimumIntake="60 mg", user_id = User1.id, foodImageName="omega-3.jpg"  )

session.add(vitamin1)
session.commit()

foodSource9 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1, user_id = User3.id )

session.add(foodSource9)
session.commit()


foodSource1 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1, user_id = User3.id )

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1, user_id = User3.id )

session.add(foodSource2)
session.commit()

foodSource3 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1, user_id = User3.id )

session.add(foodSource3)
session.commit()

foodSource4 = FoodSource(name=" ", description="",
                     serving="", amount="", vitamin=vitamin1, user_id = User3.id )

session.add(foodSource4)
session.commit()

foodSource2 = FoodSource(name=" ", description="",
                     serving="", amount="", vitamin=vitamin1,user_id = User3.id  )

session.add(foodSource2)
session.commit()

foodSource10 = FoodSource(name="", description="",
                      serving="", amount="", vitamin=vitamin1, user_id = User3.id )

session.add(foodSource10)
session.commit()


# Omega-3
vitamin1 = Vitamin(name="Omega-3",  MinimumIntake="60 mg", user_id = User1.id, foodImageName="vitD.jpg" )

session.add(vitamin1)
session.commit()


foodSource1 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1, user_id = User1.id)

session.add(foodSource1)
session.commit()

foodSource2 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1,user_id = User1.id )

session.add(foodSource2)
session.commit()


vitamin1 = Vitamin(name="Magnesium", MinimumIntake="60 mg", user_id = User1.id, foodImageName="magnesium.jpg"  )
session.add(vitamin1)
session.commit()

foodSource1 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1,user_id = User1.id )

session.add(foodSource1)
session.commit

foodSource1 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1,user_id = User1.id )

session.add(foodSource1)
session.commit()


foodSource1 = FoodSource(name="", description="",
                     serving="", amount="", vitamin=vitamin1, user_id = User1.id)

session.add(foodSource1)
session.commit()



                                                                                                                                                 

print "added menu items!"
