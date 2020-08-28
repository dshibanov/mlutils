def fillna_by_mode(df):
    for column in df:
        df[column].fillna(df[column].mode()[0], inplace=True)
    return df

def makeXy(df, target):
    X = df.copy()
    y = X[target]
#     X.drop([target], axis=1)    
    return X.drop([target], axis=1),y

