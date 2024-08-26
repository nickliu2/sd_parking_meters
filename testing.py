import pandas as pd

meters = pd.read_csv("meters_2023_by_day.csv")
meters_loc = pd.read_csv("meter_locations.csv")
meters_loc.head(2)
