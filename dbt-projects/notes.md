# Notes

## Postgres / Docker

0. Create the container: `docker run -it -v /Users/mvd/Documents/Repositories/data-science-projects/dbt-projects/atp_tour:/dbt-projects --name postgres-20230110 -e POSTGRES_USER=mdemko -e POSTGRES_PASSWORD=IwQoajaEqC -p 5432:5432 -d postgres`
0. Run bash on the container: `docker exec -it 9f3201380905f375e14b538c182d12c0c87b5cafcaf5162dbd3fa9cc39b75efd bash`
0. Start psql on the container: `psql -h localhost -p 5432 -U mdemko -W`
0. Create schema named for user as dev output: `CREATE SCHEMA AUTHORIZATION mdemko;`
0. Install curl `apt update` and `apt install curl`
0. Install conda following instructions for Debian here https://docs.conda.io/projects/conda/en/latest/user-guide/install/rpm-debian.html
0. Create the environment `conda env create -f environment.yml`
