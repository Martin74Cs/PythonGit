#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
##
##  PURPOSE :
##
##  DATE    : September 30 2024
##  AUTHOR  : Milan Šimko <milan.simko@tractebel.engie.com>
##  VERSION : 0.01
##
##  ENCODING: UTF-8
##
##  USAGE   : -
##  OPTIONS : -
##
##  NOTES   :
##
################################################################################
import os
import sys
import xlwings as xw

############################## GLOBÁLNÍ PROMĚNNÉ ###############################
generateSCR: bool = True
generateXLS: bool = False
generateTXT: bool = False
maxlevel: int = 2

#################################### METODY ####################################
def num2str(num: float, precision: int = None, NaN: str = "—") -> str:
	if num is None:               # NoneType
		return NaN
	elif isinstance(num, float):  # FloatType
		if precision is not None:
			pattern = "{:,."+str(precision)+"f}"
			retval = pattern.format(num)
		else:
			pattern = "{:,}"
			retval = pattern.format(round(num))
		return retval.replace(",", " ").replace(".", ",")
	elif isinstance(num, int):    # IntType
		if precision is not None:
			pattern = "{:,d}"+" "*(precision + 1) if precision != 0 else "{:,d}"
		else:
			pattern = "{:,}"
		retval = pattern.format(num)
		return retval.replace(",", " ")
	elif isinstance(num, str):    # StrType
		return num

def str2str(txt: str, NaS: str = "—") -> str:
	if txt is None:
		return NaS
	elif isinstance(txt, str):    # StrType
		return txt

def str2len(txt: str, length: int, NaS: str = "") -> str:
	if txt is None:
		return NaS
	elif isinstance(txt, str):    # StrType
		if len(txt) > length:
			return txt[:length] + "..."
		return txt

def itmById(_lst: list, _id: int):
	for item in _lst:
		found = item.find_by_id_recursive(_id)
		if found:
			return found
	return None

def objById(_lst: list, _id: int) -> object:
	return next((_ for _ in _lst if _.id == _id), None)

def objByTag(_lst: list, _tag: str) -> object:
	#_idx = [_.tag for _ in _lst].index(_tag)
	#_lst[_idx]
	return _lst[[_.tag for _ in _lst].index(_tag)]

def add(_lst: list, _obj: object, _id: int = None) -> None:
	# Rodič / ukazatel na jiný záznam není definovaný
	for item in _lst:
		if item.id == _obj.id:
			raise ValueError("Item ", item.id, " already exists")
	if _id is None:
		_lst.append(_obj)
	# Potomek / ukazatel na jiný záznam je definovaný
	if _id is not None:
#		ffound = False
#		for item in _lst:
#			print("CHILD", int(item.id), int(_id))
#			if int(item.id) == int(_id):
#				ffound = True
#				break
#		print(ffound)
#		if ffound == False:
#			raise ValueError("Parent item ", _id, " is not in list")
#		print("cont")
		for item in _lst:
			if item.id == _id:
				item.subitem.append(_obj)
				break
			add(item.subitem, _obj, _id)

def exportAsXLS(items: list, sheet: object, filterById: int = None) -> None:
	rec: int = 1
	row: int = 7  # první řádek v Excelu pro tisk dat
	for item in items:
		if filterById is not None and item.munit.id != filterById:  # filter
			continue
		row, rec = item.printItemAsXLS(sheet=sheet, row=row, record=rec)
	cells = sheet.range(f'E{row}:T{row}')
	cells.api.Borders(8).Weight = 3  # xlThick
	if Document.notes:
		cell = sheet.range(f'E{row}')
		cell.value = "POZNÁMKY:\n" + Document.notes
		cell.api.Font.Name = 'Courier New'
		cell.api.Font.Size = 10
		cell.api.WrapText = True      # povolí zalamování textu v buňce
#		cell.api.EntireRow.AutoFit()  # automaticky přispůsobí výšku řádku obsahu buňky
		cell.row_height = 14*cell.value.count('\n')
		cells = sheet.range(f'E{row}:T{row}')
		cells.api.Merge()
		cells = sheet.range(f'E{row+1}:T{row+1}')
		cells.api.Borders(8).Weight = 3  # xlThick

