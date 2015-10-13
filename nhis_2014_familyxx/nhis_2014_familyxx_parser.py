import pandas as pd
import numpy as np

custom_parser_input_file_name = "nhis_2014_familyxx.dat"

RECTYPE = ''
SRVY_YR = ''
HHX = ''
FMX = ''
WTFA_FAM = ''
FINT_Y_P = ''
FINT_M_P = ''
ELN_FLG = ''
CURWRKN = ''
TELCELN = ''
WRKCELN = ''
PHONEUSE = ''
FLNGINTV = ''
FM_SIZE = ''
FM_KIDS = ''
FM_ELDR = ''
FM_TYPE = ''
FM_STRCP = ''
FM_STRP = ''
FM_EDUC1 = ''
FCHLMYN = ''
FCHLMCT = ''
FSPEDYN = ''
FSPEDCT = ''
FLAADLYN = ''
FLAADLCT = ''
FLIADLYN = ''
FLIADLCT = ''
FWKLIMYN = ''
FWKLIMCT = ''
FWALKYN = ''
FWALKCT = ''
FREMEMYN = ''
FREMEMCT = ''
FANYLYN = ''
FANYLCT = ''
FHSTATEX = ''
FHSTATVG = ''
FHSTATG = ''
FHSTATFR = ''
FHSTATPR = ''
FSRUNOUT = ''
FSLAST = ''
FSBALANC = ''
FSSKIP = ''
FSSKDAYS = ''
FSLESS = ''
FSHUNGRY = ''
FSWEIGHT = ''
FSNOTEAT = ''
FSNEDAYS = ''
FDMEDYN = ''
FDMEDCT = ''
FNMEDYN = ''
FNMEDCT = ''
FHOSP2YN = ''
FHOSP2CT = ''
FHCHMYN = ''
FHCHMCT = ''
FHCPHRYN = ''
FHCPHRCT = ''
FHCDVYN = ''
FHCDVCT = ''
F10DVYN = ''
F10DVCT = ''
FHICOVYN = ''
FHICOVCT = ''
FHIPRVCT = ''
FHIEXCT = ''
FHISINCT = ''
FHICARCT = ''
FHICADCT = ''
FHICHPCT = ''
FHIMILCT = ''
FHIIHSCT = ''
FHIPUBCT = ''
FHIOGVCT = ''
FPRCOOH = ''
FHIEBCCT = ''
COVCONF = ''
FHICOST = ''
FMEDBILL = ''
FMEDBPAY = ''
FMEDBNOP = ''
FSAF = ''
FHDSTCT = ''
FDGLWCT1 = ''
FDGLWCT2 = ''
FWRKLWCT = ''
FSALYN = ''
FSALCT = ''
FSEINCYN = ''
FSEINCCT = ''
FSSRRYN = ''
FSSRRCT = ''
FPENSYN = ''
FPENSCT = ''
FOPENSYN = ''
FOPENSCT = ''
FSSIYN = ''
FSSICT = ''
FTANFYN = ''
FTANFCT = ''
FOWBENYN = ''
FOWBENCT = ''
FINTR1YN = ''
FINTR1CT = ''
FDIVDYN = ''
FDIVDCT = ''
FCHSPYN = ''
FCHSPCT = ''
FINCOTYN = ''
FINCOTCT = ''
INCGRP4 = ''
INCGRP5 = ''
RAT_CAT4 = ''
RAT_CAT5 = ''
HOUSEOWN = ''
FGAH = ''
FSSAPLYN = ''
FSSAPLCT = ''
FSDAPLYN = ''
FSDAPLCT = ''
FSNAP = ''
FSNAPMYR = ''
FWICYN = ''
FWICCT = ''

RECTYPE_LIST = []
SRVY_YR_LIST = []
HHX_LIST = []
FMX_LIST = []
WTFA_FAM_LIST = []
FINT_Y_P_LIST = []
FINT_M_P_LIST = []
ELN_FLG_LIST = []
CURWRKN_LIST = []
TELCELN_LIST = []
WRKCELN_LIST = []
PHONEUSE_LIST = []
FLNGINTV_LIST = []
FM_SIZE_LIST = []
FM_KIDS_LIST = []
FM_ELDR_LIST = []
FM_TYPE_LIST = []
FM_STRCP_LIST = []
FM_STRP_LIST = []
FM_EDUC1_LIST = []
FCHLMYN_LIST = []
FCHLMCT_LIST = []
FSPEDYN_LIST = []
FSPEDCT_LIST = []
FLAADLYN_LIST = []
FLAADLCT_LIST = []
FLIADLYN_LIST = []
FLIADLCT_LIST = []
FWKLIMYN_LIST = []
FWKLIMCT_LIST = []
FWALKYN_LIST = []
FWALKCT_LIST = []
FREMEMYN_LIST = []
FREMEMCT_LIST = []
FANYLYN_LIST = []
FANYLCT_LIST = []
FHSTATEX_LIST = []
FHSTATVG_LIST = []
FHSTATG_LIST = []
FHSTATFR_LIST = []
FHSTATPR_LIST = []
FSRUNOUT_LIST = []
FSLAST_LIST = []
FSBALANC_LIST = []
FSSKIP_LIST = []
FSSKDAYS_LIST = []
FSLESS_LIST = []
FSHUNGRY_LIST = []
FSWEIGHT_LIST = []
FSNOTEAT_LIST = []
FSNEDAYS_LIST = []
FDMEDYN_LIST = []
FDMEDCT_LIST = []
FNMEDYN_LIST = []
FNMEDCT_LIST = []
FHOSP2YN_LIST = []
FHOSP2CT_LIST = []
FHCHMYN_LIST = []
FHCHMCT_LIST = []
FHCPHRYN_LIST = []
FHCPHRCT_LIST = []
FHCDVYN_LIST = []
FHCDVCT_LIST = []
F10DVYN_LIST = []
F10DVCT_LIST = []
FHICOVYN_LIST = []
FHICOVCT_LIST = []
FHIPRVCT_LIST = []
FHIEXCT_LIST = []
FHISINCT_LIST = []
FHICARCT_LIST = []
FHICADCT_LIST = []
FHICHPCT_LIST = []
FHIMILCT_LIST = []
FHIIHSCT_LIST = []
FHIPUBCT_LIST = []
FHIOGVCT_LIST = []
FPRCOOH_LIST = []
FHIEBCCT_LIST = []
COVCONF_LIST = []
FHICOST_LIST = []
FMEDBILL_LIST = []
FMEDBPAY_LIST = []
FMEDBNOP_LIST = []
FSAF_LIST = []
FHDSTCT_LIST = []
FDGLWCT1_LIST = []
FDGLWCT2_LIST = []
FWRKLWCT_LIST = []
FSALYN_LIST = []
FSALCT_LIST = []
FSEINCYN_LIST = []
FSEINCCT_LIST = []
FSSRRYN_LIST = []
FSSRRCT_LIST = []
FPENSYN_LIST = []
FPENSCT_LIST = []
FOPENSYN_LIST = []
FOPENSCT_LIST = []
FSSIYN_LIST = []
FSSICT_LIST = []
FTANFYN_LIST = []
FTANFCT_LIST = []
FOWBENYN_LIST = []
FOWBENCT_LIST = []
FINTR1YN_LIST = []
FINTR1CT_LIST = []
FDIVDYN_LIST = []
FDIVDCT_LIST = []
FCHSPYN_LIST = []
FCHSPCT_LIST = []
FINCOTYN_LIST = []
FINCOTCT_LIST = []
INCGRP4_LIST = []
INCGRP5_LIST = []
RAT_CAT4_LIST = []
RAT_CAT5_LIST = []
HOUSEOWN_LIST = []
FGAH_LIST = []
FSSAPLYN_LIST = []
FSSAPLCT_LIST = []
FSDAPLYN_LIST = []
FSDAPLCT_LIST = []
FSNAP_LIST = []
FSNAPMYR_LIST = []
FWICYN_LIST = []
FWICCT_LIST = []

