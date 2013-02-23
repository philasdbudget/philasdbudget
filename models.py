from sqlalchemy import *


class SchoolEnrollment(Base):
  __tablename__ = 'SCHOOL_ENROLLMENT'

   SCHOOL_CODE = Column(Integer)
   SCHOOL_YEAR = Column(String)
   SCH_ATTENDANCE = Column(Float) 
   SCH_ENROLLMENT = Column(Integer)
   SCH_STUDENT_ENTERED = Column(Integer)
   SCH_STUDENT_WITHDREW = Column(Integer)

class SchoolEthnicityLowIncome(Base):
	__tablename__ = "SCHOOL_ETHNICITY_LOW_INCOME"

   SCHOOL_CODE = Column(Integer)
   SCHOOL_YEAR = Column(String) 
   AFRICAN_AMERICAN = Column(Float)
   WHITE = Column(Float)
   ASIAN = Column(Float)
   LATINO = Column(Float)
   OTHER = Column(Float) 
   PACIFIC_ISLANDER = Column(Float)
   AMERICAN_INDIAN = Column(Float) 
   SCH_LOW_INCOME_FAMILY = Column(Float)

class SchoolInformation(Base):
	__tablename__ = "SCHOOL_INFORMATION"

   SCHOOL_CODE = Column(Integer)
   SCHOOL_NAME_1 = Column(String)
   SCHOOL_NAME_2 = Column(String)
   ADDRESS = Column(String)
   SCHOOL_ZIP = Column(Integer)
   ZIP_PLUS_4 = Column(String)
   CITY = Column(String)
   STATE_CD = Column(String) 
   PHONE_NUMBER = Column(Integer)
   SCH_START_GRADE = Column(Integer)
   SCH_TERM_GRADE = Column(Integer)
   HPADDR = Column(String)
   SCHOOL_LEVEL_NAME = Column(String)

class SchoolPSSA(Base):
	__tablename__ = "SCHOOL_PSSA"

   SCHOOL_CODE = Column(Integer)
   SCHOOL_YEAR = Column(String)
   GRADE = Column(Integer)
   MATH_ADVANCED_PERCENT = Column(String)
   MATH_PROFICIENT_PERCENT = Column(String)
   MATH_BASIC_PERCENT = Column(String)
   MATH_BELOW_BASIC_PERCENT = Column(String)
   READ_ADVANCED_PERCENT = Column(String)
   READ_PROFICIENT_PERCENT = Column(String)
   READ_BASIC_PERCENT = Column(String)
   READ_BELOW_BASIC_PERCENT = Column(String)
   MATH_COMBINED_PERCENT = Column(String)
   READ_COMBINED_PERCENT = Column(String)

class SeriousIncidents(Base):
	__tablename__ = "SCHOOL_SERIOUS_INCIDENTS"

   ULCS_NO = Column(Integer)
   SCHOOL_YEAR = Column(String)
   ASSAULT = Column(Integer)
   DRUG = Column(Integer)
   MORALS = Column(Integer)
   WEAPONS = Column(Integer)
   THEFT = Column(Integer)

class SchoolStudent(Base):

	__tablename__ = "SCHOOL_STUDENT"

	SCHOOL_CODE = Column(Integer)
	SCHOOL_YEAR = Column(String)
	SCH_SPEC_ED_SERVICES = Column(Float)
	SCH_MG = Column(Float)
	SCH_ESOL_SERVICES = Column(Float)

class SchoolSuspensions(Base):

	__tablename__ = "SCHOOL_SUSPENSIONS"

	SCHOOL_CODE = Column(Integer)
	SCHOOL_YEAR = Column(String)
	TOTAL_SUSPENSIONS = Column(Integer)
	SCH_ONE_TIME_SUSP = Column(Integer)
	SCH_TWO_TIME_SUSP = Column(Integer)
	SCH_THREE_TIME_SUSP = Column(Integer)
	SCH_MORE_THAN_THREE_SUSP = Column(Integer)

class TeacherAttend(Base):
	
	__tablename__ = "TEACHER_ATTEND"

	SCHOOL_CODE = Column(Integer)
	SCHOOL_YEAR = Column(String)
	SCH_TEACHER_ATTEND = Column(Float)
	SDP_TEACHER_ATTEND_AVG = Column(Float)
	
