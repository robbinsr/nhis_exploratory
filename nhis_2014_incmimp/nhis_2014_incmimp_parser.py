import pandas as pd
import numpy as np

custom_parser_input_file_name = "nhis_2014_incmimp.dat"

RECTYPE = ''
SRVY_YR = ''
HHX = ''
FMX = ''
FPX = ''
IMPNUM = ''
FAMINCF2 = ''
TCINCM_F = ''
FAMINCI2 = ''
POVRATI3 = ''
EMPLOY_F = ''
EMPLOY_I = ''
ERNYR_F = ''
TCEARN_F = ''
ERNYR_I2 = ''

RECTYPE_LIST = []
SRVY_YR_LIST = []
HHX_LIST = []
FMX_LIST = []
FPX_LIST = []
IMPNUM_LIST = []
FAMINCF2_LIST = []
TCINCM_F_LIST = []
FAMINCI2_LIST = []
POVRATI3_LIST = []
EMPLOY_F_LIST = []
EMPLOY_I_LIST = []
ERNYR_F_LIST = []
TCEARN_F_LIST = []
ERNYR_I2_LIST = []

with open(custom_parser_input_file_name, encoding="utf8", mode="r") as f:
    for ldx, line in enumerate(f):
        if ldx < 560264:
            RECTYPE_accumulator_LIST = []
            SRVY_YR_accumulator_LIST = []
            HHX_accumulator_LIST = []
            FMX_accumulator_LIST = []
            FPX_accumulator_LIST = []
            IMPNUM_accumulator_LIST = []
            FAMINCF2_accumulator_LIST = []
            TCINCM_F_accumulator_LIST = []
            FAMINCI2_accumulator_LIST = []
            POVRATI3_accumulator_LIST = []
            EMPLOY_F_accumulator_LIST = []
            EMPLOY_I_accumulator_LIST = []
            ERNYR_F_accumulator_LIST = []
            TCEARN_F_accumulator_LIST = []
            ERNYR_I2_accumulator_LIST = []

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
                elif 11 < cdx < 14:
                    FMX_accumulator_LIST.append(char)
                    FMX = ''.join(FMX_accumulator_LIST)
                elif 13 < cdx < 16:
                    FPX_accumulator_LIST.append(char)
                    FPX = ''.join(FPX_accumulator_LIST)
                elif 15 < cdx < 17:
                    IMPNUM_accumulator_LIST.append(char)
                    IMPNUM = ''.join(IMPNUM_accumulator_LIST)
                elif 16 < cdx < 18:
                    FAMINCF2_accumulator_LIST.append(char)
                    FAMINCF2 = ''.join(FAMINCF2_accumulator_LIST)
                elif 17 < cdx < 19:
                    TCINCM_F_accumulator_LIST.append(char)
                    TCINCM_F = ''.join(TCINCM_F_accumulator_LIST)
                elif 18 < cdx < 25:
                    FAMINCI2_accumulator_LIST.append(char)
                    FAMINCI2 = ''.join(FAMINCI2_accumulator_LIST)
                elif 24 < cdx < 34:
                    POVRATI3_accumulator_LIST.append(char)
                    POVRATI3 = ''.join(POVRATI3_accumulator_LIST)
                elif 33 < cdx < 35:
                    EMPLOY_F_accumulator_LIST.append(char)
                    EMPLOY_F = ''.join(EMPLOY_F_accumulator_LIST)
                elif 34 < cdx < 36:
                    EMPLOY_I_accumulator_LIST.append(char)
                    EMPLOY_I = ''.join(EMPLOY_I_accumulator_LIST)
                elif 35 < cdx < 37:
                    ERNYR_F_accumulator_LIST.append(char)
                    ERNYR_F = ''.join(ERNYR_F_accumulator_LIST)
                elif 36 < cdx < 38:
                    TCEARN_F_accumulator_LIST.append(char)
                    TCEARN_F = ''.join(TCEARN_F_accumulator_LIST)
                elif 37 < cdx < 44:
                    ERNYR_I2_accumulator_LIST.append(char)
                    ERNYR_I2 = ''.join(ERNYR_I2_accumulator_LIST)
                else:
                    if char == '\n':
                        pass
                    else:
                        print("Problem: Email russ.robbins@outlook.com")

        RECTYPE_LIST.append(RECTYPE)
        SRVY_YR_LIST.append(SRVY_YR)
        HHX_LIST.append(HHX)
        FMX_LIST.append(FMX)
        FPX_LIST.append(FPX)
        IMPNUM_LIST.append(IMPNUM)
        FAMINCF2_LIST.append(FAMINCF2)
        TCINCM_F_LIST.append(TCINCM_F)
        FAMINCI2_LIST.append(FAMINCI2)
        POVRATI3_LIST.append(POVRATI3)
        EMPLOY_F_LIST.append(EMPLOY_F)
        EMPLOY_I_LIST.append(EMPLOY_I)
        ERNYR_F_LIST.append(ERNYR_F)
        TCEARN_F_LIST.append(TCEARN_F)
        ERNYR_I2_LIST.append(ERNYR_I2)

df = pd.DataFrame(columns=(
                            'RECTYPE',
                            'SRVY_YR',
                            'HHX',
                            'FMX',
                            'FPX',
                            'IMPNUM',
                            'FAMINCF2',
                            'TCINCM_F',
                            'FAMINCI2',
                            'POVRATI3',
                            'EMPLOY_F',
                            'EMPLOY_I',
                            'ERNYR_F',
                            'TCEARN_F',
                            'ERNYR_I2'
                                    ))

for i in range(560264):
    df.loc[i] = [
                    RECTYPE_LIST[i],
                    SRVY_YR_LIST[i],
                    HHX_LIST[i],
                    FMX_LIST[i],
                    FPX_LIST[i],
                    IMPNUM_LIST[i],
                    FAMINCF2_LIST[i],
                    TCINCM_F_LIST[i],
                    FAMINCI2_LIST[i],
                    POVRATI3_LIST[i],
                    EMPLOY_F_LIST[i],
                    EMPLOY_I_LIST[i],
                    ERNYR_F_LIST[i],
                    TCEARN_F_LIST[i],
                    ERNYR_I2_LIST[i]
                                    ]
df = df.applymap(lambda x: np.nan if str(x).isspace() else x)
df.to_csv("nhis_2014_incmimp.csv")
