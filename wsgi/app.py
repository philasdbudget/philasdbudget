from models import *
from sqlalchemy import create_engine
from flask import Flask, request
from json import dumps

app = Flask(__name__)
conn = engine.connect()

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/dates')
def dates():
    snapshots = {}
    q = select([Snapshot])
    for pk, snid, descr in conn.execute(q):
        snapshots[snid] = descr
    return dumps(snapshots)

@app.route('/schools')
def schools():
    schools = []
    q = select([Ulcs])
    for pk, ulcs in conn.execute(q):
        schools.append(ulcs)
    return dumps(schools)

@app.route('/budget/<school>')
def years_for_school(school):
    q = select([Budget.join(Item).join(Ulcs).join(Snapshot)])\
        .where(Ulcs.c.ulcs==school)\
        .distinct(Snapshot.c.snapshot)\
        .apply_labels()

    years = {}
    for row in conn.execute(q):
        snid = row['snapshots_snapshot']
        years[snid] = {
            'description': row['snapshots_descr'],
            'link': 'http://%s/budget/%s/%s' % (request.host, school, snid)
        }

    return dumps(years)

@app.route('/budget/<school>/<snapshot>')
def budget(school, snapshot):
    budget = []
    q = select([Budget.join(Item).join(Ulcs).join(Snapshot)])\
        .where(Ulcs.c.ulcs==school)\
        .where(Snapshot.c.snapshot==snapshot)\
        .apply_labels()

    for row in conn.execute(q):
        budget.append({'item': row['item_item'], 'amount': row['budget_amount']})

    return dumps(budget)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
