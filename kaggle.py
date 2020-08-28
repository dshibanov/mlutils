def submit(df, competition):
    my_submission = pd.DataFrame({'PassengerId': df_test['PassengerId'].to_numpy(), 'Survived': predicts})
    df.to_csv('submission.csv', index=False)
    print(api.competition_submit('submission.csv','API Submission',competition))

def api_init():
    api = KaggleApi()
    api.authenticate()
