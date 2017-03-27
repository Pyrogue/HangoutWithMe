#!/usr/bin/python3
#google hangouts bot targeted at the Raspberry Pi
#documentation: https://hangups.readthedocs.io/en/stable/
#extra reading: http://dabeaz.com/coroutines/

import hangups

tokenFile = "token"

cookies={}						#cookie dictionary
#login
try:
	cookies = hangups.get_auth_stdin(tokenFile)
except hangups.auth.GoogleAuthError:
	print("unable to authenticate")
	exit()

#setup environment
me = hangups.Client(cookies)	#get user
me.connect()					#connect to chat

#print whether pyro is availible
print(me.query_presence(["pyrogue6"]))


#get id
requestID=me.get_client_generated_id()

conversations = me.get_conversation(requestID)
print("conversations:")
print(conversations)
print("------------")

#build list of conversations and users
user = hangups.build_user_conversation_list(me)
print(user)

print(user.next())
# for u in user:
# 	print(u)
#print(users.get_all())

#disconnect
me.disconnect()