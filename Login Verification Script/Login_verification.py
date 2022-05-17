import time as t

def stopwatch(sec):
    while sec:
        minn, secc = divmod(sec, 60)
        timeformat = '{:02d}:{:02d}'.format(minn, secc)
        print(timeformat, end='\r')
        t.sleep(1)
        sec -= 1

email = "user@gmail.com"
password = "1234*_*User"
attempts = 1
counter = 9

def login(attempts):
    while attempts <= 3:
        check_email = input("Enter email : ")
        check_pass = input("Enter password : ")
        if check_email == email and check_pass == password:
            print(">> Your log-in is successfully!\n")
            break
        elif check_email == email and check_pass != password:
            print(">> Your password is incorrect!\n")
        elif check_email != email and check_pass == password:
            print(">> Your email is incorrect!\n")
        else:
            print(">> Your email and password is incorrect!\n")
        attempts += 1

print('>> Welcome to \'Python Login Script\' Platform!, Follow next steps to access.\nNote: You have 10 attempts to login\nFor more info follow : https://github.com/aabertente/Simple-Life-with-Python\n')
## calling login function
login(attempts)
while counter >= 1:
    print('>> Your attempts to log in have expired, please try again in 3 minutes!\n')
    ## calling stopwatch function
    stopwatch(5)
    print('>> You have {} attempts to login\n'.format(counter))
    ## calling login function
    login(attempts)
    counter -= 1
print('>> If you can access this account, for more security measures you can contact the support team\n\'   Python Login Script\' by @aabertente.')