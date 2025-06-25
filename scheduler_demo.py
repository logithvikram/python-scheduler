from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import os
import sys

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://scheduler:scheduler_pass@localhost:5433/scheduler_db"
)

# Setup SQLAlchemy DB connection with error handling
try:
    engine = create_engine(DATABASE_URL)
    metadata = MetaData()
    # Define a simple table to store job outputs
    jobs_table = Table(
        'job_outputs', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('timestamp', String, nullable=False),
    )
    # Create table if not exists
    metadata.create_all(engine)
except Exception as e:
    print(f"Database connection/setup failed: {e}")
    sys.exit(1)


def scheduled_task():
    timestamp = datetime.utcnow().isoformat()
    print(f"Task running at {timestamp}")

    with engine.connect() as conn:
        conn.execute(jobs_table.insert().values(timestamp=timestamp))
        conn.commit()

# Configure APScheduler with SQLAlchemy job store
scheduler = BlockingScheduler(jobstores={
    'default': {
        'type': 'sqlalchemy',
        'url': DATABASE_URL
    }
})

scheduler.add_job(scheduled_task, 'interval', seconds=10, id='db_insert_job')

try:
    print("Starting scheduler...")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    print("Scheduler stopped.")
