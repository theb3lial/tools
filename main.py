import os
import time

fPreto = '\033[2;30m'
fBranco = '\033[1;97m'
fVermelho = '\033[1;91m'
fAzul = '\033[1;34m'
fAmarelo = '\033[1;33m'
fVerde = '\033[1;92m'
fCiano = '\033[1;36m'
fReset = '\033[m'

def tool():
    print("""{}
       __________
  {}<_______ /
   {}<______/  /(_
    {}<____<  ( __\\
     {}<____\  \ \\
     {}<_____\\\_) )  {}b3lial
    {}/          /
   {}/ /_|  )___/
  {}/ |  / /
 {}/  |   \\\__
~~~~    (~~~)

01 {}> {}sqlmap          07 {}> {}Evil-Droid          99 {}> {}Exit
02 {}> {}dotdotpwn       08 {}> {}AdvPhishing
03 {}> {}BlackWidow      09 {}> {}slowloris
04 {}> {}sherlock        10 {}> {}One-Lin3r
05 {}> {}BlackHydra      11 {}> {}PwnXSS
06 {}> {}track-ip        12 {}> {}PhoneInfoga\n""".format(fVermelho, fVerde, fAzul, fAmarelo, fBranco, fVermelho, fReset, fVerde, fAzul, fAmarelo, fReset, fCiano, fReset, fCiano, fReset, fCiano, fReset, fCiano, fReset, fCiano, fReset, fCiano, fReset, fCiano, fReset, fCiano, fReset, fCiano, fReset, fCiano, fReset, fCiano, fReset, fCiano, fReset, fCiano, fReset))

def download():
    print("""{}
       __________
  {}<_______ /
   {}<______/  /(_
    {}<____<  ( __\\
     {}<____\  \ \\
     {}<_____\\\_) )  {}b3lial
    {}/          /
   {}/ /_|  )___/
  {}/ |  / /
 {}/  |   \\\__
~~~~    (~~~)\n""".format(fVermelho, fVerde, fAzul, fAmarelo, fBranco, fVermelho, fReset, fVerde, fAzul, fAmarelo, fReset))

def clear():
    os.system(["clear", "cls"][os.name == "nt"])

try:
    while True:
        clear()
        time.sleep(1)
        tool()
        insert = str(input("{}λ {}".format(fCiano, fReset)))
        if insert == "1" or insert == "01":
            clear()
            time.sleep(1)
            download()
            os.system("cd $HOME&&git clone https://github.com/sqlmapproject/sqlmap")
            input("\nPressione ENTER para voltar ")
        elif insert == "2" or insert == "02":
            clear()
            time.sleep(1)
            download()
            os.system("cd $HOME&&git clone https://github.com/wireghoul/dotdotpwn")
            input("\nPressione ENTER para voltar ")
        elif insert == "3" or insert == "03":
            clear()
            time.sleep(1)
            download()
            os.system("cd $HOME&&git clone https://github.com/1N3/BlackWidow")
            input("\nPressione ENTER para voltar ")
        elif insert == "4" or insert == "04":
            clear()
            time.sleep(1)
            download()
            os.system("cd $HOME&&git clone https://github.com/sherlock-project/sherlock")
            input("\nPressione ENTER para voltar ")
        elif insert == "5" or insert == "05":
            clear()
            time.sleep(1)
            download()
            os.system("cd $HOME&&git clone https://github.com/5l1v3r1/BlackHydra")
            input("\nPressione ENTER para voltar ")
        elif insert == "6" or insert == "06":
            clear()
            time.sleep(1)
            download()
            os.system("cd $HOME&&git clone https://github.com/htr-tech/track-ip")
            input("\nPressione ENTER para voltar ")
        elif insert == "7" or insert == "07":
            clear()
            time.sleep(1)
            download()
            os.system("cd $HOME&&git clone https://github.com/M4sc3r4n0/Evil-Droid")
            input("\nPressione ENTER para voltar ")
        elif insert == "8" or insert == "08":
            clear()
            time.sleep(1)
            download()
            os.system("cd $HOME&&git clone https://github.com/Ignitetch/AdvPhishing")
            input("\nPressione ENTER para voltar ")
        elif insert == "9" or insert == "09":
            clear()
            time.sleep(1)
            download()
            os.system("cd $HOME&&git clone https://github.com/gkbrk/slowloris")
            input("\nPressione ENTER para voltar ")
        elif insert == "10":
            clear()
            time.sleep(1)
            download()
            os.system("cd $HOME&&git clone https://github.com/D4Vinci/One-Lin3r")
            input("Pressione ENTER para voltar:")
        elif insert == "11":
            clear()
            time.sleep(1)
            download()
            os.system("cd $HOME&&git clone https://github.com/pwn0sec/PwnXSS")
            input("\nPressione ENTER para voltar ")
        elif insert == "12":
            clear()
            time.sleep(1)
            download()
            os.system("cd $HOME&&git clone https://github.com/ExpertAnonymous/PhoneInfoga")
            input("\nPressione ENTER para voltar ")
        elif insert == "99":
            print("Volte sempre.")
            break
        else:
            print("Opção inválida, tente novamente em 5 segundos...")
            time.sleep(5)

except KeyboardInterrupt:
    print("\nVolte sempre.")
