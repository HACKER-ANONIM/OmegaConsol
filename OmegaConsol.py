import os
import time
import socket
import webbrowser 
import platform
import subprocess
import shutil
import sys 
import requests
from datetime import datetime
            

                  
                

def main():
    while True:
        print( "CONSOL@HACKER-Omega@Consol" )
        print(""" 
    

  ____   __  __   _____  ____     _      ____   ___   _   _   ____    ____    _     
 / __ \ |  \/  | |____ |/ ___|   / \    / ___| / _ \ | \ | | / ___| / ___  \ | |    
| |  | || |\/| | |____ | |  _   / _ \  | |    | | | ||  \| | \___ \ | |  | | | |    
| |__| || |  | | |____ |_|_| | / ___ \ | |___ | |_| || |\  |  ___) || |__| | | |___ 
 \____/ |_|  |_| |_____|\____//_/   \_\ \____| \___/ |_| \_| |____/ \ ____ / |_____|



    """)
        print("omega:help: - список команд")
        command = input("Omega@consol~# >>> ")

        if command == "omega:help:":
            print("Omega: ","-"*50)
            print("omega:search: - поиск сайтов по браузеру")
            print("omega:ping: - отпровляет запрсо чтобы узнать активен ли IP")
            print("omega:network: -  сетевые параметры")
            print("omega:omap: - сканирование протов (omega map)")
            print("omega:top: - процесы" )
            print("omega:htop: - диспечер задачь")
            print("omega:skript:OS - скрипт для быстрого управления OS")
            print("omega:exit: - выход ")
            
            
            print("GitHub: ","-"*50)
            print("github:wireshark: - запускает иструмент если он установлен")
            
            print("corp:","-"*50)
            print("corp:meltego:#none")
            print("corp:protonVPN:#none")

            print("p:","-"*50)
            print("p:MR.ROBOT")
            print("-"*50)




        if command == "omega:exit:":
            break


        if command == "omega:search": #1 команда для открытия сылок
            url = input("⟪consol⟫  >>> адрес сайта:" )
            webbrowser.open(url)
            input("\nНажмите Enter для продолжения...")    
             
        elif command == "omega:ping:": #2 для пинга сылки пороверки активности сайта 
            target = input("⟪consol⟫  >>> адрес сайта:")
            print(f"\nПроверяю {target}...")

            param_count = "-n" if platform.system().lower() == "windows" else "-c"
            command = ["ping", param_count, "4", target]

            try:
                result = subprocess.run(command, capture_output=True, text=True, encoding="cp866", timeout=10)
                print(result.stdout)
                if result.returncode == 0:
                    print(f"✅ {target} АКТИВЕН")
                else:
                    print(f"❌ {target} НЕ АКТИВЕН")
            except subprocess.TimeoutExpired:
                print(f"⏱️ Превышено время ожидания.")
            except UnicodeDecodeError:
                subprocess.run(command)
            except Exception as e:
                print(f"⚠️ Ошибка: {e}")
            input("\nНажмите Enter для продолжения...")
        elif command == "omega:network:": # 3 команда простая для того чтобы узнать IP
            ip = os.system("ipconfig")
            print(ip)
            input("\nНажмите Enter для продолжения...")
                      
                         
          
        
        
        elif command == "omega:top:":
            try:
                result = subprocess.run(["powershell", "-Command", "Get-Process"],capture_output=True,text=True,timeout=10)
                print(result.stdout)
            except Exception as e:
                print(f"Ошибка: {e}")
            input("\nНажмите Enter для продолжения...")    
        elif command == "htop:":
            print(" ========= открытие диспечер задачь =========")
            time.sleep(3)
            if platform.system() == "Windows":
                subprocess.run(["taskmgr.exe"])
            else:
                print("htop работает только в Windows.")    
            print("диспечер задачь открыт >....")
            print()
            input("\nНажмите Enter для продолжения...")
             
        elif command == "p:MR.ROBOT":
            print("\033[92m" + r"""
             __  __            __ ____   ______   _______       _______     ____________
            |  \/  |          |   >___| /      \  /       \    /       \   |____    ____|
            | \  / |  _ __    |   |     |      |  |        /   |       |       |  |
            | |\/| | | '__|   |   |     |      |  |========    |       |       |  |
            | |  | | | |      |   |     |      |  |        \   |       |       |  |
            |_|  |_| |_|    * |___|     \______/  |________/   \_______/       |__|        

            """ + "\033[0m")
            webbrowser.open("https://ru.wikipedia.org/wiki/%D0%9C%D0%B8%D1%81%D1%82%D0%B5%D1%80_%D0%A0%D0%BE%D0%B1%D0%BE%D1%82")
            webbrowser.open("https://www.bing.com/search?q=mr.robot+netflix&qs=n&sp=-1&lq=0&pq=&sc=0-0&sk=&cvid=2672A84E7C33423EBBAFF9302147D96F&FPIG=B8B4DF0C11604DBA91C3650C8C3B48AE&first=1&FORM=PERE")
            input("\nНажмите Enter для продолжения... Привет элиот ! Ты нашол пасхалку")
                                                                
        elif command == "omega:skript:OS": 
            # Внутри обработки команды "skript:OS"
         base_dir = os.path.dirname(os.path.abspath(__file__))
         target_script = os.path.join(base_dir, "SKRIPT", "skriptOS.py")

         if not os.path.exists(target_script):
            print(f"Файл не найден: {target_script}")
            print("Проверь, что skriptOS.py лежит в папке SKRIPT")
         else:
            subprocess.Popen([sys.executable, target_script], creationflags=subprocess.CREATE_NEW_CONSOLE)   # ✅ ПРАВИЛЬНО *надеюсь
            print("Скрипт запущен в новом окне!")
        elif command == "github:wireshark:":
            print("⟪consol⟫  >>> |open wireshark|")
            time.sleep(2)
            print("❇️SCANING❇️")
            wireshark_path = r"C:\Program Files\Wireshark\Wireshark.exe"

            if os.path.exists(wireshark_path):
                subprocess.run([wireshark_path])   
                print("✅wireshark найден✅")
                print("♾️СКАНИРОВАНИЕ ТРАФИКА♾️")
                time.sleep(3)
            else:
                print("❌wireshark не найден❌.")  
                print("⚠️УСТАНОВИТЕ WIRESHARK⚠️.") 
            input("\nНажмите Enter для продолжения... ╰(*°▽°*)╯")
        elif command == "omega:omap:":
            print("⟪consol⟫  >>> |open Omap|")
            print("🔎OMAP🔍")
            base_dir = os.path.dirname(os.path.abspath(__file__))
            maper = os.path.join(base_dir, "skript", "Omap.py")
            subprocess.run(["python",maper])
        
        elif command == "omega:vpn:":
            print("vpn kiler DIP")
            subprocess.run([])
   
         
            

           





    
   

           
            
                       
     




       




           
if __name__ == "__main__":
    main()

        

    




         



    






    

















   




    




