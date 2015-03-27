'''
Renaming tool for UITS

By Jeremy Mill 3-25-15
jeremymill@gmail.com

Licensed until the GPL v2.0
'''
#Import Statements
import os
import sys
#command line arg
walk_dir = sys.argv[1]
#check list
bad_chars = ["\\","/",":","*","?","\"","<",">","|","#","%","{","}","~","&"]
#going to add { } ~ &
#replacement dictionary
char_dict = {"\\":"_","/":"_",":":";","*":"^","?":"_","\"":"_","<":"_",">":"_","|":"_","#":"_","%":"_","{":"(","}":")","~":"-","&":"_and_"}

#Logfile
f_obj = open('rename_files.log','w')


def replace_all(name,dict):
    for i,j in dict.iteritems():
        name = name.replace(i,j)
    return name
    
for directory in os.walk(walk_dir):
    for name in directory[2]:
        FQ_name = os.path.join(directory[0],name)
        if any(x in name for x in bad_chars):
            f_obj.write("Bad Char found in "+FQ_name+"\n")
            new_name = replace_all(name,char_dict)
            new_FQ_name = os.path.join(directory[0],new_name)
            try:
                os.rename(FQ_name, new_FQ_name)
                f_obj.write("Replaced "+FQ_name+" with "+new_FQ_name+"\n")
            except OSError:
                f_obj.write("failed to replace"+FQ_name+" with "+new_FQ_name+"\n")
            
