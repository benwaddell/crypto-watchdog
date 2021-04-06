import subprocess, time, yaml, sys, os
from subprocess import Popen, CREATE_NEW_CONSOLE

# get the path of the exe and config.yml file
path = os.path.split(sys.argv[0])[0].replace('/', '\\')

# set the path of the config.yml file
config = f'{path}\\config.yml'

# get variables from JSON config file (do not modify this file directly)
with open(config, 'r') as yml_file:
    cfg = yaml.load(yml_file, Loader=yaml.BaseLoader)

start_delay = int(cfg['start_delay'])
check_delay = int(cfg['check_delay'])
path = cfg['path']
miner = cfg['path'].split('\\')[-1]
arg = cfg['arg']
apps = cfg['apps']
normal_prof = cfg['normal_prof']
mining_prof = cfg['mining_prof']

# delay give time for the OS and apps to boot
time.sleep(start_delay)

# check in procs to see if gpu miner or gpu intensive app is currently running
def watchdog(apps):
    app_running = False
    gpu_running = False
    for app in apps:
        if app.lower() in procs.lower():
            app_running = True
        elif miner in procs:
            gpu_running = True

    # if both miner and gpu intensive app are running, kill the miner and disable the overclocking profile
    if app_running == True and gpu_running == True:
        time.sleep(10)
        subprocess.Popen(["taskkill", "/F", "/IM", miner])
        subprocess.Popen(['C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe', f'-{normal_prof}'],
                         creationflags=CREATE_NEW_CONSOLE, shell=True)
        
    # if miner or gpu intensive app not running, enable gpu overclocking profile and start miner
    elif app_running == False and gpu_running == False:
        subprocess.Popen(['C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe', f'-{mining_prof}'],
                         creationflags=CREATE_NEW_CONSOLE, shell=True)
        subprocess.Popen([path, arg], creationflags=CREATE_NEW_CONSOLE, shell=True)

# run on a loop
while True:

    # query all running processes
    procs = (subprocess.check_output(['wmic', 'process', 'get', 'description'], universal_newlines=True))

    # run the watchdog function
    watchdog(apps)

    # repeat every X seconds
    time.sleep(check_delay)
