Report of the EDA on datasets

1. Data Loading & Initial Exploration
Loaded the dataset (SuperStore_Dataset.csv) using Pandas.

Displayed the first and last 10 rows to get a sense of the data.

Inspected:

Data types

Summary statistics (describe())

Unique values in each column

General info (df.info())

Checked for:

Missing values

Duplicate rows

Dataset shape (rows × columns)

Column names

2. Duplicate Handling
Identified duplicate rows in the dataset using df.duplicated().

Removed those duplicates using df.drop_duplicates().

Reported how many rows were removed and how many Order IDs were affected.

3. PII Removal
To protect Personal Identifiable Information (PII):

Dropped the Customer Name column entirely.

Created a new column Customer Name Masked using only the initials of customer names before dropping the original.

Challenges faced:

1. Keyerror and column issue:

I faced multiple keyerror issues during the process. Sometimes the column was not created yet, or there were small issues like extra spaces or wrong naming. I had to keep checking df.column again and again to figure out what was wrong.

New Libraries I wasn't familiar with:

I explored some new libraries like Geopandas and mapping tools which I hadn’t used before. I had to search a lot of documentation and try multiple times to understand how they work.

Date Format Issues:

Date comparison was confusing. For example, I wanted to compare the year in Order date  with the year in Order id. But Order date was in string format sometimes, so it was giving errors. I had to use pd.to_datetime() and format it properly before doing any comparison.

Formatting and Type Conversion:

I had to format Postal Code as 5-digit strings using .str.zfill(5). Some values were missing or in wrong format, so I had to be careful during conversion. Also, I had to convert date columns to datetime type, otherwise other parts were failing.

Masking Customer Name:

While dropping Customer Name for privacy reasons, I created a masked column with just the initials. I had to make sure it worked for all types of names without error.

Quintile Segmentation:

Using pd.qcut() gave issues when the values had too many duplicates or not enough unique values. I got errors about bin edges. I had to explore why it was failing and how to fix it.




