import re
import os

os.chdir('/media/robbinsr/a94ffb60-544f-46c2-874c-bab46457fdb6/robbinsr_/' +
         'Projects/p_projects/nhis_exploratory/nhis_2014_injpoiep')

custom_parser_input_file_name = "nhis_2014_injpoiep.dat"
custom_parser_program_file_name = "nhis_2014_injpoiep_parser.py"
custom_parser_output_file_name = "nhis_2014_injpoiep.csv"
element_names_file_name = 'nhis_2014_injpoiep_element_names.txt'
element_positions_file_name = "nhis_2014_injpoiep_element_positions.txt"
error_log_file_name = "nhis_2014_injpoiep_write_parser_log.txt"

error_log_file_writer = open(error_log_file_name, mode='w', encoding='utf8')

error_message_1 = "Error -- Reference Error Number: "
error_message_2 = "Please read log file named {}".format(error_log_file_name)
error_message_3 = "If necessary contact russ.robbins@outlook.com"

exit = False


# noinspection PyShadowingNames,PyUnusedLocal,PyUnusedLocal
def confirm_widest_data_line_equals_largest_element_position(
        custom_parser_input_file_n,
        element_positions_file_n):
    """
    :param custom_parser_input_file_n: str
    :param element_positions_file_n: str
    :return: result: bool
    """
    custom_parser_input_f_n = custom_parser_input_file_n
    element_positions_f_n = element_positions_file_n

    with open(custom_parser_input_f_n, mode='r',
              encoding='utf8') as custom_parser_i_f_n:
        with open(element_positions_f_n, mode='r',
                  encoding='utf8') as element_p_f_n:

            highest_position = 0
            result = None
            for line in element_p_f_n:
                temp = line.strip('\ufeff')
                temp2 = temp.strip(' ')
                match = re.search('([0-9]+)(-)([0-9]+)', temp2)
                if match is not None:
                    if match.group(3):
                        if highest_position < int(match.group(3)):
                            highest_position = int(match.group(3))
                        elif highest_position >= int(match.group(3)):
                            pass
                        else:
                            # noinspection PyShadowingNames,PyShadowingNames
                            custom_error_message = error_message_1 + " 1"
                            print(custom_error_message)
                            print(error_message_2)
                            print(error_message_3)
                            error_log_file_writer.write(
                                custom_error_message + '\n')
                            error_log_file_writer.write(error_message_2 + '\n')
                            error_log_file_writer.write(error_message_3 + '\n')
                            exit = True
                            SystemExit(error_message_2)

                    elif not match.group(3):
                        custom_error_message = error_message_1 + " 2"
                        print(custom_error_message)
                        print(error_message_2)
                        print(error_message_3)
                        error_log_file_writer.write(custom_error_message + '\n')
                        error_log_file_writer.write(error_message_2 + '\n')
                        error_log_file_writer.write(error_message_3 + '\n')
                        exit = True
                        SystemExit(error_message_2)

                    else:
                        custom_error_message = error_message_1 + " 3"
                        print(custom_error_message)
                        print(error_message_2)
                        print(error_message_3)
                        error_log_file_writer.write(custom_error_message + '\n')
                        error_log_file_writer.write(error_message_2 + '\n')
                        error_log_file_writer.write(error_message_3 + '\n')
                        exit = True
                        SystemExit(error_message_2)

                elif match is None:

                    if highest_position < int(line):
                        highest_position = int(line)
                    else:
                        custom_error_message = error_message_1 + " 4"
                        print(custom_error_message)
                        print(error_message_2)
                        print(error_message_3)
                        error_log_file_writer.write(custom_error_message + '\n')
                        error_log_file_writer.write(error_message_2 + '\n')
                        error_log_file_writer.write(error_message_3 + '\n')
                        exit = True
                        SystemExit(error_message_2)

                else:
                    custom_error_message = error_message_1 + " 5"
                    print(custom_error_message)
                    print(error_message_2)
                    print(error_message_3)
                    error_log_file_writer.write(custom_error_message + '\n')
                    error_log_file_writer.write(error_message_2 + '\n')
                    error_log_file_writer.write(error_message_3 + '\n')
                    exit = True
                    SystemExit(error_message_2)

            for idx, line in enumerate(custom_parser_i_f_n):
                width = len(line) - 1
                if width == highest_position:
                    result = True
                    break
                elif width != highest_position:
                    result = False
                else:
                    custom_error_message = error_message_1 + " 6"
                    print(custom_error_message)
                    print(error_message_2)
                    print(error_message_3)
                    error_log_file_writer.write(custom_error_message + '\n')
                    error_log_file_writer.write(error_message_2 + '\n')
                    error_log_file_writer.write(error_message_3 + '\n')
                    exit = True
                    SystemExit(error_message_2)

            return result


# noinspection PyShadowingNames,PyUnusedLocal
def confirm_names_and_positions_files_same_length(element_names_file_n,
                                                  element_positions_file_n):
    """
    :param element_names_file_n: str
    :param element_positions_file_n: str
    :return: bool
    """
    element_names_f_n = element_names_file_n
    element_positions_f_n = element_positions_file_n
    with open(element_names_f_n, mode="r",
              encoding="utf8") as element_names_f:
        with open(element_positions_f_n, mode="r",
                  encoding="utf8") as element_positions_f:
            result = None
            element_names_list = []
            element_positions_list = []
            for line in element_names_f:
                temp = line.strip()
                element_names_list.append(temp)
            for line in element_positions_f:
                temp = line.strip('\ufeff')
                temp2 = temp.strip(' ')
                element_positions_list.append(temp2)
            names_list_length = len(element_names_list)
            positions_list_length = len(element_positions_list)
            if names_list_length != positions_list_length:
                result = False
            elif names_list_length == positions_list_length:
                result = True
            else:
                custom_error_message = error_message_1 + " 7"
                print(custom_error_message)
                print(error_message_2)
                print(error_message_3)
                error_log_file_writer.write(custom_error_message + '\n')
                error_log_file_writer.write(error_message_2 + '\n')
                error_log_file_writer.write(error_message_3 + '\n')
                exit = True
                SystemExit(error_message_2)

    return result


common_statements_custom_parsers_list = [
    'import pandas as pd',
    'import numpy as np',
    'with open(custom_parser_input_file_name, encoding="utf8", mode="r") as f:',
    'for ldx, line in enumerate(f):',
    'if ldx < 20:',
    'for cdx, char in enumerate(line):',
    'else:',
    'if char == \'\\n\':',
    'pass',
    'else:',
    'print("Problem: Email russ.robbins@outlook.com")',
    'df = pd.DataFrame(columns=(',
    '))',
    'for i in range(20):',
    'df.loc[i] = [',
    ']',
    'df = df.applymap(lambda x: np.nan if str(x).isspace() else x)'
]


def capture_element_names_in_list(element_names_file_n):
    """
    Read element names from file, place in list, and return list.
    :param element_names_file_n: str
    :return: bool
    """
    element_names_f_n = element_names_file_n
    with open(element_names_f_n, mode='r', encoding='utf8') as element_n_f_n:
        element_names = []
        for element_name in element_n_f_n:
            temp = element_name.strip('\ufeff')
            temp2 = temp.strip('\n')
            temp3 = temp2.strip(' ')
            match = re.search('[A-Z0-9_]+', temp3)
            if match is not None:
                e_name = str(match.group(0))
                element_names.append(e_name)
        return element_names


def build_element_value_container_declaration_list(element_names_l):
    """
    Build list of declarations to store individual element values.
    :param element_names_l: list
    :return: list
    """
    element_n_l = element_names_l
    element_value_container_declarations = []
    assert isinstance(element_names_l, list)
    for element_name in element_n_l:
        suffix = " = ''"
        element_value_container_declaration = "{}{}".format(element_name,
                                                            suffix)
        element_value_container_declarations.append(
            element_value_container_declaration)
    return element_value_container_declarations


def build_element_values_container_declaration_list(element_names_l):
    """
    Build declarations for lists that store values for each element.
    :param element_names_l: list
    :return: list
    """
    element_n_l = element_names_l
    assert isinstance(element_n_l, list)
    element_values_container_declarations = []
    for element_name in element_n_l:
        suffix = "_LIST = []"
        element_values_container_declaration = "{}{}".format(element_name,
                                                             suffix)
        element_values_container_declarations.append(
            element_values_container_declaration)
    return element_values_container_declarations


def build_element_value_chars_accumulator_declarations(element_names_l):
    """
    Build declarations for lists that accumulate chars \
    that when combined represent distinct element values.
    :param element_names_l: list
    :return: list
    """
    element_n_l = element_names_l
    assert isinstance(element_n_l, list)
    element_value_chars_accumulator_declarations = []
    for element_name in element_n_l:
        suffix = "_accumulator_LIST = []"
        element_value_chars_accumulator_declaration = "{}{}".format(
            element_name, suffix)
        element_value_chars_accumulator_declarations.append(
            element_value_chars_accumulator_declaration)
    return element_value_chars_accumulator_declarations


# noinspection PyShadowingNames,PyUnusedLocal
def build_position_based_condition_blocks_list(element_names_l,
                                               element_positions_file_n):
    """
    Build condition blocks that select values from each line for an element.
    :param element_names_l: list
    :param element_positions_file_n: list
    :return: list
    """
    element_n_l = element_names_l
    element_positions_f_n = element_positions_file_n
    with open(element_positions_f_n, mode='r',
              encoding='utf8') as element_p_f_n:
        element_positions = []
        condition_blocks = []
        for i, position in enumerate(element_p_f_n):
            temp = position.strip('\ufeff')
            position = temp.strip('\n')
            element_positions.append(position)

            elseif = 'elif '
            colon = ':'

            match1 = re.search('([0-9]+)(-*)([0-9]*)', position)
            if match1 is not None:
                if match1.group(1) is not None:
                    condition_block = []
                    if match1.group(2) is "-":
                        part_one = int(match1.group(1)) - 2
                        part_two = ' < cdx < '
                        part_three = int(match1.group(3))
                        if i == 0:
                            condition_block_line_1 = "if {}{}{}{}".format(
                                part_one, part_two, part_three, colon)
                            condition_block.append(condition_block_line_1)
                        elif i != 0:
                            condition_block_line_1 = "{}{}{}{}{}".format(
                                elseif,
                                part_one,
                                part_two,
                                part_three,
                                colon)
                            condition_block.append(condition_block_line_1)
                        else:
                            custom_error_message = error_message_1 + " 8"
                            print(custom_error_message)
                            print(error_message_2)
                            print(error_message_3)
                            error_log_file_writer.write(
                                custom_error_message + '\n')
                            error_log_file_writer.write(error_message_2 + '\n')
                            error_log_file_writer.write(error_message_3 + '\n')
                            exit = True
                            SystemExit(error_message_2)

                        condition_blocks.append(condition_block)

                    elif match1.group(2) is not '-':
                        part_one = int(match1.group(1)) - 2
                        part_two = ' < cdx < '
                        part_three = int(match1.group(1))
                        condition_block_line_1 = "{}{}{}{}{}".format(elseif,
                                                                     part_one,
                                                                     part_two,
                                                                     part_three,
                                                                     colon)
                        condition_block.append(condition_block_line_1)
                        condition_blocks.append(condition_block)

                    else:
                        custom_error_message = error_message_1 + " 9"
                        print(custom_error_message)
                        print(error_message_2)
                        print(error_message_3)
                        error_log_file_writer.write(custom_error_message + '\n')
                        error_log_file_writer.write(error_message_2 + '\n')
                        error_log_file_writer.write(error_message_3 + '\n')
                        exit = True
                        SystemExit(error_message_2)

                else:
                    custom_error_message = error_message_1 + " 10"
                    print(custom_error_message)
                    print(error_message_2)
                    print(error_message_3)
                    error_log_file_writer.write(custom_error_message + '\n')
                    error_log_file_writer.write(error_message_2 + '\n')
                    error_log_file_writer.write(error_message_3 + '\n')
                    exit = True
                    SystemExit(error_message_2)

        for i, block in enumerate(condition_blocks):
            spaces_ = u'\u0020' * 4
            part_one = element_n_l[i]
            part_two = '_accumulator_LIST.append(char)'
            condition_block_line_2 = "{}{}{}".format(spaces_, part_one,
                                                     part_two)

            block.append(condition_block_line_2)
            part_three = element_n_l[i]
            part_four = " = ''.join("
            part_five = element_n_l[i]
            part_six = '_accumulator_LIST)'
            condition_block_line_3 = "{}{}{}{}{}".format(spaces_, part_three,
                                                         part_four, part_five,
                                                         part_six)
            block.append(condition_block_line_3)

    return condition_blocks


def build_element_values_container_append_fragments_list(element_names_l):
    """
    Build set of fragment expressions. \
    Each full expression will append element values to element value lists.
    :param element_names_l: list
    :return: list
    """
    element_n_l = element_names_l
    assert isinstance(element_n_l, list)
    infix1 = "_LIST"
    infix2 = '.append('
    suffix = ')'
    element_values_container_append_fragments = []
    for element_name in element_n_l:
        element_values_container_append_fragment = '{}{}{}{}{}'.format(
            element_name, infix1, infix2,
            element_name, suffix)
        assert isinstance(element_values_container_append_fragment, str)
        element_values_container_append_fragments.append(
            element_values_container_append_fragment)
    return element_values_container_append_fragments


def build_dataframe_column_declarations_list(element_names_l):
    """
    Build list of element names (with quotes and followed by comma),\
    to use in dataframe declaration.
    :param element_names_l: list
    :return: list
    """
    element_n_l = element_names_l
    assert isinstance(element_n_l, list)
    prefix = "'"
    suffix = "',"
    dataframe_column_declarations = []
    for element_name in element_n_l:
        dataframe_column_declaration = '{}{}{}'.format(prefix, element_name,
                                                       suffix)
        dataframe_column_declarations.append(dataframe_column_declaration)

    list_length = len(dataframe_column_declarations)
    temp = dataframe_column_declarations[list_length - 1]
    temp2 = temp.strip(',')
    dataframe_column_declarations[list_length - 1] = temp2

    return dataframe_column_declarations


def build_dataframe_row_column_cell_insert_list(element_names_l):
    """
    Build list of expression fragments to insert one value \
    from a list of element values into dataframe row col cell.
    :param element_names_l: list
    :return: list
    """
    element_n_l = element_names_l
    assert isinstance(element_n_l, list)
    suffix = "_LIST[i],"
    dataframe_row_column_cell_insert_fragments = []
    for element_name in element_n_l:
        dataframe_row_column_cell_insert_fragment = '{}{}'.format(element_name,
                                                                  suffix)
        dataframe_row_column_cell_insert_fragments.append(
            dataframe_row_column_cell_insert_fragment)

    list_length = len(dataframe_row_column_cell_insert_fragments)
    temp = dataframe_row_column_cell_insert_fragments[list_length - 1]
    temp2 = temp.strip(',')
    dataframe_row_column_cell_insert_fragments[list_length - 1] = temp2

    return dataframe_row_column_cell_insert_fragments


# noinspection PyShadowingNames
def parser_writer(custom_parser_program_file_n,
                  custom_parser_input_file_n,
                  custom_parser_output_file_n,
                  common_statements_custom_parsers_l,
                  exit
                  ):
    """
    :param custom_parser_program_file_n: str
    :param custom_parser_input_file_n: str
    :param custom_parser_output_file_n: str
    :param common_statements_custom_parsers_l: list
    :param exit: bool
    :rtype: None
    """

    exit = exit
    custom_parser_program_f_n = custom_parser_program_file_n
    custom_parser_input_f_n = custom_parser_input_file_n
    custom_parser_output_f_n = custom_parser_output_file_n
    common_statements_custom_p_l = common_statements_custom_parsers_l

    names_positions_files_same_length = \
        confirm_names_and_positions_files_same_length(
            element_names_file_name,
            element_positions_file_name)

    if names_positions_files_same_length is True:
        pass
    elif names_positions_files_same_length is False:
        custom_error_message = \
            "System Exiting Names and Positions File Lengths Not Equal"
        print(custom_error_message)
        print(error_message_2)
        print(error_message_3)
        error_log_file_writer.write(custom_error_message + '\n')
        error_log_file_writer.write(error_message_2 + '\n')
        error_log_file_writer.write(error_message_3 + '\n')
        exit = True
        SystemExit(custom_error_message)
    elif names_positions_files_same_length is None:
        custom_error_message = error_message_1 + " 11"
        print(custom_error_message)
        print(error_message_2)
        print(error_message_3)
        error_log_file_writer.write(custom_error_message + '\n')
        error_log_file_writer.write(error_message_2 + '\n')
        error_log_file_writer.write(error_message_3 + '\n')
        exit = True
        SystemExit(error_message_2)
    else:
        custom_error_message = error_message_1 + " 12"
        print(custom_error_message)
        print(error_message_2)
        print(error_message_3)
        error_log_file_writer.write(custom_error_message + '\n')
        error_log_file_writer.write(error_message_2 + '\n')
        error_log_file_writer.write(error_message_3 + '\n')
        exit = True
        SystemExit(error_message_2)

    widest_data_line_equals_largest_element_position = \
        confirm_widest_data_line_equals_largest_element_position(
            custom_parser_input_file_name,
            element_positions_file_name)

    if widest_data_line_equals_largest_element_position is True:
        pass
    elif widest_data_line_equals_largest_element_position is False:
        custom_error_message = \
            "Error: Widest Data Line != Largest Element Position"
        print(custom_error_message)
        print(error_message_2)
        print(error_message_3)
        error_log_file_writer.write(custom_error_message + '\n')
        error_log_file_writer.write(error_message_2 + '\n')
        error_log_file_writer.write(error_message_3 + '\n')
        exit = True
        SystemExit(custom_error_message)
    else:
        custom_error_message = error_message_1 + " 13"
        print(custom_error_message)
        print(error_message_2)
        print(error_message_3)
        error_log_file_writer.write(custom_error_message + '\n')
        error_log_file_writer.write(error_message_2 + '\n')
        error_log_file_writer.write(error_message_3 + '\n')
        exit = True
        SystemExit(error_message_2)

    if exit is False:

        element_names_list = capture_element_names_in_list(
            element_names_file_name)

        element_value_container_declaration_list = \
            build_element_value_container_declaration_list(
                element_names_list)

        element_values_container_declaration_list = \
            build_element_values_container_declaration_list(
                element_names_list)

        element_value_chars_accumulator_declarations_list = \
            build_element_value_chars_accumulator_declarations(
                element_names_list)

        position_based_condition_blocks_list = \
            build_position_based_condition_blocks_list(
                element_names_list,
                element_positions_file_name)

        element_values_container_append_list = \
            build_element_values_container_append_fragments_list(
                element_names_list)

        dataframe_column_declarations_list = \
            build_dataframe_column_declarations_list(
                element_names_list)

        dataframe_row_column_cell_insert_list = \
            build_dataframe_row_column_cell_insert_list(
                element_names_list)

        element_value_container_declaration_l = \
            element_value_container_declaration_list
        element_values_container_declaration_l = \
            element_values_container_declaration_list
        element_value_chars_accumulator_declarations_l = \
            element_value_chars_accumulator_declarations_list
        position_based_condition_blocks_l = \
            position_based_condition_blocks_list
        element_values_container_append_fragments_l = \
            element_values_container_append_list
        dataframe_column_declarations_l = \
            dataframe_column_declarations_list
        dataframe_row_column_cell_insert_l = \
            dataframe_row_column_cell_insert_list

        with open(custom_parser_program_f_n, mode="w",
                  encoding="utf8") as custom_parser_program_writer:
            for idx, line in enumerate(common_statements_custom_p_l):
                if idx < 2:
                    custom_parser_program_writer.write(line + '\n')
                else:
                    pass

            custom_parser_program_writer.write('\n')

            custom_parser_program_writer.write(
                "custom_parser_input_file_name = " + '"' +
                custom_parser_input_f_n + '"' + '\n')

            custom_parser_program_writer.write('\n')

            for declaration in element_value_container_declaration_l:
                custom_parser_program_writer.write(declaration + '\n')

            custom_parser_program_writer.write('\n')

            for declaration in element_values_container_declaration_l:
                custom_parser_program_writer.write(declaration + '\n')

            custom_parser_program_writer.write('\n')

            for idx, line in enumerate(common_statements_custom_p_l):
                if 1 < idx < 3:
                    custom_parser_program_writer.write(line + '\n')
                else:
                    pass

            spaces = u'\u0020' * 4

            for idx, line in enumerate(common_statements_custom_p_l):
                if 2 < idx < 4:
                    custom_parser_program_writer.write(spaces + line + '\n')
                else:
                    pass

            spaces = u'\u0020' * 8

            for idx, line in enumerate(common_statements_custom_p_l):
                if 3 < idx < 5:
                    custom_parser_program_writer.write(spaces + line + '\n')
                else:
                    pass

            spaces = u'\u0020' * 12

            for declaration in element_value_chars_accumulator_declarations_l:
                custom_parser_program_writer.write(spaces + declaration + '\n')

            custom_parser_program_writer.write('\n')

            spaces = u'\u0020' * 12

            for idx, line in enumerate(common_statements_custom_p_l):
                if 4 < idx < 6:
                    custom_parser_program_writer.write(spaces + line + '\n')
                else:
                    pass

            spaces = u'\u0020' * 16

            for condition_block in position_based_condition_blocks_l:
                for line in condition_block:
                    custom_parser_program_writer.write(spaces + line + '\n')

            spaces = u'\u0020' * 16

            for idx, line in enumerate(common_statements_custom_p_l):
                if 5 < idx < 7:
                    custom_parser_program_writer.write(spaces + line + '\n')
                else:
                    pass

            spaces = u'\u0020' * 20

            for idx, line in enumerate(common_statements_custom_p_l):
                if 6 < idx < 8:
                    custom_parser_program_writer.write(spaces + line + '\n')
                else:
                    pass

            spaces = u'\u0020' * 24

            for idx, line in enumerate(common_statements_custom_p_l):
                if 7 < idx < 9:
                    custom_parser_program_writer.write(spaces + line + '\n')
                else:
                    pass

            spaces = u'\u0020' * 20

            for idx, line in enumerate(common_statements_custom_p_l):
                if 8 < idx < 10:
                    custom_parser_program_writer.write(spaces + line + '\n')
                else:
                    pass

            spaces = u'\u0020' * 24

            for idx, line in enumerate(common_statements_custom_p_l):
                if 9 < idx < 11:
                    custom_parser_program_writer.write(spaces + line + '\n')
                else:
                    pass

            custom_parser_program_writer.write('\n')

            spaces = u'\u0020' * 8

            for fragment in element_values_container_append_fragments_l:
                custom_parser_program_writer.write(spaces + fragment + '\n')

            custom_parser_program_writer.write('\n')

            for idx, line in enumerate(common_statements_custom_p_l):
                if 10 < idx < 12:
                    custom_parser_program_writer.write(line + '\n')
                else:
                    pass

            spaces = u'\u0020' * 28

            for declaration in dataframe_column_declarations_l:
                custom_parser_program_writer.write(spaces + declaration + '\n')

            spaces = u'\u0020' * 36

            for idx, line in enumerate(common_statements_custom_p_l):
                if 11 < idx < 13:
                    custom_parser_program_writer.write(spaces + line + '\n')
                else:
                    pass

            custom_parser_program_writer.write('\n')

            for idx, line in enumerate(common_statements_custom_p_l):
                if 12 < idx < 14:
                    custom_parser_program_writer.write(line + '\n')
                else:
                    pass

            spaces = u'\u0020' * 4

            for idx, line in enumerate(common_statements_custom_p_l):
                if 13 < idx < 15:
                    custom_parser_program_writer.write(spaces + line + '\n')
                else:
                    pass

            spaces = u'\u0020' * 20

            for insert in dataframe_row_column_cell_insert_l:
                custom_parser_program_writer.write(spaces + insert + '\n')

            spaces = u'\u0020' * 36

            for idx, line in enumerate(common_statements_custom_p_l):
                if 14 < idx < 16:
                    custom_parser_program_writer.write(spaces + line + '\n')
                else:
                    pass

            for idx, line in enumerate(common_statements_custom_p_l):
                if 15 < idx < 17:
                    custom_parser_program_writer.write(line + '\n')
                else:
                    pass

            custom_parser_program_writer.write(
                "df.to_csv(" + '"' + custom_parser_output_f_n + '")' + '\n')

            message1 = "{} written. Please check {} as well.".format(
                custom_parser_program_file_name, error_log_file_name)
            message2 = "If necessary, contact russ.robbins@outlook.com"
            message3 = "No errors are known to have occurred."
            print(message1)
            print(message2)
            print(message3)
            error_log_file_writer.write(message1 + '\n')
            error_log_file_writer.write(message2 + '\n')
            error_log_file_writer.write(message3 + '\n')

    return None


parser_writer(custom_parser_program_file_name,
              custom_parser_input_file_name,
              custom_parser_output_file_name,
              common_statements_custom_parsers_list,
              exit
              )

error_log_file_writer.close()
