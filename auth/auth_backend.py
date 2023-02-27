from fastapi_jwt import JwtAccessBearer



secret_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'



access_security = JwtAccessBearer(secret_key=secret_key, auto_error=True)