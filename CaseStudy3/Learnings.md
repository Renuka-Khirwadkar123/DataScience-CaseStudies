1. First thing I understood is how to explore the dataset properly — like checking df.info(), describe(), and looking at the shape, nulls, and duplicates. Earlier I used to just jump to charts, but now I know proper EDA steps matter.

2. I faced some duplicate rows, and for the first time I understood how to check if Order ID is also repeated, not just rows. So I learned that just removing duplicates is not enough, we have to see how it affects business data.

3. Date cleaning was tricky. I learned how to convert strings to datetime using pd.to_datetime(), and how to extract year, month, etc. I also learned how to compare Order ID year and Order Date year — earlier I didn’t even think this was important.

4. I tried imputing missing values logically — for example, I created a Days to Ship column and then filled missing Ship Mode based on that. This was the first time I used actual logic instead of just filling with average or mode.

5. For PII, I dropped the Customer Name column and masked it using initials. I understood the importance of this in real-world projects — even if it looks like a small thing, it matters a lot for privacy.

6. Formatting Postal Code using .str.zfill(5) was new for me. I also had to make sure numeric columns like Quantity and Sales were in the right format (int or float). Before this, I used to ignore datatypes.

7. I grouped by Customer ID to get total sales and profit, and then created quintiles using pd.qcut(). This helped me learn customer segmentation and how to classify customers into top 20%, bottom 20%, etc.

8. Lastly, I created a crosstab of Sales vs Profit quintiles. This was helpful to see which customers are high in both or only in one. It made me think more analytically, not just technically.


Tech stack used:

1. Python
2. Numpy
3. Pandas
4. Seaborn
5. Pandas
6. Matplotlib
7. Jupyter notebook in visual studio code.

