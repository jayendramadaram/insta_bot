

from selenium import webdriver
import time
import random


print("started")

start= [" hey there " , "yo guys" ,"hola people" , "ohiyo buddies"," hi guys ",
         " hola guys " , "yo dev" , " hey dev " , "hello coders " ,"yo dev"
         "hi dev", "hey programmers" , "hola dev"]

msg = ["wazzup hows life going" , "hows everything" ,"hope you are doing well" , "hope you are doing awesome"]

msg1 = ["we are part of @development_fam"]

msg2 = ["we post stuff daily on development and machine-learning stuff "]

msg31 = ["infact" 'honestly' , 'tbh' , 'actually' ]
msg32 = ['this comment is']
msg33 = ['automanted with python bot' , 'automanted with help of python bot']
msg34 = ['join us or dm us we will make your life easy with programming']


msg4 = ["follow @development_fam"]



msg51 =  ["tag", "mention" ,'tagg' 'taggg']
msg52 = ['your']
msg53 =  ['friends' , 'colleagues','comrades' ,'co-developers/friends']
msg54 = ['here','over here'  ] 


msg6 = ["we personally design our posts to train you everyday we provide lots of free high class free learning resources"]

msg7 = ['join our growing community']

msg8= ["\n"]


from instaclient import InstaClient
from instaclient.errors.common import *

client = InstaClient(driver_path='C:\webdrivers\chromedriver.exe')

try:
  client.login(username='perfect_pybot', password='********')
except  VerificationCodeNecessary:
  code = input('Enter your 2FA security code here: ')
  client.input_security_code(code)

username = input('Enter an instagram account\'s username to send dms to their followers ')
try:
  followers = client.get_followers(user=username, count=3, callback_frequency=15)

  req = []
  for i in followers[0]:req.append(i.username)


    
except InvalidUserError:print('The username is not valid')
except PrivateAccountError:print('{} is a private account'.format(username))



run = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
run.get("https://www.instagram.com")

# perfect_assistance

time.sleep(8)
logs = run.find_element_by_name("username")
logs.click()
logs.send_keys('perfect_pybot') 
logs = run.find_element_by_name("password")
logs.click()
logs.send_keys("******")
logs = run.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
logs.click()
print("1")
time.sleep(3)
logg = run.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
logg.click()
run.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()


print("...........sending DM*s ...............")
print("...........sending DM*s ...............")
print("...........sending DM*s ...............")

for i in req:
    print(i)
    cmnt = str(random.choice(start) +" "  + random.choice(msg)+" " + random.choice(msg1)+" " + random.choice(msg2))
    #" " + random.choice(msg31)+" " + random.choice(msg32)+" "+ random.choice(msg33)+" "+ random.choice(msg34)+" "+ random.choice(msg8)+" "+ random.choice(msg8)+" "+ random.choice(msg8)+" "+ random.choice(msg4)+" "+ random.choice(msg51)+" "+ random.choice(msg52)+" " + random.choice(msg53)+" "+ random.choice(msg54)+" "+ random.choice(msg6) +" "+ random.choice(msg7)




    run.get("https://www.instagram.com/direct/inbox/")
    time.sleep(2)

    logs = run.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div')
    logs.click()

    logs = run.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
    time.sleep(2)
    try:logs = run.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div[1]').click()
    except:print("****commented_sucessfully********")
    time.sleep(2)
    logs = run.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button/div')
    logs.click()
    time.sleep(4)
    run.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(cmnt)
    time.sleep(2)
    run.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
    print('.......dm sent......' , "to " ,i)





print("...........sending comments ...............")
print("...........sending comments ...............")
print("...........sending comments ...............")






run.get("https://www.instagram.com/explore/tags/programming/")

logs = run.find_elements_by_tag_name('a')
logs = [i.get_attribute('href') for i in logs]
print(logs)
print('\n\n\n\n')
print("...........sending comments ...............")
print("...........sending comments ...............")
print("...........sending comments ...............")
for link in logs:
    # input()
    run.get(link.strip())

    cmnt = str(random.choice(start) +" "  + random.choice(msg)+" " + random.choice(msg1)+" " + random.choice(msg2)+" " + random.choice(msg31)+" " + random.choice(msg32)+" "+ random.choice(msg33)+" "+ random.choice(msg34)+" "+ random.choice(msg8)+" "+ random.choice(msg8)+" "+ random.choice(msg8)+" "+ random.choice(msg4)+" "+ random.choice(msg51)+" "+ random.choice(msg52)+" " + random.choice(msg53)+" "+ random.choice(msg54)+" "+ random.choice(msg6) +" "+ random.choice(msg7))
    time.sleep(3)

    try:
        run.find_element_by_class_name('RxpZH').click() 
    except:
        continue
    time.sleep(1)
    run.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(cmnt)
    time.sleep(5)
    try:
        run.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]").click()
    except:
        print(".COMMENTED ON POST...........")
        time.sleep(5)
        continue



















#   










































































