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

def to_dataframe(input):
    # inputs should be dict or list
    vals = ['region', 'total','elementary_and_secondary_edu', 'higher_edu' ,'public_welfare','health_and_hospitals','highways','police','all_other' ,'population_thousands','year',
     	'status_code','hispanic','white','black','asian','indigneous']

    # turn inputs into pandas dataframe
    df = pd.DataFrame(columns=vals)
    df.loc[0] = input

    # one hot encode 
    one_hot = generate_mappings_states()
    df['region'] = df['region'].map(one_hot)
    df = pd.get_dummies(df, prefix='', prefix_sep='')

    # normalise 
    norm_df = norm(df)

    # return 
    return norm_df
