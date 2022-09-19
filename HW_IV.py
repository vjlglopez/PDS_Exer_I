import numpy as np
import pandas as pd


def peel(df):
    dfc = df.copy()
    df_new = dfc[1:-1]
    df_final = df_new.iloc[:, 1:-1]
    return df_final


def patch(df, upper_left, lst):
    if len(upper_left) != len(lst[0]):
        raise ValueError
    else:
        ul = upper_left
        t_ul = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
        ul_new = (t_ul[ul[0]], t_ul[ul[1]])
        val = pd.DataFrame(lst)

        for i in range(len(val)):
            if ul_new[0] == 1 and ul_new[1] == 1:
                val.columns += i
                val.index += i
            elif ul_new[0] == 1:
                val = val.rename(columns={i: ul_new[1] + i})
                val.index += i
            elif ul_new[1] == 1:
                val.columns += i
                val = val.rename(index={i: ul_new[0] + i})
            else:
                val = val.rename(index={i: ul_new[0] + i},
                                  columns={i: ul_new[1] + i})
        df.iloc[val.index, val.columns] = lst
        return df
    
    
def pop_stats(province, municipality=None, census_year=2015):
    pr = province.lower()
    cy = str(census_year)[-2:]

    df = pd.read_csv('Municipality Data - PSA.csv')
    df.rename(columns={
        'Feb-60': '60', 'May-70': '70', 'May-75': '75',
        'May-80': '80', 'May-90': '90', 'Sep-95': '95',
        'May-00': '00', 'Aug-07': '07', 'May-10': '10',
        'Aug-15': '15'}, inplace=True)
    df['province'] = df['province'].str.lower()
    df['municipality'] = df['municipality'].str.lower()
    list_pr = list(df['province'].unique())
    list_mun = list(df['municipality'].unique())
    list_date = (list(pd.melt(df, id_vars=['province', 'municipality'])
                      ['variable'].unique()))

    if municipality is not None:
        mun = municipality.lower()
        if (pr not in list_pr and mun not in list_mun) or cy not in list_date:
            return None
        else:
            df_new1 = df
            df_new1 = df_new1.set_index('municipality')
            return int(df_new1.loc[mun, cy])
    else:
        if pr not in list_pr or cy not in list_date:
            return None
        else:
            df_new2 = df
            df_new2 = df_new2.drop(df[df.is_total == 1].index)
            new2_total = df_new2.groupby('province')[cy].sum()
            new2_mean = df_new2.groupby('province')[cy].mean()
            new2_std = df_new2.groupby('province')[cy].std()
            df_fin2 = pd.concat([new2_total, new2_mean, new2_std], axis=1)
            return df_fin2.loc[pr]
        
        
def plot_pop(municipalities):
    df = pd.read_csv('Municipality Data - PSA.csv')
    df_new = (
        df.groupby('municipality')[['Feb-60', 'May-70', 'May-75', 'May-80',
                                    'May-90', 'Sep-95', 'May-00', 'Aug-07',
                                    'May-10', 'Aug-15']].mean())
    df_new = df_new.rename(
        index={'CITY OF MANILA': 'CiTy Of MaNiLa',
               'CITY OF MAKATI': 'City of Makati',
               'CITY OF ISABELA': 'city of isabela',
               'ANGELES CITY': 'Angeles City'}
    )
    manila = pd.Series(df_new.loc['CiTy Of MaNiLa'])
    makati = pd.Series(df_new.loc['City of Makati'])
    quezon = pd.Series(df_new.loc['QUEZON CITY'])
    isabela = pd.Series(df_new.loc['city of isabela'])
    angeles = pd.Series(df_new.loc['Angeles City'])

    graph = manila.plot(label="CiTy Of MaNiLa")
    graph = makati.plot(label="City of Makati")
    graph = quezon.plot(label="QUEZON CITY")
    graph = isabela.plot(label="city of isabela")
    graph = angeles.plot(label="Angeles City")
    graph.legend()
    graph.figure.canvas.draw()
    return graph


