from models import *
from settings import ROOT
from sqlalchemy import create_engine
from flask import Flask, request, render_template
from json import dumps

app = Flask(__name__)
conn = engine.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def hello():
    return 'Hello World!'

@app.route('/api/schools/totals/<snapshot>')
def school_totals(snapshot):
    items = select([
        func.sum(Budget.c.amount),
        Ulcs.c.ulcs])\
        .select_from(Budget.join(Item)\
                     .join(Ulcs)\
                     .join(Snapshot))\
        .where(Snapshot.c.snapshot==snapshot)\
        .where(Item.c.item != 'Total')\
        .group_by(Ulcs.c.ulcs)\
        .apply_labels()

    school_query = select([SchoolEnrollment])

    sums = []

    for amt,ulcs in conn.execute(items):
        enrollment = conn.execute(school_query.where(SchoolEnrollment.c.school_code==ulcs)).fetchone()

        if enrollment:
            sums.append({
                'enrollment': enrollment.sch_enrollment,
                'ulcs': { 'ulcs': ulcs,
                          'link': 'http://%s/api/budget/%s' % (ROOT, ulcs) },
                'total': amt,
                'total_norm': amt / enrollment.sch_enrollment
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
    q = select([Ulcs\
                .join(SchoolLocations)\
                .join(SchoolInformation)]).apply_labels()

    for row in conn.execute(q):
        ulcs = row['ulcs_ulcs']
        schools.append({
            'ulcs': ulcs,
            'school_name': row['school_information_school_name_1'],
            'school_name2': row['school_information_school_name_2'],
            'address': row['school_information_address'],
            'geom': map(lambda z: "%2.5f" % z,
                        row['school_location_geom'].coords(engine)),
            'link': 'http://%s/api/budget/%s' % (ROOT, ulcs)
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
            'link': 'http://%s/api/budget/%s/%s' % (ROOT, school, snid)
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
             'link': 'http://%s/api/budgetitem/%s' % (ROOT, row['item_id']),
             'amount': row['budget_amount']})


    ulcs = { 'ulcs': school,
             'link': 'http://%s/api/budget/%s' % (ROOT, school) }

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
                 'link': 'http://%s/api/budgetitem/%s' % (ROOT, row['item_id'])})

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
             'link': 'http://%s/api/budget/%s/%s' % (ROOT, ulcs, snap)
         })

    return dumps(budget)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
