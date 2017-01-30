from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Vitamin, FoodSource, User

# New imports for login session variable
from flask import session as login_session
import random
import string

#imports for client Secret manipulation
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests


app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Nutrient"


engine = create_engine('sqlite:///vitaminCatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/vitamin/<int:vitamin_id>/food/JSON')
def vitaminfoodJSON(vitamin_id):
    vitamin = session.query(vitamin).filter_by(id=vitamin_id).one()
    items = session.query(FoodSource).filter_by(
        vitamin_id=vitamin_id).all()
    return jsonify(FoodSources=[i.serialize for i in items])


@app.route('/vitamin/<int:vitamin_id>/food/<int:food_id>/JSON')
def FoodSourceJSON(vitamin_id, food_id):
    food_Item = session.query(FoodSource).filter_by(id=food_id).one()
    return jsonify(food_Item=food_Item.serialize)


@app.route('/vitamin/JSON')
def vitaminsJSON():
    vitamins = session.query(vitamin).all()
    return jsonify(vitamins=[r.serialize for r in vitamins])

# Show all vitamins
@app.route('/showvitaminboxes')
# def showVitaminboxes():
#     vitamins = session.query(Vitamin).all()
#     # return "This page will show all vitamins"
#     return render_template('index.html', vitamins=vitamins)

# Show all vitamins
# @app.route('/base')
# def base():
#     vitamins = session.query(Vitamin).all()
#     # return "This page will show all vitamins"
#     return render_template('base.html', vitamins=vitamins)

# This was example from FB developers page 
@app.route('/FB_login')
def googleAPI():
    return render_template('FB_login.html')

### MAIN HOME PAGE ### 
@app.route('/')
@app.route('/vitamindisplaycontent')
def vitamindisplaycontent():
    vitamins = session.query(Vitamin).all()
    # return "This page will show all vitamins"
    isAuthorized = 'true'
    if 'username' not in login_session:
        isAuthorized = 'false'
    return render_template('vitaminDisplayContent.html', vitamins=vitamins, authorized=isAuthorized)
   
# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


# Show all vitamins- old ugly page 
#@app.route('/')
@app.route('/vitamin/')
def showVitamins():
    vitamins = session.query(Vitamin).all()
    # return "This page will show all vitamins"
    return render_template('vitamins.html', vitamins=vitamins)


# Create a new vitamin
@app.route('/vitamin/new/', methods=['GET', 'POST'])
def newVitamin():
    if 'username' not in login_session:
        return redirect('login')
    if request.method == 'POST':
        user_id=getUserIDbyusername(login_session['username'] )
        newvitamin = Vitamin(name=request.form['name'], foodImageName="antioxidants.jpg", 
        user_id = user_id )
        session.add(newvitamin)
        session.commit()
        # url_for looks for a function 
        return redirect(url_for('vitamindisplaycontent'))
    else:
        return render_template('newVitamin.html')
    # return "This page will be for adding a new vitamin"


# Edit a vitamin
@app.route('/vitamin/<int:vitamin_id>/edit/', methods=['GET', 'POST'])
def editVitamin(vitamin_id):
    if 'username' not in login_session:
        return redirect('login')
    
    editedvitamin = session.query(
        Vitamin).filter_by(id=vitamin_id).one()
    if editedvitamin.user_id != login_session['user_id']:
        flash("you can not edit this vitamin because you did not create it")
        return redirect(url_for('vitamindisplaycontent'))
  
    if request.method == 'POST':
        if request.form['name']:
            editedvitamin.name = request.form['name']
            return redirect(url_for('showVitamins'))
    else:
        return render_template(
            'editVitamin.html', vitamin=editedvitamin)

    # return 'This page will be for editing vitamin %s' % vitamin_id


# Delete a vitamin
@app.route('/vitamin/<int:vitamin_id>/delete/', methods=['GET', 'POST'])
def deleteVitamin(vitamin_id):
    if 'username' not in login_session:
        return redirect('login')

    vitaminToDelete = session.query(
        Vitamin).filter_by(id=vitamin_id).one()
    if vitaminToDelete.user_id != login_session['user_id']:
        flash("you can not delete this vitamin because you did not create it")
        return redirect(url_for('vitamindisplaycontent'))
        
    if request.method == 'POST':
        session.delete(vitaminToDelete)
        session.commit()
        return redirect(
            url_for('vitamindisplaycontent', vitamin_id=vitamin_id))
    else:
        return render_template(
            'deleteVitamin.html', vitamin=vitaminToDelete)
    # return 'This page will be for deleting vitamin %s' % vitamin_id


