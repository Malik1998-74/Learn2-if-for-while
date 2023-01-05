import ephem

mars = ephem.Mars('2000/01/01')
counst = ephem.constellation(mars)
print(counst)