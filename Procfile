gateway: python3 -m bottle --bind=localhost:$PORT --debug --reload gateway
users: sandman2ctl -p $PORT sqlite+pysqlite:///mockroblog/users.db
timelines: sandman2ctl -p $PORT sqlite+pysqlite:///mockroblog/timelines.db
user-queries: datasette -p $PORT --reload mockroblog/users.db
timeline-queries: datasette -p $PORT --reload mockroblog/timelines.db
direct-messages: python3 -m bottle --bind=localhost:$PORT --debug --reload dm 
search-engine: python3 -m bottle --bind=localhost:$PORT --debug --reload search_engine