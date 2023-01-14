- Create virtual environment and install required libraries
```bash
 python3 -m venv venv
 source venv/bin/activate
 pip install psycopg2-binary==2.9.3
 pip install -r requirements.txt
```


docker build -t 6_back .
docker run --rm -d -p 8000:8000 --name back 6_back

- Testing if the backend is working
```bash
curl localhost:8000/test
```

- Stop our container
```bash
docker stop back
```
