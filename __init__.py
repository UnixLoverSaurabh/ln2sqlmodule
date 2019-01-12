from ln2sql import main as __main__
import re
import os

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def getSql(query, sqlDump, outputFile=None):
    # unit test
    # args = ['-d', 'ln2sqlmodule/emp_dump.sql', '-l', 'ln2sqlmodule/lang/english.csv', '-i', query, '-j', 'ln2sqlmodule/output.json','-x']
    # args = ['-d', 'ln2sqlmodule/emp_dump.sql', 'ln2sqlmodule/lang/english.csv', '-i', query, '-j', 'ln2sqlmodule/output.json']

    # args = ['-d', 'ln2sqlmodule/timesheet.sql', '-l',
    #         'ln2sqlmodule/lang/english.csv', '-i', query, '-j', 'ln2sqlmodule/output.json']

    args = ['-d', sqlDump,
            '-l', os.path.dirname(os.path.abspath(__file__)
                                  ) + '/lang/english.csv',
            '-i', query,
            '-j', outputFile]

    sql = __main__(args)

    return str(sql)


def getSql_like(query, sqlDump, outputFile=None):
    sql = getSql(query, sqlDump, outputFile)

    sql = re.sub("(WHERE \S+ )=", r'\g<1>LIKE', sql)
    sql = re.sub("(AND \S+ )=", r'\g<1>LIKE', sql)
    sql = re.sub("(OR \S+ )=", r'\g<1>LIKE', sql)

    # 'abc def' -> '%abc%def%'
    for i in re.findall("'(.*?)'", sql):
        sql = sql.replace(i, "%" + i + "%")
        sql = sql.replace(i, i.replace(' ', '%'))

    return sql


#print(getSql("get name of all emp", "./emp.sql"))

# print(getSql("all data for emp where name is 'abc xyz'", "./emp.sql"))
print(color.BOLD + color.RED + str(getSql("all data for emp where name is 'abc xyz'", "./emp.sql")) + color.END)
#print(getSql_like("all data for emp where name is 'abc xyz'", "./emp.sql"))
