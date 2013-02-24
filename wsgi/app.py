from models import *
from sqlalchemy import create_engine
from flask import Flask, request
from json import dumps

app = Flask(__name__)
conn = engine.connect()

@app.route('/api')
def hello():
    return 'Hello World!'

@app.route('/api/schools/totals/<snapshot>')
def school_totals(snapshot):
    items = select([
        func.sum(Budget.c.amount), Ulcs.c.ulcs])\
        .select_from(Budget.join(Item).join(Ulcs).join(Snapshot))\
        .where(Snapshot.c.snapshot==snapshot)\
        .where(Item.c.item != 'Total')\
        .group_by(Ulcs.c.ulcs)

    sums = []

    for amt,ulcs in conn.execute(items):
        sums.append({
            'ulcs': { 'ulcs': ulcs,
                      'link': 'http://%s/api/budget/%s' % (request.host, ulcs) },
            'total': amt
        })

    return dumps(sums)


@app.route('/api/dates')
def dates():
    snapshots = {}
    q = select([Snapshot])
    for pk, snid, descr in conn.execute(q):
        snapshots[snid] = descr
    return dumps(snapshots)

@app.route('/api/schools')
def schools():
    schools = []
    q = select([Ulcs.join(SchoolLocations)]).apply_labels()
    for row in conn.execute(q):
        ulcs = row['ulcs_ulcs']
        schools.append({
            'ulcs': ulcs,
            'geom': map(lambda z: "%2.5f" % z,
                        row['school_location_geom'].coords(engine)),
            'link': 'http://%s/api/budget/%s' % (request.host, ulcs)
        })
    return dumps(schools)

@app.route('/api/budget/<school>')
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
            'link': 'http://%s/api/budget/%s/%s' % (request.host, school, snid)
        }

    return dumps(years)

@app.route('/api/budget/<school>/<snapshot>')
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
             'link': 'http://%s/api/budgetitem/%s' % (request.host, row['item_id']),
             'amount': row['budget_amount']})


    ulcs = { 'ulcs': school,
             'link': 'http://%s/api/budget/%s' % (request.host, school) }

    budget = { 'school': ulcs,
               'snapshot': snapshot,
               'items': budget }

    return dumps(budget)

@app.route('/api/budgetitem/')
@app.route('/api/budgetitem/<itemid>')
def budget_item(itemid=None):
    # No itemid specified, list all of them
    if itemid is None:
        items = []
        q = select([Budget.join(Item)])\
            .distinct(Item.c.item)\
            .apply_labels()

        for row in conn.execute(q):
            items.append(
                {'item': row['item_item'],
                 'id': row['item_id'],
                 'link': 'http://%s/api/budgetitem/%s' % (request.host, row['item_id'])})

        return dumps(items)

    # Return the requested budget item
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
             'link': 'http://%s/api/budget/%s/%s' % (request.host, ulcs, snap)
         })

    return dumps(budget)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
