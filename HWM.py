#!/usr/bin/python3.4
#google hangouts bot targeted at the Raspberry Pi
#documentation: https://hangups.readthedocs.io/en/stable/
#extra reading: http://dabeaz.com/coroutines/

import hangups
import asyncio	#for this future stuff... wow i have a lot to learn

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

# print(user.next())
# for u in user:
# 	print(u)
#print(users.get_all())


# for i in hangups.build_user_conversation_list(me):
# 	conversation_list = i
#-----------------------------------------------------------
# loop = asyncio.get_event_loop()
# task = loop.create_task(hangups.build_user_conversation_list(me))
# (ul,cl) = loop.run_until_complete(task)
# print()
# print("USER LIST:")
# print(ul)
# print("CONVERSATION LIST:")
# print(cl)
# print()
# USER LIST:
# <hangups.user.UserList object at 0x7f425db7a400>
# CONVERSATION LIST:
# <hangups.conversation.ConversationList object at 0x7f425dbb1390>
#-----------------------------------------------------------------


# user_list = [hangups.build_user_conversation_list(me)]
# print(hangups.build_user_conversation_list.__code__)
# user_list, conversation_list = (
#     hangups.build_user_conversation_list(me)
# )

# request = hangups.hangouts_pb2.GetSuggestedEntitiesRequest(
#         request_header=client.get_request_header(),
#         max_count=100,
# query_presence(query_presence_request)

#copy-pasta from docs... i am so lost
# def sync_recent_conversations(client, _):
#     user_list, conversation_list = (
#         yield from hangups.build_user_conversation_list(client)
#     )
#     all_users = user_list.get_all()
#     all_conversations = conversation_list.get_all(include_archived=True)

#     print('{} known users'.format(len(all_users)))
#     for user in all_users:
#         print('    {}: {}'.format(user.full_name, user.id_.gaia_id))

#     print('{} known conversations'.format(len(all_conversations)))
#     for conversation in all_conversations:
#         if conversation.name:
#             name = conversation.name
#         else:
#             name = 'Unnamed conversation ({})'.format(conversation.id_)
#         print('    {}'.format(name))

# sync_recent_conversations(me,"pyrogue6")

#disconnect
me.disconnect()