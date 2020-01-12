CREATE DATABASE dnd_server;
CREATE USER dndadmin WITH PASSWORD '123qweASD';
ALTER ROLE dndadmin SET client_encoding TO 'utf8';
ALTER ROLE dndadmin SET default_transaction_isolation TO 'read committed';
ALTER ROLE dndadmin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE dnd_server TO dndadmin;