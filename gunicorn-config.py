import os

NUM_CORES = os.cpu_count()
NUM_WORKERS = NUM_CORES * 2 + 1
NUM_THREADS = NUM_WORKERS * 2


workers = int(os.environ.get('GUNICORN_PROCESSES', str(NUM_WORKERS)))

threads = int(os.environ.get('GUNICORN_THREADS', str(NUM_THREADS)))

# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))

bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8000')



forwarded_allow_ips = '*'

secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
