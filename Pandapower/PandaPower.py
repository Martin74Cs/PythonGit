import pandapower as pp

# Vytvoření prázdné sítě
net = pp.create_empty_network(name="Testovací Síť", f_hz=50, sn_mva=250)

# Vytvoření uzlů (buses)
# Hlavní uzel (např. připojení k rozvodné síti)
uzek1 = pp.create_bus(net, vn_kv=22.0, name="Hlavní Uzel")

# Sekundární uzel (např. koncový bod s nižším napětím)
uzek2 = pp.create_bus(net, vn_kv=0.4, name="Sekundární Uzel")

# Připojení externí sítě jako zdroj
pp.create_ext_grid(net, bus=uzek1, vm_pu=1.0, name="Externí Zdroj")

# Definice transformátoru
trafo = pp.create_transformer_from_parameters(
    net,
    hv_bus=uzek1,
    lv_bus=uzek2,
    name="Transformátor_1",
    sn_mva=1.0,          # Jmenovité výkon transformátoru
    vn_hv_kv=22.0,       # Vysokonapěťový napětí
    vn_lv_kv=0.4,        # Nízkonapěťový napětí
    vk_percent=5.0,      # Kurzový odpor [%]
    vkr_percent=2.0,     # Kurzový odpor s regulací [%]
    pfe_kw=2.0,          # Ztráty na železe (kW)
    i0_percent=0.4,      # Krátký obvodový proud [%]
    shift_degree=150     # Fázový posun v stupních
)

# Definice vlastního typu kabelu jako slovník
vlastni_typ_kabelu = {
    "c_nf_per_km": 10,       # Kapacitní reaktance [nF/km]
    "max_i_ka": 0.25,        # Maximální proud [kA]
    "r_ohm_per_km": 0.2,     # Odpor [Ohm/km]
    "x_ohm_per_km": 0.02,    # Reaktance [Ohm/km]
    "df": 1.0,               # Distribuční faktor
    "type": "line"           # Typ komponenty
}

vlastni_typ_kabelu_rozsireny = {
    "c_nf_per_km": 10,
    "max_i_ka": 0.5,
    "r_ohm_per_km": 0.1,
    "x_ohm_per_km": 0.2,
    "g_us_per_km": 0.0,      # Vodivost [S/km], obvykle malá pro kovy
    "s_max_mva": 1.0,        # Maximální výkon [MVA]
    "type": "line"
}

# Vytvoření vlastního standardního typu kabelu
pp.create_std_type(net, data=vlastni_typ_kabelu, name="VlastniKabel1", element='line')

# Definice vedení mezi sekundárním uzlem a dalším uzlem (např. zátěží)
# Pro ilustraci přidáme další uzel a spojení
uzek3 = pp.create_bus(net, vn_kv=0.4, name="Zátěžní Uzel")

# line = pp.create_line(net, from_bus=bus_sekundarni, to_bus=bus_zatez,
#                      length_km=0.1, std_type="NAYY 4x50 SE")
# Vytvoření vedení s vlastním typem kabelu
line = pp.create_line(
    net,
    from_bus=uzek2,
    to_bus=uzek3,
    length_km=0.1,                 # Délka vedení v kilometrech
    std_type="VlastniKabel1",      # Použití vlastního typu
    name="Vedení_VlastniKabel1"
)

# Přidání zátěže na zátěžní uzel
pp.create_load(
    net, 
    bus=uzek3, # Uzlu, ke kterému je připojena zátěž.
    p_mw=0.6,      # Aktivní výkon zátěže (MW).
    q_mvar=0.05,   # Reaktivní výkon zátěže (MVAR).
    name="Zátěž_1" # Název zátěže.
)

# Spuštění výpočtu toků výkonu
pp.runpp(net)

# Výsledky
print("Napětí na uzlech (pu):")
print(net.res_bus.vm_pu)

print("\nZatížení vedení (%):")
print(net.res_line.loading_percent)

print("\nVýsledek transformátoru:")
print(net.res_trafo)

import pandapower.plotting as plot
plot.create_trafo_collection(net)

# Nefunguje
# plot.draw_collections()

# Vizualizace Sítě: Můžeš použít pandapower.plotting pro vizualizaci sítě a výsledků.
plot.simple_plot(net)
