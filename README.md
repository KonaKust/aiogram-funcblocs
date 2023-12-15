# aiogram-funcblocs-template
## Requirements
You need to install and configure:
### MySQL / MariaDB
Database with a “users” table, including the columns “id”, “user_id”, “first_name”, “last_name”, “registration_time” and “admin”. This data is used for user registration and administrator authorization

### Redis
In-memory data store for throttling middleware
The only thing that needs to be configured is **supervised systemd** in _/etc/redis/redis.conf_
Optional setting is **maxmemory 200mb** or any other size

### PIP dependencies
`pip3 install -r requirements.txt`
