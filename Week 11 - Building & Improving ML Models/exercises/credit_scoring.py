import pandas as pd

def load_data(path):
    """Load the dataset from the provided file path"""
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f'File was not found at the location: {path}')


def explore_data(df):
    print('`nCOLUMN NAMES')
    print(df.columns.tolist())

    print('\nDATASET SHAPE')
    print(df.shape)

    print('\nBASIC INFO HIGHLIGHT')
    print(df.info())

    print('\nMEMORY USAGE')
    print(f'{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB')

    print('\nDATASET PREVIEW')
    print(df.head(7))

    print('\nBASIC STATISTICS')
    print(df.describe())

    print('\nMISSING VALUES')
    info_df = pd.DataFrame({
        'Data Types': df.dtypes,
        'Missing Values': df.isnull().sum(),
        'Missing %': ((df.isnull().sum() / len(df)) * 100).round(2)
    })
    print(info_df)


def main():
    credit_df = load_data('../../data/credit_scoring.csv')

    explore_data(credit_df)


if __name__ == '__main__':
    main()