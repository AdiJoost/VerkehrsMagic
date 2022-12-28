from street import Street
import time

street = Street(gridsize=200, tunnel=(0,50))
"""
for i in range(50):
    print(street.to_string())
    print("******************************")
    street.update()
    time.sleep(2)"""

for i in range(100):
    street = Street(gridsize=500, tunnel=(1,50), spawnRate=float(i)/100)
    street.run(200, f"secondRun_{i}")
    street = Street(gridsize=500, tunnel=(1,50), spawnRate=float(i)/100, doubleSpawn=True)
    street.run(200, f"DoubleSpawnSecondRun_{i}")