import pandas as pd
import numpy as np

custom_parser_input_file_name = "nhis_2014_funcdisb.dat"

RECTYPE = ''
SRVY_YR = ''
HHX = ''
INTV_QRT = ''
INTV_MON = ''
FMX = ''
FPX = ''
WTFA_AFD = ''
STRAT_P = ''
PSU_P = ''
FDRN_FLG = ''
VIS_0 = ''
VIS_SS2 = ''
HEAR_1R = ''
HEAR_2R = ''
HEAR_SS2 = ''
HEAR_3 = ''
HEAR_4 = ''
MOB_SS2 = ''
MOB_2R = ''
MOB_3A = ''
MOB_3B2 = ''
MOB_3C = ''
MOB_3D2 = ''
MOB_3E2 = ''
MOB_3F = ''
MOB_3G = ''
MOB_4 = ''
MOB_5 = ''
MOB_6 = ''
MOB_7 = ''
MOB_8 = ''
COM_SS = ''
COM_2 = ''
COG_SS = ''
COG_1 = ''
COG_2 = ''
COG_3 = ''
UB_SS = ''
UB_1 = ''
UB_2 = ''
ANX_1 = ''
ANX_2 = ''
ANX_3R = ''
DEP_1 = ''
DEP_2 = ''
DEP_3R = ''
PAIN_2 = ''
PAIN_4 = ''
TIRED_1 = ''
TIRED_2 = ''
TIRED_3 = ''
RCS_AFD = ''

RECTYPE_LIST = []
SRVY_YR_LIST = []
HHX_LIST = []
INTV_QRT_LIST = []
INTV_MON_LIST = []
FMX_LIST = []
FPX_LIST = []
WTFA_AFD_LIST = []
STRAT_P_LIST = []
PSU_P_LIST = []
FDRN_FLG_LIST = []
VIS_0_LIST = []
VIS_SS2_LIST = []
HEAR_1R_LIST = []
HEAR_2R_LIST = []
HEAR_SS2_LIST = []
HEAR_3_LIST = []
HEAR_4_LIST = []
MOB_SS2_LIST = []
MOB_2R_LIST = []
MOB_3A_LIST = []
MOB_3B2_LIST = []
MOB_3C_LIST = []
MOB_3D2_LIST = []
MOB_3E2_LIST = []
MOB_3F_LIST = []
MOB_3G_LIST = []
MOB_4_LIST = []
MOB_5_LIST = []
MOB_6_LIST = []
MOB_7_LIST = []
MOB_8_LIST = []
COM_SS_LIST = []
COM_2_LIST = []
COG_SS_LIST = []
COG_1_LIST = []
COG_2_LIST = []
COG_3_LIST = []
UB_SS_LIST = []
UB_1_LIST = []
UB_2_LIST = []
ANX_1_LIST = []
ANX_2_LIST = []
ANX_3R_LIST = []
DEP_1_LIST = []
DEP_2_LIST = []
DEP_3R_LIST = []
PAIN_2_LIST = []
PAIN_4_LIST = []
TIRED_1_LIST = []
TIRED_2_LIST = []
TIRED_3_LIST = []
RCS_AFD_LIST = []

with open(custom_parser_input_file_name, encoding="utf8", mode="r") as f:
    for ldx, line in enumerate(f):
        if ldx < 18302:
            RECTYPE_accumulator_LIST = []
            SRVY_YR_accumulator_LIST = []
            HHX_accumulator_LIST = []
            INTV_QRT_accumulator_LIST = []
            INTV_MON_accumulator_LIST = []
            FMX_accumulator_LIST = []
            FPX_accumulator_LIST = []
            WTFA_AFD_accumulator_LIST = []
            STRAT_P_accumulator_LIST = []
            PSU_P_accumulator_LIST = []
            FDRN_FLG_accumulator_LIST = []
            VIS_0_accumulator_LIST = []
            VIS_SS2_accumulator_LIST = []
            HEAR_1R_accumulator_LIST = []
            HEAR_2R_accumulator_LIST = []
            HEAR_SS2_accumulator_LIST = []
            HEAR_3_accumulator_LIST = []
            HEAR_4_accumulator_LIST = []
            MOB_SS2_accumulator_LIST = []
            MOB_2R_accumulator_LIST = []
            MOB_3A_accumulator_LIST = []
            MOB_3B2_accumulator_LIST = []
            MOB_3C_accumulator_LIST = []
            MOB_3D2_accumulator_LIST = []
            MOB_3E2_accumulator_LIST = []
            MOB_3F_accumulator_LIST = []
            MOB_3G_accumulator_LIST = []
            MOB_4_accumulator_LIST = []
            MOB_5_accumulator_LIST = []
            MOB_6_accumulator_LIST = []
            MOB_7_accumulator_LIST = []
            MOB_8_accumulator_LIST = []
            COM_SS_accumulator_LIST = []
            COM_2_accumulator_LIST = []
            COG_SS_accumulator_LIST = []
            COG_1_accumulator_LIST = []
            COG_2_accumulator_LIST = []
            COG_3_accumulator_LIST = []
            UB_SS_accumulator_LIST = []
            UB_1_accumulator_LIST = []
            UB_2_accumulator_LIST = []
            ANX_1_accumulator_LIST = []
            ANX_2_accumulator_LIST = []
            ANX_3R_accumulator_LIST = []
            DEP_1_accumulator_LIST = []
            DEP_2_accumulator_LIST = []
            DEP_3R_accumulator_LIST = []
            PAIN_2_accumulator_LIST = []
            PAIN_4_accumulator_LIST = []
            TIRED_1_accumulator_LIST = []
            TIRED_2_accumulator_LIST = []
            TIRED_3_accumulator_LIST = []
            RCS_AFD_accumulator_LIST = []

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
                    WTFA_AFD_accumulator_LIST.append(char)
                    WTFA_AFD = ''.join(WTFA_AFD_accumulator_LIST)
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
                    VIS_0_accumulator_LIST.append(char)
                    VIS_0 = ''.join(VIS_0_accumulator_LIST)
                elif 31 < cdx < 33:
                    VIS_SS2_accumulator_LIST.append(char)
                    VIS_SS2 = ''.join(VIS_SS2_accumulator_LIST)
                elif 32 < cdx < 34:
                    HEAR_1R_accumulator_LIST.append(char)
                    HEAR_1R = ''.join(HEAR_1R_accumulator_LIST)
                elif 33 < cdx < 35:
                    HEAR_2R_accumulator_LIST.append(char)
                    HEAR_2R = ''.join(HEAR_2R_accumulator_LIST)
                elif 34 < cdx < 36:
                    HEAR_SS2_accumulator_LIST.append(char)
                    HEAR_SS2 = ''.join(HEAR_SS2_accumulator_LIST)
                elif 35 < cdx < 37:
                    HEAR_3_accumulator_LIST.append(char)
                    HEAR_3 = ''.join(HEAR_3_accumulator_LIST)
                elif 36 < cdx < 38:
                    HEAR_4_accumulator_LIST.append(char)
                    HEAR_4 = ''.join(HEAR_4_accumulator_LIST)
                elif 37 < cdx < 39:
                    MOB_SS2_accumulator_LIST.append(char)
                    MOB_SS2 = ''.join(MOB_SS2_accumulator_LIST)
                elif 38 < cdx < 40:
                    MOB_2R_accumulator_LIST.append(char)
                    MOB_2R = ''.join(MOB_2R_accumulator_LIST)
                elif 39 < cdx < 41:
                    MOB_3A_accumulator_LIST.append(char)
                    MOB_3A = ''.join(MOB_3A_accumulator_LIST)
                elif 40 < cdx < 42:
                    MOB_3B2_accumulator_LIST.append(char)
                    MOB_3B2 = ''.join(MOB_3B2_accumulator_LIST)
                elif 41 < cdx < 43:
                    MOB_3C_accumulator_LIST.append(char)
                    MOB_3C = ''.join(MOB_3C_accumulator_LIST)
                elif 42 < cdx < 44:
                    MOB_3D2_accumulator_LIST.append(char)
                    MOB_3D2 = ''.join(MOB_3D2_accumulator_LIST)
                elif 43 < cdx < 45:
                    MOB_3E2_accumulator_LIST.append(char)
                    MOB_3E2 = ''.join(MOB_3E2_accumulator_LIST)
                elif 44 < cdx < 46:
                    MOB_3F_accumulator_LIST.append(char)
                    MOB_3F = ''.join(MOB_3F_accumulator_LIST)
                elif 45 < cdx < 47:
                    MOB_3G_accumulator_LIST.append(char)
                    MOB_3G = ''.join(MOB_3G_accumulator_LIST)
                elif 46 < cdx < 48:
                    MOB_4_accumulator_LIST.append(char)
                    MOB_4 = ''.join(MOB_4_accumulator_LIST)
                elif 47 < cdx < 49:
                    MOB_5_accumulator_LIST.append(char)
                    MOB_5 = ''.join(MOB_5_accumulator_LIST)
                elif 48 < cdx < 50:
                    MOB_6_accumulator_LIST.append(char)
                    MOB_6 = ''.join(MOB_6_accumulator_LIST)
                elif 49 < cdx < 51:
                    MOB_7_accumulator_LIST.append(char)
                    MOB_7 = ''.join(MOB_7_accumulator_LIST)
                elif 50 < cdx < 52:
                    MOB_8_accumulator_LIST.append(char)
                    MOB_8 = ''.join(MOB_8_accumulator_LIST)
                elif 51 < cdx < 53:
                    COM_SS_accumulator_LIST.append(char)
                    COM_SS = ''.join(COM_SS_accumulator_LIST)
                elif 52 < cdx < 54:
                    COM_2_accumulator_LIST.append(char)
                    COM_2 = ''.join(COM_2_accumulator_LIST)
                elif 53 < cdx < 55:
                    COG_SS_accumulator_LIST.append(char)
                    COG_SS = ''.join(COG_SS_accumulator_LIST)
                elif 54 < cdx < 56:
                    COG_1_accumulator_LIST.append(char)
                    COG_1 = ''.join(COG_1_accumulator_LIST)
                elif 55 < cdx < 57:
                    COG_2_accumulator_LIST.append(char)
                    COG_2 = ''.join(COG_2_accumulator_LIST)
                elif 56 < cdx < 58:
                    COG_3_accumulator_LIST.append(char)
                    COG_3 = ''.join(COG_3_accumulator_LIST)
                elif 57 < cdx < 59:
                    UB_SS_accumulator_LIST.append(char)
                    UB_SS = ''.join(UB_SS_accumulator_LIST)
                elif 58 < cdx < 60:
                    UB_1_accumulator_LIST.append(char)
                    UB_1 = ''.join(UB_1_accumulator_LIST)
                elif 59 < cdx < 61:
                    UB_2_accumulator_LIST.append(char)
                    UB_2 = ''.join(UB_2_accumulator_LIST)
                elif 60 < cdx < 62:
                    ANX_1_accumulator_LIST.append(char)
                    ANX_1 = ''.join(ANX_1_accumulator_LIST)
                elif 61 < cdx < 63:
                    ANX_2_accumulator_LIST.append(char)
                    ANX_2 = ''.join(ANX_2_accumulator_LIST)
                elif 62 < cdx < 64:
                    ANX_3R_accumulator_LIST.append(char)
                    ANX_3R = ''.join(ANX_3R_accumulator_LIST)
                elif 63 < cdx < 65:
                    DEP_1_accumulator_LIST.append(char)
                    DEP_1 = ''.join(DEP_1_accumulator_LIST)
                elif 64 < cdx < 66:
                    DEP_2_accumulator_LIST.append(char)
                    DEP_2 = ''.join(DEP_2_accumulator_LIST)
                elif 65 < cdx < 67:
                    DEP_3R_accumulator_LIST.append(char)
                    DEP_3R = ''.join(DEP_3R_accumulator_LIST)
                elif 66 < cdx < 68:
                    PAIN_2_accumulator_LIST.append(char)
                    PAIN_2 = ''.join(PAIN_2_accumulator_LIST)
                elif 67 < cdx < 69:
                    PAIN_4_accumulator_LIST.append(char)
                    PAIN_4 = ''.join(PAIN_4_accumulator_LIST)
                elif 68 < cdx < 70:
                    TIRED_1_accumulator_LIST.append(char)
                    TIRED_1 = ''.join(TIRED_1_accumulator_LIST)
                elif 69 < cdx < 71:
                    TIRED_2_accumulator_LIST.append(char)
                    TIRED_2 = ''.join(TIRED_2_accumulator_LIST)
                elif 70 < cdx < 72:
                    TIRED_3_accumulator_LIST.append(char)
                    TIRED_3 = ''.join(TIRED_3_accumulator_LIST)
                elif 71 < cdx < 73:
                    RCS_AFD_accumulator_LIST.append(char)
                    RCS_AFD = ''.join(RCS_AFD_accumulator_LIST)
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
        WTFA_AFD_LIST.append(WTFA_AFD)
        STRAT_P_LIST.append(STRAT_P)
        PSU_P_LIST.append(PSU_P)
        FDRN_FLG_LIST.append(FDRN_FLG)
        VIS_0_LIST.append(VIS_0)
        VIS_SS2_LIST.append(VIS_SS2)
        HEAR_1R_LIST.append(HEAR_1R)
        HEAR_2R_LIST.append(HEAR_2R)
        HEAR_SS2_LIST.append(HEAR_SS2)
        HEAR_3_LIST.append(HEAR_3)
        HEAR_4_LIST.append(HEAR_4)
        MOB_SS2_LIST.append(MOB_SS2)
        MOB_2R_LIST.append(MOB_2R)
        MOB_3A_LIST.append(MOB_3A)
        MOB_3B2_LIST.append(MOB_3B2)
        MOB_3C_LIST.append(MOB_3C)
        MOB_3D2_LIST.append(MOB_3D2)
        MOB_3E2_LIST.append(MOB_3E2)
        MOB_3F_LIST.append(MOB_3F)
        MOB_3G_LIST.append(MOB_3G)
        MOB_4_LIST.append(MOB_4)
        MOB_5_LIST.append(MOB_5)
        MOB_6_LIST.append(MOB_6)
        MOB_7_LIST.append(MOB_7)
        MOB_8_LIST.append(MOB_8)
        COM_SS_LIST.append(COM_SS)
        COM_2_LIST.append(COM_2)
        COG_SS_LIST.append(COG_SS)
        COG_1_LIST.append(COG_1)
        COG_2_LIST.append(COG_2)
        COG_3_LIST.append(COG_3)
        UB_SS_LIST.append(UB_SS)
        UB_1_LIST.append(UB_1)
        UB_2_LIST.append(UB_2)
        ANX_1_LIST.append(ANX_1)
        ANX_2_LIST.append(ANX_2)
        ANX_3R_LIST.append(ANX_3R)
        DEP_1_LIST.append(DEP_1)
        DEP_2_LIST.append(DEP_2)
        DEP_3R_LIST.append(DEP_3R)
        PAIN_2_LIST.append(PAIN_2)
        PAIN_4_LIST.append(PAIN_4)
        TIRED_1_LIST.append(TIRED_1)
        TIRED_2_LIST.append(TIRED_2)
        TIRED_3_LIST.append(TIRED_3)
        RCS_AFD_LIST.append(RCS_AFD)

df = pd.DataFrame(columns=(
                            'RECTYPE',
                            'SRVY_YR',
                            'HHX',
                            'INTV_QRT',
                            'INTV_MON',
                            'FMX',
                            'FPX',
                            'WTFA_AFD',
                            'STRAT_P',
                            'PSU_P',
                            'FDRN_FLG',
                            'VIS_0',
                            'VIS_SS2',
                            'HEAR_1R',
                            'HEAR_2R',
                            'HEAR_SS2',
                            'HEAR_3',
                            'HEAR_4',
                            'MOB_SS2',
                            'MOB_2R',
                            'MOB_3A',
                            'MOB_3B2',
                            'MOB_3C',
                            'MOB_3D2',
                            'MOB_3E2',
                            'MOB_3F',
                            'MOB_3G',
                            'MOB_4',
                            'MOB_5',
                            'MOB_6',
                            'MOB_7',
                            'MOB_8',
                            'COM_SS',
                            'COM_2',
                            'COG_SS',
                            'COG_1',
                            'COG_2',
                            'COG_3',
                            'UB_SS',
                            'UB_1',
                            'UB_2',
                            'ANX_1',
                            'ANX_2',
                            'ANX_3R',
                            'DEP_1',
                            'DEP_2',
                            'DEP_3R',
                            'PAIN_2',
                            'PAIN_4',
                            'TIRED_1',
                            'TIRED_2',
                            'TIRED_3',
                            'RCS_AFD'
                                    ))

