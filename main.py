import os
from time import sleep

fPreto = '\033[2;30m'
fBranco = '\033[1;97m'
fVermelho = '\033[1;91m'
fAzul = '\033[1;34m'
fAmarelo = '\033[1;33m'
fVerde = '\033[1;92m'
fCiano = '\033[1;36m'
fReset = '\033[m'

def tool():
    print(fVermelho + f"""
       __________
  {fVerde}<_______ /
   {fAzul}<______/  /(_
    {fAmarelo}<____<  ( __\\
     {fBranco}<____\  \ \\
     {fVermelho}<_____\\\_) )  {fReset}b3lial
    {fVerde}/          /
   {fAzul}/ /_|  )___/
  {fAmarelo}/ |  / /
 {fReset}/  |   \\\__
~~~~    (~~~)\n
01 {fCiano}> {fReset}sqlmap          07 {fCiano}> {fReset}Evil-Droid          99 {fCiano}> {fReset}exit
02 {fCiano}> {fReset}dotdotpwn       08 {fCiano}> {fReset}AdvPhishing
03 {fCiano}> {fReset}BlackWidow      09 {fCiano}> {fReset}slowloris
04 {fCiano}> {fReset}sherlock        10 {fCiano}> {fReset}One-Lin3r
05 {fCiano}> {fReset}BlackHydra      11 {fCiano}> {fReset}PwnXSS
06 {fCiano}> {fReset}track-ip        12 {fCiano}> {fReset}PhoneInfoga\n""")

def download():
    print(fVermelho + f"""
           __________
      {fVerde}<_______ /
       {fAzul}<______/  /(_
        {fAmarelo}<____<  ( __\\
         {fBranco}<____\  \ \\
         {fVermelho}<_____\\\_) )  {fReset}b3lial
        {fVerde}/          /
       {fAzul}/ /_|  )___/
      {fAmarelo}/ |  / /
     {fReset}/  |   \\\__
    ~~~~    (~~~)\n""")

def clear():
    os.system(["clear", "cls"][os.name == "nt"])

try:
    while True:
        clear()
        sleep(1)
        tool()
        insert = str(input(f"{fCiano}λ {fReset}"))
        if insert == "1" or insert == "01":
            clear()
            sleep(1)
            download()
            os.system(f"cd $HOME&&git clone https://github.com/sqlmapproject/sqlmap")
            input(f"\nPressione ENTER para voltar ")
        elif insert == "2" or insert == "02":
            clear()
            sleep(1)
            download()
            os.system(f"cd $HOME&&git clone https://github.com/wireghoul/dotdotpwn")
            input(f"\nPressione ENTER para voltar ")
        elif insert == "3" or insert == "03":
            clear()
            sleep(1)
            download()
            os.system(f"cd $HOME&&git clone https://github.com/1N3/BlackWidow")
            input(f"\nPressione ENTER para voltar ")
        elif insert == "4" or insert == "04":
            clear()
            sleep(1)
            download()
            os.system(f"cd $HOME&&git clone https://github.com/sherlock-project/sherlock")
            input(f"\nPressione ENTER para voltar ")
        elif insert == "5" or insert == "05":
            clear()
            sleep(1)
            download()
            os.system(f"cd $HOME&&git clone https://github.com/5l1v3r1/BlackHydra")
            input(f"\nPressione ENTER para voltar ")
        elif insert == "6" or insert == "06":
            clear()
            sleep(1)
            download()
            os.system(f"cd $HOME&&git clone https://github.com/htr-tech/track-ip")
            input(f"\nPressione ENTER para voltar ")
        elif insert == "7" or insert == "07":
            clear()
            sleep(1)
            download()
            os.system(f"cd $HOME&&git clone https://github.com/M4sc3r4n0/Evil-Droid")
            input(f"\nPressione ENTER para voltar ")
        elif insert == "8" or insert == "08":
            clear()
            sleep(1)
            download()
            os.system(f"cd $HOME&&git clone https://github.com/Ignitetch/AdvPhishing")
            input(f"\nPressione ENTER para voltar ")
        elif insert == "9" or insert == "09":
            clear()
            sleep(1)
            download()
            os.system(f"cd $HOME&&git clone https://github.com/gkbrk/slowloris")
            input(f"\nPressione ENTER para voltar ")
        elif insert == "10":
            clear()
            sleep(1)
            download()
            os.system(f"cd $HOME&&git clone https://github.com/D4Vinci/One-Lin3r")
            input(f"Pressione ENTER para voltar:")
        elif insert == "11":
            clear()
            sleep(1)
            download()
            os.system(f"cd $HOME&&git clone https://github.com/pwn0sec/PwnXSS")
            input(f"\nPressione ENTER para voltar ")
        elif insert == "12":
            clear()
            sleep(1)
            download()
            os.system(f"cd $HOME&&git clone https://github.com/ExpertAnonymous/PhoneInfoga")
            input(f"\nPressione ENTER para voltar ")
        elif insert == "99":
            print(f"Volte sempre.")
            break
        else:
            print(f"Opção inválida, tente novamente em 5 segundos...")
            sleep(5)

except KeyboardInterrupt:
    print(f"\nVolte sempre.")
