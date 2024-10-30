trianges = []
pentagons = []
hexagons = []

for i in range(1,100000):
    trianges.append(i*(i+1)*0.5)
    pentagons.append(i*((3*i)-1)*0.5)
    hexagons.append(i*((2*i)-1))

set_tri = set(trianges)
set_pent = set(pentagons)
set_hex = set(hexagons)

finalset = set_hex & set_pent & set_tri
print(finalset)
