import sys                                      ; sys.path.append('D:\\bin\\py')
################################################################################
from equiplist import Item, add, objById
########### STAVEBNÍ OBJEKTY / INŽENÝRSKÉ OBJEKTY / PROVOZNÍ SOUBORY ###########
from units import *
########################## STRUKTURA STROJŮ A ZAŘÍZENÍ #########################
itms: list = []

SO = objById(objs,  1)  # reference na stavební objekt
PS = objById(objs, 18)  # reference na provozní soubor
#               ID  SO  PS  TAG         NÁZEV ZAŘÍZENÍ                          KS
add(itms, Item( 10, SO, PS, "H01"     , "Jeřáb výrobní haly"                  , 1 , "mostový"))
add(itms, Item( 20, SO, PS, "H02"     , "Jeřáb výrobní haly"                  , 2 , "mostový"))

PS = objById(objs, 19)
#               ID  SO  PS  TAG         NÁZEV ZAŘÍZENÍ                          KS                           ID
add(itms, Item( 30, SO, PS, "X01A"    , "Licí linka A"                        , 1 , "kontinuální", PU=True))
add(itms, Item( 40, SO, PS, "X01B"    , "Licí linka B"                        , 1 , "kontinuální", PU=True))
add(itms, Item( 50, SO, PS, "X01A.1"  , "Vsázkovácí zařízení"                 , 1                         ), 30)
add(itms, Item( 60, SO, PS, "X01B.1"  , "Vsázkovácí zařízení"                 , 1                         ), 40)
add(itms, Item( 51, SO, PS, "X01A.1.1", "Šaržovací vozík s výtahem"           , 1                         ), 50)
add(itms, Item( 61, SO, PS, "X01B.1.1", "Šaržovací vozík s výtahem"           , 1                         ), 60)
add(itms, Item( 52, SO, PS, "X01A.1.2", "Vibrační vsázkovací vozík"           , 1                         ), 50)
add(itms, Item( 62, SO, PS, "X01B.1.2", "Vibrační vsázkovací vozík"           , 1                         ), 60)
add(itms, Item( 70, SO, PS, "X01A.2"  , "Tavící pec"                          , 1 , "indukční"            ), 30)
add(itms, Item( 80, SO, PS, "X01B.2"  , "Tavící pec"                          , 1 , "indukční"            ), 40)
add(itms, Item( 90, SO, PS, "X01A.3"  , "Licí pec"                            , 1 , "indukční"            ), 30) # Licí (ustalovací) pec
add(itms, Item(100, SO, PS, "X01B.3"  , "Licí pec"                            , 1 , "indukční"            ), 40) # Licí (ustalovací) pec
add(itms, Item(101, SO, PS, "X01A 3.1", "Krystalizátor"                       , 1                         ), 90)
add(itms, Item(102, SO, PS, "X01B 3.1", "Krystalizátor"                       , 1                         ),100)
add(itms, Item(130, SO, PS, "X01A.4"  , "Ostřikové chladící zařízení"         , 1                         ), 30)
add(itms, Item(140, SO, PS, "X01B.4"  , "Ostřikové chladící zařízení"         , 1                         ), 40)
add(itms, Item(110, SO, PS, "X01A.4.1", "Válečková podpěra"                   , 1                         ),130)
add(itms, Item(120, SO, PS, "X01B.4.1", "Válečková podpěra"                   , 1                         ),140)
add(itms, Item(150, SO, PS, "X01A.5"  , "Tažné zařízení"                      , 1                         ), 30)
add(itms, Item(160, SO, PS, "X01B.5"  , "Tažné zařízení"                      , 1                         ), 40)
add(itms, Item(170, SO, PS, "X01A.6"  , "Frézovací centrum"                   , 1                         ), 30)
add(itms, Item(180, SO, PS, "X01B.6"  , "Frézovací centrum"                   , 1                         ), 40)
add(itms, Item(190, SO, PS, "X01A.7"  , "Střihací zařízení"                   , 1                         ), 30)
add(itms, Item(200, SO, PS, "X01B.7"  , "Střihací zařízení"                   , 1                         ), 40)
add(itms, Item(210, SO, PS, "X01A.8"  , "Navíjecí zařízení"                   , 1                         ), 30)
add(itms, Item(220, SO, PS, "X01B.8"  , "Navíjecí zařízení"                   , 1                         ), 40)

PS = objById(objs, 26)  # reference na provozní soubor
#               ID  SO  PS  TAG         NÁZEV ZAŘÍZENÍ                          KS             ID
add(itms, Item(290, SO, PS, "X02"     , "Válcovací linka"                     , 1 , PU=True))
add(itms, Item(291, SO, PS, "X02.1A"  , "Navíjecí/Odvíjecí zařízení"          , 1          ), 290)
add(itms, Item(292, SO, PS, "X02.1B"  , "Navíjecí/Odvíjecí zařízení"          , 1          ), 290)
add(itms, Item(293, SO, PS, "X02.2"   , "Válcovací stolice"                   , 1          ), 290)
add(itms, Item(294, SO, PS, "X02.2.1" , "Pracovní válec"                      , 2          ), 293)
add(itms, Item(295, SO, PS, "X02.2.2" , "Opěrný válec"                        , 2          ), 293)
add(itms, Item(296, SO, PS, "X02.3"   , "Odvíjecí buben"                      , 1          ), 290)

