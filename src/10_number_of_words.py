# Count Number of Words in a Column

import pandas as pd


def run(url):
    data = pd.read_csv(url, encoding='latin1')
    data['number_words'] = [len(x.split()) for x in data["Article"]]
    return data


if __name__ == "__main__":
    res = run(
        'https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv')
    print(res.head())
