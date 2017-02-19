# -*- coding: utf-8 -*-
import time
import string
import requests
from bs4 import BeautifulSoup
import sys
from Config import *
import random


filename = raw_input("[+]Enter the filename to save the usernames to (IE userlist.txt): ")
try:
    accountlist = open(filename,'w')
except IOError:
    sys.exit("[-]Invalid filename!")

while 1:
    with requests.Session() as c:
            signup_post       = 'https://manager.linode.com/session/signup_save'
            signup_page       = 'https://manager.linode.com/session/signup'
    
            EMAIL             = raw_input("[+]Enter email address: or q to quit")
            if EMAIL == 'q':
                sys.exit("[-]Recieved q command, quitting")
            else:
                pass
            PASSWORD          = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(10))
            USERNAME          = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(6))
                        
            print "password: "    +str(PASSWORD)
            print "email: "       +str(EMAIL)
            print "username: "    +str(USERNAME)    
    
            c.get(signup_page)
            SESS_ID = c.cookies['SESSION_ID']
                
            reg_data = dict(email = EMAIL, password = PASSWORD,username = USERNAME )
            regpost = c.post(signup_post, data=reg_data, headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36","X-Requested-With":'XMLHttpRequest','SESSION_ID':SESS_ID })
        
            emailpage = c.get('https://manager.linode.com/session/signup_email').content
               
            if 'Almost there!' in str(emailpage):
                print "[+]Account creation successful\n"
                accountlist.write(USERNAME+":"+EMAIL+":"+PASSWORD+'\n')
            else:
                print '[-]Unsuccessful during account creation\n'
                pass
            
accountlist.close()