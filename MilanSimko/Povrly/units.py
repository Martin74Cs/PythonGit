import sys                                      ; sys.path.append('D:\\bin\\py')
################################################################################
from equiplist import Unit, add
########### STAVEBNÍ OBJEKTY / INŽENÝRSKÉ OBJEKTY / PROVOZNÍ SOUBORY ###########
objs: list = []

#                   IO
#                   SO
#              ID   PS   Č.  NÁZEV                                     POZNÁMKA
add(objs, Unit( 1, "SO",  2, "Nová výrobní hala"                     , None))
add(objs, Unit( 2, "SO",  3, "Potrubní mosty"                        , None))
add(objs, Unit( 3, "SO",  4, "Rozvodna VN a NN"                      , None))
add(objs, Unit( 4, "SO",  5, "Základy vzduchotechniky"               , None))
add(objs, Unit( 5, "SO",  6, "Demolice"                              , None))
add(objs, Unit( 6, "SO",  8, "Strojovna chlazení"                    , None))
add(objs, Unit( 7, "SO",  9, "Moření"                                , None))
add(objs, Unit( 8, "SO", 10, "Nůžky"                                 , None))
add(objs, Unit( 9, "SO", 11, "Nová úpravna vody"                     , None))
add(objs, Unit(10, "IO",  1, "Dešťová kanalizace"                    , None))
add(objs, Unit(11, "IO",  2, "Splašková kanalizace"                  , None))
add(objs, Unit(12, "IO",  3, "Průmyslová kanalizace"                 , None))
add(objs, Unit(13, "IO",  4, "Pitná voda"                            , None))
add(objs, Unit(14, "IO",  5, "Požární voda"                          , None))
add(objs, Unit(15, "IO",  6, "Komunikace"                            , None))
add(objs, Unit(16, "IO",  7, "Vnější silnoproudá elektrotechnika"    , None))
add(objs, Unit(17, "IO",  8, "Vnější slaboproudé rozvody"            , None))
add(objs, Unit(18, "PS",  1, "Jeřáby nové výrobní haly"              , None))
add(objs, Unit(19, "PS",  2, "Technologie tavení a lití"             , None))
add(objs, Unit(20, "PS",  3, "Technologická vzduchotechnika"         , None))
add(objs, Unit(21, "PS",  4, "Rozvod zemního plynu"                  , None))
add(objs, Unit(22, "PS",  5, "Potrubní technologické rozvody vnitřní", None))
add(objs, Unit(23, "PS",  6, "Potrubní technologické rozvody vnější" , None))
add(objs, Unit(24, "PS",  7, "Silnoproudá elektrotechnika"           , None))
add(objs, Unit(25, "PS",  8, "Slaboproudé rozvody"                   , None))
add(objs, Unit(26, "PS",  9, "Technologie válcování"                 , None))
add(objs, Unit(27, "PS", 10, "Technologie žíhání"                    , None))
add(objs, Unit(28, "PS", 11, "Technologie moření"                    , None))
add(objs, Unit(29, "PS", 12, "Technologie stříhání"                  , None))
add(objs, Unit(30, "PS", 13, "Technologie úpravy vody"               , None))
add(objs, Unit(31, "PS", 14, "Technologie chlazení"                  , None))

# vim:tw=10000:ts=4:sts=4:sw=4:noexpandtab:
