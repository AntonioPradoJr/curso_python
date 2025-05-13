vel_car = 70
pos_car = 100

RADAR_1 = 60
POS_RADAR = 101
RANGE_RADAR = 1

multar_veiculo = vel_car > RADAR_1
range_max_radar = POS_RADAR + RANGE_RADAR
range_min_radar = POS_RADAR - RANGE_RADAR



if multar_veiculo:
    if pos_car <= range_max_radar and pos_car >= range_min_radar:
        print('Você foi multado')
    else:
        print('Nada Aconteceu')
else:
    print('Nada Aconteceu')