with open(custom_parser_input_file_name, encoding="utf8", mode="r") as f:
    for ldx, line in enumerate(f):
        if ldx < 45596:
            RECTYPE_accumulator_LIST = []
            SRVY_YR_accumulator_LIST = []
            HHX_accumulator_LIST = []
            FMX_accumulator_LIST = []
            WTFA_FAM_accumulator_LIST = []
            FINT_Y_P_accumulator_LIST = []
            FINT_M_P_accumulator_LIST = []
            ELN_FLG_accumulator_LIST = []
            CURWRKN_accumulator_LIST = []
            TELCELN_accumulator_LIST = []
            WRKCELN_accumulator_LIST = []
            PHONEUSE_accumulator_LIST = []
            FLNGINTV_accumulator_LIST = []
            FM_SIZE_accumulator_LIST = []
            FM_KIDS_accumulator_LIST = []
            FM_ELDR_accumulator_LIST = []
            FM_TYPE_accumulator_LIST = []
            FM_STRCP_accumulator_LIST = []
            FM_STRP_accumulator_LIST = []
            FM_EDUC1_accumulator_LIST = []
            FCHLMYN_accumulator_LIST = []
            FCHLMCT_accumulator_LIST = []
            FSPEDYN_accumulator_LIST = []
            FSPEDCT_accumulator_LIST = []
            FLAADLYN_accumulator_LIST = []
            FLAADLCT_accumulator_LIST = []
            FLIADLYN_accumulator_LIST = []
            FLIADLCT_accumulator_LIST = []
            FWKLIMYN_accumulator_LIST = []
            FWKLIMCT_accumulator_LIST = []
            FWALKYN_accumulator_LIST = []
            FWALKCT_accumulator_LIST = []
            FREMEMYN_accumulator_LIST = []
            FREMEMCT_accumulator_LIST = []
            FANYLYN_accumulator_LIST = []
            FANYLCT_accumulator_LIST = []
            FHSTATEX_accumulator_LIST = []
            FHSTATVG_accumulator_LIST = []
            FHSTATG_accumulator_LIST = []
            FHSTATFR_accumulator_LIST = []
            FHSTATPR_accumulator_LIST = []
            FSRUNOUT_accumulator_LIST = []
            FSLAST_accumulator_LIST = []
            FSBALANC_accumulator_LIST = []
            FSSKIP_accumulator_LIST = []
            FSSKDAYS_accumulator_LIST = []
            FSLESS_accumulator_LIST = []
            FSHUNGRY_accumulator_LIST = []
            FSWEIGHT_accumulator_LIST = []
            FSNOTEAT_accumulator_LIST = []
            FSNEDAYS_accumulator_LIST = []
            FDMEDYN_accumulator_LIST = []
            FDMEDCT_accumulator_LIST = []
            FNMEDYN_accumulator_LIST = []
            FNMEDCT_accumulator_LIST = []
            FHOSP2YN_accumulator_LIST = []
            FHOSP2CT_accumulator_LIST = []
            FHCHMYN_accumulator_LIST = []
            FHCHMCT_accumulator_LIST = []
            FHCPHRYN_accumulator_LIST = []
            FHCPHRCT_accumulator_LIST = []
            FHCDVYN_accumulator_LIST = []
            FHCDVCT_accumulator_LIST = []
            F10DVYN_accumulator_LIST = []
            F10DVCT_accumulator_LIST = []
            FHICOVYN_accumulator_LIST = []
            FHICOVCT_accumulator_LIST = []
            FHIPRVCT_accumulator_LIST = []
            FHIEXCT_accumulator_LIST = []
            FHISINCT_accumulator_LIST = []
            FHICARCT_accumulator_LIST = []
            FHICADCT_accumulator_LIST = []
            FHICHPCT_accumulator_LIST = []
            FHIMILCT_accumulator_LIST = []
            FHIIHSCT_accumulator_LIST = []
            FHIPUBCT_accumulator_LIST = []
            FHIOGVCT_accumulator_LIST = []
            FPRCOOH_accumulator_LIST = []
            FHIEBCCT_accumulator_LIST = []
            COVCONF_accumulator_LIST = []
            FHICOST_accumulator_LIST = []
            FMEDBILL_accumulator_LIST = []
            FMEDBPAY_accumulator_LIST = []
            FMEDBNOP_accumulator_LIST = []
            FSAF_accumulator_LIST = []
            FHDSTCT_accumulator_LIST = []
            FDGLWCT1_accumulator_LIST = []
            FDGLWCT2_accumulator_LIST = []
            FWRKLWCT_accumulator_LIST = []
            FSALYN_accumulator_LIST = []
            FSALCT_accumulator_LIST = []
            FSEINCYN_accumulator_LIST = []
            FSEINCCT_accumulator_LIST = []
            FSSRRYN_accumulator_LIST = []
            FSSRRCT_accumulator_LIST = []
            FPENSYN_accumulator_LIST = []
            FPENSCT_accumulator_LIST = []
            FOPENSYN_accumulator_LIST = []
            FOPENSCT_accumulator_LIST = []
            FSSIYN_accumulator_LIST = []
            FSSICT_accumulator_LIST = []
            FTANFYN_accumulator_LIST = []
            FTANFCT_accumulator_LIST = []
            FOWBENYN_accumulator_LIST = []
            FOWBENCT_accumulator_LIST = []
            FINTR1YN_accumulator_LIST = []
            FINTR1CT_accumulator_LIST = []
            FDIVDYN_accumulator_LIST = []
            FDIVDCT_accumulator_LIST = []
            FCHSPYN_accumulator_LIST = []
            FCHSPCT_accumulator_LIST = []
            FINCOTYN_accumulator_LIST = []
            FINCOTCT_accumulator_LIST = []
            INCGRP4_accumulator_LIST = []
            INCGRP5_accumulator_LIST = []
            RAT_CAT4_accumulator_LIST = []
            RAT_CAT5_accumulator_LIST = []
            HOUSEOWN_accumulator_LIST = []
            FGAH_accumulator_LIST = []
            FSSAPLYN_accumulator_LIST = []
            FSSAPLCT_accumulator_LIST = []
            FSDAPLYN_accumulator_LIST = []
            FSDAPLCT_accumulator_LIST = []
            FSNAP_accumulator_LIST = []
            FSNAPMYR_accumulator_LIST = []
            FWICYN_accumulator_LIST = []
            FWICCT_accumulator_LIST = []

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
                elif 13 < cdx < 20:
                    WTFA_FAM_accumulator_LIST.append(char)
                    WTFA_FAM = ''.join(WTFA_FAM_accumulator_LIST)
                elif 19 < cdx < 24:
                    FINT_Y_P_accumulator_LIST.append(char)
                    FINT_Y_P = ''.join(FINT_Y_P_accumulator_LIST)
                elif 23 < cdx < 26:
                    FINT_M_P_accumulator_LIST.append(char)
                    FINT_M_P = ''.join(FINT_M_P_accumulator_LIST)
                elif 25 < cdx < 27:
                    ELN_FLG_accumulator_LIST.append(char)
                    ELN_FLG = ''.join(ELN_FLG_accumulator_LIST)
                elif 26 < cdx < 28:
                    CURWRKN_accumulator_LIST.append(char)
                    CURWRKN = ''.join(CURWRKN_accumulator_LIST)
                elif 27 < cdx < 29:
                    TELCELN_accumulator_LIST.append(char)
                    TELCELN = ''.join(TELCELN_accumulator_LIST)
                elif 28 < cdx < 31:
                    WRKCELN_accumulator_LIST.append(char)
                    WRKCELN = ''.join(WRKCELN_accumulator_LIST)
                elif 30 < cdx < 32:
                    PHONEUSE_accumulator_LIST.append(char)
                    PHONEUSE = ''.join(PHONEUSE_accumulator_LIST)
                elif 31 < cdx < 33:
                    FLNGINTV_accumulator_LIST.append(char)
                    FLNGINTV = ''.join(FLNGINTV_accumulator_LIST)
                elif 32 < cdx < 35:
                    FM_SIZE_accumulator_LIST.append(char)
                    FM_SIZE = ''.join(FM_SIZE_accumulator_LIST)
                elif 34 < cdx < 37:
                    FM_KIDS_accumulator_LIST.append(char)
                    FM_KIDS = ''.join(FM_KIDS_accumulator_LIST)
                elif 36 < cdx < 39:
                    FM_ELDR_accumulator_LIST.append(char)
                    FM_ELDR = ''.join(FM_ELDR_accumulator_LIST)
                elif 38 < cdx < 40:
                    FM_TYPE_accumulator_LIST.append(char)
                    FM_TYPE = ''.join(FM_TYPE_accumulator_LIST)
                elif 39 < cdx < 42:
                    FM_STRCP_accumulator_LIST.append(char)
                    FM_STRCP = ''.join(FM_STRCP_accumulator_LIST)
                elif 41 < cdx < 44:
                    FM_STRP_accumulator_LIST.append(char)
                    FM_STRP = ''.join(FM_STRP_accumulator_LIST)
                elif 43 < cdx < 46:
                    FM_EDUC1_accumulator_LIST.append(char)
                    FM_EDUC1 = ''.join(FM_EDUC1_accumulator_LIST)
                elif 45 < cdx < 47:
                    FCHLMYN_accumulator_LIST.append(char)
                    FCHLMYN = ''.join(FCHLMYN_accumulator_LIST)
                elif 46 < cdx < 49:
                    FCHLMCT_accumulator_LIST.append(char)
                    FCHLMCT = ''.join(FCHLMCT_accumulator_LIST)
                elif 48 < cdx < 50:
                    FSPEDYN_accumulator_LIST.append(char)
                    FSPEDYN = ''.join(FSPEDYN_accumulator_LIST)
                elif 49 < cdx < 52:
                    FSPEDCT_accumulator_LIST.append(char)
                    FSPEDCT = ''.join(FSPEDCT_accumulator_LIST)
                elif 51 < cdx < 53:
                    FLAADLYN_accumulator_LIST.append(char)
                    FLAADLYN = ''.join(FLAADLYN_accumulator_LIST)
                elif 52 < cdx < 55:
                    FLAADLCT_accumulator_LIST.append(char)
                    FLAADLCT = ''.join(FLAADLCT_accumulator_LIST)
                elif 54 < cdx < 56:
                    FLIADLYN_accumulator_LIST.append(char)
                    FLIADLYN = ''.join(FLIADLYN_accumulator_LIST)
                elif 55 < cdx < 58:
                    FLIADLCT_accumulator_LIST.append(char)
                    FLIADLCT = ''.join(FLIADLCT_accumulator_LIST)
                elif 57 < cdx < 59:
                    FWKLIMYN_accumulator_LIST.append(char)
                    FWKLIMYN = ''.join(FWKLIMYN_accumulator_LIST)
                elif 58 < cdx < 61:
                    FWKLIMCT_accumulator_LIST.append(char)
                    FWKLIMCT = ''.join(FWKLIMCT_accumulator_LIST)
                elif 60 < cdx < 62:
                    FWALKYN_accumulator_LIST.append(char)
                    FWALKYN = ''.join(FWALKYN_accumulator_LIST)
                elif 61 < cdx < 64:
                    FWALKCT_accumulator_LIST.append(char)
                    FWALKCT = ''.join(FWALKCT_accumulator_LIST)
                elif 63 < cdx < 65:
                    FREMEMYN_accumulator_LIST.append(char)
                    FREMEMYN = ''.join(FREMEMYN_accumulator_LIST)
                elif 64 < cdx < 67:
                    FREMEMCT_accumulator_LIST.append(char)
                    FREMEMCT = ''.join(FREMEMCT_accumulator_LIST)
                elif 66 < cdx < 68:
                    FANYLYN_accumulator_LIST.append(char)
                    FANYLYN = ''.join(FANYLYN_accumulator_LIST)
                elif 67 < cdx < 70:
                    FANYLCT_accumulator_LIST.append(char)
                    FANYLCT = ''.join(FANYLCT_accumulator_LIST)
                elif 69 < cdx < 72:
                    FHSTATEX_accumulator_LIST.append(char)
                    FHSTATEX = ''.join(FHSTATEX_accumulator_LIST)
                elif 71 < cdx < 74:
                    FHSTATVG_accumulator_LIST.append(char)
                    FHSTATVG = ''.join(FHSTATVG_accumulator_LIST)
                elif 73 < cdx < 76:
                    FHSTATG_accumulator_LIST.append(char)
                    FHSTATG = ''.join(FHSTATG_accumulator_LIST)
                elif 75 < cdx < 78:
                    FHSTATFR_accumulator_LIST.append(char)
                    FHSTATFR = ''.join(FHSTATFR_accumulator_LIST)
                elif 77 < cdx < 80:
                    FHSTATPR_accumulator_LIST.append(char)
                    FHSTATPR = ''.join(FHSTATPR_accumulator_LIST)
                elif 79 < cdx < 81:
                    FSRUNOUT_accumulator_LIST.append(char)
                    FSRUNOUT = ''.join(FSRUNOUT_accumulator_LIST)
                elif 80 < cdx < 82:
                    FSLAST_accumulator_LIST.append(char)
                    FSLAST = ''.join(FSLAST_accumulator_LIST)
                elif 81 < cdx < 83:
                    FSBALANC_accumulator_LIST.append(char)
                    FSBALANC = ''.join(FSBALANC_accumulator_LIST)
                elif 82 < cdx < 84:
                    FSSKIP_accumulator_LIST.append(char)
                    FSSKIP = ''.join(FSSKIP_accumulator_LIST)
                elif 83 < cdx < 86:
                    FSSKDAYS_accumulator_LIST.append(char)
                    FSSKDAYS = ''.join(FSSKDAYS_accumulator_LIST)
                elif 85 < cdx < 87:
                    FSLESS_accumulator_LIST.append(char)
                    FSLESS = ''.join(FSLESS_accumulator_LIST)
                elif 86 < cdx < 88:
                    FSHUNGRY_accumulator_LIST.append(char)
                    FSHUNGRY = ''.join(FSHUNGRY_accumulator_LIST)
                elif 87 < cdx < 89:
                    FSWEIGHT_accumulator_LIST.append(char)
                    FSWEIGHT = ''.join(FSWEIGHT_accumulator_LIST)
                elif 88 < cdx < 90:
                    FSNOTEAT_accumulator_LIST.append(char)
                    FSNOTEAT = ''.join(FSNOTEAT_accumulator_LIST)
                elif 89 < cdx < 92:
                    FSNEDAYS_accumulator_LIST.append(char)
                    FSNEDAYS = ''.join(FSNEDAYS_accumulator_LIST)
                elif 91 < cdx < 93:
                    FDMEDYN_accumulator_LIST.append(char)
                    FDMEDYN = ''.join(FDMEDYN_accumulator_LIST)
                elif 92 < cdx < 95:
                    FDMEDCT_accumulator_LIST.append(char)
                    FDMEDCT = ''.join(FDMEDCT_accumulator_LIST)
                elif 94 < cdx < 96:
                    FNMEDYN_accumulator_LIST.append(char)
                    FNMEDYN = ''.join(FNMEDYN_accumulator_LIST)
                elif 95 < cdx < 98:
                    FNMEDCT_accumulator_LIST.append(char)
                    FNMEDCT = ''.join(FNMEDCT_accumulator_LIST)
                elif 97 < cdx < 99:
                    FHOSP2YN_accumulator_LIST.append(char)
                    FHOSP2YN = ''.join(FHOSP2YN_accumulator_LIST)
                elif 98 < cdx < 101:
                    FHOSP2CT_accumulator_LIST.append(char)
                    FHOSP2CT = ''.join(FHOSP2CT_accumulator_LIST)
                elif 100 < cdx < 102:
                    FHCHMYN_accumulator_LIST.append(char)
                    FHCHMYN = ''.join(FHCHMYN_accumulator_LIST)
                elif 101 < cdx < 104:
                    FHCHMCT_accumulator_LIST.append(char)
                    FHCHMCT = ''.join(FHCHMCT_accumulator_LIST)
                elif 103 < cdx < 105:
                    FHCPHRYN_accumulator_LIST.append(char)
                    FHCPHRYN = ''.join(FHCPHRYN_accumulator_LIST)
                elif 104 < cdx < 107:
                    FHCPHRCT_accumulator_LIST.append(char)
                    FHCPHRCT = ''.join(FHCPHRCT_accumulator_LIST)
                elif 106 < cdx < 108:
                    FHCDVYN_accumulator_LIST.append(char)
                    FHCDVYN = ''.join(FHCDVYN_accumulator_LIST)
                elif 107 < cdx < 110:
                    FHCDVCT_accumulator_LIST.append(char)
                    FHCDVCT = ''.join(FHCDVCT_accumulator_LIST)
                elif 109 < cdx < 111:
                    F10DVYN_accumulator_LIST.append(char)
                    F10DVYN = ''.join(F10DVYN_accumulator_LIST)
                elif 110 < cdx < 113:
                    F10DVCT_accumulator_LIST.append(char)
                    F10DVCT = ''.join(F10DVCT_accumulator_LIST)
                elif 112 < cdx < 114:
                    FHICOVYN_accumulator_LIST.append(char)
                    FHICOVYN = ''.join(FHICOVYN_accumulator_LIST)
                elif 113 < cdx < 116:
                    FHICOVCT_accumulator_LIST.append(char)
                    FHICOVCT = ''.join(FHICOVCT_accumulator_LIST)
                elif 115 < cdx < 118:
                    FHIPRVCT_accumulator_LIST.append(char)
                    FHIPRVCT = ''.join(FHIPRVCT_accumulator_LIST)
                elif 117 < cdx < 120:
                    FHIEXCT_accumulator_LIST.append(char)
                    FHIEXCT = ''.join(FHIEXCT_accumulator_LIST)
                elif 119 < cdx < 122:
                    FHISINCT_accumulator_LIST.append(char)
                    FHISINCT = ''.join(FHISINCT_accumulator_LIST)
                elif 121 < cdx < 124:
                    FHICARCT_accumulator_LIST.append(char)
                    FHICARCT = ''.join(FHICARCT_accumulator_LIST)
                elif 123 < cdx < 126:
                    FHICADCT_accumulator_LIST.append(char)
                    FHICADCT = ''.join(FHICADCT_accumulator_LIST)
                elif 125 < cdx < 128:
                    FHICHPCT_accumulator_LIST.append(char)
                    FHICHPCT = ''.join(FHICHPCT_accumulator_LIST)
                elif 127 < cdx < 130:
                    FHIMILCT_accumulator_LIST.append(char)
                    FHIMILCT = ''.join(FHIMILCT_accumulator_LIST)
                elif 129 < cdx < 132:
                    FHIIHSCT_accumulator_LIST.append(char)
                    FHIIHSCT = ''.join(FHIIHSCT_accumulator_LIST)
                elif 131 < cdx < 134:
                    FHIPUBCT_accumulator_LIST.append(char)
                    FHIPUBCT = ''.join(FHIPUBCT_accumulator_LIST)
                elif 133 < cdx < 136:
                    FHIOGVCT_accumulator_LIST.append(char)
                    FHIOGVCT = ''.join(FHIOGVCT_accumulator_LIST)
                elif 135 < cdx < 137:
                    FPRCOOH_accumulator_LIST.append(char)
                    FPRCOOH = ''.join(FPRCOOH_accumulator_LIST)
                elif 136 < cdx < 139:
                    FHIEBCCT_accumulator_LIST.append(char)
                    FHIEBCCT = ''.join(FHIEBCCT_accumulator_LIST)
                elif 138 < cdx < 140:
                    COVCONF_accumulator_LIST.append(char)
                    COVCONF = ''.join(COVCONF_accumulator_LIST)
                elif 139 < cdx < 141:
                    FHICOST_accumulator_LIST.append(char)
                    FHICOST = ''.join(FHICOST_accumulator_LIST)
                elif 140 < cdx < 142:
                    FMEDBILL_accumulator_LIST.append(char)
                    FMEDBILL = ''.join(FMEDBILL_accumulator_LIST)
                elif 141 < cdx < 143:
                    FMEDBPAY_accumulator_LIST.append(char)
                    FMEDBPAY = ''.join(FMEDBPAY_accumulator_LIST)
                elif 142 < cdx < 144:
                    FMEDBNOP_accumulator_LIST.append(char)
                    FMEDBNOP = ''.join(FMEDBNOP_accumulator_LIST)
                elif 143 < cdx < 145:
                    FSAF_accumulator_LIST.append(char)
                    FSAF = ''.join(FSAF_accumulator_LIST)
                elif 144 < cdx < 147:
                    FHDSTCT_accumulator_LIST.append(char)
                    FHDSTCT = ''.join(FHDSTCT_accumulator_LIST)
                elif 146 < cdx < 149:
                    FDGLWCT1_accumulator_LIST.append(char)
                    FDGLWCT1 = ''.join(FDGLWCT1_accumulator_LIST)
                elif 148 < cdx < 151:
                    FDGLWCT2_accumulator_LIST.append(char)
                    FDGLWCT2 = ''.join(FDGLWCT2_accumulator_LIST)
                elif 150 < cdx < 153:
                    FWRKLWCT_accumulator_LIST.append(char)
                    FWRKLWCT = ''.join(FWRKLWCT_accumulator_LIST)
                elif 152 < cdx < 154:
                    FSALYN_accumulator_LIST.append(char)
                    FSALYN = ''.join(FSALYN_accumulator_LIST)
                elif 153 < cdx < 156:
                    FSALCT_accumulator_LIST.append(char)
                    FSALCT = ''.join(FSALCT_accumulator_LIST)
                elif 155 < cdx < 157:
                    FSEINCYN_accumulator_LIST.append(char)
                    FSEINCYN = ''.join(FSEINCYN_accumulator_LIST)
                elif 156 < cdx < 159:
                    FSEINCCT_accumulator_LIST.append(char)
                    FSEINCCT = ''.join(FSEINCCT_accumulator_LIST)
                elif 158 < cdx < 160:
                    FSSRRYN_accumulator_LIST.append(char)
                    FSSRRYN = ''.join(FSSRRYN_accumulator_LIST)
                elif 159 < cdx < 162:
                    FSSRRCT_accumulator_LIST.append(char)
                    FSSRRCT = ''.join(FSSRRCT_accumulator_LIST)
                elif 161 < cdx < 163:
                    FPENSYN_accumulator_LIST.append(char)
                    FPENSYN = ''.join(FPENSYN_accumulator_LIST)
                elif 162 < cdx < 165:
                    FPENSCT_accumulator_LIST.append(char)
                    FPENSCT = ''.join(FPENSCT_accumulator_LIST)
                elif 164 < cdx < 166:
                    FOPENSYN_accumulator_LIST.append(char)
                    FOPENSYN = ''.join(FOPENSYN_accumulator_LIST)
                elif 165 < cdx < 168:
                    FOPENSCT_accumulator_LIST.append(char)
                    FOPENSCT = ''.join(FOPENSCT_accumulator_LIST)
                elif 167 < cdx < 169:
                    FSSIYN_accumulator_LIST.append(char)
                    FSSIYN = ''.join(FSSIYN_accumulator_LIST)
                elif 168 < cdx < 171:
                    FSSICT_accumulator_LIST.append(char)
                    FSSICT = ''.join(FSSICT_accumulator_LIST)
                elif 170 < cdx < 172:
                    FTANFYN_accumulator_LIST.append(char)
                    FTANFYN = ''.join(FTANFYN_accumulator_LIST)
                elif 171 < cdx < 174:
                    FTANFCT_accumulator_LIST.append(char)
                    FTANFCT = ''.join(FTANFCT_accumulator_LIST)
                elif 173 < cdx < 175:
                    FOWBENYN_accumulator_LIST.append(char)
                    FOWBENYN = ''.join(FOWBENYN_accumulator_LIST)
                elif 174 < cdx < 177:
                    FOWBENCT_accumulator_LIST.append(char)
                    FOWBENCT = ''.join(FOWBENCT_accumulator_LIST)
                elif 176 < cdx < 178:
                    FINTR1YN_accumulator_LIST.append(char)
                    FINTR1YN = ''.join(FINTR1YN_accumulator_LIST)
                elif 177 < cdx < 180:
                    FINTR1CT_accumulator_LIST.append(char)
                    FINTR1CT = ''.join(FINTR1CT_accumulator_LIST)
                elif 179 < cdx < 181:
                    FDIVDYN_accumulator_LIST.append(char)
                    FDIVDYN = ''.join(FDIVDYN_accumulator_LIST)
                elif 180 < cdx < 183:
                    FDIVDCT_accumulator_LIST.append(char)
                    FDIVDCT = ''.join(FDIVDCT_accumulator_LIST)
                elif 182 < cdx < 184:
                    FCHSPYN_accumulator_LIST.append(char)
                    FCHSPYN = ''.join(FCHSPYN_accumulator_LIST)
                elif 183 < cdx < 186:
                    FCHSPCT_accumulator_LIST.append(char)
                    FCHSPCT = ''.join(FCHSPCT_accumulator_LIST)
                elif 185 < cdx < 187:
                    FINCOTYN_accumulator_LIST.append(char)
                    FINCOTYN = ''.join(FINCOTYN_accumulator_LIST)
                elif 186 < cdx < 189:
                    FINCOTCT_accumulator_LIST.append(char)
                    FINCOTCT = ''.join(FINCOTCT_accumulator_LIST)
                elif 188 < cdx < 191:
                    INCGRP4_accumulator_LIST.append(char)
                    INCGRP4 = ''.join(INCGRP4_accumulator_LIST)
                elif 190 < cdx < 193:
                    INCGRP5_accumulator_LIST.append(char)
                    INCGRP5 = ''.join(INCGRP5_accumulator_LIST)
                elif 192 < cdx < 195:
                    RAT_CAT4_accumulator_LIST.append(char)
                    RAT_CAT4 = ''.join(RAT_CAT4_accumulator_LIST)
                elif 194 < cdx < 197:
                    RAT_CAT5_accumulator_LIST.append(char)
                    RAT_CAT5 = ''.join(RAT_CAT5_accumulator_LIST)
                elif 196 < cdx < 198:
                    HOUSEOWN_accumulator_LIST.append(char)
                    HOUSEOWN = ''.join(HOUSEOWN_accumulator_LIST)
                elif 197 < cdx < 199:
                    FGAH_accumulator_LIST.append(char)
                    FGAH = ''.join(FGAH_accumulator_LIST)
                elif 198 < cdx < 200:
                    FSSAPLYN_accumulator_LIST.append(char)
                    FSSAPLYN = ''.join(FSSAPLYN_accumulator_LIST)
                elif 199 < cdx < 202:
                    FSSAPLCT_accumulator_LIST.append(char)
                    FSSAPLCT = ''.join(FSSAPLCT_accumulator_LIST)
                elif 201 < cdx < 203:
                    FSDAPLYN_accumulator_LIST.append(char)
                    FSDAPLYN = ''.join(FSDAPLYN_accumulator_LIST)
                elif 202 < cdx < 205:
                    FSDAPLCT_accumulator_LIST.append(char)
                    FSDAPLCT = ''.join(FSDAPLCT_accumulator_LIST)
                elif 204 < cdx < 206:
                    FSNAP_accumulator_LIST.append(char)
                    FSNAP = ''.join(FSNAP_accumulator_LIST)
                elif 205 < cdx < 208:
                    FSNAPMYR_accumulator_LIST.append(char)
                    FSNAPMYR = ''.join(FSNAPMYR_accumulator_LIST)
                elif 207 < cdx < 209:
                    FWICYN_accumulator_LIST.append(char)
                    FWICYN = ''.join(FWICYN_accumulator_LIST)
                elif 208 < cdx < 211:
                    FWICCT_accumulator_LIST.append(char)
                    FWICCT = ''.join(FWICCT_accumulator_LIST)
                else:
                    if char == '\n':
                        pass
                    else:
                        print("Problem: Email russ.robbins@outlook.com")

        RECTYPE_LIST.append(RECTYPE)
        SRVY_YR_LIST.append(SRVY_YR)
        HHX_LIST.append(HHX)
        FMX_LIST.append(FMX)
        WTFA_FAM_LIST.append(WTFA_FAM)
        FINT_Y_P_LIST.append(FINT_Y_P)
        FINT_M_P_LIST.append(FINT_M_P)
        ELN_FLG_LIST.append(ELN_FLG)
        CURWRKN_LIST.append(CURWRKN)
        TELCELN_LIST.append(TELCELN)
        WRKCELN_LIST.append(WRKCELN)
        PHONEUSE_LIST.append(PHONEUSE)
        FLNGINTV_LIST.append(FLNGINTV)
        FM_SIZE_LIST.append(FM_SIZE)
        FM_KIDS_LIST.append(FM_KIDS)
        FM_ELDR_LIST.append(FM_ELDR)
        FM_TYPE_LIST.append(FM_TYPE)
        FM_STRCP_LIST.append(FM_STRCP)
        FM_STRP_LIST.append(FM_STRP)
        FM_EDUC1_LIST.append(FM_EDUC1)
        FCHLMYN_LIST.append(FCHLMYN)
        FCHLMCT_LIST.append(FCHLMCT)
        FSPEDYN_LIST.append(FSPEDYN)
        FSPEDCT_LIST.append(FSPEDCT)
        FLAADLYN_LIST.append(FLAADLYN)
        FLAADLCT_LIST.append(FLAADLCT)
        FLIADLYN_LIST.append(FLIADLYN)
        FLIADLCT_LIST.append(FLIADLCT)
        FWKLIMYN_LIST.append(FWKLIMYN)
        FWKLIMCT_LIST.append(FWKLIMCT)
        FWALKYN_LIST.append(FWALKYN)
        FWALKCT_LIST.append(FWALKCT)
        FREMEMYN_LIST.append(FREMEMYN)
        FREMEMCT_LIST.append(FREMEMCT)
        FANYLYN_LIST.append(FANYLYN)
        FANYLCT_LIST.append(FANYLCT)
        FHSTATEX_LIST.append(FHSTATEX)
        FHSTATVG_LIST.append(FHSTATVG)
        FHSTATG_LIST.append(FHSTATG)
        FHSTATFR_LIST.append(FHSTATFR)
        FHSTATPR_LIST.append(FHSTATPR)
        FSRUNOUT_LIST.append(FSRUNOUT)
        FSLAST_LIST.append(FSLAST)
        FSBALANC_LIST.append(FSBALANC)
        FSSKIP_LIST.append(FSSKIP)
        FSSKDAYS_LIST.append(FSSKDAYS)
        FSLESS_LIST.append(FSLESS)
        FSHUNGRY_LIST.append(FSHUNGRY)
        FSWEIGHT_LIST.append(FSWEIGHT)
        FSNOTEAT_LIST.append(FSNOTEAT)
        FSNEDAYS_LIST.append(FSNEDAYS)
        FDMEDYN_LIST.append(FDMEDYN)
        FDMEDCT_LIST.append(FDMEDCT)
        FNMEDYN_LIST.append(FNMEDYN)
        FNMEDCT_LIST.append(FNMEDCT)
        FHOSP2YN_LIST.append(FHOSP2YN)
        FHOSP2CT_LIST.append(FHOSP2CT)
        FHCHMYN_LIST.append(FHCHMYN)
        FHCHMCT_LIST.append(FHCHMCT)
        FHCPHRYN_LIST.append(FHCPHRYN)
        FHCPHRCT_LIST.append(FHCPHRCT)
        FHCDVYN_LIST.append(FHCDVYN)
        FHCDVCT_LIST.append(FHCDVCT)
        F10DVYN_LIST.append(F10DVYN)
        F10DVCT_LIST.append(F10DVCT)
        FHICOVYN_LIST.append(FHICOVYN)
        FHICOVCT_LIST.append(FHICOVCT)
        FHIPRVCT_LIST.append(FHIPRVCT)
        FHIEXCT_LIST.append(FHIEXCT)
        FHISINCT_LIST.append(FHISINCT)
        FHICARCT_LIST.append(FHICARCT)
        FHICADCT_LIST.append(FHICADCT)
        FHICHPCT_LIST.append(FHICHPCT)
        FHIMILCT_LIST.append(FHIMILCT)
        FHIIHSCT_LIST.append(FHIIHSCT)
        FHIPUBCT_LIST.append(FHIPUBCT)
        FHIOGVCT_LIST.append(FHIOGVCT)
        FPRCOOH_LIST.append(FPRCOOH)
        FHIEBCCT_LIST.append(FHIEBCCT)
        COVCONF_LIST.append(COVCONF)
        FHICOST_LIST.append(FHICOST)
        FMEDBILL_LIST.append(FMEDBILL)
        FMEDBPAY_LIST.append(FMEDBPAY)
        FMEDBNOP_LIST.append(FMEDBNOP)
        FSAF_LIST.append(FSAF)
        FHDSTCT_LIST.append(FHDSTCT)
        FDGLWCT1_LIST.append(FDGLWCT1)
        FDGLWCT2_LIST.append(FDGLWCT2)
        FWRKLWCT_LIST.append(FWRKLWCT)
        FSALYN_LIST.append(FSALYN)
        FSALCT_LIST.append(FSALCT)
        FSEINCYN_LIST.append(FSEINCYN)
        FSEINCCT_LIST.append(FSEINCCT)
        FSSRRYN_LIST.append(FSSRRYN)
        FSSRRCT_LIST.append(FSSRRCT)
        FPENSYN_LIST.append(FPENSYN)
        FPENSCT_LIST.append(FPENSCT)
        FOPENSYN_LIST.append(FOPENSYN)
        FOPENSCT_LIST.append(FOPENSCT)
        FSSIYN_LIST.append(FSSIYN)
        FSSICT_LIST.append(FSSICT)
        FTANFYN_LIST.append(FTANFYN)
        FTANFCT_LIST.append(FTANFCT)
        FOWBENYN_LIST.append(FOWBENYN)
        FOWBENCT_LIST.append(FOWBENCT)
        FINTR1YN_LIST.append(FINTR1YN)
        FINTR1CT_LIST.append(FINTR1CT)
        FDIVDYN_LIST.append(FDIVDYN)
        FDIVDCT_LIST.append(FDIVDCT)
        FCHSPYN_LIST.append(FCHSPYN)
        FCHSPCT_LIST.append(FCHSPCT)
        FINCOTYN_LIST.append(FINCOTYN)
        FINCOTCT_LIST.append(FINCOTCT)
        INCGRP4_LIST.append(INCGRP4)
        INCGRP5_LIST.append(INCGRP5)
        RAT_CAT4_LIST.append(RAT_CAT4)
        RAT_CAT5_LIST.append(RAT_CAT5)
        HOUSEOWN_LIST.append(HOUSEOWN)
        FGAH_LIST.append(FGAH)
        FSSAPLYN_LIST.append(FSSAPLYN)
        FSSAPLCT_LIST.append(FSSAPLCT)
        FSDAPLYN_LIST.append(FSDAPLYN)
        FSDAPLCT_LIST.append(FSDAPLCT)
        FSNAP_LIST.append(FSNAP)
        FSNAPMYR_LIST.append(FSNAPMYR)
        FWICYN_LIST.append(FWICYN)
        FWICCT_LIST.append(FWICCT)