def exportAsTXT(items: list, filterById: int = None) -> None:
	rec: int = 1
	print("    ||Č. |     |     |OZNAČ.  |                                        |  |TECHNICKÝ       |PRACOVNÍ                |GEOMETR.|OBJEMOVÝ |EL.  |      |        ")
	print("GUID||ŘÁ.|IO/SO|PS   |ZAŘÍZ.  |NÁZEV ZAŘÍZENÍ                          |KS|PARAMETR        |TEKUTINA                |OBJEM   |PRŮTOK   |PŘÍK.|HMOTN.|POZNÁMKA")
	print(Item.sep.replace('-', '+'))
	for item in items:
		if filterById is not None and item.munit.id != filterById:  # filter
			continue
		rec = item.printItemAsTXT(record=rec)
	print(Item.sep)
	if Document.notes:
		print("POZNÁMKY")
		print(Document.notes + Item.sep)

class Fluid:
	pass

#################################### TŘÍDY #####################################
class Item:
	class Fluid:
		def __init__(self, _parameter: object, _fluid: str, _volume: float, _flowrate: float, note: str = None) -> None:
			self.__fluid: str = _fluid             # provozní tekutina
			self.__volume: float = _volume         # objem
			self.__flowrate: float = _flowrate     # průtok (objemový)
			self.__parameter: object = _parameter  # nějaký parametr (výkon / kapacita / nosnost / teplota / tlak / ...)
			self.__note: str = note                # poznámka

		# fluid (get/set)
		@property
		def fluid(self) -> str: return self.__fluid
		@fluid.setter
		def fluid(self, val: str): self.__fluid = val
		# volume (get/set)
		@property
		def volume(self) -> float: return self.__volume
		@volume.setter
		def volume(self, val: float): self.__volume = val
		# flowrate (get/set)
		@property
		def flowrate(self) -> float: return self.__flowrate
		@flowrate.setter
		def flowrate(self, val: float): self.__flowrate = val
		# parameter (get/set)
		@property
		def parameter(self) -> object: return self.__parameter
		@parameter.setter
		def parameter(self, val: object): self.__parameter = val
		# note (get/set)
		@property
		def note(self) -> str: return self.__note
		@note.setter
		def note(self, val: str): self.__note = val
	# end of class Fluid

	class Param:
		def __init__(self, _value: float, _unit: str) -> None:
			self.__value: float = _value  # hodnota
			self.__unit: str = _unit      # jednotka

		# value (get/set)
		@property
		def value(self) -> str: return self.__value
#		@value.setter
#		def value(self, val: str): self.__value = val
		# unit (get/set)
		@property
		def unit(self) -> str: return self.__unit
#		@unit.setter
#		def unit(self, val: str): self.__unit = val
	# end of class Param

	def __init__(self, _id: int, _cunit: object, _munit: object, _tag: str, _name: str, _pcs: int, _type: str = None, PU: bool = False, note: str = None) -> None:
		self.__id: int = _id             # unikátní identifikátor
		self.__cunit: object = _cunit    # reference na inženýrský / stavební objekt
		self.__munit: object = _munit    # reference na provozní soubor
		self.__revNo: int = None         # číslo revize

		self.__tag: str = _tag           # označení
		self.__name: str = _name         # název
		self.__pcs: int = _pcs           # kusů
		self.__type: str = _type         # typ

		self.__fluid: list = []          # provozní tekutina
		self.__dimensionX: float = None  # rozměr
		self.__dimensionY: float = None  # rozměr
		self.__dimensionZ: float = None  # rozměr
		self.__material: str = None      # materiál
		self.__heating: bool = None      # otop
		self.__mass: float = None        # hmotnost
		self.__insul: str = None         # izolace
		self.__anchor: bool = None       # kotvení
		self.__power: float = None       # výkon
		self.__noise: float = None       # hluk
		self.__note: str = note          # poznámka
		self.__PU: bool = PU             # balená jednotka

		self.__subitem: list = []        #

	# id (get/set)
	@property
	def id(self) -> int: return self.__id
	# cunit (get/set)
	@property
	def cunit(self) -> object: return self.__cunit
	@cunit.setter
	def cunit(self, val: object): self.__cunit = val
	# munit (get/set)
	@property
	def munit(self) -> object: return self.__munit
	@munit.setter
	def munit(self, val: object): self.__munit = val
	# revNo (get/set)
	@property
	def revNo(self) -> str: return self.__revNo
	@revNo.setter
	def revNo(self, val: str): self.__revNo = val
	# tag (get/set)
	@property
	def tag(self) -> str: return self.__tag
	@tag.setter
	def tag(self, val: str): self.__tag = val
	# name (get/set)
	@property
	def name(self) -> str: return self.__name
	@name.setter
	def name(self, val: str): self.__name = val
	# pcs (get/set)
	@property
	def pcs(self) -> int: return self.__pcs
	@pcs.setter
	def pcs(self, val: int): self.__pcs = val
	# type (get/set)
	@property
	def type(self) -> str: return self.__type
	@type.setter
	def type(self, val: str): self.__type = val
	# fluid (get/set)
	@property
	def fluid(self) -> list: return self.__fluid
	@fluid.setter
	def fluid(self, val: list): self.__fluid.append(val)
#	# dimensionX (get/set)
#	@property
#	def dimensionX(self) -> float: return self.__dimensionX
#	@dimensionX.setter
#	def dimensionX(self, val: float): self.__dimensionX = val
#	# dimensionY (get/set)
#	@property
#	def dimensionY(self) -> float: return self.__dimensionY
#	@dimensionY.setter
#	def dimensionY(self, val: float): self.__dimensionY = val
#	# dimensionZ (get/set)
#	@property
#	def dimensionZ(self) -> float: return self.__dimensionZ
#	@dimensionZ.setter
#	def dimensionZ(self, val: float): self.__dimensionZ = val
	# material (get/set)
	@property
	def material(self) -> str: return self.__material
	@material.setter
	def material(self, val: str): self.__material = val
	# heating (get/set)
	@property
	def heating(self) -> bool: return self.__heating
	@heating.setter
	def heating(self, val: bool): self.__heating = val
	# mass (get/set)
	@property
	def mass(self) -> float: return self.__mass
	@mass.setter
	def mass(self, val: float): self.__mass = val
	# insul (get/set)
	@property
	def insul(self) -> str: return self.__insul
	@insul.setter
	def insul(self, val: str): self.__insul = val
	# anchor (get/set)
	@property
	def anchor(self) -> bool: return self.__anchor
	@anchor.setter
	def anchor(self, val: bool): self.__anchor = val
	# power (get/set)
	@property
	def power(self) -> float: return self.__power
	@power.setter
	def power(self, val: float): self.__power = val
	# noise (get/set)
	@property
	def noise(self) -> float: return self.__noise
	@noise.setter
	def noise(self, val: float): self.__noise = val
	# note (get/set)
	@property
	def note(self) -> str: return self.__note
	@note.setter
	def note(self, val: str): self.__note = val
	# PU (get/set)
	@property
	def PU(self) -> bool: return self.__PU
	@PU.setter
	def PU(self, val: bool): self.__PU = val
	# subitem (get/set)
	@property
	def subitem(self) -> str: return self.__subitem
	@subitem.setter
	def subitem(self, val: object):
		if isinstance(val, list):
			self.__subitem = val
		else:
			raise ValueError("subitem must be a list")

	def find_by_id_recursive(self, _id: int):
		if self.id == _id:
			return self
		for item in self.subitem:
			found = item.find_by_id_recursive(_id)
			if found:
				return found
		return None

	def setWidth(_wd: list) -> str:
		size: int = len(_wd)
		sep: str = ""
		for idx in range(0,size):
			if idx < size - 1:
				sep+= "-"*_wd[idx] + "+"
#				sep+= "─"*_wd[idx] + "┼"
			else:
				sep+= "-"*_wd[idx]
#				sep+= "─"*_wd[idx]
		return sep

	#           GUID     row   SO/IO        PS         tag                name   pcs    param  munit  fluid  volume flow   power   mass  note
	fmt: str = "{:04d}||{:>3s}|{:2s} {:2s}|{:2s} {:2s}|{:8s}|{:40s}|{:>2s}|{:>6s} {:9s}|{:24s}|{:>8s}|{:>9s}|{:>5s}|{:>6s}|{:20s}"
#	fmt: str = "{:>2s}│{:5s}│\033[1m{:5s}\033[0m│{:30s}│{:>2s}│{:>6s} {:9s}│{:24s}│{:>8s}│{:>8s}│{:>6s}│{:>5s}│{:45s}"
	sep: str = setWidth([4, 0, 3, 5, 5, 8, 40, 2, 16, 24, 8, 9, 5, 6, 20])

	def printItemAsTXT(self, level: int = 0, record: int = 1) -> int:
		global maxlevel

		if self.fluid and len(self.fluid) > 1:
			if (self.fluid[0].parameter.value != "" and
			    self.fluid[0].parameter.unit  != "" and
			    self.fluid[0].fluid           != "" and
			    self.fluid[0].volume          != "" and
			    self.fluid[0].flowrate        != ""):
				self.fluid.insert(0, self.Fluid(self.Param("", ""), "", "", "", ""))

		if level == 0 and record != 1:
			print(self.sep)
		if not self.fluid:  # zařízení nemá definován seznam provozní tekutin
			if level < maxlevel:
				print(self.fmt.format(
				      self.id,                                    # unikátní identifikátor
				      num2str(record, 0),                         # číslo záznamu
				      self.cunit.pfx, f"{self.cunit.num:02d}",    # číslo IO / SO
				      self.munit.pfx, f"{self.munit.num:02d}",    # číslo PS
				      self.tag,                                   # tag zařízení
				      "  "*level + self.name.upper(),             # název zařízení
				      num2str(self.pcs, 0),                       # kusů
				      '—', '',                                    # technický parametr
				      '—', '—', '—',                              # provozní tekutina / objem / objemový průtok
				      num2str(self.power, 0),                     # elektrický příkon
				      num2str(self.mass, 0),                      # hmotnost
				      str2len(self.note, 17) if self.note is not None else ""  # poznámka
				))
		elif self.fluid: # zařízení má definován seznam provozních tekutin
			tmp: int = 1
			for f in self.fluid:
				# První řádek
				if tmp == 1 and level < maxlevel:
					print(self.fmt.format(
					      self.id,                                                       # unikátní identifikátor
					      num2str(record, 0),                                            # číslo záznamu
					      self.cunit.pfx, f"{self.cunit.num:02d}",                       # číslo IO / SO
					      self.munit.pfx, f"{self.munit.num:02d}",                       # číslo PS
					      self.tag,                                                      # tag zařízení
					      "  "*level + self.name.upper(),                                # název zařízení
					      num2str(self.pcs, 0),                                          # kusů
					      num2str(f.parameter.value, 0), str2str(f.parameter.unit, ''),  # technický parametr
					      str2str(f.fluid),                                              # provozní tekutina
					      num2str(f.volume, 1),                                          # objem
					      num2str(f.flowrate, 1),                                        # objemový průtok
					      num2str(self.power, 0),                                        # elektrický příkon
					      num2str(self.mass, 0),                                         # hmotnost
					      str2len(self.note, 17) if self.note is not None else str2len(f.note, 17) if f.note is not None else ""  # poznámka
					))
				# Další řádky
				elif tmp >= 2 and level < maxlevel:
					print(self.fmt.format(
					      self.id,                                                       # unikátní identifikátor
					      '',                                                            # číslo záznamu
					      '', '',                                                        # číslo IO / SO
					      '', '',                                                        # číslo PS
					      '',                                                            # tag zařízení
					      '',                                                            # název zařízení
					      '',                                                            # kusů
					      num2str(f.parameter.value, 0), str2str(f.parameter.unit, ''),  # technický parametr
					      str2str(f.fluid),                                              # provozní tekutina
					      num2str(f.volume, 1),                                          # geometrický objem
					      num2str(f.flowrate, 1),                                        # objemový průtok
					      '',                                                            # elektrický příkon
					      '',                                                            # hmotnost
					      str2len(f.note, 17) if f.note is not None else ""              # poznámka
					))
				tmp+= 1
		else:
			raise ValueError("oops")
		if level < maxlevel: record+= 1  # inkrementuje čítač řádků
		for item in self.subitem:
			record = item.printItemAsTXT(level + 1, record)
		return record

	def printItemAsXLS(self, sheet: object, row: int, level: int = 0, record: int = 1) -> int:
		global maxlevel

		cells = sheet.range(f'E{row}:T{row}')

		# Testuje, zda je v seznamu provozních tekutin více než jeden záznam.
		if self.fluid and len(self.fluid) > 1:
			if (self.fluid[0].parameter.value != "" and
			    self.fluid[0].parameter.unit  != "" and
			    self.fluid[0].fluid           != "" and
			    self.fluid[0].volume          != "" and
			    self.fluid[0].flowrate        != ""):
				self.fluid.insert(0, self.Fluid(self.Param("", ""), "", "", "", ""))

		if level == 0 and record != 1:
			cells.api.Borders(8).LineStyle = 1  # xlContinuous
