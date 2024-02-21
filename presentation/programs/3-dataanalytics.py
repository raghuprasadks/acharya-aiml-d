"""
Series
Dataframe
"""
import pandas as pd
stockprice =pd.Series([100,110,300,150,180,99])
print("Series")
print(stockprice)
print("data type ",type(stockprice))
print("shape ",stockprice.shape)

print("data frame")
topeconomies={
    "country":["USA","CHINA","GERMANY","JAPAN","INDIA"],
    "GDP":[27,19,4.4,4.2,4.1],
    "RANK":[1,2,3,4,5]
}
df=pd.DataFrame(topeconomies)
print(df)
print("data type ",type(df))
print("shape ",df.shape)
print("display column ",df.columns)
print("display first 5 rows")
print(df.head())
print("display first 3 rows")
print(df.head(3))
print("display bottom 5 rows")
print(df.tail())
print("display bottom 3 rows")
print(df.tail(3))
print("display sample 3 records")
print(df.sample(n=3))
print("display country column")
print(df.country)
print("Second method")
print(df["country"])

print("reading data from a csv file")
ipl = pd.read_csv("ipl.csv")
print(ipl)
print("reading csv file from git")
mydata = pd.read_csv("https://github.com/deepanshu88/Datasets/raw/master/UploadedFiles/income.csv")