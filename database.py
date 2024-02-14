import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql

engine = sa.create_engine('postgresql+psycopg2://llrbrhis:oH2Uau1jYZ3pgwUVEveYsyPxa5pVeWs3@trumpet.db.elephantsql.com/llrbrhis')

Base = declarative_base()


def insert_on_conflict_update(table, conn, keys, data_iter):
    tbl = sa.Table(table.name, sa.MetaData(), schema=table.schema, autoload_with=engine)
    data = [dict(zip(keys, row)) for row in data_iter]
    insert_stmt = postgresql.insert(tbl).values(data)
    update_stmt = {exc_k.key: exc_k for exc_k in insert_stmt.excluded}
    upsert_stmt = insert_stmt.on_conflict_do_update(
        index_elements=tbl.primary_key.columns,
        set_=update_stmt
    )
    conn.execute(upsert_stmt)


# Define objects detection table
class ObjectsDetection(Base):
    __tablename__ = 'objects_detection_table'

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(String)
    detection_time = Column(DateTime)
    object_type = Column(String)
    object_value = Column(Integer)


# Define vehicle status table
class VehicleStatus(Base):
    __tablename__ = 'vehicle_status_table'

    vehicle_id = Column(String, primary_key=True)
    report_time = Column(DateTime)
    status = Column(String)


def create_db():
    Base.metadata.create_all(engine)

    # Close the engine
    engine.dispose()
