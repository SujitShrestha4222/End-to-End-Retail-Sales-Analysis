import pandas as pd

# Loading dataset from data folder
df = pd. read_csv (r"data/retail_sales_data.csv")
# Confirming dataset loaded successfully
print ("Dataset loaded successfully")





# Storing columns unique value in list to use them in our streamlit file (i.e. app.py)
category_lst = df ["Category"]. unique (). tolist ()
print (category_lst)

region_lst = df ["Region"]. unique (). tolist ()
print (region_lst)

segment_lst = df ["Segment"]. unique (). tolist ()
print (segment_lst)

shipmode_lst = df ["Ship Mode"]. unique (). tolist ()
print (shipmode_lst)





# This line of code is basically making a dictionary where keys are the each unique categories of our column and sub-category is our values . storing this dictionary in variable called "category_dict"
category_dict = (
    df.groupby("Category")["Sub-Category"]
    .unique()
    .apply(list)
    .to_dict()
)
# where,
# key contains categories
# value contains sub_categories