# 

import pandas as pd
from states import states_names

def generate_mappings_states():
    mappings = {}
    for num in range(1, len(states_names) + 1):
        mappings[num] = states_names[num-1]
    return mappings

def norm(x):
    norm = pd.read_csv('stats_for_norm.csv')
    return (x - norm['mean']) / norm['std']

def to_dataframe(input_raw):
    # inputs should be dict or list
    vals = ['region', 'total','elementary_and_secondary_edu', 'higher_edu' ,'public_welfare','health_and_hospitals','highways','police','all_other' ,'population_thousands','year',
     'hispanic','white','black','asian','indigneous']
    
    dict_to_df = dict(zip(vals, list(input_raw)))
    for key,val in dict_to_df.items():
        dict_to_df[key] = [val]
    # turn inputs into pandas dataframe
    df = pd.DataFrame.from_dict(dict_to_df)
    
     # one hot encode 
#     one_hot = generate_mappings_states()
#     df['region'] = df['region'].map(one_hot)
#     df = pd.get_dummies(df, prefix='', prefix_sep='')

#     # normalise 
#     norm_df = norm(df)
#     print(df)

    # return 
    return df