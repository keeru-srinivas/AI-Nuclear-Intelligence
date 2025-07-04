import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df_nuclear = pd.read_csv('C:/Users/keert/OneDrive/Desktop/AI-Nuclear-Intelligence/Data/raw/nuclear_energy_overview_eia.csv')
df_uranium = pd.read_csv('C:/Users/keert/OneDrive/Desktop/AI-Nuclear-Intelligence/Data/raw/number_of_plants_producing_uranium_in_us.csv')
df_deathrates= pd.read_csv('C:/Users/keert/OneDrive/Desktop/AI-Nuclear-Intelligence/Data/raw/rates_death_from_energy_production_per_twh.csv')

#explore Nuclear dataset
print("Nuclear_Overview")
print(df_nuclear.head())
print(df_nuclear.info())
print(df_nuclear.describe())
print(df_nuclear.isnull().sum())

#explore Uranium Pricing 
print("Uranium Prices")
print(df_uranium.head())
print(df_uranium.info())
print(df_uranium.describe())
print(df_uranium.isnull().sum())

#explore death rates 
print("Death Rates")
print(df_deathrates.head())
print(df_deathrates.info())
print(df_deathrates.describe())
print(df_deathrates.isnull().sum())