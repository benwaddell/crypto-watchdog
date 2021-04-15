import subprocess
import time
import yaml
import sys
import os
from subprocess import Popen, CREATE_NEW_CONSOLE

# define any variables outside of functions
resume_timer = 0


# function to load the config.yml file and set variables
def loadconfig():

    # define global variables
    global start_delay, resume_delay, check_delay, path, miner, arg, apps, normal_prof, mining_prof

    # get the path of the exe and config.yml file
    path = os.path.split(sys.argv[0])[0].replace('/', '\\')

    # set the path of the config.yml file
    config = f'{path}\\config.yml'

    # get variables from JSON config file (do not modify this file directly)
    with open(config, 'r') as yml_file:
        cfg = yaml.load(yml_file, Loader=yaml.BaseLoader)

    start_delay = int(cfg['start_delay'])
    resume_delay = int(cfg['resume_delay'])
    check_delay = int(cfg['check_delay'])
    path = cfg['path']
    miner = cfg['path'].split('\\')[-1]
    arg = cfg['arg']
    apps = cfg['apps']
    if 'normal_prof' in cfg:
        normal_prof = cfg['normal_prof']
    else:
        normal_prof = None
    if 'mining_prof' in cfg:
        mining_prof = cfg['mining_prof']
    else:
        mining_prof = None


# function to gather running procs, check if app or miner in procs, start/stop miner if necessary
def watchdog(apps_list):

    # define variables
    global resume_timer
    app_running = False
    gpu_running = False

    # query all running processes
    procs = (subprocess.check_output(['wmic', 'process', 'get', 'description'], universal_newlines=True))

    # check if specified app or miner in procs
    for app in apps_list:
        if app.lower() in procs.lower():
            app_running = True
            resume_timer = resume_delay + check_delay
        if miner in procs:
            gpu_running = True

    # if both miner and gpu intensive app are running, kill the miner and disable the overclocking profile
    if app_running is True and gpu_running is True:
        time.sleep(10)
        subprocess.Popen(["taskkill", "/F", "/IM", miner])
        if normal_prof is not None:
            subprocess.Popen([r'C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe', f'-{normal_prof}'],
                             creationflags=CREATE_NEW_CONSOLE, shell=True)

    # if miner or gpu intensive app not running, enable gpu overclocking profile and start the miner
    elif app_running is False and gpu_running is False and resume_timer <= 0:
        if mining_prof is not None:
            subprocess.Popen([r'C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe', f'-{mining_prof}'],
                             creationflags=CREATE_NEW_CONSOLE, shell=True)
        subprocess.Popen([path, arg], creationflags=CREATE_NEW_CONSOLE, shell=True)


# function to delay the loop and countdown resume_timer variable
def delay():
    time.sleep(check_delay)
    global resume_timer
    if resume_timer > 0:
        resume_timer -= check_delay


# function to run on a loop
def run_loop():

    while True:

        # run the loadconfig function
        loadconfig()

        # run the watchdog function
        watchdog(apps)

        # delay the loop to repeat every X seconds
        delay()


# initial load of the config
loadconfig()

# delay give time for the OS and apps to boot
time.sleep(start_delay)

# run the script
run_loop()
