state_codes = [
'AL',
'AK',
'AZ',
'AR',
'CA',
'CO',
'CT',
'DE',
'FL',
'GA',
'HI',
'ID',
'IL',
'IN',
'IA',
'KS',
'KY',
'LA',
'ME',
'MD',
'MA',
'MI',
'MN',
'MS',
'MO',
'MT',
'NE',
'NV',
'NH',
'NJ',
'NM',
'NY',
'NC',
'ND',
'OH',
'OK',
'OR',
'PA',
'RI',
'SC',
'SD',
'TN',
'TX',
'UT',
'VT',
'VA',
'WA',
'WV',
'WI',
'WY']

states_names = [
'Alabama',
'Alaska',
'Arizona',
'Arkansas',
'California',
'Colorado',
'Connecticut',
'Delaware',
'Florida',
'Georgia',
'Hawaii',
'Idaho',
'Illinois',
'Indiana',
'Iowa',
'Kansas',
'Kentucky',
'Louisiana',
'Maine',
'Maryland',
'Massachusetts',
'Michigan',
'Minnesota',
'Mississippi',
'Missouri',
'Montana',
'Nebraska',
'Nevada',
'New Hampshire',
'New Jersey',
'New Mexico',
'New York',
'North Carolina',
'North Dakota',
'Ohio',
'Oklahoma',
'Oregon',
'Pennsylvania',
'Rhode Island',
'South Carolina',
'South Dakota',
'Tennessee',
'Texas',
'Utah',
'Vermont',
'Virginia',
'Washington',
'West Virginia',
'Wisconsin',
'Wyoming']

col_names = ["region", "total", "elementary_and_secondary_edu", "higher_edu", "public_welfare", "health_and_hospitals", "highways", "police", "all_other", "population_thousands"]
proper_names = ["Region", "Total Spending", "Elementary and Secondary Education", "Higher Education", "Public Welfare", "Health and Hospitals", "Highways", "Police", "Other", "Population"]

def get_state(code):
    for i in range(0, len(states_names)):
        if code == state_codes[i]:
            return states_names[i]
    return code

def get_proper_name(name):
    for i in range(0, len(proper_names)):
        if name == col_names[i]:
            return proper_names[i]
    return name

# to add status codes
def get_state_code(row):
    for i in range(0, len(states_names)):
        if (states_names[i] == row['region']):
            return state_codes[i]