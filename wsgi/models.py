from settings import USER, PASSWORD, DB, HOST
from sqlalchemy import *
from geoalchemy import *

engine = create_engine(
  "postgresql://%s:%s@%s/%s" % (USER,PASSWORD,HOST,DB))

metadata = MetaData(bind=engine)

SchoolEnrollment = Table('school_enrollment', metadata,
                         Column('school_code', None, ForeignKey('ulcs.ulcs')),
                         autoload=True)

SchoolEthnicityLowIncome = Table('school_ethnicity_low_income',
                                 metadata, autoload=True)

SchoolInformation = Table('school_information', metadata, autoload=True)
SchoolPSSA = Table('school_pssa', metadata, autoload=True)
SeriousIncidents = Table('school_serious_incidents', metadata, autoload=True)
SchoolStudent = Table('school_student', metadata, autoload=True)
SchoolSuspensions = Table('school_suspensions', metadata, autoload=True)
TeacherAttend = Table('teacher_attend', metadata, autoload=True)
Budget = Table('budget', metadata,
               Column('ulcs', None, ForeignKey('ulcs.id')),
               Column('item', None, ForeignKey('item.id')),
               Column('snapshot', None, ForeignKey('snapshots.id')),
               autoload=True)
Item = Table('item', metadata, autoload=True)
Snapshot = Table('snapshots', metadata,
                 Column('schoolyear', None, ForeignKey('school_enrollment.school_year')),
                 autoload=True)
Ulcs = Table('ulcs', metadata, autoload=True)

SchoolLocations = Table('school_location', metadata,
                        GeometryExtensionColumn('geom',Point(2)),
                        Column('school_code', None, ForeignKey('ulcs.ulcs')),
                        Column('id', Integer, primary_key=True))

# conn = engine.connect()
# for row in conn.execute(select([Budget.join(Item).join(Snapshot).join(Ulcs)]).limit(2)):
#     print row
# for row in conn.execute(select([SchoolPSSA], SchoolPSSA.c.school_code == '1580')):
#     print row
