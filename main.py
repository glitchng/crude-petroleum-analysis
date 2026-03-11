import pandas as pd
import numpy as np

data = pd.read_excel("Exporters-of-Crude-Petroleum-2016.xlsx")

africa = data[data["Continent"] == "Africa"]["Trade Value"]
asia = data[data["Continent"] == "Asia"]["Trade Value"]

print("Africa Mean:", africa.mean())
print("Africa Std:", africa.std())
print("Africa Min:", africa.min())
print("Africa Max:", africa.max())
print("Africa Range:", africa.max() - africa.min())

print("Asia Mean:", asia.mean())
print("Asia Std:", asia.std())
print("Asia Min:", asia.min())
print("Asia Max:", asia.max())
print("Asia Range:", asia.max() - asia.min())