#			cells.api.Borders(8).Weight = 3     # xlThick
			cells.api.Borders(8).Weight = 2     # xlThick

		if not self.fluid:  # zařízení nemá definován seznam provozních tekutin
			if not row % 2:
				cells = sheet.range(f'E{row}:T{row}')
				cells.color = (242,242,242)  # RGB for tolerant pink
			if level < maxlevel:
				cell = sheet.range(f'A{row}')                                # předznamenání Inženýrského objektu / Stavebního objektu
				cell.color = (242,242,242)
				cell.value = self.cunit.pfx
				cell = sheet.range(f'B{row}')                                # číslo Inženýrského objektu / Stavebního objektu
				cell.number_format = '00'
				cell.color = (217,217,217)
				cell.value = f"{self.cunit.num:02d}"
				cell = sheet.range(f'C{row}')                                # předznamenání Provozního souboru
				cell.color = (217,217,217)
				cell.value = self.munit.pfx
				cell = sheet.range(f'D{row}')                                # číslo Provozního souboru
				cell.number_format = '00'
				cell.color = (166,166,166)
				cell.value = f"{self.munit.num:02d}"
				cell = sheet.range(f'E{row}')                                # číslo záznamu
				cell.value = record
				cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter
				cell = sheet.range(f'F{row}')                                # balená jednotka
				cell.value = "ano" if self.PU else ""
				cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter
				if level < 1:
					cell = sheet.range(f'G{row}')                            # inženýrský objekt / Stavební objekt
					cell.formula = f'=A{row}&" "&TEXT(B{row},"00")'
					cell = sheet.range(f'H{row}')                            # provozní soubor
					cell.formula = f'=C{row}&" "&TEXT(D{row},"00")'
				cell = sheet.range(f'I{row}')                                # číslo zařízení
				cell.value = self.tag
				if level < 1:
					cell.api.Font.Bold = True
				cell = sheet.range(f'J{row}')                                # kusů
				cell.value = self.pcs
				cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter
				cell = sheet.range(f'K{row}')                                # název zařízení
				cell.value = "  "*level + self.name.upper()
				if level < 1:
					cell.api.Font.Bold = True
				if level > 0:
					cell.api.Font.Italic = True
					subcells = sheet.range(f'I{row}:S{row}')
