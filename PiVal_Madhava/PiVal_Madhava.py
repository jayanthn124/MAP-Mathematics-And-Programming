# Value of Pi by Madhava of Sangamagrama.

import math

def ValOfPiUpto(): 
    # Madhva Series
    fractionSumDiff = 0.0
    pi_madhava = 0.0
    count = 1
    
    while(pi_madhava != math.pi):
        fraction = float((-1.0)**(count-1) * (1 / ((2*count) - 1)))
        fractionSumDiff = fractionSumDiff + fraction
        pi_madhava = (float(4 * (fractionSumDiff)))
        print("Count = ", count, "Pi_Madhava = ", pi_madhava)
        count = count + 1
    print("The Madhava Series converged with the value of pi from math lib.")
    
if __name__ == "__main__":
    ValOfPiUpto()