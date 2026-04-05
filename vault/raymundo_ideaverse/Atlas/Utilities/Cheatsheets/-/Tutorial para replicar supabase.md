---
created: 2025-01-04
---
## How to implement data replication between Supabase and another PostgreSQL database?

### Step 1: Set Up Remote Server Configuration In Supabase

Alright, let's get started with connecting to a remote PostgreSQL database through Supabase. First things first, we need to define the remote server parameters. Here's what you'll need:

- PostgreSQL host: This is the IP address or hostname of your remote server.
- PostgreSQL port: The port where your PostgreSQL service is running.
- PostgreSQL user: Usually, this is 'postgres'.
- PostgreSQL password: The password for your PostgreSQL user.
- PostgreSQL database: The name of your database.

Head over to the Dashboard, then navigate to ‘Settings’ -> ‘Database’ -> ‘Connections’.

### Step 2: Virtual Private Network Connection

Next up, we need to set up a VPN for secure communication between Supabase and your remote PostgreSQL server. You can either go for a full network-level VPN or a client-server VPN on the PostgreSQL server itself. This will create a secure tunnel for your data to travel through.

### Step 3: Set Up Logical Replication On Supabase

Now, let's talk replication. Physical replication copies the entire database cluster, which can be a bit heavy for large databases. Instead, we can use logical replication to selectively copy data changes to specific tables.

To set up logical replication in Supabase, follow these steps:

- Open the dashboard and go to the SQL page.
- Run this SQL command to set up logical replication:
    
    ```sql
    ALTER SYSTEM SET wal_level = logical;
    ```
    
- Restart the PostgreSQL service to apply the changes.

### Step 4: Create a Publication On the Remote PostgreSQL Server

A Publication in PostgreSQL defines which tables should be replicated. Run this SQL command on your remote PostgreSQL server to create a Publication:

```sql
CREATE PUBLICATION my_publication FOR TABLE my_table;
```

Replace 'my_publication' with your chosen name for the Publication, and ‘my_table’ with the name of the table you want to replicate.

### Step 5: Create a Subscription On Supabase

A Subscription links the Supabase database to the remote Publication. Run this SQL command in Supabase to create a Subscription:

```sql
CREATE SUBSCRIPTION my_subscription
CONNECTION 'dbname=my_database host=my_host port=my_port user=my_user password=my_password'
PUBLICATION my_publication;
```

Replace 'my_subscription' with your chosen name for the Subscription, and 'my_database', 'my_host', 'my_port', 'my_user', and 'my_password' with your remote PostgreSQL server details. Also, replace 'my_publication' with the name of the Publication you created earlier.

Supabase will now start replicating data from the remote PostgreSQL database. You can monitor the replication process in the PostgreSQL statistical views or through system logs.

### Note on Potential Pitfalls

- Make sure you have enough disk space before starting the replication, especially with large datasets.
- Ensure the entire replication process is encrypted for data privacy and security.
- Using a private VPN connection between Supabase and the remote PostgreSQL database is highly recommended.
- If you run into performance issues during replication, consider increasing network bandwidth, hardware configuration, or the PostgreSQL shared_buffers parameter.

Following these steps, you can set up data replication between Supabase and another PostgreSQL database. This setup is particularly useful for teams working on data science and analytics applications that need reliable, secure, and real-time access to production data.