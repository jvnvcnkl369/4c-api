﻿# 4create-task

## Running the app locally
create .env file with required parameters(.env.example)

run migrations
``` alembic upgrade head```

run seeeder 
``` python seeder.py ```

run server 
```python server.py```

## Run with docker

create .env file with required parameters(.env.example)

``` docker compose up```
# run tests 
```pytest ./tests```

