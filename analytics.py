import pandas as pd
from contextlib import redirect_stdout


def get_phone_os_count(phone_os_list):
    df = pd.DataFrame({'phone_OS': phone_os_list})
    result = df.value_counts()
    print(result)


def create_analytics(func, lst):
    with open('os_count.txt', 'w') as fp:
        with redirect_stdout(fp):
            func(lst)
