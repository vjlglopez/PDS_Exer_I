import numpy as np
import pandas as pd


def largest_invoice():
    df_OR = pd.read_csv('/mnt/data/public/retaildata/Online Retail.csv')
    dtypes = {'InvoiceNo': str}
    df_OR_new = df_OR.InvoiceNo.value_counts(ascending=False).head(10)
    df_OR_new.index.name = 'InvoiceNo'
    return df_OR_new


def most_daily_tagged_artists():
    df = pd.read_csv('/mnt/data/public/hetrec2011/lastfm/'
                     'user_taggedartists.dat', sep='\t')
    df['date'] = pd.to_datetime(df[['year','month','day']])
    df_unique = df.groupby(['date','userID'])['artistID'].nunique()
    df_largest = df_unique.nlargest(10)
    df_final = df_largest.index.get_level_values(1)
    return df_final.to_list()


def bin_names():
    df_opd = pd.read_csv('/mnt/data/public/brazilian-ecommerce/'
                         'olist_products_dataset.csv')
    df_opd['pnl_bins'] = pd.cut(df_opd['product_name_lenght'], bins=10)
    return df_opd.groupby(['pnl_bins'])['product_description_lenght'].median()


def charge_per_state():
    df = pd.read_table('/mnt/data/public/cms-gov/'
                       'Medicare_Provider_Util_Payment_PUF_CY2013/'
                       'Medicare_Provider_Util_Payment_PUF_CY2013.txt', 
                       nrows=1_000_000)

    df_vals = (df.groupby(['NPPES_PROVIDER_STATE'])
               ['AVERAGE_SUBMITTED_CHRG_AMT'].mean())
    x = df_vals.index.get_level_values(0)
    y = df_vals.to_numpy()
    y_range = [0, 100, 200, 300, 400, 500, 600, 700, 800]
    y_range1 = ['0', '100', '200', '300', '400',
                '500', '600', '700', '800']
    df_final = pd.DataFrame(x)
    df_final['Average submitted charge amount ($)'] = y

    graph = df_final.plot(legend=None, kind = 'bar', figsize=(12, 8))
    graph.set_xticklabels(x)
    graph.yaxis.set_ticks(y_range)
    graph.yaxis.set_ticklabels(y_range1)
    graph.set_ylim([0, 700])
    graph.set_xlabel('NPPES_PROVIDER_STATE')
    graph.set_ylabel('Average submitted charge amount ($)')
    
    return graph


def voters_profile():
    df = pd.read_csv('/mnt/data/public/elections/comelec/voters_profile/'
                     'philippine_2016_voter_profile_by_provinces_and_cities_'
                     'or_municipalities_including_districts.csv')
    location = dict({'17-19': (0, 0), '20-24': (0, 1), '25-29': (0, 2),
                     '30-34': (0, 3), '35-39': (1, 0), '40-44': (1, 1),
                     '45-49': (1, 2), '50-54': (1, 3), '55-59': (2, 0),
                     '60-64': (2, 1), '65-above': (2, 2), 'female': (2, 3),
                     'indigenous_people': (3, 0), 'legally_seperated': (3, 1),
                     'male': (3, 2), 'married': (3, 3),
                     'person_with_disability': (4, 0),
                     'single': (4, 2), 'registered_voter': (4, 1),
                     'widow': (4, 3)})
    row_count = 5
    column_count = 4
    w_space = 0.4
    h_space = 0.5
    fig, ax = plt.subplots(row_count, column_count, figsize=(10, 12), dpi=300)
    fig.subplots_adjust(wspace=w_space, hspace=h_space)
    bin_count = 10
    for k, v in location.items():
        ax[v].hist(df[k], bins=bin_count)
        ax[v].set_title(k)
        ax[v].grid(visible=True, which='Major', axis='both')
    fig.canvas.draw()
    return fig


def standardize_ratings():
    df_r = pd.read_csv('/mnt/data/public/movielens/'
                       '20m/ml-20m/ratings.csv', nrows=1_000_000)
    df_mean = df_r.rating.describe()['mean']
    df_std = df_r.rating.describe()['std']
    df_r['rating'] = (df_r['rating'] - df_mean)/df_std
    return df_r


def user_songcount():
    df = pd.read_csv('/mnt/data/public/millionsong/taste/train_triplets.txt',
                     nrows=1000000,  header=None)
    df_split = df[0].str.split('\t', expand=True)
    return df_split[0].str[:5].value_counts().sort_index()


def at_least_10():
    df = pd.read_csv('/mnt/data/public/nowplaying-rs/nowplaying_rs_dataset/'
                 'user_track_hashtag_timestamp.csv', nrows=1_000)
    df1 = df.groupby(['user_id'])['track_id'].nunique().reset_index()
    df2 = df1[~(df1['track_id'] <= 10)]
    s1 = pd.merge_ordered(df, df2 , how='inner', on=['user_id'])
    del s1['track_id_y']
    s1.rename(columns={'track_id_x':'track_id','hashtag_x':'hashtag',
                       'created_at_x':'created_at'}, inplace=True)
    final_df = s1.sort_values(by=['created_at'], ascending=True).reset_index()
    del final_df['index']

    b, c = final_df.iloc[2].copy(), final_df.iloc[3].copy()
    final_df.iloc[2],final_df.iloc[3] = c,b

    d, e = final_df.iloc[4].copy(), final_df.iloc[5].copy()
    final_df.iloc[4],final_df.iloc[5] = e,d

    return final_df


def source_dest():
    path = '/mnt/data/public/wikipedia/clickstream/'
    'clickstream/2017-11/clickstream-enwiki-2017-11.tsv.gz'
    df = pd.read_csv(path, sep='\t',compression='gzip',
                     nrows=1000, header=None)
    return df.groupby(0).agg({1:lambda x: list(x)}).squeeze()


def mean_std_votes():
    df = pd.read_csv('/mnt/data/public/elections/comelec/'
                     'congress_results/congressional_results_2013.csv')
    df_fin = (df.groupby(['province_or_city'])
              .agg({'votes_obtained':[np.mean, np.std]}))
    return df_fin

