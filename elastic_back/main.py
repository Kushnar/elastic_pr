from fastapi import FastAPI, Request
from elastic_transport import ConnectionError, ConnectionTimeout
from elasticsearch import Elasticsearch, exceptions
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

ES = Elasticsearch('http://elastic:9200', request_timeout=15)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173/', 'http://front:8080/', 'localhost:8080', 'http://localhost:8080'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


class SortModel(BaseModel):
    target: str
    direction: str


class SearchData(BaseModel):
    value: str


def openfile():
    with open('test.csv', 'r', encoding='utf-8') as f:
        # reading first line, which contains keys of fields, slicing by ',' to get clean data list
        keys = []
        for k in f.readline().split(','):
            # removing \n symbols from strings and creating keys list
            keys.append(k.rstrip('\n'))

        # reading other lines with values and creating list of values variable to next saving values there
        values_lists = []
        for i in f.readlines():
            # creating line var. to next saving cleaned data to values_list
            line = []
            # slicing line by ',' to get clean list of values and then replacing typical double quotes and \n
            for el in i.split(','):
                line.append(el.strip('"').rstrip('"\n'))
            values_lists.append(line)

        # Here we have cleaned list of keys and list of cleaned lists, which contains values to db
        # Creating final dictionary to return
        final_li = []

        for i in values_lists:
            final_li.append(dict(zip(keys, i)))
        return final_li


@app.get('/')
async def root():
    return {'msg': 'Hello, visit /docs/ for more info'}


@app.get('/create-index')
async def create_index():
    try:
        # es.indices.create(index='test-index', mappings={
        #     'properties': {
        #         'customers_id': {
        #             'type': 'integer'
        #         },
        #     }
        # })
        try:
            ES.options(ignore_status=[400, 404]).indices.delete(index='test-index')
        except Exception as ex:
            print(ex)
        for i in openfile():
            ES.index(index="test-index", document=i)
        data = ES.search(index='test-index', size=30, sort=[{"customers_id.keyword": {"order": "asc"}}])['hits']['hits']
        return {'code': 200, 'data': data}
    except ConnectionError:
        print('Connection error')
        return {'error': 'Connection error'}
    except ConnectionTimeout:
        print('Connection timout')
        return {'error': 'Connection timeout'}


@app.get('/get-table-data')
async def get_table_data():
    try:
        data = ES.search(index='test-index', size=30, sort=[{"customers_id.keyword": {"order": "asc"}}])['hits']['hits']
        return {'code': 200, 'data': data} if data else {'code': 400, 'msg': 'data'}
    except exceptions.NotFoundError:
        return {'error': 'Index Not Found', 'code': 400}


@app.post('/sort-table')
async def sort_table(data: SortModel):
    try:
        if data.target and data.direction:
            if data.direction == 'True':
                order = 'asc'
            else:
                order = 'desc'
            data = ES.search(index='test-index', size=30,
                             sort=[{f"{data.target}.keyword": {"order": f"{order}"}}])['hits']['hits']
            return {'status': 'success', 'data': data} if data else {'status': 'error', 'msg': 'something wrong'}
    except Exception:
        return {'error': 'Something wrong'}


@app.post('/search')
async def search(data: SearchData):
    response = ES.search(index="test-index", query={
        "multi_match": {
            "query": f"{data.value}",
            "fields": [
                "customers_firstname",
                "customers_secondname",
                "customers_lastname",
                "customers_email_address",
            ],
            "type": "best_fields",
        }
    }
                         )['hits']['hits']
    return {'data': response}
