#python 3.8.8
#win 10 64 bit
import os, time, glob

if (False): #will be used on next
    print("Last modified: %s" % time.ctime(os.path.getmtime(v_namefile)))
    print("Created: %s" % time.ctime(os.path.getctime(v_namefile)))

#put new string[basis] for addsros
#EXAMPLE
#1. addstr("namefile.txt","additional text")
#2. addstr(r"e:\folder\namefile.txt","additional text")
#TODO
#1. handle if symbol dot "." is not exist
#2. handle if symbol dot "." is exist but not extension for example more space "namefile . e xt"
#3. now only put before extension, next can be choose beginning or end name file
def addstr(v_namefile,v_add_info,v_bool_is_ext = True):
    #to add space if add info is exist. is it necessary?
    v_add_info_raw = ""
    if (len(v_add_info)>0):
        v_add_info_raw = " "
    v_add_info_raw += v_add_info

    #put before . extension file, if v_bool_is_ext is true
    if (v_bool_is_ext):
        v_temp = v_namefile.rpartition(".")
        v_res = v_temp[0]  + v_add_info_raw + v_temp[1] + v_temp[2]
    else:
        v_res = v_namefile + v_add_info_raw
    return v_res

#abbrev from "add string rename OS"
#put new string and rename
#EXAMPLE is same with func addstr(v_namefile,v_add_info,v_bool_is_ext = True):
#TODO
#1. handle error if file not exist or other kind error file
def addsros(v_namefile,v_add_info,v_bool_is_ext = True):
    v_res = addstr(v_namefile,v_add_info,v_bool_is_ext)
    os.rename(v_namefile,v_res)

#TODO func
#1. to add meta data on current directory(subfolder not include)
#2. to add meta data on one chosen folder(subfolder not include)
#3. same as 1 and 2, but recursive on subfolder too
#4. same as 1, 2, and 3, but use wildcard too
#5. same as all num before, but can choose to rename file only or folder only or both of them

#abbrev from "get list" file and/or folder
#PARAM
#1. v_both = [ -1 = "Folder Only", 0 = "Both Folder File", 1 = "File only" ]
#   determine which one need to be add meta data on name file
#EXAMPLE
#PROGRESS
#1. testing currect dir
#ISSUE
#1. .nomedia not detect as file?
#TODO
def getls(v_name_dir = "",v_is_recursive=False,v_both = 1,v_wildcard = r"*" ):
    v_ls_file = glob.glob(os.getcwd()+r'\*')
    if (v_both == 1):
        v_ls_file = [f for f in v_ls_file if os.path.isfile(f)]
    return v_ls_file

#abbrev from "add string rename dir OS"
def addsrdiros(v_add_info="",v_name_dir="",v_bool_is_ext = True,v_is_recursive=False,v_both = 1,v_wildcard = r"*" ):
    v_ls_file = getls(v_name_dir,v_is_recursive,v_both,v_wildcard )
    for itm_ls in v_ls_file:
        addsros(itm_ls,v_add_info,v_bool_is_ext)

#1st testing
#print(getls())
#addsrdiros("sent")
#print(getls())
