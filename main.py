import json
import time
import pandas as pd
import sqlalchemy
from pathlib import Path
from database import create_db, insert_on_conflict_update

# Create SQLAlchemy engine
engine = sqlalchemy.create_engine('postgresql+psycopg2://llrbrhis:oH2Uau1jYZ3pgwUVEveYsyPxa5pVeWs3@trumpet.db.elephantsql.com/llrbrhis')


def read_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def insert_data(df, table_name):
    print(f'Inserting data into: {table_name}')
    df.to_sql(table_name, engine, if_exists='append', index=False, method=insert_on_conflict_update)


def process_new_files():
    objects_detection_file = Path('input/objects_detection.json')
    vehicle_status_file = Path('input/vehicles_status.json')

    if objects_detection_file.exists():
        print(f'Working on Object detection')
        detection_data = read_file(objects_detection_file)['objects_detection_events']
        df_detection = pd.json_normalize(detection_data, meta=['vehicle_id', 'detection_time'], record_path='detections')
        df_detection['detection_time'] = pd.to_datetime(df_detection['detection_time'])
        insert_data(df_detection, 'objects_detection_table')
        print(f'Removing file: {objects_detection_file}')
        objects_detection_file.unlink()

    if vehicle_status_file.exists():
        print(f'Working on Vehicle Status')
        status_data = read_file(vehicle_status_file)['vehicle_status']
        df_status = pd.DataFrame.from_dict(status_data)
        df_status['report_time'] = pd.to_datetime(df_status['report_time'])
        insert_data(df_status, 'vehicle_status_table')
        print(f'Removing file: {vehicle_status_file}')
        vehicle_status_file.unlink()


if __name__ == "__main__":
    try:
        while True:
            create_db()
            process_new_files()
            print(f'Finished processing, sleeping for 60 seconds')
            time.sleep(60)
    except KeyboardInterrupt:
        pass
    finally:
        engine.dispose()
