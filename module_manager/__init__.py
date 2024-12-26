import subprocess, sys

bold_start = "\033[1m"
italic_start = "\033[3m"
magenta_color = "\033[35m"
reset = "\033[0m"
green_color = "\033[32m"
red_color = "\033[31m"
gray_color = "\033[90m"

def check_and_install(module, version):
    try:
        __import__(module)
        print(f"[+] {italic_start}{magenta_color}{module}{reset} {green_color}{bold_start}установлен{reset}{bold_start}!{reset}")
    except:
        print(f"[-] {italic_start}{magenta_color}{module}{reset} {red_color}{bold_start}не установлен{reset}{bold_start}!{reset}")
        print(f'{gray_color}[..] установка модуля {italic_start}"{module}" ({version}) ...{reset}')
        try:
            instalation = subprocess.Popen([sys.executable, "-m", "pip", "install", f"{module}=={version}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            instalation.communicate()
            print(f"[+] {italic_start}{magenta_color}{module}{reset} {green_color}{bold_start}установлен{reset}{bold_start}!{reset}")
        except Exception as e:
            print(f'[!] {red_color}Ошибка при установке модуля {italic_start}"{module}" ({version}) :{reset}\n\n{e}')

def start_modules_instalation(packages):
    print(f"{bold_start}# Мастер установки {italic_start}{magenta_color}kryyaa-pkg{reset} {gray_color}0.1.0{reset}")
    for pkg in packages:
        check_and_install(pkg["name"], pkg["version"])