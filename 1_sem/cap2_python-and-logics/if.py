rm = input('Insert your RM')
age = input('Insert your age')

if int(age) >= 18:
    print('Your participation has been authorized, student RM {}'.format(rm))
    print('More information will be sent to your registered e-mail')
else:
    autorized = input('Do you have your parents authorization? Y-YES or N-NO')
    if autorized == 'Y':
        print('Your participation was authorized, student RM {}'.format(rm))
        print('More information will be sent to your parents e-mail')
    else:
        print('Your participation has been declined due to your age')