version: '3'
services:
  management:
      image: registry.alpaca.io/alpaca_management:{{ tag }}
      environment:
        DATABASE_HOST: {{ key "production/config/consul/database_host" }}
        DATABASE_PORT: {{ key "production/config/consul/database_port" }}
        DATABASE_NAME: {{ key "production/config/consul/database_name" }}
        DATABASE_USER: {{ key "production/config/consul/database_user" }}
        DATABASE_PASSWORD: {{ key "production/config/consul/database_password" }}
        DATABASE_SERVER_USER: {{ key "production/config/consul/database_server_user" }}
        DATABASE_SERVER_PASSWORD: {{ key "production/config/consul/database_server_password" }}
        REDIS_HOST: {{ key "production/config/consul/redis_host" }}
        REDIS_PORT: {{ key "production/config/consul/redis_port" }}
        ENVIRONMENT: {{ key "production/config/consul/environment" }}
        ALPACA_USERS_HOST: {{ key "production/config/consul/alpaca_users_host" }}
        ALPACA_USERS_PORT: {{ key "production/config/consul/alpaca_users_port" }}
        CREATIVES_HOST: {{ key "production/config/consul/creatives_host" }}
        CREATIVES_PORT: {{ key "production/config/consul/creatives_port" }}
        ADNETWORKS_HOST: {{ key "production/config/consul/adnetworks_host" }}
        ADNETWORKS_PORT: {{ key "production/config/consul/adnetworks_port" }}
        SQLALCHEMY_MIGRATE: {{ key "production/config/consul/sqlalchemy_migrate" }}
      ports:
        - "8082:80"
