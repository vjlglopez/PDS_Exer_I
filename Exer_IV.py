import numpy as np

def z_per_element(x, y):
    df_x = np.array(x)
    df_y = np.array(y)
    z = np.exp(df_x**2 + np.cos(df_y)) + 2
    return z


def row_dot(x, y):
    df_x = np.array(x)
    df_y = np.array(y)
    z = np.sum(np.matmul(df_x,df_y), axis=1)
    return z


def shrink(x):
    df_x = np.array(x)
    x_trans = df_x[0::2].T
    z = x_trans[1::2]
    return z


def multiplier(x, y):
    df_x = np.array(x)
    df_y = np.array(y)
    z = np.transpose(np.transpose(df_x) * df_y)
    return z


def double_quadrant(x):
    df_x = np.array(x)
    LR = np.vsplit(df_x,2)
    UL = np.hsplit(LR[0],2)
    UL[0] = UL[0] * 2
    UL_new = np.concatenate((UL[0], UL[1]),axis=1)
    LR_new = np.concatenate((UL_new, LR[1]),axis=0)
    return LR_new

