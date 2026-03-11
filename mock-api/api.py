import json
import operator
import pathlib
from time import strptime

import fastapi

app = fastapi.FastAPI(title="RappelConsoMockAPI", version='0.1')
data: list = json.loads(pathlib.Path("rappelconso-v2-gtin-espaces.json").read_text())


@app.get('/api/records')
async def get_data(limit: int = 10, offset: int = 0, order_by: str = None, where: str = None):
    if where:
        wh = where.strip().split()
        wh_date = strptime(wh[2].strip("'").split('T')[0], "%Y-%m-%d")
        wh_op = operator.gt if '>' in wh[1] else operator.lt if '<' in wh[1] else operator.eq
        results = list(filter(lambda d: wh_op(strptime(d[wh[0]].strip("'").split('T')[0],
                                                       "%Y-%m-%d"), wh_date), data))
    else:
        results = data
    if order_by:
        ob = order_by.split()
        results = sorted(results,
                         key=operator.itemgetter(ob[0]),
                         reverse=True if len(ob) > 1 and 'DESC' in ob[1].upper() else False)
    results = results[offset:offset + limit]
    return {'total_count': len(results), 'results': results}
