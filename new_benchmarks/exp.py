import os
import sys


if len(sys.argv) != 2 :
    print "usage: $python exp.py <name>"
    sys.exit()

exp_name = sys.argv[1]


# Run baseline 
# Set config  
os.system("python mod_and_upd.py 1 0 F")
# Run all benchmarks
#os.system("cd bfs")
os.chdir("bfs")
os.system("./BFS graph4096.txt &> " + exp_name + "_BFS_baseline.log")
os.chdir("..")
#os.system("cd ..")

#os.system("cd bfs2")
os.chdir("bfs2")
os.system("./BFS2 graph4096.txt &> " + exp_name + "_BFS2_baseline.log")
os.chdir("..")
#os.system("cd ..")

#os.system("cd hotsp")
os.chdir("hotsp")
os.system("HOTSP 30 6 40 ./result_30_6_40.txt &> " + exp_name + "_HOTSP_baseline.log")
os.chdir("..")
#os.system("cd ..")

#os.system("cd wp")
os.chdir("wp")
os.system("./WP < ./data/args &> " + exp_name + "_WP_baseline.log")
os.chdir("..")
#os.system("cd ..")

#os.system("cd GPU_Jacobi-s")
os.chdir("GPU_Jacobi-s")
os.system("./HW1 8 7 &> " + exp_name + "_JACOBI_baseline.log")
os.chdir("..")
#os.system("cd ..")

# for all benchmarks 
# for all settings 
# for all # of entries
# for two policies

