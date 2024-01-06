#Updated on 06.01.2024

def find_delimiter_csv( filename ) :
    #Goal: Find the seperator in a csv file automatically
    
    ## Packages
    import csv  #The csv module implements classes to read and write tabular data 
                #in CSV format. 
    
    ## Code
    sniffer = csv.Sniffer()  #The Sniffer class is used to deduce the format of a CSV file.
    
    with open( filename ) as fp : #It opens each line of the csv file
        delimiter = sniffer.sniff( fp.read( 5000 ) ).delimiter  #Analyze the given sample
                                                                #It finds the separator.
    return delimiter

def open_csv_in_df( path , filename , index_date_col , index_var_col , variable_name , date_format ) :
    #Goal: Open a csv file in a pandas dataframe format automatically
    
    #index_var_col =>  should be a scalar if there is one variable, a list if there are more than 1
    #variable_name => a string if there is one variable, a list if there are more than 1
    
    ## Packages
    import pandas as pd
    import numpy as np
    
    ## Code
    
    file = path + filename + '.csv' #Filename with the path
    
    sep = find_delimiter_csv( file ) #Delimiter of the CSV file

    data = pd.read_csv( file , sep = sep ) #Read the CSV file

    #Rename the column names
    if index_date_col >= 0 :
        data = data.rename( columns = { data.columns[ index_date_col ] : 'Date' } )
        
        #Date format
        if len( date_format ) == 0 :
            data[ 'Date' ] = pd.to_datetime( data[ 'Date' ] , dayfirst = True )
        else : 
            data[ 'Date' ] = pd.to_datetime( data[ 'Date' ] , dayfirst = True , date_format = date_format)                  

    if np.size( index_var_col ) > 1 : #many variables 
        for index in range( len( index_var_col ) ) :
            data = data.rename( columns = { data.columns[ index_var_col[ index ] ] : variable_name[ index ] } )
    
    else : #one variable
        data = data.rename( columns = { data.columns[ index_var_col ] : variable_name } ) 
        
    data.to_csv( path + filename + '_mod.csv' , index = False , sep = ';' )
    
    return data


