from sklearn.model_selection import train_test_split

def time_based_split(df: pd.DataFrame):
    # Sort by date
    df = df.sort_values('date')
    
    # 80% train, 10% validation, 10% test
    train, test = train_test_split(df, test_size=0.2, shuffle=False)
    val, test = train_test_split(test, test_size=0.5, shuffle=False)
    
    return train, val, test