#					subcells.api.Borders(8).LineStyle = 1  # xlContinuous
#					subcells.api.Borders(8).Weight = 1     # xlThick
					subcells.api.Borders(9).LineStyle = 1  # xlContinuous
					subcells.api.Borders(9).Weight = 1     # xlThick
				cell = sheet.range(f'L{row}')                                # typ
				cell.value = self.type
				cell = sheet.range(f'M{row}')                                # technický parametr
				cell.value = '—'
				cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
				cell = sheet.range(f'N{row}')                                # jednotka pro Technický parametr
				cell.value = ''
				cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignLeft
				cell = sheet.range(f'O{row}')                                # provozní tekutina
				cell.value = '—'
				cell = sheet.range(f'P{row}')                                # geometrický objem
				cell.value = '—'
				cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
				cell = sheet.range(f'Q{row}')                                # objemový průtok
				cell.value = '—'
				cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
				cell = sheet.range(f'R{row}')                                # elektrický příkon
				if level < 1 and self.PU and self.power is not None:
					cell.value = '∑ ' + num2str(self.power, 0)
				else:
					cell.value = num2str(self.power, 0)
				cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
				cell = sheet.range(f'S{row}')                                # hmotnost
				cell.value = num2str(self.mass, 0)
				cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
				cell = sheet.range(f'T{row}')                                # poznámka
				cell.value = self.note
				row+= 1
		elif self.fluid: # zařízení má definován seznam provozních tekutin
			tmp: int = 1
			for f in self.fluid:
				if not row % 2:
					cells = sheet.range(f'E{row}:T{row}')
					cells.color = (242,242,242)
				cell = sheet.range(f'A{row}')                                # předznamenání Inženýrského objektu / Stavebního objektu
				cell.color = (242,242,242)
				cell.value = self.cunit.pfx
				cell = sheet.range(f'B{row}')                                # číslo Inženýrského objektu / Stavebního objektu
				cell.number_format = '00'
				cell.color = (217,217,217)
				cell.value = f"{self.cunit.num:02d}"
				cell = sheet.range(f'C{row}')                                # předznamenání Provozního souboru
				cell.color = (217,217,217)
				cell.value = self.munit.pfx
				cell = sheet.range(f'D{row}')                                # číslo Provozního souboru
				cell.number_format = '00'
				cell.color = (166,166,166)
				cell.value = f"{self.munit.num:02d}"
				# První řádek
				if tmp == 1 and level < maxlevel:
					if level < 1:
						cell = sheet.range(f'G{row}')                            # inženýrský objekt / Stavební objekt
						cell.formula = f'=A{row}&" "&TEXT(B{row},"00")'
						cell = sheet.range(f'H{row}')                            # provozní soubor
						cell.formula = f'=C{row}&" "&TEXT(D{row},"00")'
					cell = sheet.range(f'E{row}')                                # číslo záznamu
					cell.value = record
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter
					cell = sheet.range(f'F{row}')                                # balená jednotka
					cell.value = "ano" if self.PU else ""
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter
					cell = sheet.range(f'I{row}')                                # číslo zařízení
					cell.value = self.tag
					if level < 1:
						cell.api.Font.Bold = True
					cell = sheet.range(f'J{row}')                                # kusů
					cell.value = self.pcs
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter
					cell = sheet.range(f'K{row}')                                # název zařízení
					cell.value = "  "*level + self.name.upper()
					if level < 1:
						cell.api.Font.Bold = True
					if level > 0:
						cell.api.Font.Italic = True
					cell = sheet.range(f'L{row}')                                # typ
					cell.value = self.type
					cell = sheet.range(f'M{row}')                                # technický parametr
					cell.value = num2str(f.parameter.value, 0)
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
					cell = sheet.range(f'N{row}')                                # jednotka pro technický parametr
					cell.value = str2str(f.parameter.unit, '')
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignLeft
					cell = sheet.range(f'O{row}')                                # provozní tekutina
					cell.value = str2str(f.fluid)
					cell = sheet.range(f'P{row}')                                # geometrický objem
					cell.value = num2str(f.volume, 1)
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
					cell = sheet.range(f'Q{row}')                                # objemový průtok
					cell.value = num2str(f.flowrate, 1)
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
					cell = sheet.range(f'R{row}')                                # elektrický příkon
					if level < 1 and self.PU and self.power is not None:
						cell.value = '∑ ' + num2str(self.power, 0)
					else:
						cell.value = num2str(self.power, 0)
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
					cell = sheet.range(f'S{row}')                                # hmotnost
					cell.value = num2str(self.mass, 0)
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
					cell = sheet.range(f'T{row}')                                # poznámka
					cell.value = self.note if self.note != "" else f.note
					row+= 1
				# Další řádky
				elif tmp >= 2 and level < maxlevel:
					cell = sheet.range(f'M{row}')                                # technický parametr
					cell.value = num2str(f.parameter.value, 0)
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
					cell = sheet.range(f'N{row}')                                # jednotka pro technický parametr
					cell.value = str2str(f.parameter.unit, '')
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignLeft
					cell = sheet.range(f'O{row}')                                # provozní tekutina
					cell.value = str2str(f.fluid)
					cell = sheet.range(f'P{row}')                                # geometrický objem
					cell.value = num2str(f.volume, 1)
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
					cell = sheet.range(f'Q{row}')                                # objemový průtok
					cell.value = num2str(f.flowrate, 1)
					cell.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
					cell = sheet.range(f'T{row}')                                # poznámka
					cell.value = f.note
					row+= 1
				tmp+= 1
			subcells = sheet.range(f'I{row}:S{row}')
			subcells.api.Borders(8).LineStyle = 1  # xlContinuous
			subcells.api.Borders(8).Weight = 1     # xlThick
		else:
			raise ValueError("oops")
		if Document.notes:
			sheet.api.PageSetup.PrintArea = sheet.range(f'E1:T{row+1}').address
		else:
			sheet.api.PageSetup.PrintArea = sheet.range(f'E1:T{row}').address
		if level < maxlevel: record+= 1  # inkrementuje čítač záznamů
		for item in self.subitem:
			row, record = item.printItemAsXLS(sheet, row, level + 1, record)
		return [row, record]
# end of class Item

class Unit:
	def __init__(self, _id: int, _pfx: str, _num: int, _name: str, note: str = None) -> None:
		self.__id: int = _id      # unikátní identifikátor
		self.__pfx: str = _pfx    # předznamenání IO / SO / PS
		self.__num: int = _num    # číslo
		self.__sfx: str = None    # předznamenání
		self.__name: str = _name  # název / popis
		self.__note: str = note   # poznámky

	# id (get/set)
	@property
	def id(self) -> str: return self.__id
#	@id.setter
#	def id(self, val: str): self.__id = val
	# pfx (get/set)
	@property
	def pfx(self) -> str: return self.__pfx
#	@pfx.setter
#	def pfx(self, val: str): self.__pfx = val
	# num (get/set)
	@property
	def num(self) -> str: return self.__num
#	@num.setter
#	def num(self, val: str): self.__num = val
	# sfx (get/set)
	@property
	def sfx(self) -> str: return self.__sfx
#	@sfx.setter
#	def sfx(self, val: str): self.__sfx = val
	# name (get/set)
	@property
	def name(self) -> str: return self.__name
