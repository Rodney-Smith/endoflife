import urllib
import urllib.request
import subprocess
import json
import os
import re
from datetime import timedelta,date,datetime
import pandas as pd

def eol():
    today = date.today()
    result_eol = []
    url = "https://endoflife.date/api/all.json"
    response = urllib.request.urlopen(url)
    data = json.load(response)

    for item in data:
        #print('calling api....')
        url1 = "https://endoflife.date/api/"+item+".json"
        response1 = urllib.request.urlopen(url1)
        data1 = json.load(response1)

        for item1 in range(0, len(data1)):
            try:
                datetime_str = (datetime.strptime(((data1[item1]['eol'])), '%Y-%m-%d').date())
                eol_cycle = data1[item1]['cycle']
                lts_eol = data1[item1]['lts']
                release_eol = data1[item1]['releaseDate']
                result_eol.append((item,datetime_str,eol_cycle,lts_eol,release_eol))
            except (TypeError, KeyError) as etk:
                try:
                    result_eol.append((item,datetime_str,eol_cycle,lts_eol,release_eol))
                except KeyError:
                    result_eol.append((item,datetime_str,eol_cycle,lts_eol,release_eol))
    df = pd.DataFrame(result_eol,columns=['Product', 'End of life data', 'Version','Has LTS','Release date'])
    df.to_csv('eol.csv')
                    #df.to_json('eol.json')
    return(result_eol)

if __name__ == '__main__':
    r_eol = []
    r_eol = eol()
