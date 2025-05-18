import pandas as pd
import re

#Place the raw data into a dataframe
raw_data = '''Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'''

initial_lines = raw_data.strip().split('\n')
lines = []
for line in initial_lines:
    if line: 
        lines.append(line)

header = lines[0].split(';')

rows = [] 
for line in lines[1:]:
    rows.append(line.split(';'))

df = pd.DataFrame(rows, columns=header)

print("\nOriginal DataFrame:")
print(df)

#1. Fix FlightCodes Column - Missing values are replaced with correct values
df['FlightCodes'] = pd.to_numeric(df['FlightCodes'])
df['FlightCodes'] = df['FlightCodes'].interpolate()
df['FlightCodes'] = df['FlightCodes'].astype(int)

print("\nDataFrame after fixing FlightCodes:\n")
print(df)
print("\nData types:\n")
print(df.dtypes)

#2. Split To_From Column into From and To Columns
df[['From', 'To']] = df['To_From'].str.upper().str.split('_', expand=True)
df = df.drop(columns=['To_From'])

print("\nDataFrame after splitting To_From:\n")
print(df)

#3. Clean Airline Code Column - Remove punctuation and extra spaces 
df['Airline Code'] = df['Airline Code'].str.replace(r'[^a-zA-Z0-9]', ' ', regex=True).str.strip()
df['Airline Code'] = df['Airline Code'].str.replace(r'\s+', ' ', regex=True).str.strip()

#New table with all transformations
print("\nFinal Output:\n")
print(df)

