from colorama import Fore, Style

# Creation of dicts
a = dict(one=1, two=2, three=3)
print(Style.BRIGHT + Fore.CYAN, "a is", Fore.WHITE + Style.RESET_ALL, a)

b = {'one': 1, 'two': 2, 'three': 3}
print(Style.BRIGHT + Fore.CYAN, "b is", Fore.WHITE + Style.RESET_ALL, b)

c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(Style.BRIGHT + Fore.CYAN, "c is", Fore.WHITE + Style.RESET_ALL, c)

d = dict([['one', 1], ['two', 2], ['three', 3]])
print(Style.BRIGHT + Fore.CYAN, "d is", Fore.WHITE + Style.RESET_ALL, d)
