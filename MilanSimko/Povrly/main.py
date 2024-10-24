#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
##
##  PURPOSE :
##
##  DATE    : October 10 2024
##  AUTHOR  : Milan Šimko <milan.simko@tractebel.engie.com>
##  VERSION : 0.01
##
##  ENCODING: UTF-8
##
##  USAGE   : python main.py
##  OPTIONS : -
##
##  NOTES   :
##
################################################################################
import sys                                      ; sys.path.append('D:\\bin\\py')
################################################################################
import os
import csv
import json
import xlwings as xw

import equiplist as my

################################################################################
from project import *
#from units  import *
#from items  import *
from values  import *

############################## GLOBÁLNÍ PROMĚNNÉ ###############################
my.maxlevel = 2
my.generateSCR = True
my.generateTXT = False
my.generateXLS = False

############################# SCRIPT ZAČÍNÁ ZDE ################################
os.system('clear')

# Generování různorodých výstupů
my.outputs(revs, proj, docs, itms)

# Export dat pro profese
class DateEncoder(json.JSONEncoder):
	def default(self, obj):
		return obj.__dict__

BaseAdres = "U:\\Elektro\\mcsato\\Zakázky\\Povrly.med\\"
# Získání názvu počítače
hostname = os.environ['COMPUTERNAME']
if(hostname == "MARTIN"):
	StartAdresar = os.path.dirname(__file__)
	BaseAdres = os.path.join(StartAdresar, "Soubor")
	os.makedirs(BaseAdres, exist_ok=True)

objekty = os.path.join(BaseAdres, "objekty.json")
print(objekty)
json_data = json.dumps([vars(obj) for obj in objs], indent=4, ensure_ascii=False, cls=DateEncoder)
with open(objekty, 'w', encoding='utf-8', newline='\n') as f:
	f.write(json_data)

zarizeni = os.path.join(BaseAdres, "zarizeni.json") 
json_data = json.dumps([vars(obj) for obj in itms], indent=4, ensure_ascii=False, cls=DateEncoder)
with open(zarizeni, 'w', encoding='utf-8', newline='\n') as f:
	f.write(json_data)

zarizeni = os.path.join(BaseAdres, "zarizeni.csv") 
with open(zarizeni, 'w', encoding='utf-8', newline='\n') as f:
	w = csv.DictWriter(f, fieldnames=vars(itms[0]))
	w.writerows([vars(obj) for obj in itms])


sys.path.append(r"C:\VSCode\PythonGit\Testy\Class\SaveLoad2")
import SaveLoad2 as file

zarizeni2 = os.path.join(BaseAdres, "zarizeni2.csv") 
file.SaveToCsv2(itms, zarizeni2)

sys.exit(0)
# vim:tw=10000:ts=4:sts=4:sw=4:noexpandtab:
