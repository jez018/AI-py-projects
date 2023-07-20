def saving_clustered_data_in_csv():
    print('---saving_clustered_data_in_csv')
    print(df)
    clustered_df = df.drop(df.columns[0:11], axis=1) #removes unecessary columns
    clustered_df.to_csv('clustered_df.csv') #saves it as a new file in a new extension