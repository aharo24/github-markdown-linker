

# Postgre CLI startup 

```sql
-- Create the database
CREATE DATABASE twitterdb;
```

```sql
-- Create the user with a password
CREATE USER twitter_user WITH PASSWORD 'toor';
```

```sql
-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON DATABASE twitterdb TO twitter_user;
```

