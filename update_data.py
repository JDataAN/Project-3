import schedule
import time
import pandas as pd
from sqlalchemy import create_engine

def update_state_data():
    # Load the data from the CSV file into a DataFrame
    state_data_df = pd.read_csv('StateDatabySeason63_49,48,62.csv')

    # Save the cleaned data to a new CSV file
    state_data_df.to_csv('Cleaned_StateDatabySeason63_49,48,62.csv', index=False)

    # Load the cleaned data into the database
    engine = create_engine('sqlite:///state_data.db')
    state_data_df.to_sql('state_data', engine, if_exists='replace', index=False)

# Schedule the data update tasks
schedule.every().day.at("01:00").do(update_state_data)

while True:
    schedule.run_pending()
    time.sleep(1)