#	@name.setter
#	def name(self, val: str): self.__name = val
	# note (get/set)
	@property
	def note(self) -> str: return self.__note
#	@note.setter
#	def note(self, val: str): self.__note = val
# end of class Object

class Revision:
	last: str = None

	def __init__(self, _num: str, _date: str, _desc: str, _stat: str, _prep: str, _chkd: int, _appd: str) -> None:
		self.__num:  str = _num                      # číslo revize
		self.__date: str = _date                     # datum revize
		self.__desc: str = _desc                     # popis revize
		self.__stat: int = Revision.getIndex(_stat)  # status změny
		self.__prep: str = _prep                     # zpracoval
		self.__chkd: int = _chkd                     # kontroloval
		self.__appd: str = _appd                     # schválil
		Revision.last = self.__num                   # globální číslo revize

	# num (get/set)
	@property
	def num(self) -> str: return self.__num
#	@num.setter
#	def num(self, val: str): self.__num = val
	# date (get/set)
	@property
	def date(self) -> str: return self.__date
#	@date.setter
#	def date(self, val: str): self.__date = val
	# desc (get/set)
	@property
	def desc(self) -> str: return self.__desc
#	@desc.setter
#	def desc(self, val: str): self.__desc = val
	# stat (get/set)
	@property
	def stat(self) -> int: return self.__stat
#	@stat.setter
#	def stat(self, val: int): self.__stat = val
	# prep (get/set)
	@property
	def prep(self) -> str: return self.__prep
#	@prep.setter
#	def prep(self, val: str): self.__prep = val
	# chkd (get/set)
	@property
	def chkd(self) -> str: return self.__chkd
#	@chkd.setter
#	def chkd(self, val: str): self.__chkd = val
	# appd (get/set)
	@property
	def appd(self) -> str: return self.__appd
#	@appd.setter
#	def appd(self, val: str): self.__appd = val

	@staticmethod
	def getIndex(statusIndex):
		return {
			''   : 1,
			'DFT': 2,
			'PRL': 3,
			'FIN': 4,
			'CFC': 5,
			'CAN': 6,
			'ASB': 7,
			'AFL': 8
		}[statusIndex]
# end of class Revision

class Project:
	def __init__(self) -> None:
		self.__number: str = None    # číslo projektu
		self.__client: str = None    # zákazník
		self.__name: str = None      # název projektu

	# name (get/set)
	@property
	def name(self) -> str: return self.__name
	@name.setter
	def name(self, val: str): self.__name = val
	# number (get/set)
	@property
	def number(self) -> str: return self.__number
	@number.setter
	def number(self, val: str): self.__number = val
	# client (get/set)
	@property
	def client(self) -> str: return self.__client
	@client.setter
	def client(self, val: str): self.__client = val
# end of class Project

class Document:
	notes: str = None

	def __init__(self, _prefix: str, _number: int, _subdiv: str, _comment: str, _unitId = None) -> None:
		self.__unitId: int = _unitId      # filter
		self.__prefix: str = _prefix      # předznamenání
		self.__number: int = _number      # číslo dokumentu
		self.__subdiv: str = _subdiv      # číslo orientační
		self.__comment: str = _comment    # komentáře

	# unitId (get/set)
	@property
	def unitId(self) -> int: return self.__unitId
#	@unitId.setter
#	def unitId(self, val: int): self.__unitId = val
	# prefix (get/set)
	@property
	def prefix(self) -> str: return self.__prefix
#	@prefix.setter
#	def prefix(self, val: str): self.__prefix = val
	# number (get/set)
	@property
	def number(self) -> int: return self.__number
#	@number.setter
#	def number(self, val: int): self.__number = val
	# subdiv (get/set)
	@property
	def subdiv(self) -> str: return self.__subdiv
#	@subdiv.setter
#	def subdiv(self, val: str): self.__subdiv = val
	# comment (get/set)
	@property
	def comment(self) -> str: return self.__comment
#	@comment.setter
#	def comment(self, val: str): self.__comment = val
# end of class Document

