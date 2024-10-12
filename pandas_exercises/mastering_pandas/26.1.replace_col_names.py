"""
Exercise 26.1:

Replace col names with underscore in a DataFrame.
"""

import pandas as pd

data = {'caseId': [1, 2, 3, 4, 5, 6], 'agentName': ['George', 'Phil', 'Mike', 'John', 'Kevin', 'Jason']}

df = pd.DataFrame(data)

col_names = df.columns
# print(col_names)       #   Index(['caseId', 'agentName'], dtype='object')

for col_name in col_names:
    new_col_name = "".join(["_" + char if char.isupper() and not col_name[i - 1].isupper() else char for i, char in
                            enumerate(col_name)]).lstrip("_")

    df = df.rename(columns={col_name: new_col_name})
print(df)

# Output:
#    case_Id agent_Name
# 0        1     George
# 1        2       Phil
# 2        3       Mike
# 3        4       John
# 4        5      Kevin
# 5        6      Jason