import datetime

import pandas as pd


df1 = pd.read_csv('testing_data_old.csv', sep=',')
df2 = pd.read_csv('testing_data_new.csv', sep=',')


def main():
    """Основной блок программы"""
    df3 = get_updated_dataframe(df1, df2)
    save_df(df3)


def get_updated_dataframe(df1: pd.DataFrame,
                          df2: pd.DataFrame) -> pd.DataFrame:
    """Принимает на вход: df1, df2.Возвращает обновленный df"""
    column_names = df2.columns[:-1].tolist()
    return (pd.concat([df1, df2])
            .drop_duplicates(column_names, keep='first')
            .drop_duplicates(['ID'], keep='last')
            )


def save_df(df: pd.DataFrame) -> None:
    """Сохраняет файл в папку рядом со скриптом main.py.
       Сохраненный CSV файл использует разделитель ','
    """
    date = str(datetime.date.today())
    df.to_csv(f'ready_data_{date}.csv', index=False, sep=',')


if __name__ == "__main__":
    main()
