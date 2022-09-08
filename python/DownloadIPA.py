# from https://github.com/majd/ipatool/issues/71 and https://gist.github.com/spawn9275/6303053b0fae58d5b777e2c6d9192a2d

# waring: ipa from appstore is encrypted

# pip install requests xmltodict wget
import requests
import xmltodict
import wget

email = 'youremail'  # Replace with your email and password

password = 'yourpassword'

MAC = '##:##:##:##:##:##'  # Replace with MAC address from your iPhone

app_id = '1234567890'  # You can get this from https://apps.apple.com/us/app/{app-name}/id{app_id}

app_ver = '0'  # You can leave as 0, I used the value I got from the HTTP request

# ----------------------------------------------------------------------

guid = MAC.replace(':', '')

# We need to create a persisent session to keep cookies across requests
# https://stackoverflow.com/questions/12737740/python-requests-and-persistent-sessions
saved_session = requests.Session()

auth_params = {
    'appleId': email,
    'password': password,
    'attempt': '4',
    'createSession': 'true',
    'guid': guid,
    'rmp': '0',
    'why': 'signIn'
}

auth_headers = {
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Configurator/2.0 (Macintosh; OS X 10.12.6; 16G29) AppleWebKit/2603.3.8',
}

auth_url = 'https://p25-buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/authenticate?guid=%s' % guid

# Request it twice, the first one will result in a 302 response
auth = saved_session.post(url=auth_url, headers=auth_headers, data=auth_params)

code = input('Write 2FA code (6 number) (input enter to pass): ')
auth_params['password'] += code

auth = saved_session.post(url=auth_url, headers=auth_headers, data=auth_params)

# Parse as XML
dict_data = xmltodict.parse(auth.content)

# For strictly downloading, these 3 values aren't necessary, only DSID is.
# However, if you want to implement purchase, you need password_token and store_front
DSID = dict_data['plist']['dict']['string'][4]

# password_token = dict_data['plist']['dict']['string'][1]
# store_front = auth.headers.get('x-set-apple-store-front')

dl_url = 'https://p25-buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/volumeStoreDownloadProduct'

dl_body = {'creditDisplay': '', 'guid': guid, 'salableAdamId': app_id, 'appExtVrsId': app_ver}

dl_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Configurator/2.0 (Macintosh; OS X 10.12.6; 16G29) AppleWebKit/2603.3.8',
    'X-Dsid': DSID
}

dl_params = {'guid': guid}

dl = saved_session.post(url=dl_url, headers=dl_headers, params=dl_params, data=dl_body)

# https://stackoverflow.com/questions/2148119/how-to-convert-an-xml-string-to-a-dictionary
dl_dict = xmltodict.parse(dl.content)

# Retrieve the IPA URL from the XML we parsed
ipa = dl_dict['plist']['dict']['array'][1]['dict']['string'][0]

# https://stackoverflow.com/questions/24346872/python-equivalent-of-a-given-wget-command
# https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
# If the .ipa isn't installed yet, this will download it

filename = wget.download(ipa)
print(filename)
