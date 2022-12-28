from street import Street
import time

street = Street(gridsize=200)
for i in range(50):
    print(street.to_string())
    print("******************************")
    street.update()
    time.sleep(2)