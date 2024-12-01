import pandas as pd

# Read entire CSV file into a DataFrame
df = pd.read_csv('D:\\02_NAUKA\\STRONA-CWICZENIA-FRANCUSKIE\\VERIFIED_2022-10-10_2\\missing-element\\JakubGabryel_cw_1.csv',
                 delimiter=';',
                 encoding='utf-8')


print(df.columns)
print(df.index)
print(df.values)

# Access specific columns
#print(df['column_name'])

'''
# Additional options
df = pd.read_csv('your_file.csv', 
    delimiter=';',  # if not comma-separated
    encoding='utf-8',  # specify encoding
    header=0  # use first row as column names
)

'''
