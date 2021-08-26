#import dependencies
import pandas as pd
import plotly.figure_factory as ff
import numpy as np

import plotly as py


def create_choropleth():
    pd.set_option('display.max_rows', None)
    #read csv- must specify columns as strings or lose leading zero
    df = pd.read_csv(r'choropleth_data/all-geocodes-v2016.csv', encoding='latin-1',
                    dtype={'State_Code_FIPS': str, 'County_Code_FIPS': str}
                    
                    )


    #filter our data
    df_2 = df.loc[(df['State_Code_FIPS'] == '48') & (df['Place_Code_FIPS'] == 00000)]


    #drop the index row 38113 because it says texas, not an actual county name
    df_3 = df_2.drop([38113])

    #create a blank list and add the two strings togther append to list
    count_fips_codes = [ ]

    for i in range(38114, 38368):
        code = str(df_3['State_Code_FIPS'][i]) + str(df_3['County_Code_FIPS'][i])
        count_fips_codes.append(code)



    #create blank dataframe
    code_df = pd.DataFrame()
    #set list to dataframe column
    code_df['County_Codes'] = count_fips_codes
    #create list from county name column
    county_list = df_3['Area_Name_including legal/statistical area description'].to_list()
    #split column based on whitespace

    county_list_split =[]
    for row in county_list:
        #grab the first item in the split, before the space. In this case the name of county  
        delimiter = ' '  
        striped = row.split(delimiter,3)
        if striped[-1] == 'County':
            
            striped = striped[:-1]
            county_list_split.append(striped)
        else:
            county_list_split.append(striped[0:2])
    #take county name list and put to dataframe

    code_df['County_Name']= county_list_split


    code_df['County_Name'] = code_df['County_Name'].apply(', '.join)

    code_df['County_Name'] = code_df['County_Name'].replace(',','',regex=True)


    #pull in executed offenders
    executed_men_df = pd.read_csv(r'functions_file_data_outputs/executed_men_df.csv')


    #get the counts of executed offenders 

    item = executed_men_df['County'].value_counts()
    #put those items to a dictionary
    count_by_county = item.to_dict()



    #sent dictionary keys to a list
    execution_counties = list(count_by_county.keys())
    #filter dataframe for values in the execution_counties list. 
    execution_county_codes = code_df[code_df.County_Name.isin(execution_counties)]



    #get the value counts, rename the axis and reset the index. This creates a dataframe object
    executions_df_1 = executed_men_df['County'].value_counts().rename_axis('County_Name').reset_index(name='Executions')


    #merge the two together
    joined_df = executions_df_1.merge(code_df, how='left', on='County_Name')
    joined_df.to_csv(r'choropleth_data/joined_df.csv')
    fig = ff.create_choropleth(fips=joined_df['County_Codes'], values=executions_df_1['Executions'],scope=['TX'], asp=2.5, legend_title='Number of Executed Offenders',
        title='Executed Inmates by County of Conviction')
    
    fig.write_html(r"choropleth_data/texas_executions_choropleth.html")
    fig.layout.template = None
    py.offline.plot(fig, filename=r"choropleth_data/texas_executions_choropleth_2.html")
    fig.show()
    
    
    py.offline.plot(fig,
                filename=r'choropleth_data/choropleth_texas_js.html',
                include_plotlyjs='https://cdn.plot.ly/plotly-1.42.3.min.js')
    
create_choropleth()