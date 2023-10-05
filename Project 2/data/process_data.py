import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    '''
    load_data
    Load data from file csv using pandas and merge them into one.
    INPUT:
    messages_filepath: Data messages.
    categories_filepath: Data categories type.
    RETURN:
    df_merge: DF merged messages and categories.   
    '''
    # Read file
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    # InnerJoin two DataFrame
    df_merge = messages.merge(categories, on = ['id'])
    return df_merge


def clean_data(df):
    '''
    clean_data:
    Analyze, process, transform, and clean data, before saving to DB.
    INPUT:
    df: DF merged messages and categories.
    RETURN:
    df_clean: Data is cleaned.
    '''
    # Create a data frame that has 36 columns corresponding to 36 category types.
    categories = df['categories'].str.split(';', expand=True)
    
    # Get first record
    row = categories.iloc[0]
    
    # Name column start from (index 0 -> indexMax - 2) of String
    # Rename column DF categories
    category_colnames = row.transform(lambda x: x[:-2]).tolist()
    categories.columns = category_colnames
    
    for column in categories:
        # Set lastIndex String is stored value.
        categories[column] = categories[column].transform(lambda x: x[-1:])

        # convert type string -> numeric
        categories[column] = pd.to_numeric(categories[column])
        
        # Replace value 2 -> 1 column related.
        categories['related'] = categories['related'].replace(to_replace=2, value=1)
        
    # Drop column in DF
    df = df.drop('categories', axis=1)
        
    # concatenating the original DF with DF categories
    df = pd.concat([df, categories], axis=1)
        
    # removing duplicates
    df_clean = df.drop_duplicates(keep='first')
    return df_clean
    
    
def save_data(df, database_filename):
    '''
    save_data:
    Data saving
    INPUT:
    df: Data is cleaned.
    database_filename: FileName stored.
    '''
    # Create DB
    engine = create_engine('sqlite:///'+ str(database_filename))
    # Stored Data 
    df.to_sql("disaster_response_data", engine, index=False,if_exists='replace')
    pass


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
