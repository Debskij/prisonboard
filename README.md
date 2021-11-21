# prisonboard
Job board for prisoners


## Rebuild container:
```
docker-compose -d --build
docker-compose up
```

## Setting up database:
```
docker-compose exec web flask shell
```

### In shell
```python
from app import db, init_db
from app.models import *
init_db()
```
