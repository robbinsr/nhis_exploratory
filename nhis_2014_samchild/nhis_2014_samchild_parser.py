import pandas as pd
import numpy as np

custom_parser_input_file_name = "nhis_2014_samchild.dat"

RECTYPE = ''
SRVY_YR = ''
HHX = ''
INTV_QRT = ''
INTV_MON = ''
FMX = ''
FPX = ''
WTIA_SC = ''
WTFA_SC = ''
REGION = ''
STRAT_P = ''
PSU_P = ''
SEX = ''
HISPAN_I = ''
RACERPI2 = ''
MRACRPI2 = ''
MRACBPI2 = ''
AGE_P = ''
CSRESPNO = ''
CSRELTVP = ''
LATEINTC = ''
FDRN_FLG = ''
TOTOZ_P = ''
BWTGRM_P = ''
CHGHT_TC = ''
CWGHT_TC = ''
BMI_SC = ''
AMR1R = ''
AODD1 = ''
ADD2 = ''
AMR2R = ''
AUTISM = ''
AODD2 = ''
CCONDRR1 = ''
CCONDRR2 = ''
CCONDRR3 = ''
CCONDRR4 = ''
CCONDRR5 = ''
CCONDRR6 = ''
CCONDRR7 = ''
CCONDRR8 = ''
CCONDRR9 = ''
CPOX = ''
CPOX12MO = ''
CASHMEV = ''
CASSTILL = ''
CASHYR = ''
CASERYR1 = ''
HAYF1 = ''
RALLG1 = ''
DALLG1 = ''
SALLG1 = ''
DIARH1 = ''
ANEMIA1 = ''
EARINF1 = ''
SEIZE1 = ''
HAYF2 = ''
RALLG2 = ''
DALLG2 = ''
SALLG2 = ''
DIARH2 = ''
ANEMIA2 = ''
FHEAD = ''
EARINF2 = ''
SEIZE2 = ''
STUTTER = ''
CHSTATYR = ''
SCHDAYR1 = ''
CCOLD2W = ''
CINTIL2W = ''
CHEARST2 = ''
CHRWORS = ''
CHRWORSE = ''
CHRWHIS1 = ''
CHRTALK1 = ''
CHRSHOU1 = ''
CHRSPEA1 = ''
CHRCOCR1 = ''
CHRCOCI1 = ''
CHRFAM = ''
CHRMIS = ''
CHRUNDST = ''
CHRUNDNS = ''
CHEARAG1 = ''
CHRCAUS1 = ''
CHRPRBHP = ''
CHRENT = ''
CHREHDI = ''
CHREIAGE = ''
CHRTUBE = ''
CHRTBAGE = ''
CHRTSCH = ''
CHRTSCHM = ''
CHRTSCHR = ''
CHRTEST = ''
CHRAIDNW = ''
CHRAIDLG = ''
CHRAIDYR = ''
CHRAIDEV = ''
CHRAIDRC = ''
CHRAIDLP = ''
CHRAIDOF = ''
CHRAID01 = ''
CHRAID02 = ''
CHRAID03 = ''
CHRAID04 = ''
CHRAID05 = ''
CHRAID06 = ''
CHRAID07 = ''
CHRAID08 = ''
CHRAID09 = ''
CHRAID10 = ''
CHRAID11 = ''
CHRAUD = ''
CHRALDS = ''
CHRALD01 = ''
CHRALD02 = ''
CHRALD03 = ''
CHRALD04 = ''
CHRALD05 = ''
CHRALD06 = ''
CHRALD07 = ''
CHRALD08 = ''
CHRALD09 = ''
CHRALD10 = ''
CHRALD11 = ''
CHRALD12 = ''
CHRFIRE = ''
CHRFRCRK = ''
CHRTOTR = ''
CHRFRPRT = ''
CHRWKVLN = ''
CHRWKVLT = ''
CHRWKPRT = ''
CHRLESNS = ''
CHRLST01 = ''
CHRLST02 = ''
CHRLST03 = ''
CHRLST04 = ''
CHRLST05 = ''
CHRLST06 = ''
CHRLST07 = ''
CHRLST08 = ''
CHRLST09 = ''
CHRLST10 = ''
CHRLST11 = ''
CHRLST12 = ''
CHRLSPRT = ''
CHRINT = ''
CHRINTHL = ''
CHRINTHA = ''
CHRINTHP = ''
CHRINHPR = ''
CVISION = ''
CBLIND = ''
IHSPEQ = ''
IHMOB = ''
IHMOBYR = ''
PROBRX = ''
LEARND = ''
MHIBOY2 = ''
CMHAGM15 = ''
MHIGRL2 = ''
CMHAGF15 = ''
CUSUALPL = ''
CPLKIND = ''
CHCPLROU = ''
CHCPLKND = ''
CHCCHGYR = ''
CHCCHGHI = ''
CNOUSPL1 = ''
CNOUSPL2 = ''
CNOUSPL3 = ''
CNOUSPL4 = ''
CNOUSPL5 = ''
CNOUSPL6 = ''
CNOUSPL7 = ''
CNOUSPL8 = ''
CNOUSPL9 = ''
CPRVTRYR = ''
CPRVTRFD = ''
CDRNANP = ''
CDRNAI = ''
CHCDLYR1 = ''
CHCDLYR2 = ''
CHCDLYR3 = ''
CHCDLYR4 = ''
CHCDLYR5 = ''
CHCAFYR = ''
CHCAFYRN = ''
CHCAFYRF = ''
CHCAFYR1 = ''
CHCAFYR2 = ''
CHCAFYR3 = ''
CHCAFYR4 = ''
CHCAFYR5 = ''
CHCAFYR6 = ''
CDNLONGR = ''
CHCSYR11 = ''
CHCSYR12 = ''
CHCSYR13 = ''
CHCSYR14 = ''
CHCSYR1 = ''
CHCSYR2 = ''
CHCSYR3 = ''
CHCSYR4 = ''
CHCSYR5 = ''
CHCSYR6 = ''
CHCSYR7 = ''
CHCSYR81 = ''
CHCSYR82 = ''
CHCSYR10 = ''
CHCSYREM = ''
CHPXYR_C = ''
CHERNOY2 = ''
CERVISND = ''
CERHOS = ''
CERREA1R = ''
CERREA2R = ''
CERREA3R = ''
CERREA4R = ''
CERREA5R = ''
CERREA6R = ''
CERREA7R = ''
CERREA8R = ''
CHCHYR = ''
CHCHMOYR = ''
CHCHNOY2 = ''
CHCNOYR2 = ''
CSRGYR = ''
RSRGNOYR = ''
CMDLONGR = ''
RSCL2_C2 = ''
RSCL2_E2 = ''
RSCL3_E3 = ''
RSCL5_P5 = ''
RSCL5_H5 = ''
RSCL6 = ''
CSHFLU12 = ''
CSHFLUNM = ''
CSHFLUM1 = ''
CSHFLUY1 = ''
CSHSPFL1 = ''
CSHFLUM2 = ''
CSHFLUY2 = ''
CSHSPFL2 = ''

RECTYPE_LIST = []
SRVY_YR_LIST = []
HHX_LIST = []
INTV_QRT_LIST = []
INTV_MON_LIST = []
FMX_LIST = []
FPX_LIST = []
WTIA_SC_LIST = []
WTFA_SC_LIST = []
REGION_LIST = []
STRAT_P_LIST = []
PSU_P_LIST = []
SEX_LIST = []
HISPAN_I_LIST = []
RACERPI2_LIST = []
MRACRPI2_LIST = []
MRACBPI2_LIST = []
AGE_P_LIST = []
CSRESPNO_LIST = []
CSRELTVP_LIST = []
LATEINTC_LIST = []
FDRN_FLG_LIST = []
TOTOZ_P_LIST = []
BWTGRM_P_LIST = []
CHGHT_TC_LIST = []
CWGHT_TC_LIST = []
BMI_SC_LIST = []
AMR1R_LIST = []
AODD1_LIST = []
ADD2_LIST = []
AMR2R_LIST = []
AUTISM_LIST = []
AODD2_LIST = []
CCONDRR1_LIST = []
CCONDRR2_LIST = []
CCONDRR3_LIST = []
CCONDRR4_LIST = []
CCONDRR5_LIST = []
CCONDRR6_LIST = []
CCONDRR7_LIST = []
CCONDRR8_LIST = []
CCONDRR9_LIST = []
CPOX_LIST = []
CPOX12MO_LIST = []
CASHMEV_LIST = []
CASSTILL_LIST = []
CASHYR_LIST = []
CASERYR1_LIST = []
HAYF1_LIST = []
RALLG1_LIST = []
DALLG1_LIST = []
SALLG1_LIST = []
DIARH1_LIST = []
ANEMIA1_LIST = []
EARINF1_LIST = []
SEIZE1_LIST = []
HAYF2_LIST = []
RALLG2_LIST = []
DALLG2_LIST = []
SALLG2_LIST = []
DIARH2_LIST = []
ANEMIA2_LIST = []
FHEAD_LIST = []
EARINF2_LIST = []
SEIZE2_LIST = []
STUTTER_LIST = []
CHSTATYR_LIST = []
SCHDAYR1_LIST = []
CCOLD2W_LIST = []
CINTIL2W_LIST = []
CHEARST2_LIST = []
CHRWORS_LIST = []
CHRWORSE_LIST = []
CHRWHIS1_LIST = []
CHRTALK1_LIST = []
CHRSHOU1_LIST = []
CHRSPEA1_LIST = []
CHRCOCR1_LIST = []
CHRCOCI1_LIST = []
CHRFAM_LIST = []
CHRMIS_LIST = []
CHRUNDST_LIST = []
CHRUNDNS_LIST = []
CHEARAG1_LIST = []
CHRCAUS1_LIST = []
CHRPRBHP_LIST = []
CHRENT_LIST = []
CHREHDI_LIST = []
CHREIAGE_LIST = []
CHRTUBE_LIST = []
CHRTBAGE_LIST = []
CHRTSCH_LIST = []
CHRTSCHM_LIST = []
CHRTSCHR_LIST = []
CHRTEST_LIST = []
CHRAIDNW_LIST = []
CHRAIDLG_LIST = []
CHRAIDYR_LIST = []
CHRAIDEV_LIST = []
CHRAIDRC_LIST = []
CHRAIDLP_LIST = []
CHRAIDOF_LIST = []
CHRAID01_LIST = []
CHRAID02_LIST = []
CHRAID03_LIST = []
CHRAID04_LIST = []
CHRAID05_LIST = []
CHRAID06_LIST = []
CHRAID07_LIST = []
CHRAID08_LIST = []
CHRAID09_LIST = []
CHRAID10_LIST = []
CHRAID11_LIST = []
CHRAUD_LIST = []
CHRALDS_LIST = []
CHRALD01_LIST = []
CHRALD02_LIST = []
CHRALD03_LIST = []
CHRALD04_LIST = []
CHRALD05_LIST = []
CHRALD06_LIST = []
CHRALD07_LIST = []
CHRALD08_LIST = []
CHRALD09_LIST = []
CHRALD10_LIST = []
CHRALD11_LIST = []
CHRALD12_LIST = []
CHRFIRE_LIST = []
CHRFRCRK_LIST = []
CHRTOTR_LIST = []
CHRFRPRT_LIST = []
CHRWKVLN_LIST = []
CHRWKVLT_LIST = []
CHRWKPRT_LIST = []
CHRLESNS_LIST = []
CHRLST01_LIST = []
CHRLST02_LIST = []
CHRLST03_LIST = []
CHRLST04_LIST = []
CHRLST05_LIST = []
CHRLST06_LIST = []
CHRLST07_LIST = []
CHRLST08_LIST = []
CHRLST09_LIST = []
CHRLST10_LIST = []
CHRLST11_LIST = []
CHRLST12_LIST = []
CHRLSPRT_LIST = []
CHRINT_LIST = []
CHRINTHL_LIST = []
CHRINTHA_LIST = []
CHRINTHP_LIST = []
CHRINHPR_LIST = []
CVISION_LIST = []
CBLIND_LIST = []
IHSPEQ_LIST = []
IHMOB_LIST = []
IHMOBYR_LIST = []
PROBRX_LIST = []
LEARND_LIST = []
MHIBOY2_LIST = []
CMHAGM15_LIST = []
MHIGRL2_LIST = []
CMHAGF15_LIST = []
CUSUALPL_LIST = []
CPLKIND_LIST = []
CHCPLROU_LIST = []
CHCPLKND_LIST = []
CHCCHGYR_LIST = []
CHCCHGHI_LIST = []
CNOUSPL1_LIST = []
CNOUSPL2_LIST = []
CNOUSPL3_LIST = []
CNOUSPL4_LIST = []
CNOUSPL5_LIST = []
CNOUSPL6_LIST = []
CNOUSPL7_LIST = []
CNOUSPL8_LIST = []
CNOUSPL9_LIST = []
CPRVTRYR_LIST = []
CPRVTRFD_LIST = []
CDRNANP_LIST = []
CDRNAI_LIST = []
CHCDLYR1_LIST = []
CHCDLYR2_LIST = []
CHCDLYR3_LIST = []
CHCDLYR4_LIST = []
CHCDLYR5_LIST = []
CHCAFYR_LIST = []
CHCAFYRN_LIST = []
CHCAFYRF_LIST = []
CHCAFYR1_LIST = []
CHCAFYR2_LIST = []
CHCAFYR3_LIST = []
CHCAFYR4_LIST = []
CHCAFYR5_LIST = []
CHCAFYR6_LIST = []
CDNLONGR_LIST = []
CHCSYR11_LIST = []
CHCSYR12_LIST = []
CHCSYR13_LIST = []
CHCSYR14_LIST = []
CHCSYR1_LIST = []
CHCSYR2_LIST = []
CHCSYR3_LIST = []
CHCSYR4_LIST = []
CHCSYR5_LIST = []
CHCSYR6_LIST = []
CHCSYR7_LIST = []
CHCSYR81_LIST = []
CHCSYR82_LIST = []
CHCSYR10_LIST = []
CHCSYREM_LIST = []
CHPXYR_C_LIST = []
CHERNOY2_LIST = []
CERVISND_LIST = []
CERHOS_LIST = []
CERREA1R_LIST = []
CERREA2R_LIST = []
CERREA3R_LIST = []
CERREA4R_LIST = []
CERREA5R_LIST = []
CERREA6R_LIST = []
CERREA7R_LIST = []
CERREA8R_LIST = []
CHCHYR_LIST = []
CHCHMOYR_LIST = []
CHCHNOY2_LIST = []
CHCNOYR2_LIST = []
CSRGYR_LIST = []
RSRGNOYR_LIST = []
CMDLONGR_LIST = []
RSCL2_C2_LIST = []
RSCL2_E2_LIST = []
RSCL3_E3_LIST = []
RSCL5_P5_LIST = []
RSCL5_H5_LIST = []
RSCL6_LIST = []
CSHFLU12_LIST = []
CSHFLUNM_LIST = []
CSHFLUM1_LIST = []
CSHFLUY1_LIST = []
CSHSPFL1_LIST = []
CSHFLUM2_LIST = []
CSHFLUY2_LIST = []
CSHSPFL2_LIST = []

with open(custom_parser_input_file_name, encoding="utf8", mode="r") as f:
    for ldx, line in enumerate(f):
        if ldx < 13379:
            RECTYPE_accumulator_LIST = []
            SRVY_YR_accumulator_LIST = []
            HHX_accumulator_LIST = []
            INTV_QRT_accumulator_LIST = []
            INTV_MON_accumulator_LIST = []
            FMX_accumulator_LIST = []
            FPX_accumulator_LIST = []
            WTIA_SC_accumulator_LIST = []
            WTFA_SC_accumulator_LIST = []
            REGION_accumulator_LIST = []
            STRAT_P_accumulator_LIST = []
            PSU_P_accumulator_LIST = []
            SEX_accumulator_LIST = []
            HISPAN_I_accumulator_LIST = []
            RACERPI2_accumulator_LIST = []
            MRACRPI2_accumulator_LIST = []
            MRACBPI2_accumulator_LIST = []
            AGE_P_accumulator_LIST = []
            CSRESPNO_accumulator_LIST = []
            CSRELTVP_accumulator_LIST = []
            LATEINTC_accumulator_LIST = []
            FDRN_FLG_accumulator_LIST = []
            TOTOZ_P_accumulator_LIST = []
            BWTGRM_P_accumulator_LIST = []
            CHGHT_TC_accumulator_LIST = []
            CWGHT_TC_accumulator_LIST = []
            BMI_SC_accumulator_LIST = []
            AMR1R_accumulator_LIST = []
            AODD1_accumulator_LIST = []
            ADD2_accumulator_LIST = []
            AMR2R_accumulator_LIST = []
            AUTISM_accumulator_LIST = []
            AODD2_accumulator_LIST = []
            CCONDRR1_accumulator_LIST = []
            CCONDRR2_accumulator_LIST = []
            CCONDRR3_accumulator_LIST = []
            CCONDRR4_accumulator_LIST = []
            CCONDRR5_accumulator_LIST = []
            CCONDRR6_accumulator_LIST = []
            CCONDRR7_accumulator_LIST = []
            CCONDRR8_accumulator_LIST = []
            CCONDRR9_accumulator_LIST = []
            CPOX_accumulator_LIST = []
            CPOX12MO_accumulator_LIST = []
            CASHMEV_accumulator_LIST = []
            CASSTILL_accumulator_LIST = []
            CASHYR_accumulator_LIST = []
            CASERYR1_accumulator_LIST = []
            HAYF1_accumulator_LIST = []
            RALLG1_accumulator_LIST = []
            DALLG1_accumulator_LIST = []
            SALLG1_accumulator_LIST = []
            DIARH1_accumulator_LIST = []
            ANEMIA1_accumulator_LIST = []
            EARINF1_accumulator_LIST = []
            SEIZE1_accumulator_LIST = []
            HAYF2_accumulator_LIST = []
            RALLG2_accumulator_LIST = []
            DALLG2_accumulator_LIST = []
            SALLG2_accumulator_LIST = []
            DIARH2_accumulator_LIST = []
            ANEMIA2_accumulator_LIST = []
            FHEAD_accumulator_LIST = []
            EARINF2_accumulator_LIST = []
            SEIZE2_accumulator_LIST = []
            STUTTER_accumulator_LIST = []
            CHSTATYR_accumulator_LIST = []
            SCHDAYR1_accumulator_LIST = []
            CCOLD2W_accumulator_LIST = []
            CINTIL2W_accumulator_LIST = []
            CHEARST2_accumulator_LIST = []
            CHRWORS_accumulator_LIST = []
            CHRWORSE_accumulator_LIST = []
            CHRWHIS1_accumulator_LIST = []
            CHRTALK1_accumulator_LIST = []
            CHRSHOU1_accumulator_LIST = []
            CHRSPEA1_accumulator_LIST = []
            CHRCOCR1_accumulator_LIST = []
            CHRCOCI1_accumulator_LIST = []
            CHRFAM_accumulator_LIST = []
            CHRMIS_accumulator_LIST = []
            CHRUNDST_accumulator_LIST = []
            CHRUNDNS_accumulator_LIST = []
            CHEARAG1_accumulator_LIST = []
            CHRCAUS1_accumulator_LIST = []
            CHRPRBHP_accumulator_LIST = []
            CHRENT_accumulator_LIST = []
            CHREHDI_accumulator_LIST = []
            CHREIAGE_accumulator_LIST = []
            CHRTUBE_accumulator_LIST = []
            CHRTBAGE_accumulator_LIST = []
            CHRTSCH_accumulator_LIST = []
            CHRTSCHM_accumulator_LIST = []
            CHRTSCHR_accumulator_LIST = []
            CHRTEST_accumulator_LIST = []
            CHRAIDNW_accumulator_LIST = []
            CHRAIDLG_accumulator_LIST = []
            CHRAIDYR_accumulator_LIST = []
            CHRAIDEV_accumulator_LIST = []
            CHRAIDRC_accumulator_LIST = []
            CHRAIDLP_accumulator_LIST = []
            CHRAIDOF_accumulator_LIST = []
            CHRAID01_accumulator_LIST = []
            CHRAID02_accumulator_LIST = []
            CHRAID03_accumulator_LIST = []
            CHRAID04_accumulator_LIST = []
            CHRAID05_accumulator_LIST = []
            CHRAID06_accumulator_LIST = []
            CHRAID07_accumulator_LIST = []
            CHRAID08_accumulator_LIST = []
            CHRAID09_accumulator_LIST = []
            CHRAID10_accumulator_LIST = []
            CHRAID11_accumulator_LIST = []
            CHRAUD_accumulator_LIST = []
            CHRALDS_accumulator_LIST = []
            CHRALD01_accumulator_LIST = []
            CHRALD02_accumulator_LIST = []
            CHRALD03_accumulator_LIST = []
            CHRALD04_accumulator_LIST = []
            CHRALD05_accumulator_LIST = []
            CHRALD06_accumulator_LIST = []
            CHRALD07_accumulator_LIST = []
            CHRALD08_accumulator_LIST = []
            CHRALD09_accumulator_LIST = []
            CHRALD10_accumulator_LIST = []
            CHRALD11_accumulator_LIST = []
            CHRALD12_accumulator_LIST = []
            CHRFIRE_accumulator_LIST = []
            CHRFRCRK_accumulator_LIST = []
            CHRTOTR_accumulator_LIST = []
            CHRFRPRT_accumulator_LIST = []
            CHRWKVLN_accumulator_LIST = []
            CHRWKVLT_accumulator_LIST = []
            CHRWKPRT_accumulator_LIST = []
            CHRLESNS_accumulator_LIST = []
            CHRLST01_accumulator_LIST = []
            CHRLST02_accumulator_LIST = []
            CHRLST03_accumulator_LIST = []
            CHRLST04_accumulator_LIST = []
            CHRLST05_accumulator_LIST = []
            CHRLST06_accumulator_LIST = []
            CHRLST07_accumulator_LIST = []
            CHRLST08_accumulator_LIST = []
            CHRLST09_accumulator_LIST = []
            CHRLST10_accumulator_LIST = []
            CHRLST11_accumulator_LIST = []
            CHRLST12_accumulator_LIST = []
            CHRLSPRT_accumulator_LIST = []
            CHRINT_accumulator_LIST = []
            CHRINTHL_accumulator_LIST = []
            CHRINTHA_accumulator_LIST = []
            CHRINTHP_accumulator_LIST = []
            CHRINHPR_accumulator_LIST = []
            CVISION_accumulator_LIST = []
            CBLIND_accumulator_LIST = []
            IHSPEQ_accumulator_LIST = []
            IHMOB_accumulator_LIST = []
            IHMOBYR_accumulator_LIST = []
            PROBRX_accumulator_LIST = []
            LEARND_accumulator_LIST = []
            MHIBOY2_accumulator_LIST = []
            CMHAGM15_accumulator_LIST = []
            MHIGRL2_accumulator_LIST = []
            CMHAGF15_accumulator_LIST = []
            CUSUALPL_accumulator_LIST = []
            CPLKIND_accumulator_LIST = []
            CHCPLROU_accumulator_LIST = []
            CHCPLKND_accumulator_LIST = []
            CHCCHGYR_accumulator_LIST = []
            CHCCHGHI_accumulator_LIST = []
            CNOUSPL1_accumulator_LIST = []
            CNOUSPL2_accumulator_LIST = []
            CNOUSPL3_accumulator_LIST = []
            CNOUSPL4_accumulator_LIST = []
            CNOUSPL5_accumulator_LIST = []
            CNOUSPL6_accumulator_LIST = []
            CNOUSPL7_accumulator_LIST = []
            CNOUSPL8_accumulator_LIST = []
            CNOUSPL9_accumulator_LIST = []
            CPRVTRYR_accumulator_LIST = []
            CPRVTRFD_accumulator_LIST = []
            CDRNANP_accumulator_LIST = []
            CDRNAI_accumulator_LIST = []
            CHCDLYR1_accumulator_LIST = []
            CHCDLYR2_accumulator_LIST = []
            CHCDLYR3_accumulator_LIST = []
            CHCDLYR4_accumulator_LIST = []
            CHCDLYR5_accumulator_LIST = []
            CHCAFYR_accumulator_LIST = []
            CHCAFYRN_accumulator_LIST = []
            CHCAFYRF_accumulator_LIST = []
            CHCAFYR1_accumulator_LIST = []
            CHCAFYR2_accumulator_LIST = []
            CHCAFYR3_accumulator_LIST = []
            CHCAFYR4_accumulator_LIST = []
            CHCAFYR5_accumulator_LIST = []
            CHCAFYR6_accumulator_LIST = []
            CDNLONGR_accumulator_LIST = []
            CHCSYR11_accumulator_LIST = []
            CHCSYR12_accumulator_LIST = []
            CHCSYR13_accumulator_LIST = []
            CHCSYR14_accumulator_LIST = []
            CHCSYR1_accumulator_LIST = []
            CHCSYR2_accumulator_LIST = []
            CHCSYR3_accumulator_LIST = []
            CHCSYR4_accumulator_LIST = []
            CHCSYR5_accumulator_LIST = []
            CHCSYR6_accumulator_LIST = []
            CHCSYR7_accumulator_LIST = []
            CHCSYR81_accumulator_LIST = []
            CHCSYR82_accumulator_LIST = []
            CHCSYR10_accumulator_LIST = []
            CHCSYREM_accumulator_LIST = []
            CHPXYR_C_accumulator_LIST = []
            CHERNOY2_accumulator_LIST = []
            CERVISND_accumulator_LIST = []
            CERHOS_accumulator_LIST = []
            CERREA1R_accumulator_LIST = []
            CERREA2R_accumulator_LIST = []
            CERREA3R_accumulator_LIST = []
            CERREA4R_accumulator_LIST = []
            CERREA5R_accumulator_LIST = []
            CERREA6R_accumulator_LIST = []
            CERREA7R_accumulator_LIST = []
            CERREA8R_accumulator_LIST = []
            CHCHYR_accumulator_LIST = []
            CHCHMOYR_accumulator_LIST = []
            CHCHNOY2_accumulator_LIST = []
            CHCNOYR2_accumulator_LIST = []
            CSRGYR_accumulator_LIST = []
            RSRGNOYR_accumulator_LIST = []
            CMDLONGR_accumulator_LIST = []
            RSCL2_C2_accumulator_LIST = []
            RSCL2_E2_accumulator_LIST = []
            RSCL3_E3_accumulator_LIST = []
            RSCL5_P5_accumulator_LIST = []
            RSCL5_H5_accumulator_LIST = []
            RSCL6_accumulator_LIST = []
            CSHFLU12_accumulator_LIST = []
            CSHFLUNM_accumulator_LIST = []
            CSHFLUM1_accumulator_LIST = []
            CSHFLUY1_accumulator_LIST = []
            CSHSPFL1_accumulator_LIST = []
            CSHFLUM2_accumulator_LIST = []
            CSHFLUY2_accumulator_LIST = []
            CSHSPFL2_accumulator_LIST = []

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
                elif 18 < cdx < 26:
                    WTIA_SC_accumulator_LIST.append(char)
                    WTIA_SC = ''.join(WTIA_SC_accumulator_LIST)
                elif 25 < cdx < 32:
                    WTFA_SC_accumulator_LIST.append(char)
                    WTFA_SC = ''.join(WTFA_SC_accumulator_LIST)
                elif 36 < cdx < 38:
                    REGION_accumulator_LIST.append(char)
                    REGION = ''.join(REGION_accumulator_LIST)
                elif 31 < cdx < 35:
                    STRAT_P_accumulator_LIST.append(char)
                    STRAT_P = ''.join(STRAT_P_accumulator_LIST)
                elif 34 < cdx < 37:
                    PSU_P_accumulator_LIST.append(char)
                    PSU_P = ''.join(PSU_P_accumulator_LIST)
                elif 37 < cdx < 39:
                    SEX_accumulator_LIST.append(char)
                    SEX = ''.join(SEX_accumulator_LIST)
                elif 38 < cdx < 41:
                    HISPAN_I_accumulator_LIST.append(char)
                    HISPAN_I = ''.join(HISPAN_I_accumulator_LIST)
                elif 40 < cdx < 43:
                    RACERPI2_accumulator_LIST.append(char)
                    RACERPI2 = ''.join(RACERPI2_accumulator_LIST)
                elif 42 < cdx < 45:
                    MRACRPI2_accumulator_LIST.append(char)
                    MRACRPI2 = ''.join(MRACRPI2_accumulator_LIST)
                elif 44 < cdx < 47:
                    MRACBPI2_accumulator_LIST.append(char)
                    MRACBPI2 = ''.join(MRACBPI2_accumulator_LIST)
                elif 46 < cdx < 49:
                    AGE_P_accumulator_LIST.append(char)
                    AGE_P = ''.join(AGE_P_accumulator_LIST)
                elif 48 < cdx < 51:
                    CSRESPNO_accumulator_LIST.append(char)
                    CSRESPNO = ''.join(CSRESPNO_accumulator_LIST)
                elif 50 < cdx < 52:
                    CSRELTVP_accumulator_LIST.append(char)
                    CSRELTVP = ''.join(CSRELTVP_accumulator_LIST)
                elif 51 < cdx < 53:
                    LATEINTC_accumulator_LIST.append(char)
                    LATEINTC = ''.join(LATEINTC_accumulator_LIST)
                elif 52 < cdx < 54:
                    FDRN_FLG_accumulator_LIST.append(char)
                    FDRN_FLG = ''.join(FDRN_FLG_accumulator_LIST)
                elif 53 < cdx < 57:
                    TOTOZ_P_accumulator_LIST.append(char)
                    TOTOZ_P = ''.join(TOTOZ_P_accumulator_LIST)
                elif 56 < cdx < 61:
                    BWTGRM_P_accumulator_LIST.append(char)
                    BWTGRM_P = ''.join(BWTGRM_P_accumulator_LIST)
                elif 60 < cdx < 63:
                    CHGHT_TC_accumulator_LIST.append(char)
                    CHGHT_TC = ''.join(CHGHT_TC_accumulator_LIST)
                elif 62 < cdx < 66:
                    CWGHT_TC_accumulator_LIST.append(char)
                    CWGHT_TC = ''.join(CWGHT_TC_accumulator_LIST)
                elif 65 < cdx < 70:
                    BMI_SC_accumulator_LIST.append(char)
                    BMI_SC = ''.join(BMI_SC_accumulator_LIST)
                elif 69 < cdx < 71:
                    AMR1R_accumulator_LIST.append(char)
                    AMR1R = ''.join(AMR1R_accumulator_LIST)
                elif 70 < cdx < 72:
                    AODD1_accumulator_LIST.append(char)
                    AODD1 = ''.join(AODD1_accumulator_LIST)
                elif 71 < cdx < 73:
                    ADD2_accumulator_LIST.append(char)
                    ADD2 = ''.join(ADD2_accumulator_LIST)
                elif 72 < cdx < 74:
                    AMR2R_accumulator_LIST.append(char)
                    AMR2R = ''.join(AMR2R_accumulator_LIST)
                elif 73 < cdx < 75:
                    AUTISM_accumulator_LIST.append(char)
                    AUTISM = ''.join(AUTISM_accumulator_LIST)
                elif 74 < cdx < 76:
                    AODD2_accumulator_LIST.append(char)
                    AODD2 = ''.join(AODD2_accumulator_LIST)
                elif 75 < cdx < 77:
                    CCONDRR1_accumulator_LIST.append(char)
                    CCONDRR1 = ''.join(CCONDRR1_accumulator_LIST)
                elif 76 < cdx < 78:
                    CCONDRR2_accumulator_LIST.append(char)
                    CCONDRR2 = ''.join(CCONDRR2_accumulator_LIST)
                elif 77 < cdx < 79:
                    CCONDRR3_accumulator_LIST.append(char)
                    CCONDRR3 = ''.join(CCONDRR3_accumulator_LIST)
                elif 78 < cdx < 80:
                    CCONDRR4_accumulator_LIST.append(char)
                    CCONDRR4 = ''.join(CCONDRR4_accumulator_LIST)
                elif 79 < cdx < 81:
                    CCONDRR5_accumulator_LIST.append(char)
                    CCONDRR5 = ''.join(CCONDRR5_accumulator_LIST)
                elif 80 < cdx < 82:
                    CCONDRR6_accumulator_LIST.append(char)
                    CCONDRR6 = ''.join(CCONDRR6_accumulator_LIST)
                elif 81 < cdx < 83:
                    CCONDRR7_accumulator_LIST.append(char)
                    CCONDRR7 = ''.join(CCONDRR7_accumulator_LIST)
                elif 82 < cdx < 84:
                    CCONDRR8_accumulator_LIST.append(char)
                    CCONDRR8 = ''.join(CCONDRR8_accumulator_LIST)
                elif 83 < cdx < 85:
                    CCONDRR9_accumulator_LIST.append(char)
                    CCONDRR9 = ''.join(CCONDRR9_accumulator_LIST)
                elif 84 < cdx < 86:
                    CPOX_accumulator_LIST.append(char)
                    CPOX = ''.join(CPOX_accumulator_LIST)
                elif 85 < cdx < 87:
                    CPOX12MO_accumulator_LIST.append(char)
                    CPOX12MO = ''.join(CPOX12MO_accumulator_LIST)
                elif 86 < cdx < 88:
                    CASHMEV_accumulator_LIST.append(char)
                    CASHMEV = ''.join(CASHMEV_accumulator_LIST)
                elif 87 < cdx < 89:
                    CASSTILL_accumulator_LIST.append(char)
                    CASSTILL = ''.join(CASSTILL_accumulator_LIST)
                elif 88 < cdx < 90:
                    CASHYR_accumulator_LIST.append(char)
                    CASHYR = ''.join(CASHYR_accumulator_LIST)
                elif 89 < cdx < 91:
                    CASERYR1_accumulator_LIST.append(char)
                    CASERYR1 = ''.join(CASERYR1_accumulator_LIST)
                elif 90 < cdx < 92:
                    HAYF1_accumulator_LIST.append(char)
                    HAYF1 = ''.join(HAYF1_accumulator_LIST)
                elif 91 < cdx < 93:
                    RALLG1_accumulator_LIST.append(char)
                    RALLG1 = ''.join(RALLG1_accumulator_LIST)
                elif 92 < cdx < 94:
                    DALLG1_accumulator_LIST.append(char)
                    DALLG1 = ''.join(DALLG1_accumulator_LIST)
                elif 93 < cdx < 95:
                    SALLG1_accumulator_LIST.append(char)
                    SALLG1 = ''.join(SALLG1_accumulator_LIST)
                elif 94 < cdx < 96:
                    DIARH1_accumulator_LIST.append(char)
                    DIARH1 = ''.join(DIARH1_accumulator_LIST)
                elif 95 < cdx < 97:
                    ANEMIA1_accumulator_LIST.append(char)
                    ANEMIA1 = ''.join(ANEMIA1_accumulator_LIST)
                elif 96 < cdx < 98:
                    EARINF1_accumulator_LIST.append(char)
                    EARINF1 = ''.join(EARINF1_accumulator_LIST)
                elif 97 < cdx < 99:
                    SEIZE1_accumulator_LIST.append(char)
                    SEIZE1 = ''.join(SEIZE1_accumulator_LIST)
                elif 98 < cdx < 100:
                    HAYF2_accumulator_LIST.append(char)
                    HAYF2 = ''.join(HAYF2_accumulator_LIST)
                elif 99 < cdx < 101:
                    RALLG2_accumulator_LIST.append(char)
                    RALLG2 = ''.join(RALLG2_accumulator_LIST)
                elif 100 < cdx < 102:
                    DALLG2_accumulator_LIST.append(char)
                    DALLG2 = ''.join(DALLG2_accumulator_LIST)
                elif 101 < cdx < 103:
                    SALLG2_accumulator_LIST.append(char)
                    SALLG2 = ''.join(SALLG2_accumulator_LIST)
                elif 102 < cdx < 104:
                    DIARH2_accumulator_LIST.append(char)
                    DIARH2 = ''.join(DIARH2_accumulator_LIST)
                elif 103 < cdx < 105:
                    ANEMIA2_accumulator_LIST.append(char)
                    ANEMIA2 = ''.join(ANEMIA2_accumulator_LIST)
                elif 104 < cdx < 106:
                    FHEAD_accumulator_LIST.append(char)
                    FHEAD = ''.join(FHEAD_accumulator_LIST)
                elif 105 < cdx < 107:
                    EARINF2_accumulator_LIST.append(char)
                    EARINF2 = ''.join(EARINF2_accumulator_LIST)
                elif 106 < cdx < 108:
                    SEIZE2_accumulator_LIST.append(char)
                    SEIZE2 = ''.join(SEIZE2_accumulator_LIST)
                elif 107 < cdx < 109:
                    STUTTER_accumulator_LIST.append(char)
                    STUTTER = ''.join(STUTTER_accumulator_LIST)
                elif 108 < cdx < 110:
                    CHSTATYR_accumulator_LIST.append(char)
                    CHSTATYR = ''.join(CHSTATYR_accumulator_LIST)
                elif 109 < cdx < 113:
                    SCHDAYR1_accumulator_LIST.append(char)
                    SCHDAYR1 = ''.join(SCHDAYR1_accumulator_LIST)
                elif 112 < cdx < 114:
                    CCOLD2W_accumulator_LIST.append(char)
                    CCOLD2W = ''.join(CCOLD2W_accumulator_LIST)
                elif 113 < cdx < 115:
                    CINTIL2W_accumulator_LIST.append(char)
                    CINTIL2W = ''.join(CINTIL2W_accumulator_LIST)
                elif 114 < cdx < 116:
                    CHEARST2_accumulator_LIST.append(char)
                    CHEARST2 = ''.join(CHEARST2_accumulator_LIST)
                elif 115 < cdx < 117:
                    CHRWORS_accumulator_LIST.append(char)
                    CHRWORS = ''.join(CHRWORS_accumulator_LIST)
                elif 116 < cdx < 118:
                    CHRWORSE_accumulator_LIST.append(char)
                    CHRWORSE = ''.join(CHRWORSE_accumulator_LIST)
                elif 117 < cdx < 119:
                    CHRWHIS1_accumulator_LIST.append(char)
                    CHRWHIS1 = ''.join(CHRWHIS1_accumulator_LIST)
                elif 118 < cdx < 120:
                    CHRTALK1_accumulator_LIST.append(char)
                    CHRTALK1 = ''.join(CHRTALK1_accumulator_LIST)
                elif 119 < cdx < 121:
                    CHRSHOU1_accumulator_LIST.append(char)
                    CHRSHOU1 = ''.join(CHRSHOU1_accumulator_LIST)
                elif 120 < cdx < 122:
                    CHRSPEA1_accumulator_LIST.append(char)
                    CHRSPEA1 = ''.join(CHRSPEA1_accumulator_LIST)
                elif 121 < cdx < 123:
                    CHRCOCR1_accumulator_LIST.append(char)
                    CHRCOCR1 = ''.join(CHRCOCR1_accumulator_LIST)
                elif 122 < cdx < 124:
                    CHRCOCI1_accumulator_LIST.append(char)
                    CHRCOCI1 = ''.join(CHRCOCI1_accumulator_LIST)
                elif 123 < cdx < 125:
                    CHRFAM_accumulator_LIST.append(char)
                    CHRFAM = ''.join(CHRFAM_accumulator_LIST)
                elif 124 < cdx < 126:
                    CHRMIS_accumulator_LIST.append(char)
                    CHRMIS = ''.join(CHRMIS_accumulator_LIST)
                elif 125 < cdx < 127:
                    CHRUNDST_accumulator_LIST.append(char)
                    CHRUNDST = ''.join(CHRUNDST_accumulator_LIST)
                elif 126 < cdx < 128:
                    CHRUNDNS_accumulator_LIST.append(char)
                    CHRUNDNS = ''.join(CHRUNDNS_accumulator_LIST)
                elif 127 < cdx < 130:
                    CHEARAG1_accumulator_LIST.append(char)
                    CHEARAG1 = ''.join(CHEARAG1_accumulator_LIST)
                elif 129 < cdx < 132:
                    CHRCAUS1_accumulator_LIST.append(char)
                    CHRCAUS1 = ''.join(CHRCAUS1_accumulator_LIST)
                elif 131 < cdx < 133:
                    CHRPRBHP_accumulator_LIST.append(char)
                    CHRPRBHP = ''.join(CHRPRBHP_accumulator_LIST)
                elif 132 < cdx < 134:
                    CHRENT_accumulator_LIST.append(char)
                    CHRENT = ''.join(CHRENT_accumulator_LIST)
                elif 133 < cdx < 135:
                    CHREHDI_accumulator_LIST.append(char)
                    CHREHDI = ''.join(CHREHDI_accumulator_LIST)
                elif 134 < cdx < 137:
                    CHREIAGE_accumulator_LIST.append(char)
                    CHREIAGE = ''.join(CHREIAGE_accumulator_LIST)
                elif 136 < cdx < 138:
                    CHRTUBE_accumulator_LIST.append(char)
                    CHRTUBE = ''.join(CHRTUBE_accumulator_LIST)
                elif 137 < cdx < 140:
                    CHRTBAGE_accumulator_LIST.append(char)
                    CHRTBAGE = ''.join(CHRTBAGE_accumulator_LIST)
                elif 139 < cdx < 141:
                    CHRTSCH_accumulator_LIST.append(char)
                    CHRTSCH = ''.join(CHRTSCH_accumulator_LIST)
                elif 140 < cdx < 142:
                    CHRTSCHM_accumulator_LIST.append(char)
                    CHRTSCHM = ''.join(CHRTSCHM_accumulator_LIST)
                elif 141 < cdx < 143:
                    CHRTSCHR_accumulator_LIST.append(char)
                    CHRTSCHR = ''.join(CHRTSCHR_accumulator_LIST)
                elif 142 < cdx < 144:
                    CHRTEST_accumulator_LIST.append(char)
                    CHRTEST = ''.join(CHRTEST_accumulator_LIST)
                elif 143 < cdx < 145:
                    CHRAIDNW_accumulator_LIST.append(char)
                    CHRAIDNW = ''.join(CHRAIDNW_accumulator_LIST)
                elif 144 < cdx < 147:
                    CHRAIDLG_accumulator_LIST.append(char)
                    CHRAIDLG = ''.join(CHRAIDLG_accumulator_LIST)
                elif 146 < cdx < 148:
                    CHRAIDYR_accumulator_LIST.append(char)
                    CHRAIDYR = ''.join(CHRAIDYR_accumulator_LIST)
                elif 147 < cdx < 149:
                    CHRAIDEV_accumulator_LIST.append(char)
                    CHRAIDEV = ''.join(CHRAIDEV_accumulator_LIST)
                elif 148 < cdx < 150:
                    CHRAIDRC_accumulator_LIST.append(char)
                    CHRAIDRC = ''.join(CHRAIDRC_accumulator_LIST)
                elif 149 < cdx < 152:
                    CHRAIDLP_accumulator_LIST.append(char)
                    CHRAIDLP = ''.join(CHRAIDLP_accumulator_LIST)
                elif 151 < cdx < 153:
                    CHRAIDOF_accumulator_LIST.append(char)
                    CHRAIDOF = ''.join(CHRAIDOF_accumulator_LIST)
                elif 152 < cdx < 154:
                    CHRAID01_accumulator_LIST.append(char)
                    CHRAID01 = ''.join(CHRAID01_accumulator_LIST)
                elif 153 < cdx < 155:
                    CHRAID02_accumulator_LIST.append(char)
                    CHRAID02 = ''.join(CHRAID02_accumulator_LIST)
                elif 154 < cdx < 156:
                    CHRAID03_accumulator_LIST.append(char)
                    CHRAID03 = ''.join(CHRAID03_accumulator_LIST)
                elif 155 < cdx < 157:
                    CHRAID04_accumulator_LIST.append(char)
                    CHRAID04 = ''.join(CHRAID04_accumulator_LIST)
                elif 156 < cdx < 158:
                    CHRAID05_accumulator_LIST.append(char)
                    CHRAID05 = ''.join(CHRAID05_accumulator_LIST)
                elif 157 < cdx < 159:
                    CHRAID06_accumulator_LIST.append(char)
                    CHRAID06 = ''.join(CHRAID06_accumulator_LIST)
                elif 158 < cdx < 160:
                    CHRAID07_accumulator_LIST.append(char)
                    CHRAID07 = ''.join(CHRAID07_accumulator_LIST)
                elif 159 < cdx < 161:
                    CHRAID08_accumulator_LIST.append(char)
                    CHRAID08 = ''.join(CHRAID08_accumulator_LIST)
                elif 160 < cdx < 162:
                    CHRAID09_accumulator_LIST.append(char)
                    CHRAID09 = ''.join(CHRAID09_accumulator_LIST)
                elif 161 < cdx < 163:
                    CHRAID10_accumulator_LIST.append(char)
                    CHRAID10 = ''.join(CHRAID10_accumulator_LIST)
                elif 162 < cdx < 164:
                    CHRAID11_accumulator_LIST.append(char)
                    CHRAID11 = ''.join(CHRAID11_accumulator_LIST)
                elif 163 < cdx < 165:
                    CHRAUD_accumulator_LIST.append(char)
                    CHRAUD = ''.join(CHRAUD_accumulator_LIST)
                elif 164 < cdx < 166:
                    CHRALDS_accumulator_LIST.append(char)
                    CHRALDS = ''.join(CHRALDS_accumulator_LIST)
                elif 165 < cdx < 167:
                    CHRALD01_accumulator_LIST.append(char)
                    CHRALD01 = ''.join(CHRALD01_accumulator_LIST)
                elif 166 < cdx < 168:
                    CHRALD02_accumulator_LIST.append(char)
                    CHRALD02 = ''.join(CHRALD02_accumulator_LIST)
                elif 167 < cdx < 169:
                    CHRALD03_accumulator_LIST.append(char)
                    CHRALD03 = ''.join(CHRALD03_accumulator_LIST)
                elif 168 < cdx < 170:
                    CHRALD04_accumulator_LIST.append(char)
                    CHRALD04 = ''.join(CHRALD04_accumulator_LIST)
                elif 169 < cdx < 171:
                    CHRALD05_accumulator_LIST.append(char)
                    CHRALD05 = ''.join(CHRALD05_accumulator_LIST)
                elif 170 < cdx < 172:
                    CHRALD06_accumulator_LIST.append(char)
                    CHRALD06 = ''.join(CHRALD06_accumulator_LIST)
                elif 171 < cdx < 173:
                    CHRALD07_accumulator_LIST.append(char)
                    CHRALD07 = ''.join(CHRALD07_accumulator_LIST)
                elif 172 < cdx < 174:
                    CHRALD08_accumulator_LIST.append(char)
                    CHRALD08 = ''.join(CHRALD08_accumulator_LIST)
                elif 173 < cdx < 175:
                    CHRALD09_accumulator_LIST.append(char)
                    CHRALD09 = ''.join(CHRALD09_accumulator_LIST)
                elif 174 < cdx < 176:
                    CHRALD10_accumulator_LIST.append(char)
                    CHRALD10 = ''.join(CHRALD10_accumulator_LIST)
                elif 175 < cdx < 177:
                    CHRALD11_accumulator_LIST.append(char)
                    CHRALD11 = ''.join(CHRALD11_accumulator_LIST)
                elif 176 < cdx < 178:
                    CHRALD12_accumulator_LIST.append(char)
                    CHRALD12 = ''.join(CHRALD12_accumulator_LIST)
                elif 177 < cdx < 179:
                    CHRFIRE_accumulator_LIST.append(char)
                    CHRFIRE = ''.join(CHRFIRE_accumulator_LIST)
                elif 178 < cdx < 180:
                    CHRFRCRK_accumulator_LIST.append(char)
                    CHRFRCRK = ''.join(CHRFRCRK_accumulator_LIST)
                elif 179 < cdx < 181:
                    CHRTOTR_accumulator_LIST.append(char)
                    CHRTOTR = ''.join(CHRTOTR_accumulator_LIST)
                elif 180 < cdx < 182:
                    CHRFRPRT_accumulator_LIST.append(char)
                    CHRFRPRT = ''.join(CHRFRPRT_accumulator_LIST)
                elif 181 < cdx < 183:
                    CHRWKVLN_accumulator_LIST.append(char)
                    CHRWKVLN = ''.join(CHRWKVLN_accumulator_LIST)
                elif 182 < cdx < 185:
                    CHRWKVLT_accumulator_LIST.append(char)
                    CHRWKVLT = ''.join(CHRWKVLT_accumulator_LIST)
                elif 184 < cdx < 186:
                    CHRWKPRT_accumulator_LIST.append(char)
                    CHRWKPRT = ''.join(CHRWKPRT_accumulator_LIST)
                elif 185 < cdx < 187:
                    CHRLESNS_accumulator_LIST.append(char)
                    CHRLESNS = ''.join(CHRLESNS_accumulator_LIST)
                elif 186 < cdx < 188:
                    CHRLST01_accumulator_LIST.append(char)
                    CHRLST01 = ''.join(CHRLST01_accumulator_LIST)
                elif 187 < cdx < 189:
                    CHRLST02_accumulator_LIST.append(char)
                    CHRLST02 = ''.join(CHRLST02_accumulator_LIST)
                elif 188 < cdx < 190:
                    CHRLST03_accumulator_LIST.append(char)
                    CHRLST03 = ''.join(CHRLST03_accumulator_LIST)
                elif 189 < cdx < 191:
                    CHRLST04_accumulator_LIST.append(char)
                    CHRLST04 = ''.join(CHRLST04_accumulator_LIST)
                elif 190 < cdx < 192:
                    CHRLST05_accumulator_LIST.append(char)
                    CHRLST05 = ''.join(CHRLST05_accumulator_LIST)
                elif 191 < cdx < 193:
                    CHRLST06_accumulator_LIST.append(char)
                    CHRLST06 = ''.join(CHRLST06_accumulator_LIST)
                elif 192 < cdx < 194:
                    CHRLST07_accumulator_LIST.append(char)
                    CHRLST07 = ''.join(CHRLST07_accumulator_LIST)
                elif 193 < cdx < 195:
                    CHRLST08_accumulator_LIST.append(char)
                    CHRLST08 = ''.join(CHRLST08_accumulator_LIST)
                elif 194 < cdx < 196:
                    CHRLST09_accumulator_LIST.append(char)
                    CHRLST09 = ''.join(CHRLST09_accumulator_LIST)
                elif 195 < cdx < 197:
                    CHRLST10_accumulator_LIST.append(char)
                    CHRLST10 = ''.join(CHRLST10_accumulator_LIST)
                elif 196 < cdx < 198:
                    CHRLST11_accumulator_LIST.append(char)
                    CHRLST11 = ''.join(CHRLST11_accumulator_LIST)
                elif 197 < cdx < 199:
                    CHRLST12_accumulator_LIST.append(char)
                    CHRLST12 = ''.join(CHRLST12_accumulator_LIST)
                elif 198 < cdx < 200:
                    CHRLSPRT_accumulator_LIST.append(char)
                    CHRLSPRT = ''.join(CHRLSPRT_accumulator_LIST)
                elif 199 < cdx < 201:
                    CHRINT_accumulator_LIST.append(char)
                    CHRINT = ''.join(CHRINT_accumulator_LIST)
                elif 200 < cdx < 202:
                    CHRINTHL_accumulator_LIST.append(char)
                    CHRINTHL = ''.join(CHRINTHL_accumulator_LIST)
                elif 201 < cdx < 203:
                    CHRINTHA_accumulator_LIST.append(char)
                    CHRINTHA = ''.join(CHRINTHA_accumulator_LIST)
                elif 202 < cdx < 204:
                    CHRINTHP_accumulator_LIST.append(char)
                    CHRINTHP = ''.join(CHRINTHP_accumulator_LIST)
                elif 203 < cdx < 205:
                    CHRINHPR_accumulator_LIST.append(char)
                    CHRINHPR = ''.join(CHRINHPR_accumulator_LIST)
                elif 204 < cdx < 206:
                    CVISION_accumulator_LIST.append(char)
                    CVISION = ''.join(CVISION_accumulator_LIST)
                elif 205 < cdx < 207:
                    CBLIND_accumulator_LIST.append(char)
                    CBLIND = ''.join(CBLIND_accumulator_LIST)
                elif 206 < cdx < 208:
                    IHSPEQ_accumulator_LIST.append(char)
                    IHSPEQ = ''.join(IHSPEQ_accumulator_LIST)
                elif 207 < cdx < 209:
                    IHMOB_accumulator_LIST.append(char)
                    IHMOB = ''.join(IHMOB_accumulator_LIST)
                elif 208 < cdx < 210:
                    IHMOBYR_accumulator_LIST.append(char)
                    IHMOBYR = ''.join(IHMOBYR_accumulator_LIST)
                elif 209 < cdx < 211:
                    PROBRX_accumulator_LIST.append(char)
                    PROBRX = ''.join(PROBRX_accumulator_LIST)
                elif 210 < cdx < 212:
                    LEARND_accumulator_LIST.append(char)
                    LEARND = ''.join(LEARND_accumulator_LIST)
                elif 211 < cdx < 214:
                    MHIBOY2_accumulator_LIST.append(char)
                    MHIBOY2 = ''.join(MHIBOY2_accumulator_LIST)
                elif 213 < cdx < 215:
                    CMHAGM15_accumulator_LIST.append(char)
                    CMHAGM15 = ''.join(CMHAGM15_accumulator_LIST)
                elif 214 < cdx < 217:
                    MHIGRL2_accumulator_LIST.append(char)
                    MHIGRL2 = ''.join(MHIGRL2_accumulator_LIST)
                elif 216 < cdx < 218:
                    CMHAGF15_accumulator_LIST.append(char)
                    CMHAGF15 = ''.join(CMHAGF15_accumulator_LIST)
                elif 217 < cdx < 219:
                    CUSUALPL_accumulator_LIST.append(char)
                    CUSUALPL = ''.join(CUSUALPL_accumulator_LIST)
                elif 218 < cdx < 220:
                    CPLKIND_accumulator_LIST.append(char)
                    CPLKIND = ''.join(CPLKIND_accumulator_LIST)
                elif 219 < cdx < 221:
                    CHCPLROU_accumulator_LIST.append(char)
                    CHCPLROU = ''.join(CHCPLROU_accumulator_LIST)
                elif 220 < cdx < 222:
                    CHCPLKND_accumulator_LIST.append(char)
                    CHCPLKND = ''.join(CHCPLKND_accumulator_LIST)
                elif 221 < cdx < 223:
                    CHCCHGYR_accumulator_LIST.append(char)
                    CHCCHGYR = ''.join(CHCCHGYR_accumulator_LIST)
                elif 222 < cdx < 224:
                    CHCCHGHI_accumulator_LIST.append(char)
                    CHCCHGHI = ''.join(CHCCHGHI_accumulator_LIST)
                elif 223 < cdx < 225:
                    CNOUSPL1_accumulator_LIST.append(char)
                    CNOUSPL1 = ''.join(CNOUSPL1_accumulator_LIST)
                elif 224 < cdx < 226:
                    CNOUSPL2_accumulator_LIST.append(char)
                    CNOUSPL2 = ''.join(CNOUSPL2_accumulator_LIST)
                elif 225 < cdx < 227:
                    CNOUSPL3_accumulator_LIST.append(char)
                    CNOUSPL3 = ''.join(CNOUSPL3_accumulator_LIST)
                elif 226 < cdx < 228:
                    CNOUSPL4_accumulator_LIST.append(char)
                    CNOUSPL4 = ''.join(CNOUSPL4_accumulator_LIST)
                elif 227 < cdx < 229:
                    CNOUSPL5_accumulator_LIST.append(char)
                    CNOUSPL5 = ''.join(CNOUSPL5_accumulator_LIST)
                elif 228 < cdx < 230:
                    CNOUSPL6_accumulator_LIST.append(char)
                    CNOUSPL6 = ''.join(CNOUSPL6_accumulator_LIST)
                elif 229 < cdx < 231:
                    CNOUSPL7_accumulator_LIST.append(char)
                    CNOUSPL7 = ''.join(CNOUSPL7_accumulator_LIST)
                elif 230 < cdx < 232:
                    CNOUSPL8_accumulator_LIST.append(char)
                    CNOUSPL8 = ''.join(CNOUSPL8_accumulator_LIST)
                elif 231 < cdx < 233:
                    CNOUSPL9_accumulator_LIST.append(char)
                    CNOUSPL9 = ''.join(CNOUSPL9_accumulator_LIST)
                elif 232 < cdx < 234:
                    CPRVTRYR_accumulator_LIST.append(char)
                    CPRVTRYR = ''.join(CPRVTRYR_accumulator_LIST)
                elif 233 < cdx < 235:
                    CPRVTRFD_accumulator_LIST.append(char)
                    CPRVTRFD = ''.join(CPRVTRFD_accumulator_LIST)
                elif 234 < cdx < 236:
                    CDRNANP_accumulator_LIST.append(char)
                    CDRNANP = ''.join(CDRNANP_accumulator_LIST)
                elif 235 < cdx < 237:
                    CDRNAI_accumulator_LIST.append(char)
                    CDRNAI = ''.join(CDRNAI_accumulator_LIST)
                elif 236 < cdx < 238:
                    CHCDLYR1_accumulator_LIST.append(char)
                    CHCDLYR1 = ''.join(CHCDLYR1_accumulator_LIST)
                elif 237 < cdx < 239:
                    CHCDLYR2_accumulator_LIST.append(char)
                    CHCDLYR2 = ''.join(CHCDLYR2_accumulator_LIST)
                elif 238 < cdx < 240:
                    CHCDLYR3_accumulator_LIST.append(char)
                    CHCDLYR3 = ''.join(CHCDLYR3_accumulator_LIST)
                elif 239 < cdx < 241:
                    CHCDLYR4_accumulator_LIST.append(char)
                    CHCDLYR4 = ''.join(CHCDLYR4_accumulator_LIST)
                elif 240 < cdx < 242:
                    CHCDLYR5_accumulator_LIST.append(char)
                    CHCDLYR5 = ''.join(CHCDLYR5_accumulator_LIST)
                elif 241 < cdx < 243:
                    CHCAFYR_accumulator_LIST.append(char)
                    CHCAFYR = ''.join(CHCAFYR_accumulator_LIST)
                elif 242 < cdx < 244:
                    CHCAFYRN_accumulator_LIST.append(char)
                    CHCAFYRN = ''.join(CHCAFYRN_accumulator_LIST)
                elif 243 < cdx < 245:
                    CHCAFYRF_accumulator_LIST.append(char)
                    CHCAFYRF = ''.join(CHCAFYRF_accumulator_LIST)
                elif 244 < cdx < 246:
                    CHCAFYR1_accumulator_LIST.append(char)
                    CHCAFYR1 = ''.join(CHCAFYR1_accumulator_LIST)
                elif 245 < cdx < 247:
                    CHCAFYR2_accumulator_LIST.append(char)
                    CHCAFYR2 = ''.join(CHCAFYR2_accumulator_LIST)
                elif 246 < cdx < 248:
                    CHCAFYR3_accumulator_LIST.append(char)
                    CHCAFYR3 = ''.join(CHCAFYR3_accumulator_LIST)
                elif 247 < cdx < 249:
                    CHCAFYR4_accumulator_LIST.append(char)
                    CHCAFYR4 = ''.join(CHCAFYR4_accumulator_LIST)
                elif 248 < cdx < 250:
                    CHCAFYR5_accumulator_LIST.append(char)
                    CHCAFYR5 = ''.join(CHCAFYR5_accumulator_LIST)
                elif 249 < cdx < 251:
                    CHCAFYR6_accumulator_LIST.append(char)
                    CHCAFYR6 = ''.join(CHCAFYR6_accumulator_LIST)
                elif 250 < cdx < 252:
                    CDNLONGR_accumulator_LIST.append(char)
                    CDNLONGR = ''.join(CDNLONGR_accumulator_LIST)
                elif 251 < cdx < 253:
                    CHCSYR11_accumulator_LIST.append(char)
                    CHCSYR11 = ''.join(CHCSYR11_accumulator_LIST)
                elif 252 < cdx < 254:
                    CHCSYR12_accumulator_LIST.append(char)
                    CHCSYR12 = ''.join(CHCSYR12_accumulator_LIST)
                elif 253 < cdx < 255:
                    CHCSYR13_accumulator_LIST.append(char)
                    CHCSYR13 = ''.join(CHCSYR13_accumulator_LIST)
                elif 254 < cdx < 256:
                    CHCSYR14_accumulator_LIST.append(char)
                    CHCSYR14 = ''.join(CHCSYR14_accumulator_LIST)
                elif 255 < cdx < 257:
                    CHCSYR1_accumulator_LIST.append(char)
                    CHCSYR1 = ''.join(CHCSYR1_accumulator_LIST)
                elif 256 < cdx < 258:
                    CHCSYR2_accumulator_LIST.append(char)
                    CHCSYR2 = ''.join(CHCSYR2_accumulator_LIST)
                elif 257 < cdx < 259:
                    CHCSYR3_accumulator_LIST.append(char)
                    CHCSYR3 = ''.join(CHCSYR3_accumulator_LIST)
                elif 258 < cdx < 260:
                    CHCSYR4_accumulator_LIST.append(char)
                    CHCSYR4 = ''.join(CHCSYR4_accumulator_LIST)
                elif 259 < cdx < 261:
                    CHCSYR5_accumulator_LIST.append(char)
                    CHCSYR5 = ''.join(CHCSYR5_accumulator_LIST)
                elif 260 < cdx < 262:
                    CHCSYR6_accumulator_LIST.append(char)
                    CHCSYR6 = ''.join(CHCSYR6_accumulator_LIST)
                elif 261 < cdx < 263:
                    CHCSYR7_accumulator_LIST.append(char)
                    CHCSYR7 = ''.join(CHCSYR7_accumulator_LIST)
                elif 262 < cdx < 264:
                    CHCSYR81_accumulator_LIST.append(char)
                    CHCSYR81 = ''.join(CHCSYR81_accumulator_LIST)
                elif 263 < cdx < 265:
                    CHCSYR82_accumulator_LIST.append(char)
                    CHCSYR82 = ''.join(CHCSYR82_accumulator_LIST)
                elif 264 < cdx < 266:
                    CHCSYR10_accumulator_LIST.append(char)
                    CHCSYR10 = ''.join(CHCSYR10_accumulator_LIST)
                elif 265 < cdx < 267:
                    CHCSYREM_accumulator_LIST.append(char)
                    CHCSYREM = ''.join(CHCSYREM_accumulator_LIST)
                elif 266 < cdx < 268:
                    CHPXYR_C_accumulator_LIST.append(char)
                    CHPXYR_C = ''.join(CHPXYR_C_accumulator_LIST)
                elif 267 < cdx < 270:
                    CHERNOY2_accumulator_LIST.append(char)
                    CHERNOY2 = ''.join(CHERNOY2_accumulator_LIST)
                elif 269 < cdx < 271:
                    CERVISND_accumulator_LIST.append(char)
                    CERVISND = ''.join(CERVISND_accumulator_LIST)
                elif 270 < cdx < 272:
                    CERHOS_accumulator_LIST.append(char)
                    CERHOS = ''.join(CERHOS_accumulator_LIST)
                elif 271 < cdx < 273:
                    CERREA1R_accumulator_LIST.append(char)
                    CERREA1R = ''.join(CERREA1R_accumulator_LIST)
                elif 272 < cdx < 274:
                    CERREA2R_accumulator_LIST.append(char)
                    CERREA2R = ''.join(CERREA2R_accumulator_LIST)
                elif 273 < cdx < 275:
                    CERREA3R_accumulator_LIST.append(char)
                    CERREA3R = ''.join(CERREA3R_accumulator_LIST)
                elif 274 < cdx < 276:
                    CERREA4R_accumulator_LIST.append(char)
                    CERREA4R = ''.join(CERREA4R_accumulator_LIST)
                elif 275 < cdx < 277:
                    CERREA5R_accumulator_LIST.append(char)
                    CERREA5R = ''.join(CERREA5R_accumulator_LIST)
                elif 276 < cdx < 278:
                    CERREA6R_accumulator_LIST.append(char)
                    CERREA6R = ''.join(CERREA6R_accumulator_LIST)
                elif 277 < cdx < 279:
                    CERREA7R_accumulator_LIST.append(char)
                    CERREA7R = ''.join(CERREA7R_accumulator_LIST)
                elif 278 < cdx < 280:
                    CERREA8R_accumulator_LIST.append(char)
                    CERREA8R = ''.join(CERREA8R_accumulator_LIST)
                elif 279 < cdx < 281:
                    CHCHYR_accumulator_LIST.append(char)
                    CHCHYR = ''.join(CHCHYR_accumulator_LIST)
                elif 280 < cdx < 283:
                    CHCHMOYR_accumulator_LIST.append(char)
                    CHCHMOYR = ''.join(CHCHMOYR_accumulator_LIST)
                elif 282 < cdx < 285:
                    CHCHNOY2_accumulator_LIST.append(char)
                    CHCHNOY2 = ''.join(CHCHNOY2_accumulator_LIST)
                elif 284 < cdx < 287:
                    CHCNOYR2_accumulator_LIST.append(char)
                    CHCNOYR2 = ''.join(CHCNOYR2_accumulator_LIST)
                elif 286 < cdx < 288:
                    CSRGYR_accumulator_LIST.append(char)
                    CSRGYR = ''.join(CSRGYR_accumulator_LIST)
                elif 287 < cdx < 290:
                    RSRGNOYR_accumulator_LIST.append(char)
                    RSRGNOYR = ''.join(RSRGNOYR_accumulator_LIST)
                elif 289 < cdx < 291:
                    CMDLONGR_accumulator_LIST.append(char)
                    CMDLONGR = ''.join(CMDLONGR_accumulator_LIST)
                elif 290 < cdx < 292:
                    RSCL2_C2_accumulator_LIST.append(char)
                    RSCL2_C2 = ''.join(RSCL2_C2_accumulator_LIST)
                elif 291 < cdx < 293:
                    RSCL2_E2_accumulator_LIST.append(char)
                    RSCL2_E2 = ''.join(RSCL2_E2_accumulator_LIST)
                elif 292 < cdx < 294:
                    RSCL3_E3_accumulator_LIST.append(char)
                    RSCL3_E3 = ''.join(RSCL3_E3_accumulator_LIST)
                elif 293 < cdx < 295:
                    RSCL5_P5_accumulator_LIST.append(char)
                    RSCL5_P5 = ''.join(RSCL5_P5_accumulator_LIST)
                elif 294 < cdx < 296:
                    RSCL5_H5_accumulator_LIST.append(char)
                    RSCL5_H5 = ''.join(RSCL5_H5_accumulator_LIST)
                elif 295 < cdx < 297:
                    RSCL6_accumulator_LIST.append(char)
                    RSCL6 = ''.join(RSCL6_accumulator_LIST)
                elif 296 < cdx < 298:
                    CSHFLU12_accumulator_LIST.append(char)
                    CSHFLU12 = ''.join(CSHFLU12_accumulator_LIST)
                elif 297 < cdx < 299:
                    CSHFLUNM_accumulator_LIST.append(char)
                    CSHFLUNM = ''.join(CSHFLUNM_accumulator_LIST)
                elif 298 < cdx < 301:
                    CSHFLUM1_accumulator_LIST.append(char)
                    CSHFLUM1 = ''.join(CSHFLUM1_accumulator_LIST)
                elif 300 < cdx < 305:
                    CSHFLUY1_accumulator_LIST.append(char)
                    CSHFLUY1 = ''.join(CSHFLUY1_accumulator_LIST)
                elif 304 < cdx < 306:
                    CSHSPFL1_accumulator_LIST.append(char)
                    CSHSPFL1 = ''.join(CSHSPFL1_accumulator_LIST)
                elif 305 < cdx < 308:
                    CSHFLUM2_accumulator_LIST.append(char)
                    CSHFLUM2 = ''.join(CSHFLUM2_accumulator_LIST)
                elif 307 < cdx < 312:
                    CSHFLUY2_accumulator_LIST.append(char)
                    CSHFLUY2 = ''.join(CSHFLUY2_accumulator_LIST)
                elif 311 < cdx < 313:
                    CSHSPFL2_accumulator_LIST.append(char)
                    CSHSPFL2 = ''.join(CSHSPFL2_accumulator_LIST)
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
        WTIA_SC_LIST.append(WTIA_SC)
        WTFA_SC_LIST.append(WTFA_SC)
        REGION_LIST.append(REGION)
        STRAT_P_LIST.append(STRAT_P)
        PSU_P_LIST.append(PSU_P)
        SEX_LIST.append(SEX)
        HISPAN_I_LIST.append(HISPAN_I)
        RACERPI2_LIST.append(RACERPI2)
        MRACRPI2_LIST.append(MRACRPI2)
        MRACBPI2_LIST.append(MRACBPI2)
        AGE_P_LIST.append(AGE_P)
        CSRESPNO_LIST.append(CSRESPNO)
        CSRELTVP_LIST.append(CSRELTVP)
        LATEINTC_LIST.append(LATEINTC)
        FDRN_FLG_LIST.append(FDRN_FLG)
        TOTOZ_P_LIST.append(TOTOZ_P)
        BWTGRM_P_LIST.append(BWTGRM_P)
        CHGHT_TC_LIST.append(CHGHT_TC)
        CWGHT_TC_LIST.append(CWGHT_TC)
        BMI_SC_LIST.append(BMI_SC)
        AMR1R_LIST.append(AMR1R)
        AODD1_LIST.append(AODD1)
        ADD2_LIST.append(ADD2)
        AMR2R_LIST.append(AMR2R)
        AUTISM_LIST.append(AUTISM)
        AODD2_LIST.append(AODD2)
        CCONDRR1_LIST.append(CCONDRR1)
        CCONDRR2_LIST.append(CCONDRR2)
        CCONDRR3_LIST.append(CCONDRR3)
        CCONDRR4_LIST.append(CCONDRR4)
        CCONDRR5_LIST.append(CCONDRR5)
        CCONDRR6_LIST.append(CCONDRR6)
        CCONDRR7_LIST.append(CCONDRR7)
        CCONDRR8_LIST.append(CCONDRR8)
        CCONDRR9_LIST.append(CCONDRR9)
        CPOX_LIST.append(CPOX)
        CPOX12MO_LIST.append(CPOX12MO)
        CASHMEV_LIST.append(CASHMEV)
        CASSTILL_LIST.append(CASSTILL)
        CASHYR_LIST.append(CASHYR)
        CASERYR1_LIST.append(CASERYR1)
        HAYF1_LIST.append(HAYF1)
        RALLG1_LIST.append(RALLG1)
        DALLG1_LIST.append(DALLG1)
        SALLG1_LIST.append(SALLG1)
        DIARH1_LIST.append(DIARH1)
        ANEMIA1_LIST.append(ANEMIA1)
        EARINF1_LIST.append(EARINF1)
        SEIZE1_LIST.append(SEIZE1)
        HAYF2_LIST.append(HAYF2)
        RALLG2_LIST.append(RALLG2)
        DALLG2_LIST.append(DALLG2)
        SALLG2_LIST.append(SALLG2)
        DIARH2_LIST.append(DIARH2)
        ANEMIA2_LIST.append(ANEMIA2)
        FHEAD_LIST.append(FHEAD)
        EARINF2_LIST.append(EARINF2)
        SEIZE2_LIST.append(SEIZE2)
        STUTTER_LIST.append(STUTTER)
        CHSTATYR_LIST.append(CHSTATYR)
        SCHDAYR1_LIST.append(SCHDAYR1)
        CCOLD2W_LIST.append(CCOLD2W)
        CINTIL2W_LIST.append(CINTIL2W)
        CHEARST2_LIST.append(CHEARST2)
        CHRWORS_LIST.append(CHRWORS)
        CHRWORSE_LIST.append(CHRWORSE)
        CHRWHIS1_LIST.append(CHRWHIS1)
        CHRTALK1_LIST.append(CHRTALK1)
        CHRSHOU1_LIST.append(CHRSHOU1)
        CHRSPEA1_LIST.append(CHRSPEA1)
        CHRCOCR1_LIST.append(CHRCOCR1)
        CHRCOCI1_LIST.append(CHRCOCI1)
        CHRFAM_LIST.append(CHRFAM)
        CHRMIS_LIST.append(CHRMIS)
        CHRUNDST_LIST.append(CHRUNDST)
        CHRUNDNS_LIST.append(CHRUNDNS)
        CHEARAG1_LIST.append(CHEARAG1)
        CHRCAUS1_LIST.append(CHRCAUS1)
        CHRPRBHP_LIST.append(CHRPRBHP)
        CHRENT_LIST.append(CHRENT)
        CHREHDI_LIST.append(CHREHDI)
        CHREIAGE_LIST.append(CHREIAGE)
        CHRTUBE_LIST.append(CHRTUBE)
        CHRTBAGE_LIST.append(CHRTBAGE)
        CHRTSCH_LIST.append(CHRTSCH)
        CHRTSCHM_LIST.append(CHRTSCHM)
        CHRTSCHR_LIST.append(CHRTSCHR)
        CHRTEST_LIST.append(CHRTEST)
        CHRAIDNW_LIST.append(CHRAIDNW)
        CHRAIDLG_LIST.append(CHRAIDLG)
        CHRAIDYR_LIST.append(CHRAIDYR)
        CHRAIDEV_LIST.append(CHRAIDEV)
        CHRAIDRC_LIST.append(CHRAIDRC)
        CHRAIDLP_LIST.append(CHRAIDLP)
        CHRAIDOF_LIST.append(CHRAIDOF)
        CHRAID01_LIST.append(CHRAID01)
        CHRAID02_LIST.append(CHRAID02)
        CHRAID03_LIST.append(CHRAID03)
        CHRAID04_LIST.append(CHRAID04)
        CHRAID05_LIST.append(CHRAID05)
        CHRAID06_LIST.append(CHRAID06)
        CHRAID07_LIST.append(CHRAID07)
        CHRAID08_LIST.append(CHRAID08)
        CHRAID09_LIST.append(CHRAID09)
        CHRAID10_LIST.append(CHRAID10)
        CHRAID11_LIST.append(CHRAID11)
        CHRAUD_LIST.append(CHRAUD)
        CHRALDS_LIST.append(CHRALDS)
        CHRALD01_LIST.append(CHRALD01)
        CHRALD02_LIST.append(CHRALD02)
        CHRALD03_LIST.append(CHRALD03)
        CHRALD04_LIST.append(CHRALD04)
        CHRALD05_LIST.append(CHRALD05)
        CHRALD06_LIST.append(CHRALD06)
        CHRALD07_LIST.append(CHRALD07)
        CHRALD08_LIST.append(CHRALD08)
        CHRALD09_LIST.append(CHRALD09)
        CHRALD10_LIST.append(CHRALD10)
        CHRALD11_LIST.append(CHRALD11)
        CHRALD12_LIST.append(CHRALD12)
        CHRFIRE_LIST.append(CHRFIRE)
        CHRFRCRK_LIST.append(CHRFRCRK)
        CHRTOTR_LIST.append(CHRTOTR)
        CHRFRPRT_LIST.append(CHRFRPRT)
        CHRWKVLN_LIST.append(CHRWKVLN)
        CHRWKVLT_LIST.append(CHRWKVLT)
        CHRWKPRT_LIST.append(CHRWKPRT)
        CHRLESNS_LIST.append(CHRLESNS)
        CHRLST01_LIST.append(CHRLST01)
        CHRLST02_LIST.append(CHRLST02)
        CHRLST03_LIST.append(CHRLST03)
        CHRLST04_LIST.append(CHRLST04)
        CHRLST05_LIST.append(CHRLST05)
        CHRLST06_LIST.append(CHRLST06)
        CHRLST07_LIST.append(CHRLST07)
        CHRLST08_LIST.append(CHRLST08)
        CHRLST09_LIST.append(CHRLST09)
        CHRLST10_LIST.append(CHRLST10)
        CHRLST11_LIST.append(CHRLST11)
        CHRLST12_LIST.append(CHRLST12)
        CHRLSPRT_LIST.append(CHRLSPRT)
        CHRINT_LIST.append(CHRINT)
        CHRINTHL_LIST.append(CHRINTHL)
        CHRINTHA_LIST.append(CHRINTHA)
        CHRINTHP_LIST.append(CHRINTHP)
        CHRINHPR_LIST.append(CHRINHPR)
        CVISION_LIST.append(CVISION)
        CBLIND_LIST.append(CBLIND)
        IHSPEQ_LIST.append(IHSPEQ)
        IHMOB_LIST.append(IHMOB)
        IHMOBYR_LIST.append(IHMOBYR)
        PROBRX_LIST.append(PROBRX)
        LEARND_LIST.append(LEARND)
        MHIBOY2_LIST.append(MHIBOY2)
        CMHAGM15_LIST.append(CMHAGM15)
        MHIGRL2_LIST.append(MHIGRL2)
        CMHAGF15_LIST.append(CMHAGF15)
        CUSUALPL_LIST.append(CUSUALPL)
        CPLKIND_LIST.append(CPLKIND)
        CHCPLROU_LIST.append(CHCPLROU)
        CHCPLKND_LIST.append(CHCPLKND)
        CHCCHGYR_LIST.append(CHCCHGYR)
        CHCCHGHI_LIST.append(CHCCHGHI)
        CNOUSPL1_LIST.append(CNOUSPL1)
        CNOUSPL2_LIST.append(CNOUSPL2)
        CNOUSPL3_LIST.append(CNOUSPL3)
        CNOUSPL4_LIST.append(CNOUSPL4)
        CNOUSPL5_LIST.append(CNOUSPL5)
        CNOUSPL6_LIST.append(CNOUSPL6)
        CNOUSPL7_LIST.append(CNOUSPL7)
        CNOUSPL8_LIST.append(CNOUSPL8)
        CNOUSPL9_LIST.append(CNOUSPL9)
        CPRVTRYR_LIST.append(CPRVTRYR)
        CPRVTRFD_LIST.append(CPRVTRFD)
        CDRNANP_LIST.append(CDRNANP)
        CDRNAI_LIST.append(CDRNAI)
        CHCDLYR1_LIST.append(CHCDLYR1)
        CHCDLYR2_LIST.append(CHCDLYR2)
        CHCDLYR3_LIST.append(CHCDLYR3)
        CHCDLYR4_LIST.append(CHCDLYR4)
        CHCDLYR5_LIST.append(CHCDLYR5)
        CHCAFYR_LIST.append(CHCAFYR)
        CHCAFYRN_LIST.append(CHCAFYRN)
        CHCAFYRF_LIST.append(CHCAFYRF)
        CHCAFYR1_LIST.append(CHCAFYR1)
        CHCAFYR2_LIST.append(CHCAFYR2)
        CHCAFYR3_LIST.append(CHCAFYR3)
        CHCAFYR4_LIST.append(CHCAFYR4)
        CHCAFYR5_LIST.append(CHCAFYR5)
        CHCAFYR6_LIST.append(CHCAFYR6)
        CDNLONGR_LIST.append(CDNLONGR)
        CHCSYR11_LIST.append(CHCSYR11)
        CHCSYR12_LIST.append(CHCSYR12)
        CHCSYR13_LIST.append(CHCSYR13)
        CHCSYR14_LIST.append(CHCSYR14)
        CHCSYR1_LIST.append(CHCSYR1)
        CHCSYR2_LIST.append(CHCSYR2)
        CHCSYR3_LIST.append(CHCSYR3)
        CHCSYR4_LIST.append(CHCSYR4)
        CHCSYR5_LIST.append(CHCSYR5)
        CHCSYR6_LIST.append(CHCSYR6)
        CHCSYR7_LIST.append(CHCSYR7)
        CHCSYR81_LIST.append(CHCSYR81)
        CHCSYR82_LIST.append(CHCSYR82)
        CHCSYR10_LIST.append(CHCSYR10)
        CHCSYREM_LIST.append(CHCSYREM)
        CHPXYR_C_LIST.append(CHPXYR_C)
        CHERNOY2_LIST.append(CHERNOY2)
        CERVISND_LIST.append(CERVISND)
        CERHOS_LIST.append(CERHOS)
        CERREA1R_LIST.append(CERREA1R)
        CERREA2R_LIST.append(CERREA2R)
        CERREA3R_LIST.append(CERREA3R)
        CERREA4R_LIST.append(CERREA4R)
        CERREA5R_LIST.append(CERREA5R)
        CERREA6R_LIST.append(CERREA6R)
        CERREA7R_LIST.append(CERREA7R)
        CERREA8R_LIST.append(CERREA8R)
        CHCHYR_LIST.append(CHCHYR)
        CHCHMOYR_LIST.append(CHCHMOYR)
        CHCHNOY2_LIST.append(CHCHNOY2)
        CHCNOYR2_LIST.append(CHCNOYR2)
        CSRGYR_LIST.append(CSRGYR)
        RSRGNOYR_LIST.append(RSRGNOYR)
        CMDLONGR_LIST.append(CMDLONGR)
        RSCL2_C2_LIST.append(RSCL2_C2)
        RSCL2_E2_LIST.append(RSCL2_E2)
        RSCL3_E3_LIST.append(RSCL3_E3)
        RSCL5_P5_LIST.append(RSCL5_P5)
        RSCL5_H5_LIST.append(RSCL5_H5)
        RSCL6_LIST.append(RSCL6)
        CSHFLU12_LIST.append(CSHFLU12)
        CSHFLUNM_LIST.append(CSHFLUNM)
        CSHFLUM1_LIST.append(CSHFLUM1)
        CSHFLUY1_LIST.append(CSHFLUY1)
        CSHSPFL1_LIST.append(CSHSPFL1)
        CSHFLUM2_LIST.append(CSHFLUM2)
        CSHFLUY2_LIST.append(CSHFLUY2)
        CSHSPFL2_LIST.append(CSHSPFL2)

df = pd.DataFrame(columns=(
                            'RECTYPE',
                            'SRVY_YR',
                            'HHX',
                            'INTV_QRT',
                            'INTV_MON',
                            'FMX',
                            'FPX',
                            'WTIA_SC',
                            'WTFA_SC',
                            'REGION',
                            'STRAT_P',
                            'PSU_P',
                            'SEX',
                            'HISPAN_I',
                            'RACERPI2',
                            'MRACRPI2',
                            'MRACBPI2',
                            'AGE_P',
                            'CSRESPNO',
                            'CSRELTVP',
                            'LATEINTC',
                            'FDRN_FLG',
                            'TOTOZ_P',
                            'BWTGRM_P',
                            'CHGHT_TC',
                            'CWGHT_TC',
                            'BMI_SC',
                            'AMR1R',
                            'AODD1',
                            'ADD2',
                            'AMR2R',
                            'AUTISM',
                            'AODD2',
                            'CCONDRR1',
                            'CCONDRR2',
                            'CCONDRR3',
                            'CCONDRR4',
                            'CCONDRR5',
                            'CCONDRR6',
                            'CCONDRR7',
                            'CCONDRR8',
                            'CCONDRR9',
                            'CPOX',
                            'CPOX12MO',
                            'CASHMEV',
                            'CASSTILL',
                            'CASHYR',
                            'CASERYR1',
                            'HAYF1',
                            'RALLG1',
                            'DALLG1',
                            'SALLG1',
                            'DIARH1',
                            'ANEMIA1',
                            'EARINF1',
                            'SEIZE1',
                            'HAYF2',
                            'RALLG2',
                            'DALLG2',
                            'SALLG2',
                            'DIARH2',
                            'ANEMIA2',
                            'FHEAD',
                            'EARINF2',
                            'SEIZE2',
                            'STUTTER',
                            'CHSTATYR',
                            'SCHDAYR1',
                            'CCOLD2W',
                            'CINTIL2W',
                            'CHEARST2',
                            'CHRWORS',
                            'CHRWORSE',
                            'CHRWHIS1',
                            'CHRTALK1',
                            'CHRSHOU1',
                            'CHRSPEA1',
                            'CHRCOCR1',
                            'CHRCOCI1',
                            'CHRFAM',
                            'CHRMIS',
                            'CHRUNDST',
                            'CHRUNDNS',
                            'CHEARAG1',
                            'CHRCAUS1',
                            'CHRPRBHP',
                            'CHRENT',
                            'CHREHDI',
                            'CHREIAGE',
                            'CHRTUBE',
                            'CHRTBAGE',
                            'CHRTSCH',
                            'CHRTSCHM',
                            'CHRTSCHR',
                            'CHRTEST',
                            'CHRAIDNW',
                            'CHRAIDLG',
                            'CHRAIDYR',
                            'CHRAIDEV',
                            'CHRAIDRC',
                            'CHRAIDLP',
                            'CHRAIDOF',
                            'CHRAID01',
                            'CHRAID02',
                            'CHRAID03',
                            'CHRAID04',
                            'CHRAID05',
                            'CHRAID06',
                            'CHRAID07',
                            'CHRAID08',
                            'CHRAID09',
                            'CHRAID10',
                            'CHRAID11',
                            'CHRAUD',
                            'CHRALDS',
                            'CHRALD01',
                            'CHRALD02',
                            'CHRALD03',
                            'CHRALD04',
                            'CHRALD05',
                            'CHRALD06',
                            'CHRALD07',
                            'CHRALD08',
                            'CHRALD09',
                            'CHRALD10',
                            'CHRALD11',
                            'CHRALD12',
                            'CHRFIRE',
                            'CHRFRCRK',
                            'CHRTOTR',
                            'CHRFRPRT',
                            'CHRWKVLN',
                            'CHRWKVLT',
                            'CHRWKPRT',
                            'CHRLESNS',
                            'CHRLST01',
                            'CHRLST02',
                            'CHRLST03',
                            'CHRLST04',
                            'CHRLST05',
                            'CHRLST06',
                            'CHRLST07',
                            'CHRLST08',
                            'CHRLST09',
                            'CHRLST10',
                            'CHRLST11',
                            'CHRLST12',
                            'CHRLSPRT',
                            'CHRINT',
                            'CHRINTHL',
                            'CHRINTHA',
                            'CHRINTHP',
                            'CHRINHPR',
                            'CVISION',
                            'CBLIND',
                            'IHSPEQ',
                            'IHMOB',
                            'IHMOBYR',
                            'PROBRX',
                            'LEARND',
                            'MHIBOY2',
                            'CMHAGM15',
                            'MHIGRL2',
                            'CMHAGF15',
                            'CUSUALPL',
                            'CPLKIND',
                            'CHCPLROU',
                            'CHCPLKND',
                            'CHCCHGYR',
                            'CHCCHGHI',
                            'CNOUSPL1',
                            'CNOUSPL2',
                            'CNOUSPL3',
                            'CNOUSPL4',
                            'CNOUSPL5',
                            'CNOUSPL6',
                            'CNOUSPL7',
                            'CNOUSPL8',
                            'CNOUSPL9',
                            'CPRVTRYR',
                            'CPRVTRFD',
                            'CDRNANP',
                            'CDRNAI',
                            'CHCDLYR1',
                            'CHCDLYR2',
                            'CHCDLYR3',
                            'CHCDLYR4',
                            'CHCDLYR5',
                            'CHCAFYR',
                            'CHCAFYRN',
                            'CHCAFYRF',
                            'CHCAFYR1',
                            'CHCAFYR2',
                            'CHCAFYR3',
                            'CHCAFYR4',
                            'CHCAFYR5',
                            'CHCAFYR6',
                            'CDNLONGR',
                            'CHCSYR11',
                            'CHCSYR12',
                            'CHCSYR13',
                            'CHCSYR14',
                            'CHCSYR1',
                            'CHCSYR2',
                            'CHCSYR3',
                            'CHCSYR4',
                            'CHCSYR5',
                            'CHCSYR6',
                            'CHCSYR7',
                            'CHCSYR81',
                            'CHCSYR82',
                            'CHCSYR10',
                            'CHCSYREM',
                            'CHPXYR_C',
                            'CHERNOY2',
                            'CERVISND',
                            'CERHOS',
                            'CERREA1R',
                            'CERREA2R',
                            'CERREA3R',
                            'CERREA4R',
                            'CERREA5R',
                            'CERREA6R',
                            'CERREA7R',
                            'CERREA8R',
                            'CHCHYR',
                            'CHCHMOYR',
                            'CHCHNOY2',
                            'CHCNOYR2',
                            'CSRGYR',
                            'RSRGNOYR',
                            'CMDLONGR',
                            'RSCL2_C2',
                            'RSCL2_E2',
                            'RSCL3_E3',
                            'RSCL5_P5',
                            'RSCL5_H5',
                            'RSCL6',
                            'CSHFLU12',
                            'CSHFLUNM',
                            'CSHFLUM1',
                            'CSHFLUY1',
                            'CSHSPFL1',
                            'CSHFLUM2',
                            'CSHFLUY2',
                            'CSHSPFL2'
                                    ))

for i in range(13379):
    df.loc[i] = [
                    RECTYPE_LIST[i],
                    SRVY_YR_LIST[i],
                    HHX_LIST[i],
                    INTV_QRT_LIST[i],
                    INTV_MON_LIST[i],
                    FMX_LIST[i],
                    FPX_LIST[i],
                    WTIA_SC_LIST[i],
                    WTFA_SC_LIST[i],
                    REGION_LIST[i],
                    STRAT_P_LIST[i],
                    PSU_P_LIST[i],
                    SEX_LIST[i],
                    HISPAN_I_LIST[i],
                    RACERPI2_LIST[i],
                    MRACRPI2_LIST[i],
                    MRACBPI2_LIST[i],
                    AGE_P_LIST[i],
                    CSRESPNO_LIST[i],
                    CSRELTVP_LIST[i],
                    LATEINTC_LIST[i],
                    FDRN_FLG_LIST[i],
                    TOTOZ_P_LIST[i],
                    BWTGRM_P_LIST[i],
                    CHGHT_TC_LIST[i],
                    CWGHT_TC_LIST[i],
                    BMI_SC_LIST[i],
                    AMR1R_LIST[i],
                    AODD1_LIST[i],
                    ADD2_LIST[i],
                    AMR2R_LIST[i],
                    AUTISM_LIST[i],
                    AODD2_LIST[i],
                    CCONDRR1_LIST[i],
                    CCONDRR2_LIST[i],
                    CCONDRR3_LIST[i],
                    CCONDRR4_LIST[i],
                    CCONDRR5_LIST[i],
                    CCONDRR6_LIST[i],
                    CCONDRR7_LIST[i],
                    CCONDRR8_LIST[i],
                    CCONDRR9_LIST[i],
                    CPOX_LIST[i],
                    CPOX12MO_LIST[i],
                    CASHMEV_LIST[i],
                    CASSTILL_LIST[i],
                    CASHYR_LIST[i],
                    CASERYR1_LIST[i],
                    HAYF1_LIST[i],
                    RALLG1_LIST[i],
                    DALLG1_LIST[i],
                    SALLG1_LIST[i],
                    DIARH1_LIST[i],
                    ANEMIA1_LIST[i],
                    EARINF1_LIST[i],
                    SEIZE1_LIST[i],
                    HAYF2_LIST[i],
                    RALLG2_LIST[i],
                    DALLG2_LIST[i],
                    SALLG2_LIST[i],
                    DIARH2_LIST[i],
                    ANEMIA2_LIST[i],
                    FHEAD_LIST[i],
                    EARINF2_LIST[i],
                    SEIZE2_LIST[i],
                    STUTTER_LIST[i],
                    CHSTATYR_LIST[i],
                    SCHDAYR1_LIST[i],
                    CCOLD2W_LIST[i],
                    CINTIL2W_LIST[i],
                    CHEARST2_LIST[i],
                    CHRWORS_LIST[i],
                    CHRWORSE_LIST[i],
                    CHRWHIS1_LIST[i],
                    CHRTALK1_LIST[i],
                    CHRSHOU1_LIST[i],
                    CHRSPEA1_LIST[i],
                    CHRCOCR1_LIST[i],
                    CHRCOCI1_LIST[i],
                    CHRFAM_LIST[i],
                    CHRMIS_LIST[i],
                    CHRUNDST_LIST[i],
                    CHRUNDNS_LIST[i],
                    CHEARAG1_LIST[i],
                    CHRCAUS1_LIST[i],
                    CHRPRBHP_LIST[i],
                    CHRENT_LIST[i],
                    CHREHDI_LIST[i],
                    CHREIAGE_LIST[i],
                    CHRTUBE_LIST[i],
                    CHRTBAGE_LIST[i],
                    CHRTSCH_LIST[i],
                    CHRTSCHM_LIST[i],
                    CHRTSCHR_LIST[i],
                    CHRTEST_LIST[i],
                    CHRAIDNW_LIST[i],
                    CHRAIDLG_LIST[i],
                    CHRAIDYR_LIST[i],
                    CHRAIDEV_LIST[i],
                    CHRAIDRC_LIST[i],
                    CHRAIDLP_LIST[i],
                    CHRAIDOF_LIST[i],
                    CHRAID01_LIST[i],
                    CHRAID02_LIST[i],
                    CHRAID03_LIST[i],
                    CHRAID04_LIST[i],
                    CHRAID05_LIST[i],
                    CHRAID06_LIST[i],
                    CHRAID07_LIST[i],
                    CHRAID08_LIST[i],
                    CHRAID09_LIST[i],
                    CHRAID10_LIST[i],
                    CHRAID11_LIST[i],
                    CHRAUD_LIST[i],
                    CHRALDS_LIST[i],
                    CHRALD01_LIST[i],
                    CHRALD02_LIST[i],
                    CHRALD03_LIST[i],
                    CHRALD04_LIST[i],
                    CHRALD05_LIST[i],
                    CHRALD06_LIST[i],
                    CHRALD07_LIST[i],
                    CHRALD08_LIST[i],
                    CHRALD09_LIST[i],
                    CHRALD10_LIST[i],
                    CHRALD11_LIST[i],
                    CHRALD12_LIST[i],
                    CHRFIRE_LIST[i],
                    CHRFRCRK_LIST[i],
                    CHRTOTR_LIST[i],
                    CHRFRPRT_LIST[i],
                    CHRWKVLN_LIST[i],
                    CHRWKVLT_LIST[i],
                    CHRWKPRT_LIST[i],
                    CHRLESNS_LIST[i],
                    CHRLST01_LIST[i],
                    CHRLST02_LIST[i],
                    CHRLST03_LIST[i],
                    CHRLST04_LIST[i],
                    CHRLST05_LIST[i],
                    CHRLST06_LIST[i],
                    CHRLST07_LIST[i],
                    CHRLST08_LIST[i],
                    CHRLST09_LIST[i],
                    CHRLST10_LIST[i],
                    CHRLST11_LIST[i],
                    CHRLST12_LIST[i],
                    CHRLSPRT_LIST[i],
                    CHRINT_LIST[i],
                    CHRINTHL_LIST[i],
                    CHRINTHA_LIST[i],
                    CHRINTHP_LIST[i],
                    CHRINHPR_LIST[i],
                    CVISION_LIST[i],
                    CBLIND_LIST[i],
                    IHSPEQ_LIST[i],
                    IHMOB_LIST[i],
                    IHMOBYR_LIST[i],
                    PROBRX_LIST[i],
                    LEARND_LIST[i],
                    MHIBOY2_LIST[i],
                    CMHAGM15_LIST[i],
                    MHIGRL2_LIST[i],
                    CMHAGF15_LIST[i],
                    CUSUALPL_LIST[i],
                    CPLKIND_LIST[i],
                    CHCPLROU_LIST[i],
                    CHCPLKND_LIST[i],
                    CHCCHGYR_LIST[i],
                    CHCCHGHI_LIST[i],
                    CNOUSPL1_LIST[i],
                    CNOUSPL2_LIST[i],
                    CNOUSPL3_LIST[i],
                    CNOUSPL4_LIST[i],
                    CNOUSPL5_LIST[i],
                    CNOUSPL6_LIST[i],
                    CNOUSPL7_LIST[i],
                    CNOUSPL8_LIST[i],
                    CNOUSPL9_LIST[i],
                    CPRVTRYR_LIST[i],
                    CPRVTRFD_LIST[i],
                    CDRNANP_LIST[i],
                    CDRNAI_LIST[i],
                    CHCDLYR1_LIST[i],
                    CHCDLYR2_LIST[i],
                    CHCDLYR3_LIST[i],
                    CHCDLYR4_LIST[i],
                    CHCDLYR5_LIST[i],
                    CHCAFYR_LIST[i],
                    CHCAFYRN_LIST[i],
                    CHCAFYRF_LIST[i],
                    CHCAFYR1_LIST[i],
                    CHCAFYR2_LIST[i],
                    CHCAFYR3_LIST[i],
                    CHCAFYR4_LIST[i],
                    CHCAFYR5_LIST[i],
                    CHCAFYR6_LIST[i],
                    CDNLONGR_LIST[i],
                    CHCSYR11_LIST[i],
                    CHCSYR12_LIST[i],
                    CHCSYR13_LIST[i],
                    CHCSYR14_LIST[i],
                    CHCSYR1_LIST[i],
                    CHCSYR2_LIST[i],
                    CHCSYR3_LIST[i],
                    CHCSYR4_LIST[i],
                    CHCSYR5_LIST[i],
                    CHCSYR6_LIST[i],
                    CHCSYR7_LIST[i],
                    CHCSYR81_LIST[i],
                    CHCSYR82_LIST[i],
                    CHCSYR10_LIST[i],
                    CHCSYREM_LIST[i],
                    CHPXYR_C_LIST[i],
                    CHERNOY2_LIST[i],
                    CERVISND_LIST[i],
                    CERHOS_LIST[i],
                    CERREA1R_LIST[i],
                    CERREA2R_LIST[i],
                    CERREA3R_LIST[i],
                    CERREA4R_LIST[i],
                    CERREA5R_LIST[i],
                    CERREA6R_LIST[i],
                    CERREA7R_LIST[i],
                    CERREA8R_LIST[i],
                    CHCHYR_LIST[i],
                    CHCHMOYR_LIST[i],
                    CHCHNOY2_LIST[i],
                    CHCNOYR2_LIST[i],
                    CSRGYR_LIST[i],
                    RSRGNOYR_LIST[i],
                    CMDLONGR_LIST[i],
                    RSCL2_C2_LIST[i],
                    RSCL2_E2_LIST[i],
                    RSCL3_E3_LIST[i],
                    RSCL5_P5_LIST[i],
                    RSCL5_H5_LIST[i],
                    RSCL6_LIST[i],
                    CSHFLU12_LIST[i],
                    CSHFLUNM_LIST[i],
                    CSHFLUM1_LIST[i],
                    CSHFLUY1_LIST[i],
                    CSHSPFL1_LIST[i],
                    CSHFLUM2_LIST[i],
                    CSHFLUY2_LIST[i],
                    CSHSPFL2_LIST[i]
                                    ]
df = df.applymap(lambda x: np.nan if str(x).isspace() else x)
df.to_csv("nhis_2014_samchild.csv")
