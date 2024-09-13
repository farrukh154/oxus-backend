from .constants import CATEGORY_COLUMN
from .constants import CATEGORY

def calculate_standard(df, i):
  df.loc[df['contract code'] != None, f'{CATEGORY_COLUMN}{i}'] = CATEGORY['c1']['id']

def calculate_under_control(df, i):
  df.loc[df[f'late_days{i}'].astype(int) >= 8, f'{CATEGORY_COLUMN}{i}'] = CATEGORY['c2']['id']

def calculate_not_standard(df, i):
  df.loc[df[f'late_days{i}'].astype(int) >= 30, f'{CATEGORY_COLUMN}{i}'] = CATEGORY['c3']['id']

def calculate_uncertain(df, i):
  df.loc[df[f'late_days{i}'].astype(int) >= 90, f'{CATEGORY_COLUMN}{i}'] = CATEGORY['c4']['id']

def calculate_hopeless(df, i):
  df.loc[df[f'late_days{i}'].astype(int) >= 180, f'{CATEGORY_COLUMN}{i}'] = CATEGORY['c5']['id']

def calculate_o_court_case(df):
  df.loc[df['dateofcourtcases'].notnull(), 'court_case'] = 5

def calculate_max_category(df):
  df['max_category'] = df[['Category_0', 'Category_1', 'Category_2', 'Category_3', 'Category_4', 'Category_5', 'Category_6', 'court_case']].max(axis=1)
  # return df

def calculate_o_RSCHD(df):
  df.loc[df['rschd'].astype(int) > 0, 'category_add_if_RSCHD'] = 1
  df.loc[df['contract code'] != None, 'final_category'] = df['max_category'] + df['category_add_if_RSCHD']
  df.loc[df['final_category'] > 5, 'final_category'] = 5


def calculate_o_parallels(df):
  df['Parallel'] = df['customerid'].duplicated(keep=False).map({True: 'Yes', False: 'No'}) # no need, used just for we can add
  df['final_category'] = df.groupby('customerid')['final_category'].transform('max')

def calculate_o_set_percentage(df):
  df.loc[df['currency'] == 'TJS', 'percentage'] = CATEGORY['c1']['TJS']
  df.loc[df['currency'] == 'USD', 'percentage'] = CATEGORY['c1']['USD']

  df.loc[(df['currency'] == 'TJS') & (df['final_category'] >= 2), 'percentage'] = CATEGORY['c2']['TJS']
  df.loc[(df['currency'] == 'USD') & (df['final_category'] >= 2), 'percentage'] = CATEGORY['c2']['USD']

  df.loc[(df['currency'] == 'TJS') & (df['final_category'] >= 3), 'percentage'] = CATEGORY['c3']['TJS']
  df.loc[(df['currency'] == 'USD') & (df['final_category'] >= 3), 'percentage'] = CATEGORY['c3']['USD']

  df.loc[(df['currency'] == 'TJS') & (df['final_category'] >= 4), 'percentage'] = CATEGORY['c4']['TJS']
  df.loc[(df['currency'] == 'USD') & (df['final_category'] >= 4), 'percentage'] = CATEGORY['c4']['USD']

  df.loc[(df['currency'] == 'TJS') & (df['final_category'] >= 5), 'percentage'] = CATEGORY['c5']['TJS']
  df.loc[(df['currency'] == 'USD') & (df['final_category'] >= 5), 'percentage'] = CATEGORY['c5']['USD']