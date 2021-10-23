Welcome to this dbt project!

### About this project

This project is a transformation pipeline for answering two questions in an easy and performant way
1. Number of pageviews, on a given time period (hour, day, month, etc), per postcode - based on the current/most recent postcode of a user.
2. Number of pageviews, on a given time period (hour, day, month, etc), per postcode - based on the postcode a user was in at the time when that user made a pageview.

### Running this project

As this is a demo project you'll first need to load the data into Snowflake from the data folder.
- You can directly load the data into Snowflake with the Snowflake Python Connector using the load scripts in the scripts folder.

For this project to work properly you'll need to have an environment running dbt and Airflow.
- Check out [the dbt docs](https://docs.getdbt.com/dbt-cli/installation) and [Airflow docs](https://airflow.apache.org/docs/apache-airflow/stable/installation.html) for installation instructions
- Also check out [how to run dbt using the cli](https://docs.getdbt.com/docs/running-a-dbt-project/using-the-cli) if you're planing on not using the dbt Cloud IDE.
- Keep in mind that by default, dbt expects your profiles.yml file to be located in the ~/.dbt/ directory. Since the profile for this project is in the profiles folder you'll either need to move it to the default folder or [direct dbt there in other ways](https://docs.getdbt.com/dbt-cli/configure-your-profile#using-a-custom-profile-directory)

In the scripts folder you'll also find an Airflow script for scheduling the Transform pipeline.
- Consists of 2 DAGs, a daily one and an hourly one to keep the models as fresh as practical.
- This project assumes you have an Airflow environment somewhere else and therefore only provides the DAGs.

### Any questions?:
Contact me (Alexander) at post@alexanderfridriksson.com