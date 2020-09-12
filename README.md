# Texas-Death-Row

Check out the App in action. 
https://texas-deathrow-dashboard.herokuapp.com/

Check out the webscraper in action. 
https://youtu.be/nlKY6kUIcBY

Check out the Texas Department of Criminal Justice website. 
https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html

---------------------------------------------------------------------------------------------------------------------



![Alt text](image/table.png?raw=true "Optional Title")


The state of Texas remains the most active death row in the United States. The project stems from my interest in the criminal justice system and the application of the death penalty in Texas. 

In this repository you will find two seperate apps, that work together to get a better picture of the data behind executions in Texas. 

In the main repo. ----------------------------------------------------------------------------------------------------------------------------

Using BeautifulSoup, the program scrapes the Texas Department of Corrections death row page and pulls down related statistics such as offender name, age and race. More specifically, I was interested in each prisoners last statement. 

Using ChromeDriver, the program visits each condemed mans page and pulls down his final words. Using python string manipulation and natural language processing, we are able to get a picture of the most common words spoken during all 600+ prisoners final moments. 

This webscraper can be accessed by using the Web_Scrape_App with the combined requirements.txt and chromedriver. The webscraper data is presented in a Flask application in the web browser. 


In the Flask_App folder ----------------------------------------------------------------------------------------------------------------------------

This folder includes a cleaned up and production ready version of the webscrape app. Due to limitations with Heroku, rather than dynamically scrape the data everytime the user runs the app; the execution data is stored in a SQLite file. This file will run a scaled down dashboard(without the scraper) on a local host who runs it. Users will need to install the requirements.txt file(C:\Users\Gabriel Hernandez\Desktop\Flask_App_and_Scraper\Flask_App) and run python app.py in their terminal. 


Both applicationsWeb_Scrape_App and Flask_App/app.py feature several API's. The API's return the most common final words gathered from executed offenders, the most active counties by number of executions and a list of all executed offenders. THe dashboard's creates two plots using D3.js(Javascript) and an offender of the day which updates randomly when the app refreshes on refresh.  


![Alt text](image/Dashboard.PNG?raw=true "Optional Title")



![Alt text](image/most_common.PNG?raw=true "Optional Title")





![Alt text](image/stats.PNG?raw=true "Optional Title")
