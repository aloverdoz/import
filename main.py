from application.salary import money
from application.db.people import  pipl
from datetime import datetime

def tday():
    money()
    pipl()
    print(datetime.now().strftime('%F %T %f')[:-7])

if __name__ == '__main__':
    tday()
