import platform
import os
platform_ = platform.system()
platform_ver = platform.release()
def __main__():
    if platform_ == 'Linux':
        import distro
        with open("/proc/cpuinfo", "r") as f:
            cpuinfo = f.read()
        with open("/proc/meminfo", "r") as f:
            meminfo = f.read()
        with open('/proc/uptime', "r") as f:
            uptime = f.read()
        with open('/proc/consoles', "r") as f:
            session = f.read() 
        print("\033[34mUser:\033[33m", os.getlogin())
        print("\033[34mHost:\033[33m", os.uname().nodename)
        print("\033[34mOS:\033[33m", platform_)
        distro_ = print("\033[34mDistro:\033[33m", distro.id())
        print("\033[34mDistro Version:\033[33m", platform_ver)
        disver = print("\033[34mKernel Version:\033[33m", distro.version())
        disname = print("\033[34mName and Release Type:\033[33m", distro.name())
        architech = print("\033[0m\033[34mArchitecture:\033[33m", platform.machine())
        for line in cpuinfo.split('\n'):
            if 'model name' in line.lower():
                cpu = line.split(":")[1].strip()
                print(f"\033[34mCPU Model:\033[33m{cpu}")
                break
        coreslin = print("\033[34mCPU Cores:\033[33m", os.cpu_count())
        for line in meminfo.split("\n"):
            if 'MemTotal' in line:
                ramkb = int(line.split()[1].strip())
                ramgb = (ramkb / 1048576)
                print(f"\033[34mRAM Totals:\033[33m{ramgb:.2f} GB")
                break
        for line in meminfo.split("\n"):
            if 'MemFree' in line:
                ramkb = int(line.split()[1].strip())
                ramgb = (ramkb / 1048576)
                print(f"\033[34mRAM Free:\033[33m{ramgb:.2f} GB")
                break
        for line in session.split('\n'):
            if session.startswith('tty0'):
                if session.count('\n') < 0:
                    ses1, ses2 = session.splitlines() 
                    print("Session 1:", ses1.strip())
                    print('Session 2:', ses2.strip())
                break
        print("\033[34mUptime(Hours):\033[33m", int(float(uptime.split()[0]) // 3600), "Hrs")
        network_name = print("\033[34mNetwork Host:\033[33m", platform.node())
        linuxlogo = (
    f"\033[36m                .88888888:.\033[0m\n"
    f"\033[36m               88888888.88888.\033[0m\n"
    f"\033[36m             .8888888888888888.\033[0m\n"          
    f"\033[36m             888888888888888888\033[0m\n"    
    f"\033[36m             88'\033[37m _`88'_\033[36m  `88888\033[0m\n"            
    f"\033[36m             88\033[37m 88 88 88\033[36m  88888\033[0m\n"         
    f"\033[36m             88\033[37m_88_::_\033[36m88\033[33m_:88888\033[0m\n"    
    f"\033[36m             88\033[33m:::,::,:::::8888\033[0m\n"                    
    f"\033[36m             88\033[33m`:::::::::'`8888\033[0m\n"
    f"\033[36m            .88  \033[33m`::::'    \033[36m8:88.\033[0m\n"
    f"\033[36m           8888            `8:888.\033[0m\n"
    f"\033[36m         .8888'             `888888.\033[0m\n"
    f"\033[36m        .8888:..\033[37m  .::.\033[36m  ...:'8888888:.\033[0m\n"
    f"\033[36m       .8888.\033[37m'     :'\033[36m     `'::`88:88888\033[0m\n"
    f"\033[36m      .8888\033[37m        '\033[36m         `.888:8888.\033[0m\n"
    f"\033[36m     888:8\033[37m         .\033[36m           888:88888\033[0m\n"
    f"\033[36m   .888:88\033[37m        .:\033[36m           888:88888:\033[0m\n"
    f"\033[36m   8888888.\033[37m       ::\033[36m           88:888888\033[0m\n"
    f"\033[36m   `.::.888.\033[37m      ::\033[36m          .88888888\033[0m\n"
    f"\033[36m  .::::::.888.\033[37m    ::\033[36m         :::`8888'.:.\033[0m\n"
    f"\033[36m ::::::::::.888   \033[37m'\033[36m         .::::::::::::\033[0m\n"
    f"\033[36m ::::::::::::.8    \033[37m'\033[36m      .:8::::::::::::.\033[0m\n"
    f"\033[36m.::::::::::::::.        .:888:::::::::::::\033[0m\n"
    f"\033[36m:::::::::::::::88:.__..:88888:::::::::::'\033[0m\n"
     f"`'.:::::::::::88888888888.88:::::::::\n"
      f"     `':::_:\033[33m:' -- '' -'-'\033[36m `':_::::'` \033[0m\n"
    )
        print(linuxlogo)
    if platform_ == 'Windows':
        winarch = print("\033[34mArchitecture:\033[0m", platform.machine())
        winver = print(f"\033[34mVersion:\033[0m {platform.version()}")
        windowslogo = f"""
\x1b[34m
   ⣤⣴⣾⣿⣿⣿⣿⣿⣶                  \033[34mOS:\033[0mWindows\033[34m
  ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿  ⢰⣦⣄⣀⣀⣠⣴⣾⣿⠃      \033[34mVersion:\033[0m{platform.release()}\033[34m
  ⢸⣿⣿⣿⣿⣿⣿⣿⣿⡏  ⣼⣿⣿⣿⣿⣿⣿⣿⣿       \033[34mArchitecture:\033[0m{platform.architecture()}\033[34m
  ⣼⣿⡿⠿⠛⠻⠿⣿⣿⡇  ⣿⣿⣿⣿⣿⣿⣿⣿⡿       \033[34mNetwork Host:\033[0m{platform.node()}\033[34m
  ⠉   ⢀      ⢰⣿⣿⣿⣿⣿⣿⣿⣿⠇       \033[34mCPU:\033[0m{platform.processor()}\033[34m
  ⣠⣴⣶⣿⣿⣿⣷⣶⣤                   \033[34mCPU Cores:\033[0m{os.cpu_count()}\033[34m
 ⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇  ⣶⣦⣄⣀⣀⣀⣤⣤⣶ 
 ⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇  ⣿⣿⣿⣿⣿⣿⣿⣿⡟
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁ ⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢠⣿⡿⠿⠛⠉⠉⠉⠛⠿  ⢸⣿⣿⣿⣿⣿⣿⣿⣿⠁
           ⠻⢿⣿⣿⣿⣿⣿⠿⠛
\x1b[0m
""".strip('()').strip("''") 
        print(windowslogo)
__main__()
