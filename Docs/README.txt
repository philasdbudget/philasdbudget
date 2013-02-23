README.txt
This README file contains some background information and guidance on School District of Philadelphia data. All data is aggregated per school, and is given per school year (e.g. 2011-2012). This set of data was extracted on October 22, 2012 in coordination with State Reporting requirements. Due to other state and federal reporting requirements, much of this data is available from other sources. Typically each entity has their own requirements, and frequently refactor and aggregate data in different ways. Please keep this in mind if you compare this data with data derived from other sources. Most importantly, do not hesitate to contact us if you have any questions, or would like to request other data sets.
Happy data diving!
opendata@philasd.org

Notes on individual files:

README.TXT  - You're soaking in it!

SCHOOL_INFORMATION.csv
Provides basic information on each school, including School_code (a unique identifier for each school).
SCHOOL_CODE - Unique identifier for each program; note that there may be several programs within a given school building (for example, Head Start).
SCHOOL_NAME_1 - Name of school.
SCHOOL_NAME_2 - Alternate name of school.
ADDRESS - Street address of school.
SCHOOL_ZIP - Zip code of school.
SCHOOL_ZIP_PLUS_4 - Zip+4 of school, often blank.
CITY - self explanatory.
STATE_CD - self explanatory.
PHONE_NUMBER - self explanatory.
SCH_START_GRADE - The lowest grade offered in the school; "00" means kindergarden.
SCH_TERM_GRADE - The highest grade offered in the school.
HPADDR - Web site address for school.
SCHOOL_LEVEL_NAME - Type of School.

SCHOOL_ENROLLMENT.csv - SDP School Enrollment data for five years.
SCHOOL_CODE - Unique identifier for each program; note that there may be several programs within a given school building (for example, Head Start).
SCHOOL_YEAR - Two years separated by a hyphen, corresponding to an academic school year.
SCH_ATTENDANCE - Attendance of students, reported as a percentage, reflecting the entire school year.
SCH_ENROLLMENT - Total number of students enrolled in school at the start of the year.
SCH_STUDENT_ENTERED - Number of students that entered the school after the start of the year.
SCH_STUDENT_WITHDREW - Number of students that withdrew from school during the year; this may include transfers to another school, drop outs, and expulsions.

SCHOOL_ETHNICITY_LOW_INCOME.csv - Ethnic and Low Income Information for students for five years, expressed as a percentage.  Note: Census Changes in Ethnicity Categories can be seen 2012-2013 data.
SCHOOL_CODE - Unique identifier for each program; note that there may be several programs within a given school building (for example, Head Start).
SCHOOL_YEAR - Two years separated by a hyphen, corresponding to an academic school year.
AFRICAN_AMERICAN - Percentage of African-American students.
WHITE - Percentage of white students.
ASIAN - Percentage of Asian students.
LATINO - Percentage of Latino students.
OTHER - Percentage of students without ethnic information.
PACIFIC_ISLANDER - Percentage of Pacific Islander students.
AMERICAN_INDIAN - Percentage of American Indian students.
SCH_LOW_INCOME_FAMILY - Percentage of students that are from low-income families; this is determined by the school.

SCHOOL_PSSA.csv - Aggregate PSSA scores (both math and science) for four years (2008-2009 forward). PSSA tests are given in 3-8th grade, and again in 11th grade. The scores are reported as percentage of students scoring Advanced, Proficient, Basic or Below basic.  These numbers currently exclude individual PASA scores as that was the previous requirement.  SDP will have new files with PASA scores included by end of February 2013.
SCHOOL_CODE - Unique identifier for each program; note that there may be several programs within a given school building (for example, Head Start).
SCHOOL_YEAR - Two years separated by a hyphen, corresponding to an academic school year.
GRADE - Grade level.
MATH_ADVANCED_PERCENT - Percentage of students that took the PSSA Math test that scored Advanced.
MATH_PROFICIENT_PERCENT - Percentage of students that took the PSSA Math test that scored Proficient.
MATH_BASIC_PERCENT - Percentage of students that took the PSSA Math test that scored Basic.
MATH_BELOW_BASIC_PERCENT - Percentage of students that took the PSSA Math test that scored Below Basic.
READ_ADVANCED_PERCENT - Percentage of students that took the PSSA Reading test that scored Advanced.
READ_PROFICIENT_PERCENT - Percentage of students that took the PSSA Reading test that scored Proficient.
READ_BASIC_PERCENT - Percentage of students that took the PSSA Math Reading that scored Basic.
READ_BELOW_BASIC_PERCENT - Percentage of students that took the PSSA Reading test that scored Below Basic.
MATH_COMBINED_PERCENT - Percentage of students that took the PSSA Math test that scored Advanced OR Proficient.
READ_COMBINED_PERCENT - Percentage of students that took the PSSA Reading test that scored Advanced OR Proficient.

SCHOOL_SERIOUS_INCIDENTS.txt  - Serious incident information for four years (2008-2009 forward).
SCHOOL_CODE - Unique identifier for each program; note that there may be several programs within a given school building (for example, Head Start).
SCHOOL_YEAR - Two years separated by a hyphen, corresponding to an academic school year.
INCIDENT_TYPE - Description of serious incident type.
INCIDENT_COUNT - Total count per year per incident type.

SCHOOL_STUDENT.txt  - Information on students with disabilities, mentally gifted and English language learners for five years.
SCHOOL_CODE - Unique identifier for each program; note that there may be several programs within a given school building (for example, Head Start).
SCHOOL_YEAR - Two years separated by a hyphen, corresponding to an academic school year.
SCH_SPEC_ED_SERVICES - Percentage of students receiving special educational services per year, per school.
SCH_MG - Percentage of students receiving mentally gifted educational services per year, per school.
SCH_ESOL_SERVICES - Percentage of students receiving English for speakers of other languages services per year, per school.

SCHOOL_SUSPENSIONS.txt  - Distinct Student Suspension data for four years (2008-2009 forward).
SCHOOL_CODE - Unique identifier for each program; note that there may be several programs within a given school building (for example, Head Start).
SCHOOL_YEAR - Two years separated by a hyphen, corresponding to an academic school year.
TOTAL_SUSPENSIONS - Total number of suspensions per year, per school.
SCH_ONE_TIME_SUSP - Total number of children that were suspended once (and only once) during the year, per school.
SCH_TWO_TIME_SUSP - Total number of children that were suspended twice during the year, per school.
SCH_THREE_TIME_SUSP - Total number of children that were suspended three times during the year, per school.
SCH_MORE_THAN_THREE_SUSP - Total number of children that were suspended more than three times during the year, per school.

TEACHER_ATTEND.txt  - Information on teacher attendance for three years.
SCHOOL_CODE - Unique identifier for each program; note that there may be several programs within a given school building (for example, Head Start).
SCHOOL_YEAR - Two years separated by a hyphen, corresponding to an academic school year.
SCH_TEACHER_ATTEND - Average teacher attendance per school, by year.
SDP_TEACHER_ATTEND - District wide average of all teachers, by year.
