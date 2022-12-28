from street import Street
import time

street = Street(gridsize=200)
for i in range(20):
    print(street.to_string())
    print("******************************")
    street.update()
    time.sleep(2)