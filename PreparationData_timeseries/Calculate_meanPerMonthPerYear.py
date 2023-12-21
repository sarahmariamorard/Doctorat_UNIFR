##############################################################################
# It creates a table with the x-axis representing the year and the y-axis
# represents the months. The code is calculating the monthly mean for each
# year.
#
# Author : S. Morard
# Created on 05.12.2023
# Updated on 21.12.2023
#
# Inpute file : The code is written for a csv file with two columns. The
#               column #0 represents the dates and the column #1 represents
#               the variable.
#
# Output file : A table is created with the x-axis representing the years and
#               the y-axis representing the months from JAN to DEC with the 
#               monthly mean value of the variable.
#
# This script is related with the python file "Calculate_mean_PerMonthPerYear_settingfile.py"
# In this setting script, we write the particularity of the file.
# Then, we just need to give the dictionnary name into "name" here in the script.
#
##############################################################################
name = 'STO_LIN'

# Packages
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import datetime
import pickle
from Calculate_meanPerMonthPerYear_settingfile import *  #Change the name of the import

# Functions
def storeData( name ) :
    #It stores the data into a database.
    db = globals()[ name ]
    dbfile = open( 'db' , 'wb' )
    pickle.dump( db , dbfile )
    dbfile.close()
    
def loadData():
    #It loads the data from the database
    dbfile = open( 'db' , 'rb' )
    db = pickle.load( dbfile )
    dbfile.close()
    
    #Each key becomes a value
    for key , value in db.items() :
        globals()[key] = value
    return( key )

storeData( name )
loadData()

def create_input_output_folder( path ) : 
    #It creates the folder structure "inptut" + "output".
    if not os.path.exists( path + 'input' ) :
        os.makedirs( path + 'input' )

    if not os.path.exists( path + 'output' ) :
        os.makedirs( path + 'output' )

def open_csv( path = path , filename = filename , sep = ';' , index_date_col = index_date_col , index_var_col = index_var_col , variable_name = variable_name , date_format = date_format ) : 
    #Read the CSV file
    data = pd.read_csv( path + 'input/' + filename + '.csv' , sep = sep )
    #Rename the column names
    data = data.rename( columns = { data.columns[ index_date_col ] : 'Date' } )
    data = data.rename( columns = { data.columns[ index_var_col ] : variable_name} )
    
    #Date format
    if len( date_format ) == 0 : 
        data[ 'Date' ] = pd.to_datetime( data[ 'Date' ] , dayfirst = True)
    else :
        data[ 'Date' ] = pd.to_datetime( data[ 'Date' ] , dayfirst = True , format = date_format)
    
    return data

def create_dataframe_xYears_yMonths( data , variable_name = variable_name , path = path , filename = filename , suffix_savename = suffix_savename , sep = ';' , index_bool = False) :
    #Creation of the dataframe
    year_ini = data[ 'Date' ].iloc[ 0 ].year
    year_fin = data[ 'Date' ].iloc[ -1 ].year

    xaxis_df = np.arange( year_ini , year_fin + 1 , 1 ) #years vector
    yaxis_df = np.arange( 1 , 12 + 1 , 1 ) #months vector
    
    dataframe = pd.DataFrame()
    dataframe[ 'month' ] = yaxis_df
    
    for col in range( len( xaxis_df ) ) :
        dataframe[ str( xaxis_df[ col ] ) ] = np.nan
    
    #Put the values in the dataframe
    for index in range( len( data ) ) :
        x = data[ 'Date' ][ index ].year
        y = data[ 'Date' ][ index ].month
        
        x_i = np.where( x == xaxis_df )[ 0 ][ 0 ]
        y_i = np.where( y == yaxis_df )[ 0 ][ 0 ]
    
        dataframe[ str( xaxis_df[ x_i ] ) ][ y_i ] = data[ variable_name ][ index ]
        
        dataframe.to_csv( path + 'output/' + filename + suffix_savename + '.csv' , index = index_bool , sep = sep )

    return dataframe
    
# Code
data = open_csv()
new_data = create_dataframe_xYears_yMonths( data )