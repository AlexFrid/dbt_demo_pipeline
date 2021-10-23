from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import datetime

DBT_PROJECT_DIR = '../dbt'
DBT_PROFILE_DIR = '../dbt/profiles'

default_args = {
    "owner": "Alexander_Fridriksson",
    "depends_on_past": False,
    "start_date": datetime(2021, 8, 23),
    "email": ["post@alexanderfridriksson.com"],
    "email_on_failure": True
    }

# Runs daily at 2 am to catch user data that is updated in snowflake around midnight each day
with DAG(dag_id='dbt_daily_run', default_args=default_args, schedule_interval='0 2 * * *') as dag:

    dbt_snapshot = BashOperator(
        task_id="dbt_snapshot",
        bash_command=f"dbt snapshot --profiles-dir {DBT_PROFILE_DIR} --project-dir {DBT_PROJECT_DIR}"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"dbt run --exclude stg_pageviews fct_pageviews fct_pageviews_count_current_postcode fct_pageviews_count_historic_postcode --profiles-dir {DBT_PROFILE_DIR} --project-dir {DBT_PROJECT_DIR}"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"dbt test --exclude stg_pageviews fct_pageviews fct_pageviews_count_current_postcode fct_pageviews_count_historic_postcode --profiles-dir {DBT_PROFILE_DIR} --project-dir {DBT_PROJECT_DIR}"
    )

    dbt_docs = BashOperator(
        task_id="dbt_docs",
        bash_command=f"dbt docs generate --profiles-dir {DBT_PROFILE_DIR} --project-dir {DBT_PROJECT_DIR}"
    )

    dbt_snapshot >> dbt_run >> dbt_test >> dbt_docs


# Runs every hour at 30 minutes to catch pageview data that is updated in snowflake every hour
with DAG(dag_id='dbt_hourly_run', default_args=default_args, schedule_interval='30 * * * *') as dag:


    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"dbt run --models stg_pageviews fct_pageviews fct_pageviews_count_current_postcode fct_pageviews_count_historic_postcode --profiles-dir {DBT_PROJECT_DIR} --project-dir {DBT_PROJECT_DIR}"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"dbt test --models stg_pageviews fct_pageviews fct_pageviews_count_current_postcode fct_pageviews_count_historic_postcode --profiles-dir {DBT_PROJECT_DIR} --project-dir {DBT_PROJECT_DIR}"
    )

    dbt_run >> dbt_test