# Show a vitamin FoodSources
@app.route('/vitamin/<int:vitamin_id>/')
@app.route('/vitamin/<int:vitamin_id>/food/')
def showVitamin(vitamin_id):
    vitamin = session.query(Vitamin).filter_by(id=vitamin_id).one()
    items = session.query(FoodSource).filter_by(
        vitamin_id=vitamin_id).all()
    isAuthorized = 'true'
    if 'username' not in login_session:
        isAuthorized = 'false'
    return render_template('vitamin.html', items=items, vitamin=vitamin, authorized=isAuthorized)
    # return 'This page is the food for vitamin %s' % vitamin_id


# Create a new food item
@app.route(
    '/vitamin/<int:vitamin_id>/food/new/', methods=['GET', 'POST'])
def newFoodSource(vitamin_id):
    if 'username' not in login_session:
        return redirect('login')
 
    if request.method == 'POST':
        user_id=getUserIDbyusername(login_session['username'] )
        
        newItem = FoodSource(name=request.form['name'], description=request.form[
                           'description'], serving=request.form['serving'], amount=request.form['amount'], vitamin_id=vitamin_id, user_id=user_id)
        session.add(newItem)
        session.commit()
        vitamin = session.query(Vitamin).filter_by(id=vitamin_id).one()
        return redirect(url_for('showVitamin', vitamin_id=vitamin_id))
    else:
        vitamin = session.query(Vitamin).filter_by(id=vitamin_id).one()
        return render_template('newFoodSource.html', vitamin_id=vitamin_id, vitamin=vitamin)

    return render_template('newFoodSource.html', vitamin_id=vitamin_id, vitamin=vitamin)
    # return 'This page is for making a new FoodSource for vitamin %s'
    # %vitamin_id


# Edit a food item
@app.route('/vitamin/<int:vitamin_id>/food/<int:food_id>/edit',
           methods=['GET', 'POST'])
def editFoodSource(vitamin_id, food_id):
    if 'username' not in login_session:
        return redirect('login')

    editedItem = session.query(FoodSource).filter_by(id=food_id).one()
    if editedItem.user_id != login_session['user_id']:
        flash("you can not edit this vitamin because you did not create it")
        return redirect(url_for('showVitamin', vitamin_id=vitamin_id))
    
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.serving = request.form['description']
        if request.form['serving']:
            editedItem.amount = request.form['serving']
        if request.form['amount']:
            editedItem.amount = request.form['amount']
   
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showVitamin', vitamin_id=vitamin_id))
    else:
        vitamin = session.query(Vitamin).filter_by(id=vitamin_id).one()
        return render_template(
            'editFoodSource.html', vitamin=vitamin, vitamin_id=vitamin_id, food_id=food_id, item=editedItem)

    # return 'This page is for editing food item %s' % food_id

# Delete a food item


@app.route('/vitamin/<int:vitamin_id>/food/<int:food_id>/delete',
           methods=['GET', 'POST'])
def deleteFoodSource(vitamin_id, food_id):
    if 'username' not in login_session:
        return redirect('login')

    itemToDelete = session.query(FoodSource).filter_by(id=food_id).one()
    if itemToDelete.user_id != login_session['user_id']:
        flash("you can not delete this vitamin because you did not create it")
        return redirect(url_for('showVitamin', vitamin_id=vitamin_id))
        
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showVitamin', vitamin_id=vitamin_id))
    else:
        return render_template('deleteFoodSource.html', vitamin_id=vitamin_id, item=itemToDelete)
    # return "This page is for deleting food item %s" % food_id


# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

def getUserIDbyusername(username):
    try:
        user = session.query(User).filter_by(username=username).one()
        return user.id
    except:
        return None


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            #del login_session['credentials']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('vitamindisplaycontent'))
    else:
        flash("You were not logged in")
    return 


#http://sean.lyn.ch/2011/07/android-the-facebook-sdk-sso-and-you/

@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token

    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
        app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API, changed from 2.4 1/23/17
    userinfo_url = "https://graph.facebook.com/v2.8/me"
    # strip expire tag from access token
    token = result.split("&")[0]


    url = 'https://graph.facebook.com/v2.4/me?%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # hote that failed because of app secret proof. Either set proof to no or include
    # sha 256 hash w/ request
    print "url sent for API access:%s"% url
    print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout, let's strip out the information before the equals sign in our token
    stored_token = token.split("=")[1]
    login_session['access_token'] = stored_token

    # Get user picture
    url = 'https://graph.facebook.com/v2.4/me/picture?%s&redirect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id,access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"






# gconnect

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output




@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] != '200':
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response





if __name__ == '__main__':
    app.secret_key = 'LetFoodBeThyMedicine'
    app.debug = True
    # threaded = true suggested as solution for slow localhost response, threaded=True, sql error
    app.run(host='0.0.0.0', port=5000 )
