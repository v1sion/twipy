import os
import string
import random
from app import create_app, db
from app.models import User, Post

app = create_app()


def dummy_password(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))


def seed_db():
    user1 = User(email='willis.adams@example.com', name='Willis Adams', about_me='Creator or Twipy app',
                 active=True)
    user1.set_password(dummy_password())
    db.session.add(user1)
    db.session.commit()
    app.logger.info('User {user} created with email {email}'.format(user=user1.name, email=user1.email))
    user2 = User(email='conan.gray@example.com', name='Conan Gray', about_me='Curiosity Killed The Cat', active=True)
    user2.set_password(dummy_password())
    db.session.add(user2)
    user2.follow(user1)
    db.session.commit()
    app.logger.info('User {user} created with email {email}'.format(user=user2.name, email=user2.email))
    user3 = User(email='justion.sedillo@example.com', name='Justin Sedillo', about_me='Head Over Heels',
                 active=True)
    user3.set_password(dummy_password())
    db.session.add(user3)
    user3.follow(user1)
    db.session.commit()
    app.logger.info('User {user} created with email {email}'.format(user=user3.name, email=user3.email))

    user4 = User(email='john.snake@example.com', name='John Snake', about_me='The sky is blue',
                 active=True)
    user4.set_password(dummy_password())
    db.session.add(user4)
    user4.follow(user1)
    db.session.commit()
    app.logger.info('User {user} created with email {email}'.format(user=user4.name, email=user4.email))

    post1 = Post(body='Not the Sharpest Tool in the Shed', author=user1, private=False)
    db.session.add(post1)
    db.session.commit()

    post2 = Post(body='What Goes Up Must Come Down', author=user2, private=False)
    db.session.add(post2)
    db.session.commit()

    post3 = Post(body=os.environ.get('PRIVATE_POST'), author=user1, private=True)
    db.session.add(post3)
    db.session.commit()

    post4 = Post(body='Ride Him, Cowboy!', author=user3, private=True)
    db.session.add(post4)
    db.session.commit()

    post5 = Post(body='If You Can\'t Stand the Heat, Get Out of the Kitchen', author=user4, private=False)
    db.session.add(post5)
    db.session.commit()


@app.cli.command('seed')
def initdb_command():
    """Initializes the database."""
    seed_db()
    print('Initialized the database.')


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
