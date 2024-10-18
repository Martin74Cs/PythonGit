import sys                                      ; sys.path.append('D:\\bin\\py')
################################################################################
from equiplist import Item, itmById
################################################################################
from items import *
################################################################################
# Jeřáb obsluhující linku kontinuálního lití
for i in [10]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(15000., "kg"), None, None, None)
	itm.mass  = 12570. # kg
	itm.power = 11.71  # kW
	itm.noise = 65.    # dB(A) FIXME
# Jeřáby obsluhující stolici válcování za studena na žíhací poklopové pece
for i in [20]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(25000., "kg"), None, None, None)
	itm.mass  = None    # kg FIXME
	itm.power = None    # kW FIXME

################################################################################
# Linka kontinuálního lití
for i in [30, 40]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(2000., "kg/h"), "mosaz", None, None)
	itm.power = 1515.  # kW

# Šaržovací vozík s výtahem
for i in [51, 61]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(None, None), "vsázka", None, None)
	itm.power = 5.5  # kW
	itm.note  = ""

# Vibrační vsázkovací vozík
for i in [52, 62]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(None, None), "vsázka", None, None)

# Tavící pec linky kontinuálního lití
for i in [70, 80]:
	itm = itmById(itms, i)
#	itm.fluid = Item.Fluid(Item.Param(2400., "kg/h"     ), "mosaz"                  , None, None   )
	itm.fluid = Item.Fluid(Item.Param(None , None       ), "chladící voda procesní" , None,    17.1)
#	itm.fluid = Item.Fluid(Item.Param(None , None       ), "chladící voda havarijní", None,     5. )
	itm.fluid = Item.Fluid(Item.Param(None , None       ), "odpadní voda průmyslová", None,     5. )
	itm.fluid = Item.Fluid(Item.Param( 400., "kWh/týden"), "zemní plyn"             , None, None   )
#	itm.fluid = Item.Fluid(Item.Param(None , None       ), "odplyny"                , None, 10000. , note="objemový průtok v [Nm3/h]")
	itm.mass  = 7000.  # kg
	itm.power = 850.   # kW
	itm.noise = 85.    # dB(A)

# Licí (ustalovací) pec linky kontinuálního lití
for i in [90, 100]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(None , None       ), "chladící voda procesní" , None,    9.1)
#	itm.fluid = Item.Fluid(Item.Param(None , None       ), "chladící voda havarijní", None,    7. )
	itm.fluid = Item.Fluid(Item.Param( 400., "kWh/týden"), "zemní plyn"             , None, None  )
#	itm.fluid = Item.Fluid(Item.Param(None , None       ), "odplyny"                , None, 5000. , note="objemový průtok v [Nm3/h]")
	itm.mass  = None  # kg
	itm.power = 250.  # kW
	itm.noise = 80.   # dB(A)

# Válečková podpěra
for i in [110, 120]:
	itm = itmById(itms, i)

# Ostřikové chladící zařízení
for i in [130, 140]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(None, None    ), "chladící voda průmyslová", None,  4.2)
	itm.fluid = Item.Fluid(Item.Param(  5., "bar(g)"), "tlakový vzduch"          , None, None)

# Tažné zařízení
for i in [150, 160]:
	itm = itmById(itms, i)
	itm.power = 23.  # kW

# Frézovací centrum
for i in [170, 180]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(  5., "bar(g)"), "tlakový vzduch", None, None)
	itm.power = 40.5  # kW
	itm.noise = 85.   # dB(A)

# Střihací zařízení
for i in [190, 200]:
	itm = itmById(itms, i)
	itm.power = 18.   # kW
	itm.noise = 80.   # dB(A)

# Navíjecí zařízení
for i in [210, 220]:
	itm = itmById(itms, i)
	itm.power = 8.2   # kW

################################################################################
# Válcovací linka
for i in [290]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(None, None), "chladící voda procesní", None,    140.)
	itm.fluid = Item.Fluid(Item.Param(None, None), "tlakový vzduch"        , None,    130., note="objemový průtok v [Nm3/h]")
#	itm.fluid = Item.Fluid(Item.Param(None, None), "vzduch s prachem"      , None, 120000., note="objemový průtok v [Nm3/h]")
	itm.power = 4000.  # kW
	itm.noise = 85.    # dB(A)

# Navíjecí/odvíjecí zařízení
for i in [291, 292]:
	itm = itmById(itms, i)
	itm.power = itm.pcs*600.  # kW

