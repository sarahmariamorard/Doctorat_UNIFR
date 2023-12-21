##############################################################################
# Setting file for the code : Calculate_meanPerMonthPerYear.py
#
# Author: S.Morard
# Created on 06.12.2023
# Updated on 06.12.2023
#
# There are two functions at the end of the code to store the dictionnary
# into a binary file and then to retrieve it later.
# We just need to give following the model, the variables .
#
##############################################################################

# Dictionnary
# model = {
#     'path' : '' ,
#     'filename' : '' ,
#     'index_date_col' : 0 ,
#     'index_var_col' : 1 ,
#     'variable_name' : '' ,
#     'date_format' : '',
#     'suffix_savename' : '_monthlyMean_PerYear' }

STO_Tair = {
    'path' : 'C:/Users/MorardSa/Documents/code/essai/' ,
    'filename' : 'STO_Tair_20020612_20230125_d_monthly' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'Tair' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }

STO_Pair = {
    'path' : 'C:/Users/MorardSa/Documents/code/essai/' ,
    'filename' : 'STO_Pressure_20020101_20230126_d_monthly' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'Pair' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }

STO_LIN = {
    'path' : 'C:/Users/MorardSa/Documents/code/GitHub_test/' ,
    'filename' : 'STO_Lin_20230125_20020101_d_level3_monthly' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'Lin' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }

STO_LOUT = {
    'path' : 'C:/Users/MorardSa/Documents/code/essai/' ,
    'filename' : '' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'Lout' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }

STO_Rainfall = {
    'path' : 'C:/Users/MorardSa/Documents/code/essai/' ,
    'filename' : 'STO_rainfall_mm_d_monthly' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'rainfall' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }

STO_RH = {
    'path' : 'C:/Users/MorardSa/Documents/code/essai/' ,
    'filename' : 'STO_RH_20020612_20230126_d_level1_monthly' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'RH' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }

STO_SH = {
    'path' : 'C:/Users/MorardSa/Documents/code/essai/' ,
    'filename' : 'STO_RH_20020612_20230126_d_specificHumidity_monthly' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'SH' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }

STO_SIN = {
    'path' : 'C:/Users/MorardSa/Documents/code/essai/' ,
    'filename' : 'STO_Sin_20020101_20230126_d_level3_monthly' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'Sin' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }

STO_Snowfall = {
    'path' : 'C:/Users/MorardSa/Documents/code/essai/' ,
    'filename' : 'STO_snowfall_d_monthly' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'snowfall' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }

STO_snowh = {
    'path' : 'C:/Users/MorardSa/Documents/code/essai/' ,
    'filename' : 'STO_snowfall_20020101_20230126_d_monthly' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'snowh' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }

STO_SOUT = {
    'path' : 'C:/Users/MorardSa/Documents/code/essai/' ,
    'filename' : 'STO_Sout_20020101_20230126_d_level3_monthly' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'Sout' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }

STO_WindDir = {
    'path' : 'C:/Users/MorardSa/Documents/code/essai/' ,
    'filename' : '' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'wd' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }

STO_WindSpeed = {
    'path' : 'C:/Users/MorardSa/Documents/code/essai/' ,
    'filename' : 'STO_windSpeed_20020612_20230125_d_monthly' ,
    'index_date_col' : 0 ,
    'index_var_col' : 1 ,
    'variable_name' : 'ws' ,
    'date_format' : '',
    'suffix_savename' : '_monthlyMean_PerYear' }
