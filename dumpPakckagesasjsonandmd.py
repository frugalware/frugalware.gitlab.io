#!/usr/bin/env python

import pacman
import json
import datetime
import argparse

parser = argparse.ArgumentParser(
                    prog='dumpPakckagesasjsonandmd.py',
                    description='Dump package description and metadata to .md files and JSON Index',
                    epilog='Here be dragons')

root = "/"
parser.add_argument('-d', '--package_directory', help="Directory containing fdb and fpm files", default=root+"var/cache/pacman-g2/pkg") 
parser.add_argument('-t', '--hugo_directory', help="Directory containing hugo", default="./")
parser.add_argument('-b', '--dbpath', help="Path to db")

args = parser.parse_args()
                    
packages_as_dict = {}
packages_path = args.package_directory

if pacman.initialize(root) == -1:
    print("initializing DB failed")
    exit

db = pacman.db_register("frugalware-current")

if 'dbpath' in args:
    pacman.set_option(pacman.OPT_DBPATH, pacman.char_to_unsigned_long(args.dbpath))

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


#    package_as_dict = {
#        'name' : name,
#        'version' : version ,
#        'desc' : pacman.void_to_char(pacman.pkg_getinfo(pkg, pacman.PKG_DESC)).decode('latin-1').encode("utf-8") ,
#        'groups' : groups,
#        'url' : url ,
#        'arch' : arch ,
#        'builddate' : pacman.void_to_char(pacman.pkg_getinfo(pkg, pacman.PKG_BUILDDATE)) ,
#        'size' : pacman.void_to_long(pacman.pkg_getinfo(pkg, pacman.PKG_SIZE)) ,
#        'usize' : pacman.void_to_long(pacman.pkg_getinfo(pkg, pacman.PKG_USIZE)) ,
#        'sha1sums' : pacman.void_to_char(pacman.pkg_getinfo(pkg, pacman.PKG_SHA1SUM)) ,
#        'depends' : depends ,
#        'license' : licenses,
#        'files' : files
#    }
#    packages_as_dict.append(package_as_dict)


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


    i = pacman.list_next(i)


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
#    if files:
#        f.write('files = "'+str(files)+'"\n')
    f.write("+++\n")
    f.write(desc)
    f.close()

with open(args.hugo_directory+'static/js/lunr/PagesIndex.json', 'w') as f:
    json.dump(list(packages_as_dict.values()), f, sort_keys=True, indent=4 * ' ')

pacman.release()