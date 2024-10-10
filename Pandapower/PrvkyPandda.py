import pandapower as pp

net = pp.create_empty_network(name="test", f_hz=50, sn_mva= 40)
# net = pp.create_empty_network()

# create buses
b0 = pp.create_bus(net, vn_kv=22.0, name = "Test")
# b1 = pp.create_b(net, vn_kv=22.0, name="Bus 1")
# b2 = pp.create_bus(net, vn_kv=0.4, name="Bus 2")

# trafo = pp.create_transformer_from_parameters(net, hv_bus=b1, lv_bus=b2, name="MartinTrafo1", sn_mva=0.4, vn_hv_kv=22, vn_lv_kv=0.42, 
#                                       vk_percent=5.0, vkr_percent=2.0, pfe_kw=2.0, i0_percent=0.4, shift_degree=150)

# Spusťte tok energie:
pp.runpp(net)

# výsledky
print(net.res_bus.vm_pu)
print(net.res_line.loading_percent)