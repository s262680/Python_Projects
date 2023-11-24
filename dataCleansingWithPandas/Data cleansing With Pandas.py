# Data cleansing with Pandas

import pandas

df=pandas.read_csv(r"C:\Users\baby_\Desktop\Projects\Python Projects\Pandas data cleansing exercises data\Original Customer Call List.csv")

print(df)

# drop duplicated rows
cleanedDf=df.drop_duplicates()

print(cleanedDf)

# drop unnecessary column
# replace na with blank
cleanedDf=cleanedDf.drop(columns="Not_Useful_Column")
cleanedDf=cleanedDf.fillna("")

print(cleanedDf)

# simply remove spaces using strip
cleanedDf["First_Name"]=cleanedDf["First_Name"].str.strip()

# remove symbols in last name column using regular expression
# ^ represent match any character except those in the list
# \s represent space
cleanedDf["Last_Name"]=cleanedDf["Last_Name"].replace(r'[^a-zA-Z0-9\s]', '', regex=True)

# remove symbols in phone number column using regular expression
# then add dashes to phone numbers by using while loop if string is not blank
cleanedDf["Phone_Number"]=cleanedDf["Phone_Number"].replace(r'[^0-9]', '', regex=True)
x=0
while x < len(cleanedDf):
    temp=str(cleanedDf["Phone_Number"][x])
    if temp:
        cleanedDf["Phone_Number"][x]=temp[0:3]+"-"+temp[3:6]+"-"+temp[6:len(temp)]
    x+=1

# Separate address by comma with the split function and drop the full address column
cleanedDf[["Street", "State","Zip_Code"]]=cleanedDf["Address"].str.split(",", n=2,expand=True)
cleanedDf=cleanedDf.drop(columns="Address")

# replace Yes with Y and No with N in Paying Customer and Do_Not_Contact columns
cleanedDf["Paying Customer"]=cleanedDf["Paying Customer"].replace("Yes","Y")
cleanedDf["Paying Customer"]=cleanedDf["Paying Customer"].replace("No","N")
cleanedDf["Do_Not_Contact"]=cleanedDf["Do_Not_Contact"].replace("Yes","Y")
cleanedDf["Do_Not_Contact"]=cleanedDf["Do_Not_Contact"].replace("No","N")

# replace all "N/a" and null with blank
cleanedDf=cleanedDf.replace("N/a","")
cleanedDf=cleanedDf.fillna("")

# another way to loop through the df index
# drop the row if the phone number is missing or "Do_Not_Contact" is Y so customer won't get contacted
for x in cleanedDf.index:
    if cleanedDf.loc[x, "Phone_Number"] == "" or cleanedDf.loc[x, "Do_Not_Contact"]=="Y":
        cleanedDf.drop(x, inplace=True)
# another way to drop row with null values is to use df.dropna() function

# reset the index
cleanedDf=cleanedDf.reset_index(drop=True)

print(cleanedDf)
print(len(cleanedDf))

cleanedDf.to_csv(r"C:\Users\baby_\Desktop\Projects\Python Projects\Pandas data cleansing exercises data\Cleaned Customer Call List.csv")