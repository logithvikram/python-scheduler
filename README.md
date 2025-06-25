# APScheduler Demo

This repository demonstrates using [APScheduler](https://apscheduler.readthedocs.io/) with a PostgreSQL database for job storage and logging job outputs using SQLAlchemy.

## Features

- Schedules a recurring job every 10 seconds.
- Stores job execution timestamps in a PostgreSQL database.
- Uses SQLAlchemy for database interactions.
- Docker Compose setup for PostgreSQL.

## Requirements

- Python 3.8+
- Docker & Docker Compose

## Setup

1. **Clone the repository**

   ```sh
   git clone <repo-url>
   cd apscheduler
   ```

2. **Start PostgreSQL using Docker Compose**

   ```sh
   docker-compose up -d
   ```

3. **Install Python dependencies**

   ```sh
   pip install apscheduler sqlalchemy psycopg2-binary
   ```

4. **Run the scheduler**

   ```sh
   python scheduler_demo.py
   ```

## Configuration

- The database connection string can be set via the `DATABASE_URL` environment variable.
- By default, it connects to:  
  `postgresql+psycopg2://scheduler:scheduler_pass@localhost:5433/scheduler_db`

## Stopping

- To stop the scheduler, press `Ctrl+C`.
- To stop and remove the database container:

  ```sh
  docker-compose down
  ```

## License

MIT License.
