import time
import gate_control_functions as gc
import API_Controler as APIC
import sensor_controler as sc

'''
touchWarning = False
tempWarning = False
humidityWarning = False
windSpeedWarning = False
rainWarning = False
'''

#treshholds Oranje
tempTresholdO = 25
humTresholdO = 35
windSpeedTresholdO = 30
rainTresholdO = 5

#thresholds rood
tempTresholdR = 30
humTresholdR = 50
windSpeedTresholdR = 50
rainTresholdR = 10

def define_threat_level():
    threatCount = 0

    if sc.get_touch()==1:
        threatCount+=2
    if sc.get_humidity() >= humTresholdO:
        threatCount+=1
    if sc.get_humidity() >= humTresholdR:
        threatCount+=1
    if sc.get_temp() >= tempTresholdO:
        threatCount += 1
    if sc.get_temp() >= tempTresholdR:
        threatCount += 1
    if sc.get_wind() >= windSpeedTresholdO:
        threatCount += 1
    if sc.get_wind() >= windSpeedTresholdR:
        threatCount += 1
    #regen moet er nog bij maar het werkt nog niet helemaal

    #bij threatcount>4 oranje bij >6 rood, dit gebeurt in de screen clas
    return threatCount
