#!/usr/bin/env python
# coding: utf-8

# #### Задание 1
# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
# [1, 1, 1, 2, 2, 3, 3],
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].

# In[130]:


import pandas as pd

data = {'author_id':[1, 2, 3], 'author_name':['Тургенев', 'Чехов', 'Островский']}
authors = pd.DataFrame(data)
authors


# In[131]:


data_books ={'author_id':[1, 1, 1, 2, 2, 3, 3], 
             'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 
                            'Гроза', 'Таланты и поклонники'], 
             'price':[450, 300, 350, 500, 450, 370, 290]}
book = pd.DataFrame(data_books)
book


# #### Задание 2
# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

# In[132]:


authors_price = pd.merge(authors, book, how ='outer', on ='author_id')
authors_price


# #### Задание 3
# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

# In[133]:


top5 = authors_price.sort_values(by='price', ascending = False).head(5)
top5


# #### Задание 4
# Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

# In[134]:


authors_stat = pd.DataFrame()

for index, row in authors.iterrows():
    new_row = {'author_name':row['author_name'], 
               'min_price':[round(authors_price.loc[authors_price['author_name'] == row['author_name'], 'price'].min())],
               'max_price':[round(authors_price.loc[authors_price['author_name'] == row['author_name'], 'price'].max())],
               'mean_price': [round(authors_price.loc[authors_price['author_name'] == row['author_name'], 'price'].mean())]}
    authors_stat = authors_stat.append(new_row, ignore_index=True)
authors_stat

