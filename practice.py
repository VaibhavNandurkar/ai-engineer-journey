import pandas as pd 
# import numpy as np

#                         #Series

# IPL_team = ["CSK", "RCB", "MI", "SRH", "GT"]

# series = pd.Series(IPL_team, index=[101,102,103,104,105])
# print(series.loc[103])


#                         #DataFrame

# dataframe = {
#         "Player": ['Rohit', 'Kohli', 'Siraj', 'Warner', 'Dhoni'],
#         "Team":   ['MI', 'RCB', 'GT', 'SRH', 'CSK'],
#         "Runs":   [450, 560, 50, 500, 256],
#         "Wickets": [0, 0, 18, 0, 0]
# }
# df = pd.DataFrame(dataframe)
# df["Performance"] = np.where(df["Runs"]>50,"Good","Average")
# print(df[["Player","Runs"]])
# print(df[df["Runs"] > 50])
# print(df)

df = pd.read_csv("pokemon_data.csv")
                        #1st question
# print(df.shape)
# print(df.head())
# print(df.columns.to_list())
                        #2nd question
# print(df["Name"])   #ans = str
# print(df[["Name", "Type1"]])  #ans = 150 rows * 2 columns
                        #3rd question
# print(df.iloc[0:10])
# print(df.iloc[5:15, [1, 5]])
# print(df.iloc[-5:])
                        #4th question
# print(df.loc[24, ["Name", "Type1", "Height"]])
# print(df.loc[10:20, ["Name", "Weight"]])

                        #5th question
# fire = df["Type1"] == "Fire" 
# print(fire)
# fire_count = df[fire] 
# print(len(fire_count))           #ans 12       

# weight = df["Weight"]  > 100
# print(weight)
# weight_count = df[weight]
# print(len(weight_count))   # ans 15

# legendary = df["Legendary"] == True
# print(legendary)
# legendary_count = df[legendary]
# print(len(legendary_count))   #ans 4

                        #6th question
# print(df[(df["Type1"] == "Water") & (df["Weight"] > 50)])      
# print(df[(df["Type1"] == "Fire") | (df["Type1"] == "Ice")])                  
# tall = df[(df["Legendary"] == False) & (df["Height"] > 2)]  
# print(tall["Name"])

                        #8th question 

# df.loc[df["Legendary"]== True, "Weight"] = 999
# print(df[df["Legendary"] == True]["Weight"])

# df2 = pd.read_csv("pokemon_data.csv")
# df2[df2["Legendary"]== True]["Weight"]=999
# print(df2[df2["Legendary"] == True]["Weight"])

                        #10th question
                    
water_mask = (df["Type1"] == "Water") | (df["Type2"] == "Water")
heavy_mask = df["Weight"] > 50
heavy_water = water_mask & heavy_mask
result = df.loc[heavy_water, ["Name", "Type1", "Type2", "Weight"]]
df.loc[heavy_water,"HeavyWater"] = True
print(result)
print(result.shape)