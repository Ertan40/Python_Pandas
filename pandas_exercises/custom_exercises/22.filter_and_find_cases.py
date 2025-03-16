import pandas as pd


surveys = "C://users//ertan//Downloads//data_csat.xlsx"
df_survey = pd.read_excel(surveys)

print(f"Columns survey: {df_survey.columns.tolist()}")

# Count of nulls
df_survey_null = df_survey['Case'].isna().sum()
print(df_survey_null)   # 54

# Drop nulls
df_survey = df_survey.dropna(subset=['Case'])
agents_to_filter = ['Ethan Ahmed', 'Benjamin Popovich', 'Sophia Belen', 'Elijah Ali', 'Liam Timofey', 'Mateo Marquez']

# Filter agents who have scores lower than 4
filtered_df = df_survey[(df_survey['Agent'].isin(agents_to_filter)) & (df_survey['Agent Satisfaction'] < 4)]

# Group by 'Agent' and calculate total cases with lower score
total_cases_with_lower_score = filtered_df.groupby('Agent')['Case'].size()

# Group by 'Agent' and aggregate cases as a comma-separated string
cases_by_agent_with_lower_score = filtered_df.groupby('Agent')['Case'].agg(lambda x: ', '.join(map(str, x))).reset_index()

# Print the results
print(f"Agent's cases with lower score: \n{cases_by_agent_with_lower_score}")
print(f"Total cases by agent with lower score: \n{total_cases_with_lower_score}")