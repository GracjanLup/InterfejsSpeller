# Funkcja do aktywacji po mrugnięciu

czestotliwosc = [2,4,5]
counter = -1


def does_blink():
    while True:
        #czestotliwosc.append()
        counter+1
        x = 0
        if counter>=20:
            for i in range(8):
                if czestotliwosc[counter - i + 1] > czestotliwosc[counter - i]:
                    x+1
                    if x == 8 and czestotliwosc[conter - 2*i] < -10000:
                        x = 0
                        return True;


does_blink()
