from gpio import *
from time import *

def main():
    while True:
        customWrite(0, "0,0");  (1st 0 is d0 slote)
        delay(1000);
        customWrite(0, "0,1");
        delay(1000);
        customWrite(0, "1,0");
        delay(1000);
        customWrite(0, "1,1");
        delay(1000);

if __name__ == "__main__":
	main()