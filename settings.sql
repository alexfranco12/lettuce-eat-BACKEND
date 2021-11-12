-- settings.sql
CREATE DATABASE lettuceeat;
CREATE USER lettuceeatuser WITH PASSWORD 'lettuce';
GRANT ALL PRIVILEGES ON DATABASE lettuceeat TO lettuceeatuser;