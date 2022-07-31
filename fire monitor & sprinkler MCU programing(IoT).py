from gpio import *
from time import *

def handleSensorData():
	value = digitalRead(4)  #4 is (d4) fire dector port
	if value == 0:
		customWrite(1, '0')  #1 is(d1)fire sprinkler conected port
	else:
		customWrite(1, '1')  #2n 1/0 is(1=on)(0=off)
	
	
def main():
	add_event_detect(4, handleSensorData)  #4 is (d4) fire dector port
	
	while True:
		delay(1000)

if __name__ == "__main__":
	main()