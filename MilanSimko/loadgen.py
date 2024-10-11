#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
##
##  PURPOSE : FIXME
##
##  DATE    : FIXME FIXME FIXME
##  AUTHOR  : Dr. Milan Šimko  <milan.simko@tractebel.engie.com>
##  VERSION : 0.01
##
##  ENCODING: UTF-8
##
##  USAGE   : py FIXME.py
##  OPTIONS : -
##
################################################################################
import xlsxwriter

#################################### METODY ####################################
def hstif(item):
	return {
		0 : "As Designed",
		1 : "Rigid",
		2 : "Ignore"
	}[item]

def otypes(otype):
	return {
		0 : "Disp/Force/Stress",
		1 : "Disp/Force",
		2 : "Disp/Stress",
		3 : "Force/Stress",
		4 : "Disp",
		5 : "Force",
		6 : "Stress"
	}[otype]

def otype(stype):
	return {
		"HGR": otypes(0),
		"HYD": otypes(1),
		"OPE": otypes(1),
		"SUS": otypes(3),
		"EXP": otypes(6),
		"OCC": otypes(6)
	}[stype]

#################################### TŘÍDY #####################################
class Data:
	isOperational = None
	isSuppress = None
	P     = None  # číslo definice vnitřního tlaku
	T     = None  # číslo definice teploty
	case  = ""
	name  = ""
	note  = ""
	cmthd = ""
	stype = ""
	hstif = ""

class HYD(Data):
	def __init__(self):
		global Lnum; self.L = Lnum; Lnum+=1
		self.H     = "+H" if hasHanger else ""
		self.case  = "WW+HP"+self.H
		self.name  = "HYDRO TEST CASE"
		self.stype = "HYD"
		self.hstif = hstif(1) if hasHanger else hstif(0)

class HGR(Data):
	def __init__(self, case, name, hstif):
		global Lnum; self.L = Lnum; Lnum+=1
		self.isSuppress = True
		self.case  = case
		self.name  = name                                # název zatěžujícího stavu
		self.stype = "HGR"                               # typ napětí
		self.hstif = hstif

class OPE(Data):
	def __init__(self, T, P, i):
		global Lnum; self.L = Lnum; Lnum+=1
		self.P     = P                                   # číslo definice vnitřního tlaku
		self.T     = T                                   # číslo definice teploty
		self.case  = "W+T"+str(self.T)+"+P"+str(self.P)  # definice zatěžujícího stavu
		self.name  = "OPERATING CASE CONDITION "+str(i)  # název zatěžujícího stavu
		self.stype = "OPE"                               # typ napětí
		self.hstif = hstif(0)

class OPE_U(Data):
	def __init__(self, T, P, case, name):
		global Lnum; self.L = Lnum; Lnum+=1
		self.P     = P                                   # číslo definice vnitřního tlaku
		self.T     = T                                   # číslo definice teploty
		self.case  = case                                # definice zatěžujícího stavu
		self.name  = name                                # název zatěžujícího stavu
		self.stype = "OPE"                               # typ napětí
		self.hstif = hstif(0)

class OPE_WIN(Data):
	def __init__(self, T, P, case, name):
		global Lnum; self.L = Lnum; Lnum+=1
		self.P     = P                                   # číslo definice vnitřního tlaku
		self.T     = T                                   # číslo definice teploty
		self.case  = case                                # definice zatěžujícího stavu
		self.name  = name                                # název zatěžujícího stavu
		self.stype = "OPE"                               # typ napětí
		self.hstif = hstif(0)

class SUS(Data):
	def __init__(self, P, i):
		global Lnum; self.L = Lnum; Lnum+=1
		self.H     = "+H" if hasHanger else ""
		self.P     = P                                   # číslo definice vnitřního tlaku
		self.case  = "W+P"+str(self.P)+self.H            # definice zatěžujícího stavu
		self.name  = "SUSTAINED CASE CONDITION "+str(i)  # název zatěžujícího stavu
		self.stype = "SUS"                               # typ napětí
		self.hstif = hstif(0)

class EXP(Data):
	def __init__(self, Li, Lj, i, j):
		global Lnum; self.L = Lnum; Lnum+=1
		self.case = "L"+str(Li)+"-L"+str(Lj)                           # definice zatěžujícího stavu
		if i == j:
			self.name = "EXPANSION CASE CONDITION "+str(i)             # název zatěžujícího stavu
		else:
			self.name = "EXPANSION CASE CONDITION "+str(i)+"-"+str(j)  # název zatěžujícího stavu
			self.note = "NOTE: plný rozkmit napětí"
		self.cmthd = "Algebraic"                                       # metoda lineární kombinace
		self.stype = "EXP"                                             # typ napětí

