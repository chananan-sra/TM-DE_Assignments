- Why default group is appear?
- Can't use EnvVar
- Dagster import path is invalid

# Answer

### If the data is to be ingested periodically, what changes will you make to your current approach?
- Create job and schedule to trigger periodically.
- Or create sensors to check if there's files at the source location. Ingest it and remove or back-up the file 


### Draw a data architecture showing different components of your ETL process.
    diagram here

### How will you verify the correctness of the ingested data?
- Manually count using PostgreSQL to see if there's equal numbers of input and output
- Create a unit test to check data type, datetime format.

# Overview

## Purpose

This pipeline's goal is to clean and extract daily checkin data into PostgreSQL database.
## Scope


## High-Level Architecture

## Key Components

# Diagram
