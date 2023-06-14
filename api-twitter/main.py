from fastapi import FastAPI
from src.responses import TrendItem
from src.services import get_mongos_trends, save_trends

from typing import List

import uvicorn


app = FastAPI()


@app.get('/trends', response_model=List[TrendItem])
def get_trends_routes():
    return get_mongos_trends()


if __name__ == '__main__':
    trends = get_mongos_trends()

    if not trends:
        save_trends()

    uvicorn.run(app, host='0.0.0.0', port=8000)