import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    
    calculations = {}
    a = np.array(list).reshape(3,3)

    # calculate mean values
    f_mean = a.mean()
    a0_mean = a.mean(axis=0).tolist()
    a1_mean = a.mean(axis=1).tolist()
    calculations['mean'] = [a0_mean, a1_mean, f_mean]

    # calculate variance values
    f_var = a.var()
    a0_var = a.var(axis=0).tolist()
    a1_var = a.var(axis=1).tolist()
    calculations['variance'] = [a0_var, a1_var, f_var]

    # calculate std dev values
    f_std = a.std()
    a0_std = a.std(axis=0).tolist()
    a1_std = a.std(axis=1).tolist()
    calculations['standard deviation'] = [a0_std, a1_std, f_std]

    # calculate max values
    f_max = a.max()
    a0_max = a.max(axis=0).tolist()
    a1_max = a.max(axis=1).tolist()
    calculations['max'] = [a0_max, a1_max, f_max]

    # calculate min values
    f_min = a.min()
    a0_min = a.min(axis=0).tolist()
    a1_min = a.min(axis=1).tolist()
    calculations['min'] = [a0_min, a1_min, f_min]

    # calculate sum values
    f_sum = a.sum()
    a0_sum = a.sum(axis=0).tolist()
    a1_sum = a.sum(axis=1).tolist()
    calculations['sum'] = [a0_sum, a1_sum, f_sum]

    return calculations