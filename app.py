import psycopg2
import pandas as pd

from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker


def read_csv(filename):
    """
        Receives a filename.
        Returns a DataFrame
    """
    df = pd.read_csv(filename)
    return df

def read_db(engine):
    result_set = engine.execute('SELECT * FROM pf."TelecomUsers"')  
    return result_set

def write_db(df,table_name,schema,engine):
    """ 
        Receives a dataframe.
        Insert dataframe into DB
    """
    print("Writing dataframe to PostgreSQL")
    df.to_sql(name=table_name, con=engine, schema = schema, if_exists='replace')
    print("End Writing")

def connect(conn):
    engine = create_engine(conn)
    return engine

if __name__ == '__main__':
    
    db_string = 'postgresql://ftovar:secret@localhost:5432/DataScienceDB'
    table_name = 'TelecomUsers'
    schema = 'pf'

    engine = connect(db_string)

    filename = 'telecom_users.csv'
    data = read_csv(filename)
    print(data)

    write_db(data,table_name,schema,engine)

    result = read_db(engine)
    df = pd.DataFrame(result)
    print(df)


#ftovar@franco-ubuntu:~/docker/pgdev$ sudo apt-get install libpq-dev python-dev
#pip install psycopg2
#pip install SQLAlchemy