import math
import entrada

LATA_1 = 18
LATA_2 = 3.6
LATA_3 = 2.5
LATA_4 = 0.5
litros_por_metro = 5.0

#IMPUT
area_a_ser_pintada = entrada.area_paredes()
print(area_a_ser_pintada)
litros_a_serem_usados = float(area_a_ser_pintada / litros_por_metro)


#latas de 18l
numero_latas_18l = math.floor(litros_a_serem_usados / LATA_1)
litros_faltantes = litros_a_serem_usados % LATA_1

#latas de 3.6l
numero_latas_3l = math.floor(litros_faltantes / LATA_2)
litros_faltantes = litros_faltantes % LATA_2

#latas de 2.5l
numero_latas_2l = math.floor(litros_faltantes / LATA_3)
litros_faltantes = litros_faltantes % LATA_3
#latas de 0.5l
numero_latas_1l = math.ceil(litros_faltantes / LATA_4)
litros_faltantes = litros_faltantes % LATA_4


print(f'Area a ser Pintada: {area_a_ser_pintada} e litros necessários: {litros_a_serem_usados}')
print(f'Latas de 18L: {numero_latas_18l}')
print(f'Latas de 3.6L: {numero_latas_3l}')
print(f'Latas de 2.5L: {numero_latas_2l}')
print(f'Latas de 0.5L: {numero_latas_1l}')
