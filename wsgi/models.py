from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

Base = declarative_base()

class SchoolEnrollment(Base):
    __tablename__ = 'SCHOOL_ENROLLMENT'

    school_code = Column(Integer, primary_key=True)
    school_year = Column(String, primary_key=True)
    sch_attendance = Column(Float)
    sch_enrollment = Column(Integer)
    sch_student_entered = Column(Integer)
    sch_student_withdrew = Column(Integer)

class SchoolEthnicityLowIncome(Base):
    __tablename__ = "SCHOOL_ETHNICITY_LOW_INCOME"

    school_code = Column(Integer, primary_key=True)
    school_year = Column(String, primary_key=True)
    african_american = Column(Float)
    white = Column(Float)
    asian = Column(Float)
    latino = Column(Float)
    other = Column(Float)
    pacific_islander = Column(Float)
    american_indian = Column(Float)
    sch_low_income_family = Column(Float)

class SchoolInformation(Base):
    __tablename__ = "SCHOOL_INFORMATION"

    school_code = Column(Integer, primary_key=True)
    school_name_1 = Column(String)
    school_name_2 = Column(String)
    address = Column(String)
    school_zip = Column(Integer)
    zip_plus_4 = Column(String)
    city = Column(String)
    state_cd = Column(String)
    phone_number = Column(Integer)
    sch_start_grade = Column(Integer)
    sch_term_grade = Column(Integer)
    hpaddr = Column(String)
    school_level_name = Column(String)

class SchoolPSSA(Base):
    __tablename__ = "SCHOOL_PSSA"

    school_code = Column(Integer, primary_key=True)
    school_year = Column(String, primary_key=True)
    grade = Column(Integer)
    math_advanced_percent = Column(String)
    math_proficient_percent = Column(String)
    math_basic_percent = Column(String)
    math_below_basic_percent = Column(String)
    read_advanced_percent = Column(String)
    read_proficient_percent = Column(String)
    read_basic_percent = Column(String)
    read_below_basic_percent = Column(String)
    math_combined_percent = Column(String)
    read_combined_percent = Column(String)

class SeriousIncidents(Base):
    __tablename__ = "SCHOOL_SERIOUS_INCIDENTS"

    ulcs_no = Column(Integer, primary_key=True)
    school_year = Column(String, primary_key=True)
    assault = Column(Integer)
    drug = Column(Integer)
    morals = Column(Integer)
    weapons = Column(Integer)
    theft = Column(Integer)

class SchoolStudent(Base):

    __tablename__ = "SCHOOL_STUDENT"

    school_code = Column(Integer, primary_key=True)
    school_year = Column(String, primary_key=True)
    sch_spec_ed_services = Column(Float)
    sch_mg = Column(Float)
    sch_esol_services = Column(Float)

class SchoolSuspensions(Base):

    __tablename__ = "SCHOOL_SUSPENSIONS"

    school_code = Column(Integer, primary_key=True)
    school_year = Column(String, primary_key=True)
    total_suspensions = Column(Integer)
    sch_one_time_susp = Column(Integer)
    sch_two_time_susp = Column(Integer)
    sch_three_time_susp = Column(Integer)
    sch_more_than_three_susp = Column(Integer)

class TeacherAttend(Base):

    __tablename__ = "TEACHER_ATTEND"

    school_code = Column(Integer, primary_key=True)
    school_year = Column(String, primary_key=True)
    sch_teacher_attend = Column(Float)
    sdp_teacher_attend_avg = Column(Float)
