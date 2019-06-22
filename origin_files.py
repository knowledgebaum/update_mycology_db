import os
from pathlib import Path
####################
###ORIGIN TEXT FILES ###
####################

#PATHS
base_path = Path("C:/webDev/pycharm/matchmaker/data/origin_data/")

bir_path=os.path.join(base_path, "bir_origin.txt")
bol_path=os.path.join(base_path, "bol_Origin.txt")
clu_path=os.path.join(base_path, "clu_origin.txt")
cor_path=os.path.join(base_path, "cor_origin.txt")
cru_path=os.path.join(base_path, "cru_origin.txt")
cup_path=os.path.join(base_path, "cup_origin.txt")
gil_path=os.path.join(base_path, "gil_origin.txt")
jel_path=os.path.join(base_path, "jel_Origin.txt")
mor_path=os.path.join(base_path, "mor_origin.txt")
oth_path=os.path.join(base_path, "oth_Origin.txt")
pol_path=os.path.join(base_path, "pol_origin.txt")
puf_path=os.path.join(base_path, "puf_origin.txt")
too_path=os.path.join(base_path, "too_Origin.txt")
tru_path=os.path.join(base_path, "tru_origin.txt")
vei_path=os.path.join(base_path, "vei_origin.txt")



#LIST OF FILE VARS
list_origin_files = [bir_path,
                    bol_path,
                    clu_path,
                    cor_path,
                    cru_path,
                    cup_path,
                    gil_path,
                    jel_path,
                    mor_path,
                    oth_path,
                    pol_path,
                    puf_path,
                    too_path,
                    tru_path,
                    vei_path
]

list_column_values = [
14,18,17,18,10,18,18,10,18,10,18,18,18,18,18
]