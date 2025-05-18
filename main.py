import pandas as pd

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

print(df)

