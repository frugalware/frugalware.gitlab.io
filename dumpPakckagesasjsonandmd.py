#!/usr/bin/env python

import pacman
import json
import datetime
import argparse
from lunr import lunr

parser = argparse.ArgumentParser(
                    prog='dumpPakckagesasjsonandmd.py',
                    description='Dump package description and metadata to .md files and JSON Index',
                    epilog='Here be dragons')

root = "/"
parser.add_argument('-d', '--package_directory', help="Directory containing fdb and fpm files", default=root+"var/cache/pacman-g2/pkg") 
parser.add_argument('-t', '--hugo_directory', help="Directory containing hugo", default="./")
parser.add_argument('-j', '--json_path', help="Where to create index file", default="/pub/PagesIndex.json")
parser.add_argument('-b', '--dbpath', help="Path to db")
parser.add_argument('-n', '--dbname', help="Name of db", default="frugalware-current")

args = parser.parse_args()
                    
packages_as_dict = {}
packages_path = args.package_directory

if pacman.initialize(root) == -1:
    print("initializing DB failed")
    exit

if 'dbpath' in args:
    if pacman.set_option(pacman.OPT_DBPATH, pacman.char_to_unsigned_long(args.dbpath)) == -1:
        print("failed to set option DBPATH")
        exit

db = pacman.db_register(args.dbname)

i = pacman.db_getpkgcache(db)
while i :
    pkg = pacman.void_to_PM_PKG(pacman.list_getdata(i))
    name = pacman.void_to_char(pacman.pkg_getinfo(pkg, pacman.PKG_NAME))
    version = pacman.void_to_char(pacman.pkg_getinfo(pkg, pacman.PKG_VERSION))
    arch = pacman.void_to_char(pacman.pkg_getinfo(pkg, pacman.PKG_ARCH))
    files = None
    url = None
    builddate = None
    licenses = None

    groups = []
    j = pacman.void_to_PM_LIST(pacman.pkg_getinfo(pkg, pacman.PKG_GROUPS))
    while j:
        group = pacman.void_to_char(pacman.list_getdata(j))
        groups.append(group)
        j = pacman.list_next(j)

    depends = []
    k = pacman.void_to_PM_LIST(pacman.pkg_getinfo(pkg, pacman.PKG_DEPENDS))
    while k:
        depend = pacman.void_to_char(pacman.list_getdata(k))
        depends.append(depend)
        k = pacman.list_next(k)

    desc = pacman.void_to_char(pacman.pkg_getinfo(pkg, pacman.PKG_DESC))
    size = pacman.void_to_long(pacman.pkg_getinfo(pkg, pacman.PKG_SIZE))
    usize = pacman.void_to_long(pacman.pkg_getinfo(pkg, pacman.PKG_USIZE))
    sha1sum = pacman.void_to_char(pacman.pkg_getinfo(pkg, pacman.PKG_SHA1SUM))

    full_pkg = pacman.PKGp_new()
    package_path= packages_path + name + "-" + version + "-" + arch + ".fpm"

    if pacman.pkg_load(package_path, full_pkg) != -1:
        files = []
        licenses = []

        m = pacman.void_to_PM_LIST(pacman.pkg_getinfo(pacman.PKGp_to_PKG(full_pkg), pacman.PKG_FILES))
        while m:
            package_file = pacman.void_to_char(pacman.list_getdata(m))
            files.append(package_file)
            m = pacman.list_next(m)

        n = pacman.void_to_PM_LIST(pacman.pkg_getinfo(pacman.PKGp_to_PKG(full_pkg), pacman.PKG_LICENSE))
        while n:
            license = pacman.void_to_char(pacman.list_getdata(n))
            licenses.append(license)
            n = pacman.list_next(n)
        url = pacman.void_to_char(pacman.pkg_getinfo(pacman.PKGp_to_PKG(full_pkg), pacman.PKG_URL))
        builddate = pacman.void_to_char(pacman.pkg_getinfo(pacman.PKGp_to_PKG(full_pkg), pacman.PKG_BUILDDATE))


        packages_as_dict[name] = {
            'name': name,
            'version' : version ,
            'desc' : desc ,
        }
        if files:
            packages_as_dict[name]['files'] = files
        if url:
            packages_as_dict[name]['url'] = url
        if builddate:
            packages_as_dict[name]['builddate'] = builddate
        if licenses:
            packages_as_dict[name]['licenses'] = licenses

        f = open(args.hugo_directory+'content/package/'+name+'.md', 'w')
        f.write("+++\n")
        f.write("draft = false\n")
        f.write('title = "'+name+" "+version+'"\n')
        f.write('version = "'+version+'"\n')
        if builddate:
            date_object = datetime.datetime.strptime(builddate, '%c')
            f.write('date = "'+date_object.isoformat()+'"\n')

        f.write('categories = '+str(groups)+'\n')
        if url:
            f.write('upstreamurl = "'+url+'"\n')
        f.write('arch = "'+arch+'"\n')
        f.write('size = "'+str(size)+'"\n')
        f.write('usize = "'+str(usize)+'"\n')
        f.write('sha1sum = "'+sha1sum+'"\n')
        f.write('depends = "'+str(depends)+'"\n')
        if licenses:
            f.write('license = "'+str(license)+'"\n')
        if files:
            f.write('files = "'+str(files)+'"\n')
        f.write("+++\n")
        f.write(desc)
        f.close()

    i = pacman.list_next(i)

idx = lunr(
    ref='name', fields=('desc', 'version'), documents=packages_as_dict.values()
)

with open(args.json_path, 'w') as f:
    print(idx.serialize(), file=f)


pacman.release()
