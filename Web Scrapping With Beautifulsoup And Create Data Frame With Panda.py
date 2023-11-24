# web scrapping the table data from a webpage beautifulsoup 
# create data frame and export to a local file with panda 

from bs4 import BeautifulSoup
import requests
import pandas

url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_Kingdom"

# extract all html data from the url
page= requests.get(url)
soup=BeautifulSoup(page.text,"html.parser") 

# pull 1st table in the webpage table data by class (example only, this variable will not be used)
fortuneList2022=soup.find("table",class_="wikitable sortable")
# pull 2nd table in the webpage table data by index
globalDatabaseList2021=soup.find_all("table")[1]

# extract the text of all headers from globalDatabaseList2021 into a list and remove unnecessary spacing by using strip()
tableHeaders=[]
for temp in globalDatabaseList2021.find_all("th"):
    tableHeaders.append(temp.text.strip())

# assign table headers to data frame columns
df=pandas.DataFrame(columns=tableHeaders)

# Use nested loop to extract row data as list and append these data into another list that separated by rows
# loop start at 1 instead of 0 as the first list item is empty
individualRow=[]
for tempRows in globalDatabaseList2021.find_all("tr")[1:]:
        individualRow.append([tempData.text.strip() for tempData in tempRows.find_all("td")])

# same output as the code above but different structure
# individualRow=[]
# for tempRows in globalDatabaseList2021.find_all("tr"):
#     individualData=[]
#     for tempData in tempRows.find_all("td"):
#         individualData.append(tempData.text.strip())
#     individualRow.append(individualData)

# store the row data into the data frame
for temp in individualRow:      
      df.loc[len(df)]=temp

# export the into an excel file and remove the list index number
df.to_excel(r"C:\Users\baby_\Desktop\Projects\Python Projects\Web Scrapping - Generated data file\globalDatabaseList2021.xlsx", index=False)



    






