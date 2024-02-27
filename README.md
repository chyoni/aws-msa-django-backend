# Virtual Environment

### Create Virtual Environment

```bash
# path: your django project path
python3 -m venv ./
```

### Run Virtual Environment

```bash
source ./bin/activate
```

### Exit Virtual Environment

```bash
deactivate
```

# Dependencies install

### Create requirements.txt

```bash
pip freeze --all > requirements.txt
```

### Install dependencies via requirements.txt
```bash
pip install -r requirements.txt
```

# Migration

```bash
1. Go to backend-server Container 
2. python manage.py makemigrations
3. python manage.py migrate
```

# RabbitMQ

### Required
- Create file this path: ./config/constants.py
- add this line:
```bash
RABBITMQ_URL="Your CloudAMQP Instance URL"
```