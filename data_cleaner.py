#removed duplicates, replaced empty data with average or median of the columns
def clean_data(df):
    df_cleaned = df.drop_duplicates().copy()
    df_cleaned['sales'] = df_cleaned['sales'].fillna(df_cleaned['sales'].mean())
    df_cleaned['customer_satisfaction'] = df_cleaned['customer_satisfaction'].fillna(df_cleaned['customer_satisfaction'].mean())
    df_cleaned['delivery_days'] = df_cleaned['delivery_days'].fillna(df_cleaned['delivery_days'].median())

    return df_cleaned