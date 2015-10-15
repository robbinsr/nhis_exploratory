import pandas as pd
import numpy as np

input_data_FILE = "nhis_2014_paradata.dat"

RECTYPE = ''
SRVY_YR = ''
HHX = ''
INTV_QRT = ''
INTV_MON = ''
FMX = ''
OUTCOME1 = ''
WTIA_PD = ''
QCSASCFM = ''
QCFAM = ''
TOTCOUNT = ''
MODE_P = ''
MODE_T = ''
CTSTAT1 = ''
CTSTAT2 = ''
CTSTAT3 = ''
UNABLE1R = ''
UNABLE2R = ''
UNABLE3R = ''
UNABLE4R = ''
UNABLE5R = ''
UNABL99R = ''
LANG1R = ''
LANG2R = ''
LANG3R = ''
LANG4R = ''
LANG5R = ''
NCTP01R = ''
NCTPR03R = ''
NCTPR04R = ''
NCTP05R = ''
NCTPR07R = ''
NCTPR08R = ''
NCTPR09R = ''
NCTPR10R = ''
NCTPR11R = ''
NCTP12R = ''
NCTPR99R = ''
NCTL01R = ''
NCTL02R = ''
NCTEL03R = ''
NCTEL04R = ''
NCTEL05R = ''
NCTL06R = ''
NCTL07R = ''
NCTEL99R = ''
RELC01R = ''
RELUC02R = ''
RELUC03R = ''
RELUC05R = ''
RELUC06R = ''
RELUC07R = ''
RELC08R = ''
RELC09R = ''
RELUC11R = ''
RELUC12R = ''
RELC15R = ''
RELUC98R = ''
RELUC99R = ''
STRAT01R = ''
STRAT02R = ''
STRAT03R = ''
STRAT04R = ''
STRAT05R = ''
STRAT06R = ''
STRT11R = ''
STRAT12R = ''
STRAT13R = ''
STRT14R = ''
STRAT98R = ''
STRAT99R = ''
REASSIGN = ''
FLNGINTV = ''
INTRPT = ''
NONRES = ''
NONRES2 = ''
INTMODE = ''
RESPOND = ''
COOPFAM = ''
PARWHY = ''
BRKWHER = ''
BRKRES1 = ''
NCOMRES = ''
TYPEABC = ''
TYPEA1 = ''
TYPEB2 = ''
TELN_FLG = ''
CURWRKN = ''
TELCELN = ''
WRKCELN = ''
PHONEUSE = ''
ENDPNT = ''
STRTPNT = ''
HHC_TOD = ''
FMSTRPNT = ''
FAM_TOD = ''
SASTRPNT = ''
SA_TOD = ''
SCSTRPNT = ''
SC_TOD = ''
STRAT_P = ''
PSU_P = ''
CENREG = ''

RECTYPE_LIST = []
SRVY_YR_LIST = []
HHX_LIST = []
INTV_QRT_LIST = []
INTV_MON_LIST = []
FMX_LIST = []
OUTCOME1_LIST = []
WTIA_PD_LIST = []
QCSASCFM_LIST = []
QCFAM_LIST = []
TOTCOUNT_LIST = []
MODE_P_LIST = []
MODE_T_LIST = []
CTSTAT1_LIST = []
CTSTAT2_LIST = []
CTSTAT3_LIST = []
UNABLE1R_LIST = []
UNABLE2R_LIST = []
UNABLE3R_LIST = []
UNABLE4R_LIST = []
UNABLE5R_LIST = []
UNABL99R_LIST = []
LANG1R_LIST = []
LANG2R_LIST = []
LANG3R_LIST = []
LANG4R_LIST = []
LANG5R_LIST = []
NCTP01R_LIST = []
NCTPR03R_LIST = []
NCTPR04R_LIST = []
NCTP05R_LIST = []
NCTPR07R_LIST = []
NCTPR08R_LIST = []
NCTPR09R_LIST = []
NCTPR10R_LIST = []
NCTPR11R_LIST = []
NCTP12R_LIST = []
NCTPR99R_LIST = []
NCTL01R_LIST = []
NCTL02R_LIST = []
NCTEL03R_LIST = []
NCTEL04R_LIST = []
NCTEL05R_LIST = []
NCTL06R_LIST = []
NCTL07R_LIST = []
NCTEL99R_LIST = []
RELC01R_LIST = []
RELUC02R_LIST = []
RELUC03R_LIST = []
RELUC05R_LIST = []
RELUC06R_LIST = []
RELUC07R_LIST = []
RELC08R_LIST = []
RELC09R_LIST = []
RELUC11R_LIST = []
RELUC12R_LIST = []
RELC15R_LIST = []
RELUC98R_LIST = []
RELUC99R_LIST = []
STRAT01R_LIST = []
STRAT02R_LIST = []
STRAT03R_LIST = []
STRAT04R_LIST = []
STRAT05R_LIST = []
STRAT06R_LIST = []
STRT11R_LIST = []
STRAT12R_LIST = []
STRAT13R_LIST = []
STRT14R_LIST = []
STRAT98R_LIST = []
STRAT99R_LIST = []
REASSIGN_LIST = []
FLNGINTV_LIST = []
INTRPT_LIST = []
NONRES_LIST = []
NONRES2_LIST = []
INTMODE_LIST = []
RESPOND_LIST = []
COOPFAM_LIST = []
PARWHY_LIST = []
BRKWHER_LIST = []
BRKRES1_LIST = []
NCOMRES_LIST = []
TYPEABC_LIST = []
TYPEA1_LIST = []
TYPEB2_LIST = []
TELN_FLG_LIST = []
CURWRKN_LIST = []
TELCELN_LIST = []
WRKCELN_LIST = []
PHONEUSE_LIST = []
ENDPNT_LIST = []
STRTPNT_LIST = []
HHC_TOD_LIST = []
FMSTRPNT_LIST = []
FAM_TOD_LIST = []
SASTRPNT_LIST = []
SA_TOD_LIST = []
SCSTRPNT_LIST = []
SC_TOD_LIST = []
STRAT_P_LIST = []
PSU_P_LIST = []
CENREG_LIST = []

with open(input_data_FILE, encoding="utf8", mode="r") as f_data:
    for ldx, line in enumerate(f_data):
        if ldx < 20:
            RECTYPE_accumulator_LIST = []
            SRVY_YR_accumulator_LIST = []
            HHX_accumulator_LIST = []
            INTV_QRT_accumulator_LIST = []
            INTV_MON_accumulator_LIST = []
            FMX_accumulator_LIST = []
            OUTCOME1_accumulator_LIST = []
            WTIA_PD_accumulator_LIST = []
            QCSASCFM_accumulator_LIST = []
            QCFAM_accumulator_LIST = []
            TOTCOUNT_accumulator_LIST = []
            MODE_P_accumulator_LIST = []
            MODE_T_accumulator_LIST = []
            CTSTAT1_accumulator_LIST = []
            CTSTAT2_accumulator_LIST = []
            CTSTAT3_accumulator_LIST = []
            UNABLE1R_accumulator_LIST = []
            UNABLE2R_accumulator_LIST = []
            UNABLE3R_accumulator_LIST = []
            UNABLE4R_accumulator_LIST = []
            UNABLE5R_accumulator_LIST = []
            UNABL99R_accumulator_LIST = []
            LANG1R_accumulator_LIST = []
            LANG2R_accumulator_LIST = []
            LANG3R_accumulator_LIST = []
            LANG4R_accumulator_LIST = []
            LANG5R_accumulator_LIST = []
            NCTP01R_accumulator_LIST = []
            NCTPR03R_accumulator_LIST = []
            NCTPR04R_accumulator_LIST = []
            NCTP05R_accumulator_LIST = []
            NCTPR07R_accumulator_LIST = []
            NCTPR08R_accumulator_LIST = []
            NCTPR09R_accumulator_LIST = []
            NCTPR10R_accumulator_LIST = []
            NCTPR11R_accumulator_LIST = []
            NCTP12R_accumulator_LIST = []
            NCTPR99R_accumulator_LIST = []
            NCTL01R_accumulator_LIST = []
            NCTL02R_accumulator_LIST = []
            NCTEL03R_accumulator_LIST = []
            NCTEL04R_accumulator_LIST = []
            NCTEL05R_accumulator_LIST = []
            NCTL06R_accumulator_LIST = []
            NCTL07R_accumulator_LIST = []
            NCTEL99R_accumulator_LIST = []
            RELC01R_accumulator_LIST = []
            RELUC02R_accumulator_LIST = []
            RELUC03R_accumulator_LIST = []
            RELUC05R_accumulator_LIST = []
            RELUC06R_accumulator_LIST = []
            RELUC07R_accumulator_LIST = []
            RELC08R_accumulator_LIST = []
            RELC09R_accumulator_LIST = []
            RELUC11R_accumulator_LIST = []
            RELUC12R_accumulator_LIST = []
            RELC15R_accumulator_LIST = []
            RELUC98R_accumulator_LIST = []
            RELUC99R_accumulator_LIST = []
            STRAT01R_accumulator_LIST = []
            STRAT02R_accumulator_LIST = []
            STRAT03R_accumulator_LIST = []
            STRAT04R_accumulator_LIST = []
            STRAT05R_accumulator_LIST = []
            STRAT06R_accumulator_LIST = []
            STRT11R_accumulator_LIST = []
            STRAT12R_accumulator_LIST = []
            STRAT13R_accumulator_LIST = []
            STRT14R_accumulator_LIST = []
            STRAT98R_accumulator_LIST = []
            STRAT99R_accumulator_LIST = []
            REASSIGN_accumulator_LIST = []
            FLNGINTV_accumulator_LIST = []
            INTRPT_accumulator_LIST = []
            NONRES_accumulator_LIST = []
            NONRES2_accumulator_LIST = []
            INTMODE_accumulator_LIST = []
            RESPOND_accumulator_LIST = []
            COOPFAM_accumulator_LIST = []
            PARWHY_accumulator_LIST = []
            BRKWHER_accumulator_LIST = []
            BRKRES1_accumulator_LIST = []
            NCOMRES_accumulator_LIST = []
            TYPEABC_accumulator_LIST = []
            TYPEA1_accumulator_LIST = []
            TYPEB2_accumulator_LIST = []
            TELN_FLG_accumulator_LIST = []
            CURWRKN_accumulator_LIST = []
            TELCELN_accumulator_LIST = []
            WRKCELN_accumulator_LIST = []
            PHONEUSE_accumulator_LIST = []
            ENDPNT_accumulator_LIST = []
            STRTPNT_accumulator_LIST = []
            HHC_TOD_accumulator_LIST = []
            FMSTRPNT_accumulator_LIST = []
            FAM_TOD_accumulator_LIST = []
            SASTRPNT_accumulator_LIST = []
            SA_TOD_accumulator_LIST = []
            SCSTRPNT_accumulator_LIST = []
            SC_TOD_accumulator_LIST = []
            STRAT_P_accumulator_LIST = []
            PSU_P_accumulator_LIST = []
            CENREG_accumulator_LIST = []

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
                elif 16 < cdx < 20:
                    OUTCOME1_accumulator_LIST.append(char)
                    OUTCOME1 = ''.join(OUTCOME1_accumulator_LIST)
                elif 19 < cdx < 28:
                    WTIA_PD_accumulator_LIST.append(char)
                    WTIA_PD = ''.join(WTIA_PD_accumulator_LIST)
                elif 27 < cdx < 29:
                    QCSASCFM_accumulator_LIST.append(char)
                    QCSASCFM = ''.join(QCSASCFM_accumulator_LIST)
                elif 28 < cdx < 30:
                    QCFAM_accumulator_LIST.append(char)
                    QCFAM = ''.join(QCFAM_accumulator_LIST)
                elif 29 < cdx < 32:
                    TOTCOUNT_accumulator_LIST.append(char)
                    TOTCOUNT = ''.join(TOTCOUNT_accumulator_LIST)
                elif 31 < cdx < 34:
                    MODE_P_accumulator_LIST.append(char)
                    MODE_P = ''.join(MODE_P_accumulator_LIST)
                elif 33 < cdx < 36:
                    MODE_T_accumulator_LIST.append(char)
                    MODE_T = ''.join(MODE_T_accumulator_LIST)
                elif 35 < cdx < 38:
                    CTSTAT1_accumulator_LIST.append(char)
                    CTSTAT1 = ''.join(CTSTAT1_accumulator_LIST)
                elif 37 < cdx < 40:
                    CTSTAT2_accumulator_LIST.append(char)
                    CTSTAT2 = ''.join(CTSTAT2_accumulator_LIST)
                elif 39 < cdx < 42:
                    CTSTAT3_accumulator_LIST.append(char)
                    CTSTAT3 = ''.join(CTSTAT3_accumulator_LIST)
                elif 41 < cdx < 43:
                    UNABLE1R_accumulator_LIST.append(char)
                    UNABLE1R = ''.join(UNABLE1R_accumulator_LIST)
                elif 42 < cdx < 44:
                    UNABLE2R_accumulator_LIST.append(char)
                    UNABLE2R = ''.join(UNABLE2R_accumulator_LIST)
                elif 43 < cdx < 45:
                    UNABLE3R_accumulator_LIST.append(char)
                    UNABLE3R = ''.join(UNABLE3R_accumulator_LIST)
                elif 44 < cdx < 46:
                    UNABLE4R_accumulator_LIST.append(char)
                    UNABLE4R = ''.join(UNABLE4R_accumulator_LIST)
                elif 45 < cdx < 47:
                    UNABLE5R_accumulator_LIST.append(char)
                    UNABLE5R = ''.join(UNABLE5R_accumulator_LIST)
                elif 46 < cdx < 48:
                    UNABL99R_accumulator_LIST.append(char)
                    UNABL99R = ''.join(UNABL99R_accumulator_LIST)
                elif 47 < cdx < 49:
                    LANG1R_accumulator_LIST.append(char)
                    LANG1R = ''.join(LANG1R_accumulator_LIST)
                elif 48 < cdx < 50:
                    LANG2R_accumulator_LIST.append(char)
                    LANG2R = ''.join(LANG2R_accumulator_LIST)
                elif 49 < cdx < 51:
                    LANG3R_accumulator_LIST.append(char)
                    LANG3R = ''.join(LANG3R_accumulator_LIST)
                elif 50 < cdx < 52:
                    LANG4R_accumulator_LIST.append(char)
                    LANG4R = ''.join(LANG4R_accumulator_LIST)
                elif 51 < cdx < 53:
                    LANG5R_accumulator_LIST.append(char)
                    LANG5R = ''.join(LANG5R_accumulator_LIST)
                elif 52 < cdx < 54:
                    NCTP01R_accumulator_LIST.append(char)
                    NCTP01R = ''.join(NCTP01R_accumulator_LIST)
                elif 53 < cdx < 55:
                    NCTPR03R_accumulator_LIST.append(char)
                    NCTPR03R = ''.join(NCTPR03R_accumulator_LIST)
                elif 54 < cdx < 56:
                    NCTPR04R_accumulator_LIST.append(char)
                    NCTPR04R = ''.join(NCTPR04R_accumulator_LIST)
                elif 55 < cdx < 57:
                    NCTP05R_accumulator_LIST.append(char)
                    NCTP05R = ''.join(NCTP05R_accumulator_LIST)
                elif 56 < cdx < 58:
                    NCTPR07R_accumulator_LIST.append(char)
                    NCTPR07R = ''.join(NCTPR07R_accumulator_LIST)
                elif 57 < cdx < 59:
                    NCTPR08R_accumulator_LIST.append(char)
                    NCTPR08R = ''.join(NCTPR08R_accumulator_LIST)
                elif 58 < cdx < 60:
                    NCTPR09R_accumulator_LIST.append(char)
                    NCTPR09R = ''.join(NCTPR09R_accumulator_LIST)
                elif 59 < cdx < 61:
                    NCTPR10R_accumulator_LIST.append(char)
                    NCTPR10R = ''.join(NCTPR10R_accumulator_LIST)
                elif 60 < cdx < 62:
                    NCTPR11R_accumulator_LIST.append(char)
                    NCTPR11R = ''.join(NCTPR11R_accumulator_LIST)
                elif 61 < cdx < 63:
                    NCTP12R_accumulator_LIST.append(char)
                    NCTP12R = ''.join(NCTP12R_accumulator_LIST)
                elif 62 < cdx < 64:
                    NCTPR99R_accumulator_LIST.append(char)
                    NCTPR99R = ''.join(NCTPR99R_accumulator_LIST)
                elif 63 < cdx < 65:
                    NCTL01R_accumulator_LIST.append(char)
                    NCTL01R = ''.join(NCTL01R_accumulator_LIST)
                elif 64 < cdx < 66:
                    NCTL02R_accumulator_LIST.append(char)
                    NCTL02R = ''.join(NCTL02R_accumulator_LIST)
                elif 65 < cdx < 67:
                    NCTEL03R_accumulator_LIST.append(char)
                    NCTEL03R = ''.join(NCTEL03R_accumulator_LIST)
                elif 66 < cdx < 68:
                    NCTEL04R_accumulator_LIST.append(char)
                    NCTEL04R = ''.join(NCTEL04R_accumulator_LIST)
                elif 67 < cdx < 69:
                    NCTEL05R_accumulator_LIST.append(char)
                    NCTEL05R = ''.join(NCTEL05R_accumulator_LIST)
                elif 68 < cdx < 70:
                    NCTL06R_accumulator_LIST.append(char)
                    NCTL06R = ''.join(NCTL06R_accumulator_LIST)
                elif 69 < cdx < 71:
                    NCTL07R_accumulator_LIST.append(char)
                    NCTL07R = ''.join(NCTL07R_accumulator_LIST)
                elif 70 < cdx < 72:
                    NCTEL99R_accumulator_LIST.append(char)
                    NCTEL99R = ''.join(NCTEL99R_accumulator_LIST)
                elif 71 < cdx < 73:
                    RELC01R_accumulator_LIST.append(char)
                    RELC01R = ''.join(RELC01R_accumulator_LIST)
                elif 72 < cdx < 74:
                    RELUC02R_accumulator_LIST.append(char)
                    RELUC02R = ''.join(RELUC02R_accumulator_LIST)
                elif 73 < cdx < 75:
                    RELUC03R_accumulator_LIST.append(char)
                    RELUC03R = ''.join(RELUC03R_accumulator_LIST)
                elif 74 < cdx < 76:
                    RELUC05R_accumulator_LIST.append(char)
                    RELUC05R = ''.join(RELUC05R_accumulator_LIST)
                elif 75 < cdx < 77:
                    RELUC06R_accumulator_LIST.append(char)
                    RELUC06R = ''.join(RELUC06R_accumulator_LIST)
                elif 76 < cdx < 78:
                    RELUC07R_accumulator_LIST.append(char)
                    RELUC07R = ''.join(RELUC07R_accumulator_LIST)
                elif 77 < cdx < 79:
                    RELC08R_accumulator_LIST.append(char)
                    RELC08R = ''.join(RELC08R_accumulator_LIST)
                elif 78 < cdx < 80:
                    RELC09R_accumulator_LIST.append(char)
                    RELC09R = ''.join(RELC09R_accumulator_LIST)
                elif 79 < cdx < 81:
                    RELUC11R_accumulator_LIST.append(char)
                    RELUC11R = ''.join(RELUC11R_accumulator_LIST)
                elif 80 < cdx < 82:
                    RELUC12R_accumulator_LIST.append(char)
                    RELUC12R = ''.join(RELUC12R_accumulator_LIST)
                elif 81 < cdx < 83:
                    RELC15R_accumulator_LIST.append(char)
                    RELC15R = ''.join(RELC15R_accumulator_LIST)
                elif 82 < cdx < 84:
                    RELUC98R_accumulator_LIST.append(char)
                    RELUC98R = ''.join(RELUC98R_accumulator_LIST)
                elif 83 < cdx < 85:
                    RELUC99R_accumulator_LIST.append(char)
                    RELUC99R = ''.join(RELUC99R_accumulator_LIST)
                elif 84 < cdx < 86:
                    STRAT01R_accumulator_LIST.append(char)
                    STRAT01R = ''.join(STRAT01R_accumulator_LIST)
                elif 85 < cdx < 87:
                    STRAT02R_accumulator_LIST.append(char)
                    STRAT02R = ''.join(STRAT02R_accumulator_LIST)
                elif 86 < cdx < 88:
                    STRAT03R_accumulator_LIST.append(char)
                    STRAT03R = ''.join(STRAT03R_accumulator_LIST)
                elif 87 < cdx < 89:
                    STRAT04R_accumulator_LIST.append(char)
                    STRAT04R = ''.join(STRAT04R_accumulator_LIST)
                elif 88 < cdx < 90:
                    STRAT05R_accumulator_LIST.append(char)
                    STRAT05R = ''.join(STRAT05R_accumulator_LIST)
                elif 89 < cdx < 91:
                    STRAT06R_accumulator_LIST.append(char)
                    STRAT06R = ''.join(STRAT06R_accumulator_LIST)
                elif 90 < cdx < 92:
                    STRT11R_accumulator_LIST.append(char)
                    STRT11R = ''.join(STRT11R_accumulator_LIST)
                elif 91 < cdx < 93:
                    STRAT12R_accumulator_LIST.append(char)
                    STRAT12R = ''.join(STRAT12R_accumulator_LIST)
                elif 92 < cdx < 94:
                    STRAT13R_accumulator_LIST.append(char)
                    STRAT13R = ''.join(STRAT13R_accumulator_LIST)
                elif 93 < cdx < 95:
                    STRT14R_accumulator_LIST.append(char)
                    STRT14R = ''.join(STRT14R_accumulator_LIST)
                elif 94 < cdx < 96:
                    STRAT98R_accumulator_LIST.append(char)
                    STRAT98R = ''.join(STRAT98R_accumulator_LIST)
                elif 95 < cdx < 97:
                    STRAT99R_accumulator_LIST.append(char)
                    STRAT99R = ''.join(STRAT99R_accumulator_LIST)
                elif 96 < cdx < 98:
                    REASSIGN_accumulator_LIST.append(char)
                    REASSIGN = ''.join(REASSIGN_accumulator_LIST)
                elif 97 < cdx < 99:
                    FLNGINTV_accumulator_LIST.append(char)
                    FLNGINTV = ''.join(FLNGINTV_accumulator_LIST)
                elif 98 < cdx < 100:
                    INTRPT_accumulator_LIST.append(char)
                    INTRPT = ''.join(INTRPT_accumulator_LIST)
                elif 99 < cdx < 101:
                    NONRES_accumulator_LIST.append(char)
                    NONRES = ''.join(NONRES_accumulator_LIST)
                elif 100 < cdx < 102:
                    NONRES2_accumulator_LIST.append(char)
                    NONRES2 = ''.join(NONRES2_accumulator_LIST)
                elif 101 < cdx < 103:
                    INTMODE_accumulator_LIST.append(char)
                    INTMODE = ''.join(INTMODE_accumulator_LIST)
                elif 102 < cdx < 104:
                    RESPOND_accumulator_LIST.append(char)
                    RESPOND = ''.join(RESPOND_accumulator_LIST)
                elif 103 < cdx < 105:
                    COOPFAM_accumulator_LIST.append(char)
                    COOPFAM = ''.join(COOPFAM_accumulator_LIST)
                elif 104 < cdx < 106:
                    PARWHY_accumulator_LIST.append(char)
                    PARWHY = ''.join(PARWHY_accumulator_LIST)
                elif 105 < cdx < 107:
                    BRKWHER_accumulator_LIST.append(char)
                    BRKWHER = ''.join(BRKWHER_accumulator_LIST)
                elif 106 < cdx < 109:
                    BRKRES1_accumulator_LIST.append(char)
                    BRKRES1 = ''.join(BRKRES1_accumulator_LIST)
                elif 108 < cdx < 111:
                    NCOMRES_accumulator_LIST.append(char)
                    NCOMRES = ''.join(NCOMRES_accumulator_LIST)
                elif 110 < cdx < 112:
                    TYPEABC_accumulator_LIST.append(char)
                    TYPEABC = ''.join(TYPEABC_accumulator_LIST)
                elif 111 < cdx < 113:
                    TYPEA1_accumulator_LIST.append(char)
                    TYPEA1 = ''.join(TYPEA1_accumulator_LIST)
                elif 112 < cdx < 114:
                    TYPEB2_accumulator_LIST.append(char)
                    TYPEB2 = ''.join(TYPEB2_accumulator_LIST)
                elif 113 < cdx < 115:
                    TELN_FLG_accumulator_LIST.append(char)
                    TELN_FLG = ''.join(TELN_FLG_accumulator_LIST)
                elif 114 < cdx < 116:
                    CURWRKN_accumulator_LIST.append(char)
                    CURWRKN = ''.join(CURWRKN_accumulator_LIST)
                elif 115 < cdx < 117:
                    TELCELN_accumulator_LIST.append(char)
                    TELCELN = ''.join(TELCELN_accumulator_LIST)
                elif 116 < cdx < 119:
                    WRKCELN_accumulator_LIST.append(char)
                    WRKCELN = ''.join(WRKCELN_accumulator_LIST)
                elif 118 < cdx < 120:
                    PHONEUSE_accumulator_LIST.append(char)
                    PHONEUSE = ''.join(PHONEUSE_accumulator_LIST)
                elif 119 < cdx < 121:
                    ENDPNT_accumulator_LIST.append(char)
                    ENDPNT = ''.join(ENDPNT_accumulator_LIST)
                elif 120 < cdx < 122:
                    STRTPNT_accumulator_LIST.append(char)
                    STRTPNT = ''.join(STRTPNT_accumulator_LIST)
                elif 121 < cdx < 123:
                    HHC_TOD_accumulator_LIST.append(char)
                    HHC_TOD = ''.join(HHC_TOD_accumulator_LIST)
                elif 122 < cdx < 124:
                    FMSTRPNT_accumulator_LIST.append(char)
                    FMSTRPNT = ''.join(FMSTRPNT_accumulator_LIST)
                elif 123 < cdx < 125:
                    FAM_TOD_accumulator_LIST.append(char)
                    FAM_TOD = ''.join(FAM_TOD_accumulator_LIST)
                elif 124 < cdx < 126:
                    SASTRPNT_accumulator_LIST.append(char)
                    SASTRPNT = ''.join(SASTRPNT_accumulator_LIST)
                elif 125 < cdx < 127:
                    SA_TOD_accumulator_LIST.append(char)
                    SA_TOD = ''.join(SA_TOD_accumulator_LIST)
                elif 126 < cdx < 128:
                    SCSTRPNT_accumulator_LIST.append(char)
                    SCSTRPNT = ''.join(SCSTRPNT_accumulator_LIST)
                elif 127 < cdx < 129:
                    SC_TOD_accumulator_LIST.append(char)
                    SC_TOD = ''.join(SC_TOD_accumulator_LIST)
                elif 128 < cdx < 132:
                    STRAT_P_accumulator_LIST.append(char)
                    STRAT_P = ''.join(STRAT_P_accumulator_LIST)
                elif 131 < cdx < 134:
                    PSU_P_accumulator_LIST.append(char)
                    PSU_P = ''.join(PSU_P_accumulator_LIST)
                elif 133 < cdx < 135:
                    CENREG_accumulator_LIST.append(char)
                    CENREG = ''.join(CENREG_accumulator_LIST)
                else:
                    if char == '\n':
                        pass
                    else:
                        print("CASE NOT HANDLED")

        RECTYPE_LIST.append(RECTYPE)
        SRVY_YR_LIST.append(SRVY_YR)
        HHX_LIST.append(HHX)
        INTV_QRT_LIST.append(INTV_QRT)
        INTV_MON_LIST.append(INTV_MON)
        FMX_LIST.append(FMX)
        OUTCOME1_LIST.append(OUTCOME1)
        WTIA_PD_LIST.append(WTIA_PD)
        QCSASCFM_LIST.append(QCSASCFM)
        QCFAM_LIST.append(QCFAM)
        TOTCOUNT_LIST.append(TOTCOUNT)
        MODE_P_LIST.append(MODE_P)
        MODE_T_LIST.append(MODE_T)
        CTSTAT1_LIST.append(CTSTAT1)
        CTSTAT2_LIST.append(CTSTAT2)
        CTSTAT3_LIST.append(CTSTAT3)
        UNABLE1R_LIST.append(UNABLE1R)
        UNABLE2R_LIST.append(UNABLE2R)
        UNABLE3R_LIST.append(UNABLE3R)
        UNABLE4R_LIST.append(UNABLE4R)
        UNABLE5R_LIST.append(UNABLE5R)
        UNABL99R_LIST.append(UNABL99R)
        LANG1R_LIST.append(LANG1R)
        LANG2R_LIST.append(LANG2R)
        LANG3R_LIST.append(LANG3R)
        LANG4R_LIST.append(LANG4R)
        LANG5R_LIST.append(LANG5R)
        NCTP01R_LIST.append(NCTP01R)
        NCTPR03R_LIST.append(NCTPR03R)
        NCTPR04R_LIST.append(NCTPR04R)
        NCTP05R_LIST.append(NCTP05R)
        NCTPR07R_LIST.append(NCTPR07R)
        NCTPR08R_LIST.append(NCTPR08R)
        NCTPR09R_LIST.append(NCTPR09R)
        NCTPR10R_LIST.append(NCTPR10R)
        NCTPR11R_LIST.append(NCTPR11R)
        NCTP12R_LIST.append(NCTP12R)
        NCTPR99R_LIST.append(NCTPR99R)
        NCTL01R_LIST.append(NCTL01R)
        NCTL02R_LIST.append(NCTL02R)
        NCTEL03R_LIST.append(NCTEL03R)
        NCTEL04R_LIST.append(NCTEL04R)
        NCTEL05R_LIST.append(NCTEL05R)
        NCTL06R_LIST.append(NCTL06R)
        NCTL07R_LIST.append(NCTL07R)
        NCTEL99R_LIST.append(NCTEL99R)
        RELC01R_LIST.append(RELC01R)
        RELUC02R_LIST.append(RELUC02R)
        RELUC03R_LIST.append(RELUC03R)
        RELUC05R_LIST.append(RELUC05R)
        RELUC06R_LIST.append(RELUC06R)
        RELUC07R_LIST.append(RELUC07R)
        RELC08R_LIST.append(RELC08R)
        RELC09R_LIST.append(RELC09R)
        RELUC11R_LIST.append(RELUC11R)
        RELUC12R_LIST.append(RELUC12R)
        RELC15R_LIST.append(RELC15R)
        RELUC98R_LIST.append(RELUC98R)
        RELUC99R_LIST.append(RELUC99R)
        STRAT01R_LIST.append(STRAT01R)
        STRAT02R_LIST.append(STRAT02R)
        STRAT03R_LIST.append(STRAT03R)
        STRAT04R_LIST.append(STRAT04R)
        STRAT05R_LIST.append(STRAT05R)
        STRAT06R_LIST.append(STRAT06R)
        STRT11R_LIST.append(STRT11R)
        STRAT12R_LIST.append(STRAT12R)
        STRAT13R_LIST.append(STRAT13R)
        STRT14R_LIST.append(STRT14R)
        STRAT98R_LIST.append(STRAT98R)
        STRAT99R_LIST.append(STRAT99R)
        REASSIGN_LIST.append(REASSIGN)
        FLNGINTV_LIST.append(FLNGINTV)
        INTRPT_LIST.append(INTRPT)
        NONRES_LIST.append(NONRES)
        NONRES2_LIST.append(NONRES2)
        INTMODE_LIST.append(INTMODE)
        RESPOND_LIST.append(RESPOND)
        COOPFAM_LIST.append(COOPFAM)
        PARWHY_LIST.append(PARWHY)
        BRKWHER_LIST.append(BRKWHER)
        BRKRES1_LIST.append(BRKRES1)
        NCOMRES_LIST.append(NCOMRES)
        TYPEABC_LIST.append(TYPEABC)
        TYPEA1_LIST.append(TYPEA1)
        TYPEB2_LIST.append(TYPEB2)
        TELN_FLG_LIST.append(TELN_FLG)
        CURWRKN_LIST.append(CURWRKN)
        TELCELN_LIST.append(TELCELN)
        WRKCELN_LIST.append(WRKCELN)
        PHONEUSE_LIST.append(PHONEUSE)
        ENDPNT_LIST.append(ENDPNT)
        STRTPNT_LIST.append(STRTPNT)
        HHC_TOD_LIST.append(HHC_TOD)
        FMSTRPNT_LIST.append(FMSTRPNT)
        FAM_TOD_LIST.append(FAM_TOD)
        SASTRPNT_LIST.append(SASTRPNT)
        SA_TOD_LIST.append(SA_TOD)
        SCSTRPNT_LIST.append(SCSTRPNT)
        SC_TOD_LIST.append(SC_TOD)
        STRAT_P_LIST.append(STRAT_P)
        PSU_P_LIST.append(PSU_P)
        CENREG_LIST.append(CENREG)

df = pd.DataFrame(columns=(
                            'RECTYPE',
                            'SRVY_YR',
                            'HHX',
                            'INTV_QRT',
                            'INTV_MON',
                            'FMX',
                            'OUTCOME1',
                            'WTIA_PD',
                            'QCSASCFM',
                            'QCFAM',
                            'TOTCOUNT',
                            'MODE_P',
                            'MODE_T',
                            'CTSTAT1',
                            'CTSTAT2',
                            'CTSTAT3',
                            'UNABLE1R',
                            'UNABLE2R',
                            'UNABLE3R',
                            'UNABLE4R',
                            'UNABLE5R',
                            'UNABL99R',
                            'LANG1R',
                            'LANG2R',
                            'LANG3R',
                            'LANG4R',
                            'LANG5R',
                            'NCTP01R',
                            'NCTPR03R',
                            'NCTPR04R',
                            'NCTP05R',
                            'NCTPR07R',
                            'NCTPR08R',
                            'NCTPR09R',
                            'NCTPR10R',
                            'NCTPR11R',
                            'NCTP12R',
                            'NCTPR99R',
                            'NCTL01R',
                            'NCTL02R',
                            'NCTEL03R',
                            'NCTEL04R',
                            'NCTEL05R',
                            'NCTL06R',
                            'NCTL07R',
                            'NCTEL99R',
                            'RELC01R',
                            'RELUC02R',
                            'RELUC03R',
                            'RELUC05R',
                            'RELUC06R',
                            'RELUC07R',
                            'RELC08R',
                            'RELC09R',
                            'RELUC11R',
                            'RELUC12R',
                            'RELC15R',
                            'RELUC98R',
                            'RELUC99R',
                            'STRAT01R',
                            'STRAT02R',
                            'STRAT03R',
                            'STRAT04R',
                            'STRAT05R',
                            'STRAT06R',
                            'STRT11R',
                            'STRAT12R',
                            'STRAT13R',
                            'STRT14R',
                            'STRAT98R',
                            'STRAT99R',
                            'REASSIGN',
                            'FLNGINTV',
                            'INTRPT',
                            'NONRES',
                            'NONRES2',
                            'INTMODE',
                            'RESPOND',
                            'COOPFAM',
                            'PARWHY',
                            'BRKWHER',
                            'BRKRES1',
                            'NCOMRES',
                            'TYPEABC',
                            'TYPEA1',
                            'TYPEB2',
                            'TELN_FLG',
                            'CURWRKN',
                            'TELCELN',
                            'WRKCELN',
                            'PHONEUSE',
                            'ENDPNT',
                            'STRTPNT',
                            'HHC_TOD',
                            'FMSTRPNT',
                            'FAM_TOD',
                            'SASTRPNT',
                            'SA_TOD',
                            'SCSTRPNT',
                            'SC_TOD',
                            'STRAT_P',
                            'PSU_P',
                            'CENREG'
                                    ))

