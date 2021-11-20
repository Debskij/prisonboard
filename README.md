# prisonboard
Job board for prisoners


## Rebuild container:
docker-compose -d --build
docker-compose up

## Setting up database:
docker-compose exec web flask shell

### In shell

from app import db

db.drop_all()
db.create_all()
db.session.commit()

### Creating object instance:

db.session.add(User(email='abc@example.com'))
db.session.commit()
