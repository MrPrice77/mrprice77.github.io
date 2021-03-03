profiles = [
    {
    'username' : 'gandalfTheGrey',
    'password' : 'noneShallPass!'
    },
    {'username' : 'gandalfTheBlack',
    'password' : 'someShallPass!'
    },
    {'username' : 'gandalfTheBlue',
    'password' : 'youShallPass!'
    },
    {'username' : 'gandalfTheGreen',
    'password' : 'theyShallPass!'
    },
    {'username' : 'iAmSmeagol',
    'password' : 'myPrecious!'
    }
]

def login(username_attempt, password_attempt, profile):
    '''Function check username and password attempt and returns whether True or False'''
    for profile in profiles:
        if username_attempt == profile['username'] and password_attempt == profile['password']:
            return True
    return False


def user_exists(create_un):
    '''Checks to see if username exists'''
    for profile in profiles:
        if create_un == profile['username']:
            return True

def create_user():
    '''Prompts user to create username and password'''
    print('Create User\n-----------')
    create_un = input('    Enter your new username: ')
    while True:
        user_exists(create_un)
        if user_exists(create_un) == True:
            print('\n    That username already exists!')
            create_un = input('    Enter your new username:\n    ')
        else:
            create_pw = input('    Enter your password:\n    ')
            print(f'\nThanks for signing up, {create_un}!.')
            profiles.append({'username' : create_un, 'password': create_pw})
            break
    

print('Welcome!')
try: # if integer of 1 or 2 not selected below, program will exit   
    choices = int(input('''
Please select from the following options:
    
    1. Create user
    2. Login

Enter the number of your choice: '''))

    if choices == 1: # sends user through create user cycle
        create_user()

    elif choices == 2: # sends user through login cycle
        print('Login:\n------\n')
        count = 3
        while True: # REPL that asks user if they want to create an account or log in. Checks username/password and loops if incorrect or already exists.

            username_attempt = input('    username: ') # User input for username
            password_attempt = input('    password: ') # User input for password
            
            profile = ''
            login_attempt = login(username_attempt, password_attempt, profile) # Shorter function for login

            if login_attempt == True:
                print(f'\nWelcome, {username_attempt}!') # Successful attempt ends the loop
                break
            elif login_attempt == False:
                print('\n    Error! Your username or password was incorrect!\n') # Prints failed attempt and loops back to user input
                count -= 1
                if count == 0:
                    print('\nYour login has been unsuccessful three times! Try again later. Goodbye!') # Three failed attempts closes the program
                    break
                if count > 0:
                    attempt_again = input("Enter 'y' to try again, 'n' to quit: ") # Asks user if they would like to try again upon failed login attempt
                    if attempt_again == 'y':
                        print(f'\nYou have {count} login attempt(s) remaining...\n') # Notifies user of number of attempts remaining

                    elif attempt_again == 'n':
                        print('\nGoodbye') # Tells the user goodbye if they do not want to attempt another login
                        break
except ValueError: # If ValueError, closes the program
    print('Incorrect input')
    exit()