#python 3.8.8
#win 10 64 bit
import os, time

if (False): #will be used on next
    print("Last modified: %s" % time.ctime(os.path.getmtime(v_namefile)))
    print("Created: %s" % time.ctime(os.path.getctime(v_namefile)))

#put new string[basis] for addstrren
#EXAMPLE
#1. addstr("namefile.txt","additional text")
#2. addstr(r"e:\folder\namefile.txt","additional text")
#TODO
#1. handle if symbol dot "." is not exist
#2. handle if symbol dot "." is exist but not extension for example more space "namefile . e xt"
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

