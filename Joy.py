from replit import web
from flask import *
import requests
import random
import json
from bs4 import BeautifulSoup
#@YassaHany
#@Style_Game

JoyYassa = Flask(__name__)

@JoyYassa.route('/')
def home_page():
    name = ('name')
    pss = "@YassaTeam"
    letters='1234567890qwertyuiopasdfghjklzxcvbnm'
    
    email=name+''.join(random.choice(letters) for i in range(5))+'@YassaTeam.SG'
    data={
    'gender':'male',
    'password':pss,
    'password_repeat':pss,
    'birth_month':'3',
    'birth_year':'2000',
    'creation_point':'client_mobile',
    'email':email,
    'birth_day':'8',
    'displayname':name,
    'key':'bff58e9698f40080ec4f9ad97a2f21e0',
    'platform':'iOS-ARM',
    'creation_flow':'mobile_email',
    'iagree':'1',
    }
    head={
    'content-type':'application/x-www-form-urlencoded',
    'Host':'spclient.wg.spotify.com',
    'Content-Type':'application/x-www-form-urlencoded',
    'Connection':'keep-alive',
    'Accept':'*/*',
    'User-Agent':'Spotify/8.5.7 iOS/13.5.1 (iPhone12,8)',
    'Accept-Language':'en, en;q=0.01',
    'Content-Length':'283',
    'Accept-Encoding':'gzip, deflate, br',
    }
 
    response=requests.post('https://spclient.wg.spotify.com/signup/public/v1/account',headers=head,data=data).json()
    print (email)
    print (pss)
    print (response)
    return {"email":email,"passowrd":pss,"By":"YassaHany&StyleGame"}
    

JoyYassa.run(host = '0.0.0.0')
