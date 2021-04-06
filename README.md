# CryptoWatchdog

CryptoWatchdog is a program that automates the starting/stopping of crypto mining software based on which applications are currently running. Applications that should stop the mining process can be specified in the config.yml file.

# Installation
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


# Usage

It is recommended to start CryptoWatchdog at system startup, either through Task Scheduler or as a Windows Startup item.

CryptoWatchdog can be used with any mining software and optionally will work with MSI Afterburner profiles to adjust overclocking settings.

The following options are editable in the config.yml file.

```
## Set the delay in seconds for starting
## the watchdog (default: 60).
## Useful for giving the PC time to boot.

start_delay: 60

## Set, in seconds, how often an application
## check should be performed (default: 5).

check_delay: 5

## Specify the full path to the miner.
## REQUIRED -- Please change for your miner:

path: 'C:\CryptoMining\miner\miner.exe'

## Specify command line argument for miner.
## Set as empty string if no argument (i.e. '' ).
## REQUIRED -- Please change for your miner:

arg: '-c config.txt'

## Specify MSI Afterburner profile to use
## when not mining.
## Remove the # to enable.

#normal_prof: 'Profile1'

## Specify MSI Afterburner profile to use
## when mining.
## Remove the # to enable.

#mining_prof: 'Profile2'

## Specify apps that should force the miner to stop
## (ex: "- Photoshop.exe").
## Case does not matter (i.e. "- Photoshop.exe" is
## the same as "- PhOtOsHoP.eXe").

apps:
  - 'Application1.exe'
  - 'Application2.exe'
  - 'Application3.exe'
```