def find_max(province):
    df = pd.read_csv('Municipality Data - PSA.csv')
    df['province'] = df['province'].str.lower()
    p = province.lower()
    if p not in df['province'].tolist():
        raise ValueError
    else:
        df[['Feb-60', 'May-70', 'May-75', 'May-80',
            'May-90', 'Sep-95', 'May-00', 'Aug-07',
            'May-10', 'Aug-15']] = (
            abs(df[['Feb-60', 'May-70', 'May-75', 'May-80',
                    'May-90', 'Sep-95', 'May-00', 'Aug-07',
                    'May-10', 'Aug-15']].diff(axis=1)))
        df = df.drop(df[df.is_total == 1].index)
        df_new = df.melt(id_vars=['province', 'municipality'],
                         value_vars=['Feb-60', 'May-70', 'May-75', 'May-80',
                                     'May-90', 'Sep-95', 'May-00', 'Aug-07',
                                     'May-10', 'Aug-15'],
                         value_name='population')
        df_fin = df_new.groupby(['province']).agg({'population': 'max'})
        value = df_fin.loc[p][0]
        df_ans = df_new.set_index(['municipality', 'variable'])
        muni = df_ans.population[df_ans.population == value].index.to_list()
        dated = muni[0][1]
        col_list = df.columns[2:-1].to_list()
        indexed = col_list.index(dated)
        couple = [col_list[indexed], col_list[indexed - 1]]
        return muni[0][0], couple[1], couple[0]
    
    
def most_populous():
    df = pd.read_csv('Municipality Data - PSA.csv')
    df = df.drop(df[df.is_total == 1].index)
    df_final = (df.groupby(['province'])['Aug-15'].mean()
                .nlargest(10).sort_values(ascending=False))
    return df_final


def hourly_hashtag():
    df = pd.read_csv('/mnt/data/public/nowplaying-rs/'
                     'nowplaying_rs_dataset/user_track_hashtag_timestamp.csv',
                     nrows=1_000_000)
    df['created_at'] = (pd.to_datetime(df['created_at'].astype(str)) +
                        pd.DateOffset(hours=8))
    df.set_index('created_at', inplace=True)
    df.index = df.index.tz_localize('Asia/Manila')
    df_new = df.reset_index()
    df_fin = (df_new.groupby(['hashtag']).agg({'created_at': 'value_counts'})
              .rename(columns={'created_at': 'count'}))
    df_final = (df_fin.groupby(['hashtag', pd.Grouper(freq='H', level=1)])
                ['count'].sum().reset_index())
    return df_final


def aisle_counts():
    df1 = pd.read_csv('/mnt/data/public/instacart/instacart_2017_05_01/'
                      'order_products__prior.csv', nrows=1_000_000)
    df2 = pd.read_csv('/mnt/data/public/instacart/'
                      'instacart_2017_05_01/products.csv')
    df3 = pd.read_csv('/mnt/data/public/instacart/'
                      'instacart_2017_05_01/aisles.csv')
    df4 = pd.read_csv('/mnt/data/public/instacart/'
                      'instacart_2017_05_01/orders.csv')
    df_merged1 = pd.merge_ordered(df1, df2, how='inner', on=['product_id'])
    df_merged2 = pd.merge_ordered(df_merged1, df3,
                                  how='inner', on=['aisle_id'])
    df_merged3 = pd.merge_ordered(df_merged2, df4,
                                  how='inner', on=['order_id'])
    df_new = df_merged3.groupby(['aisle'])['add_to_cart_order'].count()
    return df_new.sort_values(ascending=False)


def from_to():
    df = pd.read_csv('/mnt/data/public/wikipedia/clickstream/'
                     'clickstream/2017-11/clickstream-enwiki-2017-11.tsv.gz',
                     sep='\t', compression='gzip', nrows=1_000, header=None)
    df_new = pd.pivot_table(df, index=[df[0]], columns=[df[1]])
    df_fin = df_new.fillna(0)
    df_fin.columns = df_fin.columns.droplevel(0)
    df_final = df_fin.rename_axis(None, axis=1)
    return df_final

