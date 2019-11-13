LOGIN_CREDENTIALS = { 'user123':'password123', 'userXYZ':'passwordXYZ', 'u1':'p1', 'uu':'pp'}

DB_NAME = "db_csv_uploader"
DB_LOCATION = "postgresql://pguser:pgpassword@localhost:5432/" + DB_NAME
DB_TABLE_NAME = "job_postings"

COLUMNS_LIST = ['organization', 'Industry', 'City/State', 'postedby', 'title', 'description', 'experience', 'Exp-Category', 'skill', 'salary', 'Approx_Date']