# preprocess transcript data for online verification

# input data index info
# 0: semester (xxxx-xxxx x to xxxx-xxxx-x)
# 1: course code
# 2: course number
# 3: course name
# 4: course category
# 5: credit
# 6: grade
# 7: final grade (same as grade, theoretically)

import csv

filename = 'data'
elective_categories_cn = ['本专业选修课', '素质教育选修课（社会科学类）', '创新与拓展项目']
elective_categories_en = ['']

# open file
in_f = open(filename + '.tsv', 'r')
out_f = open(filename + '.csv', 'w')
# csv writer
writer = csv.writer(out_f, delimiter=',', lineterminator='\n')

# read tab separated data
for line in in_f:
    course_item = line.split('\t')
    # xxxx-xxxx x to xxxx-xxxx-x
    course_item[0] = course_item[0].replace(' ', '-')

    # check course category
    if course_item[4] in elective_categories_cn:
        # elective
        course_item[4] = '选修课'
    else:
        course_item[4] = '必修课'

    # course name, grade, credit, period (null), period unit (null), course category, semester
    course_grade_info = [course_item[3], course_item[6], course_item[5], '', '', course_item[4], course_item[0]]
    writer.writerow(course_grade_info)
    print(course_grade_info)

in_f.close()
out_f.close()
