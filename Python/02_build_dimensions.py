import pandas as pd

df_death = pd.read_csv('C:/Users/keert/OneDrive/Desktop/AI-Nuclear-Intelligence/Data/raw/rates_death_from_energy_production_per_twh.csv')

# Extract unique energy types (Entity column)
energy_types = df_death['Entity'].dropna().unique()
df_dim_energy = pd.DataFrame({'EnergyTypeName': sorted(energy_types)})
df_dim_energy['EnergyTypeID'] = df_dim_energy.reset_index().index + 1

# Save to cleaned folder
df_dim_energy.to_csv('Data/cleaned/dim_energytype.csv', index=False)

print("✅ Energy type dimension created successfully!")

print(df_dim_energy.head())

# Create the source type data manually in Python as this info isn't in any dataset directly
source_data = {
    'SourceTypeID': [1, 2, 3],
    'SourceTypeName': [
        'Uranium Purchase Price Report',
        'EIA Nuclear Generation Report',
        'Death Rates per TWh Study'
    ]
}

# Create DataFrame
df_source_type = pd.DataFrame(source_data)

# Save to CSV
output_path = ('Data/cleaned/dim_sourcetype.csv')
df_source_type.to_csv(output_path, index=False)

print("dim_sourcetype.csv created successfully at:", output_path)


import pandas as pd

# Create time dimension (e.g., from 2000 to 2025)
years = list(range(2000, 2026))
months = list(range(1, 13))

time_records = []
time_id = 1

for year in years:
    for month in months:
        quarter = (month - 1) // 3 + 1  # ← Add quarter logic here
        time_records.append({
            'TimeID': time_id,
            'Year': year,
            'Month': month,
            'Quarter': quarter
        })
        time_id += 1

df_time = pd.DataFrame(time_records)

# Save to cleaned folder
df_time.to_csv('Data/cleaned/dim_time.csv', index=False)

print("✅ Time dimension created with Quarter included!")
print(df_time.head())
