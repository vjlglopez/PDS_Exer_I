import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np
import pandas as pd


def double_work(df):
    t_start = '2021-01-01 09:00:00'
    t_end = '2021-01-01 17:00:00'
    df.loc[t_start:t_end, 'a'] = df.loc[t_start:t_end, 'b'] * 2
    return df


def hourly_mem_usage():
    parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %X')
    df = pd.read_csv('mem.csv', parse_dates=['Time'], date_parser=parser)
    df['Time'] = (pd.to_datetime(df['Time'].astype(str)) +
                  pd.DateOffset(hours=8))
    df.set_index('Time', inplace=True)
    df.index = df.index.tz_localize('Asia/Manila')
    return df['accesslab'].resample('H').mean()


def daily_mem_usage():
    parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %X')
    df = pd.read_csv('mem.csv', parse_dates=['Time'], date_parser=parser)
    df['Time'] = pd.DatetimeIndex(df['Time']).to_period('D')
    df.set_index('Time', inplace=True)
    df_new = df['accesslab'].resample('D').mean()
    return df_new


def longest_distances():
    df = pd.read_csv('/mnt/data/public/nyctaxi/trip_data/trip_data_1.csv', 
                     nrows=1_000_000, parse_dates=['pickup_datetime'])
    df_new = (df.groupby([df.pickup_datetime.dt.hour, 'passenger_count'])
              ['trip_distance'].max())
    return df_new


def mean_ratings():
    df = pd.read_csv('/mnt/data/public/insideairbnb/'
                     'data.insideairbnb.com/united-kingdom/'
                     'england/london/2015-04-06/data/listings.csv.gz', 
                     compression='gzip', parse_dates=['host_since'])
    df['review_scores_ratings'] = (
        df.filter(
            items=['review_scores_cleanliness',
                   'review_scores_checkin',
                   'review_scores_communication',
                   'review_scores_location',
                   'review_scores_value']).mean(axis=1,
                                                numeric_only=True,
                                                skipna=True)
    )
    df.set_index('host_since', inplace=True)
    df_new = (df.groupby([pd.Grouper(freq='M',level=0)])
              ['review_scores_ratings'].mean())
    return df_new


def product_aisles():
    df1 = pd.read_csv('/mnt/data/public/instacart/'
                      'instacart_2017_05_01/products.csv')
    df2 = pd.read_csv('/mnt/data/public/instacart/'
                      'instacart_2017_05_01/aisles.csv')
    df_merged = pd.merge_ordered(df1, df2 , how='inner', on=['aisle_id'])
    return df_merged.set_index(['product_id'])


def tracks_with_loc():
    df1 = pd.read_csv('/mnt/data/public/millionsong/AdditionalFiles/'
                      'unique_tracks.txt', header=None,
                      on_bad_lines='skip')
    df2 = pd.read_csv('/mnt/data/public/millionsong/AdditionalFiles/'
                      'artist_location.txt', header=None,
                      on_bad_lines='skip')
    df1_split = df1[0].str.split('<SEP>', expand=True)
    df2_split = df2[0].str.split('<SEP>', expand=True)
    
    df1_renamed = df1_split.rename(columns={0:'track_id', 1:'song_id',
                                            2:'artist', 3:'title'})
    df2_renamed = df2_split.rename(columns={0:'artist_id', 1: 'lat', 2:'lon',
                                            3:'artist', 4:'location'})
    
    df2_unique = df2_renamed.drop_duplicates(subset='artist', keep='first')
    df_merged = pd.merge(df1_renamed, df2_unique, how='left', on=['artist'])
    return df_merged


def party_votes():
    df = pd.read_csv('/mnt/data/public/elections/comelec/'
                     'congress_results/congressional_results_2013.csv')
    df_new  = (df.groupby(['province_or_city','party_affiliation'])
               ['votes_obtained'].first().unstack())
    df_fill = df_new.fillna(0)
    df_final = df_fill.astype('int')
    return df_final


def naia_traffic():
    df = pd.read_csv('/mnt/data/public/opendata/transport/caap-aircraft/'
                     'airdata_aircraft_movement_2016.csv')
    df_NAIA = df[df['airport'] == 'NAIA']
    df_new = df_NAIA.drop(['region', 'airport', 'total',
                           'Unnamed: 16'], axis=1)

    df_fin = pd.melt(df_new, id_vars='airline_operator',var_name='month',
                     value_name='passengers')
    df_fin['passengers'] = df_fin['passengers'].astype(int)
    df_fin['month'] = df_fin['month'].str.title()
    return df_fin


def pudo():
    df = pd.read_csv('/mnt/data/public/nyctaxi/all/'
                     'yellow_tripdata_2017-12.csv', nrows=1_000_000)
    df_new = df.groupby(['PULocationID']).agg({'DOLocationID': 'nunique'})
    df_new  = (df.groupby(['PULocationID','DOLocationID'])
               ['DOLocationID'].sum().unstack())
    df_fill = df_new.fillna(0)
    df_final = df_fill.astype('int')
    return df_final