class OCC(Data):
	def __init__(self, Li, Lj, name, cmthd, sign):
		global Lnum; self.L = Lnum; Lnum+=1
		self.case  = "L"+str(Li)+sign+"L"+str(Lj)                      # definice zatěžujícího stavu
		self.name  = name                                              # název zatěžujícího stavu
		self.cmthd = cmthd                                             # metoda lineární kombinace
		self.stype = "OCC"                                             # typ napětí

############################## GLOBÁLNÍ PROMĚNNÉ ###############################
global hasSeismic; hasSeismic = False
global hasHanger; hasHanger = False
global hasWind; hasWind = False

global Lnum; Lnum = 1
global Larr; Larr = []

############################# SCRIPT ZAČÍNÁ ZDE ################################
retval = input("Budou pružné závěsy? (0=Ne|1=Ano)       : ")
retval = retval.lower() in ['1', 'y']
if retval: hasHanger = True

retval = input("Bude zatížení zemětřesením? (0=Ne|1=Ano): ")
retval = retval.lower() in ['1', 'y']
if retval: hasSeismic = True

retval = input("Bude zatížení větrem? (0=Ne|1=Ano)      : ")
retval = retval.lower() in ['1', 'y']
if retval: hasWind = True

nOPE = int(input("\nZadej počet zatěžujících stavů: "))

# Předdefinuje zatěžující stavy pro pružné závěsy
if hasHanger:
	Larr.append(HGR("W", "WEIGHT FOR HANGER LOADS", hstif(1)))
	for i in range(1,nOPE+1):
		Larr.append(HGR("", "OPERATING FOR HANGER TRAVEL "+str(i), hstif(2)))
	Larr.append(HGR("WNC+H", "ACTUAL HANGER COLD LOADS", hstif(0)))

# Definuje hydrostatickou tlakovou zkoušku
Larr.append(HYD())

# Definuje
for i in range(1,nOPE+1):
	T = int(input("{:d}| W+T".format(i)))
	P = int(input("{:d}| W+T{:d}+P".format(i,T)))
	Larr.append(OPE(T, P, i))

	# Definuje zatěžující stavy pro pružné závěsy
	if hasHanger:
		idx = [i.name if i.stype == "HGR" else None for i in Larr].index("OPERATING FOR HANGER TRAVEL "+str(i))  # najde index L, pro i.Name == index()
		jdx = [i.name if i.stype == "OPE" else None for i in Larr].index("OPERATING CASE CONDITION "+str(i))     # najde index L, pro i.Name == index()
		Larr[idx].case = Larr[jdx].case
		Larr[jdx].case = Larr[jdx].case+"+H"

print()
for i in Larr:
	if i.stype == "OPE":
		print("\033[1;37m L{:<2d}  {:14s}  ({:3s})  {:53s}\033[0;m".format(i.L, i.case, i.stype, i.name))
	else:
		print(" L{:<2d}  {:14s}  ({:3s})  {:53s}".format(i.L, i.case, i.stype, i.name))
print()

# Označí zatěžující stav jako provozní
nTMP = int(input("Zadej počet provozních stavů: "))
for i in range(1,nTMP+1):
	star = int(input("{:d}| L".format(i)))
	for j in Larr:
		if j.L == star: j.isOperational = True

# Definuje
for i in Larr:
	if i.isOperational and hasSeismic:
		Larr.append(OPE_U(i.T, i.P, i.case+"+U1", i.name+" WITH SEISMIC LOAD +X"))
		Larr.append(OPE_U(i.T, i.P, i.case+"-U1", i.name+" WITH SEISMIC LOAD −X"))
		Larr.append(OPE_U(i.T, i.P, i.case+"+U2", i.name+" WITH SEISMIC LOAD +Y"))
		Larr.append(OPE_U(i.T, i.P, i.case+"-U2", i.name+" WITH SEISMIC LOAD −Y"))
		Larr.append(OPE_U(i.T, i.P, i.case+"+U3", i.name+" WITH SEISMIC LOAD +Z"))
		Larr.append(OPE_U(i.T, i.P, i.case+"-U3", i.name+" WITH SEISMIC LOAD −Z"))

