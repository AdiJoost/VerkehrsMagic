from street import Street
import time

street = Street(gridsize=200, tunnel=(0,50))
"""
for i in range(50):
    print(street.to_string())
    print("******************************")
    street.update()
    time.sleep(2)"""
spawnrates = [5, 10, 15, 20, 30 , 40 ,50, 60, 70, 80, 90 ,100]
"""
for i in spawnrates:
    street = Street(gridsize=500, tunnel=(1,50), spawnRate=float(i)/100)
    street.run(200, f"secondRun_{i}")
    street = Street(gridsize=500, tunnel=(1,50), spawnRate=float(i)/100, doubleSpawn=True)
    street.run(200, f"DoubleSpawnSecondRun_{i}")"""

street = Street(gridsize=5000, tunnel=(1,50), spawnRate=0.2)
street.run(1000, plotName="Test5000-2")