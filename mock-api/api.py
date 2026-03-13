import contextlib
import json
import operator
import pathlib
import time

import fastapi

DATA: list = []


@contextlib.asynccontextmanager
async def lifespan(_app: fastapi.FastAPI):
    global DATA
    DATA = json.loads(pathlib.Path("rappelconso-v2-gtin-espaces.json").read_text())
    yield
    del DATA


app = fastapi.FastAPI(title="RappelConsoMockAPI", version='0.1', lifespan=lifespan)


@app.get('/api/records')
async def get_data(limit: int = 10, offset: int = 0, order_by: str = None, where: str = None):
    if where:
        wh = where.strip().split()
        wh_date = time.strptime(wh[2].strip("'").split('T')[0], "%Y-%m-%d")
        wh_op = operator.gt if '>' in wh[1] else operator.lt if '<' in wh[1] else operator.eq
        results = list(filter(lambda d: wh_op(time.strptime(d[wh[0]].strip("'").split('T')[0],
                                                            "%Y-%m-%d"), wh_date), DATA))
    else:
        results = DATA
    if order_by:
        ob = order_by.split()
        results = sorted(results,
                         key=operator.itemgetter(ob[0]),
                         reverse=True if len(ob) > 1 and 'DESC' in ob[1].upper() else False)
    results = results[offset:offset + limit]
    return {'total_count': len(results), 'results': results}
