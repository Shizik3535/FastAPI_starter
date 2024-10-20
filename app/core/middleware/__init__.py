from fastapi.middleware.cors import CORSMiddleware

from app.main import app
# import middleware
from app.core.middleware.cors import origins


middleware = [
    # all middlewares
]

# add middleware
for middleware in middleware:
    app.add_middleware(middleware)


# add cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