# Válcovací stolice
for i in [293]:
	itm = itmById(itms, i)
	itm.power = itm.pcs*2*900.  # kW

# Odvíjecí buben
for i in [296]:
	itm = itmById(itms, i)
	itm.power = itm.pcs*160.  # kW

################################################################################
# Poklopové pece / EBNER
# Nabídka je na 11 základů pro poklopy, ale bude 11 základů ... pišvejc = 7/11
# Nabídka je na  5 ohřevových poklopů, ale budou 3 poklopy  ... pišvejc = 3/5
# Nabídka je na  6 chladících poklopů, ale budou 4 poklopy  ... pišvejc = 4/6
for i in [300]:
	itm = itmById(itms, i)
	itm.power = 2080.  # kW

# Základ poklopové pece
for i in [301]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(4., "bar(g)"), "chladící voda procesní", None, itm.pcs*(15.*1/11.))
	itm.mass  = None  # kg FIXME
	itm.power = itm.pcs*37.  # kW

# Rozvaděč medií
for i in [901, 902, 903, 904, 905, 906, 907]:
	itm = itmById(itms, i)
#	itm.fluid = Item.Fluid(Item.Param( 4. , "bar(g)"    ), "chladící voda"           , None, None)
#	itm.fluid = Item.Fluid(Item.Param(14. , "bar(g)"    ), "dusík"                   , None, None)
#	itm.fluid = Item.Fluid(Item.Param( 3. , "bar(g)"    ), "vodík"                   , None, None)

# Ohřívací zvon
for i in [908, 909, 910]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(14., "bar(g)"), "dusík", None, itm.pcs*(525.*1/5.), note="objemový průtok v [Nm3/h]")
	itm.fluid = Item.Fluid(Item.Param( 3., "bar(g)"), "vodík", None, itm.pcs*(102.*1/5.), note="objemový průtok v [Nm3/h]")
	itm.mass  = None   # kg FIXME
	itm.power = 580.+0.75  # kW

# Chladící zvon
for i in [911, 912, 913, 914]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(4., "bar(g)"), "chladící voda procesní", None, itm.pcs*( 78.*1/6.))
	itm.mass  = None         # kg FIXME
	itm.power = itm.pcs*5.5*2  # kW

# Vývěva
for i in [306]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(None, None), "ochranná atmosféra", None, itm.pcs*(250.*1/2.), note="objemový průtok v [Nm3/h]")
	itm.note  = "zjistit od PCI počet ks"
	itm.power = itm.pcs*30.  # kW

################################################################################
# Mořící linka
for i in [310]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(None, None    ), "demineralizovaná voda", None,  2. )
	itm.fluid = Item.Fluid(Item.Param(  4., "bar(g)"), "chladící voda"        , None,  7. )
	itm.fluid = Item.Fluid(Item.Param(  6., "bar(g)"), "tlakový vzduch"       , None, 37.5, note="objemový průtok v [Nm3/h]")
	itm.power = 660.  # kW

################################################################################
# Dělící linka
for i in [320]:
	itm = itmById(itms, i)

################################################################################
# Odsávací jednotka licí linky
for i in [330, 340]:
	itm = itmById(itms, i)
	itm.power = 280.+56.  # kW

# Odsávací jednotka tavící a licí
for i in [331, 341]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(None, None), "odplyny", None, 40000., note="objemový průtok v [Nm3/h]")
	itm.mass  = 27400.  # kg
	itm.power = 280.    # kW
	itm.noise = 77.     # dB(A)

# Odsávací jednotka frézovacího centra
for i in [332, 342]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(None, None), "vzduch s třískami", None, 18000., note="objemový průtok v [Nm3/h]")
	itm.mass  = None    # kg FIXME
	itm.power = 56.     # kW
	itm.noise = 79.9    # dB(A)

# Odsávací jednotka válcovací linky
for i in [350]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(None, None), "vzduch s prachem", None, 120000., note="objemový průtok v [Nm3/h]")
	itm.mass  = None    # kg FIXME
	itm.power = 150.    # kW
	itm.noise = None    # dB(A) FIXME

################################################################################
for i in [361, 362]:
	itm = itmById(itms, i)
	itm.fluid = Item.Fluid(Item.Param(None, None), "chladící voda", None, None)

# vim:tw=10000:ts=4:sts=4:sw=4:noexpandtab:
