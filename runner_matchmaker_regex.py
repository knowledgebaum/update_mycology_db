import re
from origin_files import list_column_values, list_origin_files
from match_model import session, dict_to_sql


def regex_string_maker(col_nums):
    base_string = "([A-Z]{3,} [A-Z]{3,}|[A-Z]{3,})(  .*\n)"

    # Python is pretty sweet
    # if you do "this" * 4
    # you get back
    # In [1]: "this" * 4
    # Out[1]: 'thisthisthisthis'

    # So we can short cut this method by
    # just doing the base string * the cols

    return base_string * col_nums


def to_dict(matches):
    mushroom_list = []
    for match in matches:
        # Key = even
        # Value = odd
        match_list_even = match[0::2]  # Even GROUPS
        match_list_odd = match[1::2]  # Odd GROUPS
        output = dict(zip(match_list_even, match_list_odd))
        dict_to_sql(output, session)
        #mushroom_list.append(output)
        print(match_list_even)

    #return mushroom_list


###Iterate Through Origin Files


# Make this a method so we can call it in debugging
def matching():
    for i in range(len(list_origin_files)):
        regex_string = regex_string_maker(list_column_values[i])
        mycology_pattern = re.compile(regex_string, re.MULTILINE)

        print(mycology_pattern)

        # I think you are getting off track here.
        # I *think* you were trying to get the content of the file
        # and here you are getting the name of the file
        #
        # Thus, the regex pattern you have going for your matches will not match anything
        this_is_the_file_name = list_origin_files[i]
        print(this_is_the_file_name)

        with open(list_origin_files[i]) as content_file:
            #import pudb

            #pudb.set_trace()
            content = content_file.read()
            matches = re.findall(mycology_pattern, content)

            # This line doesnt do anything by the way
            to_dict(matches)
            print("=" * 10)
            print(matches)
            print("=" * 10)
            # dict_to_sql(myco_dict, session)


matching()

###########################
#########CUT###############
###########################

# ##SINGLE
# mycology_pattern = re.compile(regex_string_maker(14), re.MULTILINE)
#
# matches = re.findall(mycology_pattern, "C:\webDev\pycharm\matchmaker\data\origin_data\sed\\bir_origin.txt")
