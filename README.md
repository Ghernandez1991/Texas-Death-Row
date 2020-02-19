# Texas-Death-Row

Check out the app in action. 
https://github.com/Ghernandez1991/Texas-Death-Row/blob/master/image/bandicam%202020-02-19%2013-34-20-743.mp4
---------------------------------------------------------------------------------------------------------------------
#note- still working on deploying the app. Due to issues with selenium webdriver/http time out on heroku, this app may not be deployable on their platform. Currently investigating AWS or Azure. 



![Alt text](image/table.png?raw=true "Optional Title")


The state of Texas remains the most active death row in the United States. The project stems from my interest in the criminal justice system and the application of the death penalty in Texas. 

Using BeautifulSoup, the program scrapes the Texas Department of Corrections death row page and pulls down related statistics such as offender name, age and race. More specifically, I was interested in each prisoners last statement. 

Using ChromeDriver, the program visits each condemed mans page and pulls down his final words. Using python string manipulation, we are able to get a picture of the most common words spoken during all 600+ prisoners final moments. 


Included is a jupyter notebook which analyzes the web scraped data and returns the most common list of words uttered during inmate final statements. 

For users looking for the dashboard and API, refer to the app.py file. The application scrapes the DOC website and creates a data dashboard and several API's. The API's return the most common final words, the most active counties by execution and a list of all executed offenders. THe dashboard creates two plots using Javascript and an offender of the day which updates on refresh.  


![Alt text](image/Dashboard.PNG?raw=true "Optional Title")



![Alt text](image/most_common.PNG?raw=true "Optional Title")





![Alt text](image/stats.PNG?raw=true "Optional Title")
