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