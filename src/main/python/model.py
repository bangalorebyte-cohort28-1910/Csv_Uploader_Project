from sqlalchemy import create_engine

# engine = create_engine('postgresql+psycopg2://postgres:gudluk1234@localhost/xlsUploader')

# connection = engine.connect()

# print(engine.table_names())

def push_csv_records_to_db():
    """
    This function would fetch the records from the dataframe 
    and update them in the database
    @param dataframe object
    @return String ['DB_UPDATE_SUCCESSFUL' | 'DB_UPDATE_FAILED']
    """
    
    pass