from fastapi import FastAPI
import final_t as ft
import schedule
import logging
import log_package as lp
import module_file as mf
app = FastAPI()

logger = lp.log_setting(logging)

@app.get("/")
def read_root():




    return ft.reserve__stock()

