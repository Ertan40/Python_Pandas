"""
17. Write a Pandas program to split a given dataframe into groups and create a new column with count from GroupBy.
Test Data:

  book_name book_type  book_id
0     Book1      Math        1
1     Book2   Physics        2
2     Book3  Computer        3
3     Book4   Science        4
4     Book1      Math        1
5     Book2   Physics        2
6     Book3  Computer        3
7     Book5   English        5
"""

import pandas as pd

pd.set_option('display.max_rows', None)

data = {'book_name': ['Book1', 'Book2', 'Book3', 'Book4', 'Book1', 'Book2', 'Book3', 'Book5'],
        'book_type': ['Math', 'Physics', 'Computer', 'Science', 'Math', 'Physics', 'Computer', 'English'],
        'book_id': [1, 2, 3, 4, 1, 2, 3, 5]}

df = pd.DataFrame(data=data)

print("Original DataFrame:")
print(df)

print("\nNew column with count from groupby:")
result = df.groupby(['book_name', 'book_type'])['book_type'].count().reset_index(name='count')
print(result)

# Output:
# Original DataFrame:
#   book_name book_type  book_id
# 0     Book1      Math        1
# 1     Book2   Physics        2
# 2     Book3  Computer        3
# 3     Book4   Science        4
# 4     Book1      Math        1
# 5     Book2   Physics        2
# 6     Book3  Computer        3
# 7     Book5   English        5
#
# New column with count from groupby:
#   book_name book_type  count
# 0     Book1      Math      2
# 1     Book2   Physics      2
# 2     Book3  Computer      2
# 3     Book4   Science      1
# 4     Book5   English      1
