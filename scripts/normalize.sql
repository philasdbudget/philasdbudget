-- After loading school budget data this script     --
-- normalizes the data and sets useful foreign keys --

DROP TABLE IF EXISTS snapshots;
DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS ulcs;
DROP TABLE IF EXISTS budget;

CREATE TABLE snapshots (
     id       SERIAL,
     schoolyear varchar(100),
     snapshot varchar(10) NOT NULL,
     descr     varchar(250) NOT NULL
);
INSERT INTO snapshots (id, schoolyear, snapshot, descr)
       VALUES ('1', '2012-2013', '181', 'FY13 School Budgets May 24, 2012');

INSERT INTO snapshots (id, schoolyear, snapshot, descr)
       VALUES ('2', '2011-2012', '161', 'FY12 School Budgets May 27, 2011');

INSERT INTO snapshots (id, schoolyear, snapshot, descr)
       VALUES ('3', '2010-2011', '141', 'FY11 School Budgets  April 22,2010');

INSERT INTO snapshots (id, schoolyear, snapshot, descr)
       VALUES ('4', '2010-2011b', '121', 'FY10 School Budgets February 1, 2010');

INSERT INTO snapshots (id, schoolyear, snapshot, descr)
       VALUES ('5', '2009-2010', '101', 'FY10 School Budgets April 1 2009');

INSERT INTO snapshots (id, schoolyear, snapshot, descr)
       VALUES ('6', '2008-2009', '61', 'FY09 School Budgets (February 2009)');

CREATE TABLE ulcs (
     id       SERIAL,
     ulcs varchar(10) NOT NULL
);

INSERT INTO ulcs (ulcs) SELECT DISTINCT ulcs FROM budget_items;

CREATE TABLE item (
     id       SERIAL,
     item varchar(250) NOT NULL
);

INSERT INTO item (item) SELECT DISTINCT item FROM budget_items;

CREATE TABLE budget (
     id       SERIAL,
     ulcs     INTEGER NOT NULL,
     snapshot INTEGER NOT NULL,
     item     INTEGER NOT NULL,
     amount   integer
);

CREATE INDEX budget_ulcs ON budget (ulcs);
CREATE INDEX budget_snapshot ON budget (snapshot);
CREATE INDEX budget_item ON budget (item);

DROP TABLE IF EXISTS budget_items_tmp;
CREATE TABLE budget_items_tmp AS SELECT * FROM budget_items;

UPDATE budget_items_tmp SET ulcs = (SELECT id FROM ulcs WHERE ulcs = budget_items_tmp.ulcs);
UPDATE budget_items_tmp SET item = (SELECT id FROM item WHERE item = budget_items_tmp.item);
UPDATE budget_items_tmp SET snapshot = (SELECT id FROM snapshots WHERE snapshot = budget_items_tmp.snapshot);

INSERT INTO budget (id, ulcs, snapshot, item, amount)
       SELECT id, ulcs::int, snapshot::int, item::int, amount FROM budget_items_tmp;

DROP TABLE IF EXISTS budget_items_tmp;
