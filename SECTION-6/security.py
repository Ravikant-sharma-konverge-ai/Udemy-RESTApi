from hmac import compare_digest
from models.User import UserModel #our own created file

#users = [
    #{
        #'id' : 1,
        #'username':'bob',
        #'password':'asdf'
    #}
#]
#users = [
    #User(1,'bob','asdf')

#]    
#username_mapping = {'bob':{
        #'id':1,
        #'username':'bob',
        #'password':'asdf'
    #}
#}
#username_mapping = {u.username: u for u in users}

#userid_mapping = {1:{
        #'id':1,
        #'username': 'bob',
        #'password': 'asdf'
    #}
#}
#userid_mapping = {u.id: u for u in users}


def authenticate(username,password):  # this is basically to compare the username and password of a user and send back the access token by JWT
    user = UserModel.find_by_username(username)
    if user and compare_digest(user.password,password): 
        return user

def identity(payload):               # this function is basically for veryfring the identity in the token to keep checking that user has logged in earlier , means this will use the token given by the authenticate function to use on every request so that don't have tp log in every time.
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
    

