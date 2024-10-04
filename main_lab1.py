from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{starting_number}")
def get_factorial(starting_number:int):

    if starting_number == 0:
        return {"result": False}
    

    num=1
    #while loop para sa factorial
    while starting_number >= 1:
        num = num * starting_number
        starting_number = starting_number - 1

    if num != 0:
        return {"result":num}






    