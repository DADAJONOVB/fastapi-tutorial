import ormar
from database.config import MainMeta
import datetime
from passlib.hash import pbkdf2_sha256


class User(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=255, unique=True)
    password: str = ormar.String(max_length=255)
    data_register: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    is_active: bool = ormar.Boolean(default=True)
    first_name: str = ormar.String(max_length=100)

    async def save(self, *args, **kwars):
        self.password = pbkdf2_sha256.hash(self.password)
        await super().save(*args, **kwars)