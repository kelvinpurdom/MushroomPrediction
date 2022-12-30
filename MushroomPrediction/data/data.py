import pandas as pd

DATA_PATH = '../raw_data/secondary_data.csv'

def get_data():
    '''returns a DataFrame with nrows from s3 bucket'''
    df = pd.read_csv(DATA_PATH, sep=";", low_memory=False)
    return df


#removing empty data
def clean_data(df, test=False):

    drop_columns = ['gill-spacing', 'stem-root',
                'stem-surface', 'veil-type',
                'veil-color', 'spore-print-color',
                ]
    df.drop(columns=drop_columns, inplace=True)
    return df


if __name__ == '__main__':
    df = get_data()
