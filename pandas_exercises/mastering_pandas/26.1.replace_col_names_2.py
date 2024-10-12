"""
Exercise 26.1:

Replace col names with underscore in a DataFrame.
"""

import pandas as pd
import re


data = {'caseID': [1, 2, 3, 4, 5, 6], 'agentName': ['George', 'Phil', 'Mike', 'John', 'Kevin', 'Jason']}
df = pd.DataFrame(data)


# Function to add underscore before uppercase letters and make the name lowercase
def add_underscore_before_uppercase(col_name):
    # Use regex to insert an underscore before any uppercase letter
    new_col_name = re.sub(r'([a-z])([A-Z])', r'\1_\2', col_name)
    return new_col_name
    # return new_col_name.lower()  # Optional: Convert the final column name to lowercase


# Apply the function to all columns
df.columns = [add_underscore_before_uppercase(col) for col in df.columns]


print(df)

# Output:
#    case_ID agent_Name
# 0        1     George
# 1        2       Phil
# 2        3       Mike
# 3        4       John
# 4        5      Kevin
# 5        6      Jason