df = pd.DataFrame(columns=(
                            'RECTYPE',
                            'SRVY_YR',
                            'HHX',
                            'FMX',
                            'WTFA_FAM',
                            'FINT_Y_P',
                            'FINT_M_P',
                            'ELN_FLG',
                            'CURWRKN',
                            'TELCELN',
                            'WRKCELN',
                            'PHONEUSE',
                            'FLNGINTV',
                            'FM_SIZE',
                            'FM_KIDS',
                            'FM_ELDR',
                            'FM_TYPE',
                            'FM_STRCP',
                            'FM_STRP',
                            'FM_EDUC1',
                            'FCHLMYN',
                            'FCHLMCT',
                            'FSPEDYN',
                            'FSPEDCT',
                            'FLAADLYN',
                            'FLAADLCT',
                            'FLIADLYN',
                            'FLIADLCT',
                            'FWKLIMYN',
                            'FWKLIMCT',
                            'FWALKYN',
                            'FWALKCT',
                            'FREMEMYN',
                            'FREMEMCT',
                            'FANYLYN',
                            'FANYLCT',
                            'FHSTATEX',
                            'FHSTATVG',
                            'FHSTATG',
                            'FHSTATFR',
                            'FHSTATPR',
                            'FSRUNOUT',
                            'FSLAST',
                            'FSBALANC',
                            'FSSKIP',
                            'FSSKDAYS',
                            'FSLESS',
                            'FSHUNGRY',
                            'FSWEIGHT',
                            'FSNOTEAT',
                            'FSNEDAYS',
                            'FDMEDYN',
                            'FDMEDCT',
                            'FNMEDYN',
                            'FNMEDCT',
                            'FHOSP2YN',
                            'FHOSP2CT',
                            'FHCHMYN',
                            'FHCHMCT',
                            'FHCPHRYN',
                            'FHCPHRCT',
                            'FHCDVYN',
                            'FHCDVCT',
                            'F10DVYN',
                            'F10DVCT',
                            'FHICOVYN',
                            'FHICOVCT',
                            'FHIPRVCT',
                            'FHIEXCT',
                            'FHISINCT',
                            'FHICARCT',
                            'FHICADCT',
                            'FHICHPCT',
                            'FHIMILCT',
                            'FHIIHSCT',
                            'FHIPUBCT',
                            'FHIOGVCT',
                            'FPRCOOH',
                            'FHIEBCCT',
                            'COVCONF',
                            'FHICOST',
                            'FMEDBILL',
                            'FMEDBPAY',
                            'FMEDBNOP',
                            'FSAF',
                            'FHDSTCT',
                            'FDGLWCT1',
                            'FDGLWCT2',
                            'FWRKLWCT',
                            'FSALYN',
                            'FSALCT',
                            'FSEINCYN',
                            'FSEINCCT',
                            'FSSRRYN',
                            'FSSRRCT',
                            'FPENSYN',
                            'FPENSCT',
                            'FOPENSYN',
                            'FOPENSCT',
                            'FSSIYN',
                            'FSSICT',
                            'FTANFYN',
                            'FTANFCT',
                            'FOWBENYN',
                            'FOWBENCT',
                            'FINTR1YN',
                            'FINTR1CT',
                            'FDIVDYN',
                            'FDIVDCT',
                            'FCHSPYN',
                            'FCHSPCT',
                            'FINCOTYN',
                            'FINCOTCT',
                            'INCGRP4',
                            'INCGRP5',
                            'RAT_CAT4',
                            'RAT_CAT5',
                            'HOUSEOWN',
                            'FGAH',
                            'FSSAPLYN',
                            'FSSAPLCT',
                            'FSDAPLYN',
                            'FSDAPLCT',
                            'FSNAP',
                            'FSNAPMYR',
                            'FWICYN',
                            'FWICCT'
                                    ))

