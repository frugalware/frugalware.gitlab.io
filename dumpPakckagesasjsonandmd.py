#!/usr/bin/env python

import json
import datetime
import argparse
import mariadb
import sys
from lunr import lunr
from functools import reduce

parser = argparse.ArgumentParser(
                    prog='dumpPakckagesasjsonandmd.py',
                    description='Dump package description and metadata to .md files and JSON Index',
                    epilog='Here be dragons')

parser.add_argument('-t', '--hugo_directory', help="Directory containing hugo", default="./")
parser.add_argument('-j', '--json_path', help="Where to create index file", default="/pub/PagesIndex.json")
parser.add_argument('-u', '--username', help="DB username")
parser.add_argument('-p', '--password', help="DB password")
parser.add_argument('-d', '--dbname', help="DB name", default="frugalware2")
parser.add_argument('-f', '--fwver', help="FW Ver", default="current")
parser.add_argument('-a', '--arch', help="FW arg", default="x86_64")
parser.add_argument('-s', '--server', help="DB server or socket", default="localhost")

args = parser.parse_args()

packages_as_dict = {}

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=args.username,
        password=args.password,
        host=args.server,
        port=3306,
        database=args.dbname
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor(dictionary=True)

cur.execute("SELECT * FROM packages WHERE arch = ? AND fwver = ?", (args.arch, args.fwver))


for package in cur:
    depends = []
    files = []
    reverse_depends = []
    
    package_id = package['id']
    name = package['pkgname']
    version = package['pkgver']
    arch = package['arch']    
    url = package['url']
    builddate = package['builddate']        
    
    desc = package['desc']
    size = package['size']
    usize = package['usize']
    sha1sum = package['sha1sum']
    
    # Get Cursor
    cur2 = conn.cursor()

    cur2.execute("SELECT file FROM files WHERE pkg_id = ? ORDER BY file", ([package_id]))
    files = cur2.fetchall()
    files = flattened = [item for sublist in files for item in sublist]
    files = list(filter(lambda filename: not(filename.endswith('/')), files))
    
    # Get Cursor
    cur3 = conn.cursor()
    
    cur3.execute("SELECT name FROM groups \
        WHERE id in (SELECT group_id FROM ct_groups WHERE pkg_id = ?) ORDER BY name", ([package_id]))
    groups = cur3.fetchall()
    if groups:
        groups = groups[0]
    
    # Get Cursor
    cur4 = conn.cursor()
    
    cur4.execute("SELECT pkgname, version FROM depends D \
        JOIN packages P ON D.depend_id = P.id \
        WHERE D.pkg_id = ? ORDER by pkgname", ([package_id]))
    for depend in cur4:
        if depend[1]:
            depends += [depend[0] + depend[1]]
        else:
            depends += [depend[0]]
            
    cur4.execute("SELECT pkgname FROM depends D \
        JOIN packages P ON D.pkg_id = P.id \
        WHERE D.depend_id = ? ORDER by pkgname", ([package_id]))
    for reverse_depend in cur4:
        reverse_depends += reverse_depend         

    # Get Cursor
    cur5 = conn.cursor()
    cur5.execute("SELECT license FROM licenses WHERE pkg_id = ?", ([package_id]))
    package_license = cur5.fetchall()
    if package_license:
        package_license = package_license[0][0]

        

    packages_as_dict[name] = {
        'name': name,
        'version' : version ,
        'desc' : desc ,
    }

    f = open(args.hugo_directory+'content/package/'+name+'.md', 'w')
    f.write("+++\n")
    f.write("draft = false\n")
    f.write('title = "'+name+" "+version+'"\n')
    f.write('version = "'+version+'"\n')
    f.write('description = "'+desc+'"\n')
    f.write('date = "'+builddate.isoformat()+'"\n')
    f.write('aliases = "/packages/'+str(package_id)+'"\n')

    f.write('categories = '+str(list(groups))+'\n')
    f.write('upstreamurl = "'+url+'"\n')
    f.write('arch = "'+arch+'"\n')
    f.write('size = "'+str(size)+'"\n')
    f.write('usize = "'+str(usize)+'"\n')
    f.write('sha1sum = "'+sha1sum+'"\n')
    f.write('depends = "'+str(depends)+'"\n')
    if reverse_depends:
        f.write('reverse_depends = "'+str(reverse_depends)+'"\n')
    
    if package_license:
        f.write('license = "'+str(package_license)+'"\n')
    
    f.write("+++\n")
    f.write(desc)
    f.write('{{< files text="show files" >}}')
    for file in files:
        f.write("* "+str(file)+"\n")
    f.write("{{< /files >}}")
    f.close()

if packages_as_dict:
    idx = lunr(
        ref='name', fields=('desc', 'version'), documents=packages_as_dict.values()
    )

    with open(args.json_path, 'w') as f:
        print(idx.serialize(), file=f)

