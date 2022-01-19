# Smart Watch IoT Server

This is an application that acquires your heart rate with a smartwatch, and recommends and plays back the appropriate BPM according to your heart rate.

The colored servers in the figure below are constructed.
The URLs of each repository are as follows.

- **(This repository) AWS server** (https://github.com/ITK13201/smart-watch-iot-server)
- Raspberry Pi IoT Server (https://github.com/ITK13201/smart-watch-iot-client)
- Raspberry Pi Discord Server (https://github.com/ITK13201/smart-watch-iot-interactive-server)

![system_chart](./docs/img/system_chart.png)

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
