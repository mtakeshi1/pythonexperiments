import json
from datetime import datetime, timedelta
import os
import subprocess
from sys import argv
from typing import Dict, Tuple
import io


def parse_date(s: str) -> datetime:
    if s.find('.') >= 0:
        s = s[:s.find('.')]
    aa = datetime.fromisoformat(s)
    return aa - timedelta(hours=3)


def formatdate(d: datetime) -> str:
    return f'{d.year}-{d.month}-{d.day} {d.hour}:{d.minute}'


def parse_file(fileorstream):
    infile = json.load(fileorstream)

    mintime: None | datetime = None
    maxtime: None | datetime = None
    programs: Dict[str, int] = dict()
    intervals: Dict[Tuple[datetime, datetime], Dict[str, int]] = dict()

    for e in infile:
        dt = parse_date(e['date'])
        if not mintime or dt < mintime:
            mintime = dt
        if not max or dt > mintime:
            maxtime = dt
        # print(e.keys())
        if int(e['inactive']) >= 600000 :
            if len(programs) > 0:
                intervals[(mintime, maxtime)] = programs
                programs = dict()
                mintime = None
                maxtime = None
        else:
            for w in e['windows']:
                if w['active']:
                    k = w['program']
                    programs[k] = programs.get(k, 0) + 1
                    # print(w['program'])

    if mintime and maxtime:
        intervals[(mintime, maxtime)] = programs

    for key, val in intervals.items():
        m = int((key[1] - key[0]).total_seconds()/60)
        hours,mins = divmod(m, 60)
        print(f'{formatdate(key[0])}\t{formatdate(key[1])} - total: {hours}:{mins}  \t{val}')


if len(argv) < 2:
    basedir = '/home/takeshi/.arbtt/'
    for f in os.listdir(basedir):
        if f.startswith('capture') and f.endswith('.log'):
            fullpath = os.path.join(basedir, f)
            # print(f'parsing {fullpath}')
            proc = subprocess.run(['arbtt-dump', '-f', fullpath, '-t', 'JSON'], capture_output=True)
            parse_file(io.BytesIO(proc.stdout))

else:
    parse_file(open(argv[1], 'r'))
