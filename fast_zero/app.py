from fastapi import FastAPI

from fast_zero.routers import auth, users

app = FastAPI(
    title='Estudando Fast API',
    description='Aprendendo a criar APIs com FastAPI',
    version='0.0.1',
)

app.include_router(users.router)
app.include_router(auth.router)