def outputs(revisions: list, project: object, documents: list, items: list):
	global generateSCR
	global generateXLS
	global generateTXT
	global maxlevel

	# Zobrazení databáze
	if generateSCR:
		original_maxlevel = maxlevel; maxlevel = 10000
		exportAsTXT(items)
		maxlevel = original_maxlevel

	# Tisk databáze
	for document in documents:
		if generateTXT:
			try:
				# Uložení původního sys.stdout
				original_sys_stdout = sys.stdout
				if document.number is not None:
					with open(f"./OUTPUT/{document.prefix}{document.number}{Revision.last}.TXT", mode='w', encoding='utf-8', newline='\n') as f:
						sys.stdout = f
						exportAsTXT(items, document.unitId)
						print("vim:ff=unix:fenc=utf-8:")
						sys.stdout.flush()  # Ruční vyprázdnění bufferu
			except OSError as e:
				print(f"Došlo k chybě při zápisu do souboru: {e}")
			except Exception as e:
				print(f"Došlo k neočekávané chybě: {e}")
			finally:
				# Obnovení původního sys.stdout
				sys.stdout = original_sys_stdout
		# end of if generateTXT:
		if generateXLS:
			if document.number is not None:
				# Kopírování šablony
				os.system(f"cp -f /d/bin/py/equiplist.xlsx ./OUTPUT/{document.prefix}{document.number}{Revision.last}.xlsx")
				try:
					app = xw.App(visible=False)  # vytvoří instanci aplikace Excel na pozadí
					# Načtení existujícího sešitu
					wb = app.books.open(f"./OUTPUT/{document.prefix}{document.number}{Revision.last}.xlsx", read_only=False)
					# Vybrání listu titulní strany
					sheet = wb.sheets["titulni list"]
					sheet.range('E9' ).value = document.number   # číslo dokumentu
					sheet.range('C12').value = document.subdiv   # číslo orientační
					sheet.range('C13').value = project.number  # číslo projektu
					sheet.range('C18').value = project.client  # zákazník
					sheet.range('C19').value = project.name    # název projektu
					sheet.range('C21').value = document.comment  # komentáře
					# Tabulka revizních změn
#					ole_objects = sheet.api.Shapes
#					for ole_object in ole_objects:
#						print(ole_object.Name)
					tablerow: int = 52
					for revision in revisions:
						sheet.range(f'A{tablerow}').value = revision.num   # číslo změny
						sheet.range(f'B{tablerow}').value = revision.date  # datum změny
						sheet.range(f'C{tablerow}').value = revision.desc  # popis změny
#						sheet.api.Shapes('Drop Down 1').ControlFormat.ListIndex = FIXME typ dokumentu
#						sheet.api.Shapes('Drop Down 2').ControlFormat.ListIndex = FIXME stupeň utajení
						if tablerow == 52: sheet.api.Shapes('Drop Down 3').ControlFormat.ListIndex = revision.stat  # řádek 52
						if tablerow == 51: sheet.api.Shapes('Drop Down 4').ControlFormat.ListIndex = revision.stat  # řádek 51
						if tablerow == 50: sheet.api.Shapes('Drop Down 5').ControlFormat.ListIndex = revision.stat  # řádek 50
						if tablerow == 49: sheet.api.Shapes('Drop Down 6').ControlFormat.ListIndex = revision.stat  # řádek 49
						if tablerow == 48: sheet.api.Shapes('Drop Down 7').ControlFormat.ListIndex = revision.stat  # řádek 48
#						if tablerow == 47: sheet.api.Shapes('Drop Down 8').ControlFormat.ListIndex = revision.stat  # řádek 47
						sheet.range(f'E{tablerow}').value = revision.prep  # zpracoval
						sheet.range(f'F{tablerow}').value = revision.chkd  # kontroloval
						sheet.range(f'G{tablerow}').value = revision.appd  # schválil
						tablerow-= 1
					# Vybrání listu seznamu strojů a zařízení
					sheet = wb.sheets["seznam"]
					# Vyplnění buněk
					exportAsXLS(items, sheet, document.unitId)
					# Uložení a zavření sešitu
					try:
						wb.save()
					except Exception as e:
						print(f"Sešit nemohl být uložen běžným způsobem: {e}")
					try:
						wb.to_pdf()
					except Exception as e:
						print(f"Sešit nemohl být uložen jako PDF: {e}")
					try:
						wb.close()
					except Exception as e:
						print(f"Sešit nemohl být zavřen běžným způsobem: {e}")
				except Exception as e:
					print(f"Došlo k neočekávané chybě: {e}")
				finally:
					if 'app' in locals():
						try:
							app.quit()  # ukončí instanci aplikace Excel
						except Exception as e:
							print(f"Excel nemohl být ukončen běžným způsobem: {e}")
							app.kill()  # Násilné ukončení aplikace
			# end of if document.number is not None:
		# end of if generateXLS:
	# end of for document in documents:
	if generateXLS or generateTXT:
		print("\nHurá! Šup s tím do světa!")

# vim:tw=78:ts=4:sts=4:sw=4:noexpandtab:
