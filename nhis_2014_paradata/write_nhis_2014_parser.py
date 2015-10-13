import re
import os

os.chdir(
    '/media/robbinsr/a94ffb60-544f-46c2-874c-bab46457fdb6/robbinsr_/Projects/p_projects/nhis_exploratory/nhis_2014_paradata')

data_elements_names_file = 'nhis_2014_paradata_element_names.txt'
element_positions_file_name = "nhis_2014_paradata_element_positions.txt"
template_program_file_name = "write_nhis_2014_parser_template.txt"
resulting_program_input_file_name = "nhis_2014_paradata.dat"
resulting_program_file_name = "nhis_2014_paradata_parser.py"
resulting_program_output_file_name = "nhis_2014_paradata_data.csv"


def capture_element_names_in_list(elements_names_file):
    with open(elements_names_file, mode='r', encoding='utf8') as element_names_f:
        element_names = []
        element_n_f = element_names_f
        for element_name in element_n_f:
            temp = element_name.strip('\ufeff')
            e_name = temp.strip('\n')
            element_names.append(e_name)
        return element_names


element_names_list = capture_element_names_in_list(data_elements_names_file)


def build_list_of_element_name_string_declarations(element_names_l):
    element_names = element_names_l
    e_name_decls = []
    assert isinstance(element_names, list)
    for element_name in element_names:
        suffix = " = ''"
        e_name_decl = "{}{}".format(element_name, suffix)
        e_name_decls.append(e_name_decl)
    return e_name_decls


element_name_decls = build_list_of_element_name_string_declarations(element_names_list)


# print(element_value_container_declaration_list)


def build_list_of_element_values_list_declarations(element_names_l):
    """
    """
    element_names = element_names_l
    assert isinstance(element_names, list)
    e_values_list_decls = []
    for element_name in element_names:
        suffix = "_LIST = []"
        element_values_list_decl = "{}{}".format(element_name, suffix)
        e_values_list_decls.append(element_values_list_decl)
    return e_values_list_decls


element_values_list_decls = build_list_of_element_values_list_declarations(element_names_list)


def build_list_of_value_accumulator_list_declarations(element_names_l):
    element_n_l = element_names_l
    assert isinstance(element_n_l, list)
    e_value_accumulator_decls = []
    for element_name in element_n_l:
        suffix = "_accumulator_LIST = []"
        element_value_accumulator_decl = "{}{}".format(element_name, suffix)
        e_value_accumulator_decls.append(element_value_accumulator_decl)
    return e_value_accumulator_decls


element_value_accumulator_decls = build_list_of_value_accumulator_list_declarations(element_names_list)


def build_list_of_append_values_to_element_value_lists(element_names_l):
    element_n_l = element_names_l
    assert isinstance(element_n_l, list)
    infix1 = "_LIST"
    infix2 = '.append('
    suffix = ')'
    e_value_append_exprs = []
    for element_name in element_n_l:
        element_value_append_expr = '{}{}{}{}{}'.format(element_name, infix1, infix2, element_name, suffix)
        assert isinstance(element_value_append_expr, str)
        e_value_append_exprs.append(element_value_append_expr)
    return e_value_append_exprs


element_value_append_exprs = build_list_of_append_values_to_element_value_lists(element_names_list)


def build_list_of_dataframe_column_declarations(element_names_l):
    element_n_l = element_names_l
    assert isinstance(element_n_l, list)
    prefix = "'"
    suffix = "',"
    df_element_decls = []
    for element_name in element_n_l:
        dataframe_element_decl = '{}{}{}'.format(prefix, element_name, suffix)
        df_element_decls.append(dataframe_element_decl)

    list_length = len(df_element_decls)
    temp = df_element_decls[list_length - 1]
    temp2 = temp.strip(',')
    df_element_decls[list_length - 1] = temp2

    return df_element_decls


dataframe_element_decls = build_list_of_dataframe_column_declarations(element_names_list)


def build_list_of_dataframe_cell_insert_refs(element_names_l):
    element_n_l = element_names_l
    assert isinstance(element_n_l, list)
    suffix = "_LIST[i],"
    df_cell_insert_refs = []
    for element_name in element_n_l:
        dataframe_cell_insert_ref = '{}{}'.format(element_name, suffix)
        df_cell_insert_refs.append(dataframe_cell_insert_ref)

    list_length = len(df_cell_insert_refs)
    temp = df_cell_insert_refs[list_length - 1]
    temp2 = temp.strip(',')
    df_cell_insert_refs[list_length - 1] = temp2

    return df_cell_insert_refs


dataframe_cell_inserts = build_list_of_dataframe_cell_insert_refs(element_names_list)


def build_list_of_condition_blocks_for_element_position_line_reads(element_names_l, element_positions_f):
    e_n_l = element_names_l
    e_p_f = element_positions_f
    with open(e_p_f, mode='r', encoding='utf8') as element_positions_f:
        element_positions_l = []
        cond_blocks = []
        for i, position in enumerate(element_positions_f):
            temp = position.strip('\ufeff')
            position = temp.strip('\n')
            element_positions_l.append(position)

            ifelse = 'elif '
            ifelse_close = ':'

            match1 = re.search('([0-9]+)(-*)([0-9]*)', position)
            if match1 is not None:
                if match1.group(1) is not None:
                    cond_block = []
                    # print(match1.group(2))
                    if match1.group(2) is "-":
                        part_one = int(match1.group(1)) - 2
                        part_two = ' < cdx < '
                        part_three = int(match1.group(3))
                        if i == 0:
                            condition_block_line_1 = "if {}{}{}{}".format(part_one, part_two, part_three, ifelse_close)
                        else:
                            condition_block_line_1 = "{}{}{}{}{}".format(ifelse, part_one, part_two, part_three,
                                                                         ifelse_close)
                        # print(condition_block_line_1)
                        cond_block.append(condition_block_line_1)
                        cond_blocks.append(cond_block)

                    elif match1.group(2) is not '-':
                        part_one = int(match1.group(1)) - 2
                        part_two = ' < cdx < '
                        part_three = int(match1.group(1))
                        condition_block_line_1 = "{}{}{}{}{}".format(ifelse, part_one, part_two, part_three,
                                                                     ifelse_close)
                        # print(condition_block_line_1)
                        cond_block.append(condition_block_line_1)
                        cond_blocks.append(cond_block)
                else:
                    print("CASE NOT HANDLED 1")

        for i, block in enumerate(cond_blocks):
            spaces_ = u'\u0020' * 4
            part_one = e_n_l[i]
            part_two = '_accumulator_LIST.append(char)'
            condition_block_line_2 = "{}{}{}".format(spaces_, part_one, part_two)
            # print(condition_block_line_2)
            block.append(condition_block_line_2)
            part_three = e_n_l[i]
            part_four = " = ''.join("
            part_five = e_n_l[i]
            part_six = '_accumulator_LIST)'
            condition_block_line_3 = "{}{}{}{}{}".format(spaces_, part_three, part_four, part_five, part_six)
            block.append(condition_block_line_3)

    return cond_blocks


condition_blocks = build_list_of_condition_blocks_for_element_position_line_reads(element_names_list,
                                                                                  element_positions_file_name)


def build_list_of_template_program_statements(template_program_file):
    t_program_lines = []
    with open(template_program_file, mode="r", encoding='utf8') as template_program_f:
        for expr in template_program_f:
            t_program_lines.append(expr)

    return t_program_lines


template_program_statements = build_list_of_template_program_statements(template_program_file_name)

with open(resulting_program_file_name, mode="w", encoding="utf8") as f_parser:
    for idx, line in enumerate(template_program_statements):
        if idx < 2:
            f_parser.write(line)

    f_parser.write('\n')

    f_parser.write("input_data_FILE = " + '"' + resulting_program_input_file_name + '"' + '\n')

    f_parser.write('\n')

    for declaration in element_name_decls:
        f_parser.write(declaration + '\n')

    f_parser.write('\n')

    for declaration in element_values_list_decls:
        f_parser.write(declaration + '\n')

    f_parser.write('\n')

    for idx, line in enumerate(template_program_statements):
        if 1 < idx < 3:
            f_parser.write(line)

    spaces = u'\u0020' * 4

    for idx, line in enumerate(template_program_statements):
        if 2 < idx < 4:
            f_parser.write(spaces + line)

    spaces = u'\u0020' * 8

    for idx, line in enumerate(template_program_statements):
        if 3 < idx < 5:
            f_parser.write(spaces + line)

    spaces = u'\u0020' * 12

    for declaration in element_value_accumulator_decls:
        f_parser.write(spaces + declaration + '\n')

    f_parser.write('\n')

    spaces = u'\u0020' * 12

    for idx, line in enumerate(template_program_statements):
        if 4 < idx < 6:
            f_parser.write(spaces + line)

    spaces = u'\u0020' * 16

    for condition_block in condition_blocks:
        for line in condition_block:
            f_parser.write(spaces + line + '\n')

    spaces = u'\u0020' * 16

    for idx, line in enumerate(template_program_statements):
        if 5 < idx < 7:
            f_parser.write(spaces + line)

    spaces = u'\u0020' * 20

    for idx, line in enumerate(template_program_statements):
        if 6 < idx < 8:
            f_parser.write(spaces + line)

    spaces = u'\u0020' * 24

    for idx, line in enumerate(template_program_statements):
        if 7 < idx < 9:
            f_parser.write(spaces + line)

    spaces = u'\u0020' * 20

    for idx, line in enumerate(template_program_statements):
        if 8 < idx < 10:
            f_parser.write(spaces + line)

    spaces = u'\u0020' * 24

    for idx, line in enumerate(template_program_statements):
        if 9 < idx < 11:
            f_parser.write(spaces + line)

    f_parser.write('\n')

    spaces = u'\u0020' * 8

    for expression in element_value_append_exprs:
        f_parser.write(spaces + expression + '\n')

    f_parser.write('\n')

    for idx, line in enumerate(template_program_statements):
        if 10 < idx < 12:
            f_parser.write(line)

    spaces = u'\u0020' * 28

    for declaration in dataframe_element_decls:
        f_parser.write(spaces + declaration + '\n')

    spaces = u'\u0020' * 36

    for idx, line in enumerate(template_program_statements):
        if 11 < idx < 13:
            f_parser.write(spaces + line)

    f_parser.write('\n')

    for idx, line in enumerate(template_program_statements):
        if 12 < idx < 14:
            f_parser.write(line)

    spaces = u'\u0020' * 4

    for idx, line in enumerate(template_program_statements):
        if 13 < idx < 15:
            f_parser.write(spaces + line)

    spaces = u'\u0020' * 20

    for insert in dataframe_cell_inserts:
        f_parser.write(spaces + insert + '\n')

    spaces = u'\u0020' * 36

    for idx, line in enumerate(template_program_statements):
        if 14 < idx < 16:
            f_parser.write(spaces + line + '\n')

    for idx, line in enumerate(template_program_statements):
        if 15 < idx < 17:
            f_parser.write(line + '\n')

    f_parser.write("df.to_csv(" + '"' + resulting_program_output_file_name + '")' + '\n')
