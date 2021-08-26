
#import dependencies
from os import remove
import pandas as pd
from bs4 import BeautifulSoup
import requests
import pymongo
from collections import Counter
from splinter import Browser
executable_path = {"executable_path": r"chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)
import time
import matplotlib.pyplot as plt
import numpy as np
import plotly_express as px



def get_executed_offenders_df():

    # visit the TDOJ death row page
    death_url = 'https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html'
    # call the browers and go to the url
    browser.visit(death_url)

    # grab the value in the browser
    texas_html = browser.html
    # convert to a beautiful soup object
    texas_soup = BeautifulSoup(texas_html, 'html.parser')

    # find the table object inside the soup object- set to variabel
    texas_table = texas_soup.find('table', class_='tdcj_table indent')

    # gather url
    url5 = "https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html"

    # read the url using pdread
    tables = pd.read_html(url5)
    
    #set the first item to a DF
    executed_men_df = tables[0]
    #show dataframe
    executed_men_df
    # send to csv
    executed_men_df.to_csv(r'functions_file_data_outputs\executed_men_df.csv')
    return executed_men_df




def get_list_of_final_statements():
    # visit the TDOJ death row page
    death_url = 'https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html'
    # call the browers and go to the url
    browser.visit(death_url)

    # grab the value in the browser
    texas_html = browser.html
    # convert to a beautiful soup object
    texas_soup = BeautifulSoup(texas_html, 'html.parser')

    # find the table object inside the soup object- set to variabel
    texas_table = texas_soup.find('table', class_='tdcj_table indent')

    # gather url
    url5 = "https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html"

    # we need to create lists of all the links inside the offender table in order to use beautiful soup later
    # create a list to append items to
    list_of_items = []

    # we are going to iterate over the table object
    for a in texas_table.find_all('a', href=True):
        # take the a[href] to a link
        link = a['href']
        # take the link and append it to the
        list_of_items.append(link)

    

        # create new list
    new_list = []
    # take the partial string missing in the list in the prior cell
    s = "https://www.tdcj.texas.gov/death_row/"
    # for loop thorugh the existing list
    for i in list_of_items:
        # take the partial string in the list
        new = s+str(i)
        # add the two strings together after convering i to a string
        new_list.append(new)
        # add to the new list. Some of the strings are only partial. It is not a full URL. Need to add https: in order for the browser to 
        #recognize it when building the bot

    html_links = []
    jpeg_links = []

    #note that each offender has two or three  links, one with just their names and the #
    # second with the word jpeg and then a third with their last words
    for link in new_list:
        # if the string URL contains hrml append to html links
        if "html" in link:
            html_links.append(link)
        else:
            # otherwise send to jpeg links
            jpeg_links.append(link)

    # there are prisoners who did not give a statement, these are dead links, we are going to remove them

    dead_links = []
    final_statements = []

    # go through html links
    for link in html_links:
        # remove html stings with the word no_ in them
        if "no_" in link:
            dead_links.append(link)
            # if no exists put it to the dead links list
        else:
            # otherwise append to final statements
            final_statements.append(link)

    typos = []
    final_final_statements = []
    # the typos from the previous list which includes death_row//death_row, we want to take those off as it will throw and error
    # when we try to vist that website
    for link in final_statements:

        if "death_row//death_row" in link:
            typos.append(link)
        else:
            final_final_statements.append(link)

    # we only want links which deather their "last" statement so we want to strip out the superfulious links

    others = []
    last_statements = []
    for link in final_final_statements:

        if "last.html" in link:
            last_statements.append(link)
        else:
            others.append(link)
    global statements_final
    statements_final = []
    counter = 0
    global date_of_execution
    date_of_execution = []
    global offender_name
    offender_name = []
    global inmate_final_statement
    inmate_final_statement = []
    # the counter is the number of inmates on the list
    for link in last_statements:
        # loop though the list for the length of the list
        if counter == len(last_statements):
            break
        # visit the browser
        browser.visit(link)
        html1 = browser.html
        soup1 = BeautifulSoup(html1, 'html.parser')
        # find all the p tags in the BS object
        page = soup1.find_all("p")
        
        # take each object and convert to string
        statement = str(page)
        test1 = BeautifulSoup(statement)
        clean = test1.get_text()
        # we want the text of that string by removing the other p tags

    # append to our list and add one to the counter
        statements_final.append(clean)
             
        #get date of execution 
        statement_1 = str(page[1])
        test_2 = BeautifulSoup(statement_1)
        clean_1 = test_2.get_text()
        date_of_execution.append(clean_1)
        
           
        #get inmate name and DOC numnber 
        statement_2 = str(page[3])
        test_3 = BeautifulSoup(statement_2)
        clean_2 = test_3.get_text()
        offender_name.append(clean_2)
                
        statement_3 = str(page[-1])
        test_4 = BeautifulSoup(statement_3)
        clean_3 = test_4.get_text()
        print(clean_3)
        inmate_final_statement.append(clean_3)
          
        counter += 1  
    #the final statements are often missing when grabbing the P tags from html. 
    #if we split them from the entire p tag(which is gathered in statements final) we ensure
    #we get statements for all offenders who provided one
    global split_final_statements
    split_final_statements = []
    for i in range(len(statements_final)):
        split_word = statements_final[i].split('Statement:', 1)[1]
        split_final_statements.append(split_word)

    
    
    dict = {'Date_of_Execution': date_of_execution, 'Offender_Name_DOC_Number': offender_name, 'Inmate_Final_Statement': split_final_statements} 
    global df  
    df = pd.DataFrame(dict)
    df.to_csv(r'functions_file_data_outputs\final_statements_with_stopwords.csv')
    
    return statements_final, df



def remove_stop_words():

     

    stop_words = ['I', 'to', 'and', 'the', 'you', 'of', 'my', 'for', 'that', ',', 'am', 'have', 'a', 'is', 'in', 'Last', 'Statement', 'Execution',
                    'your', 'it', 'with']

    from nltk.corpus import stopwords
    from nltk import word_tokenize
    # set the stop words list to english
    stop = set(stopwords.words('english'))
    # change all the words on the stop list to lower and then split
    output_array=[]
    for sentence in split_final_statements:
        temp_list=[]
        for word in sentence.split():
            if word.lower() not in stop:
                temp_list.append(word)
        output_array.append(' '.join(temp_list))   
       
       
 #output_array is a list of all statements with their stopwords removed        

    #cleaned_statements = [i for i in word_tokenize(
        #split_final_statements.lower()) if i not in stop]

    #type(cleaned_statements)
    replaced_array = []
    for i in range(0, len(output_array)):
        
        # replace all useless punctiation with spaces along with words that were not picked up by nltk stopwords
        cleaned_statements = output_array[i].replace(',', '')
        cleaned_statements_1 = cleaned_statements.replace('"\'"', '')
        cleaned_statements_2 = cleaned_statements_1.replace("'.' ", '')
        cleaned_statements_3 = cleaned_statements_2.replace("'' ", '')
        cleaned_statements_4 = cleaned_statements_3.replace("'['", '')
        cleaned_statements_5 = cleaned_statements_4.replace("']'", '')
        cleaned_statements_6 = cleaned_statements_5.replace("'#'", '')
        cleaned_statements_7 = cleaned_statements_6.replace('statement', '')
        cleaned_statements_8 = cleaned_statements_7.replace('last', '')
        cleaned_statements_9 = cleaned_statements_8.replace('execution', '')
        cleaned_statements_10 = cleaned_statements_9.replace('date', '')
        cleaned_statements_11 = cleaned_statements_10.replace('offender', '')
        cleaned_statements_12 = cleaned_statements_11.replace("''", '')
        cleaned_statements_13 = cleaned_statements_12.replace("'’'", '')
        cleaned_statements_14 = cleaned_statements_13.replace("'``'", '')
        cleaned_statements_15 = cleaned_statements_14.replace('""', '')
        cleaned_statements_16 = cleaned_statements_15.replace('"n\'t"', '')
        cleaned_statements_17 = cleaned_statements_16.replace('"\'s"', '')
        cleaned_statements_18 = cleaned_statements_17.replace('"\'m"', '')
        cleaned_statements_19 = cleaned_statements_18.replace('"\'ll"', '')
        cleaned_statements_20 = cleaned_statements_19.replace("';'", '')
        cleaned_statements_21 = cleaned_statements_20.replace("':'", '')
        replaced_array.append(cleaned_statements_21)



    import plotly.express as px
    from collections import Counter
    #create master dataframe including offenders final statement with stop words removed
    dictionary_final_clean = {'Offender_Name': offender_name, 'Date_of_Execution': date_of_execution, 'Final_Statement' :replaced_array }
    global data_frame_final
    data_frame_final = pd.DataFrame.from_dict(dictionary_final_clean)
    
    data_frame_final.to_csv(r'functions_file_data_outputs\final_statements_without_stopwords.csv')
    return data_frame_final
    




def data_cleaning():
    #df will all the values 
    from collections import Counter
    from itertools import chain
    
    data_frame_final 
    words = []
    counts = []
    index = []
    data_frame_final['list_of_words']  = np.nan
    data_frame_final['most_common_words']  = np.nan
    data_frame_final['count_of_words']  = np.nan
    data_frame_final['count_of_words'] = data_frame_final['count_of_words'].astype(str)
     # split() returns list of all the words in the string
    for i in range(0, len(data_frame_final)):
        split_it = data_frame_final['Final_Statement'][i].split()
        data_frame_final['list_of_words'][i] = split_it
        
        
        # Pass the split_it list to instance of Counter class.
        Counter_variable  = Counter(split_it)
        # most_common() produces k frequently encountered
        # input values and their respective counts.
        most_occur = Counter_variable.most_common(5)
        

    # going through the most occred word list and split them into a list of words, and the number of times they show up. THis will help
    # us later when we make the pie chart
        #[i[0] for i in most_occur]
        #for item in most_occur:
        data_frame_final['most_common_words'][i] = [i[0] for i in most_occur]
        
        data_frame_final['count_of_words'][i] = [i[1] for i in most_occur]

  
    #explode based on the most_common_words
    explode_common_words_df = data_frame_final.explode('most_common_words')
    #drop columns that are unhasable lists
    explode_common_words_df_dropped = explode_common_words_df.drop(['list_of_words', 'count_of_words'], axis=1)
    #explode based on the count of words 
    explode_countof_words_df = data_frame_final.explode('count_of_words')
    #drop columns that are unhasable lists
    explode_countof_words_df_dropped = explode_countof_words_df.drop(['list_of_words', 'most_common_words'], axis=1)
    
    #set count of words to a list
    count_of_words_list = explode_countof_words_df_dropped['count_of_words'].to_list()
    #add to first dataframe as a column 
   
    explode_common_words_df_dropped['count_of_words'] = count_of_words_list
    
    global cleaned_df
    cleaned_df = explode_common_words_df_dropped
    cleaned_df.to_csv(r'functions_file_data_outputs\most_common_words_by_offender.csv')
    
    return cleaned_df




def create_charts():
    #create pie chart for each offenders most common words
    fig = px.pie(cleaned_df.loc[ [0], :], values='count_of_words', 
                 names='most_common_words', title='Most_common_words', 
                 hover_name= 'Offender_Name', hover_data= ['Date_of_Execution'])
    fig.show()

    
    
    #create pie chart for most common county of execution
    
    #read in dataset from earlier
    df = pd.read_csv(r'functions_file_data_outputs\executed_men_df.csv')

    execution_counties = df['County'].value_counts()
    execution_counties = execution_counties.to_frame(name='Count of Executions')
    execution_counties['County'] = execution_counties.index
    execution_counties = execution_counties.nlargest(10, 'Count of Executions')
    
    
    fig_2 = px.pie(execution_counties, values='Count of Executions', 
                 names='County', title='Top_Ten_Counties_By_Executions', 
                 hover_name= 'County', hover_data= ['Count of Executions'])

    fig_2

    
    #population by race
    
    execution_race = df['Race'].value_counts()
    execution_race = execution_race.to_frame(name='Count_of_Executions')
    execution_race['Race'] = execution_race.index
    fig_3 = px.pie(execution_race, values='Count_of_Executions', 
                 names='Race', title='Race_of_Executed_Defendents', 
                 hover_name= 'Race', hover_data= ['Count_of_Executions'])
    
    fig_3
    
    
    #plot age and race for all offenders
    
    fig_4 = px.scatter(df, x="Date", y="Age",
	          color="Race",
                 hover_name="County", hover_data=['First Name', 'Last Name'])
    fig_4
    
    
    #plot average age by race 
    grouped_by_race = df.groupby(by='Race').mean().reset_index()
    
    
    fig_5 = px.bar(grouped_by_race, x='Race', y='Age')
    fig_5
    
    
    
    
    #plot average age by county
    grouped_by_County = df.groupby(by='County').mean().reset_index()
    average_age = grouped_by_County['Age'].mean()
    
    fig_6 = px.scatter(grouped_by_County, x="County", y="Age",
                       color=((grouped_by_County['Age'] < average_age) &
            (grouped_by_County['Age'] < average_age)
        ).astype('int'),
         hover_name="County", hover_data=['Age'], title='Average_Age_of_Executed_By_County')
            
                       
                       
                       
                       
	          
    fig_6
    
    
    

    return fig, fig_2, fig_3,fig_4, fig_5, fig_6


#run all functions in order
get_executed_offenders_df()
get_list_of_final_statements()
remove_stop_words()
data_cleaning()
create_charts()





if __name__ == "__main__":
    print('test')
