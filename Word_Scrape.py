def DOC_Word_Scrape():
    #import dependencies 
    import pandas as pd
    from bs4 import BeautifulSoup
    import requests
    import pymongo
    from collections import Counter 
    from splinter import Browser
    executable_path = {"executable_path": r"F:\TDOJ project\chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    import time
    import matplotlib.pyplot as plt

    # visit the TDOJ death row page
    death_url = 'https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html'
    #call the browers and go to the url
    browser.visit(death_url)

    #grab the value in the browser
    texas_html = browser.html
    #convert to a beautiful soup object
    texas_soup = BeautifulSoup(texas_html, 'html.parser')

    #find the table object inside the soup object- set to variabel 
    texas_table = texas_soup.find('table', class_='tdcj_table indent')


    #gather url 
    url5 = "https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html"

    #read the url using pdread
    tables = pd.read_html(url5)
    #tables



        #we need to create lists of all the links inside the offender table in order to use beautiful soup later
    #create a list to append items to
    list_of_items = []

    #we are going to iterate over the table object
    for a in texas_table.find_all('a', href=True):
        #take the a[href] to a link
        link = a['href']
        #take the link and append it to the 
        list_of_items.append(link)
        
        #print ("Found the URL:", a['href'])



        #create new list
    new_list = []
    #take the partial string missing in the list in the prior cell
    s = "https://www.tdcj.texas.gov/death_row/"
    # for loop thorugh the existing list
    for i in list_of_items:
        #take the partial string in the list
        new = s+str(i)
        #add the two strings together after convering i to a string
        new_list.append(new)
        #add to the new list and 
        #print(new)


    html_links=[]
    jpeg_links=[]

    #note that each offender has two or three  links, one with just their names and the #
    #second with the word jpeg and then a third with their last words 
    for link in new_list:
        #if the string URL contains hrml append to html links
        if "html" in link: 
            html_links.append(link)
        else:
            #otherwise send to jpeg links
            jpeg_links.append(link)
                


    #there are prisoners who did not give a statement, these are dead links, we are going to remove them 

    dead_links = []
    final_statements = []

    #go through html links 
    for link in html_links:
        #remove html stings with the word no_ in them
        if "no_" in link: 
            dead_links.append(link)
            #if no exists put it to the dead links list
        else:
            #otherwise append to final statements 
            final_statements.append(link)
                



    typos = []
    final_final_statements = []
    #the typos from the previous list which includes death_row//death_row, we want to take those off as it will throw and error
    #when we try to vist that website 
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
                
    statements_final = []
    counter = 0

    #the counter is the number of inmates on the list
    for link in last_statements:
        #loop though the list for the length of the list 
        if counter == len(last_statements):
            break
        #visit the browser
        browser.visit(link)
        html1 = browser.html
        soup1 = BeautifulSoup(html1, 'html.parser')
        #find all the p tags in the BS object
        page = soup1.find_all("p")
        
        #take each object and convert to string    
        statement = str(page)
        test1 = BeautifulSoup(statement)
        clean = test1.get_text()
        #we want the text of that string by removing the other p tags
        
    
    #append to our list and add one to the counter 
        statements_final.append(clean)
        counter += 1
        
    #print our list and what type it is
    #print(statements_final)
    #print(type(statements_final))
    #convert it to string
    allstatements = str(statements_final)
    #print
    #print(allstatements)


    #convert to string and print
    mystring = str(statements_final)
    #print(mystring)

    #sent entire object to beautiful soup 
    soup = BeautifulSoup(mystring)
    #get the text from the BS object
    #print(soup.get_text())


    #allstatements is our string of all final statements
    stopwords = ['I','to','and','the','you','of','my', 'for', 'that', ',','am', 'have', 'a', 'is', 'in', 'Last', 'Statement', 'Execution', 
    'your', 'it', 'with']

    from nltk.corpus import stopwords
    from nltk import word_tokenize
    #set the stop words list to english
    stop = set(stopwords.words('english'))
    #change all the words on the stop list to lower and then split
    print([i for i in allstatements.lower().split() if i not in stop])

    cleaned_statements = [i for i in word_tokenize(allstatements.lower()) if i not in stop] 

    type(cleaned_statements)


    # convert to string
    cleaned_statements = str(cleaned_statements)
    #replace all useless punctiation with spaces along with words that were not picked up by nltk stopwords
    cleaned_statements = cleaned_statements.replace(',', '')
    cleaned_statements = cleaned_statements.replace('"\'"', '')
    cleaned_statements = cleaned_statements.replace("'.' ", '')
    cleaned_statements = cleaned_statements.replace("'' ", '')
    cleaned_statements = cleaned_statements.replace("'['", '')
    cleaned_statements = cleaned_statements.replace("']'", '')
    cleaned_statements = cleaned_statements.replace("'#'", '')
    cleaned_statements = cleaned_statements.replace('statement', '')
    cleaned_statements = cleaned_statements.replace('last', '')
    cleaned_statements = cleaned_statements.replace('execution', '')
    cleaned_statements = cleaned_statements.replace('date', '')
    cleaned_statements = cleaned_statements.replace('offender', '')
    cleaned_statements = cleaned_statements.replace("''", '')
    cleaned_statements = cleaned_statements.replace("'’'", '')
    cleaned_statements = cleaned_statements.replace("'``'", '')
    cleaned_statements = cleaned_statements.replace('""', '')
    cleaned_statements = cleaned_statements.replace('"n\'t"', '')
    cleaned_statements = cleaned_statements.replace('"\'s"', '')
    cleaned_statements = cleaned_statements.replace('"\'m"', '')
    cleaned_statements = cleaned_statements.replace('"\'ll"', '')
    cleaned_statements = cleaned_statements.replace("';'", '')
    cleaned_statements = cleaned_statements.replace("':'", '')


    from collections import Counter 
    # split() returns list of all the words in the string 
    split_it = cleaned_statements.split() 
    
    # Pass the split_it list to instance of Counter class. 
    Counter = Counter(split_it) 
    
    # most_common() produces k frequently encountered 
    # input values and their respective counts. 
    most_occur = Counter.most_common(50) 
    
    #print(most_occur) 


    #going through the most occred word list and split them into a list of words, and the number of times they show up. THis will help
    #us later when we make the pie chart
    words = []
    counts = []
    for item in most_occur:
        words.append(item[0])
        counts.append(item[1])


    #print our list of words
    #print(words)
    #print our list of counts 
    #print(counts)


    most_spoken = counts
    final_words = words

    plt.pie(most_spoken, labels=final_words, startangle=90, autopct='%.1f%%', radius=1)
    plt.title('Offender Final Words', loc= "left")
    fig = plt.gcf()
    fig.set_size_inches(13 ,13)
    plt.show()

    d = {'Most_Spoken_Words': final_words,'Count_of_Words':most_spoken}

    df = pd.DataFrame(d)
    #df



    #df.to_json(orient='index')

    return df

if __name__ == "__main__":
    print(DOC_Word_Scrape())