import random
from app.database import SessionLocal
from app.models import models
from app.main import app


users_data = [
    {"username": "john_doe", "email": "john@example.com"},
    {"username": "jane_smith", "email": "jane@example.com"},
    {"username": "bob_johnson", "email": "bob@example.com"},
]

posts_data = [
    {
        "title": "First Post",
        "content": "This is the content of the first post.",
        "status": "published",
    },
    {
        "title": "Second Post",
        "content": "This is the content of the second post.",
        "status": "draft",
    },
    {
        "title": "Third Post",
        "content": "This is the content of the third post.",
        "status": "published",
    },
]

comments_data = [
    "Great post!",
    "I disagree with this.",
    "Thanks for sharing!",
    "Interesting perspective.",
    "Could you elaborate more on this point?",
]

tags_data = [
    "Technology",
    "Politics",
    "Sports",
    "Entertainment",
    "Science",
]


def seed_data():
    db = SessionLocal()
    try:
        # Seed Users
        users = []
        for user_info in users_data:
            user = models.User(**user_info)
            db.add(user)
            users.append(user)
        db.commit()

        # Seed Tags
        tags = []
        for tag_name in tags_data:
            tag = models.Tag(name=tag_name)
            db.add(tag)
            tags.append(tag)
        db.commit()

        # Seed Posts
        posts = []
        for post_info in posts_data:
            user = random.choice(users)
            post = models.Post(**post_info, user_id=user.id)
            post.tags = random.sample(tags, random.randint(1, 3))
            db.add(post)
            posts.append(post)
        db.commit()

        # Seed Comments
        for _ in range(20):
            user = random.choice(users)
            post = random.choice(posts)
            comment_content = random.choice(comments_data)
            comment = models.Comment(
                content=comment_content, user_id=user.id, post_id=post.id
            )
            db.add(comment)
        db.commit()

        print("Data seeding completed successfully.")
    except Exception as e:
        print(f"An error occurred while seeding data: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
