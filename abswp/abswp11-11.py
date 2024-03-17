import smtplib
conn = smtplib.SMTP('smtp-mail.outlook.com', 587)
print(type(conn))
print(conn)

print(conn.ehlo())
conn.starttls()

conn.login('jordan.fable711@gmail.com','puoulcnosbkvbedm')
print(conn.sendmail('jordan.fable711@gmail.com','jordan.fable711@gmail.com','\
Subject: so long...\n\n\ Dear jordan,\n this would be really cool if it worked\
first try.\n\n - Jordan'))
conn.quit()
print('done')

#my gmail didn't work, my outlook mail WOULD have worked, but hte school
#disabled it I think, which is totally fair

#wait nevermind, watch the rest of the video to find out how to make gmail work
#apparently it uses a different password
