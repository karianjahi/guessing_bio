import sys
from guessing_bio import GuessBio
arguments = sys.argv[1:]
if len(arguments) != 2:
    print("You have to provide two names separated by space")
else:
    results = GuessBio(arguments[0], arguments[1]).guess_bio()
    print("")
    print("")
    print(f'My names are {results["First name"]} {results["Last name"]}\nI '
          f'live in {results["address"]}\nYou can always reach me on mobile no: '
          f'{results["phone"]}\nor using the email address {results["email"]}')
    print("")
    print("")