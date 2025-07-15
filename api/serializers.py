from datetime import datetime

class Comment:
    def __init__(self, email, content, created = None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment1 = Comment("admin@gmail.com", "test comment content")