for i in range(20):
    df.loc[i] = [
                    RECTYPE_LIST[i],
                    SRVY_YR_LIST[i],
                    HHX_LIST[i],
                    INTV_QRT_LIST[i],
                    INTV_MON_LIST[i],
                    FMX_LIST[i],
                    OUTCOME1_LIST[i],
                    WTIA_PD_LIST[i],
                    QCSASCFM_LIST[i],
                    QCFAM_LIST[i],
                    TOTCOUNT_LIST[i],
                    MODE_P_LIST[i],
                    MODE_T_LIST[i],
                    CTSTAT1_LIST[i],
                    CTSTAT2_LIST[i],
                    CTSTAT3_LIST[i],
                    UNABLE1R_LIST[i],
                    UNABLE2R_LIST[i],
                    UNABLE3R_LIST[i],
                    UNABLE4R_LIST[i],
                    UNABLE5R_LIST[i],
                    UNABL99R_LIST[i],
                    LANG1R_LIST[i],
                    LANG2R_LIST[i],
                    LANG3R_LIST[i],
                    LANG4R_LIST[i],
                    LANG5R_LIST[i],
                    NCTP01R_LIST[i],
                    NCTPR03R_LIST[i],
                    NCTPR04R_LIST[i],
                    NCTP05R_LIST[i],
                    NCTPR07R_LIST[i],
                    NCTPR08R_LIST[i],
                    NCTPR09R_LIST[i],
                    NCTPR10R_LIST[i],
                    NCTPR11R_LIST[i],
                    NCTP12R_LIST[i],
                    NCTPR99R_LIST[i],
                    NCTL01R_LIST[i],
                    NCTL02R_LIST[i],
                    NCTEL03R_LIST[i],
                    NCTEL04R_LIST[i],
                    NCTEL05R_LIST[i],
                    NCTL06R_LIST[i],
                    NCTL07R_LIST[i],
                    NCTEL99R_LIST[i],
                    RELC01R_LIST[i],
                    RELUC02R_LIST[i],
                    RELUC03R_LIST[i],
                    RELUC05R_LIST[i],
                    RELUC06R_LIST[i],
                    RELUC07R_LIST[i],
                    RELC08R_LIST[i],
                    RELC09R_LIST[i],
                    RELUC11R_LIST[i],
                    RELUC12R_LIST[i],
                    RELC15R_LIST[i],
                    RELUC98R_LIST[i],
                    RELUC99R_LIST[i],
                    STRAT01R_LIST[i],
                    STRAT02R_LIST[i],
                    STRAT03R_LIST[i],
                    STRAT04R_LIST[i],
                    STRAT05R_LIST[i],
                    STRAT06R_LIST[i],
                    STRT11R_LIST[i],
                    STRAT12R_LIST[i],
                    STRAT13R_LIST[i],
                    STRT14R_LIST[i],
                    STRAT98R_LIST[i],
                    STRAT99R_LIST[i],
                    REASSIGN_LIST[i],
                    FLNGINTV_LIST[i],
                    INTRPT_LIST[i],
                    NONRES_LIST[i],
                    NONRES2_LIST[i],
                    INTMODE_LIST[i],
                    RESPOND_LIST[i],
                    COOPFAM_LIST[i],
                    PARWHY_LIST[i],
                    BRKWHER_LIST[i],
                    BRKRES1_LIST[i],
                    NCOMRES_LIST[i],
                    TYPEABC_LIST[i],
                    TYPEA1_LIST[i],
                    TYPEB2_LIST[i],
                    TELN_FLG_LIST[i],
                    CURWRKN_LIST[i],
                    TELCELN_LIST[i],
                    WRKCELN_LIST[i],
                    PHONEUSE_LIST[i],
                    ENDPNT_LIST[i],
                    STRTPNT_LIST[i],
                    HHC_TOD_LIST[i],
                    FMSTRPNT_LIST[i],
                    FAM_TOD_LIST[i],
                    SASTRPNT_LIST[i],
                    SA_TOD_LIST[i],
                    SCSTRPNT_LIST[i],
                    SC_TOD_LIST[i],
                    STRAT_P_LIST[i],
                    PSU_P_LIST[i],
                    CENREG_LIST[i]
                                    ]

df = df.applymap(lambda x: np.nan if str(x).isspace() else x)
df.to_csv("nhis_2014_paradata_data.csv")
