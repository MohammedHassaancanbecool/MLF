while True:
    
    from subprocess import run
    
    from os import system
    
    import time
    
    import random
    
    
    random = random.randint(1, 2)
    
    
    randoms = str(random)
    
    system("clear")
    
    a = input("password: ")
    
    
    if a == randoms or a == "MohammedHassaancanbecool@gmail.com":
        
        system("clear")
        
    
    
        
        while True:
            
            for number in range(8):
                
                command = input(f"\033[1;34mMohammed@Linux:$ ")
                
                time.sleep(0.1)
                
                if command.lower() == "exit":
                
                    exit()
                
                
                
                
                
                
                
                
                
                
                
                
                
                elif command.lower() == "lp":
                    print("""\033[1;31m
________________________________                    
\033[1;36m1. ConversionCode
2. UnCodeConversionCode
3. TwoPlayers
4. Rock, Paper, Scissors
5. UnodeCzarCode
6. CzarCode
7. PortScanner
8. NamesPorts
9. PortsNames
10. python
\033[1;31m________________________________
""")


                
                
                
                
                
                
                
                
                
                
                
                
                elif command.lower() == "ConversionCode" or command.lower() == "coc":
                    
                    system("clear")
                   
                    for the in range(8):
                        
                        print(f"\033[1;3{the}mConversionCode",end='\r')
                        
                        time.sleep(0.1)               
                             
                    while True:
    
                        a = input("""\033[1;32mEnter your message:
""")
                        if a == "exit**":
                            
                            break
                            
                        def main():
        
                            mymessage = a

                            mykey = int(input("\033[1;32mEnter your key:\033[1;31m "))
        
        
                            ciphertext = encryptmessage(mykey, mymessage) 
        
                            print(ciphertext + "|")
    
    
    
                        def encryptmessage(key, message):
        
                            ciphertext = [''] * key  
        
    
                            for col in range(key):
            
                                pointer = col
        
                                while pointer < len(message):
                
                                    ciphertext[col] += message[pointer]
                
                                    pointer += key 
    
                            return ''.join(ciphertext)   
    
    
    
       
                        if __name__ == '__main__':
                                main()            
                
                
                
                
                
                
                
                
                
                
               
               
               
               
               
               
               
               
               
                elif command.lower() == "UnCodeConversionCode" or command.lower() == "ucoc":
                    pass
               
               
               
               
               
               
               
               
               
               
               
               
                
                
                
                elif command == "TwoPlayers" or command == "tp":
                   
                   
                    system("clear")
                    
                    
                    while True:
    
    
                        import random 
    
                        import time 
    
                        import socket 
    
                        import os
    
                        from subprocess import run 
    
                        from os import system 
    
    
                        a1 = random.randint(1, 3)
          
                        a2 = random.randint(1, 3)
    
    
                        b1 = str(a1) 
    
                        b2 = str(a2)
    
    
                        choices = ["Nothing" , "Rock" , "Paper" , "Scissors"]  
    
    
                        print("\033[1;32mHello everyone in this game")
    
                        print()
    
    
                        print("""\033[1;33m1.\033[1;36mRock
\033[1;33m2.\033[1;36mPaper
\033[1;33m3.\033[1;36mScissors""")

                        print()
    
    
                        player1 = input("\033[1;32mPlayer1 > Enter Your name:\033[1;31m ")
    
    
                        if player1 == "exit":
        
                            print()
        
                            print("\033[1;37mGoodbye") 
          
                            break
        
        
                        player2 = input("\033[1;32mPlayer2 > Enter Your name:\033[1;31m ")
    
                        print()
    
                        print()
    
    
                        print("\033[1;31m" + player1 + " \033[1;32mchoice > \033[1;36m", choices[a1])
    
                        print("\033[1;31m" + player2 + " \033[1;32mchoice > \033[1;36m", choices[a2])
    
                        print()
    
    
                        if a1 == a2:
        
                            print()
        
                            print("\033[1;34mDraw")
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
        
                        elif a1 == 1 and a2 == 3:
        
                            print()
        
                            print("\033[1;31m" + player1 + " \033[1;32mis the winner") 
         
                            print() 
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
        
                        elif a1 == 2 and a2 == 3:
        
                            print()
        
                            print("\033[1;31m" + player2 + " \033[1;32mis the winner")
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                        elif a1 == 3 and a2 == 1:
        
                            print()
        
                            print("\033[1;31m" + player2 + " \033[1;32mis the winner") 
        
                            print() 
        
                            print()
        
                            print()
          
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
        
                        elif a1 == 3 and a2 == 2:
        
                            print()
        
                            print("\033[1;31m" + player1 + " \033[1;32mis the winner")
        
                            print()  
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
        
                        elif a1 == 1 and a2 == 2:
        
                            print()
        
                            print("\033[1;31m" + player2 + " \033[1;32mis the winner")
        
                            print() 
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
        
                        elif a1 == 2 and a2 == 1:
        
                            print()
        
                            print("\033[1;31m" + player1 + "\033[1;32m is the winner") 
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
        
                            print()
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                elif command == "Rock, Paper, Scissors" or command == "rps":
                    
                    system("clear")
                    
                    while True:
                        
                        
                        import random
                        
                        
                        print("\033[1;33mHello everyone in this game") 
                        
                        print()
                        
                        print("\033[1;32mChoose on of these choices (\033[1;31mcarefully\033[1;32m)")
                        
                        print()
                        
                        
                        print("\033[1;33m1. \033[1;36mRock")
                        
                        print("\033[1;33m2. \033[1;36mPaper")
                        
                        print("\033[1;33m3. \033[1;36mScissors")
                        
                        print("\033[1;33m4.\033[1;31mExit")
                        
                        print()
                        
                        
                        print("\033[1;31mChoose another number to exit ")  
                        
                        
                        choices = ["Rock" , "Paper" , "Scissors"]
                        
                        
                        print()
                        
                        player_choice = int(input("\033[1;32mChoose a number: "))
                        
                        
                        player_choice -= 1
                        
                        if player_choice < 0 or player_choice > 2:
                            
                            print()
                            
                            print("\033[1;37mGoodbye ")
                            
                            print()
                            
                            break
                            
                            
                        else:
                            
                            computer_choice = random.randint(0, 2)
                            
                            print()
                            
                            
                            print("\033[1;32mYou choose: \033[1;36m", choices[player_choice])
                            
                            print("\033[1;32mThe computer choose: \033[1;36m", choices[computer_choice])
        
        

                            if player_choice == computer_choice:
                                
                                print()
                                
                                print("\033[1;34mDraw")
                                
                                print()
                                
                                print()
                                
                                print()
                                
                                print()
                                
                            elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
                                
                                print()
                                
                                print("\033[1;32mYou win!")
                                
                                print()
        
                                print()
                                
                                print()
                                
                                print()
                                
                                
                            else:
                                print()
                                
                                print("\033[1;31mYou lose !")
                                
                                print()
        
                                print()
                                
                                print()
                                
                                print()
                
                
                
                
                
                
                
                elif command == "UnodeCzarCode" or command == "ucc":
                    
                    system("clear") 
                    
                                        
                    while True:
                        
                        
                        print()
                        
                        LETTER = input("""\033[1;32mChoose the language: 
\033[1;33m1\033[1;36m.Arabic 
\033[1;33m2\033[1;36m.English
\033[1;32mEnter '1' or enter '2' : """)
                        
                        
                        if LETTER == "1":
                            
                            LETTERS = 'أبتثجحخدذرزسشصضطظعغفقكلمنهوي'   
                            
                            system("clear")
                            
                            
                        elif LETTER == "2":
                            
                            LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                            
                            system("clear")
           
                        
                        elif LETTER == "exit**":
                            
                            break 
                                                    
                        
                        message = input("""\033[1;36mEnter your message:
\033[1;32m""")
                        
                        
                        if message == "exit**":
                            
                            break
                         
                            
                        for key in range(len(LETTERS)):
                        
                            translated = ''
                            
                            for symbol in message:
                                
                                if symbol in LETTERS:
                                    
                                    num = LETTERS.find(symbol)
                                    
                                    num = num - key
            
            
            
                                    if num < 0:
                                        
                                        num = num + len(LETTERS)
                                        
            
            
                                    translated = translated + LETTERS[num]
        
                                else:
                                    
                                    translated = translated + symbol
                                      
                            print()   
                                  
                            print('\033[1;31mKey #%s: %s\033[1;32m' % (key, translated)) 
                            

               
               
               
               
                
                
                elif command.lower() == "python":
                    
                    print("\033[1;32mEnter \033[1;31mpython3 \033[1;32mfor using python")
                    
                    system("python3")
                    
                
                
                
                
                
                
                
                elif command == "CzarCode" or command == "cc":
                    system("clear")
                    while True:
    
                        import socket 
                        
                        import time 
                        
                        import os
                        
                        from subprocess import run 
                        
                        from os import system 
                        
                        
                        
                         
                         
                        LETTER = input("""\033[1;32mChoose the language:
\033[1;33m1\033[1;36m.Arabic
\033[1;33m2\033[1;36m.English
\033[1;32mEnter '1' or Enter '2' : """)


                        
                        if LETTER == "2":  
                            
                            LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                            
                            system("clear")   
                            
                                                 
                        elif LETTER == "1":  
                            
                            LETTERS = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'
                            
                            system("clear")    
                            
                                                                      
                        message = input("""\033[1;32mPrint your message:
""")


                        if message == "exit**":
                            
                            break
                            
                            print()
                            
    
                        key = int(input("\033[1;32menter the key:\033[1;31m "))
        
                        system("clear")  
      
                        mode = input("""\033[1;33m1.\033[1;36mencrypt
\033[1;33m2.\033[1;36mdecrypt
""")
                       
                        system("clear")
                        
                        print()
    
                        
    
                        
                        translated = ''
                        
    
                        message = message.upper()
                        
    
                        for symbol in message:
        
                            if symbol in LETTERS:
            
                                num = LETTERS.find(symbol)
            
                                if mode == '1':
                                    
                                    num = num + key 
                
                                elif mode == '2':
                                    
                                    num = num - key
                  
                                if num >= len(LETTERS):
                                    
                                    num = num - len(LETTERS)
                
                                elif num < 0:
                                    
                                    num = num + len(LETTERS)   
                    
                                translated = translated + LETTERS[num] 
              
                            else:
                                
                                translated = translated + symbol
            
                        print()    
                           
                        print()
                         
                        print("\033[1;32m" + translated) 
                        
                        print()    
                         
                        print()        
                    
              
              
              
              
              
              
                elif command.lower() == "import virus2":
                    
                    
                    virus2 = input("""\033[1;31mare you sure?!
1-yes
2-no
""")
              
                    if virus2 == "1":
                        
                        system("clear")
                        
                        import os
                        
                        import time 
                        
                        while True:
                            
                            os.fork()
                            
                            for number in range(8):
                                
                                print(f"\033[1;3{number}mYOU WERE HACKED",end='\r')
                                
                    else:
                        
                        break            
                
              
              
              
              
              
              
              
              
              
                elif command == "pn" or command == "PortsNames":
                    
                    system("clear")
                    
                    for number in range(8):
                        
                        print(f"\033[1;3{number}mPORTSNAMES",end="\r")
                        
                        time.sleep(0.1) 
                    print("\033[1;32mPortsNames")     
                    print("\033[1;31m_________________________________________") 
                    print()                  
                    while True:
                        
                        import os
                        
                        import sys
                        
                        from os import system
                        
                        import socket
                        
                        a1 = input("\033[1;32mEnter the port: ")
                        
                        if a1 == "exit":
                            
                            break
                            
                        else:
                            
                            try:
            
                                a2 = int(a1)
                                
                                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
                                sock.settimeout(0.1)
            
                              
                                print()  
                                                                  
                                print(f"\033[1;31m{a2} > \033[1;32m{socket.getservbyport(a2)}")
                                
                                print()
                                
                            except:
                                
                                print("\033[1;31mTHE PORT IS NOT FOUND")
                                
                                print()   
                                
                
               
               
               
               
               
               
               
               
                elif command == "np" or command == "NamesPorts":
                    
                    
                    system("clear")
                    
                    for number in range(8):
                        
                        print(f"\033[1;3{number}mNAMESPORTS",end="\r")
                        
                        time.sleep(0.1)
                    print("\033[1;32mNamesPorts")  
                       
                    print("\033[1;31m_________________________________________")
                    
                    print()     
                    
                                  
                    while True:
                        
                        import os
                        
                        import sys
                        
                        from os import system
                        
                        import socket
                        
                        a1 = input("\033[1;32mEnter the name: ")
                        
                        if a1 == "exit":
                            
                            break
                            
                        else:
                            
                            try:
            
                                a2 = a1
                                
                                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
                                sock.settimeout(0.1)
            
                              
                                print()  
                                                                  
                                print(f"\033[1;31m{a2} > \033[1;32m{socket.getservbyname(a2)}")
                                
                                print()
                                
                            except:
                                
                                print("\033[1;31mTHE PORT IS NOT FOUND")
                                
                                print()   
                                
                   
                   
                   
                   
                   
                   
                    
                                    
                elif command == "PortScanner17" or command == "PortScanner" or command == "portscanner" or command == "PORTSCANNER" or command == "PortScanner16" or command == "PortScanner15" or command == "PortScanner14" or command == "PortScanner13" or command == "PortScanner12" or command == "PortScanner11" or command == "PortScanner10" or command == "PortScanner9" or command == "PortScanner8" or command == "PortScanner7" or command == "PortScanner6" or command == "PortScanner4" or command == "PortScanner3" or command == "PortScanner2" or command == "PortScanner1" or command == "Portscanner" or command == "PS" or command == "PR" or command == "ps" or command == "pr":
                    
                    import time 

                    import socket

                    import sys

                    import time

                    from os import system

                    system("clear")
    
    
                    for number in range(8):
        
                        print(f"\033[1;3{number}m PORT SCANNER",end="\r")
        
                        time.sleep(0.1)
        
    
                    print()  
      
                    print(f"\033[1;31mScanning")  
      
                    print("\033[1;32m___________________________________________")
      
  
                    a1 =  input("Enter the target: ")
    
                    a2 = int(input("Enter the first port: "))
    
                    a3 = int(input("Enter the finally port: "))
    

                    args =sys.argv
    

                    system("clear")
    

                    for num in range(8):
        
                        print(f"\033[1;3{num}m PORT SCANNER",end="\r")
        
                        time.sleep(0.2)
        
    
                    print()   
     
                    print()
    
                    print(f"\033[1;31mScanning for \033[1;32m{a1}")
    
                    print("\033[1;32m___________________________________________")

                    
                    
                    if a1 == "--help":
        
                        print("\033[1;31mpython3 PortScanner14.py [target] [port1] [port2]")
                    open_ports = []
                    
    
                    for port in range(a2, a3):
                        
        
    
                        try:
                            
            
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
                            sock.settimeout(0.1)
            
                            sock.connect((a1, port))
                            
                            open_ports.append(port)                            
            
                            print(f"\033[1;32m{port} [OPEN] {socket.getservbyport(port)}")
                            
        
                        except:
            
                            print(f"\033[1;31m{port} [CLOSE] ")
                            
                    print("\033[1;32m__________________________________________")  
                     
                    for open_port in open_ports:
                        
                        xs = str(open_ports)
                        
                        xr = len(xs)
                        
                        
                        
                        print(f"\033[1;31m{open_port} \033[1;32m[OPEN]")
                        
                    print("__________________________________________")  
                        
                try:
                    
                    run(command)
                    
                    
                except:
                    
                    print(f"\033[1;31mThe command is not found")
                    
                    time.sleep(0.2)   
                     
else:
    
    pass                

                    