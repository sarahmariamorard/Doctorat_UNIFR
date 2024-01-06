#Updated on 06.01.2024

def find_delimiter_csv( filename ) :
    #Goal: Find the seperator in a csv file automatically
    
    #input = 1 csv file
    #output = separator
    
    #filename => path + filename + extent
    
    ## Packages
    import csv  #The csv module implements classes to read and write tabular data 
                #in CSV format. 
    
    ## Code
    sniffer = csv.Sniffer()  #The Sniffer class is used to deduce the format of a CSV file.
    
    with open( filename ) as fp : #It opens each line of the csv file
        delimiter = sniffer.sniff( fp.read( 5000 ) ).delimiter  #Analyze the given sample
                                                                #It finds the separator.
    return delimiter



