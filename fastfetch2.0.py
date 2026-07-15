#!/usr/bin/env python3
import platform
import os
import time
import sys
import subprocess
import importlib.util
platform_ = platform.system()
platform_ver = platform.release()
def __main__():
    if platform_ == 'Linux':
        pacname = 'distro'
        if not os.path.exists('.venv'):
            print('Installing Distro.Making VEnv')
            subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True) 
            print('Done Making VEnv.Installing Distro via pip')         
            subprocess.run([".venv/bin/python", "-m", "ensurepip", "--upgrade"], check=True)
            subprocess.run([".venv/bin/python", "-m", "pip", "install", "distro"], check=True)
            print('Done installing dependencies!')
        py_ver = f"python{sys.version_info.major}.{sys.version_info.minor}"
        venv_path = os.path.abspath(f".venv/lib/{py_ver}/site-packages")
        sys.path.insert(0, venv_path)
        try:
            import distro
            distroid = distro.id()
        except (ModuleNotFoundError, ImportError, NameError) as e:
            print('Please Install Distro via "pip install distro"')
        with open("/proc/cpuinfo", "r") as f:
            cpuinfo = f.read()
        with open("/proc/meminfo", "r") as f:
            meminfo = f.read()
        with open('/proc/uptime', "r") as f:
            uptime = f.read()
        with open('/proc/consoles', "r") as f:
            session = f.read()
        while True:
            try:
                device = 'Unknown'
                if os.path.exists('/sys/block/'):
                    for device in os.listdir('/sys/block/'):
                        if device.startswith(('sd', 'nvme', 'vd', 'hd')):
                            drivepath = f'/sys/block/{device}/device/model'
                            with open(drivepath, "r") as f:
                                model = f.read().strip()
                            break
                break
            except(FileNotFoundError, PermissionError) as e:
                print('File is Not Found or Permission was denied')
                break
        package_commands = {
    'arch': 'pacman -Q | wc -l',
    'alpine': 'apk info | wc -l',
    'debian': 'dpkg -l | grep ^ii | wc -l',
    'ubuntu': 'dpkg -l | grep ^ii | wc -l',
    'mint': 'dpkg -l | grep ^ii | wc -l',
    'fedora': 'rpm -qa | wc -l',
    'centos': 'rpm -qa | wc -l',
    'rhel': 'rpm -qa | wc -l',
    'rocky': 'rpm -qa | wc -l',
    'almalinux': 'rpm -qa | wc -l',
    'opensuse': 'rpm -qa | wc -l',
    'gentoo': 'qlist -I | wc -l',
    'void': 'xbps-query -l | wc -l'
    }
        print("\033[1;34mUser:\033[1;38;2;250;250;0m", os.getlogin())
        print("\033[34mHost:\033[1;38;2;250;250;0m", os.uname().nodename)
        print("\033[34mOS:\033[1;38;2;250;250;0m", platform_)
        distro_ = print("\033[34mDistro:\033[1;38;2;250;250;0m", distro.id())
        print("\033[34mKernel Version:\033[1;38;2;250;250;0m", platform_ver)
        disver = print("\033[34mDistro Version:\033[1;38;2;250;250;0m", distro.version())
        disname = print("\033[34mName and Release Type:\033[1;38;2;250;250;0m", distro.name())
        architech = print("\033[0m\033[1;34mArchitecture:\033[1;38;2;250;250;0m", platform.machine())
        for line in cpuinfo.split('\n'):
            if 'model name' in line.lower():
                cpu = line.split(":")[1].strip()
                print(f"\033[34mCPU Model:\033[1;38;2;250;250;0m{cpu}")
                break
        coreslin = print("\033[34mCPU Cores:\033[1;38;2;250;250;0m", os.cpu_count())
        for line in meminfo.split("\n"):
            if 'MemTotal' in line:
                ramkb = int(line.split()[1].strip())
                ramgb = (ramkb / 1048576)
                print(f"\033[34mRAM Total:\033[1;38;2;250;250;0m{ramgb:.2f} GB")
                break
        for line in meminfo.split("\n"):
            if 'MemAvailable' in line:
                frramkb = int(line.split()[1].strip())
                frramgb = (frramkb / 1048576)
                ramper = (frramkb / ramkb * 100)
                if ramper >= 70.00:
                    print(f"\033[34mRAM Free:\033[1;38;2;0;255;0m{ramper:.2f}%\033[1;38;2;250;250;0m Remaining (Healthy)")
                elif ramper >= 50.00:
                    print(f"\033[34mRAM Free:\033[1;38;2;255;255;0m {ramper:.2f}%\033[1;38;2;250;250;0m Remaining (Warning)")
                else:
                    print(f"\033[34mRAM Free:\033[1;38;2;255;0;0m {ramper:.2f}%\033[1;38;2;250;250;0m Remaining (Low)")
                break
        for line in meminfo.split('\n'):
            if 'SwapTotal' in line:
                swap = int(line.split()[1].strip())
                swapgb = (swap / 1048576)
                print(f"\033[34mTotal Swap:\033[1;38;2;250;250;0m{swapgb:.2f} GB")
                break
        for line in meminfo.split('\n'):
            if 'SwapFree' in line:
                totswapkb = int(line.split()[1].strip())
                totswapgb = (totswapkb / 1048576)
                swapper  = (totswapkb / swap * 100)
                if totswapgb >= 70.00:
                    print(f"\033[34mFree Swap:\033[1;38;2;255;0;0m{swapper:.2f}%\033[1;38;2;250;250;0m Remaining (Low)")
                elif totswapgb <= 50.00:
                    print(f"\033[34mFree Swap:\033[1;38;2;250;250;0m{swapper:.2f}%\033[1;38;2;250;250;0m Remaining (Warning)")
                else:
                    print(f"\033[34mFree Swap:\033[1;38;2;0;255;0m{swapper:.2f}%\033[1;38;2;250;250;0m Remaining (Healthy)")
                break
            print(f"\033[34mDrive Model:\033[1;38;2;250;250;0m{model.strip('\n')}")
        for line in session.split('\n'):
            session = session.strip(' ').splitlines()
            for index, line in enumerate(session):
                print(f"\033[34mSessions:\033[1;38;2;250;250;0m {index + 1}:", line.strip())
                break
            break
        getdis = package_commands.get(distroid, "")
        if distroid in package_commands:
            print(f'\033[34mPackages(PM):\033[1;38;2;250;250;0m', subprocess.getoutput(getdis).strip())
        print("\033[34mUptime(Hours):\033[1;38;2;250;250;0m", int(float(uptime.split()[0]) // 3600), "Hrs")
        network_name = print("\033[34mNetwork Host:\033[1;38;2;250;250;0m", platform.node())
        linuxlogo = (
    f"\033[1;38;2;23;147;209m                .88888888:.\033[0m\n"
    f"\033[1;38;2;23;147;209m               88888888.88888.\033[0m\n"
    f"\033[1;38;2;23;147;209m             .8888888888888888.\033[0m\n"          
    f"\033[1;38;2;23;147;209m             888888888888888888\033[0m\n"    
    f"\033[1;38;2;23;147;209m             88'\033[1;37m _`88'_\033[1;38;2;23;147;209m  `88888\033[0m\n"            
    f"\033[1;38;2;23;147;209m             88\033[1;37m 88 88 88\033[1;38;2;23;147;209m  88888\033[0m\n"         
    f"\033[1;38;2;23;147;209m             88\033[1;37m_88_::_\033[1;38;2;23;147;209m88\033[1;38;2;250;250;0m_:88888\033[0m\n"    
    f"\033[1;38;2;23;147;209m             88\033[1;38;2;250;250;0m:::,::,:::::8888\033[0m\n"                    
    f"\033[1;38;2;23;147;209m             88\033[1;38;2;250;250;0m`:::::::::'`8888\033[0m\n"
    f"\033[1;38;2;23;147;209m            .88  \033[1;38;2;250;250;0m`::::'    \033[1;38;2;23;147;209m8:88.\033[0m\n"
    f"\033[1;38;2;23;147;209m           8888            `8:888.\033[0m\n"
    f"\033[1;38;2;23;147;209m         .8888'             `888888.\033[0m\n"
    f"\033[1;38;2;23;147;209m        .8888:..\033[1;37m  .::.\033[1;38;2;23;147;209m  ...:'8888888:.\033[0m\n"
    f"\033[1;38;2;23;147;209m       .8888.\033[1;37m'     :'\033[1;38;2;23;147;209m     `'::`88:88888\033[0m\n"
    f"\033[1;38;2;23;147;209m      .8888\033[1;37m        '\033[1;38;2;23;147;209m         `.888:8888.\033[0m\n"
    f"\033[1;38;2;23;147;209m     888:8\033[1;37m         .\033[1;38;2;23;147;209m           888:88888\033[0m\n"
    f"\033[1;38;2;23;147;209m   .888:88\033[1;37m        .:\033[1;38;2;23;147;209m           888:88888:\033[0m\n"
    f"\033[1;38;2;23;147;209m   8888888.\033[1;37m       ::\033[1;38;2;23;147;209m           88:888888\033[0m\n"
    f"\033[1;38;2;23;147;209m   `.::.888.\033[1;37m      ::\033[1;38;2;23;147;209m          .88888888\033[0m\n"
    f"\033[1;38;2;23;147;209m  .::::::.888.\033[1;37m    ::\033[1;38;2;23;147;209m         :::`8888'.:.\033[0m\n"
    f"\033[1;38;2;23;147;209m ::::::::::.888   \033[1;37m'\033[1;38;2;23;147;209m         .::::::::::::\033[0m\n"
    f"\033[1;38;2;23;147;209m ::::::::::::.8    \033[1;37m'\033[1;38;2;23;147;209m      .:8::::::::::::.\033[0m\n"
    f"\033[1;38;2;23;147;209m.::::::::::::::.        .:888:::::::::::::\033[0m\n"
    f"\033[1;38;2;23;147;209m:::::::::::::::88:.__..:88888:::::::::::'\033[0m\n"
    f"\033[1;38;2;23;147;209m`'.:::::::::::88888888888.88:::::::::\033[0m\n"
    f"     `':::_:\033[1;38;2;250;250;0m:' -- '' -'-'\033[1;38;2;23;147;209m `':_::::'` \033[0m\n"
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
