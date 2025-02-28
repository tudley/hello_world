from .weather import weather
print("Hello world")
print("lets make a change after staging the initial version of this file!")
print('making a small change and committing without staging')
name = input('whats your name? ')
print('nice to meet you, ' + name)
good_day = input('are you having a nice day (y/n)? ')
if good_day == 'y':
    print('i am glad to hear it')
elif good_day == 'n':
    print('i am sorry to hear it')
else:
    print('i didnt understand your response. O hope you;re having a good day')

temp = int(input("what is the temo where you are?"))
weather(temp)