PS = objById(objs, 27)  # reference na provozní soubor
#               ID  SO  PS  TAG         NÁZEV ZAŘÍZENÍ                          KS                  ID
add(itms, Item(300, SO, PS, "X03"     , "Žíhací linka"                        , 1 , PU=True     ))
add(itms, Item(301, SO, PS, "X03.1"   , "Základ poklopové pece"               , 7               ), 300)
add(itms, Item(302, SO, PS, "X03.2"   , "Redukční stanice"                    , 1               ), 300)
#dd(itms, Item(303, SO, PS, "X03.3"   , "Rozvaděč medií"                      , 7               ), 300)
add(itms, Item(901, SO, PS, "X03.3A"  , "Rozvaděč medií"                      , 1               ), 300)
add(itms, Item(902, SO, PS, "X03.3B"  , "Rozvaděč medií"                      , 1               ), 300)
add(itms, Item(903, SO, PS, "X03.3C"  , "Rozvaděč medií"                      , 1               ), 300)
add(itms, Item(904, SO, PS, "X03.3D"  , "Rozvaděč medií"                      , 1               ), 300)
add(itms, Item(905, SO, PS, "X03.3E"  , "Rozvaděč medií"                      , 1               ), 300)
add(itms, Item(906, SO, PS, "X03.3F"  , "Rozvaděč medií"                      , 1               ), 300)
add(itms, Item(907, SO, PS, "X03.3G"  , "Rozvaděč medií"                      , 1               ), 300)
#dd(itms, Item(304, SO, PS, "X03.4"   , "Ohřívací zvon"                       , 3               ), 300)
add(itms, Item(908, SO, PS, "X03.4A"  , "Ohřívací zvon"                       , 1 , "elektrický"), 300)
add(itms, Item(909, SO, PS, "X03.4B"  , "Ohřívací zvon"                       , 1 , "elektrický"), 300)
add(itms, Item(910, SO, PS, "X03.4C"  , "Ohřívací zvon"                       , 1 , "elektrický"), 300)
#dd(itms, Item(305, SO, PS, "X03.5"   , "Chladící zvon"                       , 4               ), 300)
add(itms, Item(911, SO, PS, "X03.5A"  , "Chladící zvon"                       , 1               ), 300)
add(itms, Item(912, SO, PS, "X03.5B"  , "Chladící zvon"                       , 1               ), 300)
add(itms, Item(913, SO, PS, "X03.5C"  , "Chladící zvon"                       , 1               ), 300)
add(itms, Item(914, SO, PS, "X03.5D"  , "Chladící zvon"                       , 1               ), 300)
add(itms, Item(306, SO, PS, "X03.6"   , "Vývěva"                              , 1               ), 300)
#dd(itms, Item(915, SO, PS, "X03.6A"  , "Vývěva"                              , 1               ), 300)
#dd(itms, Item(916, SO, PS, "X03.6B"  , "Vývěva"                              , 1               ), 300)

SO = objById(objs,  7)  # reference na stavební objekt
PS = objById(objs, 28)  # reference na provozní soubor
#               ID  SO  PS  TAG         NÁZEV ZAŘÍZENÍ                          KS
add(itms, Item(310, SO, PS, "X04"     , "Mořící linka"                        , 1 , PU=True, note="stávající SO 013"))

SO = objById(objs,  8)  # reference na stavební objekt
PS = objById(objs, 29)  # reference na provozní soubor
#               ID  SO  PS  TAG .       NÁZEV ZAŘÍZENÍ                          KS
add(itms, Item(320, SO, PS, "X05"     , "Dělící linka"                        , 1 , PU=True, note="stávající SO 006"))

SO = objById(objs,  4)  # reference na stavební objekt
PS = objById(objs, 20)  # reference na provozní soubor
#               ID  SO  PS  TAG .       NÁZEV ZAŘÍZENÍ                          KS             ID
add(itms, Item(330, SO, PS, "X06A"    , "Odsávací jednotka licí linky"        , 1 , PU=True))
add(itms, Item(340, SO, PS, "X06B"    , "Odsávací jednotka licí linky"        , 1 , PU=True))
add(itms, Item(331, SO, PS, "X06A.1"  , "Odsávací jednotka tavící a licí pece", 1          ), 330)
add(itms, Item(341, SO, PS, "X06B.1"  , "Odsávací jednotka tavící a licí pece", 1          ), 340)
add(itms, Item(332, SO, PS, "X06A.2"  , "Odsávací jednotka frézovacího centra", 1          ), 330)
add(itms, Item(342, SO, PS, "X06B.2"  , "Odsávací jednotka frézovacího centra", 1          ), 340)
add(itms, Item(350, SO, PS, "X07"     , "Odsávací jednotka válcovací linky"   , 1 , PU=True))

SO = objById(objs,  6)  # reference na stavební objekt
PS = objById(objs, 31)  # reference na provozní soubor
#               ID  SO  PS  TAG .       NÁZEV ZAŘÍZENÍ                          KS             ID
add(itms, Item(360, SO, PS, "X08"     , "Chlazení zařízení"                   , 1 , PU=True))
add(itms, Item(361, SO, PS, "X08.1"   , "Chladící systém tavící pece"         , 1          ), 360)
add(itms, Item(362, SO, PS, "X08.2"   , "Chladící systém licí pece"           , 1          ), 360)
add(itms, Item(363, SO, PS, "X08.3"   , "Chladící systém poklopové pece"      , 1          ), 360)

# vim:tw=10000:ts=4:sts=4:sw=4:noexpandtab:
