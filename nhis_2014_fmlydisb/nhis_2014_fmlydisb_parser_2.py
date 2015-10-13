import pandas as pd
import numpy as np

custom_parser_input_file_name = "nhis_2014_fmlydisb.dat"

RECTYPE = ''
SRVY_YR = ''
HHX = ''
INTV_QRT = ''
INTV_MON = ''
FMX = ''
FPX = ''
WTFA_FDB = ''
STRAT_P = ''
PSU_P = ''
FDRN_FLG = ''
P2DFHEAR = ''
P2DFSEE = ''
P2DFCON = ''
P2DFWALK = ''
P2DFDRES = ''
P2DFERR = ''

RECTYPE_LIST = []
SRVY_YR_LIST = []
HHX_LIST = []
INTV_QRT_LIST = []
INTV_MON_LIST = []
FMX_LIST = []
FPX_LIST = []
WTFA_FDB_LIST = []
STRAT_P_LIST = []
PSU_P_LIST = []
FDRN_FLG_LIST = []
P2DFHEAR_LIST = []
P2DFSEE_LIST = []
P2DFCON_LIST = []
P2DFWALK_LIST = []
P2DFDRES_LIST = []
P2DFERR_LIST = []

with open(custom_parser_input_file_name, encoding="utf8", mode="r") as f:
    for ldx, line in enumerate(f):
        if ldx < 55775:
            RECTYPE_accumulator_LIST = []
            SRVY_YR_accumulator_LIST = []
            HHX_accumulator_LIST = []
            INTV_QRT_accumulator_LIST = []
            INTV_MON_accumulator_LIST = []
            FMX_accumulator_LIST = []
            FPX_accumulator_LIST = []
            WTFA_FDB_accumulator_LIST = []
            STRAT_P_accumulator_LIST = []
            PSU_P_accumulator_LIST = []
            FDRN_FLG_accumulator_LIST = []
            P2DFHEAR_accumulator_LIST = []
            P2DFSEE_accumulator_LIST = []
            P2DFCON_accumulator_LIST = []
            P2DFWALK_accumulator_LIST = []
            P2DFDRES_accumulator_LIST = []
            P2DFERR_accumulator_LIST = []

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
                elif 14 < cdx < 17:
                    FMX_accumulator_LIST.append(char)
                    FMX = ''.join(FMX_accumulator_LIST)
                elif 16 < cdx < 19:
                    FPX_accumulator_LIST.append(char)
                    FPX = ''.join(FPX_accumulator_LIST)
                elif 18 < cdx < 25:
                    WTFA_FDB_accumulator_LIST.append(char)
                    WTFA_FDB = ''.join(WTFA_FDB_accumulator_LIST)
                elif 24 < cdx < 28:
                    STRAT_P_accumulator_LIST.append(char)
                    STRAT_P = ''.join(STRAT_P_accumulator_LIST)
                elif 27 < cdx < 30:
                    PSU_P_accumulator_LIST.append(char)
                    PSU_P = ''.join(PSU_P_accumulator_LIST)
                elif 29 < cdx < 31:
                    FDRN_FLG_accumulator_LIST.append(char)
                    FDRN_FLG = ''.join(FDRN_FLG_accumulator_LIST)
                elif 30 < cdx < 32:
                    P2DFHEAR_accumulator_LIST.append(char)
                    P2DFHEAR = ''.join(P2DFHEAR_accumulator_LIST)
                elif 31 < cdx < 33:
                    P2DFSEE_accumulator_LIST.append(char)
                    P2DFSEE = ''.join(P2DFSEE_accumulator_LIST)
                elif 32 < cdx < 34:
                    P2DFCON_accumulator_LIST.append(char)
                    P2DFCON = ''.join(P2DFCON_accumulator_LIST)
                elif 33 < cdx < 35:
                    P2DFWALK_accumulator_LIST.append(char)
                    P2DFWALK = ''.join(P2DFWALK_accumulator_LIST)
                elif 34 < cdx < 36:
                    P2DFDRES_accumulator_LIST.append(char)
                    P2DFDRES = ''.join(P2DFDRES_accumulator_LIST)
                elif 35 < cdx < 37:
                    P2DFERR_accumulator_LIST.append(char)
                    P2DFERR = ''.join(P2DFERR_accumulator_LIST)
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
        FMX_LIST.append(FMX)
        FPX_LIST.append(FPX)
        WTFA_FDB_LIST.append(WTFA_FDB)
        STRAT_P_LIST.append(STRAT_P)
        PSU_P_LIST.append(PSU_P)
        FDRN_FLG_LIST.append(FDRN_FLG)
        P2DFHEAR_LIST.append(P2DFHEAR)
        P2DFSEE_LIST.append(P2DFSEE)
        P2DFCON_LIST.append(P2DFCON)
        P2DFWALK_LIST.append(P2DFWALK)
        P2DFDRES_LIST.append(P2DFDRES)
        P2DFERR_LIST.append(P2DFERR)

df = pd.DataFrame(columns=(
                            'RECTYPE',
                            'SRVY_YR',
                            'HHX',
                            'INTV_QRT',
                            'INTV_MON',
                            'FMX',
                            'FPX',
                            'WTFA_FDB',
                            'STRAT_P',
                            'PSU_P',
                            'FDRN_FLG',
                            'P2DFHEAR',
                            'P2DFSEE',
                            'P2DFCON',
                            'P2DFWALK',
                            'P2DFDRES',
                            'P2DFERR'
                                    ))

for i in range(55775):
    df.loc[i] = [
                    RECTYPE_LIST[i],
                    SRVY_YR_LIST[i],
                    HHX_LIST[i],
                    INTV_QRT_LIST[i],
                    INTV_MON_LIST[i],
                    FMX_LIST[i],
                    FPX_LIST[i],
                    WTFA_FDB_LIST[i],
                    STRAT_P_LIST[i],
                    PSU_P_LIST[i],
                    FDRN_FLG_LIST[i],
                    P2DFHEAR_LIST[i],
                    P2DFSEE_LIST[i],
                    P2DFCON_LIST[i],
                    P2DFWALK_LIST[i],
                    P2DFDRES_LIST[i],
                    P2DFERR_LIST[i]
                                    ]
df = df.applymap(lambda x: np.nan if str(x).isspace() else x)
df.to_csv("nhis_2014_fmlydisb.csv")
