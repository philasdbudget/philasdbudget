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
    q = select([Ulcs.join(SchoolLocations)]).apply_labels()
    for row in conn.execute(q):
        ulcs = row['ulcs_ulcs']
        schools.append({
            'ulcs': ulcs,
            'geom': map(lambda z: "%2.5f" % z,
                        row['school_location_geom'].coords(engine)),
            'link': 'http://%s/budget/%s' % (request.host, ulcs)
        })
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
        budget.append(
            {'item': row['item_item'],
             'id': row['item_id'],
             'link': 'http://%s/budgetitem/%s' % (request.host, row['item_id']),
             'amount': row['budget_amount']})


    ulcs = { 'ulcs': school,
             'link': 'http://%s/budget/%s' % (request.host, school) }

    budget = { 'school': ulcs,
               'snapshot': snapshot,
               'items': budget }

    return dumps(budget)

@app.route('/budgetitem/<itemid>')
def budget_item(itemid):
    budget = {}
    q = select([Budget.join(Item).join(Ulcs).join(Snapshot)])\
        .where(Item.c.id==itemid)\
        .apply_labels()

    for row in conn.execute(q):
        snap = row['snapshots_snapshot']
        if snap in budget:
            snaps = budget[snap]
        else:
            snaps = {}
            budget[snap] = snaps

        ulcs = row['ulcs_ulcs']
        if ulcs in snaps:
            ulcses = snaps[ulcs]
        else:
            ulcses = []
            snaps[ulcs] = ulcses

        ulcses.append(
            {'item': row['item_item'],
             'amount': row['budget_amount'],
             'link': 'http://%s/budget/%s/%s' % (request.host, ulcs, snap)
         })

    return dumps(budget)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
