import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']



if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
        #^^don't want mapit.py
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#webbrowser.open('https://youtube.com')

#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)


#new lesson
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)

len(res.text)
print(res.text[:200])

res.raise_for_status()
badRes = requests.get('http://automateboredtofinish.com')
print(badRes.raise_for_status)
