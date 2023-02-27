import ormar
import datetime
from database.config import MainMeta
from  typing import Optional
from auth.models import User



class Blog(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=255)
    body: str = ormar.Text()
    created: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    is_active: bool = ormar.Boolean(default=True)
    author: Optional[User] = ormar.ForeignKey(User)

class Comment(ormar.Model):
    class Meta(MainMeta):
        pass
    
    id: int = ormar.Integer(primary_key=True)
    body: str = ormar.Text()
    blog: Optional[Blog] = ormar.ForeignKey(Blog)
    created: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)