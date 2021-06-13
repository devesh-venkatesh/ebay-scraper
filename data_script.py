import pandas as pd

def pandas_script():
  df = pd.read_csv('results.csv')
  print('')
  print('Mean of search results: ')
  print(round(df.mean(), 2))
