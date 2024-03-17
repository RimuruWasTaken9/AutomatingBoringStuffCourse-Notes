'''
none of this is gonna run, but I wanna write it down anyway
I'm uncommenting it incase it runs somehow anyway for now
'''
"""
import imapclient
conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('jordan.fable711@gmail.com','puoulcnosbkvbedm')
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['SINCE 20-Aug-2015'])
print(UIDs)

conn.fetch([47474],['BODY[]','FLAGS'])
#the 47474 comes from the UIDs variable, i assume its a
#specific code or number for a given email
import pyzmail
#pyzmail just won't import for some reason, at all, but I'll still add code
message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
message.get_subject()
#this code above returns the subject of the email

message.get_addresses('from')
#this code above gets the email address of the sender

message.text_part
#this code checks if there is any text part in the email

message.html_part == None
#this code checks if there is any html part in the email

message.text_part.get_payload().decode('UTF-8')
#this should give the text of the body of the email

message.text_part.charset
message.text_part.charset == None


conn.list_folders()
#this lists all the folders in the email, the name of the folder is gonna
#be the third value in each tuple

conn.select_folder('INBOX', readonly=False)

UIDs = conn.search(['ON 24-Aug-2015'])
UIDs

conn.delete_messages([47474]) #to delete one specific email
conn.delete_messages([UIDs]) #to delete all emails from specified date

"""