# Definuje
for i in Larr:
	if i.isOperational and hasWind:
		Larr.append(OPE_WIN(i.T, i.P, i.case+"+WIN1", i.name+" WITH WIND LOAD +X"))
		Larr.append(OPE_WIN(i.T, i.P, i.case+"+WIN2", i.name+" WITH WIND LOAD −X"))
		Larr.append(OPE_WIN(i.T, i.P, i.case+"+WIN3", i.name+" WITH WIND LOAD +Z"))
		Larr.append(OPE_WIN(i.T, i.P, i.case+"+WIN4", i.name+" WITH WIND LOAD −Z"))

# Definuje zatěžující stavy pro trvalé zatížení
for i in range(1,P+1):
	Larr.append(SUS(i, i))

# Definuje zatěžující stavy pro teplotní namáhání
for i in range(1,nOPE+1):
	idx = [i.name if i.stype == "OPE" else None for i in Larr].index("OPERATING CASE CONDITION "+str(i))  # najde index L pro i.Name == index()
	jdx = [i.P    if i.stype == "SUS" else None for i in Larr].index(Larr[idx].P)                         # najde index L pro i.P    == index()
	Larr.append(EXP(Larr[idx].L, Larr[jdx].L, i, i))
	for j in range(1,i):
		idx = [i.name if i.stype == "OPE" else None for i in Larr].index("OPERATING CASE CONDITION "+str(i))  # najde index L pro i.Name == index()
		jdx = [i.name if i.stype == "OPE" else None for i in Larr].index("OPERATING CASE CONDITION "+str(j))  # najde index L pro i.Name == index()
		Larr.append(EXP(Larr[jdx].L, Larr[idx].L, j, i))

# Definuje zatěžující stavy pro čisté zatížení od zemětřesení při provozních podmínkách
for i in Larr:
	if i.isOperational and hasSeismic:
		for j in ["+X", "−X", "+Y", "−Y", "+Z", "−Z"]:
			idx = [k.name if k.stype == "OPE" else None for k in Larr].index(i.name+" WITH SEISMIC LOAD "+str(j))  # najde index L pro i.Name == index()
			Larr.append(OCC(Larr[idx].L, i.L, "PURE SEISMIC LOAD "+str(j)+" AT "+i.name, "Algebraic", "-"))
			Larr[len(Larr)-1].isSuppress = True  # zatěžující stav nebude vyhodnocován

# Definuje zatěžující stavy pro čisté zatížení od větru při provozních podmínkách
for i in Larr:
	if i.isOperational and hasWind:
		for j in ["+X", "−X", "+Z", "−Z"]:
			idx = [k.name if k.stype == "OPE" else None for k in Larr].index(i.name+" WITH WIND LOAD "+str(j))  # najde index L pro i.Name == index()
			Larr.append(OCC(Larr[idx].L, i.L, "PURE WIND LOAD "+str(j)+" AT "+i.name, "Algebraic", "-"))
			Larr[len(Larr)-1].isSuppress = True  # zatěžující stav nebude vyhodnocován

# Definuje zatěžující stavy pro čisté zatížení od zemětřesení včetně trvalého zatížení při provozních podmínkách
for i in Larr:
	if i.isOperational and hasSeismic:
		idx = [i.P if i.stype == "SUS" else None for i in Larr].index(i.P)  # najde index L pro i.P == index()
		for j in ["+X", "−X", "+Y", "−Y", "+Z", "−Z"]:
			jdx = [k.name if k.stype == "OCC" else None for k in Larr].index("PURE SEISMIC LOAD "+str(j)+" AT "+i.name)  # najde index L pro i.Name == index()
			Larr.append(OCC(Larr[idx].L, Larr[jdx].L, Larr[idx].name+" WITH PURE SEISMIC LOAD "+str(j), "Scalar", "+"))

# Definuje zatěžující stavy pro čisté zatížení od větru včetně trvalého zatížení při provozních podmínkách
for i in Larr:
	if i.isOperational and hasWind:
		idx = [i.P if i.stype == "SUS" else None for i in Larr].index(i.P)  # najde index L pro i.P == index()
		for j in ["+X", "−X", "+Z", "−Z"]:
			jdx = [k.name if k.stype == "OCC" else None for k in Larr].index("PURE WIND LOAD "+str(j)+" AT "+i.name)  # najde index L pro i.Name == index()
			Larr.append(OCC(Larr[idx].L, Larr[jdx].L, Larr[idx].name+" WITH PURE WIND LOAD "+str(j), "Scalar", "+"))

