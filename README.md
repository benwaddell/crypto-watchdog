# CryptoWatchdog

CryptoWatchdog is an application that runs in the background and automates the starting/stopping of crypto mining software based on which other application are currently running. This is useful if you use a personal computer for mining when idle, but need to disable mining when certain GPU intensive applications are running.

## How It Works

CryptoWatchdog operates quietly in the background to continuously monitor for applications that should disable mining. These applications must be specified in the config.yml file.

The currently running processes will be queried to determine if one of these specified applications is running.

* If none of these applications are running, mining will be started.

* If one of these applications is running, mining will be stopped.

The running processes will continue to be queried to check for changes. Once the specified application is no longer running, mining will resume.

This allows you to configure your personal gaming/editing computer to mine cryptocurrency when idle, with full automation for starting and stopping mining as necessary. Applications that should disable mining can be added or removed as needed through the config.yml file.

## Installation
CryptoWatchdog can be run in Python or as a standalone Windows executable file.

### To use Windows standalone executable:
- Download and extract zip file. Keep extracted files together.
- Configure config.yml file to match your miner and preferred settings.


### To use in Python:
- Install PyYAML:
    ```bash
    pip install PyYAML
    ```
- Download **cryptowatchdog.py** and **config.yml**. Keep these files together.
- Configure config.yml file to match your miner and preferred settings.
- Run in Python:
    ```bash
    python cryptowatchdog.py
    ```


## Usage

It is recommended to start CryptoWatchdog at system startup, either through Task Scheduler or as a Windows Startup item.

CryptoWatchdog can be used with any mining software and optionally will work with MSI Afterburner profiles to adjust overclocking settings.

The following settings are editable in the config.yml file.

```
## Set the delay in seconds for starting
## the watchdog (default: 60).
## Useful for giving the PC time to boot.

start_delay: 60

## Set the delay in seconds for resuming
## the miner after Applications are closed (default: 0).

resume_delay: 0

## Set, in seconds, how often an application
## check should be performed (default: 5).

check_delay: 5

## Specify the full path to the miner.
## REQUIRED -- Please change:

path: 'C:\CryptoMining\miner\miner.exe'

## Specify command line argument for miner.
## Set as empty string if no argument (i.e. '' ).
## REQUIRED -- Please change:

arg: '-c config.txt'

## Specify MSI Afterburner profile to use
## when not mining.
## Remove the # to enable.

#normal_prof: 'Profile1'

## Specify MSI Afterburner profile to use when mining.
## Remove the # to enable.

#mining_prof: 'Profile2'

## Specify Applications that should force the miner
## to stop (ex: "- Photoshop.exe").
## Case does not matter (i.e. "- Photoshop.exe" is
## the same as "- PhOtOsHoP.eXe").

apps:
  - 'Application1.exe'
  - 'Application2.exe'
  - 'Application3.exe'
```