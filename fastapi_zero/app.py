from fastapi import FastAPI

from fastapi_zero.routes import router
from fastapi_zero.settings.settings import Settings


class App(FastAPI):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.include_router(router=router)
        self.title = Settings().NAME_PROJECT
        self.description = Settings().DESCRIPTION
        self.version = Settings().VERSION
        self.root_path = Settings().ROOT_PATH


app = App()