# Tisk
print()
for i in Larr:
	if i.isOperational:
		print("\033[1;37m*L{:<2d}  {:14s}  ({:3s})  {:53s}  {:9s}\033[0;m  {:s}".format(i.L, i.case, i.stype, i.name, i.cmthd, i.note))
	else:
		if i.isSuppress:
			print("\033[2;37m L{:<2d}  {:14s}  ({:3s})  {:53s}  {:9s}\033[0;m  {:s}".format(i.L, i.case, i.stype, i.name, i.cmthd, i.note))
		else:
			print("\033[1;37m L{:<2d}  {:14s}  ({:3s})  {:53s}  {:9s}\033[0;m  {:s}".format(i.L, i.case, i.stype, i.name, i.cmthd, i.note))


print()
print("<subsection>Seznam uvažovaných statických zatěžujících stavů</subsection>")
print("<table rows=\"{:d}\" cols=\"4\">".format(len(Larr)+1))
print("<cel></cel>   <cel>Zatěžující stav</cel><cel>Typ zatížení</cel><cel>Metoda kombinace</cel>")
for i in Larr:
	print("{:<14}{:<26s}{:<23s}{:<27s}{:<s}".format(
	      "<cel>L"+str(i.L)+"</cel>",
	      "<cel>"+i.case.replace("-", "−")+"</cel>",
	      "<cel>("+i.stype+")</cel>",
	      "<cel>"+i.cmthd+"</cel>" if i.cmthd else "<cel>—</cel>",
	      "<!-- "+i.name+" -->"))
print("</table>")

# Vytvoří workbook a vloží worksheet
workbook = xlsxwriter.Workbook("LOAD_CASES_EDITOR.XLSX")
worksheet = workbook.add_worksheet()
digit = workbook.add_format({'num_format': '###0.0000'})
head = workbook.add_format({'bold': True, 'text_wrap': True, 'align': 'center', 'valign': 'vcenter'})
off = workbook.add_format({'bg_color': '#F2F2F2'})
row = 0
worksheet.write(row,  1, "Load Cases", head)
worksheet.write(row,  2, "Stress\nType", head)
worksheet.write(row,  3, "Load Case Name", head)
worksheet.write(row,  4, "Output\nStatus", head)
worksheet.write(row,  5, "Output\nType", head)
worksheet.write(row,  6, "Comb\nMethod", head)
worksheet.write(row,  7, "Snubbers\nActive?", head)
worksheet.write(row,  8, "Hanger\nStiffness", head)
worksheet.write(row,  9, "Elastic\nModulus", head)
worksheet.write(row, 10, "Elbow\nStiffening\nPressure", head)
worksheet.write(row, 11, "Elbow\nStiffening\nElastic\nModulus", head)
worksheet.write(row, 12, "SUS/OCC\nCase Sh", head)
worksheet.write(row, 13, "Friction\nMultiplier", head)
worksheet.write(row, 14, "OCC Load\nFactor", head)
worksheet.write(row, 15, "Flange\nAnalysis\nTemperature", head)
row+=1
worksheet.conditional_format('H2:P'+str(len(Larr)+1), {'type': 'blanks', 'format': off})
for i in Larr:
	worksheet.write(row,  0, "L"+str(i.L))
	worksheet.write(row,  1, i.case)
	worksheet.write(row,  2, i.stype)
	worksheet.write(row,  3, i.name)
	worksheet.write(row,  4, "Suppress" if i.isSuppress else "Keep")
	worksheet.write(row,  5, otype(i.stype))
	worksheet.write(row,  6, i.cmthd)
#	worksheet.write(row,  7, "")
	worksheet.write(row,  8, i.hstif)
	worksheet.write(row,  9, "EC" if i.stype == "HGR" or i.stype == "HYD" or i.stype == "OPE" or i.stype == "SUS" else None)
	worksheet.write(row, 10, "PMax" if i.cmthd == '' or i.cmthd == "Algebraic" else None)
	worksheet.write(row, 11, "EC" if i.cmthd == '' or i.cmthd == "Algebraic" else None)
	worksheet.write(row, 12, "Sh_min" if i.stype == "SUS" or i.stype == "OCC" else None)
	worksheet.write(row, 13, 1.0000 if i.stype == "HGR" or i.stype == "HYD" or i.stype == "OPE" or i.stype == "SUS" else None, digit)
#	worksheet.write(row, 14, "")
	worksheet.write(row, 15, "None")
	row+=1
worksheet.autofit()  # přizpůsobí šířku sloupců obsahu buňky
worksheet.freeze_panes(1, 3)
workbook.close()

# vim:tw=78:ts=4:sts=4:sw=4:noexpandtab:
