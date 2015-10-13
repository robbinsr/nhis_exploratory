import pandas as pd
import numpy as np

custom_parser_input_file_name = "nhis_2014_injpoiep.dat"

RECTYPE = ''
SRVY_YR = ''
HHX = ''
FMX = ''
FPX = ''
IPEPNO = ''
WTFA = ''
IPDATEM = ''
IPDATEY = ''
IPDATENO = ''
IPDATETP = ''
IPDATEMT = ''
RPCKDMR = ''
RPD = ''
BIETD = ''
EIETD = ''
EDIPBR = ''
IMPMETH = ''
MUMON = ''
MUYEAR = ''
ETFLG = ''
BEIFLG = ''
ICAUS = ''
ECAUS = ''
IJBODY1 = ''
IJBODY2 = ''
IJBODY3 = ''
IJBODY4 = ''
IJTYPE1A = ''
IJTYPE1B = ''
IJTYPE2A = ''
IJTYPE2B = ''
IJTYPE3A = ''
IJTYPE3B = ''
IJTYPE4A = ''
IJTYPE4B = ''
PPCC = ''
IPEV = ''
IPER = ''
IPDO = ''
IPPCHCP = ''
IPOTH = ''
IPHOSP = ''
IPIHNO = ''
IMTRAF = ''
IMVWHO = ''
IMVTYP = ''
ISBELT = ''
IHELMT = ''
IFALL1 = ''
IFALL2 = ''
IFALLWHY = ''
PPOIS = ''
IPWHAT1 = ''
IPWHAT2 = ''
IPWHER1 = ''
IPWHER2 = ''
IPEMP = ''
IPWKLS = ''
IPSTU = ''
IPSCLS = ''
ICD9_1 = ''
ICD9_2 = ''
ICD9_3 = ''
ICD9_4 = ''
ICD9_5 = ''
ICD9_6 = ''
ICD9_7 = ''
ICD9_8 = ''
ECODE_1T = ''
ECODE_2T = ''
ECODE_3T = ''

RECTYPE_LIST = []
SRVY_YR_LIST = []
HHX_LIST = []
FMX_LIST = []
FPX_LIST = []
IPEPNO_LIST = []
WTFA_LIST = []
IPDATEM_LIST = []
IPDATEY_LIST = []
IPDATENO_LIST = []
IPDATETP_LIST = []
IPDATEMT_LIST = []
RPCKDMR_LIST = []
RPD_LIST = []
BIETD_LIST = []
EIETD_LIST = []
EDIPBR_LIST = []
IMPMETH_LIST = []
MUMON_LIST = []
MUYEAR_LIST = []
ETFLG_LIST = []
BEIFLG_LIST = []
ICAUS_LIST = []
ECAUS_LIST = []
IJBODY1_LIST = []
IJBODY2_LIST = []
IJBODY3_LIST = []
IJBODY4_LIST = []
IJTYPE1A_LIST = []
IJTYPE1B_LIST = []
IJTYPE2A_LIST = []
IJTYPE2B_LIST = []
IJTYPE3A_LIST = []
IJTYPE3B_LIST = []
IJTYPE4A_LIST = []
IJTYPE4B_LIST = []
PPCC_LIST = []
IPEV_LIST = []
IPER_LIST = []
IPDO_LIST = []
IPPCHCP_LIST = []
IPOTH_LIST = []
IPHOSP_LIST = []
IPIHNO_LIST = []
IMTRAF_LIST = []
IMVWHO_LIST = []
IMVTYP_LIST = []
ISBELT_LIST = []
IHELMT_LIST = []
IFALL1_LIST = []
IFALL2_LIST = []
IFALLWHY_LIST = []
PPOIS_LIST = []
IPWHAT1_LIST = []
IPWHAT2_LIST = []
IPWHER1_LIST = []
IPWHER2_LIST = []
IPEMP_LIST = []
IPWKLS_LIST = []
IPSTU_LIST = []
IPSCLS_LIST = []
ICD9_1_LIST = []
ICD9_2_LIST = []
ICD9_3_LIST = []
ICD9_4_LIST = []
ICD9_5_LIST = []
ICD9_6_LIST = []
ICD9_7_LIST = []
ICD9_8_LIST = []
ECODE_1T_LIST = []
ECODE_2T_LIST = []
ECODE_3T_LIST = []

with open(custom_parser_input_file_name, encoding="utf8", mode="r") as f:
    for ldx, line in enumerate(f):
        if ldx < 20:
            RECTYPE_accumulator_LIST = []
            SRVY_YR_accumulator_LIST = []
            HHX_accumulator_LIST = []
            FMX_accumulator_LIST = []
            FPX_accumulator_LIST = []
            IPEPNO_accumulator_LIST = []
            WTFA_accumulator_LIST = []
            IPDATEM_accumulator_LIST = []
            IPDATEY_accumulator_LIST = []
            IPDATENO_accumulator_LIST = []
            IPDATETP_accumulator_LIST = []
            IPDATEMT_accumulator_LIST = []
            RPCKDMR_accumulator_LIST = []
            RPD_accumulator_LIST = []
            BIETD_accumulator_LIST = []
            EIETD_accumulator_LIST = []
            EDIPBR_accumulator_LIST = []
            IMPMETH_accumulator_LIST = []
            MUMON_accumulator_LIST = []
            MUYEAR_accumulator_LIST = []
            ETFLG_accumulator_LIST = []
            BEIFLG_accumulator_LIST = []
            ICAUS_accumulator_LIST = []
            ECAUS_accumulator_LIST = []
            IJBODY1_accumulator_LIST = []
            IJBODY2_accumulator_LIST = []
            IJBODY3_accumulator_LIST = []
            IJBODY4_accumulator_LIST = []
            IJTYPE1A_accumulator_LIST = []
            IJTYPE1B_accumulator_LIST = []
            IJTYPE2A_accumulator_LIST = []
            IJTYPE2B_accumulator_LIST = []
            IJTYPE3A_accumulator_LIST = []
            IJTYPE3B_accumulator_LIST = []
            IJTYPE4A_accumulator_LIST = []
            IJTYPE4B_accumulator_LIST = []
            PPCC_accumulator_LIST = []
            IPEV_accumulator_LIST = []
            IPER_accumulator_LIST = []
            IPDO_accumulator_LIST = []
            IPPCHCP_accumulator_LIST = []
            IPOTH_accumulator_LIST = []
            IPHOSP_accumulator_LIST = []
            IPIHNO_accumulator_LIST = []
            IMTRAF_accumulator_LIST = []
            IMVWHO_accumulator_LIST = []
            IMVTYP_accumulator_LIST = []
            ISBELT_accumulator_LIST = []
            IHELMT_accumulator_LIST = []
            IFALL1_accumulator_LIST = []
            IFALL2_accumulator_LIST = []
            IFALLWHY_accumulator_LIST = []
            PPOIS_accumulator_LIST = []
            IPWHAT1_accumulator_LIST = []
            IPWHAT2_accumulator_LIST = []
            IPWHER1_accumulator_LIST = []
            IPWHER2_accumulator_LIST = []
            IPEMP_accumulator_LIST = []
            IPWKLS_accumulator_LIST = []
            IPSTU_accumulator_LIST = []
            IPSCLS_accumulator_LIST = []
            ICD9_1_accumulator_LIST = []
            ICD9_2_accumulator_LIST = []
            ICD9_3_accumulator_LIST = []
            ICD9_4_accumulator_LIST = []
            ICD9_5_accumulator_LIST = []
            ICD9_6_accumulator_LIST = []
            ICD9_7_accumulator_LIST = []
            ICD9_8_accumulator_LIST = []
            ECODE_1T_accumulator_LIST = []
            ECODE_2T_accumulator_LIST = []
            ECODE_3T_accumulator_LIST = []

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
                elif 15 < cdx < 18:
                    IPEPNO_accumulator_LIST.append(char)
                    IPEPNO = ''.join(IPEPNO_accumulator_LIST)
                elif 17 < cdx < 24:
                    WTFA_accumulator_LIST.append(char)
                    WTFA = ''.join(WTFA_accumulator_LIST)
                elif 23 < cdx < 26:
                    IPDATEM_accumulator_LIST.append(char)
                    IPDATEM = ''.join(IPDATEM_accumulator_LIST)
                elif 25 < cdx < 30:
                    IPDATEY_accumulator_LIST.append(char)
                    IPDATEY = ''.join(IPDATEY_accumulator_LIST)
                elif 29 < cdx < 33:
                    IPDATENO_accumulator_LIST.append(char)
                    IPDATENO = ''.join(IPDATENO_accumulator_LIST)
                elif 32 < cdx < 34:
                    IPDATETP_accumulator_LIST.append(char)
                    IPDATETP = ''.join(IPDATETP_accumulator_LIST)
                elif 33 < cdx < 35:
                    IPDATEMT_accumulator_LIST.append(char)
                    IPDATEMT = ''.join(IPDATEMT_accumulator_LIST)
                elif 34 < cdx < 38:
                    RPCKDMR_accumulator_LIST.append(char)
                    RPCKDMR = ''.join(RPCKDMR_accumulator_LIST)
                elif 37 < cdx < 41:
                    RPD_accumulator_LIST.append(char)
                    RPD = ''.join(RPD_accumulator_LIST)
                elif 40 < cdx < 44:
                    BIETD_accumulator_LIST.append(char)
                    BIETD = ''.join(BIETD_accumulator_LIST)
                elif 43 < cdx < 47:
                    EIETD_accumulator_LIST.append(char)
                    EIETD = ''.join(EIETD_accumulator_LIST)
                elif 46 < cdx < 48:
                    EDIPBR_accumulator_LIST.append(char)
                    EDIPBR = ''.join(EDIPBR_accumulator_LIST)
                elif 47 < cdx < 49:
                    IMPMETH_accumulator_LIST.append(char)
                    IMPMETH = ''.join(IMPMETH_accumulator_LIST)
                elif 48 < cdx < 51:
                    MUMON_accumulator_LIST.append(char)
                    MUMON = ''.join(MUMON_accumulator_LIST)
                elif 50 < cdx < 55:
                    MUYEAR_accumulator_LIST.append(char)
                    MUYEAR = ''.join(MUYEAR_accumulator_LIST)
                elif 54 < cdx < 56:
                    ETFLG_accumulator_LIST.append(char)
                    ETFLG = ''.join(ETFLG_accumulator_LIST)
                elif 55 < cdx < 57:
                    BEIFLG_accumulator_LIST.append(char)
                    BEIFLG = ''.join(BEIFLG_accumulator_LIST)
                elif 56 < cdx < 59:
                    ICAUS_accumulator_LIST.append(char)
                    ICAUS = ''.join(ICAUS_accumulator_LIST)
                elif 58 < cdx < 61:
                    ECAUS_accumulator_LIST.append(char)
                    ECAUS = ''.join(ECAUS_accumulator_LIST)
                elif 60 < cdx < 63:
                    IJBODY1_accumulator_LIST.append(char)
                    IJBODY1 = ''.join(IJBODY1_accumulator_LIST)
                elif 62 < cdx < 65:
                    IJBODY2_accumulator_LIST.append(char)
                    IJBODY2 = ''.join(IJBODY2_accumulator_LIST)
                elif 64 < cdx < 67:
                    IJBODY3_accumulator_LIST.append(char)
                    IJBODY3 = ''.join(IJBODY3_accumulator_LIST)
                elif 66 < cdx < 69:
                    IJBODY4_accumulator_LIST.append(char)
                    IJBODY4 = ''.join(IJBODY4_accumulator_LIST)
                elif 68 < cdx < 71:
                    IJTYPE1A_accumulator_LIST.append(char)
                    IJTYPE1A = ''.join(IJTYPE1A_accumulator_LIST)
                elif 70 < cdx < 73:
                    IJTYPE1B_accumulator_LIST.append(char)
                    IJTYPE1B = ''.join(IJTYPE1B_accumulator_LIST)
                elif 72 < cdx < 75:
                    IJTYPE2A_accumulator_LIST.append(char)
                    IJTYPE2A = ''.join(IJTYPE2A_accumulator_LIST)
                elif 74 < cdx < 77:
                    IJTYPE2B_accumulator_LIST.append(char)
                    IJTYPE2B = ''.join(IJTYPE2B_accumulator_LIST)
                elif 76 < cdx < 79:
                    IJTYPE3A_accumulator_LIST.append(char)
                    IJTYPE3A = ''.join(IJTYPE3A_accumulator_LIST)
                elif 78 < cdx < 81:
                    IJTYPE3B_accumulator_LIST.append(char)
                    IJTYPE3B = ''.join(IJTYPE3B_accumulator_LIST)
                elif 80 < cdx < 83:
                    IJTYPE4A_accumulator_LIST.append(char)
                    IJTYPE4A = ''.join(IJTYPE4A_accumulator_LIST)
                elif 82 < cdx < 85:
                    IJTYPE4B_accumulator_LIST.append(char)
                    IJTYPE4B = ''.join(IJTYPE4B_accumulator_LIST)
                elif 84 < cdx < 86:
                    PPCC_accumulator_LIST.append(char)
                    PPCC = ''.join(PPCC_accumulator_LIST)
                elif 85 < cdx < 87:
                    IPEV_accumulator_LIST.append(char)
                    IPEV = ''.join(IPEV_accumulator_LIST)
                elif 86 < cdx < 88:
                    IPER_accumulator_LIST.append(char)
                    IPER = ''.join(IPER_accumulator_LIST)
                elif 87 < cdx < 89:
                    IPDO_accumulator_LIST.append(char)
                    IPDO = ''.join(IPDO_accumulator_LIST)
                elif 88 < cdx < 90:
                    IPPCHCP_accumulator_LIST.append(char)
                    IPPCHCP = ''.join(IPPCHCP_accumulator_LIST)
                elif 89 < cdx < 91:
                    IPOTH_accumulator_LIST.append(char)
                    IPOTH = ''.join(IPOTH_accumulator_LIST)
                elif 90 < cdx < 92:
                    IPHOSP_accumulator_LIST.append(char)
                    IPHOSP = ''.join(IPHOSP_accumulator_LIST)
                elif 91 < cdx < 94:
                    IPIHNO_accumulator_LIST.append(char)
                    IPIHNO = ''.join(IPIHNO_accumulator_LIST)
                elif 93 < cdx < 95:
                    IMTRAF_accumulator_LIST.append(char)
                    IMTRAF = ''.join(IMTRAF_accumulator_LIST)
                elif 94 < cdx < 96:
                    IMVWHO_accumulator_LIST.append(char)
                    IMVWHO = ''.join(IMVWHO_accumulator_LIST)
                elif 95 < cdx < 98:
                    IMVTYP_accumulator_LIST.append(char)
                    IMVTYP = ''.join(IMVTYP_accumulator_LIST)
                elif 97 < cdx < 99:
                    ISBELT_accumulator_LIST.append(char)
                    ISBELT = ''.join(ISBELT_accumulator_LIST)
                elif 98 < cdx < 100:
                    IHELMT_accumulator_LIST.append(char)
                    IHELMT = ''.join(IHELMT_accumulator_LIST)
                elif 99 < cdx < 102:
                    IFALL1_accumulator_LIST.append(char)
                    IFALL1 = ''.join(IFALL1_accumulator_LIST)
                elif 101 < cdx < 104:
                    IFALL2_accumulator_LIST.append(char)
                    IFALL2 = ''.join(IFALL2_accumulator_LIST)
                elif 103 < cdx < 105:
                    IFALLWHY_accumulator_LIST.append(char)
                    IFALLWHY = ''.join(IFALLWHY_accumulator_LIST)
                elif 104 < cdx < 106:
                    PPOIS_accumulator_LIST.append(char)
                    PPOIS = ''.join(PPOIS_accumulator_LIST)
                elif 105 < cdx < 108:
                    IPWHAT1_accumulator_LIST.append(char)
                    IPWHAT1 = ''.join(IPWHAT1_accumulator_LIST)
                elif 107 < cdx < 110:
                    IPWHAT2_accumulator_LIST.append(char)
                    IPWHAT2 = ''.join(IPWHAT2_accumulator_LIST)
                elif 109 < cdx < 112:
                    IPWHER1_accumulator_LIST.append(char)
                    IPWHER1 = ''.join(IPWHER1_accumulator_LIST)
                elif 111 < cdx < 114:
                    IPWHER2_accumulator_LIST.append(char)
                    IPWHER2 = ''.join(IPWHER2_accumulator_LIST)
                elif 113 < cdx < 115:
                    IPEMP_accumulator_LIST.append(char)
                    IPEMP = ''.join(IPEMP_accumulator_LIST)
                elif 114 < cdx < 116:
                    IPWKLS_accumulator_LIST.append(char)
                    IPWKLS = ''.join(IPWKLS_accumulator_LIST)
                elif 115 < cdx < 117:
                    IPSTU_accumulator_LIST.append(char)
                    IPSTU = ''.join(IPSTU_accumulator_LIST)
                elif 116 < cdx < 118:
                    IPSCLS_accumulator_LIST.append(char)
                    IPSCLS = ''.join(IPSCLS_accumulator_LIST)
                elif 117 < cdx < 123:
                    ICD9_1_accumulator_LIST.append(char)
                    ICD9_1 = ''.join(ICD9_1_accumulator_LIST)
                elif 122 < cdx < 128:
                    ICD9_2_accumulator_LIST.append(char)
                    ICD9_2 = ''.join(ICD9_2_accumulator_LIST)
                elif 127 < cdx < 133:
                    ICD9_3_accumulator_LIST.append(char)
                    ICD9_3 = ''.join(ICD9_3_accumulator_LIST)
                elif 132 < cdx < 138:
                    ICD9_4_accumulator_LIST.append(char)
                    ICD9_4 = ''.join(ICD9_4_accumulator_LIST)
                elif 137 < cdx < 143:
                    ICD9_5_accumulator_LIST.append(char)
                    ICD9_5 = ''.join(ICD9_5_accumulator_LIST)
                elif 142 < cdx < 148:
                    ICD9_6_accumulator_LIST.append(char)
                    ICD9_6 = ''.join(ICD9_6_accumulator_LIST)
                elif 147 < cdx < 153:
                    ICD9_7_accumulator_LIST.append(char)
                    ICD9_7 = ''.join(ICD9_7_accumulator_LIST)
                elif 152 < cdx < 158:
                    ICD9_8_accumulator_LIST.append(char)
                    ICD9_8 = ''.join(ICD9_8_accumulator_LIST)
                elif 157 < cdx < 163:
                    ECODE_1T_accumulator_LIST.append(char)
                    ECODE_1T = ''.join(ECODE_1T_accumulator_LIST)
                elif 162 < cdx < 168:
                    ECODE_2T_accumulator_LIST.append(char)
                    ECODE_2T = ''.join(ECODE_2T_accumulator_LIST)
                elif 167 < cdx < 173:
                    ECODE_3T_accumulator_LIST.append(char)
                    ECODE_3T = ''.join(ECODE_3T_accumulator_LIST)
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
        IPEPNO_LIST.append(IPEPNO)
        WTFA_LIST.append(WTFA)
        IPDATEM_LIST.append(IPDATEM)
        IPDATEY_LIST.append(IPDATEY)
        IPDATENO_LIST.append(IPDATENO)
        IPDATETP_LIST.append(IPDATETP)
        IPDATEMT_LIST.append(IPDATEMT)
        RPCKDMR_LIST.append(RPCKDMR)
        RPD_LIST.append(RPD)
        BIETD_LIST.append(BIETD)
        EIETD_LIST.append(EIETD)
        EDIPBR_LIST.append(EDIPBR)
        IMPMETH_LIST.append(IMPMETH)
        MUMON_LIST.append(MUMON)
        MUYEAR_LIST.append(MUYEAR)
        ETFLG_LIST.append(ETFLG)
        BEIFLG_LIST.append(BEIFLG)
        ICAUS_LIST.append(ICAUS)
        ECAUS_LIST.append(ECAUS)
        IJBODY1_LIST.append(IJBODY1)
        IJBODY2_LIST.append(IJBODY2)
        IJBODY3_LIST.append(IJBODY3)
        IJBODY4_LIST.append(IJBODY4)
        IJTYPE1A_LIST.append(IJTYPE1A)
        IJTYPE1B_LIST.append(IJTYPE1B)
        IJTYPE2A_LIST.append(IJTYPE2A)
        IJTYPE2B_LIST.append(IJTYPE2B)
        IJTYPE3A_LIST.append(IJTYPE3A)
        IJTYPE3B_LIST.append(IJTYPE3B)
        IJTYPE4A_LIST.append(IJTYPE4A)
        IJTYPE4B_LIST.append(IJTYPE4B)
        PPCC_LIST.append(PPCC)
        IPEV_LIST.append(IPEV)
        IPER_LIST.append(IPER)
        IPDO_LIST.append(IPDO)
        IPPCHCP_LIST.append(IPPCHCP)
        IPOTH_LIST.append(IPOTH)
        IPHOSP_LIST.append(IPHOSP)
        IPIHNO_LIST.append(IPIHNO)
        IMTRAF_LIST.append(IMTRAF)
        IMVWHO_LIST.append(IMVWHO)
        IMVTYP_LIST.append(IMVTYP)
        ISBELT_LIST.append(ISBELT)
        IHELMT_LIST.append(IHELMT)
        IFALL1_LIST.append(IFALL1)
        IFALL2_LIST.append(IFALL2)
        IFALLWHY_LIST.append(IFALLWHY)
        PPOIS_LIST.append(PPOIS)
        IPWHAT1_LIST.append(IPWHAT1)
        IPWHAT2_LIST.append(IPWHAT2)
        IPWHER1_LIST.append(IPWHER1)
        IPWHER2_LIST.append(IPWHER2)
        IPEMP_LIST.append(IPEMP)
        IPWKLS_LIST.append(IPWKLS)
        IPSTU_LIST.append(IPSTU)
        IPSCLS_LIST.append(IPSCLS)
        ICD9_1_LIST.append(ICD9_1)
        ICD9_2_LIST.append(ICD9_2)
        ICD9_3_LIST.append(ICD9_3)
        ICD9_4_LIST.append(ICD9_4)
        ICD9_5_LIST.append(ICD9_5)
        ICD9_6_LIST.append(ICD9_6)
        ICD9_7_LIST.append(ICD9_7)
        ICD9_8_LIST.append(ICD9_8)
        ECODE_1T_LIST.append(ECODE_1T)
        ECODE_2T_LIST.append(ECODE_2T)
        ECODE_3T_LIST.append(ECODE_3T)

df = pd.DataFrame(columns=(
                            'RECTYPE',
                            'SRVY_YR',
                            'HHX',
                            'FMX',
                            'FPX',
                            'IPEPNO',
                            'WTFA',
                            'IPDATEM',
                            'IPDATEY',
                            'IPDATENO',
                            'IPDATETP',
                            'IPDATEMT',
                            'RPCKDMR',
                            'RPD',
                            'BIETD',
                            'EIETD',
                            'EDIPBR',
                            'IMPMETH',
                            'MUMON',
                            'MUYEAR',
                            'ETFLG',
                            'BEIFLG',
                            'ICAUS',
                            'ECAUS',
                            'IJBODY1',
                            'IJBODY2',
                            'IJBODY3',
                            'IJBODY4',
                            'IJTYPE1A',
                            'IJTYPE1B',
                            'IJTYPE2A',
                            'IJTYPE2B',
                            'IJTYPE3A',
                            'IJTYPE3B',
                            'IJTYPE4A',
                            'IJTYPE4B',
                            'PPCC',
                            'IPEV',
                            'IPER',
                            'IPDO',
                            'IPPCHCP',
                            'IPOTH',
                            'IPHOSP',
                            'IPIHNO',
                            'IMTRAF',
                            'IMVWHO',
                            'IMVTYP',
                            'ISBELT',
                            'IHELMT',
                            'IFALL1',
                            'IFALL2',
                            'IFALLWHY',
                            'PPOIS',
                            'IPWHAT1',
                            'IPWHAT2',
                            'IPWHER1',
                            'IPWHER2',
                            'IPEMP',
                            'IPWKLS',
                            'IPSTU',
                            'IPSCLS',
                            'ICD9_1',
                            'ICD9_2',
                            'ICD9_3',
                            'ICD9_4',
                            'ICD9_5',
                            'ICD9_6',
                            'ICD9_7',
                            'ICD9_8',
                            'ECODE_1T',
                            'ECODE_2T',
                            'ECODE_3T'
                                    ))

