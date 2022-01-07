# Smart Watch IoT Server

## Install

- docker
- docker-compose

## Setup

### 1. Clone

```shell
git clone git@github.com:ITK13201/smart-watch-iot-server.git
cd smart-watch-iot-server
```

### 2. Init environments

```shell
./scripts/environment/init.sh
```

### 3. Build

```shell
docker-compose build
```

## Usage

### Start container

```bash
docker-compose up -d
```

### Stop container

```bash
docker-compose down
```

### Logging

```bash
docker-compose logs -f
```

### Migrate

```bash
docker-compose exec app python manage.py migrate
```

### Create superuser

```bash
docker-compose exec app python manage.py createsuperuser
```
