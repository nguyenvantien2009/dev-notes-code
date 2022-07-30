import pandas as pd

data = [
    ['user1', 'url_1', 12, '2022-01-01'],
    ['user1', 'url_2', 112, '2022-01-02'],
    ['user1', 'url_2', 11, '2022-01-03'],
    ['user1', 'url_2', 112, '2022-01-04'],
    ['user1', 'url_4', 112, '2022-01-04'],
    ['user1', 'url_2', 112, '2022-01-05'],
    ['user1', 'url_4', 12, '2022-01-01'],
    ['user2', 'url_1', 11, '2022-02-01'],
    ['user4', 'url_3', 1112, '2022-01-01'],
    ['user3', 'url_2', 10, '2022-01-10'],
    ['user3', 'url_2', 12, '2022-02-10'],
    ['user3', 'url_2', 12, '2022-02-11'],
    ['user3', 'url_2', 1112, '2022-01-01']
]

df = pd.DataFrame(data=data, columns=[
  'user', 'url', 'number_requests', 'date'
])

df_train = pd.DataFrame()
users = list(set(df['user'])) 
for u in users:
  df_user = df[df['user']==u][[
    'url', 'number_requests', 'date'
  ]]
  df_user_pivot =  df_user.pivot(
    columns='url', 
    values='number_requests', 
    index='date'
  )
  df_corr = df_user_pivot.corr()
  df_corr.fillna(0, inplace=True)
  
  # convert dataframe to 1 row.
  df_row = pd.DataFrame(df_corr.stack()).T

  # set index with user.
  df_row['user'] = u
  df_row.set_index('user', inplace=True)
  
  # concat dataframe from series row.
  df_train = pd.concat([df_train, df_row]).fillna(0)

# show dataframe for training.
display(df_train)
