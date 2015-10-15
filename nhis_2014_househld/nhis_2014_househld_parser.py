import pandas as pd
import numpy as np

custom_parser_input_file_name = "nhis_2014_househld.dat"

RECTYPE = ''
SRVY_YR = ''
HHX = ''
INTV_QRT = ''
INTV_MON = ''
WTIA_HH = ''
WTFA_HH = ''
LIVQRT = ''
NON_INTV = ''
ACPT_FAM = ''
REJ_FAM = ''
ACPT_PER = ''
REJ_PER = ''
ACPTCHLD = ''
REGION = ''
STRAT_P = ''
PSU_P = ''

RECTYPE_LIST = []
SRVY_YR_LIST = []
HHX_LIST = []
INTV_QRT_LIST = []
INTV_MON_LIST = []
WTIA_HH_LIST = []
WTFA_HH_LIST = []
LIVQRT_LIST = []
NON_INTV_LIST = []
ACPT_FAM_LIST = []
REJ_FAM_LIST = []
ACPT_PER_LIST = []
REJ_PER_LIST = []
ACPTCHLD_LIST = []
REGION_LIST = []
STRAT_P_LIST = []
PSU_P_LIST = []

with open(custom_parser_input_file_name, encoding="utf8", mode="r") as f:
    for ldx, line in enumerate(f):
        if ldx < 60346:
            RECTYPE_accumulator_LIST = []
            SRVY_YR_accumulator_LIST = []
            HHX_accumulator_LIST = []
            INTV_QRT_accumulator_LIST = []
            INTV_MON_accumulator_LIST = []
            WTIA_HH_accumulator_LIST = []
            WTFA_HH_accumulator_LIST = []
            LIVQRT_accumulator_LIST = []
            NON_INTV_accumulator_LIST = []
            ACPT_FAM_accumulator_LIST = []
            REJ_FAM_accumulator_LIST = []
            ACPT_PER_accumulator_LIST = []
            REJ_PER_accumulator_LIST = []
            ACPTCHLD_accumulator_LIST = []
            REGION_accumulator_LIST = []
            STRAT_P_accumulator_LIST = []
            PSU_P_accumulator_LIST = []

            for cdx, char in enumerate(line):
                if -1 < cdx < 2:
                    RECTYPE_accumulator_LIST.append(char)
                    RECTYPE = ''.join(RECTYPE_accumulator_LIST)
                elif 1 < cdx < 6:
                    SRVY_YR_accumulator_LIST.append(char)
                    SRVY_YR = ''.join(SRVY_YR_accumulator_LIST)
                elif 5 < cdx < 12:
                    HHX_accumulator_LIST.append(char)
                    HHX = ''.join(HHX_accumulator_LIST)
                elif 11 < cdx < 13:
                    INTV_QRT_accumulator_LIST.append(char)
                    INTV_QRT = ''.join(INTV_QRT_accumulator_LIST)
                elif 12 < cdx < 15:
                    INTV_MON_accumulator_LIST.append(char)
                    INTV_MON = ''.join(INTV_MON_accumulator_LIST)
                elif 14 < cdx < 21:
                    WTIA_HH_accumulator_LIST.append(char)
                    WTIA_HH = ''.join(WTIA_HH_accumulator_LIST)
                elif 20 < cdx < 27:
                    WTFA_HH_accumulator_LIST.append(char)
                    WTFA_HH = ''.join(WTFA_HH_accumulator_LIST)
                elif 26 < cdx < 29:
                    LIVQRT_accumulator_LIST.append(char)
                    LIVQRT = ''.join(LIVQRT_accumulator_LIST)
                elif 28 < cdx < 30:
                    NON_INTV_accumulator_LIST.append(char)
                    NON_INTV = ''.join(NON_INTV_accumulator_LIST)
                elif 29 < cdx < 32:
                    ACPT_FAM_accumulator_LIST.append(char)
                    ACPT_FAM = ''.join(ACPT_FAM_accumulator_LIST)
                elif 31 < cdx < 34:
                    REJ_FAM_accumulator_LIST.append(char)
                    REJ_FAM = ''.join(REJ_FAM_accumulator_LIST)
                elif 33 < cdx < 36:
                    ACPT_PER_accumulator_LIST.append(char)
                    ACPT_PER = ''.join(ACPT_PER_accumulator_LIST)
                elif 35 < cdx < 38:
                    REJ_PER_accumulator_LIST.append(char)
                    REJ_PER = ''.join(REJ_PER_accumulator_LIST)
                elif 37 < cdx < 40:
                    ACPTCHLD_accumulator_LIST.append(char)
                    ACPTCHLD = ''.join(ACPTCHLD_accumulator_LIST)
                elif 39 < cdx < 41:
                    REGION_accumulator_LIST.append(char)
                    REGION = ''.join(REGION_accumulator_LIST)
                elif 40 < cdx < 44:
                    STRAT_P_accumulator_LIST.append(char)
                    STRAT_P = ''.join(STRAT_P_accumulator_LIST)
                elif 43 < cdx < 46:
                    PSU_P_accumulator_LIST.append(char)
                    PSU_P = ''.join(PSU_P_accumulator_LIST)
                else:
                    if char == '\n':
                        pass
                    else:
                        print("Problem: Email russ.robbins@outlook.com")

        RECTYPE_LIST.append(RECTYPE)
        SRVY_YR_LIST.append(SRVY_YR)
        HHX_LIST.append(HHX)
        INTV_QRT_LIST.append(INTV_QRT)
        INTV_MON_LIST.append(INTV_MON)
        WTIA_HH_LIST.append(WTIA_HH)
        WTFA_HH_LIST.append(WTFA_HH)
        LIVQRT_LIST.append(LIVQRT)
        NON_INTV_LIST.append(NON_INTV)
        ACPT_FAM_LIST.append(ACPT_FAM)
        REJ_FAM_LIST.append(REJ_FAM)
        ACPT_PER_LIST.append(ACPT_PER)
        REJ_PER_LIST.append(REJ_PER)
        ACPTCHLD_LIST.append(ACPTCHLD)
        REGION_LIST.append(REGION)
        STRAT_P_LIST.append(STRAT_P)
        PSU_P_LIST.append(PSU_P)

df = pd.DataFrame(columns=(
                            'RECTYPE',
                            'SRVY_YR',
                            'HHX',
                            'INTV_QRT',
                            'INTV_MON',
                            'WTIA_HH',
                            'WTFA_HH',
                            'LIVQRT',
                            'NON_INTV',
                            'ACPT_FAM',
                            'REJ_FAM',
                            'ACPT_PER',
                            'REJ_PER',
                            'ACPTCHLD',
                            'REGION',
                            'STRAT_P',
                            'PSU_P'
                                    ))

for i in range(60346):
    df.loc[i] = [
                    RECTYPE_LIST[i],
                    SRVY_YR_LIST[i],
                    HHX_LIST[i],
                    INTV_QRT_LIST[i],
                    INTV_MON_LIST[i],
                    WTIA_HH_LIST[i],
                    WTFA_HH_LIST[i],
                    LIVQRT_LIST[i],
                    NON_INTV_LIST[i],
                    ACPT_FAM_LIST[i],
                    REJ_FAM_LIST[i],
                    ACPT_PER_LIST[i],
                    REJ_PER_LIST[i],
                    ACPTCHLD_LIST[i],
                    REGION_LIST[i],
                    STRAT_P_LIST[i],
                    PSU_P_LIST[i]
                                    ]
df = df.applymap(lambda x: np.nan if str(x).isspace() else x)
df.to_csv("nhis_2014_househld.csv")
