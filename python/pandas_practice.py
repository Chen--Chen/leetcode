import pandas as pd, numpy as np

# ##########################
# ######## DataFrame #######
# ##########################


# # Creating DataFrames
# df = pd.DataFrame({"a": [4,5,6],
#                    "b": [7,8,9],
#                    "c": [10,11,12]},
#                    index = [1,2,3]
#                    )


# df = pd.DataFrame(
#     [[4,7,10],
#     [5,8,11],
#     [6,9,12]],
#     # index=[1,2,3],
#     columns = ['a', 'b', 'c'],
# )


# df = pd.DataFrame(
#     {"a": [4,5,6],
#      "b": [7,8,9],
#      "c": [10,11,12]},
#      index = pd.MultiIndex.from_tuples(
#          [('d', 1), ('d',2), ('e',2)],
#          names = ['n','v']
#      )
# )

# # df = (pd.melt(df)
# # .rename(columns={
# # 'variable' : 'var', 
# # 'value' : 'val'}).query('val>11')
# # )
# # print(df)

# df = pd.melt(df)
# df = df.pivot(columns = 'variable', values='value')

# # print(df)



# df = pd.read_csv('C:/Users/cheng/Desktop/leetcode/Kaggle/titanic/test.csv')

# # df.drop_duplicates()
# # df = df.dropna()
# # df.fillna('just_test',inplace=True)

# # df = df.pivot_table(index ='Embarked' , columns = 'Sex', values = 'Fare', aggfunc=np.sum)

# # print(df.loc[df['Age']>50,'Pclass':'Name'])


# df = df.assign(newcolumn=lambda df: df.Age*df.Fare)

# # print(df.head())
# # print(df.min(axis=0))

# print(df.groupby(by = "Sex").quantile([0.25,0.75]))
# df.Age.plot.hist()




# ################################
# ######## Lambda Function #######
# ################################
# # df.apply()
# # lambda


# def custom_rating(genre,rating):
#     if 'Thriller' in genre:
#         return min(10,rating+1)
#     elif 'Comedy' in genre:
#         return max(0,rating-1)
#     else:
#         return rating
        
# df['CustomRating'] = df.apply(lambda x: custom_rating(x['Genre'],x['Rating']),axis=1)

# # df.apply(lambda x: func(x['col1'],x['col2']),axis=1)



# #################################################
# ######## Query in pandas using sql syntax #######
# #################################################

# import pandas as pd
# import pandasql as ps
# import numpy as np

# df = pd.DataFrame([[1234, 'Customer A', '123 Street', np.nan],
#                [1234, 'Customer A', np.nan, '333 Street'],
#                [1233, 'Customer B', '444 Street', '333 Street'],
#               [1233, 'Customer B', '444 Street', '666 Street']], columns=
# ['ID', 'Customer', 'Billing Address', 'Shipping Address'])

# q1 = """SELECT ID FROM df """

# print(ps.sqldf(q1, locals()))




# data = {'col_1': [3,2,1,0], 'col_2': ['a','b','c','d']}
# data_df = pd.DataFrame.from_dict(data, orient='index', columns=['A','B','C','D'])
# print(data_df)



# sales = [{'account':'Jones LLC', 'Jan':150,  'Feb':200,  'Mar': 140 },
#          {'account':'Alpha Co', 'Jan':200,  'Feb':210,  'Mar': 215},
#          {'account':'Blue Inc', 'Jan':50,  'Feb':90,  'Mar': 95}
# ]

# df = pd.DataFrame(sales)

# print(df)


# sales = {'account': ['Jones LLC', 'Alpha Co','Blue Inc' ],
#          'Jan': [150, 200, 50],
#          'Feb': [200, 210, 90],
#          'Mar': [140, 215, 95]}

# df = pd.DataFrame.from_dict(sales)

# sales = [('Jones LLC', 150, 200, 50),
#          ('Alpha Co', 200, 210, 90),
#          ('Blue Inc', 140, 215, 95)]

# labels = ['account', 'Jan', 'Feb', 'Mar']
# df = pd.DataFrame.from_records(sales, columns = labels)
# print(df)

# sales = [('account', ['Jones LLC', 'Alpha Co','Blue Inc' ]),
#          ('Jan', [150, 200, 50]),
#          ('Feb', [200, 210, 90]),
#          ('Mar', [140, 215, 95])]
# df = pd.DataFrame.from_items(sales)


x = np.random.randn(5)
y = np.sin(x)

print(x)
print(y)


df = pd.DataFrame({'X': x})
df['Y'] = pd.Series(y)
print(df, type(df))


df = pd.DataFrame({'a': ['red', 'yellow', 'blue'], 'b': [0.5, 0.25, 0.125]})
print(df)



print(df.to_dict('dict'))
