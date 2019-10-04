# importando módulos
import tweepy
from auth import *

# Autenticando usuário
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Autenticando Token
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# tweet
api.update_status(status =" Teste, está funcionando!")