for i in range(18302):
    df.loc[i] = [
                    RECTYPE_LIST[i],
                    SRVY_YR_LIST[i],
                    HHX_LIST[i],
                    INTV_QRT_LIST[i],
                    INTV_MON_LIST[i],
                    FMX_LIST[i],
                    FPX_LIST[i],
                    WTFA_AFD_LIST[i],
                    STRAT_P_LIST[i],
                    PSU_P_LIST[i],
                    FDRN_FLG_LIST[i],
                    VIS_0_LIST[i],
                    VIS_SS2_LIST[i],
                    HEAR_1R_LIST[i],
                    HEAR_2R_LIST[i],
                    HEAR_SS2_LIST[i],
                    HEAR_3_LIST[i],
                    HEAR_4_LIST[i],
                    MOB_SS2_LIST[i],
                    MOB_2R_LIST[i],
                    MOB_3A_LIST[i],
                    MOB_3B2_LIST[i],
                    MOB_3C_LIST[i],
                    MOB_3D2_LIST[i],
                    MOB_3E2_LIST[i],
                    MOB_3F_LIST[i],
                    MOB_3G_LIST[i],
                    MOB_4_LIST[i],
                    MOB_5_LIST[i],
                    MOB_6_LIST[i],
                    MOB_7_LIST[i],
                    MOB_8_LIST[i],
                    COM_SS_LIST[i],
                    COM_2_LIST[i],
                    COG_SS_LIST[i],
                    COG_1_LIST[i],
                    COG_2_LIST[i],
                    COG_3_LIST[i],
                    UB_SS_LIST[i],
                    UB_1_LIST[i],
                    UB_2_LIST[i],
                    ANX_1_LIST[i],
                    ANX_2_LIST[i],
                    ANX_3R_LIST[i],
                    DEP_1_LIST[i],
                    DEP_2_LIST[i],
                    DEP_3R_LIST[i],
                    PAIN_2_LIST[i],
                    PAIN_4_LIST[i],
                    TIRED_1_LIST[i],
                    TIRED_2_LIST[i],
                    TIRED_3_LIST[i],
                    RCS_AFD_LIST[i]
                                    ]
df = df.applymap(lambda x: np.nan if str(x).isspace() else x)
df.to_csv("nhis_2014_funcdisb.csv")
