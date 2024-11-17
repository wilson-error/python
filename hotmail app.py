


print('welcome to hotmail service ')
print('have you ever created an email account')
print('1.yes, I have an email account')
print('2.I have never created an email account before')
a = int(input())
if a == 2:
    print('now you can create your very first email.')
    r = input('please enter your email name , at least 1 letter and 1 number:  ')
    print()
    print('you are all set, your email account is',r,end = '@hotmail.com')
    print()
    print('you have successfully created your account, now proceed the login in your browser.')
   
elif a == 1:
    print('Proceeded the login protocol in your browser')




print()





jkl = [1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
aaccc = ['is officially the end of windows10','the Spring fair activity is coming soon!',"dad's business went well, I want you to come back and see dad",'another device logged into your Hotmail account','a new game called hero wars has been made, click the link to play']


print('this is the login page,enter your Hotmail account to get started with Hotmail!')
b = input('input name only, do not input @hotmail.com: ')

print('you have successfully logged in your Hotmail account. now , you can start using it.')
strq = b

def home_screen():
    print('welcome back to Hotmail!!!')
    print("your email account is", strq ,end = '@hotmail.com')
    print()
    print('h = Home screen')
    print('i = inbox')
    print('c = Composer')
    print('q = quit')
    print('a = account settings')
    a = input()
    if a == 'h':
        home_screen()
    elif a =='i':
        import random
        wer = random.choice(jkl)
        print('you have',wer,'email in your inbox')
        print()
        print('do you want to delete all your emails?')
        print('f = delete all')
        print('j = Read the emails')
        a1234 = input()
        if a1234 == 'f':
            print('all of the emails has been deleted, enjoy your inbox 0')
            import time
            time.sleep(10)
            home_screen()
        else:
            for _ in range(wer):
                a1234 = random.choice(aaccc)
                print(a1234)
            print('do you want to delete all your emails?')
            print('d = Delete all')
            print('k = Keep')
            d = input()
            if d == 'd':
                print('enjoy your inbox 0')
                import time
                time.sleep(10)
                home_screen()
            else:
                print("you don't always have to have an empty inbox")
                import time
                time.sleep(5)
                home_screen()
                
    elif a == 'c':
        print('s = send email')
        t = input('To:')
        s = input('subject: ')
        n = input('input s To send the email: ')
        if n == 's':
            print('email sent')
            import time
            time.sleep(5)
            home_screen()
    elif a == 'q':
        print('you have forced hotmail to quit')

    elif a == 'a':
        print('c = change email')
        print('l = Log out ')
        print('x = Close account')
        iiir = input()
        if iiir == "c":
            print('do you want to change your email? , You will Open a new account and all of your history will not sync unless you import data')
            print('f = yes')
            print('j = no')
            f12 = input()
            if f12 == 'f':
                r = input('please enter your new email name , at least 1 letter and 1 number:  ')
                print()
                print('you are all set, your email account is',r,end = '@hotmail.com')
                print()
                print('you have successfully created your account, now proceed the login in your browser.')


                print('this is the login page,enter your Hotmail account to get started with Hotmail!')
                b = input('input name only, do not input @hotmail.com: ')

                print('you have successfully logged in your Hotmail account. now , you can start using it.')
                print()
                 
                

                print('do you need to import data?')
                print('i = Import')
                jjkk11 = input()
                if jjkk11 == 'i':
                    print('importing your data (^_^)')
                    import time
                    time.sleep(15)
                    home_screen()
            else:
                time.sleep(5)
                home_screen()


        if iiir == 'l':
            print('are you sure you want to logout, you can login again to Use hotmail')
            print('f = yes')
            print('j = no')
            f12 = input()
            if f12 == 'f':
                print('you have logged out successfully, sign in again to start using your Hotmail.')
                print('this is the login page,enter your Hotmail account to get started with Hotmail!')
                b = input('input name only, do not input @hotmail.com: ')

                print('you have successfully logged in your Hotmail account. now , you can start using it.')
                print()

                
                home_screen()
            else:
                time.sleep(5)
                home_screen()
        if iiir == 'x':
            print('if you close your Hotmail account, you will be logged out from all devices linked to your Hotmail account, you cannot import any data from your old account')
            print('f = yes')
            print('j = no')
            tttt11 = input()
            if tttt11== 'f':
                print('you have closed your Hotmail account, create a new one to start using Hotmail')
                r = input('please enter your new email name , at least 1 letter and 1 number:  ')
                print()
                print('you are all set, your email account is',r,end = '@hotmail.com')
                print()
                print('you have successfully created your account, now proceed the login in your browser.')


                print('this is the login page,enter your Hotmail account to get started with Hotmail!')
                b = input('input name only, do not input @hotmail.com: ')

                print('you have successfully logged in your Hotmail account. now , you can start using it.')
                print()
                
                
                import time
                time.sleep(5)
                home_screen()











home_screen()