for i in range(45596):
    df.loc[i] = [
                    RECTYPE_LIST[i],
                    SRVY_YR_LIST[i],
                    HHX_LIST[i],
                    FMX_LIST[i],
                    WTFA_FAM_LIST[i],
                    FINT_Y_P_LIST[i],
                    FINT_M_P_LIST[i],
                    ELN_FLG_LIST[i],
                    CURWRKN_LIST[i],
                    TELCELN_LIST[i],
                    WRKCELN_LIST[i],
                    PHONEUSE_LIST[i],
                    FLNGINTV_LIST[i],
                    FM_SIZE_LIST[i],
                    FM_KIDS_LIST[i],
                    FM_ELDR_LIST[i],
                    FM_TYPE_LIST[i],
                    FM_STRCP_LIST[i],
                    FM_STRP_LIST[i],
                    FM_EDUC1_LIST[i],
                    FCHLMYN_LIST[i],
                    FCHLMCT_LIST[i],
                    FSPEDYN_LIST[i],
                    FSPEDCT_LIST[i],
                    FLAADLYN_LIST[i],
                    FLAADLCT_LIST[i],
                    FLIADLYN_LIST[i],
                    FLIADLCT_LIST[i],
                    FWKLIMYN_LIST[i],
                    FWKLIMCT_LIST[i],
                    FWALKYN_LIST[i],
                    FWALKCT_LIST[i],
                    FREMEMYN_LIST[i],
                    FREMEMCT_LIST[i],
                    FANYLYN_LIST[i],
                    FANYLCT_LIST[i],
                    FHSTATEX_LIST[i],
                    FHSTATVG_LIST[i],
                    FHSTATG_LIST[i],
                    FHSTATFR_LIST[i],
                    FHSTATPR_LIST[i],
                    FSRUNOUT_LIST[i],
                    FSLAST_LIST[i],
                    FSBALANC_LIST[i],
                    FSSKIP_LIST[i],
                    FSSKDAYS_LIST[i],
                    FSLESS_LIST[i],
                    FSHUNGRY_LIST[i],
                    FSWEIGHT_LIST[i],
                    FSNOTEAT_LIST[i],
                    FSNEDAYS_LIST[i],
                    FDMEDYN_LIST[i],
                    FDMEDCT_LIST[i],
                    FNMEDYN_LIST[i],
                    FNMEDCT_LIST[i],
                    FHOSP2YN_LIST[i],
                    FHOSP2CT_LIST[i],
                    FHCHMYN_LIST[i],
                    FHCHMCT_LIST[i],
                    FHCPHRYN_LIST[i],
                    FHCPHRCT_LIST[i],
                    FHCDVYN_LIST[i],
                    FHCDVCT_LIST[i],
                    F10DVYN_LIST[i],
                    F10DVCT_LIST[i],
                    FHICOVYN_LIST[i],
                    FHICOVCT_LIST[i],
                    FHIPRVCT_LIST[i],
                    FHIEXCT_LIST[i],
                    FHISINCT_LIST[i],
                    FHICARCT_LIST[i],
                    FHICADCT_LIST[i],
                    FHICHPCT_LIST[i],
                    FHIMILCT_LIST[i],
                    FHIIHSCT_LIST[i],
                    FHIPUBCT_LIST[i],
                    FHIOGVCT_LIST[i],
                    FPRCOOH_LIST[i],
                    FHIEBCCT_LIST[i],
                    COVCONF_LIST[i],
                    FHICOST_LIST[i],
                    FMEDBILL_LIST[i],
                    FMEDBPAY_LIST[i],
                    FMEDBNOP_LIST[i],
                    FSAF_LIST[i],
                    FHDSTCT_LIST[i],
                    FDGLWCT1_LIST[i],
                    FDGLWCT2_LIST[i],
                    FWRKLWCT_LIST[i],
                    FSALYN_LIST[i],
                    FSALCT_LIST[i],
                    FSEINCYN_LIST[i],
                    FSEINCCT_LIST[i],
                    FSSRRYN_LIST[i],
                    FSSRRCT_LIST[i],
                    FPENSYN_LIST[i],
                    FPENSCT_LIST[i],
                    FOPENSYN_LIST[i],
                    FOPENSCT_LIST[i],
                    FSSIYN_LIST[i],
                    FSSICT_LIST[i],
                    FTANFYN_LIST[i],
                    FTANFCT_LIST[i],
                    FOWBENYN_LIST[i],
                    FOWBENCT_LIST[i],
                    FINTR1YN_LIST[i],
                    FINTR1CT_LIST[i],
                    FDIVDYN_LIST[i],
                    FDIVDCT_LIST[i],
                    FCHSPYN_LIST[i],
                    FCHSPCT_LIST[i],
                    FINCOTYN_LIST[i],
                    FINCOTCT_LIST[i],
                    INCGRP4_LIST[i],
                    INCGRP5_LIST[i],
                    RAT_CAT4_LIST[i],
                    RAT_CAT5_LIST[i],
                    HOUSEOWN_LIST[i],
                    FGAH_LIST[i],
                    FSSAPLYN_LIST[i],
                    FSSAPLCT_LIST[i],
                    FSDAPLYN_LIST[i],
                    FSDAPLCT_LIST[i],
                    FSNAP_LIST[i],
                    FSNAPMYR_LIST[i],
                    FWICYN_LIST[i],
                    FWICCT_LIST[i]
                                    ]
df = df.applymap(lambda x: np.nan if str(x).isspace() else x)
df.to_csv("nhis_2014_familyxx.csv")