for i in range(20):
    df.loc[i] = [
                    RECTYPE_LIST[i],
                    SRVY_YR_LIST[i],
                    HHX_LIST[i],
                    FMX_LIST[i],
                    FPX_LIST[i],
                    IPEPNO_LIST[i],
                    WTFA_LIST[i],
                    IPDATEM_LIST[i],
                    IPDATEY_LIST[i],
                    IPDATENO_LIST[i],
                    IPDATETP_LIST[i],
                    IPDATEMT_LIST[i],
                    RPCKDMR_LIST[i],
                    RPD_LIST[i],
                    BIETD_LIST[i],
                    EIETD_LIST[i],
                    EDIPBR_LIST[i],
                    IMPMETH_LIST[i],
                    MUMON_LIST[i],
                    MUYEAR_LIST[i],
                    ETFLG_LIST[i],
                    BEIFLG_LIST[i],
                    ICAUS_LIST[i],
                    ECAUS_LIST[i],
                    IJBODY1_LIST[i],
                    IJBODY2_LIST[i],
                    IJBODY3_LIST[i],
                    IJBODY4_LIST[i],
                    IJTYPE1A_LIST[i],
                    IJTYPE1B_LIST[i],
                    IJTYPE2A_LIST[i],
                    IJTYPE2B_LIST[i],
                    IJTYPE3A_LIST[i],
                    IJTYPE3B_LIST[i],
                    IJTYPE4A_LIST[i],
                    IJTYPE4B_LIST[i],
                    PPCC_LIST[i],
                    IPEV_LIST[i],
                    IPER_LIST[i],
                    IPDO_LIST[i],
                    IPPCHCP_LIST[i],
                    IPOTH_LIST[i],
                    IPHOSP_LIST[i],
                    IPIHNO_LIST[i],
                    IMTRAF_LIST[i],
                    IMVWHO_LIST[i],
                    IMVTYP_LIST[i],
                    ISBELT_LIST[i],
                    IHELMT_LIST[i],
                    IFALL1_LIST[i],
                    IFALL2_LIST[i],
                    IFALLWHY_LIST[i],
                    PPOIS_LIST[i],
                    IPWHAT1_LIST[i],
                    IPWHAT2_LIST[i],
                    IPWHER1_LIST[i],
                    IPWHER2_LIST[i],
                    IPEMP_LIST[i],
                    IPWKLS_LIST[i],
                    IPSTU_LIST[i],
                    IPSCLS_LIST[i],
                    ICD9_1_LIST[i],
                    ICD9_2_LIST[i],
                    ICD9_3_LIST[i],
                    ICD9_4_LIST[i],
                    ICD9_5_LIST[i],
                    ICD9_6_LIST[i],
                    ICD9_7_LIST[i],
                    ICD9_8_LIST[i],
                    ECODE_1T_LIST[i],
                    ECODE_2T_LIST[i],
                    ECODE_3T_LIST[i]
                                    ]
df = df.applymap(lambda x: np.nan if str(x).isspace() else x)
df.to_csv("nhis_2014_injpoiep.csv")
