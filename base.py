import pandas as pd 
import requests


# class Base:
#     # 
#     def __init__(self):
#         self.df = None
#         self = pd.read_csv(r'C:\Users\patty\OneDrive\Desktop\MongoDB\student-por.csv')
# #display(df)
#     def return_string(self):
#         return self
    
# def get_data(self):
#     ''' Scraping the data from the dataset and create a dataframe object from it'''
#     response = requests.get(self)
#     r = response.json()['data'][0]['download_uri']
#     response1 = requests.get(r)
#     self.df = pd.DataFrame.from_dict(response1.json())
#     return self.df

# if __name__ == '__main__':
#     c = Base()
#     print(c.return_string())
#     print(c.df)
# c.df.to_csv('student_poor_clnd.csv')

def wrangle(filepath):
    return pd.read_csv(filepath)


def wrangle(filepath):
    df = pd.read_csv(filepath)

    return df 
if __name__ == '__main__':
    df = wrangle(r'C:\Users\patty\OneDrive\Desktop\MongoDB\student-por.csv')
    df.to_csv('student_por_cleaned.com', index=False)
