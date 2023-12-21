##############################################################################
# It plots the timeseries (hourly, daily, monthly, yearly and hyd. yearly). 
# The x-axis represents the timeseries. The y-axis represents the variable.
# 
# Author : S. Morard
# Created on 07.12.2023
# Updated on 21.12.2023
#
# Input file : The code is written for a csv file with two columns. The
#              column #0 represents the dates and the column #1 represents the
#              variable.
#
# Output file : A plot is created with the x-axis representing the timeseries
#               and the y-axis represents the variable.
#
# This script is related with the python file "Plot_timeseries_settingfile.py". 
# In this setting script, we write the particularity of the file. Then, we 
# just need to give the dictionnary name into "name" here in the script.
#
#############################################################################

name = 'STO_Tair'


# Packages
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import datetime
import pickle
from Plot_timeseries_settingfile import *  #Change the name of the import

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
storeData( 'plot' )
loadData()

def create_input_output_folder( path ) : 
    if not os.path.exists( path + 'input' ) :
        os.makedirs( path + 'input' )

    if not os.path.exists( path + 'output' ) :
        os.makedirs( path + 'output' )

def open_csv( path = path , filename = filename_d , sep = ';' , index_date_col = index_date_col , index_var_col = index_var_col , variable_name = variable_name , date_format = date_format ) : 
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

def plot_param( filename , lim , lim_1 , index_date_col = index_date_col , fontstyle = fontstyle , fontsize = fontsize , transparent_background = transparent_background , savefig = savefig , ylabel = '' ) : 
    #Plot parameters
    plt.rcParams[ 'font.sans-serif' ] = fontstyle
    plt.rcParams[ 'font.size' ]       = fontsize
    plt.rcParams[ 'savefig.transparent' ] 	= transparent_background
    plt.rcParams[ 'savefig.bbox' ] 		= savefig

    #Definition of the xticks
    ini = data[ data.columns[ index_date_col ] ][ 0 ].year #initial year
    fin = data[ data.columns[ index_date_col ] ].iloc[ -1 ].year #final year

    xticks_names = np.arange( xlim_min , xlim_max + 2 , 1 ) #name of the xticks
    xticks_intervall = np.round( 365.2476923077 * xticks_names - 719537.996923077 , 0) #intervall of the xticks

    plt.xticks( xticks_intervall )
    plt.xticks( xticks_intervall , xticks_names )
    plt.xlim( [ datetime.datetime( xlim_min , 1 , 1 ) , datetime.datetime( xlim_max , 1 , 1 ) ] )

    #YLIM
    ylim_min = np.floor( np.min( data[ data.columns[ index_var_col ] ] ) ) // lim * lim
    ylim_max = np.ceil( np.max( data[ data.columns[ index_var_col ] ] ) ) // lim * lim + lim
    plt.ylim( [ ylim_min , ylim_max ] )
    plt.yticks( np.arange( ylim_min , ylim_max + lim_1 , lim_1 ) )

    #labels
    plt.xlabel( 'Date' )
    plt.ylabel( ylabel )

    #Gaps
    where_nan = np.where( np.isnan( np.asarray( data[ data.columns[ index_var_col ] ] ) ) == True )[ 0 ]
    xmax = np.max( data[ data.columns[ index_var_col ] ] )
    plt.vlines( data[ data.columns[ index_date_col ] ][ where_nan ] , ylim_min , ylim_max , color = 'royalblue' , linewidth = 1 , label = 'gaps' )
    
    #Diverses
    plt.grid()
    plt.legend(ncol = 2 )
    
    plt.savefig( path + 'output/' + filename + '.png' )
    plt.show()
    
def plot( index_date_col , index_var_col ,  filename = filename_d , symbol = 'x' , markersize = 2 , color = 'darkturquoise' , label = '' ) :
    plt.plot( data[ data.columns[ index_date_col ] ] , data[ data.columns[ index_var_col ] ] , symbol , markersize = markersize , color = color , label = label )
    
    #Gaps
    where_nan = np.where( np.isnan( np.asarray( data[ data.columns[ index_var_col ] ] ) ) == True )[ 0 ]
    
    if len( where_nan ) > 0 :
        filewrite = open( path + 'output/' + filename + '_gaps.txt' , 'w' )
        for i in data[ data.columns[ index_date_col ] ][ where_nan ] :
            filewrite.write( str( i ) )
            filewrite.write( '\n' )
        filewrite.close() #Close the writing file

    print( where_nan )
    
# Code
plt.rcParams[ 'figure.figsize' ] = ( x_width , y_width ) #size of the figure ( x , y )

# Hourly
if len( filename_h ) > 0 :
    data = open_csv( path = path , filename = filename_h , sep = ';' , index_date_col = index_date_col , index_var_col = index_var_col , variable_name = variable_name , date_format = date_format )
    plot( index_date_col , index_var_col ,  filename = filename_d , symbol = symbol , markersize = markersize , color = color , label = label )
    plot_param( filename_h , lim , lim , index_date_col = index_date_col , fontstyle = fontstyle , fontsize = fontsize , transparent_background = transparent_background , savefig = savefig , ylabel = ylabel )

# Daily
if len( filename_d ) > 0 :
    data = open_csv( path = path , filename = filename_d , sep = ';' , index_date_col = index_date_col , index_var_col = index_var_col , variable_name = variable_name , date_format = date_format )
    plot( index_date_col , index_var_col ,  filename = filename_d , symbol = symbol , markersize = markersize , color = color , label = label )
    plot_param( filename_d , lim , lim , index_date_col = index_date_col , fontstyle = fontstyle , fontsize = fontsize , transparent_background = transparent_background , savefig = savefig , ylabel = ylabel )

# Monthly
if len( filename_m ) > 0 :
    data = open_csv( path = path , filename = filename_m , sep = ';' , index_date_col = index_date_col , index_var_col = index_var_col , variable_name = variable_name , date_format = date_format )
    plot( index_date_col , index_var_col ,  filename = filename_m , symbol = symbol , markersize = markersize , color = color , label = label )
    plot_param( filename_m , lim , lim , index_date_col = index_date_col , fontstyle = fontstyle , fontsize = fontsize , transparent_background = transparent_background , savefig = savefig , ylabel = ylabel )

# Yearly
if len( filename_y ) > 0 :
    data = open_csv( path = path , filename = filename_y , sep = ';' , index_date_col = index_date_col , index_var_col = index_var_col , variable_name = variable_name , date_format = date_format )
    plot( index_date_col , index_var_col ,  filename = filename_y , symbol = symbol , markersize = markersize , color = color , label = label )
    plot_param( filename_y , lim , 1 , index_date_col = index_date_col , fontstyle = fontstyle , fontsize = fontsize , transparent_background = transparent_background , savefig = savefig , ylabel = ylabel )

# Hyd. yearly
if len( filename_hy ) > 0 :
    data = open_csv( path = path , filename = filename_hy , sep = ';' , index_date_col = index_date_col , index_var_col = index_var_col , variable_name = variable_name , date_format = date_format )
    plot( index_date_col , index_var_col ,  filename = filename_hy , symbol = symbol , markersize = markersize , color = color , label = label )
    plot_param( filename_hy , lim , 1 , index_date_col = index_date_col , fontstyle = fontstyle , fontsize = fontsize , transparent_background = transparent_background , savefig = savefig , ylabel = ylabel )