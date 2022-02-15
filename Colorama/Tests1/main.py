from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
print("_______________________")
print('\033[36;42;1m' + 'some red text')
print('\033[39m') # and reset to default color