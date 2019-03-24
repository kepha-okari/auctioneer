# # works with both python 2 and 3
# from __future__ import print_function

# import africastalking

# class SMS:
#     def __init__(self):
# 		# Set your app credentials
#         self.username = "Nanda"
#         self.api_key = "ccd6a5c49876e24e7408a7f2d5f8d6e04a3a8d56f00d9920874ec94ff656d36b"


#         # apikey1 = '718f4eac92cbff832b403a8418673425c09c89dedf26a8f2eb68021d49aeb398'


#         # Initialize the SDK
#         africastalking.initialize(self.username, self.api_key)

#         # Get the SMS service
#         self.sms = africastalking.SMS

#     def send(self):
#             # Set the numbers you want to send to in international format
#             recipients = ["+254707630747"]

#             # Set your message
#             message = "I'm a lumberjack and it's ok, I sleep all night and I work all day";

#             # Set your shortCode or senderId
#             sender = "shortCode or senderId"
#             try:
# 				# Thats it, hit send and we'll take care of the rest.
#                 response = self.sms.send(message, recipients, sender)
#                 print (response)
#             except Exception as e:
#                 print ('Encountered an error while sending: %s' % str(e))

# if __name__ == '__main__':
#     SMS().send()



#     # to = user_contact
#     # message = 'This is a test message'

#     # gateway = AfricasTalkingGateway(username, apikey)

#     # try:
#     #     results = gateway.sendMessage(to, message)
#     #     for recipient in results:
#     #         print('number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
#     #                                                             recipient['status'],
#     #                                                             recipient['messageId'],
#     #                                                             recipient['cost']))
#     # except AfricasTalkingGatewayException as e:
#     #     print('Encountered an error while sending: %s' % str(e))

#     #     to = user_contact
# #     message = 'Congratulations '+ request.user.username.upper() +'for showing interest on my art work.\n' 'We will be able to tell the highest bid in the next '+ str(when)[:10] + ' at ' + str(when)[11:16]


# #     gateway = AfricasTalkingGateway(username, apikey)

# #     try:
# #         # Thats it, hit send and we'll take care of the rest.

# #         results = gateway.sendMessage(to, message)

# #         for recipient in results:
# #             # status is either "Success" or "error message"
# #             print('number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
# #                                                                 recipient['status'],
# #                                                                 recipient['messageId'],
# #                                                                 recipient['cost']))

# #     except AfricasTalkingGatewayException as e:
# #         print('Encountered an error while sending: %s' % str(e))


# # def schedule_bid(request, *args):

#     username = USERNAME
#     apikey = API_KEY
    
    
    


#     to = '+254707630747'
#     message = ' Hello Bidder'

#     gateway = AfricasTalkingGateway(username, apikey)

#     try:
#         # Thats it, hit send and we'll take care of the rest.

#         results = gateway.sendMessage(to, message)

#         for recipient in results:
#             # status is either "Success" or "error message"
#             print('number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
#                                                                 recipient['status'],
#                                                                 recipient['messageId'],
#                                                                 recipient['cost']))

#     except AfricasTalkingGatewayException as e:
#         print('Encountered an error while sending: %s' % str(e))





# def send_message(request, **args):
#     username = config.USERNAME
    
#     api_key = config.API_KEY
    
#     message = "You posted"
   
#     africastalking.initialize(username, api_key)
    
#     sms = africastalking.sms
   
#     response = sms.send(message, '0707630747')