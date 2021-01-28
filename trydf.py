import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "cost": [5, 4, 4.5]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 
