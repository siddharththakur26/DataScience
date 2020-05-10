import re
import script_data_collection

# print("data collection is completed")
################################################ FUNCTION STARTS ################################################
def extract_specific_contents(contents, text_type):

    # DECLARE THE PATTERNS TO BE FOUND IN THE TEXT
    mda_regex = re.finditer(r"item\s\d(.|[.])(|[.])\smanagement", contents)
    qqdmr_regex = re.finditer(r"item\s\d(.|[.])(|[.])\squantitative", contents)
    rf_regex = re.finditer(r"item\s\d(.|[.])(|[.])\srisk\sfactors", contents)

    # print(mda_regex)
    # list_item_patterns=[]
    # counter=1
    start_index = ending_index = 0
    counter = 1
    ####################################################################################
    """
    COUNTER == 1
    THE FIRST MATCH IS FROM TABLE OF CONTENT.
    COUNTER == 2
    THE SECOND MATCH IS FROM THE SECTION ITSELF. THIS PROVIDES THE INITIAL INDEX OF THE SECTION
    """
    ####################################################################################
    if text_type == "mda":
        for match in mda_regex:
            if counter == 1:
                ending_index = match.start()
            if counter == 2:
                start_index = match.start()
            counter += 1
        # print(contents[start_index:start_index+30])
        # print(match)
    elif text_type == "qqdmr":
        for match in qqdmr_regex:
            if counter == 1:
                ending_index = match.start()
            if counter == 2:
                start_index = match.start()
            counter += 1
    elif text_type == "rf":
        for match in rf_regex:
            if counter == 1:
                ending_index = match.start()
            if counter == 2:
                start_index = match.start()
            counter += 1

    ####################################################################################
    ####################################################################################

    # FIND THE STRING WHERE THE WHOLE PROCESS NEEDS TO STOP
    """
    FOR EXAMPLE:
    ITEM 7 AND THEN COMES ITEM 8 OR ITEM 7A. THEREFORE, CREATE A PATTERN THAT MATCHES
    ITEM 8 OR ITEM 7A
    I.E.
    ITEM 7 BECOMES THE INITIAL STARTING POINT AND ITEM 7A OR ITEM 8 BECOMES THE ENDING POINT
    FOR A STRING
    """
    # CONCERNED STRING WHERE THE PATTERN EXIST
    end_content = contents[ending_index : ending_index + 500]
    item_ = re.finditer(r"item\s\d([.]|.)", end_content)
    counter = 1
    start_value = end_value = 0

    for match in item_:
        if counter == 2:
            start_value = match.start()
            end_value = match.end()
        counter += 1

    # PATTERN GENERATED
    end_section = end_content[start_value:end_value]

    # SECTION SELECTED
    contents = contents[start_index::]
    # print(contents)

    # MATCH THE END SECTION PATTERN
    end_regex = re.finditer(r"{}".format(end_section), contents)
    end_section_index = 0

    for match in end_regex:
        end_section_index = match.start()
        break

    return contents[:end_section_index]


################################################ END OF FUNCTION ################################################
total_links = len(script_data_collection.url_links) + 1

for i in range(1, total_links):
    f = open("sec_file_{}.txt".format(i), "r")
    string = f.read()
    # REMOVE UNWANTED SYMBOLS SUCH AS #@!%^&*()_- ETC
    temp = re.sub("[^a-zA-Z0-9'., ]", " ", string)
    # REMOVE UNWANTED SPACES
    temp = " ".join(temp.split())
    # REMOVE UNWANTED DOTS
    consequitivedots = re.compile(r"\.{3,}")
    temp = consequitivedots.sub("", temp)
    # CONVERT TEXT IN LOWER CASE
    contents = temp.lower()

    #########################################################################################################
    mda_content = extract_specific_contents(contents, "mda")
    qqdmr_content = extract_specific_contents(contents, "qqdmr")
    rf_content = extract_specific_contents(contents, "rf")
    file2write_mda = open("sec_file_mda_{}.txt".format(i), "w+", encoding="UTF-8")
    file2write_mda.write(mda_content)
    file2write_mda.close()
    file2write_qqdmr = open("sec_file_qqdmr_{}.txt".format(i), "w+", encoding="UTF-8")
    file2write_qqdmr.write(qqdmr_content)
    file2write_qqdmr.close()
    file2write_rf = open("sec_file_rf_{}.txt".format(i), "w+", encoding="UTF-8")
    file2write_rf.write(rf_content)
    file2write_rf.close()

