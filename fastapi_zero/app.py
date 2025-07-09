from fastapi import FastAPI

from fastapi_zero.core import Settings
from fastapi_zero.routes import router


class App(FastAPI):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.include_router(router=router)
        self.title = Settings().NAME_PROJECT
        self.description = Settings().DESCRIPTION
        self.version = Settings().VERSION
        self.root_path = Settings().ROOT_PATH


app = App()
