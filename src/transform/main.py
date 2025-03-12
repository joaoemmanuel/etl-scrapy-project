import pandas as pd
import sqlite3
from datetime import datetime

# Inserting the jsonl content into df variable
df = pd.read_json('../../data/data.jsonl', lines=True)

# Setting all columns to visible in pandas
pd.options.display.max_columns = None

# Creating two new columns, source and date of collection, respectively
df['_source'] = 'https://lista.mercadolivre.com.br/tenis-corrida-masculino'
df['_collection_date'] = datetime.now()

# Transforming null values to 0 and converting values to float
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_cents'] = df['old_price_cents'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_cents'] = df['new_price_cents'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

# Removing parentheses from data and converting values to int
df['reviews_amount'] = df['reviews_amount'].str.replace(r'[\(\)]', '', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

# Transform and join the full values with cents and insert the values in new columns
df['old_price'] = df['old_price_reais'] + (df['old_price_cents'] / 100)
df['new_price'] = df['new_price_reais'] + (df['new_price_cents'] / 100)

# Remove old price related columns
df.drop(columns=['old_price_reais', 'old_price_cents', 'new_price_reais', 'new_price_cents'], inplace=True)

# Connecting to SQLite database
conn = sqlite3.connect('../../data/mercadolivre.db')

# Saving dataframe to SQLite database
df.to_sql('mercadolivre_products', conn, if_exists='replace', index=False)

# Closing connection to database
conn.close()