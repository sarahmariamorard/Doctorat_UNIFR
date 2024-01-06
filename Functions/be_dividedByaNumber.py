#Updated on 06.01.2023

def be_dividedByaNumber( division , number) :
    if ( number % division ) == 0 : 
        print( f" The number {number} is divisble by {division}." )
        
    else : 
        print( f" The number {number} is not divisible by {division}. The rest is {number%division}." )
        