from fastapi import FastAPI, HTTPException
import logging, uvicorn
import requests

# kreiranje logera https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__) 
logger.setLevel("DEBUG")

# kreiranje logger consol
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# format
formatter = logging.Formatter('%(levelname)s:     %(name)s.%(funcName)s: %(message)s')

# dodaj format u consol-u
ch.setFormatter(formatter)

# dodaj consol-u logger
logger.addHandler(ch)

app = FastAPI()

@app.get("/")
async def health_check():
    logger.info("{Health : OK}, 200")
    return {"Health": "OK"}

@app.get("/get-data")
async def get_data():
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.0165&lon=21.0059&appid=cc48c29524a69fb60ffad1e23ec4184d')
    
    logger.info("{0}".format(r.text))
    return {"data": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")