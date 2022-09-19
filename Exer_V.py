import numpy as np
import pandas as pd


def init_series():
    np_s1 = np.array([1.0, 12.0, 23.0, 34.0, 45.0, 56.0,
                      67.0, 78.0, 89.0, 100.0])
    np_s3 = np.array([5, 5, 5])
    s1 = pd.Series(np_s1, index=[x for x in 'abcdefghij'], name='foo')
    s2 = pd.Series(range(0,10), index=[x for x in 'fghijklmno'])
    s3 = pd.Series(np_s3, index=[x for x in 'xyz'])
    return s1, s2, s3


def init_df(s1, s2):
    df1 = pd.DataFrame(s1)
    df2_joined = pd.concat([s2,s1], axis=1)
    df2 = df2_joined.sort_index()
    return df1, df2


def top_plus_bottom():
    df_OR = pd.read_csv('/mnt/data/public/retaildata/Online Retail.csv')
    df_first_5 = df_OR[['Quantity', 'UnitPrice']].head(5)
    df_last_5 = df_OR[['Quantity', 'UnitPrice']].tail(5)
    df_first = np.array(df_first_5)
    df_last = np.array(df_last_5)
    return df_first + df_last


def count_alone():
    df = pd.read_csv('/mnt/data/public/elections/comelec/voters_profile'
                     '/philippine_2016_voter_profile_by_age_group.csv')
    df_alone = df[['single', 'widow', 'legally_seperated']]
    df["alone"] = df_alone.sum(axis=1)
    return df.sort_values('alone', ascending=False)


def scores_stats():
    df = pd.read_csv('/mnt/data/public/movielens/20m/'
                     'ml-20m/genome-scores.csv')
    ss = df.relevance.describe()
    return ss


def top_cat():
    df = pd.read_csv("/mnt/data/public/agora/Agora.csv",
                     encoding='latin1', usecols=[1])
    return df.value_counts().head(10)


def listing_info():
    df = pd.read_csv('/mnt/data/public/insideairbnb/data.insideairbnb.com'
                     '/united-kingdom/england/london/'
                     '2015-04-06/data/listings.csv.gz')
    df_indexed = df.set_index(df['id'])
    df_sorted = df_indexed.sort_index(ascending=True)
    df_new = df_sorted[['name', 'summary', 'space', 'description']]
    df_with_loc = df_new.loc['11076':'15400']
    return df_with_loc[4:]


def aisle_dep():
    df_products = pd.read_csv('/mnt/data/public/instacart'
                              '/instacart_2017_05_01/products.csv')
    df_indexed = df_products.set_index(df_products['product_id'])
    df_a5 = df_indexed.loc[df_indexed['aisle_id']==5]
    df_sorted = df_a5.sort_values(['aisle_id'])
    df_sorted['product_name_new'] = (
        df_sorted['product_name'].map(str) +
        ' (' + df_sorted['aisle_id'].map(str) + '-' +
        df_sorted['department_id'].map(str) + ')'
    )
    extracted_col = df_sorted["product_name_new"]
    df_indexed = df_indexed.join(extracted_col)
    df_indexed['product_name'] = (df_indexed['product_name_new'].
                                  combine_first(df_indexed['product_name']))
    del df_indexed['product_name_new']
    del df_indexed['product_id']
    return df_indexed


def camsur_reps():
    df = pd.read_csv('/mnt/data/public/elections/comelec/'
                     'congress_results/congressional_results_2013.csv')
    df_surname = df['name'].str.split(',', expand=True)
    extracted_col = df_surname[0]
    df = df.join(extracted_col)
    df_new = df.rename(columns = {0:'surname'})
    df_final = df_new.loc[df['province_or_city']=='Camarines Sur']
    return df_final[['surname','votes_obtained']]


def no_pop():
    df = pd.read_csv('/mnt/data/public/millionsong/'
                     'AdditionalFiles/tracks_per_year.txt', header = None)
    df_split = df[0].str.split('<SEP>', expand=True)
    df_new = (df_split.rename(columns = {0:'year', 1:'track_id',
                                         2:'artist', 3:'title'}))
    df_new.drop(df_new.index[df_new['artist'] == 'Britney Spears'],
                inplace = True)
    df_new.drop(df_new.index[df_new['artist'] == 'Backstreet Boys'],
                inplace = True)
    df_new["year"] = pd.to_numeric(df_new["year"])
    df_new.drop(df_new[df_new['year'] > 1999].index, inplace=True)
    return df_new


def read_trips():
    df = pd.read_csv('/mnt/data/public/nyctaxi/trip_data/'
                     'trip_data_1.csv', nrows=100)
    df['rate_code'] = df['rate_code'].astype(str)
    df['pickup_datetime'] = pd.to_datetime(df["pickup_datetime"])
    df['dropoff_datetime'] = pd.to_datetime(df["dropoff_datetime"]) 
    return df


def write_trips(df_trips):
    df = read_trips()
    df_new = df[['pickup_longitude','pickup_latitude',
                 'dropoff_longitude' ,'dropoff_latitude']]
    return df_new.to_csv('trip_coords.csv')

