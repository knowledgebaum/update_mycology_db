import re
from origin_files import list_column_values, list_origin_files
from match_model import session, dict_to_sql


def regex_string_maker(col_nums):
    base_string = "([A-Z]{3,} [A-Z]{3,}|[A-Z]{3,})(  .*\\n)"
    end_string = ""
    for i in range(col_nums):
        end_string += base_string
    return end_string


def to_dict(matches):
    mushroom_list = []
    for match in matches:
        #Key = even
        #Value = odd
        match_list_even = match[0::2] #Even GROUPS
        match_list_odd = match[1::2]  #Odd GROUPS
        output = dict(zip(match_list_even, match_list_odd))
        dict_to_sql(output, session)
        #mushroom_list.append(output)
    return output



###Iterate Through Origin Files

for i in range(len(list_origin_files)):
    mycology_pattern = re.compile(regex_string_maker(list_column_values[i]), re.MULTILINE)
    matches = re.findall(mycology_pattern, list_origin_files[i])
    to_dict(matches)
    #dict_to_sql(myco_dict, session)















###########################
#########CUT###############
###########################

# ##SINGLE
# mycology_pattern = re.compile(regex_string_maker(14), re.MULTILINE)
#
# matches = re.findall(mycology_pattern, "C:\webDev\pycharm\matchmaker\data\origin_data\sed\\bir_origin.txt")
