import pandas as pd
import numpy as np

# Read the CSV file
slm = pd.read_csv(r"C:\Users\kumar\Downloads\Anil_project (1)\Anil_project\master\prodfile\slm_scn_definition.csv", sep=",")
inp=pd.read_csv(r"C:\Users\kumar\Downloads\Anil_project (1)\Anil_project\master\input\scenario_input.csv", sep=",")

# Print the DataFrame
print(slm)
print(inp)
# Create a dictionary from the DataFrame
scenario_dict = {row['SCENARIONAME']: row['SCENARIOID'] for index, row in slm.iterrows()}
scenario1_dict = {row['SCENARIONAME']: row['SCENARIOID'] for index, row in inp.iterrows()}

# Print the dictionary
print(scenario_dict)
print(scenario1_dict)
