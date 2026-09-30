# Dockerising a Java application with MySQL

Consolidated from the historical `in-few-steps` repository and updated to emphasise separate application/database containers.

## Java application image

```dockerfile
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY build/libs/app.jar /app/app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
```

Build it with:

```bash
docker build -t example-java-app .
```

## Compose with MySQL

```yaml
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      DB_HOST: db
      DB_PORT: 3306
      DB_NAME: app
      DB_USER: app
      DB_PASSWORD: ${DB_PASSWORD}
    depends_on:
      - db

  db:
    image: mysql:8.4
    environment:
      MYSQL_DATABASE: app
      MYSQL_USER: app
      MYSQL_PASSWORD: ${DB_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
    volumes:
      - mysql-data:/var/lib/mysql

volumes:
  mysql-data:
```

Keep secrets outside the compose file, use health checks for production-style orchestration, and run schema migrations explicitly rather than relying on container start order alone.
