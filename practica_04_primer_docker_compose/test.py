#loop that prints on screen the numbers from 1 to 20 every 1 second in a new line
import time

while True:
    for i in range(1,21):
        print("the number is: ", i)
        time.sleep(1)
    print("End of the loop, starting again...")
