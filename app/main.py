from fastapi import FastAPI

# Импортируем настройки проекта из config.py.
# from app.api.endpoints.meeting_room import router

# Импортируем главный роутер.
from app.api.routers import main_router
from app.core.config import settings
from app.core.init_db import create_first_superuser

app = FastAPI(title=settings.app_title,
              description=settings.description,
              docs_url='/swagger',
              )

# Подключаем роутер.
app.include_router(main_router)

# При старте приложения запускаем корутину create_first_superuser.
@app.on_event('startup')
async def startup():
    await create_first_superuser()

