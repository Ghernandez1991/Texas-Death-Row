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

In this branch you will find several additions from the master branch. 


Functions_file.py is an improved version of the web scraping app, and the natural language processing completed in the original flask app(master branch). 
The file contains functions to scrape the data, to gather the inmates final statement(with and without stopwords) and to clean the data so it can be analyzed for each inmate. The file also creates several plotly charts. 




Choropleth.py gathers FIPS state/county codes for Texas and creates a dataframe with them and the number of executed offenders by county. Using this data, plotly can create a choropleth map based on county lines/divisions. 






![Alt text](image/age_of_all_offenders.PNG?raw=true "Optional Title")



![Alt text](image/average_age_by_county.PNG?raw=true "Optional Title")





![Alt text](image/average_age_by_race.PNG?raw=true "Optional Title")


![Alt text](image/race_of_offenders.PNG?raw=true "Optional Title")
