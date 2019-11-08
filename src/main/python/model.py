# Required imports
from sqlalchemy import create_engine, Table, Column, String, MetaData, inspect
import pandas as pd
import logging, settings
from sqlalchemy.orm import sessionmaker

# Setting logger to use current filename
logger = logging.getLogger(__name__)

# Creating a global variable for Database Engine
DB_ENGINE = None


# Function to create Database Engine (connection)
def fetch_db_engine():
    """
    This function fetches the Database connection and 
    sets it to the Global variable for further use
    """
    global DB_ENGINE
    if DB_ENGINE == None :
        #connecting to database
        engine = create_engine(settings.DB_LOCATION)
        engine.connect()
        DB_ENGINE = engine


def create_table_job_postings():
    """
    This function creates the table 'job_postings'
    """
    logger.debug('Executing method create_table_job_postings()')
    fetch_db_engine()
    meta = MetaData(DB_ENGINE)  
    job_postings = Table('job_postings', meta,
  					   Column('index', String),	
                       Column('organization', String),
                       Column('Industry', String),
                       Column('City/State', String),
                       Column('postedby', String),
                       Column('title', String),
                       Column('description', String),
                       Column('experience', String),
                       Column('Exp-Category', String),
                       Column('skill', String),
                       Column('salary', String),
                       Column('Approx_Date', String))

    logger.debug("calling create_all()")
    
    DBSession = sessionmaker(bind=DB_ENGINE)
    session = DBSession()
    meta.create_all(DB_ENGINE)
    session.commit()
    logger.debug('Exiting method create_table_job_postings()')
    

def push_csv_records_to_db(df):
    """
    This function would fetch the records from the dataframe 
    and update them in the database
    @param dataframe object
    @return String ['DB_UPDATE_SUCCESSFUL' | 'DB_UPDATE_FAILED']
    """

    logger.debug('Executing method push_csv_records_to_db()')

    fetch_db_engine()
    inspector = inspect(DB_ENGINE)
    table_names = str(inspector.get_table_names())

    # Get table information
    logger.debug('DB Table Names' + table_names)

    # ------ This code should be deleted as it is expected that 
    # ------ the client would already have this table existing
    # ------ and the code is expected to show an error if the table does'nt exist.
    # --------------- CODE STARTING FROM HERE -------------------------
    if settings.DB_TABLE_NAME not in table_names:
        logger.debug(settings.DB_TABLE_NAME + ' does not table exist')
        logger.debug("Calling create_table_job_postings()")
        create_table_job_postings()

        logger.debug("Checking again if table exists...")
        fetch_db_engine()
        inspector = inspect(DB_ENGINE)
        table_names = str(inspector.get_table_names())
        logger.debug('DB Table Names Again :: ' + table_names)
    # ---------------CODE TILL HERE -- NEEDS TO BE DELETED ------------
        
    if settings.DB_TABLE_NAME in table_names:
        logger.debug(settings.DB_TABLE_NAME + ' table exists')
        try:
            df.to_sql('job_postings', DB_ENGINE, if_exists='append' )
            db_response = 'DB_UPDATE_SUCCESSFUL'
        except:
            logger.exception("Exception occured while trying to append data to the table :: " + settings.DB_TABLE_NAME)
            db_response = 'DB_UPDATE_FAILED'
    else:
        logger.error(settings.DB_TABLE_NAME + " table does not exist in the database.")
        db_response = 'DB_UPDATE_FAILED'

    logger.debug('Exiting method push_csv_records_to_db()')
    
    return db_response

