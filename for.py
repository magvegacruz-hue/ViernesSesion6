from colorama import Fore, Style
for i in range(10):
  if i%2==0:
     print(Fore.GREEN + f"{i} es par." + Style.RESET_ALL)
  else:
     print(Fore.RED + f"{i} es impar." + Style.RESET_ALL)