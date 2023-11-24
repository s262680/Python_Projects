import pandas

# optional style for visualisation
import matplotlib.pyplot as plt



# Importing files

df1=pandas.read_excel(r"C:\Users\baby_\Desktop\Projects\Python Projects\Web Scrapping - Generated data file\globalDatabaseList2021.xlsx")
df2=pandas.read_csv(r"C:\Users\baby_\Desktop\Projects\Python Projects\Web Scrapping - Generated data file\globalDatabaseList2021.txt")
df3=pandas.read_json(r"C:\Users\baby_\Desktop\Projects\Python Projects\Web Scrapping - Generated data file\globalDatabaseList2021.json")

# specified which sheet to read in excel
df4=pandas.read_excel(r"C:\Users\baby_\Desktop\Projects\Excel projects\Data Cleaning in Excel Exercises.xlsx", sheet_name="US_Presidents OG")
df5=pandas.read_excel(r"C:\Users\baby_\Desktop\Projects\Excel projects\Data Cleaning in Excel Exercises.xlsx", sheet_name="US_Presidents Working Sheet")

# add  ,sep="\"  or  ,sep=","  after the path to separate data with a specific symbol

# pandas.set_option("display.max.columns",100)

# check data info, memory usage etc
df1.info()

# display number of rows and columns
df1.shape

##########################################################################################################
# Filtering 

# display first and last 10 rows
df1.head(10)
df1.tail(10)

# display a specific column
df1["Name"]

# display a specific row (use iloc if no index number display)
df1.loc[25]

# Filtering by number
df1[df1["Rank"]<=5]

# Filtering by a list of text
specificCountries=["Shell","Tesco","Legal & General"]
df1[df1["Name"].isin(specificCountries)]

# Filtering by whether the rows contain the specified text
df1[df1["Name"].str.contains("ner")]

# change index column
tempDf=df1.set_index("Industry")

# filtering multiple columns, axis is not necessary but set it to 0 if wish to filter rows instead
tempDf.filter(items=["Rank","Name"],axis=1)

# filtering by index name
tempDf.loc["Mining"]

# filtering by index name and only display a specific column
tempDf.loc["Mining","Name"]

# filtering by interger location
tempDf.iloc[3]

# sorting rank in descending order and name in ascending order
df1[df1["Headquarters"].str.contains("London")].sort_values(by=["Rank","Name"], ascending=[False, True])

##########################################################################################################
# Indexing

# other way to change index column
indexingDf=pandas.read_csv(r"C:\Users\baby_\Desktop\Projects\Python Projects\Web Scrapping - Generated data file\globalDatabaseList2021.txt", index_col="Industry")

# reset the index to default number
indexingDf.reset_index(inplace=True)

# multiple indexs
indexingDf.set_index(["Industry","Name"],inplace=True)

# sort and group by index
indexingDf=indexingDf.sort_index()
print(indexingDf)

# locate specific row with muliple indexs, iloc doesn't working properly with multiple indexs
print(indexingDf.loc["Retailing","Tesco"])

##########################################################################################################
# Grouping and aggregating

# group and aggregate all columns
groupedDf=df1.groupby("Industry")
print(groupedDf.count())

# aggregate specific columns with multiple aggregations
print(groupedDf.agg({"Revenue(billions GBP£)":["count","sum","mean","max"], "Rank":["min","max"]}))

# multiple groups
multiGroupDf=df1.groupby(["Industry","Headquarters"])
print(multiGroupDf.agg({"Revenue(billions GBP£)":["count","sum","mean","max"]}))

# quick aggregation overview 
multiGroupDf.describe()

##########################################################################################################
# Merge, join, concatnate
staffDF1=pandas.read_excel(r"C:\Users\baby_\Desktop\Projects\Python Projects\Pandas join exercises data\salespersonDataPart1.xlsx")
staffDF2=pandas.read_excel(r"C:\Users\baby_\Desktop\Projects\Python Projects\Pandas join exercises data\salespersonDataPart2.xlsx")

# by using merge (joining by not using index)
# inner join
innerJoinDf=staffDF1.merge(staffDF2,how="inner",on="ID")
print(innerJoinDf)

# left join
leftJoinDf=staffDF1.merge(staffDF2,how="left",on="ID")
print(leftJoinDf)

# inner join
outerJoinDf=staffDF1.merge(staffDF2,how="outer",on="ID")
print(outerJoinDf)

# cross join, compare 1 row on a table to all rows in another table 
crossJoinDf=staffDF1.merge(staffDF2,how="cross")
print(crossJoinDf)

# by using join (joining by using index)
joinIndexDf=staffDF1.set_index("ID").join(staffDF2.set_index("ID"),how="inner",lsuffix="_left",rsuffix="_right")
print(joinIndexDf)

# concatcatnate (same as append)
concatDf=pandas.concat([staffDF1,staffDF2],join="outer")
print(concatDf)

##########################################################################################################
# Visualisation
print(df1)

# optional styles
# plt.style.available
# plt.style.use("classic")

# basic examples (inaccurate use of the data)
df1.set_index("Name").plot.bar( title="test bar chart")
df1.set_index("Name").plot.barh(title="test bar chart", stacked=True)

# choosing data for x and y axis
df1.plot.bar(x="Name", y ="Rank")
df1.plot.scatter(x="Rank", y="Revenue(billions GBP£)", s=500, c="Orange")
df1.plot.hist(y ="Revenue(billions GBP£)", bins=5)

# with visualising with group and aggregate
df1.groupby("Industry").agg({"Revenue(billions GBP£)":"sum"}).plot.bar(title="Total revenue by industry")
df1.groupby("Industry").agg({"Revenue(billions GBP£)":"sum"}).plot.pie(y="Revenue(billions GBP£)",title="Total revenue by industry",figsize=(15,15))

##########################################################################################################

