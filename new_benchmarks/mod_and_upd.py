import os
import sys

#mod gpgpu_config 

if len(sys.argv) != 4 :
    print "usage: $python mod_and_upd.py <num_ntries> <if_open> <replace_pol>"
    sys.exit()

# open 
# add
num_entries = sys.argv[1]
if_open     = sys.argv[2] 
replace_pol = sys.argv[3]

if int(num_entries) <= 0 :
    print "Invalid number of entries "
    sys.exit()
if if_open != "0" and if_open != "1" :
    print "Invalid switch "
    sys.exit()
if replace_pol != "F" and replace_pol != "L" :
    print "Invalid replacement policy "
    sys.exit()


#RFC_config = "-gpgpu_cache:RFC  64:1:64,L:L:m:N:L,A:32:8,8"
RFC_config = "-gpgpu_cache:RFC  64:1:" + num_entries  + "," + replace_pol + ":L:m:N:L,A:32:8,8"
RFC_switch = "-gpgpu_cache_RFC_open "+ if_open 

# copy original 
os.system("cp ./o_gpgpusim.config ./gpgpusim.config") 

# append 
f = open("gpgpusim.config" , "a" )  
f.write(RFC_config)
f.write("\n")
f.write(RFC_switch)
f.close()

#update to all 
command = "./update_all_config.sh" 
os.system(command)


