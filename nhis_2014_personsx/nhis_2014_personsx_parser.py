import pandas as pd
import numpy as np

custom_parser_input_file_name = "nhis_2014_personsx.dat"

RECTYPE = ''
SRVY_YR = ''
HHX = ''
INTV_QRT = ''
INTV_MON = ''
FMX = ''
FPX = ''
WTIA = ''
WTFA = ''
REGION = ''
STRAT_P = ''
PSU_P = ''
SEX = ''
ORIGIN_I = ''
ORIGIMPT = ''
HISPAN_I = ''
HISPIMPT = ''
RACERPI2 = ''
RACEIMP2 = ''
MRACRPI2 = ''
MRACBPI2 = ''
RACRECI3 = ''
HISCODI3 = ''
ERIMPFLG = ''
NOWAF = ''
RRP = ''
HHREFLG = ''
FRRP = ''
DOB_M = ''
DOB_Y_P = ''
AGE_P = ''
AGE_CHG = ''
FMRPFLG = ''
FMREFLG = ''
R_MARITL = ''
FSPOUS2 = ''
COHAB1 = ''
COHAB2 = ''
FCOHAB3 = ''
CDCMSTAT = ''
SIB_DEGP = ''
FMOTHER1 = ''
MOM_DEGP = ''
FFATHER1 = ''
DAD_DEGP = ''
PARENTS = ''
MOM_ED = ''
DAD_ED = ''
ASTATFLG = ''
CSTATFLG = ''
QCADULT = ''
QCCHILD = ''
FDRN_FLG = ''
PLAPLYLM = ''
PLAPLYUN = ''
PSPEDEIS = ''
PSPEDEM = ''
PLAADL = ''
LABATH = ''
LADRESS = ''
LAEAT = ''
LABED = ''
LATOILT = ''
LAHOME = ''
PLAIADL = ''
PLAWKNOW = ''
PLAWKLIM = ''
PLAWALK = ''
PLAREMEM = ''
PLIMANY = ''
LA1AR = ''
LAHCC1 = ''
LAHCC2 = ''
LAHCC3 = ''
LAHCC4 = ''
LAHCC5 = ''
LAHCC6 = ''
LAHCC7A = ''
LAHCC8 = ''
LAHCC9 = ''
LAHCC10 = ''
LAHCC11 = ''
LAHCC12 = ''
LAHCC13 = ''
LAHCC90 = ''
LAHCC91 = ''
LCTIME1 = ''
LCUNIT1 = ''
LCDURA1 = ''
LCDURB1 = ''
LCCHRC1 = ''
LCTIME2 = ''
LCUNIT2 = ''
LCDURA2 = ''
LCDURB2 = ''
LCCHRC2 = ''
LCTIME3 = ''
LCUNIT3 = ''
LCDURA3 = ''
LCDURB3 = ''
LCCHRC3 = ''
LCTIME4 = ''
LCUNIT4 = ''
LCDURA4 = ''
LCDURB4 = ''
LCCHRC4 = ''
LCTIME5 = ''
LCUNIT5 = ''
LCDURA5 = ''
LCDURB5 = ''
LCCHRC5 = ''
LCTIME6 = ''
LCUNIT6 = ''
LCDURA6 = ''
LCDURB6 = ''
LCCHRC6 = ''
LCTIME7A = ''
LCUNIT7A = ''
LCDURA7A = ''
LCDURB7A = ''
LCCHRC7A = ''
LCTIME8 = ''
LCUNIT8 = ''
LCDURA8 = ''
LCDURB8 = ''
LCCHRC8 = ''
LCTIME9 = ''
LCUNIT9 = ''
LCDURA9 = ''
LCDURB9 = ''
LCCHRC9 = ''
LCTIME10 = ''
LCUNIT10 = ''
LCDURA10 = ''
LCDURB10 = ''
LCCHRC10 = ''
LCTIME11 = ''
LCUNIT11 = ''
LCDURA11 = ''
LCDURB11 = ''
LCCHRC11 = ''
LCTIME12 = ''
LCUNIT12 = ''
LCDURA12 = ''
LCDURB12 = ''
LCCHRC12 = ''
LCTIME13 = ''
LCUNIT13 = ''
LCDURA13 = ''
LCDURB13 = ''
LCCHRC13 = ''
LCTIME90 = ''
LCUNIT90 = ''
LCDURA90 = ''
LCDURB90 = ''
LCCHRC90 = ''
LCTIME91 = ''
LCUNIT91 = ''
LCDURA91 = ''
LCDURB91 = ''
LCCHRC91 = ''
LAHCA1 = ''
LAHCA2 = ''
LAHCA3 = ''
LAHCA4 = ''
LAHCA5 = ''
LAHCA6 = ''
LAHCA7 = ''
LAHCA8 = ''
LAHCA9 = ''
LAHCA10 = ''
LAHCA11 = ''
LAHCA12 = ''
LAHCA13 = ''
LAHCA14A = ''
LAHCA15 = ''
LAHCA16 = ''
LAHCA17 = ''
LAHCA18 = ''
LAHCA19_ = ''
LAHCA20_ = ''
LAHCA21_ = ''
LAHCA22_ = ''
LAHCA23_ = ''
LAHCA24_ = ''
LAHCA25_ = ''
LAHCA26_ = ''
LAHCA27_ = ''
LAHCA28_ = ''
LAHCA29_ = ''
LAHCA30_ = ''
LAHCA31_ = ''
LAHCA32_ = ''
LAHCA33_ = ''
LAHCA34_ = ''
LAHCA90 = ''
LAHCA91 = ''
LATIME1 = ''
LAUNIT1 = ''
LADURA1 = ''
LADURB1 = ''
LACHRC1 = ''
LATIME2 = ''
LAUNIT2 = ''
LADURA2 = ''
LADURB2 = ''
LACHRC2 = ''
LATIME3 = ''
LAUNIT3 = ''
LADURA3 = ''
LADURB3 = ''
LACHRC3 = ''
LATIME4 = ''
LAUNIT4 = ''
LADURA4 = ''
LADURB4 = ''
LACHRC4 = ''
LATIME5 = ''
LAUNIT5 = ''
LADURA5 = ''
LADURB5 = ''
LACHRC5 = ''
LATIME6 = ''
LAUNIT6 = ''
LADURA6 = ''
LADURB6 = ''
LACHRC6 = ''
LATIME7 = ''
LAUNIT7 = ''
LADURA7 = ''
LADURB7 = ''
LACHRC7 = ''
LATIME8 = ''
LAUNIT8 = ''
LADURA8 = ''
LADURB8 = ''
LACHRC8 = ''
LATIME9 = ''
LAUNIT9 = ''
LADURA9 = ''
LADURB9 = ''
LACHRC9 = ''
LATIME10 = ''
LAUNIT10 = ''
LADURA10 = ''
LADURB10 = ''
LACHRC10 = ''
LATIME11 = ''
LAUNIT11 = ''
LADURA11 = ''
LADURB11 = ''
LACHRC11 = ''
LATIME12 = ''
LAUNIT12 = ''
LADURA12 = ''
LADURB12 = ''
LACHRC12 = ''
LATIME13 = ''
LAUNIT13 = ''
LADURA13 = ''
LADURB13 = ''
LACHRC13 = ''
LTIME14A = ''
LUNIT14A = ''
LDURA14A = ''
LDURB14A = ''
LCHRC14A = ''
LATIME15 = ''
LAUNIT15 = ''
LADURA15 = ''
LADURB15 = ''
LACHRC15 = ''
LATIME16 = ''
LAUNIT16 = ''
LADURA16 = ''
LADURB16 = ''
LACHRC16 = ''
LATIME17 = ''
LAUNIT17 = ''
LADURA17 = ''
LADURB17 = ''
LACHRC17 = ''
LATIME18 = ''
LAUNIT18 = ''
LADURA18 = ''
LADURB18 = ''
LACHRC18 = ''
LATIME19 = ''
LAUNIT19 = ''
LADURA19 = ''
LADURB19 = ''
LACHRC19 = ''
LATIME20 = ''
LAUNIT20 = ''
LADURA20 = ''
LADURB20 = ''
LACHRC20 = ''
LATIME21 = ''
LAUNIT21 = ''
LADURA21 = ''
LADURB21 = ''
LACHRC21 = ''
LATIME22 = ''
LAUNIT22 = ''
LADURA22 = ''
LADURB22 = ''
LACHRC22 = ''
LATIME23 = ''
LAUNIT23 = ''
LADURA23 = ''
LADURB23 = ''
LACHRC23 = ''
LATIME24 = ''
LAUNIT24 = ''
LADURA24 = ''
LADURB24 = ''
LACHRC24 = ''
LATIME25 = ''
LAUNIT25 = ''
LADURA25 = ''
LADURB25 = ''
LACHRC25 = ''
LATIME26 = ''
LAUNIT26 = ''
LADURA26 = ''
LADURB26 = ''
LACHRC26 = ''
LATIME27 = ''
LAUNIT27 = ''
LADURA27 = ''
LADURB27 = ''
LACHRC27 = ''
LATIME28 = ''
LAUNIT28 = ''
LADURA28 = ''
LADURB28 = ''
LACHRC28 = ''
LATIME29 = ''
LAUNIT29 = ''
LADURA29 = ''
LADURB29 = ''
LACHRC29 = ''
LATIME30 = ''
LAUNIT30 = ''
LADURA30 = ''
LADURB30 = ''
LACHRC30 = ''
LATIME31 = ''
LAUNIT31 = ''
LADURA31 = ''
LADURB31 = ''
LACHRC31 = ''
LATIME32 = ''
LAUNIT32 = ''
LADURA32 = ''
LADURB32 = ''
LACHRC32 = ''
LATIME33 = ''
LAUNIT33 = ''
LADURA33 = ''
LADURB33 = ''
LACHRC33 = ''
LATIME34 = ''
LAUNIT34 = ''
LADURA34 = ''
LADURB34 = ''
LACHRC34 = ''
LATIME90 = ''
LAUNIT90 = ''
LADURA90 = ''
LADURB90 = ''
LACHRC90 = ''
LATIME91 = ''
LAUNIT91 = ''
LADURA91 = ''
LADURB91 = ''
LACHRC91 = ''
LCONDRT = ''
LACHRONR = ''
PHSTAT = ''
PDMED12M = ''
PNMED12M = ''
PHOSPYR2 = ''
HOSPNO = ''
HPNITE = ''
PHCHM2W = ''
PHCHMN2W = ''
PHCPH2WR = ''
PHCPHN2W = ''
PHCDV2W = ''
PHCDVN2W = ''
P10DVYR = ''
NOTCOV = ''
MEDICARE = ''
MCPART = ''
MCCHOICE = ''
MCHMO = ''
MCADVR = ''
MCPREM = ''
MCREF = ''
MCPARTD = ''
MEDICAID = ''
MAFLG = ''
MACHMD = ''
MXCHNG = ''
MEDPREM = ''
MDPRINC = ''
MAPCMD = ''
MAREF = ''
SINGLE = ''
SSTYPEA = ''
SSTYPEB = ''
SSTYPEC = ''
SSTYPED = ''
SSTYPEE = ''
SSTYPEF = ''
SSTYPEG = ''
SSTYPEH = ''
SSTYPEI = ''
SSTYPEJ = ''
SSTYPEK = ''
SSTYPEL = ''
PRIVATE = ''
PRFLG = ''
EXCHANGE = ''
WHONAM1 = ''
PRPOLH1 = ''
PRCOOH1 = ''
PRCTOH1 = ''
PRRLOH11 = ''
PRRLOH21 = ''
PRRLOH31 = ''
PRRLOH41 = ''
PRCNUM1 = ''
COHU191 = ''
COH19251 = ''
COHO251 = ''
PLNWRKR1 = ''
PLNEXCH1 = ''
EXCHPR1 = ''
PLNPAY11 = ''
PLNPAY21 = ''
PLNPAY31 = ''
PLNPAY41 = ''
PLNPAY51 = ''
PLNPAY61 = ''
PLNPAY71 = ''
PLNPRE1 = ''
HICOSTR1 = ''
EMPPAY1 = ''
ECOSTR1 = ''
EMPCSTP1 = ''
PLNMGD1 = ''
HDHP1 = ''
HSAHRA1 = ''
MGCHMD1 = ''
MGPRMD1 = ''
MGPYMD1 = ''
MGPREF1 = ''
PCPREQ1 = ''
PRRXCOV1 = ''
PRDNCOV1 = ''
PXCHNG = ''
PLEXCHPR = ''
PSTRFPRM = ''
PSSPRINC = ''
PSTDOC = ''
PSTCMD = ''
PSTREF = ''
WHONAM2 = ''
PRPOLH2 = ''
PRCOOH2 = ''
PRCTOH2 = ''
PRRLOH12 = ''
PRRLOH22 = ''
PRRLOH32 = ''
PRRLOH42 = ''
PRCNUM2 = ''
COHU192 = ''
COH19252 = ''
COHO252 = ''
PLNWRKR2 = ''
PLNEXCH2 = ''
EXCHPR2 = ''
PLNPAY12 = ''
PLNPAY22 = ''
PLNPAY32 = ''
PLNPAY42 = ''
PLNPAY52 = ''
PLNPAY62 = ''
PLNPAY72 = ''
PLNPRE2 = ''
HICOSTR2 = ''
EMPPAY2 = ''
ECOSTR2 = ''
EMPCSTP2 = ''
PLNMGD2 = ''
HDHP2 = ''
HSAHRA2 = ''
MGCHMD2 = ''
MGPRMD2 = ''
MGPYMD2 = ''
MGPREF2 = ''
PCPREQ2 = ''
PRRXCOV2 = ''
PRDNCOV2 = ''
PRPLPLUS = ''
FCOVCONF = ''
SCHIP = ''
CHFLG = ''
CHXCHNG = ''
STRFPRM1 = ''
CHPRINC = ''
STDOC1 = ''
STPCMD1 = ''
STREF1 = ''
OTHPUB = ''
OPFLG = ''
OPXCHNG = ''
PLEXCHOP = ''
STRFPRM2 = ''
SSPRINC = ''
STDOC2 = ''
STPCMD2 = ''
STREF2 = ''
OTHGOV = ''
OGFLG = ''
OGXCHNG = ''
PLEXCHOG = ''
STRFPRM3 = ''
OGPRINC = ''
STDOC3 = ''
STPCMD3 = ''
STREF3 = ''
MILCARE = ''
MILSPC1 = ''
MILSPC2 = ''
MILSPC3 = ''
MILSPC4 = ''
MILMAN = ''
IHS = ''
HILAST = ''
HISTOP1 = ''
HISTOP2 = ''
HISTOP3 = ''
HISTOP4 = ''
HISTOP5 = ''
HISTOP6 = ''
HISTOP7 = ''
HISTOP8 = ''
HISTOP9 = ''
HISTOP10 = ''
HISTOP11 = ''
HISTOP12 = ''
HISTOP13 = ''
HISTOP14 = ''
HISTOP15 = ''
HINOTYR = ''
HINOTMYR = ''
FHICHNG = ''
FHIKDBA = ''
FHIKDBB = ''
FHIKDBC = ''
FHIKDBD = ''
FHIKDBE = ''
FHIKDBF = ''
FHIKDBG = ''
FHIKDBH = ''
FHIKDBI = ''
FHIKDBJ = ''
FHIKDBK = ''
PWRKBR1 = ''
HCSPFYR = ''
MEDBILL = ''
MEDBPAY = ''
MEDBNOP = ''
FSA = ''
HIKINDNA = ''
HIKINDNB = ''
HIKINDNC = ''
HIKINDND = ''
HIKINDNE = ''
HIKINDNF = ''
HIKINDNG = ''
HIKINDNH = ''
HIKINDNI = ''
HIKINDNJ = ''
HIKINDNK = ''
MCAREPRB = ''
MCAIDPRB = ''
SINCOV = ''
PLBORN = ''
REGIONBR = ''
GEOBRTH = ''
YRSINUS = ''
CITIZENP = ''
HEADST = ''
HEADSTV1 = ''
EDUC1 = ''
ARMFVER = ''
ARMFEV = ''
ARMFFC = ''
ARMFTM1P = ''
ARMFTM2P = ''
ARMFTM3P = ''
ARMFTM4P = ''
ARMFTM5P = ''
ARMFTM6P = ''
ARMFTM7P = ''
ARMFDS2P = ''
DOINGLWP = ''
WHYNOWKP = ''
WRKHRS2 = ''
WRKFTALL = ''
WRKLYR1 = ''
WRKMYR = ''
ERNYR_P = ''
HIEMPOF = ''
FINCINT = ''
PSAL = ''
PSEINC = ''
PSSRR = ''
PSSRRDB = ''
PSSRRD = ''
PPENS = ''
POPENS = ''
PSSI = ''
PSSID = ''
PTANF = ''
POWBEN = ''
PINTRSTR = ''
PDIVD = ''
PCHLDSP = ''
PINCOT = ''
PSSAPL = ''
PSDAPL = ''
TANFMYR = ''
ELIGPWIC = ''
PWIC = ''
WIC_FLAG = ''
ENGLANG = ''

RECTYPE_LIST = []
SRVY_YR_LIST = []
HHX_LIST = []
INTV_QRT_LIST = []
INTV_MON_LIST = []
FMX_LIST = []
FPX_LIST = []
WTIA_LIST = []
WTFA_LIST = []
REGION_LIST = []
STRAT_P_LIST = []
PSU_P_LIST = []
SEX_LIST = []
ORIGIN_I_LIST = []
ORIGIMPT_LIST = []
HISPAN_I_LIST = []
HISPIMPT_LIST = []
RACERPI2_LIST = []
RACEIMP2_LIST = []
MRACRPI2_LIST = []
MRACBPI2_LIST = []
RACRECI3_LIST = []
HISCODI3_LIST = []
ERIMPFLG_LIST = []
NOWAF_LIST = []
RRP_LIST = []
HHREFLG_LIST = []
FRRP_LIST = []
DOB_M_LIST = []
DOB_Y_P_LIST = []
AGE_P_LIST = []
AGE_CHG_LIST = []
FMRPFLG_LIST = []
FMREFLG_LIST = []
R_MARITL_LIST = []
FSPOUS2_LIST = []
COHAB1_LIST = []
COHAB2_LIST = []
FCOHAB3_LIST = []
CDCMSTAT_LIST = []
SIB_DEGP_LIST = []
FMOTHER1_LIST = []
MOM_DEGP_LIST = []
FFATHER1_LIST = []
DAD_DEGP_LIST = []
PARENTS_LIST = []
MOM_ED_LIST = []
DAD_ED_LIST = []
ASTATFLG_LIST = []
CSTATFLG_LIST = []
QCADULT_LIST = []
QCCHILD_LIST = []
FDRN_FLG_LIST = []
PLAPLYLM_LIST = []
PLAPLYUN_LIST = []
PSPEDEIS_LIST = []
PSPEDEM_LIST = []
PLAADL_LIST = []
LABATH_LIST = []
LADRESS_LIST = []
LAEAT_LIST = []
LABED_LIST = []
LATOILT_LIST = []
LAHOME_LIST = []
PLAIADL_LIST = []
PLAWKNOW_LIST = []
PLAWKLIM_LIST = []
PLAWALK_LIST = []
PLAREMEM_LIST = []
PLIMANY_LIST = []
LA1AR_LIST = []
LAHCC1_LIST = []
LAHCC2_LIST = []
LAHCC3_LIST = []
LAHCC4_LIST = []
LAHCC5_LIST = []
LAHCC6_LIST = []
LAHCC7A_LIST = []
LAHCC8_LIST = []
LAHCC9_LIST = []
LAHCC10_LIST = []
LAHCC11_LIST = []
LAHCC12_LIST = []
LAHCC13_LIST = []
LAHCC90_LIST = []
LAHCC91_LIST = []
LCTIME1_LIST = []
LCUNIT1_LIST = []
LCDURA1_LIST = []
LCDURB1_LIST = []
LCCHRC1_LIST = []
LCTIME2_LIST = []
LCUNIT2_LIST = []
LCDURA2_LIST = []
LCDURB2_LIST = []
LCCHRC2_LIST = []
LCTIME3_LIST = []
LCUNIT3_LIST = []
LCDURA3_LIST = []
LCDURB3_LIST = []
LCCHRC3_LIST = []
LCTIME4_LIST = []
LCUNIT4_LIST = []
LCDURA4_LIST = []
LCDURB4_LIST = []
LCCHRC4_LIST = []
LCTIME5_LIST = []
LCUNIT5_LIST = []
LCDURA5_LIST = []
LCDURB5_LIST = []
LCCHRC5_LIST = []
LCTIME6_LIST = []
LCUNIT6_LIST = []
LCDURA6_LIST = []
LCDURB6_LIST = []
LCCHRC6_LIST = []
LCTIME7A_LIST = []
LCUNIT7A_LIST = []
LCDURA7A_LIST = []
LCDURB7A_LIST = []
LCCHRC7A_LIST = []
LCTIME8_LIST = []
LCUNIT8_LIST = []
LCDURA8_LIST = []
LCDURB8_LIST = []
LCCHRC8_LIST = []
LCTIME9_LIST = []
LCUNIT9_LIST = []
LCDURA9_LIST = []
LCDURB9_LIST = []
LCCHRC9_LIST = []
LCTIME10_LIST = []
LCUNIT10_LIST = []
LCDURA10_LIST = []
LCDURB10_LIST = []
LCCHRC10_LIST = []
LCTIME11_LIST = []
LCUNIT11_LIST = []
LCDURA11_LIST = []
LCDURB11_LIST = []
LCCHRC11_LIST = []
LCTIME12_LIST = []
LCUNIT12_LIST = []
LCDURA12_LIST = []
LCDURB12_LIST = []
LCCHRC12_LIST = []
LCTIME13_LIST = []
LCUNIT13_LIST = []
LCDURA13_LIST = []
LCDURB13_LIST = []
LCCHRC13_LIST = []
LCTIME90_LIST = []
LCUNIT90_LIST = []
LCDURA90_LIST = []
LCDURB90_LIST = []
LCCHRC90_LIST = []
LCTIME91_LIST = []
LCUNIT91_LIST = []
LCDURA91_LIST = []
LCDURB91_LIST = []
LCCHRC91_LIST = []
LAHCA1_LIST = []
LAHCA2_LIST = []
LAHCA3_LIST = []
LAHCA4_LIST = []
LAHCA5_LIST = []
LAHCA6_LIST = []
LAHCA7_LIST = []
LAHCA8_LIST = []
LAHCA9_LIST = []
LAHCA10_LIST = []
LAHCA11_LIST = []
LAHCA12_LIST = []
LAHCA13_LIST = []
LAHCA14A_LIST = []
LAHCA15_LIST = []
LAHCA16_LIST = []
LAHCA17_LIST = []
LAHCA18_LIST = []
LAHCA19__LIST = []
LAHCA20__LIST = []
LAHCA21__LIST = []
LAHCA22__LIST = []
LAHCA23__LIST = []
LAHCA24__LIST = []
LAHCA25__LIST = []
LAHCA26__LIST = []
LAHCA27__LIST = []
LAHCA28__LIST = []
LAHCA29__LIST = []
LAHCA30__LIST = []
LAHCA31__LIST = []
LAHCA32__LIST = []
LAHCA33__LIST = []
LAHCA34__LIST = []
LAHCA90_LIST = []
LAHCA91_LIST = []
LATIME1_LIST = []
LAUNIT1_LIST = []
LADURA1_LIST = []
LADURB1_LIST = []
LACHRC1_LIST = []
LATIME2_LIST = []
LAUNIT2_LIST = []
LADURA2_LIST = []
LADURB2_LIST = []
LACHRC2_LIST = []
LATIME3_LIST = []
LAUNIT3_LIST = []
LADURA3_LIST = []
LADURB3_LIST = []
LACHRC3_LIST = []
LATIME4_LIST = []
LAUNIT4_LIST = []
LADURA4_LIST = []
LADURB4_LIST = []
LACHRC4_LIST = []
LATIME5_LIST = []
LAUNIT5_LIST = []
LADURA5_LIST = []
LADURB5_LIST = []
LACHRC5_LIST = []
LATIME6_LIST = []
LAUNIT6_LIST = []
LADURA6_LIST = []
LADURB6_LIST = []
LACHRC6_LIST = []
LATIME7_LIST = []
LAUNIT7_LIST = []
LADURA7_LIST = []
LADURB7_LIST = []
LACHRC7_LIST = []
LATIME8_LIST = []
LAUNIT8_LIST = []
LADURA8_LIST = []
LADURB8_LIST = []
LACHRC8_LIST = []
LATIME9_LIST = []
LAUNIT9_LIST = []
LADURA9_LIST = []
LADURB9_LIST = []
LACHRC9_LIST = []
LATIME10_LIST = []
LAUNIT10_LIST = []
LADURA10_LIST = []
LADURB10_LIST = []
LACHRC10_LIST = []
LATIME11_LIST = []
LAUNIT11_LIST = []
LADURA11_LIST = []
LADURB11_LIST = []
LACHRC11_LIST = []
LATIME12_LIST = []
LAUNIT12_LIST = []
LADURA12_LIST = []
LADURB12_LIST = []
LACHRC12_LIST = []
LATIME13_LIST = []
LAUNIT13_LIST = []
LADURA13_LIST = []
LADURB13_LIST = []
LACHRC13_LIST = []
LTIME14A_LIST = []
LUNIT14A_LIST = []
LDURA14A_LIST = []
LDURB14A_LIST = []
LCHRC14A_LIST = []
LATIME15_LIST = []
LAUNIT15_LIST = []
LADURA15_LIST = []
LADURB15_LIST = []
LACHRC15_LIST = []
LATIME16_LIST = []
LAUNIT16_LIST = []
LADURA16_LIST = []
LADURB16_LIST = []
LACHRC16_LIST = []
LATIME17_LIST = []
LAUNIT17_LIST = []
LADURA17_LIST = []
LADURB17_LIST = []
LACHRC17_LIST = []
LATIME18_LIST = []
LAUNIT18_LIST = []
LADURA18_LIST = []
LADURB18_LIST = []
LACHRC18_LIST = []
LATIME19_LIST = []
LAUNIT19_LIST = []
LADURA19_LIST = []
LADURB19_LIST = []
LACHRC19_LIST = []
LATIME20_LIST = []
LAUNIT20_LIST = []
LADURA20_LIST = []
LADURB20_LIST = []
LACHRC20_LIST = []
LATIME21_LIST = []
LAUNIT21_LIST = []
LADURA21_LIST = []
LADURB21_LIST = []
LACHRC21_LIST = []
LATIME22_LIST = []
LAUNIT22_LIST = []
LADURA22_LIST = []
LADURB22_LIST = []
LACHRC22_LIST = []
LATIME23_LIST = []
LAUNIT23_LIST = []
LADURA23_LIST = []
LADURB23_LIST = []
LACHRC23_LIST = []
LATIME24_LIST = []
LAUNIT24_LIST = []
LADURA24_LIST = []
LADURB24_LIST = []
LACHRC24_LIST = []
LATIME25_LIST = []
LAUNIT25_LIST = []
LADURA25_LIST = []
LADURB25_LIST = []
LACHRC25_LIST = []
LATIME26_LIST = []
LAUNIT26_LIST = []
LADURA26_LIST = []
LADURB26_LIST = []
LACHRC26_LIST = []
LATIME27_LIST = []
LAUNIT27_LIST = []
LADURA27_LIST = []
LADURB27_LIST = []
LACHRC27_LIST = []
LATIME28_LIST = []
LAUNIT28_LIST = []
LADURA28_LIST = []
LADURB28_LIST = []
LACHRC28_LIST = []
LATIME29_LIST = []
LAUNIT29_LIST = []
LADURA29_LIST = []
LADURB29_LIST = []
LACHRC29_LIST = []
LATIME30_LIST = []
LAUNIT30_LIST = []
LADURA30_LIST = []
LADURB30_LIST = []
LACHRC30_LIST = []
LATIME31_LIST = []
LAUNIT31_LIST = []
LADURA31_LIST = []
LADURB31_LIST = []
LACHRC31_LIST = []
LATIME32_LIST = []
LAUNIT32_LIST = []
LADURA32_LIST = []
LADURB32_LIST = []
LACHRC32_LIST = []
LATIME33_LIST = []
LAUNIT33_LIST = []
LADURA33_LIST = []
LADURB33_LIST = []
LACHRC33_LIST = []
LATIME34_LIST = []
LAUNIT34_LIST = []
LADURA34_LIST = []
LADURB34_LIST = []
LACHRC34_LIST = []
LATIME90_LIST = []
LAUNIT90_LIST = []
LADURA90_LIST = []
LADURB90_LIST = []
LACHRC90_LIST = []
LATIME91_LIST = []
LAUNIT91_LIST = []
LADURA91_LIST = []
LADURB91_LIST = []
LACHRC91_LIST = []
LCONDRT_LIST = []
LACHRONR_LIST = []
PHSTAT_LIST = []
PDMED12M_LIST = []
PNMED12M_LIST = []
PHOSPYR2_LIST = []
HOSPNO_LIST = []
HPNITE_LIST = []
PHCHM2W_LIST = []
PHCHMN2W_LIST = []
PHCPH2WR_LIST = []
PHCPHN2W_LIST = []
PHCDV2W_LIST = []
PHCDVN2W_LIST = []
P10DVYR_LIST = []
NOTCOV_LIST = []
MEDICARE_LIST = []
MCPART_LIST = []
MCCHOICE_LIST = []
MCHMO_LIST = []
MCADVR_LIST = []
MCPREM_LIST = []
MCREF_LIST = []
MCPARTD_LIST = []
MEDICAID_LIST = []
MAFLG_LIST = []
MACHMD_LIST = []
MXCHNG_LIST = []
MEDPREM_LIST = []
MDPRINC_LIST = []
MAPCMD_LIST = []
MAREF_LIST = []
SINGLE_LIST = []
SSTYPEA_LIST = []
SSTYPEB_LIST = []
SSTYPEC_LIST = []
SSTYPED_LIST = []
SSTYPEE_LIST = []
SSTYPEF_LIST = []
SSTYPEG_LIST = []
SSTYPEH_LIST = []
SSTYPEI_LIST = []
SSTYPEJ_LIST = []
SSTYPEK_LIST = []
SSTYPEL_LIST = []
PRIVATE_LIST = []
PRFLG_LIST = []
EXCHANGE_LIST = []
WHONAM1_LIST = []
PRPOLH1_LIST = []
PRCOOH1_LIST = []
PRCTOH1_LIST = []
PRRLOH11_LIST = []
PRRLOH21_LIST = []
PRRLOH31_LIST = []
PRRLOH41_LIST = []
PRCNUM1_LIST = []
COHU191_LIST = []
COH19251_LIST = []
COHO251_LIST = []
PLNWRKR1_LIST = []
PLNEXCH1_LIST = []
EXCHPR1_LIST = []
PLNPAY11_LIST = []
PLNPAY21_LIST = []
PLNPAY31_LIST = []
PLNPAY41_LIST = []
PLNPAY51_LIST = []
PLNPAY61_LIST = []
PLNPAY71_LIST = []
PLNPRE1_LIST = []
HICOSTR1_LIST = []
EMPPAY1_LIST = []
ECOSTR1_LIST = []
EMPCSTP1_LIST = []
PLNMGD1_LIST = []
HDHP1_LIST = []
HSAHRA1_LIST = []
MGCHMD1_LIST = []
MGPRMD1_LIST = []
MGPYMD1_LIST = []
MGPREF1_LIST = []
PCPREQ1_LIST = []
PRRXCOV1_LIST = []
PRDNCOV1_LIST = []
PXCHNG_LIST = []
PLEXCHPR_LIST = []
PSTRFPRM_LIST = []
PSSPRINC_LIST = []
PSTDOC_LIST = []
PSTCMD_LIST = []
PSTREF_LIST = []
WHONAM2_LIST = []
PRPOLH2_LIST = []
PRCOOH2_LIST = []
PRCTOH2_LIST = []
PRRLOH12_LIST = []
PRRLOH22_LIST = []
PRRLOH32_LIST = []
PRRLOH42_LIST = []
PRCNUM2_LIST = []
COHU192_LIST = []
COH19252_LIST = []
COHO252_LIST = []
PLNWRKR2_LIST = []
PLNEXCH2_LIST = []
EXCHPR2_LIST = []
PLNPAY12_LIST = []
PLNPAY22_LIST = []
PLNPAY32_LIST = []
PLNPAY42_LIST = []
PLNPAY52_LIST = []
PLNPAY62_LIST = []
PLNPAY72_LIST = []
PLNPRE2_LIST = []
HICOSTR2_LIST = []
EMPPAY2_LIST = []
ECOSTR2_LIST = []
EMPCSTP2_LIST = []
PLNMGD2_LIST = []
HDHP2_LIST = []
HSAHRA2_LIST = []
MGCHMD2_LIST = []
MGPRMD2_LIST = []
MGPYMD2_LIST = []
MGPREF2_LIST = []
PCPREQ2_LIST = []
PRRXCOV2_LIST = []
PRDNCOV2_LIST = []
PRPLPLUS_LIST = []
FCOVCONF_LIST = []
SCHIP_LIST = []
CHFLG_LIST = []
CHXCHNG_LIST = []
STRFPRM1_LIST = []
CHPRINC_LIST = []
STDOC1_LIST = []
STPCMD1_LIST = []
STREF1_LIST = []
OTHPUB_LIST = []
OPFLG_LIST = []
OPXCHNG_LIST = []
PLEXCHOP_LIST = []
STRFPRM2_LIST = []
SSPRINC_LIST = []
STDOC2_LIST = []
STPCMD2_LIST = []
STREF2_LIST = []
OTHGOV_LIST = []
OGFLG_LIST = []
OGXCHNG_LIST = []
PLEXCHOG_LIST = []
STRFPRM3_LIST = []
OGPRINC_LIST = []
STDOC3_LIST = []
STPCMD3_LIST = []
STREF3_LIST = []
MILCARE_LIST = []
MILSPC1_LIST = []
MILSPC2_LIST = []
MILSPC3_LIST = []
MILSPC4_LIST = []
MILMAN_LIST = []
IHS_LIST = []
HILAST_LIST = []
HISTOP1_LIST = []
HISTOP2_LIST = []
HISTOP3_LIST = []
HISTOP4_LIST = []
HISTOP5_LIST = []
HISTOP6_LIST = []
HISTOP7_LIST = []
HISTOP8_LIST = []
HISTOP9_LIST = []
HISTOP10_LIST = []
HISTOP11_LIST = []
HISTOP12_LIST = []
HISTOP13_LIST = []
HISTOP14_LIST = []
HISTOP15_LIST = []
HINOTYR_LIST = []
HINOTMYR_LIST = []
FHICHNG_LIST = []
FHIKDBA_LIST = []
FHIKDBB_LIST = []
FHIKDBC_LIST = []
FHIKDBD_LIST = []
FHIKDBE_LIST = []
FHIKDBF_LIST = []
FHIKDBG_LIST = []
FHIKDBH_LIST = []
FHIKDBI_LIST = []
FHIKDBJ_LIST = []
FHIKDBK_LIST = []
PWRKBR1_LIST = []
HCSPFYR_LIST = []
MEDBILL_LIST = []
MEDBPAY_LIST = []
MEDBNOP_LIST = []
FSA_LIST = []
HIKINDNA_LIST = []
HIKINDNB_LIST = []
HIKINDNC_LIST = []
HIKINDND_LIST = []
HIKINDNE_LIST = []
HIKINDNF_LIST = []
HIKINDNG_LIST = []
HIKINDNH_LIST = []
HIKINDNI_LIST = []
HIKINDNJ_LIST = []
HIKINDNK_LIST = []
MCAREPRB_LIST = []
MCAIDPRB_LIST = []
SINCOV_LIST = []
PLBORN_LIST = []
REGIONBR_LIST = []
GEOBRTH_LIST = []
YRSINUS_LIST = []
CITIZENP_LIST = []
HEADST_LIST = []
HEADSTV1_LIST = []
EDUC1_LIST = []
ARMFVER_LIST = []
ARMFEV_LIST = []
ARMFFC_LIST = []
ARMFTM1P_LIST = []
ARMFTM2P_LIST = []
ARMFTM3P_LIST = []
ARMFTM4P_LIST = []
ARMFTM5P_LIST = []
ARMFTM6P_LIST = []
ARMFTM7P_LIST = []
ARMFDS2P_LIST = []
DOINGLWP_LIST = []
WHYNOWKP_LIST = []
WRKHRS2_LIST = []
WRKFTALL_LIST = []
WRKLYR1_LIST = []
WRKMYR_LIST = []
ERNYR_P_LIST = []
HIEMPOF_LIST = []
FINCINT_LIST = []
PSAL_LIST = []
PSEINC_LIST = []
PSSRR_LIST = []
PSSRRDB_LIST = []
PSSRRD_LIST = []
PPENS_LIST = []
POPENS_LIST = []
PSSI_LIST = []
PSSID_LIST = []
PTANF_LIST = []
POWBEN_LIST = []
PINTRSTR_LIST = []
PDIVD_LIST = []
PCHLDSP_LIST = []
PINCOT_LIST = []
PSSAPL_LIST = []
PSDAPL_LIST = []
TANFMYR_LIST = []
ELIGPWIC_LIST = []
PWIC_LIST = []
WIC_FLAG_LIST = []
ENGLANG_LIST = []

with open(custom_parser_input_file_name, encoding="utf8", mode="r") as f:
    for ldx, line in enumerate(f):
        if ldx < 112052:
            RECTYPE_accumulator_LIST = []
            SRVY_YR_accumulator_LIST = []
            HHX_accumulator_LIST = []
            INTV_QRT_accumulator_LIST = []
            INTV_MON_accumulator_LIST = []
            FMX_accumulator_LIST = []
            FPX_accumulator_LIST = []
            WTIA_accumulator_LIST = []
            WTFA_accumulator_LIST = []
            REGION_accumulator_LIST = []
            STRAT_P_accumulator_LIST = []
            PSU_P_accumulator_LIST = []
            SEX_accumulator_LIST = []
            ORIGIN_I_accumulator_LIST = []
            ORIGIMPT_accumulator_LIST = []
            HISPAN_I_accumulator_LIST = []
            HISPIMPT_accumulator_LIST = []
            RACERPI2_accumulator_LIST = []
            RACEIMP2_accumulator_LIST = []
            MRACRPI2_accumulator_LIST = []
            MRACBPI2_accumulator_LIST = []
            RACRECI3_accumulator_LIST = []
            HISCODI3_accumulator_LIST = []
            ERIMPFLG_accumulator_LIST = []
            NOWAF_accumulator_LIST = []
            RRP_accumulator_LIST = []
            HHREFLG_accumulator_LIST = []
            FRRP_accumulator_LIST = []
            DOB_M_accumulator_LIST = []
            DOB_Y_P_accumulator_LIST = []
            AGE_P_accumulator_LIST = []
            AGE_CHG_accumulator_LIST = []
            FMRPFLG_accumulator_LIST = []
            FMREFLG_accumulator_LIST = []
            R_MARITL_accumulator_LIST = []
            FSPOUS2_accumulator_LIST = []
            COHAB1_accumulator_LIST = []
            COHAB2_accumulator_LIST = []
            FCOHAB3_accumulator_LIST = []
            CDCMSTAT_accumulator_LIST = []
            SIB_DEGP_accumulator_LIST = []
            FMOTHER1_accumulator_LIST = []
            MOM_DEGP_accumulator_LIST = []
            FFATHER1_accumulator_LIST = []
            DAD_DEGP_accumulator_LIST = []
            PARENTS_accumulator_LIST = []
            MOM_ED_accumulator_LIST = []
            DAD_ED_accumulator_LIST = []
            ASTATFLG_accumulator_LIST = []
            CSTATFLG_accumulator_LIST = []
            QCADULT_accumulator_LIST = []
            QCCHILD_accumulator_LIST = []
            FDRN_FLG_accumulator_LIST = []
            PLAPLYLM_accumulator_LIST = []
            PLAPLYUN_accumulator_LIST = []
            PSPEDEIS_accumulator_LIST = []
            PSPEDEM_accumulator_LIST = []
            PLAADL_accumulator_LIST = []
            LABATH_accumulator_LIST = []
            LADRESS_accumulator_LIST = []
            LAEAT_accumulator_LIST = []
            LABED_accumulator_LIST = []
            LATOILT_accumulator_LIST = []
            LAHOME_accumulator_LIST = []
            PLAIADL_accumulator_LIST = []
            PLAWKNOW_accumulator_LIST = []
            PLAWKLIM_accumulator_LIST = []
            PLAWALK_accumulator_LIST = []
            PLAREMEM_accumulator_LIST = []
            PLIMANY_accumulator_LIST = []
            LA1AR_accumulator_LIST = []
            LAHCC1_accumulator_LIST = []
            LAHCC2_accumulator_LIST = []
            LAHCC3_accumulator_LIST = []
            LAHCC4_accumulator_LIST = []
            LAHCC5_accumulator_LIST = []
            LAHCC6_accumulator_LIST = []
            LAHCC7A_accumulator_LIST = []
            LAHCC8_accumulator_LIST = []
            LAHCC9_accumulator_LIST = []
            LAHCC10_accumulator_LIST = []
            LAHCC11_accumulator_LIST = []
            LAHCC12_accumulator_LIST = []
            LAHCC13_accumulator_LIST = []
            LAHCC90_accumulator_LIST = []
            LAHCC91_accumulator_LIST = []
            LCTIME1_accumulator_LIST = []
            LCUNIT1_accumulator_LIST = []
            LCDURA1_accumulator_LIST = []
            LCDURB1_accumulator_LIST = []
            LCCHRC1_accumulator_LIST = []
            LCTIME2_accumulator_LIST = []
            LCUNIT2_accumulator_LIST = []
            LCDURA2_accumulator_LIST = []
            LCDURB2_accumulator_LIST = []
            LCCHRC2_accumulator_LIST = []
            LCTIME3_accumulator_LIST = []
            LCUNIT3_accumulator_LIST = []
            LCDURA3_accumulator_LIST = []
            LCDURB3_accumulator_LIST = []
            LCCHRC3_accumulator_LIST = []
            LCTIME4_accumulator_LIST = []
            LCUNIT4_accumulator_LIST = []
            LCDURA4_accumulator_LIST = []
            LCDURB4_accumulator_LIST = []
            LCCHRC4_accumulator_LIST = []
            LCTIME5_accumulator_LIST = []
            LCUNIT5_accumulator_LIST = []
            LCDURA5_accumulator_LIST = []
            LCDURB5_accumulator_LIST = []
            LCCHRC5_accumulator_LIST = []
            LCTIME6_accumulator_LIST = []
            LCUNIT6_accumulator_LIST = []
            LCDURA6_accumulator_LIST = []
            LCDURB6_accumulator_LIST = []
            LCCHRC6_accumulator_LIST = []
            LCTIME7A_accumulator_LIST = []
            LCUNIT7A_accumulator_LIST = []
            LCDURA7A_accumulator_LIST = []
            LCDURB7A_accumulator_LIST = []
            LCCHRC7A_accumulator_LIST = []
            LCTIME8_accumulator_LIST = []
            LCUNIT8_accumulator_LIST = []
            LCDURA8_accumulator_LIST = []
            LCDURB8_accumulator_LIST = []
            LCCHRC8_accumulator_LIST = []
            LCTIME9_accumulator_LIST = []
            LCUNIT9_accumulator_LIST = []
            LCDURA9_accumulator_LIST = []
            LCDURB9_accumulator_LIST = []
            LCCHRC9_accumulator_LIST = []
            LCTIME10_accumulator_LIST = []
            LCUNIT10_accumulator_LIST = []
            LCDURA10_accumulator_LIST = []
            LCDURB10_accumulator_LIST = []
            LCCHRC10_accumulator_LIST = []
            LCTIME11_accumulator_LIST = []
            LCUNIT11_accumulator_LIST = []
            LCDURA11_accumulator_LIST = []
            LCDURB11_accumulator_LIST = []
            LCCHRC11_accumulator_LIST = []
            LCTIME12_accumulator_LIST = []
            LCUNIT12_accumulator_LIST = []
            LCDURA12_accumulator_LIST = []
            LCDURB12_accumulator_LIST = []
            LCCHRC12_accumulator_LIST = []
            LCTIME13_accumulator_LIST = []
            LCUNIT13_accumulator_LIST = []
            LCDURA13_accumulator_LIST = []
            LCDURB13_accumulator_LIST = []
            LCCHRC13_accumulator_LIST = []
            LCTIME90_accumulator_LIST = []
            LCUNIT90_accumulator_LIST = []
            LCDURA90_accumulator_LIST = []
            LCDURB90_accumulator_LIST = []
            LCCHRC90_accumulator_LIST = []
            LCTIME91_accumulator_LIST = []
            LCUNIT91_accumulator_LIST = []
            LCDURA91_accumulator_LIST = []
            LCDURB91_accumulator_LIST = []
            LCCHRC91_accumulator_LIST = []
            LAHCA1_accumulator_LIST = []
            LAHCA2_accumulator_LIST = []
            LAHCA3_accumulator_LIST = []
            LAHCA4_accumulator_LIST = []
            LAHCA5_accumulator_LIST = []
            LAHCA6_accumulator_LIST = []
            LAHCA7_accumulator_LIST = []
            LAHCA8_accumulator_LIST = []
            LAHCA9_accumulator_LIST = []
            LAHCA10_accumulator_LIST = []
            LAHCA11_accumulator_LIST = []
            LAHCA12_accumulator_LIST = []
            LAHCA13_accumulator_LIST = []
            LAHCA14A_accumulator_LIST = []
            LAHCA15_accumulator_LIST = []
            LAHCA16_accumulator_LIST = []
            LAHCA17_accumulator_LIST = []
            LAHCA18_accumulator_LIST = []
            LAHCA19__accumulator_LIST = []
            LAHCA20__accumulator_LIST = []
            LAHCA21__accumulator_LIST = []
            LAHCA22__accumulator_LIST = []
            LAHCA23__accumulator_LIST = []
            LAHCA24__accumulator_LIST = []
            LAHCA25__accumulator_LIST = []
            LAHCA26__accumulator_LIST = []
            LAHCA27__accumulator_LIST = []
            LAHCA28__accumulator_LIST = []
            LAHCA29__accumulator_LIST = []
            LAHCA30__accumulator_LIST = []
            LAHCA31__accumulator_LIST = []
            LAHCA32__accumulator_LIST = []
            LAHCA33__accumulator_LIST = []
            LAHCA34__accumulator_LIST = []
            LAHCA90_accumulator_LIST = []
            LAHCA91_accumulator_LIST = []
            LATIME1_accumulator_LIST = []
            LAUNIT1_accumulator_LIST = []
            LADURA1_accumulator_LIST = []
            LADURB1_accumulator_LIST = []
            LACHRC1_accumulator_LIST = []
            LATIME2_accumulator_LIST = []
            LAUNIT2_accumulator_LIST = []
            LADURA2_accumulator_LIST = []
            LADURB2_accumulator_LIST = []
            LACHRC2_accumulator_LIST = []
            LATIME3_accumulator_LIST = []
            LAUNIT3_accumulator_LIST = []
            LADURA3_accumulator_LIST = []
            LADURB3_accumulator_LIST = []
            LACHRC3_accumulator_LIST = []
            LATIME4_accumulator_LIST = []
            LAUNIT4_accumulator_LIST = []
            LADURA4_accumulator_LIST = []
            LADURB4_accumulator_LIST = []
            LACHRC4_accumulator_LIST = []
            LATIME5_accumulator_LIST = []
            LAUNIT5_accumulator_LIST = []
            LADURA5_accumulator_LIST = []
            LADURB5_accumulator_LIST = []
            LACHRC5_accumulator_LIST = []
            LATIME6_accumulator_LIST = []
            LAUNIT6_accumulator_LIST = []
            LADURA6_accumulator_LIST = []
            LADURB6_accumulator_LIST = []
            LACHRC6_accumulator_LIST = []
            LATIME7_accumulator_LIST = []
            LAUNIT7_accumulator_LIST = []
            LADURA7_accumulator_LIST = []
            LADURB7_accumulator_LIST = []
            LACHRC7_accumulator_LIST = []
            LATIME8_accumulator_LIST = []
            LAUNIT8_accumulator_LIST = []
            LADURA8_accumulator_LIST = []
            LADURB8_accumulator_LIST = []
            LACHRC8_accumulator_LIST = []
            LATIME9_accumulator_LIST = []
            LAUNIT9_accumulator_LIST = []
            LADURA9_accumulator_LIST = []
            LADURB9_accumulator_LIST = []
            LACHRC9_accumulator_LIST = []
            LATIME10_accumulator_LIST = []
            LAUNIT10_accumulator_LIST = []
            LADURA10_accumulator_LIST = []
            LADURB10_accumulator_LIST = []
            LACHRC10_accumulator_LIST = []
            LATIME11_accumulator_LIST = []
            LAUNIT11_accumulator_LIST = []
            LADURA11_accumulator_LIST = []
            LADURB11_accumulator_LIST = []
            LACHRC11_accumulator_LIST = []
            LATIME12_accumulator_LIST = []
            LAUNIT12_accumulator_LIST = []
            LADURA12_accumulator_LIST = []
            LADURB12_accumulator_LIST = []
            LACHRC12_accumulator_LIST = []
            LATIME13_accumulator_LIST = []
            LAUNIT13_accumulator_LIST = []
            LADURA13_accumulator_LIST = []
            LADURB13_accumulator_LIST = []
            LACHRC13_accumulator_LIST = []
            LTIME14A_accumulator_LIST = []
            LUNIT14A_accumulator_LIST = []
            LDURA14A_accumulator_LIST = []
            LDURB14A_accumulator_LIST = []
            LCHRC14A_accumulator_LIST = []
            LATIME15_accumulator_LIST = []
            LAUNIT15_accumulator_LIST = []
            LADURA15_accumulator_LIST = []
            LADURB15_accumulator_LIST = []
            LACHRC15_accumulator_LIST = []
            LATIME16_accumulator_LIST = []
            LAUNIT16_accumulator_LIST = []
            LADURA16_accumulator_LIST = []
            LADURB16_accumulator_LIST = []
            LACHRC16_accumulator_LIST = []
            LATIME17_accumulator_LIST = []
            LAUNIT17_accumulator_LIST = []
            LADURA17_accumulator_LIST = []
            LADURB17_accumulator_LIST = []
            LACHRC17_accumulator_LIST = []
            LATIME18_accumulator_LIST = []
            LAUNIT18_accumulator_LIST = []
            LADURA18_accumulator_LIST = []
            LADURB18_accumulator_LIST = []
            LACHRC18_accumulator_LIST = []
            LATIME19_accumulator_LIST = []
            LAUNIT19_accumulator_LIST = []
            LADURA19_accumulator_LIST = []
            LADURB19_accumulator_LIST = []
            LACHRC19_accumulator_LIST = []
            LATIME20_accumulator_LIST = []
            LAUNIT20_accumulator_LIST = []
            LADURA20_accumulator_LIST = []
            LADURB20_accumulator_LIST = []
            LACHRC20_accumulator_LIST = []
            LATIME21_accumulator_LIST = []
            LAUNIT21_accumulator_LIST = []
            LADURA21_accumulator_LIST = []
            LADURB21_accumulator_LIST = []
            LACHRC21_accumulator_LIST = []
            LATIME22_accumulator_LIST = []
            LAUNIT22_accumulator_LIST = []
            LADURA22_accumulator_LIST = []
            LADURB22_accumulator_LIST = []
            LACHRC22_accumulator_LIST = []
            LATIME23_accumulator_LIST = []
            LAUNIT23_accumulator_LIST = []
            LADURA23_accumulator_LIST = []
            LADURB23_accumulator_LIST = []
            LACHRC23_accumulator_LIST = []
            LATIME24_accumulator_LIST = []
            LAUNIT24_accumulator_LIST = []
            LADURA24_accumulator_LIST = []
            LADURB24_accumulator_LIST = []
            LACHRC24_accumulator_LIST = []
            LATIME25_accumulator_LIST = []
            LAUNIT25_accumulator_LIST = []
            LADURA25_accumulator_LIST = []
            LADURB25_accumulator_LIST = []
            LACHRC25_accumulator_LIST = []
            LATIME26_accumulator_LIST = []
            LAUNIT26_accumulator_LIST = []
            LADURA26_accumulator_LIST = []
            LADURB26_accumulator_LIST = []
            LACHRC26_accumulator_LIST = []
            LATIME27_accumulator_LIST = []
            LAUNIT27_accumulator_LIST = []
            LADURA27_accumulator_LIST = []
            LADURB27_accumulator_LIST = []
            LACHRC27_accumulator_LIST = []
            LATIME28_accumulator_LIST = []
            LAUNIT28_accumulator_LIST = []
            LADURA28_accumulator_LIST = []
            LADURB28_accumulator_LIST = []
            LACHRC28_accumulator_LIST = []
            LATIME29_accumulator_LIST = []
            LAUNIT29_accumulator_LIST = []
            LADURA29_accumulator_LIST = []
            LADURB29_accumulator_LIST = []
            LACHRC29_accumulator_LIST = []
            LATIME30_accumulator_LIST = []
            LAUNIT30_accumulator_LIST = []
            LADURA30_accumulator_LIST = []
            LADURB30_accumulator_LIST = []
            LACHRC30_accumulator_LIST = []
            LATIME31_accumulator_LIST = []
            LAUNIT31_accumulator_LIST = []
            LADURA31_accumulator_LIST = []
            LADURB31_accumulator_LIST = []
            LACHRC31_accumulator_LIST = []
            LATIME32_accumulator_LIST = []
            LAUNIT32_accumulator_LIST = []
            LADURA32_accumulator_LIST = []
            LADURB32_accumulator_LIST = []
            LACHRC32_accumulator_LIST = []
            LATIME33_accumulator_LIST = []
            LAUNIT33_accumulator_LIST = []
            LADURA33_accumulator_LIST = []
            LADURB33_accumulator_LIST = []
            LACHRC33_accumulator_LIST = []
            LATIME34_accumulator_LIST = []
            LAUNIT34_accumulator_LIST = []
            LADURA34_accumulator_LIST = []
            LADURB34_accumulator_LIST = []
            LACHRC34_accumulator_LIST = []
            LATIME90_accumulator_LIST = []
            LAUNIT90_accumulator_LIST = []
            LADURA90_accumulator_LIST = []
            LADURB90_accumulator_LIST = []
            LACHRC90_accumulator_LIST = []
            LATIME91_accumulator_LIST = []
            LAUNIT91_accumulator_LIST = []
            LADURA91_accumulator_LIST = []
            LADURB91_accumulator_LIST = []
            LACHRC91_accumulator_LIST = []
            LCONDRT_accumulator_LIST = []
            LACHRONR_accumulator_LIST = []
            PHSTAT_accumulator_LIST = []
            PDMED12M_accumulator_LIST = []
            PNMED12M_accumulator_LIST = []
            PHOSPYR2_accumulator_LIST = []
            HOSPNO_accumulator_LIST = []
            HPNITE_accumulator_LIST = []
            PHCHM2W_accumulator_LIST = []
            PHCHMN2W_accumulator_LIST = []
            PHCPH2WR_accumulator_LIST = []
            PHCPHN2W_accumulator_LIST = []
            PHCDV2W_accumulator_LIST = []
            PHCDVN2W_accumulator_LIST = []
            P10DVYR_accumulator_LIST = []
            NOTCOV_accumulator_LIST = []
            MEDICARE_accumulator_LIST = []
            MCPART_accumulator_LIST = []
            MCCHOICE_accumulator_LIST = []
            MCHMO_accumulator_LIST = []
            MCADVR_accumulator_LIST = []
            MCPREM_accumulator_LIST = []
            MCREF_accumulator_LIST = []
            MCPARTD_accumulator_LIST = []
            MEDICAID_accumulator_LIST = []
            MAFLG_accumulator_LIST = []
            MACHMD_accumulator_LIST = []
            MXCHNG_accumulator_LIST = []
            MEDPREM_accumulator_LIST = []
            MDPRINC_accumulator_LIST = []
            MAPCMD_accumulator_LIST = []
            MAREF_accumulator_LIST = []
            SINGLE_accumulator_LIST = []
            SSTYPEA_accumulator_LIST = []
            SSTYPEB_accumulator_LIST = []
            SSTYPEC_accumulator_LIST = []
            SSTYPED_accumulator_LIST = []
            SSTYPEE_accumulator_LIST = []
            SSTYPEF_accumulator_LIST = []
            SSTYPEG_accumulator_LIST = []
            SSTYPEH_accumulator_LIST = []
            SSTYPEI_accumulator_LIST = []
            SSTYPEJ_accumulator_LIST = []
            SSTYPEK_accumulator_LIST = []
            SSTYPEL_accumulator_LIST = []
            PRIVATE_accumulator_LIST = []
            PRFLG_accumulator_LIST = []
            EXCHANGE_accumulator_LIST = []
            WHONAM1_accumulator_LIST = []
            PRPOLH1_accumulator_LIST = []
            PRCOOH1_accumulator_LIST = []
            PRCTOH1_accumulator_LIST = []
            PRRLOH11_accumulator_LIST = []
            PRRLOH21_accumulator_LIST = []
            PRRLOH31_accumulator_LIST = []
            PRRLOH41_accumulator_LIST = []
            PRCNUM1_accumulator_LIST = []
            COHU191_accumulator_LIST = []
            COH19251_accumulator_LIST = []
            COHO251_accumulator_LIST = []
            PLNWRKR1_accumulator_LIST = []
            PLNEXCH1_accumulator_LIST = []
            EXCHPR1_accumulator_LIST = []
            PLNPAY11_accumulator_LIST = []
            PLNPAY21_accumulator_LIST = []
            PLNPAY31_accumulator_LIST = []
            PLNPAY41_accumulator_LIST = []
            PLNPAY51_accumulator_LIST = []
            PLNPAY61_accumulator_LIST = []
            PLNPAY71_accumulator_LIST = []
            PLNPRE1_accumulator_LIST = []
            HICOSTR1_accumulator_LIST = []
            EMPPAY1_accumulator_LIST = []
            ECOSTR1_accumulator_LIST = []
            EMPCSTP1_accumulator_LIST = []
            PLNMGD1_accumulator_LIST = []
            HDHP1_accumulator_LIST = []
            HSAHRA1_accumulator_LIST = []
            MGCHMD1_accumulator_LIST = []
            MGPRMD1_accumulator_LIST = []
            MGPYMD1_accumulator_LIST = []
            MGPREF1_accumulator_LIST = []
            PCPREQ1_accumulator_LIST = []
            PRRXCOV1_accumulator_LIST = []
            PRDNCOV1_accumulator_LIST = []
            PXCHNG_accumulator_LIST = []
            PLEXCHPR_accumulator_LIST = []
            PSTRFPRM_accumulator_LIST = []
            PSSPRINC_accumulator_LIST = []
            PSTDOC_accumulator_LIST = []
            PSTCMD_accumulator_LIST = []
            PSTREF_accumulator_LIST = []
            WHONAM2_accumulator_LIST = []
            PRPOLH2_accumulator_LIST = []
            PRCOOH2_accumulator_LIST = []
            PRCTOH2_accumulator_LIST = []
            PRRLOH12_accumulator_LIST = []
            PRRLOH22_accumulator_LIST = []
            PRRLOH32_accumulator_LIST = []
            PRRLOH42_accumulator_LIST = []
            PRCNUM2_accumulator_LIST = []
            COHU192_accumulator_LIST = []
            COH19252_accumulator_LIST = []
            COHO252_accumulator_LIST = []
            PLNWRKR2_accumulator_LIST = []
            PLNEXCH2_accumulator_LIST = []
            EXCHPR2_accumulator_LIST = []
            PLNPAY12_accumulator_LIST = []
            PLNPAY22_accumulator_LIST = []
            PLNPAY32_accumulator_LIST = []
            PLNPAY42_accumulator_LIST = []
            PLNPAY52_accumulator_LIST = []
            PLNPAY62_accumulator_LIST = []
            PLNPAY72_accumulator_LIST = []
            PLNPRE2_accumulator_LIST = []
            HICOSTR2_accumulator_LIST = []
            EMPPAY2_accumulator_LIST = []
            ECOSTR2_accumulator_LIST = []
            EMPCSTP2_accumulator_LIST = []
            PLNMGD2_accumulator_LIST = []
            HDHP2_accumulator_LIST = []
            HSAHRA2_accumulator_LIST = []
            MGCHMD2_accumulator_LIST = []
            MGPRMD2_accumulator_LIST = []
            MGPYMD2_accumulator_LIST = []
            MGPREF2_accumulator_LIST = []
            PCPREQ2_accumulator_LIST = []
            PRRXCOV2_accumulator_LIST = []
            PRDNCOV2_accumulator_LIST = []
            PRPLPLUS_accumulator_LIST = []
            FCOVCONF_accumulator_LIST = []
            SCHIP_accumulator_LIST = []
            CHFLG_accumulator_LIST = []
            CHXCHNG_accumulator_LIST = []
            STRFPRM1_accumulator_LIST = []
            CHPRINC_accumulator_LIST = []
            STDOC1_accumulator_LIST = []
            STPCMD1_accumulator_LIST = []
            STREF1_accumulator_LIST = []
            OTHPUB_accumulator_LIST = []
            OPFLG_accumulator_LIST = []
            OPXCHNG_accumulator_LIST = []
            PLEXCHOP_accumulator_LIST = []
            STRFPRM2_accumulator_LIST = []
            SSPRINC_accumulator_LIST = []
            STDOC2_accumulator_LIST = []
            STPCMD2_accumulator_LIST = []
            STREF2_accumulator_LIST = []
            OTHGOV_accumulator_LIST = []
            OGFLG_accumulator_LIST = []
            OGXCHNG_accumulator_LIST = []
            PLEXCHOG_accumulator_LIST = []
            STRFPRM3_accumulator_LIST = []
            OGPRINC_accumulator_LIST = []
            STDOC3_accumulator_LIST = []
            STPCMD3_accumulator_LIST = []
            STREF3_accumulator_LIST = []
            MILCARE_accumulator_LIST = []
            MILSPC1_accumulator_LIST = []
            MILSPC2_accumulator_LIST = []
            MILSPC3_accumulator_LIST = []
            MILSPC4_accumulator_LIST = []
            MILMAN_accumulator_LIST = []
            IHS_accumulator_LIST = []
            HILAST_accumulator_LIST = []
            HISTOP1_accumulator_LIST = []
            HISTOP2_accumulator_LIST = []
            HISTOP3_accumulator_LIST = []
            HISTOP4_accumulator_LIST = []
            HISTOP5_accumulator_LIST = []
            HISTOP6_accumulator_LIST = []
            HISTOP7_accumulator_LIST = []
            HISTOP8_accumulator_LIST = []
            HISTOP9_accumulator_LIST = []
            HISTOP10_accumulator_LIST = []
            HISTOP11_accumulator_LIST = []
            HISTOP12_accumulator_LIST = []
            HISTOP13_accumulator_LIST = []
            HISTOP14_accumulator_LIST = []
            HISTOP15_accumulator_LIST = []
            HINOTYR_accumulator_LIST = []
            HINOTMYR_accumulator_LIST = []
            FHICHNG_accumulator_LIST = []
            FHIKDBA_accumulator_LIST = []
            FHIKDBB_accumulator_LIST = []
            FHIKDBC_accumulator_LIST = []
            FHIKDBD_accumulator_LIST = []
            FHIKDBE_accumulator_LIST = []
            FHIKDBF_accumulator_LIST = []
            FHIKDBG_accumulator_LIST = []
            FHIKDBH_accumulator_LIST = []
            FHIKDBI_accumulator_LIST = []
            FHIKDBJ_accumulator_LIST = []
            FHIKDBK_accumulator_LIST = []
            PWRKBR1_accumulator_LIST = []
            HCSPFYR_accumulator_LIST = []
            MEDBILL_accumulator_LIST = []
            MEDBPAY_accumulator_LIST = []
            MEDBNOP_accumulator_LIST = []
            FSA_accumulator_LIST = []
            HIKINDNA_accumulator_LIST = []
            HIKINDNB_accumulator_LIST = []
            HIKINDNC_accumulator_LIST = []
            HIKINDND_accumulator_LIST = []
            HIKINDNE_accumulator_LIST = []
            HIKINDNF_accumulator_LIST = []
            HIKINDNG_accumulator_LIST = []
            HIKINDNH_accumulator_LIST = []
            HIKINDNI_accumulator_LIST = []
            HIKINDNJ_accumulator_LIST = []
            HIKINDNK_accumulator_LIST = []
            MCAREPRB_accumulator_LIST = []
            MCAIDPRB_accumulator_LIST = []
            SINCOV_accumulator_LIST = []
            PLBORN_accumulator_LIST = []
            REGIONBR_accumulator_LIST = []
            GEOBRTH_accumulator_LIST = []
            YRSINUS_accumulator_LIST = []
            CITIZENP_accumulator_LIST = []
            HEADST_accumulator_LIST = []
            HEADSTV1_accumulator_LIST = []
            EDUC1_accumulator_LIST = []
            ARMFVER_accumulator_LIST = []
            ARMFEV_accumulator_LIST = []
            ARMFFC_accumulator_LIST = []
            ARMFTM1P_accumulator_LIST = []
            ARMFTM2P_accumulator_LIST = []
            ARMFTM3P_accumulator_LIST = []
            ARMFTM4P_accumulator_LIST = []
            ARMFTM5P_accumulator_LIST = []
            ARMFTM6P_accumulator_LIST = []
            ARMFTM7P_accumulator_LIST = []
            ARMFDS2P_accumulator_LIST = []
            DOINGLWP_accumulator_LIST = []
            WHYNOWKP_accumulator_LIST = []
            WRKHRS2_accumulator_LIST = []
            WRKFTALL_accumulator_LIST = []
            WRKLYR1_accumulator_LIST = []
            WRKMYR_accumulator_LIST = []
            ERNYR_P_accumulator_LIST = []
            HIEMPOF_accumulator_LIST = []
            FINCINT_accumulator_LIST = []
            PSAL_accumulator_LIST = []
            PSEINC_accumulator_LIST = []
            PSSRR_accumulator_LIST = []
            PSSRRDB_accumulator_LIST = []
            PSSRRD_accumulator_LIST = []
            PPENS_accumulator_LIST = []
            POPENS_accumulator_LIST = []
            PSSI_accumulator_LIST = []
            PSSID_accumulator_LIST = []
            PTANF_accumulator_LIST = []
            POWBEN_accumulator_LIST = []
            PINTRSTR_accumulator_LIST = []
            PDIVD_accumulator_LIST = []
            PCHLDSP_accumulator_LIST = []
            PINCOT_accumulator_LIST = []
            PSSAPL_accumulator_LIST = []
            PSDAPL_accumulator_LIST = []
            TANFMYR_accumulator_LIST = []
            ELIGPWIC_accumulator_LIST = []
            PWIC_accumulator_LIST = []
            WIC_FLAG_accumulator_LIST = []
            ENGLANG_accumulator_LIST = []

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
                    WTIA_accumulator_LIST.append(char)
                    WTIA = ''.join(WTIA_accumulator_LIST)
                elif 24 < cdx < 31:
                    WTFA_accumulator_LIST.append(char)
                    WTFA = ''.join(WTFA_accumulator_LIST)
                elif 30 < cdx < 32:
                    REGION_accumulator_LIST.append(char)
                    REGION = ''.join(REGION_accumulator_LIST)
                elif 31 < cdx < 35:
                    STRAT_P_accumulator_LIST.append(char)
                    STRAT_P = ''.join(STRAT_P_accumulator_LIST)
                elif 34 < cdx < 37:
                    PSU_P_accumulator_LIST.append(char)
                    PSU_P = ''.join(PSU_P_accumulator_LIST)
                elif 36 < cdx < 38:
                    SEX_accumulator_LIST.append(char)
                    SEX = ''.join(SEX_accumulator_LIST)
                elif 37 < cdx < 39:
                    ORIGIN_I_accumulator_LIST.append(char)
                    ORIGIN_I = ''.join(ORIGIN_I_accumulator_LIST)
                elif 38 < cdx < 40:
                    ORIGIMPT_accumulator_LIST.append(char)
                    ORIGIMPT = ''.join(ORIGIMPT_accumulator_LIST)
                elif 39 < cdx < 42:
                    HISPAN_I_accumulator_LIST.append(char)
                    HISPAN_I = ''.join(HISPAN_I_accumulator_LIST)
                elif 41 < cdx < 43:
                    HISPIMPT_accumulator_LIST.append(char)
                    HISPIMPT = ''.join(HISPIMPT_accumulator_LIST)
                elif 42 < cdx < 45:
                    RACERPI2_accumulator_LIST.append(char)
                    RACERPI2 = ''.join(RACERPI2_accumulator_LIST)
                elif 44 < cdx < 46:
                    RACEIMP2_accumulator_LIST.append(char)
                    RACEIMP2 = ''.join(RACEIMP2_accumulator_LIST)
                elif 45 < cdx < 48:
                    MRACRPI2_accumulator_LIST.append(char)
                    MRACRPI2 = ''.join(MRACRPI2_accumulator_LIST)
                elif 47 < cdx < 50:
                    MRACBPI2_accumulator_LIST.append(char)
                    MRACBPI2 = ''.join(MRACBPI2_accumulator_LIST)
                elif 49 < cdx < 51:
                    RACRECI3_accumulator_LIST.append(char)
                    RACRECI3 = ''.join(RACRECI3_accumulator_LIST)
                elif 50 < cdx < 52:
                    HISCODI3_accumulator_LIST.append(char)
                    HISCODI3 = ''.join(HISCODI3_accumulator_LIST)
                elif 51 < cdx < 53:
                    ERIMPFLG_accumulator_LIST.append(char)
                    ERIMPFLG = ''.join(ERIMPFLG_accumulator_LIST)
                elif 52 < cdx < 54:
                    NOWAF_accumulator_LIST.append(char)
                    NOWAF = ''.join(NOWAF_accumulator_LIST)
                elif 53 < cdx < 56:
                    RRP_accumulator_LIST.append(char)
                    RRP = ''.join(RRP_accumulator_LIST)
                elif 55 < cdx < 57:
                    HHREFLG_accumulator_LIST.append(char)
                    HHREFLG = ''.join(HHREFLG_accumulator_LIST)
                elif 56 < cdx < 59:
                    FRRP_accumulator_LIST.append(char)
                    FRRP = ''.join(FRRP_accumulator_LIST)
                elif 58 < cdx < 61:
                    DOB_M_accumulator_LIST.append(char)
                    DOB_M = ''.join(DOB_M_accumulator_LIST)
                elif 60 < cdx < 65:
                    DOB_Y_P_accumulator_LIST.append(char)
                    DOB_Y_P = ''.join(DOB_Y_P_accumulator_LIST)
                elif 64 < cdx < 67:
                    AGE_P_accumulator_LIST.append(char)
                    AGE_P = ''.join(AGE_P_accumulator_LIST)
                elif 66 < cdx < 68:
                    AGE_CHG_accumulator_LIST.append(char)
                    AGE_CHG = ''.join(AGE_CHG_accumulator_LIST)
                elif 67 < cdx < 69:
                    FMRPFLG_accumulator_LIST.append(char)
                    FMRPFLG = ''.join(FMRPFLG_accumulator_LIST)
                elif 68 < cdx < 70:
                    FMREFLG_accumulator_LIST.append(char)
                    FMREFLG = ''.join(FMREFLG_accumulator_LIST)
                elif 69 < cdx < 71:
                    R_MARITL_accumulator_LIST.append(char)
                    R_MARITL = ''.join(R_MARITL_accumulator_LIST)
                elif 70 < cdx < 73:
                    FSPOUS2_accumulator_LIST.append(char)
                    FSPOUS2 = ''.join(FSPOUS2_accumulator_LIST)
                elif 72 < cdx < 74:
                    COHAB1_accumulator_LIST.append(char)
                    COHAB1 = ''.join(COHAB1_accumulator_LIST)
                elif 73 < cdx < 75:
                    COHAB2_accumulator_LIST.append(char)
                    COHAB2 = ''.join(COHAB2_accumulator_LIST)
                elif 74 < cdx < 77:
                    FCOHAB3_accumulator_LIST.append(char)
                    FCOHAB3 = ''.join(FCOHAB3_accumulator_LIST)
                elif 76 < cdx < 78:
                    CDCMSTAT_accumulator_LIST.append(char)
                    CDCMSTAT = ''.join(CDCMSTAT_accumulator_LIST)
                elif 77 < cdx < 79:
                    SIB_DEGP_accumulator_LIST.append(char)
                    SIB_DEGP = ''.join(SIB_DEGP_accumulator_LIST)
                elif 78 < cdx < 81:
                    FMOTHER1_accumulator_LIST.append(char)
                    FMOTHER1 = ''.join(FMOTHER1_accumulator_LIST)
                elif 80 < cdx < 82:
                    MOM_DEGP_accumulator_LIST.append(char)
                    MOM_DEGP = ''.join(MOM_DEGP_accumulator_LIST)
                elif 81 < cdx < 84:
                    FFATHER1_accumulator_LIST.append(char)
                    FFATHER1 = ''.join(FFATHER1_accumulator_LIST)
                elif 83 < cdx < 85:
                    DAD_DEGP_accumulator_LIST.append(char)
                    DAD_DEGP = ''.join(DAD_DEGP_accumulator_LIST)
                elif 84 < cdx < 86:
                    PARENTS_accumulator_LIST.append(char)
                    PARENTS = ''.join(PARENTS_accumulator_LIST)
                elif 85 < cdx < 88:
                    MOM_ED_accumulator_LIST.append(char)
                    MOM_ED = ''.join(MOM_ED_accumulator_LIST)
                elif 87 < cdx < 90:
                    DAD_ED_accumulator_LIST.append(char)
                    DAD_ED = ''.join(DAD_ED_accumulator_LIST)
                elif 89 < cdx < 91:
                    ASTATFLG_accumulator_LIST.append(char)
                    ASTATFLG = ''.join(ASTATFLG_accumulator_LIST)
                elif 90 < cdx < 92:
                    CSTATFLG_accumulator_LIST.append(char)
                    CSTATFLG = ''.join(CSTATFLG_accumulator_LIST)
                elif 91 < cdx < 93:
                    QCADULT_accumulator_LIST.append(char)
                    QCADULT = ''.join(QCADULT_accumulator_LIST)
                elif 92 < cdx < 94:
                    QCCHILD_accumulator_LIST.append(char)
                    QCCHILD = ''.join(QCCHILD_accumulator_LIST)
                elif 93 < cdx < 95:
                    FDRN_FLG_accumulator_LIST.append(char)
                    FDRN_FLG = ''.join(FDRN_FLG_accumulator_LIST)
                elif 94 < cdx < 96:
                    PLAPLYLM_accumulator_LIST.append(char)
                    PLAPLYLM = ''.join(PLAPLYLM_accumulator_LIST)
                elif 95 < cdx < 97:
                    PLAPLYUN_accumulator_LIST.append(char)
                    PLAPLYUN = ''.join(PLAPLYUN_accumulator_LIST)
                elif 96 < cdx < 98:
                    PSPEDEIS_accumulator_LIST.append(char)
                    PSPEDEIS = ''.join(PSPEDEIS_accumulator_LIST)
                elif 97 < cdx < 99:
                    PSPEDEM_accumulator_LIST.append(char)
                    PSPEDEM = ''.join(PSPEDEM_accumulator_LIST)
                elif 98 < cdx < 100:
                    PLAADL_accumulator_LIST.append(char)
                    PLAADL = ''.join(PLAADL_accumulator_LIST)
                elif 99 < cdx < 101:
                    LABATH_accumulator_LIST.append(char)
                    LABATH = ''.join(LABATH_accumulator_LIST)
                elif 100 < cdx < 102:
                    LADRESS_accumulator_LIST.append(char)
                    LADRESS = ''.join(LADRESS_accumulator_LIST)
                elif 101 < cdx < 103:
                    LAEAT_accumulator_LIST.append(char)
                    LAEAT = ''.join(LAEAT_accumulator_LIST)
                elif 102 < cdx < 104:
                    LABED_accumulator_LIST.append(char)
                    LABED = ''.join(LABED_accumulator_LIST)
                elif 103 < cdx < 105:
                    LATOILT_accumulator_LIST.append(char)
                    LATOILT = ''.join(LATOILT_accumulator_LIST)
                elif 104 < cdx < 106:
                    LAHOME_accumulator_LIST.append(char)
                    LAHOME = ''.join(LAHOME_accumulator_LIST)
                elif 105 < cdx < 107:
                    PLAIADL_accumulator_LIST.append(char)
                    PLAIADL = ''.join(PLAIADL_accumulator_LIST)
                elif 106 < cdx < 108:
                    PLAWKNOW_accumulator_LIST.append(char)
                    PLAWKNOW = ''.join(PLAWKNOW_accumulator_LIST)
                elif 107 < cdx < 109:
                    PLAWKLIM_accumulator_LIST.append(char)
                    PLAWKLIM = ''.join(PLAWKLIM_accumulator_LIST)
                elif 108 < cdx < 110:
                    PLAWALK_accumulator_LIST.append(char)
                    PLAWALK = ''.join(PLAWALK_accumulator_LIST)
                elif 109 < cdx < 111:
                    PLAREMEM_accumulator_LIST.append(char)
                    PLAREMEM = ''.join(PLAREMEM_accumulator_LIST)
                elif 110 < cdx < 112:
                    PLIMANY_accumulator_LIST.append(char)
                    PLIMANY = ''.join(PLIMANY_accumulator_LIST)
                elif 111 < cdx < 113:
                    LA1AR_accumulator_LIST.append(char)
                    LA1AR = ''.join(LA1AR_accumulator_LIST)
                elif 112 < cdx < 114:
                    LAHCC1_accumulator_LIST.append(char)
                    LAHCC1 = ''.join(LAHCC1_accumulator_LIST)
                elif 113 < cdx < 115:
                    LAHCC2_accumulator_LIST.append(char)
                    LAHCC2 = ''.join(LAHCC2_accumulator_LIST)
                elif 114 < cdx < 116:
                    LAHCC3_accumulator_LIST.append(char)
                    LAHCC3 = ''.join(LAHCC3_accumulator_LIST)
                elif 115 < cdx < 117:
                    LAHCC4_accumulator_LIST.append(char)
                    LAHCC4 = ''.join(LAHCC4_accumulator_LIST)
                elif 116 < cdx < 118:
                    LAHCC5_accumulator_LIST.append(char)
                    LAHCC5 = ''.join(LAHCC5_accumulator_LIST)
                elif 117 < cdx < 119:
                    LAHCC6_accumulator_LIST.append(char)
                    LAHCC6 = ''.join(LAHCC6_accumulator_LIST)
                elif 118 < cdx < 120:
                    LAHCC7A_accumulator_LIST.append(char)
                    LAHCC7A = ''.join(LAHCC7A_accumulator_LIST)
                elif 119 < cdx < 121:
                    LAHCC8_accumulator_LIST.append(char)
                    LAHCC8 = ''.join(LAHCC8_accumulator_LIST)
                elif 120 < cdx < 122:
                    LAHCC9_accumulator_LIST.append(char)
                    LAHCC9 = ''.join(LAHCC9_accumulator_LIST)
                elif 121 < cdx < 123:
                    LAHCC10_accumulator_LIST.append(char)
                    LAHCC10 = ''.join(LAHCC10_accumulator_LIST)
                elif 122 < cdx < 124:
                    LAHCC11_accumulator_LIST.append(char)
                    LAHCC11 = ''.join(LAHCC11_accumulator_LIST)
                elif 123 < cdx < 125:
                    LAHCC12_accumulator_LIST.append(char)
                    LAHCC12 = ''.join(LAHCC12_accumulator_LIST)
                elif 124 < cdx < 126:
                    LAHCC13_accumulator_LIST.append(char)
                    LAHCC13 = ''.join(LAHCC13_accumulator_LIST)
                elif 125 < cdx < 127:
                    LAHCC90_accumulator_LIST.append(char)
                    LAHCC90 = ''.join(LAHCC90_accumulator_LIST)
                elif 126 < cdx < 128:
                    LAHCC91_accumulator_LIST.append(char)
                    LAHCC91 = ''.join(LAHCC91_accumulator_LIST)
                elif 127 < cdx < 130:
                    LCTIME1_accumulator_LIST.append(char)
                    LCTIME1 = ''.join(LCTIME1_accumulator_LIST)
                elif 129 < cdx < 131:
                    LCUNIT1_accumulator_LIST.append(char)
                    LCUNIT1 = ''.join(LCUNIT1_accumulator_LIST)
                elif 130 < cdx < 133:
                    LCDURA1_accumulator_LIST.append(char)
                    LCDURA1 = ''.join(LCDURA1_accumulator_LIST)
                elif 132 < cdx < 134:
                    LCDURB1_accumulator_LIST.append(char)
                    LCDURB1 = ''.join(LCDURB1_accumulator_LIST)
                elif 133 < cdx < 135:
                    LCCHRC1_accumulator_LIST.append(char)
                    LCCHRC1 = ''.join(LCCHRC1_accumulator_LIST)
                elif 134 < cdx < 137:
                    LCTIME2_accumulator_LIST.append(char)
                    LCTIME2 = ''.join(LCTIME2_accumulator_LIST)
                elif 136 < cdx < 138:
                    LCUNIT2_accumulator_LIST.append(char)
                    LCUNIT2 = ''.join(LCUNIT2_accumulator_LIST)
                elif 137 < cdx < 140:
                    LCDURA2_accumulator_LIST.append(char)
                    LCDURA2 = ''.join(LCDURA2_accumulator_LIST)
                elif 139 < cdx < 141:
                    LCDURB2_accumulator_LIST.append(char)
                    LCDURB2 = ''.join(LCDURB2_accumulator_LIST)
                elif 140 < cdx < 142:
                    LCCHRC2_accumulator_LIST.append(char)
                    LCCHRC2 = ''.join(LCCHRC2_accumulator_LIST)
                elif 141 < cdx < 144:
                    LCTIME3_accumulator_LIST.append(char)
                    LCTIME3 = ''.join(LCTIME3_accumulator_LIST)
                elif 143 < cdx < 145:
                    LCUNIT3_accumulator_LIST.append(char)
                    LCUNIT3 = ''.join(LCUNIT3_accumulator_LIST)
                elif 144 < cdx < 147:
                    LCDURA3_accumulator_LIST.append(char)
                    LCDURA3 = ''.join(LCDURA3_accumulator_LIST)
                elif 146 < cdx < 148:
                    LCDURB3_accumulator_LIST.append(char)
                    LCDURB3 = ''.join(LCDURB3_accumulator_LIST)
                elif 147 < cdx < 149:
                    LCCHRC3_accumulator_LIST.append(char)
                    LCCHRC3 = ''.join(LCCHRC3_accumulator_LIST)
                elif 148 < cdx < 151:
                    LCTIME4_accumulator_LIST.append(char)
                    LCTIME4 = ''.join(LCTIME4_accumulator_LIST)
                elif 150 < cdx < 152:
                    LCUNIT4_accumulator_LIST.append(char)
                    LCUNIT4 = ''.join(LCUNIT4_accumulator_LIST)
                elif 151 < cdx < 154:
                    LCDURA4_accumulator_LIST.append(char)
                    LCDURA4 = ''.join(LCDURA4_accumulator_LIST)
                elif 153 < cdx < 155:
                    LCDURB4_accumulator_LIST.append(char)
                    LCDURB4 = ''.join(LCDURB4_accumulator_LIST)
                elif 154 < cdx < 156:
                    LCCHRC4_accumulator_LIST.append(char)
                    LCCHRC4 = ''.join(LCCHRC4_accumulator_LIST)
                elif 155 < cdx < 158:
                    LCTIME5_accumulator_LIST.append(char)
                    LCTIME5 = ''.join(LCTIME5_accumulator_LIST)
                elif 157 < cdx < 159:
                    LCUNIT5_accumulator_LIST.append(char)
                    LCUNIT5 = ''.join(LCUNIT5_accumulator_LIST)
                elif 158 < cdx < 161:
                    LCDURA5_accumulator_LIST.append(char)
                    LCDURA5 = ''.join(LCDURA5_accumulator_LIST)
                elif 160 < cdx < 162:
                    LCDURB5_accumulator_LIST.append(char)
                    LCDURB5 = ''.join(LCDURB5_accumulator_LIST)
                elif 161 < cdx < 163:
                    LCCHRC5_accumulator_LIST.append(char)
                    LCCHRC5 = ''.join(LCCHRC5_accumulator_LIST)
                elif 162 < cdx < 165:
                    LCTIME6_accumulator_LIST.append(char)
                    LCTIME6 = ''.join(LCTIME6_accumulator_LIST)
                elif 164 < cdx < 166:
                    LCUNIT6_accumulator_LIST.append(char)
                    LCUNIT6 = ''.join(LCUNIT6_accumulator_LIST)
                elif 165 < cdx < 168:
                    LCDURA6_accumulator_LIST.append(char)
                    LCDURA6 = ''.join(LCDURA6_accumulator_LIST)
                elif 167 < cdx < 169:
                    LCDURB6_accumulator_LIST.append(char)
                    LCDURB6 = ''.join(LCDURB6_accumulator_LIST)
                elif 168 < cdx < 170:
                    LCCHRC6_accumulator_LIST.append(char)
                    LCCHRC6 = ''.join(LCCHRC6_accumulator_LIST)
                elif 169 < cdx < 172:
                    LCTIME7A_accumulator_LIST.append(char)
                    LCTIME7A = ''.join(LCTIME7A_accumulator_LIST)
                elif 171 < cdx < 173:
                    LCUNIT7A_accumulator_LIST.append(char)
                    LCUNIT7A = ''.join(LCUNIT7A_accumulator_LIST)
                elif 172 < cdx < 175:
                    LCDURA7A_accumulator_LIST.append(char)
                    LCDURA7A = ''.join(LCDURA7A_accumulator_LIST)
                elif 174 < cdx < 176:
                    LCDURB7A_accumulator_LIST.append(char)
                    LCDURB7A = ''.join(LCDURB7A_accumulator_LIST)
                elif 175 < cdx < 177:
                    LCCHRC7A_accumulator_LIST.append(char)
                    LCCHRC7A = ''.join(LCCHRC7A_accumulator_LIST)
                elif 176 < cdx < 179:
                    LCTIME8_accumulator_LIST.append(char)
                    LCTIME8 = ''.join(LCTIME8_accumulator_LIST)
                elif 178 < cdx < 180:
                    LCUNIT8_accumulator_LIST.append(char)
                    LCUNIT8 = ''.join(LCUNIT8_accumulator_LIST)
                elif 179 < cdx < 182:
                    LCDURA8_accumulator_LIST.append(char)
                    LCDURA8 = ''.join(LCDURA8_accumulator_LIST)
                elif 181 < cdx < 183:
                    LCDURB8_accumulator_LIST.append(char)
                    LCDURB8 = ''.join(LCDURB8_accumulator_LIST)
                elif 182 < cdx < 184:
                    LCCHRC8_accumulator_LIST.append(char)
                    LCCHRC8 = ''.join(LCCHRC8_accumulator_LIST)
                elif 183 < cdx < 186:
                    LCTIME9_accumulator_LIST.append(char)
                    LCTIME9 = ''.join(LCTIME9_accumulator_LIST)
                elif 185 < cdx < 187:
                    LCUNIT9_accumulator_LIST.append(char)
                    LCUNIT9 = ''.join(LCUNIT9_accumulator_LIST)
                elif 186 < cdx < 189:
                    LCDURA9_accumulator_LIST.append(char)
                    LCDURA9 = ''.join(LCDURA9_accumulator_LIST)
                elif 188 < cdx < 190:
                    LCDURB9_accumulator_LIST.append(char)
                    LCDURB9 = ''.join(LCDURB9_accumulator_LIST)
                elif 189 < cdx < 191:
                    LCCHRC9_accumulator_LIST.append(char)
                    LCCHRC9 = ''.join(LCCHRC9_accumulator_LIST)
                elif 190 < cdx < 193:
                    LCTIME10_accumulator_LIST.append(char)
                    LCTIME10 = ''.join(LCTIME10_accumulator_LIST)
                elif 192 < cdx < 194:
                    LCUNIT10_accumulator_LIST.append(char)
                    LCUNIT10 = ''.join(LCUNIT10_accumulator_LIST)
                elif 193 < cdx < 196:
                    LCDURA10_accumulator_LIST.append(char)
                    LCDURA10 = ''.join(LCDURA10_accumulator_LIST)
                elif 195 < cdx < 197:
                    LCDURB10_accumulator_LIST.append(char)
                    LCDURB10 = ''.join(LCDURB10_accumulator_LIST)
                elif 196 < cdx < 198:
                    LCCHRC10_accumulator_LIST.append(char)
                    LCCHRC10 = ''.join(LCCHRC10_accumulator_LIST)
                elif 197 < cdx < 200:
                    LCTIME11_accumulator_LIST.append(char)
                    LCTIME11 = ''.join(LCTIME11_accumulator_LIST)
                elif 199 < cdx < 201:
                    LCUNIT11_accumulator_LIST.append(char)
                    LCUNIT11 = ''.join(LCUNIT11_accumulator_LIST)
                elif 200 < cdx < 203:
                    LCDURA11_accumulator_LIST.append(char)
                    LCDURA11 = ''.join(LCDURA11_accumulator_LIST)
                elif 202 < cdx < 204:
                    LCDURB11_accumulator_LIST.append(char)
                    LCDURB11 = ''.join(LCDURB11_accumulator_LIST)
                elif 203 < cdx < 205:
                    LCCHRC11_accumulator_LIST.append(char)
                    LCCHRC11 = ''.join(LCCHRC11_accumulator_LIST)
                elif 204 < cdx < 207:
                    LCTIME12_accumulator_LIST.append(char)
                    LCTIME12 = ''.join(LCTIME12_accumulator_LIST)
                elif 206 < cdx < 208:
                    LCUNIT12_accumulator_LIST.append(char)
                    LCUNIT12 = ''.join(LCUNIT12_accumulator_LIST)
                elif 207 < cdx < 210:
                    LCDURA12_accumulator_LIST.append(char)
                    LCDURA12 = ''.join(LCDURA12_accumulator_LIST)
                elif 209 < cdx < 211:
                    LCDURB12_accumulator_LIST.append(char)
                    LCDURB12 = ''.join(LCDURB12_accumulator_LIST)
                elif 210 < cdx < 212:
                    LCCHRC12_accumulator_LIST.append(char)
                    LCCHRC12 = ''.join(LCCHRC12_accumulator_LIST)
                elif 211 < cdx < 214:
                    LCTIME13_accumulator_LIST.append(char)
                    LCTIME13 = ''.join(LCTIME13_accumulator_LIST)
                elif 213 < cdx < 215:
                    LCUNIT13_accumulator_LIST.append(char)
                    LCUNIT13 = ''.join(LCUNIT13_accumulator_LIST)
                elif 214 < cdx < 217:
                    LCDURA13_accumulator_LIST.append(char)
                    LCDURA13 = ''.join(LCDURA13_accumulator_LIST)
                elif 216 < cdx < 218:
                    LCDURB13_accumulator_LIST.append(char)
                    LCDURB13 = ''.join(LCDURB13_accumulator_LIST)
                elif 217 < cdx < 219:
                    LCCHRC13_accumulator_LIST.append(char)
                    LCCHRC13 = ''.join(LCCHRC13_accumulator_LIST)
                elif 218 < cdx < 221:
                    LCTIME90_accumulator_LIST.append(char)
                    LCTIME90 = ''.join(LCTIME90_accumulator_LIST)
                elif 220 < cdx < 222:
                    LCUNIT90_accumulator_LIST.append(char)
                    LCUNIT90 = ''.join(LCUNIT90_accumulator_LIST)
                elif 221 < cdx < 224:
                    LCDURA90_accumulator_LIST.append(char)
                    LCDURA90 = ''.join(LCDURA90_accumulator_LIST)
                elif 223 < cdx < 225:
                    LCDURB90_accumulator_LIST.append(char)
                    LCDURB90 = ''.join(LCDURB90_accumulator_LIST)
                elif 224 < cdx < 226:
                    LCCHRC90_accumulator_LIST.append(char)
                    LCCHRC90 = ''.join(LCCHRC90_accumulator_LIST)
                elif 225 < cdx < 228:
                    LCTIME91_accumulator_LIST.append(char)
                    LCTIME91 = ''.join(LCTIME91_accumulator_LIST)
                elif 227 < cdx < 229:
                    LCUNIT91_accumulator_LIST.append(char)
                    LCUNIT91 = ''.join(LCUNIT91_accumulator_LIST)
                elif 228 < cdx < 231:
                    LCDURA91_accumulator_LIST.append(char)
                    LCDURA91 = ''.join(LCDURA91_accumulator_LIST)
                elif 230 < cdx < 232:
                    LCDURB91_accumulator_LIST.append(char)
                    LCDURB91 = ''.join(LCDURB91_accumulator_LIST)
                elif 231 < cdx < 233:
                    LCCHRC91_accumulator_LIST.append(char)
                    LCCHRC91 = ''.join(LCCHRC91_accumulator_LIST)
                elif 232 < cdx < 234:
                    LAHCA1_accumulator_LIST.append(char)
                    LAHCA1 = ''.join(LAHCA1_accumulator_LIST)
                elif 233 < cdx < 235:
                    LAHCA2_accumulator_LIST.append(char)
                    LAHCA2 = ''.join(LAHCA2_accumulator_LIST)
                elif 234 < cdx < 236:
                    LAHCA3_accumulator_LIST.append(char)
                    LAHCA3 = ''.join(LAHCA3_accumulator_LIST)
                elif 235 < cdx < 237:
                    LAHCA4_accumulator_LIST.append(char)
                    LAHCA4 = ''.join(LAHCA4_accumulator_LIST)
                elif 236 < cdx < 238:
                    LAHCA5_accumulator_LIST.append(char)
                    LAHCA5 = ''.join(LAHCA5_accumulator_LIST)
                elif 237 < cdx < 239:
                    LAHCA6_accumulator_LIST.append(char)
                    LAHCA6 = ''.join(LAHCA6_accumulator_LIST)
                elif 238 < cdx < 240:
                    LAHCA7_accumulator_LIST.append(char)
                    LAHCA7 = ''.join(LAHCA7_accumulator_LIST)
                elif 239 < cdx < 241:
                    LAHCA8_accumulator_LIST.append(char)
                    LAHCA8 = ''.join(LAHCA8_accumulator_LIST)
                elif 240 < cdx < 242:
                    LAHCA9_accumulator_LIST.append(char)
                    LAHCA9 = ''.join(LAHCA9_accumulator_LIST)
                elif 241 < cdx < 243:
                    LAHCA10_accumulator_LIST.append(char)
                    LAHCA10 = ''.join(LAHCA10_accumulator_LIST)
                elif 242 < cdx < 244:
                    LAHCA11_accumulator_LIST.append(char)
                    LAHCA11 = ''.join(LAHCA11_accumulator_LIST)
                elif 243 < cdx < 245:
                    LAHCA12_accumulator_LIST.append(char)
                    LAHCA12 = ''.join(LAHCA12_accumulator_LIST)
                elif 244 < cdx < 246:
                    LAHCA13_accumulator_LIST.append(char)
                    LAHCA13 = ''.join(LAHCA13_accumulator_LIST)
                elif 245 < cdx < 247:
                    LAHCA14A_accumulator_LIST.append(char)
                    LAHCA14A = ''.join(LAHCA14A_accumulator_LIST)
                elif 246 < cdx < 248:
                    LAHCA15_accumulator_LIST.append(char)
                    LAHCA15 = ''.join(LAHCA15_accumulator_LIST)
                elif 247 < cdx < 249:
                    LAHCA16_accumulator_LIST.append(char)
                    LAHCA16 = ''.join(LAHCA16_accumulator_LIST)
                elif 248 < cdx < 250:
                    LAHCA17_accumulator_LIST.append(char)
                    LAHCA17 = ''.join(LAHCA17_accumulator_LIST)
                elif 249 < cdx < 251:
                    LAHCA18_accumulator_LIST.append(char)
                    LAHCA18 = ''.join(LAHCA18_accumulator_LIST)
                elif 250 < cdx < 252:
                    LAHCA19__accumulator_LIST.append(char)
                    LAHCA19_ = ''.join(LAHCA19__accumulator_LIST)
                elif 251 < cdx < 253:
                    LAHCA20__accumulator_LIST.append(char)
                    LAHCA20_ = ''.join(LAHCA20__accumulator_LIST)
                elif 252 < cdx < 254:
                    LAHCA21__accumulator_LIST.append(char)
                    LAHCA21_ = ''.join(LAHCA21__accumulator_LIST)
                elif 253 < cdx < 255:
                    LAHCA22__accumulator_LIST.append(char)
                    LAHCA22_ = ''.join(LAHCA22__accumulator_LIST)
                elif 254 < cdx < 256:
                    LAHCA23__accumulator_LIST.append(char)
                    LAHCA23_ = ''.join(LAHCA23__accumulator_LIST)
                elif 255 < cdx < 257:
                    LAHCA24__accumulator_LIST.append(char)
                    LAHCA24_ = ''.join(LAHCA24__accumulator_LIST)
                elif 256 < cdx < 258:
                    LAHCA25__accumulator_LIST.append(char)
                    LAHCA25_ = ''.join(LAHCA25__accumulator_LIST)
                elif 257 < cdx < 259:
                    LAHCA26__accumulator_LIST.append(char)
                    LAHCA26_ = ''.join(LAHCA26__accumulator_LIST)
                elif 258 < cdx < 260:
                    LAHCA27__accumulator_LIST.append(char)
                    LAHCA27_ = ''.join(LAHCA27__accumulator_LIST)
                elif 259 < cdx < 261:
                    LAHCA28__accumulator_LIST.append(char)
                    LAHCA28_ = ''.join(LAHCA28__accumulator_LIST)
                elif 260 < cdx < 262:
                    LAHCA29__accumulator_LIST.append(char)
                    LAHCA29_ = ''.join(LAHCA29__accumulator_LIST)
                elif 261 < cdx < 263:
                    LAHCA30__accumulator_LIST.append(char)
                    LAHCA30_ = ''.join(LAHCA30__accumulator_LIST)
                elif 262 < cdx < 264:
                    LAHCA31__accumulator_LIST.append(char)
                    LAHCA31_ = ''.join(LAHCA31__accumulator_LIST)
                elif 263 < cdx < 265:
                    LAHCA32__accumulator_LIST.append(char)
                    LAHCA32_ = ''.join(LAHCA32__accumulator_LIST)
                elif 264 < cdx < 266:
                    LAHCA33__accumulator_LIST.append(char)
                    LAHCA33_ = ''.join(LAHCA33__accumulator_LIST)
                elif 265 < cdx < 267:
                    LAHCA34__accumulator_LIST.append(char)
                    LAHCA34_ = ''.join(LAHCA34__accumulator_LIST)
                elif 266 < cdx < 268:
                    LAHCA90_accumulator_LIST.append(char)
                    LAHCA90 = ''.join(LAHCA90_accumulator_LIST)
                elif 267 < cdx < 269:
                    LAHCA91_accumulator_LIST.append(char)
                    LAHCA91 = ''.join(LAHCA91_accumulator_LIST)
                elif 268 < cdx < 271:
                    LATIME1_accumulator_LIST.append(char)
                    LATIME1 = ''.join(LATIME1_accumulator_LIST)
                elif 270 < cdx < 272:
                    LAUNIT1_accumulator_LIST.append(char)
                    LAUNIT1 = ''.join(LAUNIT1_accumulator_LIST)
                elif 271 < cdx < 274:
                    LADURA1_accumulator_LIST.append(char)
                    LADURA1 = ''.join(LADURA1_accumulator_LIST)
                elif 273 < cdx < 275:
                    LADURB1_accumulator_LIST.append(char)
                    LADURB1 = ''.join(LADURB1_accumulator_LIST)
                elif 274 < cdx < 276:
                    LACHRC1_accumulator_LIST.append(char)
                    LACHRC1 = ''.join(LACHRC1_accumulator_LIST)
                elif 275 < cdx < 278:
                    LATIME2_accumulator_LIST.append(char)
                    LATIME2 = ''.join(LATIME2_accumulator_LIST)
                elif 277 < cdx < 279:
                    LAUNIT2_accumulator_LIST.append(char)
                    LAUNIT2 = ''.join(LAUNIT2_accumulator_LIST)
                elif 278 < cdx < 281:
                    LADURA2_accumulator_LIST.append(char)
                    LADURA2 = ''.join(LADURA2_accumulator_LIST)
                elif 280 < cdx < 282:
                    LADURB2_accumulator_LIST.append(char)
                    LADURB2 = ''.join(LADURB2_accumulator_LIST)
                elif 281 < cdx < 283:
                    LACHRC2_accumulator_LIST.append(char)
                    LACHRC2 = ''.join(LACHRC2_accumulator_LIST)
                elif 282 < cdx < 285:
                    LATIME3_accumulator_LIST.append(char)
                    LATIME3 = ''.join(LATIME3_accumulator_LIST)
                elif 284 < cdx < 286:
                    LAUNIT3_accumulator_LIST.append(char)
                    LAUNIT3 = ''.join(LAUNIT3_accumulator_LIST)
                elif 285 < cdx < 288:
                    LADURA3_accumulator_LIST.append(char)
                    LADURA3 = ''.join(LADURA3_accumulator_LIST)
                elif 287 < cdx < 289:
                    LADURB3_accumulator_LIST.append(char)
                    LADURB3 = ''.join(LADURB3_accumulator_LIST)
                elif 288 < cdx < 290:
                    LACHRC3_accumulator_LIST.append(char)
                    LACHRC3 = ''.join(LACHRC3_accumulator_LIST)
                elif 289 < cdx < 292:
                    LATIME4_accumulator_LIST.append(char)
                    LATIME4 = ''.join(LATIME4_accumulator_LIST)
                elif 291 < cdx < 293:
                    LAUNIT4_accumulator_LIST.append(char)
                    LAUNIT4 = ''.join(LAUNIT4_accumulator_LIST)
                elif 292 < cdx < 295:
                    LADURA4_accumulator_LIST.append(char)
                    LADURA4 = ''.join(LADURA4_accumulator_LIST)
                elif 294 < cdx < 296:
                    LADURB4_accumulator_LIST.append(char)
                    LADURB4 = ''.join(LADURB4_accumulator_LIST)
                elif 295 < cdx < 297:
                    LACHRC4_accumulator_LIST.append(char)
                    LACHRC4 = ''.join(LACHRC4_accumulator_LIST)
                elif 296 < cdx < 299:
                    LATIME5_accumulator_LIST.append(char)
                    LATIME5 = ''.join(LATIME5_accumulator_LIST)
                elif 298 < cdx < 300:
                    LAUNIT5_accumulator_LIST.append(char)
                    LAUNIT5 = ''.join(LAUNIT5_accumulator_LIST)
                elif 299 < cdx < 302:
                    LADURA5_accumulator_LIST.append(char)
                    LADURA5 = ''.join(LADURA5_accumulator_LIST)
                elif 301 < cdx < 303:
                    LADURB5_accumulator_LIST.append(char)
                    LADURB5 = ''.join(LADURB5_accumulator_LIST)
                elif 302 < cdx < 304:
                    LACHRC5_accumulator_LIST.append(char)
                    LACHRC5 = ''.join(LACHRC5_accumulator_LIST)
                elif 303 < cdx < 306:
                    LATIME6_accumulator_LIST.append(char)
                    LATIME6 = ''.join(LATIME6_accumulator_LIST)
                elif 305 < cdx < 307:
                    LAUNIT6_accumulator_LIST.append(char)
                    LAUNIT6 = ''.join(LAUNIT6_accumulator_LIST)
                elif 306 < cdx < 309:
                    LADURA6_accumulator_LIST.append(char)
                    LADURA6 = ''.join(LADURA6_accumulator_LIST)
                elif 308 < cdx < 310:
                    LADURB6_accumulator_LIST.append(char)
                    LADURB6 = ''.join(LADURB6_accumulator_LIST)
                elif 309 < cdx < 311:
                    LACHRC6_accumulator_LIST.append(char)
                    LACHRC6 = ''.join(LACHRC6_accumulator_LIST)
                elif 310 < cdx < 313:
                    LATIME7_accumulator_LIST.append(char)
                    LATIME7 = ''.join(LATIME7_accumulator_LIST)
                elif 312 < cdx < 314:
                    LAUNIT7_accumulator_LIST.append(char)
                    LAUNIT7 = ''.join(LAUNIT7_accumulator_LIST)
                elif 313 < cdx < 316:
                    LADURA7_accumulator_LIST.append(char)
                    LADURA7 = ''.join(LADURA7_accumulator_LIST)
                elif 315 < cdx < 317:
                    LADURB7_accumulator_LIST.append(char)
                    LADURB7 = ''.join(LADURB7_accumulator_LIST)
                elif 316 < cdx < 318:
                    LACHRC7_accumulator_LIST.append(char)
                    LACHRC7 = ''.join(LACHRC7_accumulator_LIST)
                elif 317 < cdx < 320:
                    LATIME8_accumulator_LIST.append(char)
                    LATIME8 = ''.join(LATIME8_accumulator_LIST)
                elif 319 < cdx < 321:
                    LAUNIT8_accumulator_LIST.append(char)
                    LAUNIT8 = ''.join(LAUNIT8_accumulator_LIST)
                elif 320 < cdx < 323:
                    LADURA8_accumulator_LIST.append(char)
                    LADURA8 = ''.join(LADURA8_accumulator_LIST)
                elif 322 < cdx < 324:
                    LADURB8_accumulator_LIST.append(char)
                    LADURB8 = ''.join(LADURB8_accumulator_LIST)
                elif 323 < cdx < 325:
                    LACHRC8_accumulator_LIST.append(char)
                    LACHRC8 = ''.join(LACHRC8_accumulator_LIST)
                elif 324 < cdx < 327:
                    LATIME9_accumulator_LIST.append(char)
                    LATIME9 = ''.join(LATIME9_accumulator_LIST)
                elif 326 < cdx < 328:
                    LAUNIT9_accumulator_LIST.append(char)
                    LAUNIT9 = ''.join(LAUNIT9_accumulator_LIST)
                elif 327 < cdx < 330:
                    LADURA9_accumulator_LIST.append(char)
                    LADURA9 = ''.join(LADURA9_accumulator_LIST)
                elif 329 < cdx < 331:
                    LADURB9_accumulator_LIST.append(char)
                    LADURB9 = ''.join(LADURB9_accumulator_LIST)
                elif 330 < cdx < 332:
                    LACHRC9_accumulator_LIST.append(char)
                    LACHRC9 = ''.join(LACHRC9_accumulator_LIST)
                elif 331 < cdx < 334:
                    LATIME10_accumulator_LIST.append(char)
                    LATIME10 = ''.join(LATIME10_accumulator_LIST)
                elif 333 < cdx < 335:
                    LAUNIT10_accumulator_LIST.append(char)
                    LAUNIT10 = ''.join(LAUNIT10_accumulator_LIST)
                elif 334 < cdx < 337:
                    LADURA10_accumulator_LIST.append(char)
                    LADURA10 = ''.join(LADURA10_accumulator_LIST)
                elif 336 < cdx < 338:
                    LADURB10_accumulator_LIST.append(char)
                    LADURB10 = ''.join(LADURB10_accumulator_LIST)
                elif 337 < cdx < 339:
                    LACHRC10_accumulator_LIST.append(char)
                    LACHRC10 = ''.join(LACHRC10_accumulator_LIST)
                elif 338 < cdx < 341:
                    LATIME11_accumulator_LIST.append(char)
                    LATIME11 = ''.join(LATIME11_accumulator_LIST)
                elif 340 < cdx < 342:
                    LAUNIT11_accumulator_LIST.append(char)
                    LAUNIT11 = ''.join(LAUNIT11_accumulator_LIST)
                elif 341 < cdx < 344:
                    LADURA11_accumulator_LIST.append(char)
                    LADURA11 = ''.join(LADURA11_accumulator_LIST)
                elif 343 < cdx < 345:
                    LADURB11_accumulator_LIST.append(char)
                    LADURB11 = ''.join(LADURB11_accumulator_LIST)
                elif 344 < cdx < 346:
                    LACHRC11_accumulator_LIST.append(char)
                    LACHRC11 = ''.join(LACHRC11_accumulator_LIST)
                elif 345 < cdx < 348:
                    LATIME12_accumulator_LIST.append(char)
                    LATIME12 = ''.join(LATIME12_accumulator_LIST)
                elif 347 < cdx < 349:
                    LAUNIT12_accumulator_LIST.append(char)
                    LAUNIT12 = ''.join(LAUNIT12_accumulator_LIST)
                elif 348 < cdx < 351:
                    LADURA12_accumulator_LIST.append(char)
                    LADURA12 = ''.join(LADURA12_accumulator_LIST)
                elif 350 < cdx < 352:
                    LADURB12_accumulator_LIST.append(char)
                    LADURB12 = ''.join(LADURB12_accumulator_LIST)
                elif 351 < cdx < 353:
                    LACHRC12_accumulator_LIST.append(char)
                    LACHRC12 = ''.join(LACHRC12_accumulator_LIST)
                elif 352 < cdx < 355:
                    LATIME13_accumulator_LIST.append(char)
                    LATIME13 = ''.join(LATIME13_accumulator_LIST)
                elif 354 < cdx < 356:
                    LAUNIT13_accumulator_LIST.append(char)
                    LAUNIT13 = ''.join(LAUNIT13_accumulator_LIST)
                elif 355 < cdx < 358:
                    LADURA13_accumulator_LIST.append(char)
                    LADURA13 = ''.join(LADURA13_accumulator_LIST)
                elif 357 < cdx < 359:
                    LADURB13_accumulator_LIST.append(char)
                    LADURB13 = ''.join(LADURB13_accumulator_LIST)
                elif 358 < cdx < 360:
                    LACHRC13_accumulator_LIST.append(char)
                    LACHRC13 = ''.join(LACHRC13_accumulator_LIST)
                elif 359 < cdx < 362:
                    LTIME14A_accumulator_LIST.append(char)
                    LTIME14A = ''.join(LTIME14A_accumulator_LIST)
                elif 361 < cdx < 363:
                    LUNIT14A_accumulator_LIST.append(char)
                    LUNIT14A = ''.join(LUNIT14A_accumulator_LIST)
                elif 362 < cdx < 365:
                    LDURA14A_accumulator_LIST.append(char)
                    LDURA14A = ''.join(LDURA14A_accumulator_LIST)
                elif 364 < cdx < 366:
                    LDURB14A_accumulator_LIST.append(char)
                    LDURB14A = ''.join(LDURB14A_accumulator_LIST)
                elif 365 < cdx < 367:
                    LCHRC14A_accumulator_LIST.append(char)
                    LCHRC14A = ''.join(LCHRC14A_accumulator_LIST)
                elif 366 < cdx < 369:
                    LATIME15_accumulator_LIST.append(char)
                    LATIME15 = ''.join(LATIME15_accumulator_LIST)
                elif 368 < cdx < 370:
                    LAUNIT15_accumulator_LIST.append(char)
                    LAUNIT15 = ''.join(LAUNIT15_accumulator_LIST)
                elif 369 < cdx < 372:
                    LADURA15_accumulator_LIST.append(char)
                    LADURA15 = ''.join(LADURA15_accumulator_LIST)
                elif 371 < cdx < 373:
                    LADURB15_accumulator_LIST.append(char)
                    LADURB15 = ''.join(LADURB15_accumulator_LIST)
                elif 372 < cdx < 374:
                    LACHRC15_accumulator_LIST.append(char)
                    LACHRC15 = ''.join(LACHRC15_accumulator_LIST)
                elif 373 < cdx < 376:
                    LATIME16_accumulator_LIST.append(char)
                    LATIME16 = ''.join(LATIME16_accumulator_LIST)
                elif 375 < cdx < 377:
                    LAUNIT16_accumulator_LIST.append(char)
                    LAUNIT16 = ''.join(LAUNIT16_accumulator_LIST)
                elif 376 < cdx < 379:
                    LADURA16_accumulator_LIST.append(char)
                    LADURA16 = ''.join(LADURA16_accumulator_LIST)
                elif 378 < cdx < 380:
                    LADURB16_accumulator_LIST.append(char)
                    LADURB16 = ''.join(LADURB16_accumulator_LIST)
                elif 379 < cdx < 381:
                    LACHRC16_accumulator_LIST.append(char)
                    LACHRC16 = ''.join(LACHRC16_accumulator_LIST)
                elif 380 < cdx < 383:
                    LATIME17_accumulator_LIST.append(char)
                    LATIME17 = ''.join(LATIME17_accumulator_LIST)
                elif 382 < cdx < 384:
                    LAUNIT17_accumulator_LIST.append(char)
                    LAUNIT17 = ''.join(LAUNIT17_accumulator_LIST)
                elif 383 < cdx < 386:
                    LADURA17_accumulator_LIST.append(char)
                    LADURA17 = ''.join(LADURA17_accumulator_LIST)
                elif 385 < cdx < 387:
                    LADURB17_accumulator_LIST.append(char)
                    LADURB17 = ''.join(LADURB17_accumulator_LIST)
                elif 386 < cdx < 388:
                    LACHRC17_accumulator_LIST.append(char)
                    LACHRC17 = ''.join(LACHRC17_accumulator_LIST)
                elif 387 < cdx < 390:
                    LATIME18_accumulator_LIST.append(char)
                    LATIME18 = ''.join(LATIME18_accumulator_LIST)
                elif 389 < cdx < 391:
                    LAUNIT18_accumulator_LIST.append(char)
                    LAUNIT18 = ''.join(LAUNIT18_accumulator_LIST)
                elif 390 < cdx < 393:
                    LADURA18_accumulator_LIST.append(char)
                    LADURA18 = ''.join(LADURA18_accumulator_LIST)
                elif 392 < cdx < 394:
                    LADURB18_accumulator_LIST.append(char)
                    LADURB18 = ''.join(LADURB18_accumulator_LIST)
                elif 393 < cdx < 395:
                    LACHRC18_accumulator_LIST.append(char)
                    LACHRC18 = ''.join(LACHRC18_accumulator_LIST)
                elif 394 < cdx < 397:
                    LATIME19_accumulator_LIST.append(char)
                    LATIME19 = ''.join(LATIME19_accumulator_LIST)
                elif 396 < cdx < 398:
                    LAUNIT19_accumulator_LIST.append(char)
                    LAUNIT19 = ''.join(LAUNIT19_accumulator_LIST)
                elif 397 < cdx < 400:
                    LADURA19_accumulator_LIST.append(char)
                    LADURA19 = ''.join(LADURA19_accumulator_LIST)
                elif 399 < cdx < 401:
                    LADURB19_accumulator_LIST.append(char)
                    LADURB19 = ''.join(LADURB19_accumulator_LIST)
                elif 400 < cdx < 402:
                    LACHRC19_accumulator_LIST.append(char)
                    LACHRC19 = ''.join(LACHRC19_accumulator_LIST)
                elif 401 < cdx < 404:
                    LATIME20_accumulator_LIST.append(char)
                    LATIME20 = ''.join(LATIME20_accumulator_LIST)
                elif 403 < cdx < 405:
                    LAUNIT20_accumulator_LIST.append(char)
                    LAUNIT20 = ''.join(LAUNIT20_accumulator_LIST)
                elif 404 < cdx < 407:
                    LADURA20_accumulator_LIST.append(char)
                    LADURA20 = ''.join(LADURA20_accumulator_LIST)
                elif 406 < cdx < 408:
                    LADURB20_accumulator_LIST.append(char)
                    LADURB20 = ''.join(LADURB20_accumulator_LIST)
                elif 407 < cdx < 409:
                    LACHRC20_accumulator_LIST.append(char)
                    LACHRC20 = ''.join(LACHRC20_accumulator_LIST)
                elif 408 < cdx < 411:
                    LATIME21_accumulator_LIST.append(char)
                    LATIME21 = ''.join(LATIME21_accumulator_LIST)
                elif 410 < cdx < 412:
                    LAUNIT21_accumulator_LIST.append(char)
                    LAUNIT21 = ''.join(LAUNIT21_accumulator_LIST)
                elif 411 < cdx < 414:
                    LADURA21_accumulator_LIST.append(char)
                    LADURA21 = ''.join(LADURA21_accumulator_LIST)
                elif 413 < cdx < 415:
                    LADURB21_accumulator_LIST.append(char)
                    LADURB21 = ''.join(LADURB21_accumulator_LIST)
                elif 414 < cdx < 416:
                    LACHRC21_accumulator_LIST.append(char)
                    LACHRC21 = ''.join(LACHRC21_accumulator_LIST)
                elif 415 < cdx < 418:
                    LATIME22_accumulator_LIST.append(char)
                    LATIME22 = ''.join(LATIME22_accumulator_LIST)
                elif 417 < cdx < 419:
                    LAUNIT22_accumulator_LIST.append(char)
                    LAUNIT22 = ''.join(LAUNIT22_accumulator_LIST)
                elif 418 < cdx < 421:
                    LADURA22_accumulator_LIST.append(char)
                    LADURA22 = ''.join(LADURA22_accumulator_LIST)
                elif 420 < cdx < 422:
                    LADURB22_accumulator_LIST.append(char)
                    LADURB22 = ''.join(LADURB22_accumulator_LIST)
                elif 421 < cdx < 423:
                    LACHRC22_accumulator_LIST.append(char)
                    LACHRC22 = ''.join(LACHRC22_accumulator_LIST)
                elif 422 < cdx < 425:
                    LATIME23_accumulator_LIST.append(char)
                    LATIME23 = ''.join(LATIME23_accumulator_LIST)
                elif 424 < cdx < 426:
                    LAUNIT23_accumulator_LIST.append(char)
                    LAUNIT23 = ''.join(LAUNIT23_accumulator_LIST)
                elif 425 < cdx < 428:
                    LADURA23_accumulator_LIST.append(char)
                    LADURA23 = ''.join(LADURA23_accumulator_LIST)
                elif 427 < cdx < 429:
                    LADURB23_accumulator_LIST.append(char)
                    LADURB23 = ''.join(LADURB23_accumulator_LIST)
                elif 428 < cdx < 430:
                    LACHRC23_accumulator_LIST.append(char)
                    LACHRC23 = ''.join(LACHRC23_accumulator_LIST)
                elif 429 < cdx < 432:
                    LATIME24_accumulator_LIST.append(char)
                    LATIME24 = ''.join(LATIME24_accumulator_LIST)
                elif 431 < cdx < 433:
                    LAUNIT24_accumulator_LIST.append(char)
                    LAUNIT24 = ''.join(LAUNIT24_accumulator_LIST)
                elif 432 < cdx < 435:
                    LADURA24_accumulator_LIST.append(char)
                    LADURA24 = ''.join(LADURA24_accumulator_LIST)
                elif 434 < cdx < 436:
                    LADURB24_accumulator_LIST.append(char)
                    LADURB24 = ''.join(LADURB24_accumulator_LIST)
                elif 435 < cdx < 437:
                    LACHRC24_accumulator_LIST.append(char)
                    LACHRC24 = ''.join(LACHRC24_accumulator_LIST)
                elif 436 < cdx < 439:
                    LATIME25_accumulator_LIST.append(char)
                    LATIME25 = ''.join(LATIME25_accumulator_LIST)
                elif 438 < cdx < 440:
                    LAUNIT25_accumulator_LIST.append(char)
                    LAUNIT25 = ''.join(LAUNIT25_accumulator_LIST)
                elif 439 < cdx < 442:
                    LADURA25_accumulator_LIST.append(char)
                    LADURA25 = ''.join(LADURA25_accumulator_LIST)
                elif 441 < cdx < 443:
                    LADURB25_accumulator_LIST.append(char)
                    LADURB25 = ''.join(LADURB25_accumulator_LIST)
                elif 442 < cdx < 444:
                    LACHRC25_accumulator_LIST.append(char)
                    LACHRC25 = ''.join(LACHRC25_accumulator_LIST)
                elif 443 < cdx < 446:
                    LATIME26_accumulator_LIST.append(char)
                    LATIME26 = ''.join(LATIME26_accumulator_LIST)
                elif 445 < cdx < 447:
                    LAUNIT26_accumulator_LIST.append(char)
                    LAUNIT26 = ''.join(LAUNIT26_accumulator_LIST)
                elif 446 < cdx < 449:
                    LADURA26_accumulator_LIST.append(char)
                    LADURA26 = ''.join(LADURA26_accumulator_LIST)
                elif 448 < cdx < 450:
                    LADURB26_accumulator_LIST.append(char)
                    LADURB26 = ''.join(LADURB26_accumulator_LIST)
                elif 449 < cdx < 451:
                    LACHRC26_accumulator_LIST.append(char)
                    LACHRC26 = ''.join(LACHRC26_accumulator_LIST)
                elif 450 < cdx < 453:
                    LATIME27_accumulator_LIST.append(char)
                    LATIME27 = ''.join(LATIME27_accumulator_LIST)
                elif 452 < cdx < 454:
                    LAUNIT27_accumulator_LIST.append(char)
                    LAUNIT27 = ''.join(LAUNIT27_accumulator_LIST)
                elif 453 < cdx < 456:
                    LADURA27_accumulator_LIST.append(char)
                    LADURA27 = ''.join(LADURA27_accumulator_LIST)
                elif 455 < cdx < 457:
                    LADURB27_accumulator_LIST.append(char)
                    LADURB27 = ''.join(LADURB27_accumulator_LIST)
                elif 456 < cdx < 458:
                    LACHRC27_accumulator_LIST.append(char)
                    LACHRC27 = ''.join(LACHRC27_accumulator_LIST)
                elif 457 < cdx < 460:
                    LATIME28_accumulator_LIST.append(char)
                    LATIME28 = ''.join(LATIME28_accumulator_LIST)
                elif 459 < cdx < 461:
                    LAUNIT28_accumulator_LIST.append(char)
                    LAUNIT28 = ''.join(LAUNIT28_accumulator_LIST)
                elif 460 < cdx < 463:
                    LADURA28_accumulator_LIST.append(char)
                    LADURA28 = ''.join(LADURA28_accumulator_LIST)
                elif 462 < cdx < 464:
                    LADURB28_accumulator_LIST.append(char)
                    LADURB28 = ''.join(LADURB28_accumulator_LIST)
                elif 463 < cdx < 465:
                    LACHRC28_accumulator_LIST.append(char)
                    LACHRC28 = ''.join(LACHRC28_accumulator_LIST)
                elif 464 < cdx < 467:
                    LATIME29_accumulator_LIST.append(char)
                    LATIME29 = ''.join(LATIME29_accumulator_LIST)
                elif 466 < cdx < 468:
                    LAUNIT29_accumulator_LIST.append(char)
                    LAUNIT29 = ''.join(LAUNIT29_accumulator_LIST)
                elif 467 < cdx < 470:
                    LADURA29_accumulator_LIST.append(char)
                    LADURA29 = ''.join(LADURA29_accumulator_LIST)
                elif 469 < cdx < 471:
                    LADURB29_accumulator_LIST.append(char)
                    LADURB29 = ''.join(LADURB29_accumulator_LIST)
                elif 470 < cdx < 472:
                    LACHRC29_accumulator_LIST.append(char)
                    LACHRC29 = ''.join(LACHRC29_accumulator_LIST)
                elif 471 < cdx < 474:
                    LATIME30_accumulator_LIST.append(char)
                    LATIME30 = ''.join(LATIME30_accumulator_LIST)
                elif 473 < cdx < 475:
                    LAUNIT30_accumulator_LIST.append(char)
                    LAUNIT30 = ''.join(LAUNIT30_accumulator_LIST)
                elif 474 < cdx < 477:
                    LADURA30_accumulator_LIST.append(char)
                    LADURA30 = ''.join(LADURA30_accumulator_LIST)
                elif 476 < cdx < 478:
                    LADURB30_accumulator_LIST.append(char)
                    LADURB30 = ''.join(LADURB30_accumulator_LIST)
                elif 477 < cdx < 479:
                    LACHRC30_accumulator_LIST.append(char)
                    LACHRC30 = ''.join(LACHRC30_accumulator_LIST)
                elif 478 < cdx < 481:
                    LATIME31_accumulator_LIST.append(char)
                    LATIME31 = ''.join(LATIME31_accumulator_LIST)
                elif 480 < cdx < 482:
                    LAUNIT31_accumulator_LIST.append(char)
                    LAUNIT31 = ''.join(LAUNIT31_accumulator_LIST)
                elif 481 < cdx < 484:
                    LADURA31_accumulator_LIST.append(char)
                    LADURA31 = ''.join(LADURA31_accumulator_LIST)
                elif 483 < cdx < 485:
                    LADURB31_accumulator_LIST.append(char)
                    LADURB31 = ''.join(LADURB31_accumulator_LIST)
                elif 484 < cdx < 486:
                    LACHRC31_accumulator_LIST.append(char)
                    LACHRC31 = ''.join(LACHRC31_accumulator_LIST)
                elif 485 < cdx < 488:
                    LATIME32_accumulator_LIST.append(char)
                    LATIME32 = ''.join(LATIME32_accumulator_LIST)
                elif 487 < cdx < 489:
                    LAUNIT32_accumulator_LIST.append(char)
                    LAUNIT32 = ''.join(LAUNIT32_accumulator_LIST)
                elif 488 < cdx < 491:
                    LADURA32_accumulator_LIST.append(char)
                    LADURA32 = ''.join(LADURA32_accumulator_LIST)
                elif 490 < cdx < 492:
                    LADURB32_accumulator_LIST.append(char)
                    LADURB32 = ''.join(LADURB32_accumulator_LIST)
                elif 491 < cdx < 493:
                    LACHRC32_accumulator_LIST.append(char)
                    LACHRC32 = ''.join(LACHRC32_accumulator_LIST)
                elif 492 < cdx < 495:
                    LATIME33_accumulator_LIST.append(char)
                    LATIME33 = ''.join(LATIME33_accumulator_LIST)
                elif 494 < cdx < 496:
                    LAUNIT33_accumulator_LIST.append(char)
                    LAUNIT33 = ''.join(LAUNIT33_accumulator_LIST)
                elif 495 < cdx < 498:
                    LADURA33_accumulator_LIST.append(char)
                    LADURA33 = ''.join(LADURA33_accumulator_LIST)
                elif 497 < cdx < 499:
                    LADURB33_accumulator_LIST.append(char)
                    LADURB33 = ''.join(LADURB33_accumulator_LIST)
                elif 498 < cdx < 500:
                    LACHRC33_accumulator_LIST.append(char)
                    LACHRC33 = ''.join(LACHRC33_accumulator_LIST)
                elif 499 < cdx < 502:
                    LATIME34_accumulator_LIST.append(char)
                    LATIME34 = ''.join(LATIME34_accumulator_LIST)
                elif 501 < cdx < 503:
                    LAUNIT34_accumulator_LIST.append(char)
                    LAUNIT34 = ''.join(LAUNIT34_accumulator_LIST)
                elif 502 < cdx < 505:
                    LADURA34_accumulator_LIST.append(char)
                    LADURA34 = ''.join(LADURA34_accumulator_LIST)
                elif 504 < cdx < 506:
                    LADURB34_accumulator_LIST.append(char)
                    LADURB34 = ''.join(LADURB34_accumulator_LIST)
                elif 505 < cdx < 507:
                    LACHRC34_accumulator_LIST.append(char)
                    LACHRC34 = ''.join(LACHRC34_accumulator_LIST)
                elif 506 < cdx < 509:
                    LATIME90_accumulator_LIST.append(char)
                    LATIME90 = ''.join(LATIME90_accumulator_LIST)
                elif 508 < cdx < 510:
                    LAUNIT90_accumulator_LIST.append(char)
                    LAUNIT90 = ''.join(LAUNIT90_accumulator_LIST)
                elif 509 < cdx < 512:
                    LADURA90_accumulator_LIST.append(char)
                    LADURA90 = ''.join(LADURA90_accumulator_LIST)
                elif 511 < cdx < 513:
                    LADURB90_accumulator_LIST.append(char)
                    LADURB90 = ''.join(LADURB90_accumulator_LIST)
                elif 512 < cdx < 514:
                    LACHRC90_accumulator_LIST.append(char)
                    LACHRC90 = ''.join(LACHRC90_accumulator_LIST)
                elif 513 < cdx < 516:
                    LATIME91_accumulator_LIST.append(char)
                    LATIME91 = ''.join(LATIME91_accumulator_LIST)
                elif 515 < cdx < 517:
                    LAUNIT91_accumulator_LIST.append(char)
                    LAUNIT91 = ''.join(LAUNIT91_accumulator_LIST)
                elif 516 < cdx < 519:
                    LADURA91_accumulator_LIST.append(char)
                    LADURA91 = ''.join(LADURA91_accumulator_LIST)
                elif 518 < cdx < 520:
                    LADURB91_accumulator_LIST.append(char)
                    LADURB91 = ''.join(LADURB91_accumulator_LIST)
                elif 519 < cdx < 521:
                    LACHRC91_accumulator_LIST.append(char)
                    LACHRC91 = ''.join(LACHRC91_accumulator_LIST)
                elif 520 < cdx < 522:
                    LCONDRT_accumulator_LIST.append(char)
                    LCONDRT = ''.join(LCONDRT_accumulator_LIST)
                elif 521 < cdx < 523:
                    LACHRONR_accumulator_LIST.append(char)
                    LACHRONR = ''.join(LACHRONR_accumulator_LIST)
                elif 522 < cdx < 524:
                    PHSTAT_accumulator_LIST.append(char)
                    PHSTAT = ''.join(PHSTAT_accumulator_LIST)
                elif 523 < cdx < 525:
                    PDMED12M_accumulator_LIST.append(char)
                    PDMED12M = ''.join(PDMED12M_accumulator_LIST)
                elif 524 < cdx < 526:
                    PNMED12M_accumulator_LIST.append(char)
                    PNMED12M = ''.join(PNMED12M_accumulator_LIST)
                elif 525 < cdx < 527:
                    PHOSPYR2_accumulator_LIST.append(char)
                    PHOSPYR2 = ''.join(PHOSPYR2_accumulator_LIST)
                elif 526 < cdx < 530:
                    HOSPNO_accumulator_LIST.append(char)
                    HOSPNO = ''.join(HOSPNO_accumulator_LIST)
                elif 529 < cdx < 533:
                    HPNITE_accumulator_LIST.append(char)
                    HPNITE = ''.join(HPNITE_accumulator_LIST)
                elif 532 < cdx < 534:
                    PHCHM2W_accumulator_LIST.append(char)
                    PHCHM2W = ''.join(PHCHM2W_accumulator_LIST)
                elif 533 < cdx < 536:
                    PHCHMN2W_accumulator_LIST.append(char)
                    PHCHMN2W = ''.join(PHCHMN2W_accumulator_LIST)
                elif 535 < cdx < 537:
                    PHCPH2WR_accumulator_LIST.append(char)
                    PHCPH2WR = ''.join(PHCPH2WR_accumulator_LIST)
                elif 536 < cdx < 539:
                    PHCPHN2W_accumulator_LIST.append(char)
                    PHCPHN2W = ''.join(PHCPHN2W_accumulator_LIST)
                elif 538 < cdx < 540:
                    PHCDV2W_accumulator_LIST.append(char)
                    PHCDV2W = ''.join(PHCDV2W_accumulator_LIST)
                elif 539 < cdx < 542:
                    PHCDVN2W_accumulator_LIST.append(char)
                    PHCDVN2W = ''.join(PHCDVN2W_accumulator_LIST)
                elif 541 < cdx < 543:
                    P10DVYR_accumulator_LIST.append(char)
                    P10DVYR = ''.join(P10DVYR_accumulator_LIST)
                elif 542 < cdx < 544:
                    NOTCOV_accumulator_LIST.append(char)
                    NOTCOV = ''.join(NOTCOV_accumulator_LIST)
                elif 543 < cdx < 545:
                    MEDICARE_accumulator_LIST.append(char)
                    MEDICARE = ''.join(MEDICARE_accumulator_LIST)
                elif 544 < cdx < 546:
                    MCPART_accumulator_LIST.append(char)
                    MCPART = ''.join(MCPART_accumulator_LIST)
                elif 545 < cdx < 547:
                    MCCHOICE_accumulator_LIST.append(char)
                    MCCHOICE = ''.join(MCCHOICE_accumulator_LIST)
                elif 546 < cdx < 548:
                    MCHMO_accumulator_LIST.append(char)
                    MCHMO = ''.join(MCHMO_accumulator_LIST)
                elif 547 < cdx < 549:
                    MCADVR_accumulator_LIST.append(char)
                    MCADVR = ''.join(MCADVR_accumulator_LIST)
                elif 548 < cdx < 550:
                    MCPREM_accumulator_LIST.append(char)
                    MCPREM = ''.join(MCPREM_accumulator_LIST)
                elif 549 < cdx < 551:
                    MCREF_accumulator_LIST.append(char)
                    MCREF = ''.join(MCREF_accumulator_LIST)
                elif 550 < cdx < 552:
                    MCPARTD_accumulator_LIST.append(char)
                    MCPARTD = ''.join(MCPARTD_accumulator_LIST)
                elif 551 < cdx < 553:
                    MEDICAID_accumulator_LIST.append(char)
                    MEDICAID = ''.join(MEDICAID_accumulator_LIST)
                elif 552 < cdx < 554:
                    MAFLG_accumulator_LIST.append(char)
                    MAFLG = ''.join(MAFLG_accumulator_LIST)
                elif 553 < cdx < 555:
                    MACHMD_accumulator_LIST.append(char)
                    MACHMD = ''.join(MACHMD_accumulator_LIST)
                elif 554 < cdx < 556:
                    MXCHNG_accumulator_LIST.append(char)
                    MXCHNG = ''.join(MXCHNG_accumulator_LIST)
                elif 555 < cdx < 557:
                    MEDPREM_accumulator_LIST.append(char)
                    MEDPREM = ''.join(MEDPREM_accumulator_LIST)
                elif 556 < cdx < 558:
                    MDPRINC_accumulator_LIST.append(char)
                    MDPRINC = ''.join(MDPRINC_accumulator_LIST)
                elif 557 < cdx < 559:
                    MAPCMD_accumulator_LIST.append(char)
                    MAPCMD = ''.join(MAPCMD_accumulator_LIST)
                elif 558 < cdx < 560:
                    MAREF_accumulator_LIST.append(char)
                    MAREF = ''.join(MAREF_accumulator_LIST)
                elif 559 < cdx < 561:
                    SINGLE_accumulator_LIST.append(char)
                    SINGLE = ''.join(SINGLE_accumulator_LIST)
                elif 560 < cdx < 562:
                    SSTYPEA_accumulator_LIST.append(char)
                    SSTYPEA = ''.join(SSTYPEA_accumulator_LIST)
                elif 561 < cdx < 563:
                    SSTYPEB_accumulator_LIST.append(char)
                    SSTYPEB = ''.join(SSTYPEB_accumulator_LIST)
                elif 562 < cdx < 564:
                    SSTYPEC_accumulator_LIST.append(char)
                    SSTYPEC = ''.join(SSTYPEC_accumulator_LIST)
                elif 563 < cdx < 565:
                    SSTYPED_accumulator_LIST.append(char)
                    SSTYPED = ''.join(SSTYPED_accumulator_LIST)
                elif 564 < cdx < 566:
                    SSTYPEE_accumulator_LIST.append(char)
                    SSTYPEE = ''.join(SSTYPEE_accumulator_LIST)
                elif 565 < cdx < 567:
                    SSTYPEF_accumulator_LIST.append(char)
                    SSTYPEF = ''.join(SSTYPEF_accumulator_LIST)
                elif 566 < cdx < 568:
                    SSTYPEG_accumulator_LIST.append(char)
                    SSTYPEG = ''.join(SSTYPEG_accumulator_LIST)
                elif 567 < cdx < 569:
                    SSTYPEH_accumulator_LIST.append(char)
                    SSTYPEH = ''.join(SSTYPEH_accumulator_LIST)
                elif 568 < cdx < 570:
                    SSTYPEI_accumulator_LIST.append(char)
                    SSTYPEI = ''.join(SSTYPEI_accumulator_LIST)
                elif 569 < cdx < 571:
                    SSTYPEJ_accumulator_LIST.append(char)
                    SSTYPEJ = ''.join(SSTYPEJ_accumulator_LIST)
                elif 570 < cdx < 572:
                    SSTYPEK_accumulator_LIST.append(char)
                    SSTYPEK = ''.join(SSTYPEK_accumulator_LIST)
                elif 571 < cdx < 573:
                    SSTYPEL_accumulator_LIST.append(char)
                    SSTYPEL = ''.join(SSTYPEL_accumulator_LIST)
                elif 572 < cdx < 574:
                    PRIVATE_accumulator_LIST.append(char)
                    PRIVATE = ''.join(PRIVATE_accumulator_LIST)
                elif 573 < cdx < 575:
                    PRFLG_accumulator_LIST.append(char)
                    PRFLG = ''.join(PRFLG_accumulator_LIST)
                elif 574 < cdx < 576:
                    EXCHANGE_accumulator_LIST.append(char)
                    EXCHANGE = ''.join(EXCHANGE_accumulator_LIST)
                elif 575 < cdx < 577:
                    WHONAM1_accumulator_LIST.append(char)
                    WHONAM1 = ''.join(WHONAM1_accumulator_LIST)
                elif 576 < cdx < 578:
                    PRPOLH1_accumulator_LIST.append(char)
                    PRPOLH1 = ''.join(PRPOLH1_accumulator_LIST)
                elif 577 < cdx < 579:
                    PRCOOH1_accumulator_LIST.append(char)
                    PRCOOH1 = ''.join(PRCOOH1_accumulator_LIST)
                elif 578 < cdx < 581:
                    PRCTOH1_accumulator_LIST.append(char)
                    PRCTOH1 = ''.join(PRCTOH1_accumulator_LIST)
                elif 580 < cdx < 582:
                    PRRLOH11_accumulator_LIST.append(char)
                    PRRLOH11 = ''.join(PRRLOH11_accumulator_LIST)
                elif 581 < cdx < 583:
                    PRRLOH21_accumulator_LIST.append(char)
                    PRRLOH21 = ''.join(PRRLOH21_accumulator_LIST)
                elif 582 < cdx < 584:
                    PRRLOH31_accumulator_LIST.append(char)
                    PRRLOH31 = ''.join(PRRLOH31_accumulator_LIST)
                elif 583 < cdx < 585:
                    PRRLOH41_accumulator_LIST.append(char)
                    PRRLOH41 = ''.join(PRRLOH41_accumulator_LIST)
                elif 584 < cdx < 587:
                    PRCNUM1_accumulator_LIST.append(char)
                    PRCNUM1 = ''.join(PRCNUM1_accumulator_LIST)
                elif 586 < cdx < 589:
                    COHU191_accumulator_LIST.append(char)
                    COHU191 = ''.join(COHU191_accumulator_LIST)
                elif 588 < cdx < 591:
                    COH19251_accumulator_LIST.append(char)
                    COH19251 = ''.join(COH19251_accumulator_LIST)
                elif 590 < cdx < 593:
                    COHO251_accumulator_LIST.append(char)
                    COHO251 = ''.join(COHO251_accumulator_LIST)
                elif 592 < cdx < 595:
                    PLNWRKR1_accumulator_LIST.append(char)
                    PLNWRKR1 = ''.join(PLNWRKR1_accumulator_LIST)
                elif 594 < cdx < 596:
                    PLNEXCH1_accumulator_LIST.append(char)
                    PLNEXCH1 = ''.join(PLNEXCH1_accumulator_LIST)
                elif 595 < cdx < 597:
                    EXCHPR1_accumulator_LIST.append(char)
                    EXCHPR1 = ''.join(EXCHPR1_accumulator_LIST)
                elif 596 < cdx < 598:
                    PLNPAY11_accumulator_LIST.append(char)
                    PLNPAY11 = ''.join(PLNPAY11_accumulator_LIST)
                elif 597 < cdx < 599:
                    PLNPAY21_accumulator_LIST.append(char)
                    PLNPAY21 = ''.join(PLNPAY21_accumulator_LIST)
                elif 598 < cdx < 600:
                    PLNPAY31_accumulator_LIST.append(char)
                    PLNPAY31 = ''.join(PLNPAY31_accumulator_LIST)
                elif 599 < cdx < 601:
                    PLNPAY41_accumulator_LIST.append(char)
                    PLNPAY41 = ''.join(PLNPAY41_accumulator_LIST)
                elif 600 < cdx < 602:
                    PLNPAY51_accumulator_LIST.append(char)
                    PLNPAY51 = ''.join(PLNPAY51_accumulator_LIST)
                elif 601 < cdx < 603:
                    PLNPAY61_accumulator_LIST.append(char)
                    PLNPAY61 = ''.join(PLNPAY61_accumulator_LIST)
                elif 602 < cdx < 604:
                    PLNPAY71_accumulator_LIST.append(char)
                    PLNPAY71 = ''.join(PLNPAY71_accumulator_LIST)
                elif 603 < cdx < 605:
                    PLNPRE1_accumulator_LIST.append(char)
                    PLNPRE1 = ''.join(PLNPRE1_accumulator_LIST)
                elif 604 < cdx < 610:
                    HICOSTR1_accumulator_LIST.append(char)
                    HICOSTR1 = ''.join(HICOSTR1_accumulator_LIST)
                elif 609 < cdx < 611:
                    EMPPAY1_accumulator_LIST.append(char)
                    EMPPAY1 = ''.join(EMPPAY1_accumulator_LIST)
                elif 610 < cdx < 616:
                    ECOSTR1_accumulator_LIST.append(char)
                    ECOSTR1 = ''.join(ECOSTR1_accumulator_LIST)
                elif 615 < cdx < 619:
                    EMPCSTP1_accumulator_LIST.append(char)
                    EMPCSTP1 = ''.join(EMPCSTP1_accumulator_LIST)
                elif 618 < cdx < 620:
                    PLNMGD1_accumulator_LIST.append(char)
                    PLNMGD1 = ''.join(PLNMGD1_accumulator_LIST)
                elif 619 < cdx < 621:
                    HDHP1_accumulator_LIST.append(char)
                    HDHP1 = ''.join(HDHP1_accumulator_LIST)
                elif 620 < cdx < 622:
                    HSAHRA1_accumulator_LIST.append(char)
                    HSAHRA1 = ''.join(HSAHRA1_accumulator_LIST)
                elif 621 < cdx < 623:
                    MGCHMD1_accumulator_LIST.append(char)
                    MGCHMD1 = ''.join(MGCHMD1_accumulator_LIST)
                elif 622 < cdx < 624:
                    MGPRMD1_accumulator_LIST.append(char)
                    MGPRMD1 = ''.join(MGPRMD1_accumulator_LIST)
                elif 623 < cdx < 625:
                    MGPYMD1_accumulator_LIST.append(char)
                    MGPYMD1 = ''.join(MGPYMD1_accumulator_LIST)
                elif 624 < cdx < 626:
                    MGPREF1_accumulator_LIST.append(char)
                    MGPREF1 = ''.join(MGPREF1_accumulator_LIST)
                elif 625 < cdx < 627:
                    PCPREQ1_accumulator_LIST.append(char)
                    PCPREQ1 = ''.join(PCPREQ1_accumulator_LIST)
                elif 626 < cdx < 628:
                    PRRXCOV1_accumulator_LIST.append(char)
                    PRRXCOV1 = ''.join(PRRXCOV1_accumulator_LIST)
                elif 627 < cdx < 629:
                    PRDNCOV1_accumulator_LIST.append(char)
                    PRDNCOV1 = ''.join(PRDNCOV1_accumulator_LIST)
                elif 628 < cdx < 630:
                    PXCHNG_accumulator_LIST.append(char)
                    PXCHNG = ''.join(PXCHNG_accumulator_LIST)
                elif 629 < cdx < 631:
                    PLEXCHPR_accumulator_LIST.append(char)
                    PLEXCHPR = ''.join(PLEXCHPR_accumulator_LIST)
                elif 630 < cdx < 632:
                    PSTRFPRM_accumulator_LIST.append(char)
                    PSTRFPRM = ''.join(PSTRFPRM_accumulator_LIST)
                elif 631 < cdx < 633:
                    PSSPRINC_accumulator_LIST.append(char)
                    PSSPRINC = ''.join(PSSPRINC_accumulator_LIST)
                elif 632 < cdx < 634:
                    PSTDOC_accumulator_LIST.append(char)
                    PSTDOC = ''.join(PSTDOC_accumulator_LIST)
                elif 633 < cdx < 635:
                    PSTCMD_accumulator_LIST.append(char)
                    PSTCMD = ''.join(PSTCMD_accumulator_LIST)
                elif 634 < cdx < 636:
                    PSTREF_accumulator_LIST.append(char)
                    PSTREF = ''.join(PSTREF_accumulator_LIST)
                elif 635 < cdx < 637:
                    WHONAM2_accumulator_LIST.append(char)
                    WHONAM2 = ''.join(WHONAM2_accumulator_LIST)
                elif 636 < cdx < 638:
                    PRPOLH2_accumulator_LIST.append(char)
                    PRPOLH2 = ''.join(PRPOLH2_accumulator_LIST)
                elif 637 < cdx < 639:
                    PRCOOH2_accumulator_LIST.append(char)
                    PRCOOH2 = ''.join(PRCOOH2_accumulator_LIST)
                elif 638 < cdx < 641:
                    PRCTOH2_accumulator_LIST.append(char)
                    PRCTOH2 = ''.join(PRCTOH2_accumulator_LIST)
                elif 640 < cdx < 642:
                    PRRLOH12_accumulator_LIST.append(char)
                    PRRLOH12 = ''.join(PRRLOH12_accumulator_LIST)
                elif 641 < cdx < 643:
                    PRRLOH22_accumulator_LIST.append(char)
                    PRRLOH22 = ''.join(PRRLOH22_accumulator_LIST)
                elif 642 < cdx < 644:
                    PRRLOH32_accumulator_LIST.append(char)
                    PRRLOH32 = ''.join(PRRLOH32_accumulator_LIST)
                elif 643 < cdx < 645:
                    PRRLOH42_accumulator_LIST.append(char)
                    PRRLOH42 = ''.join(PRRLOH42_accumulator_LIST)
                elif 644 < cdx < 647:
                    PRCNUM2_accumulator_LIST.append(char)
                    PRCNUM2 = ''.join(PRCNUM2_accumulator_LIST)
                elif 646 < cdx < 649:
                    COHU192_accumulator_LIST.append(char)
                    COHU192 = ''.join(COHU192_accumulator_LIST)
                elif 648 < cdx < 651:
                    COH19252_accumulator_LIST.append(char)
                    COH19252 = ''.join(COH19252_accumulator_LIST)
                elif 650 < cdx < 653:
                    COHO252_accumulator_LIST.append(char)
                    COHO252 = ''.join(COHO252_accumulator_LIST)
                elif 652 < cdx < 655:
                    PLNWRKR2_accumulator_LIST.append(char)
                    PLNWRKR2 = ''.join(PLNWRKR2_accumulator_LIST)
                elif 654 < cdx < 656:
                    PLNEXCH2_accumulator_LIST.append(char)
                    PLNEXCH2 = ''.join(PLNEXCH2_accumulator_LIST)
                elif 655 < cdx < 657:
                    EXCHPR2_accumulator_LIST.append(char)
                    EXCHPR2 = ''.join(EXCHPR2_accumulator_LIST)
                elif 656 < cdx < 658:
                    PLNPAY12_accumulator_LIST.append(char)
                    PLNPAY12 = ''.join(PLNPAY12_accumulator_LIST)
                elif 657 < cdx < 659:
                    PLNPAY22_accumulator_LIST.append(char)
                    PLNPAY22 = ''.join(PLNPAY22_accumulator_LIST)
                elif 658 < cdx < 660:
                    PLNPAY32_accumulator_LIST.append(char)
                    PLNPAY32 = ''.join(PLNPAY32_accumulator_LIST)
                elif 659 < cdx < 661:
                    PLNPAY42_accumulator_LIST.append(char)
                    PLNPAY42 = ''.join(PLNPAY42_accumulator_LIST)
                elif 660 < cdx < 662:
                    PLNPAY52_accumulator_LIST.append(char)
                    PLNPAY52 = ''.join(PLNPAY52_accumulator_LIST)
                elif 661 < cdx < 663:
                    PLNPAY62_accumulator_LIST.append(char)
                    PLNPAY62 = ''.join(PLNPAY62_accumulator_LIST)
                elif 662 < cdx < 664:
                    PLNPAY72_accumulator_LIST.append(char)
                    PLNPAY72 = ''.join(PLNPAY72_accumulator_LIST)
                elif 663 < cdx < 665:
                    PLNPRE2_accumulator_LIST.append(char)
                    PLNPRE2 = ''.join(PLNPRE2_accumulator_LIST)
                elif 664 < cdx < 670:
                    HICOSTR2_accumulator_LIST.append(char)
                    HICOSTR2 = ''.join(HICOSTR2_accumulator_LIST)
                elif 669 < cdx < 671:
                    EMPPAY2_accumulator_LIST.append(char)
                    EMPPAY2 = ''.join(EMPPAY2_accumulator_LIST)
                elif 670 < cdx < 676:
                    ECOSTR2_accumulator_LIST.append(char)
                    ECOSTR2 = ''.join(ECOSTR2_accumulator_LIST)
                elif 675 < cdx < 679:
                    EMPCSTP2_accumulator_LIST.append(char)
                    EMPCSTP2 = ''.join(EMPCSTP2_accumulator_LIST)
                elif 678 < cdx < 680:
                    PLNMGD2_accumulator_LIST.append(char)
                    PLNMGD2 = ''.join(PLNMGD2_accumulator_LIST)
                elif 679 < cdx < 681:
                    HDHP2_accumulator_LIST.append(char)
                    HDHP2 = ''.join(HDHP2_accumulator_LIST)
                elif 680 < cdx < 682:
                    HSAHRA2_accumulator_LIST.append(char)
                    HSAHRA2 = ''.join(HSAHRA2_accumulator_LIST)
                elif 681 < cdx < 683:
                    MGCHMD2_accumulator_LIST.append(char)
                    MGCHMD2 = ''.join(MGCHMD2_accumulator_LIST)
                elif 682 < cdx < 684:
                    MGPRMD2_accumulator_LIST.append(char)
                    MGPRMD2 = ''.join(MGPRMD2_accumulator_LIST)
                elif 683 < cdx < 685:
                    MGPYMD2_accumulator_LIST.append(char)
                    MGPYMD2 = ''.join(MGPYMD2_accumulator_LIST)
                elif 684 < cdx < 686:
                    MGPREF2_accumulator_LIST.append(char)
                    MGPREF2 = ''.join(MGPREF2_accumulator_LIST)
                elif 685 < cdx < 687:
                    PCPREQ2_accumulator_LIST.append(char)
                    PCPREQ2 = ''.join(PCPREQ2_accumulator_LIST)
                elif 686 < cdx < 688:
                    PRRXCOV2_accumulator_LIST.append(char)
                    PRRXCOV2 = ''.join(PRRXCOV2_accumulator_LIST)
                elif 687 < cdx < 689:
                    PRDNCOV2_accumulator_LIST.append(char)
                    PRDNCOV2 = ''.join(PRDNCOV2_accumulator_LIST)
                elif 688 < cdx < 690:
                    PRPLPLUS_accumulator_LIST.append(char)
                    PRPLPLUS = ''.join(PRPLPLUS_accumulator_LIST)
                elif 689 < cdx < 691:
                    FCOVCONF_accumulator_LIST.append(char)
                    FCOVCONF = ''.join(FCOVCONF_accumulator_LIST)
                elif 690 < cdx < 692:
                    SCHIP_accumulator_LIST.append(char)
                    SCHIP = ''.join(SCHIP_accumulator_LIST)
                elif 691 < cdx < 693:
                    CHFLG_accumulator_LIST.append(char)
                    CHFLG = ''.join(CHFLG_accumulator_LIST)
                elif 692 < cdx < 694:
                    CHXCHNG_accumulator_LIST.append(char)
                    CHXCHNG = ''.join(CHXCHNG_accumulator_LIST)
                elif 693 < cdx < 695:
                    STRFPRM1_accumulator_LIST.append(char)
                    STRFPRM1 = ''.join(STRFPRM1_accumulator_LIST)
                elif 694 < cdx < 696:
                    CHPRINC_accumulator_LIST.append(char)
                    CHPRINC = ''.join(CHPRINC_accumulator_LIST)
                elif 695 < cdx < 697:
                    STDOC1_accumulator_LIST.append(char)
                    STDOC1 = ''.join(STDOC1_accumulator_LIST)
                elif 696 < cdx < 698:
                    STPCMD1_accumulator_LIST.append(char)
                    STPCMD1 = ''.join(STPCMD1_accumulator_LIST)
                elif 697 < cdx < 699:
                    STREF1_accumulator_LIST.append(char)
                    STREF1 = ''.join(STREF1_accumulator_LIST)
                elif 698 < cdx < 700:
                    OTHPUB_accumulator_LIST.append(char)
                    OTHPUB = ''.join(OTHPUB_accumulator_LIST)
                elif 699 < cdx < 701:
                    OPFLG_accumulator_LIST.append(char)
                    OPFLG = ''.join(OPFLG_accumulator_LIST)
                elif 700 < cdx < 702:
                    OPXCHNG_accumulator_LIST.append(char)
                    OPXCHNG = ''.join(OPXCHNG_accumulator_LIST)
                elif 701 < cdx < 703:
                    PLEXCHOP_accumulator_LIST.append(char)
                    PLEXCHOP = ''.join(PLEXCHOP_accumulator_LIST)
                elif 702 < cdx < 704:
                    STRFPRM2_accumulator_LIST.append(char)
                    STRFPRM2 = ''.join(STRFPRM2_accumulator_LIST)
                elif 703 < cdx < 705:
                    SSPRINC_accumulator_LIST.append(char)
                    SSPRINC = ''.join(SSPRINC_accumulator_LIST)
                elif 704 < cdx < 706:
                    STDOC2_accumulator_LIST.append(char)
                    STDOC2 = ''.join(STDOC2_accumulator_LIST)
                elif 705 < cdx < 707:
                    STPCMD2_accumulator_LIST.append(char)
                    STPCMD2 = ''.join(STPCMD2_accumulator_LIST)
                elif 706 < cdx < 708:
                    STREF2_accumulator_LIST.append(char)
                    STREF2 = ''.join(STREF2_accumulator_LIST)
                elif 707 < cdx < 709:
                    OTHGOV_accumulator_LIST.append(char)
                    OTHGOV = ''.join(OTHGOV_accumulator_LIST)
                elif 708 < cdx < 710:
                    OGFLG_accumulator_LIST.append(char)
                    OGFLG = ''.join(OGFLG_accumulator_LIST)
                elif 709 < cdx < 711:
                    OGXCHNG_accumulator_LIST.append(char)
                    OGXCHNG = ''.join(OGXCHNG_accumulator_LIST)
                elif 710 < cdx < 712:
                    PLEXCHOG_accumulator_LIST.append(char)
                    PLEXCHOG = ''.join(PLEXCHOG_accumulator_LIST)
                elif 711 < cdx < 713:
                    STRFPRM3_accumulator_LIST.append(char)
                    STRFPRM3 = ''.join(STRFPRM3_accumulator_LIST)
                elif 712 < cdx < 714:
                    OGPRINC_accumulator_LIST.append(char)
                    OGPRINC = ''.join(OGPRINC_accumulator_LIST)
                elif 713 < cdx < 715:
                    STDOC3_accumulator_LIST.append(char)
                    STDOC3 = ''.join(STDOC3_accumulator_LIST)
                elif 714 < cdx < 716:
                    STPCMD3_accumulator_LIST.append(char)
                    STPCMD3 = ''.join(STPCMD3_accumulator_LIST)
                elif 715 < cdx < 717:
                    STREF3_accumulator_LIST.append(char)
                    STREF3 = ''.join(STREF3_accumulator_LIST)
                elif 716 < cdx < 718:
                    MILCARE_accumulator_LIST.append(char)
                    MILCARE = ''.join(MILCARE_accumulator_LIST)
                elif 717 < cdx < 719:
                    MILSPC1_accumulator_LIST.append(char)
                    MILSPC1 = ''.join(MILSPC1_accumulator_LIST)
                elif 718 < cdx < 720:
                    MILSPC2_accumulator_LIST.append(char)
                    MILSPC2 = ''.join(MILSPC2_accumulator_LIST)
                elif 719 < cdx < 721:
                    MILSPC3_accumulator_LIST.append(char)
                    MILSPC3 = ''.join(MILSPC3_accumulator_LIST)
                elif 720 < cdx < 722:
                    MILSPC4_accumulator_LIST.append(char)
                    MILSPC4 = ''.join(MILSPC4_accumulator_LIST)
                elif 721 < cdx < 723:
                    MILMAN_accumulator_LIST.append(char)
                    MILMAN = ''.join(MILMAN_accumulator_LIST)
                elif 722 < cdx < 724:
                    IHS_accumulator_LIST.append(char)
                    IHS = ''.join(IHS_accumulator_LIST)
                elif 723 < cdx < 725:
                    HILAST_accumulator_LIST.append(char)
                    HILAST = ''.join(HILAST_accumulator_LIST)
                elif 724 < cdx < 726:
                    HISTOP1_accumulator_LIST.append(char)
                    HISTOP1 = ''.join(HISTOP1_accumulator_LIST)
                elif 725 < cdx < 727:
                    HISTOP2_accumulator_LIST.append(char)
                    HISTOP2 = ''.join(HISTOP2_accumulator_LIST)
                elif 726 < cdx < 728:
                    HISTOP3_accumulator_LIST.append(char)
                    HISTOP3 = ''.join(HISTOP3_accumulator_LIST)
                elif 727 < cdx < 729:
                    HISTOP4_accumulator_LIST.append(char)
                    HISTOP4 = ''.join(HISTOP4_accumulator_LIST)
                elif 728 < cdx < 730:
                    HISTOP5_accumulator_LIST.append(char)
                    HISTOP5 = ''.join(HISTOP5_accumulator_LIST)
                elif 729 < cdx < 731:
                    HISTOP6_accumulator_LIST.append(char)
                    HISTOP6 = ''.join(HISTOP6_accumulator_LIST)
                elif 730 < cdx < 732:
                    HISTOP7_accumulator_LIST.append(char)
                    HISTOP7 = ''.join(HISTOP7_accumulator_LIST)
                elif 731 < cdx < 733:
                    HISTOP8_accumulator_LIST.append(char)
                    HISTOP8 = ''.join(HISTOP8_accumulator_LIST)
                elif 732 < cdx < 734:
                    HISTOP9_accumulator_LIST.append(char)
                    HISTOP9 = ''.join(HISTOP9_accumulator_LIST)
                elif 733 < cdx < 735:
                    HISTOP10_accumulator_LIST.append(char)
                    HISTOP10 = ''.join(HISTOP10_accumulator_LIST)
                elif 734 < cdx < 736:
                    HISTOP11_accumulator_LIST.append(char)
                    HISTOP11 = ''.join(HISTOP11_accumulator_LIST)
                elif 735 < cdx < 737:
                    HISTOP12_accumulator_LIST.append(char)
                    HISTOP12 = ''.join(HISTOP12_accumulator_LIST)
                elif 736 < cdx < 738:
                    HISTOP13_accumulator_LIST.append(char)
                    HISTOP13 = ''.join(HISTOP13_accumulator_LIST)
                elif 737 < cdx < 739:
                    HISTOP14_accumulator_LIST.append(char)
                    HISTOP14 = ''.join(HISTOP14_accumulator_LIST)
                elif 738 < cdx < 740:
                    HISTOP15_accumulator_LIST.append(char)
                    HISTOP15 = ''.join(HISTOP15_accumulator_LIST)
                elif 739 < cdx < 741:
                    HINOTYR_accumulator_LIST.append(char)
                    HINOTYR = ''.join(HINOTYR_accumulator_LIST)
                elif 740 < cdx < 743:
                    HINOTMYR_accumulator_LIST.append(char)
                    HINOTMYR = ''.join(HINOTMYR_accumulator_LIST)
                elif 742 < cdx < 744:
                    FHICHNG_accumulator_LIST.append(char)
                    FHICHNG = ''.join(FHICHNG_accumulator_LIST)
                elif 743 < cdx < 745:
                    FHIKDBA_accumulator_LIST.append(char)
                    FHIKDBA = ''.join(FHIKDBA_accumulator_LIST)
                elif 744 < cdx < 746:
                    FHIKDBB_accumulator_LIST.append(char)
                    FHIKDBB = ''.join(FHIKDBB_accumulator_LIST)
                elif 745 < cdx < 747:
                    FHIKDBC_accumulator_LIST.append(char)
                    FHIKDBC = ''.join(FHIKDBC_accumulator_LIST)
                elif 746 < cdx < 748:
                    FHIKDBD_accumulator_LIST.append(char)
                    FHIKDBD = ''.join(FHIKDBD_accumulator_LIST)
                elif 747 < cdx < 749:
                    FHIKDBE_accumulator_LIST.append(char)
                    FHIKDBE = ''.join(FHIKDBE_accumulator_LIST)
                elif 748 < cdx < 750:
                    FHIKDBF_accumulator_LIST.append(char)
                    FHIKDBF = ''.join(FHIKDBF_accumulator_LIST)
                elif 749 < cdx < 751:
                    FHIKDBG_accumulator_LIST.append(char)
                    FHIKDBG = ''.join(FHIKDBG_accumulator_LIST)
                elif 750 < cdx < 752:
                    FHIKDBH_accumulator_LIST.append(char)
                    FHIKDBH = ''.join(FHIKDBH_accumulator_LIST)
                elif 751 < cdx < 753:
                    FHIKDBI_accumulator_LIST.append(char)
                    FHIKDBI = ''.join(FHIKDBI_accumulator_LIST)
                elif 752 < cdx < 754:
                    FHIKDBJ_accumulator_LIST.append(char)
                    FHIKDBJ = ''.join(FHIKDBJ_accumulator_LIST)
                elif 753 < cdx < 755:
                    FHIKDBK_accumulator_LIST.append(char)
                    FHIKDBK = ''.join(FHIKDBK_accumulator_LIST)
                elif 754 < cdx < 757:
                    PWRKBR1_accumulator_LIST.append(char)
                    PWRKBR1 = ''.join(PWRKBR1_accumulator_LIST)
                elif 756 < cdx < 758:
                    HCSPFYR_accumulator_LIST.append(char)
                    HCSPFYR = ''.join(HCSPFYR_accumulator_LIST)
                elif 757 < cdx < 759:
                    MEDBILL_accumulator_LIST.append(char)
                    MEDBILL = ''.join(MEDBILL_accumulator_LIST)
                elif 758 < cdx < 760:
                    MEDBPAY_accumulator_LIST.append(char)
                    MEDBPAY = ''.join(MEDBPAY_accumulator_LIST)
                elif 759 < cdx < 761:
                    MEDBNOP_accumulator_LIST.append(char)
                    MEDBNOP = ''.join(MEDBNOP_accumulator_LIST)
                elif 760 < cdx < 762:
                    FSA_accumulator_LIST.append(char)
                    FSA = ''.join(FSA_accumulator_LIST)
                elif 761 < cdx < 763:
                    HIKINDNA_accumulator_LIST.append(char)
                    HIKINDNA = ''.join(HIKINDNA_accumulator_LIST)
                elif 762 < cdx < 764:
                    HIKINDNB_accumulator_LIST.append(char)
                    HIKINDNB = ''.join(HIKINDNB_accumulator_LIST)
                elif 763 < cdx < 765:
                    HIKINDNC_accumulator_LIST.append(char)
                    HIKINDNC = ''.join(HIKINDNC_accumulator_LIST)
                elif 764 < cdx < 766:
                    HIKINDND_accumulator_LIST.append(char)
                    HIKINDND = ''.join(HIKINDND_accumulator_LIST)
                elif 765 < cdx < 767:
                    HIKINDNE_accumulator_LIST.append(char)
                    HIKINDNE = ''.join(HIKINDNE_accumulator_LIST)
                elif 766 < cdx < 768:
                    HIKINDNF_accumulator_LIST.append(char)
                    HIKINDNF = ''.join(HIKINDNF_accumulator_LIST)
                elif 767 < cdx < 769:
                    HIKINDNG_accumulator_LIST.append(char)
                    HIKINDNG = ''.join(HIKINDNG_accumulator_LIST)
                elif 768 < cdx < 770:
                    HIKINDNH_accumulator_LIST.append(char)
                    HIKINDNH = ''.join(HIKINDNH_accumulator_LIST)
                elif 769 < cdx < 771:
                    HIKINDNI_accumulator_LIST.append(char)
                    HIKINDNI = ''.join(HIKINDNI_accumulator_LIST)
                elif 770 < cdx < 772:
                    HIKINDNJ_accumulator_LIST.append(char)
                    HIKINDNJ = ''.join(HIKINDNJ_accumulator_LIST)
                elif 771 < cdx < 773:
                    HIKINDNK_accumulator_LIST.append(char)
                    HIKINDNK = ''.join(HIKINDNK_accumulator_LIST)
                elif 772 < cdx < 774:
                    MCAREPRB_accumulator_LIST.append(char)
                    MCAREPRB = ''.join(MCAREPRB_accumulator_LIST)
                elif 773 < cdx < 775:
                    MCAIDPRB_accumulator_LIST.append(char)
                    MCAIDPRB = ''.join(MCAIDPRB_accumulator_LIST)
                elif 774 < cdx < 776:
                    SINCOV_accumulator_LIST.append(char)
                    SINCOV = ''.join(SINCOV_accumulator_LIST)
                elif 775 < cdx < 777:
                    PLBORN_accumulator_LIST.append(char)
                    PLBORN = ''.join(PLBORN_accumulator_LIST)
                elif 776 < cdx < 779:
                    REGIONBR_accumulator_LIST.append(char)
                    REGIONBR = ''.join(REGIONBR_accumulator_LIST)
                elif 778 < cdx < 780:
                    GEOBRTH_accumulator_LIST.append(char)
                    GEOBRTH = ''.join(GEOBRTH_accumulator_LIST)
                elif 779 < cdx < 781:
                    YRSINUS_accumulator_LIST.append(char)
                    YRSINUS = ''.join(YRSINUS_accumulator_LIST)
                elif 780 < cdx < 782:
                    CITIZENP_accumulator_LIST.append(char)
                    CITIZENP = ''.join(CITIZENP_accumulator_LIST)
                elif 781 < cdx < 783:
                    HEADST_accumulator_LIST.append(char)
                    HEADST = ''.join(HEADST_accumulator_LIST)
                elif 782 < cdx < 784:
                    HEADSTV1_accumulator_LIST.append(char)
                    HEADSTV1 = ''.join(HEADSTV1_accumulator_LIST)
                elif 783 < cdx < 786:
                    EDUC1_accumulator_LIST.append(char)
                    EDUC1 = ''.join(EDUC1_accumulator_LIST)
                elif 785 < cdx < 787:
                    ARMFVER_accumulator_LIST.append(char)
                    ARMFVER = ''.join(ARMFVER_accumulator_LIST)
                elif 786 < cdx < 788:
                    ARMFEV_accumulator_LIST.append(char)
                    ARMFEV = ''.join(ARMFEV_accumulator_LIST)
                elif 787 < cdx < 789:
                    ARMFFC_accumulator_LIST.append(char)
                    ARMFFC = ''.join(ARMFFC_accumulator_LIST)
                elif 788 < cdx < 790:
                    ARMFTM1P_accumulator_LIST.append(char)
                    ARMFTM1P = ''.join(ARMFTM1P_accumulator_LIST)
                elif 789 < cdx < 791:
                    ARMFTM2P_accumulator_LIST.append(char)
                    ARMFTM2P = ''.join(ARMFTM2P_accumulator_LIST)
                elif 790 < cdx < 792:
                    ARMFTM3P_accumulator_LIST.append(char)
                    ARMFTM3P = ''.join(ARMFTM3P_accumulator_LIST)
                elif 791 < cdx < 793:
                    ARMFTM4P_accumulator_LIST.append(char)
                    ARMFTM4P = ''.join(ARMFTM4P_accumulator_LIST)
                elif 792 < cdx < 794:
                    ARMFTM5P_accumulator_LIST.append(char)
                    ARMFTM5P = ''.join(ARMFTM5P_accumulator_LIST)
                elif 793 < cdx < 795:
                    ARMFTM6P_accumulator_LIST.append(char)
                    ARMFTM6P = ''.join(ARMFTM6P_accumulator_LIST)
                elif 794 < cdx < 796:
                    ARMFTM7P_accumulator_LIST.append(char)
                    ARMFTM7P = ''.join(ARMFTM7P_accumulator_LIST)
                elif 795 < cdx < 797:
                    ARMFDS2P_accumulator_LIST.append(char)
                    ARMFDS2P = ''.join(ARMFDS2P_accumulator_LIST)
                elif 796 < cdx < 798:
                    DOINGLWP_accumulator_LIST.append(char)
                    DOINGLWP = ''.join(DOINGLWP_accumulator_LIST)
                elif 797 < cdx < 800:
                    WHYNOWKP_accumulator_LIST.append(char)
                    WHYNOWKP = ''.join(WHYNOWKP_accumulator_LIST)
                elif 799 < cdx < 802:
                    WRKHRS2_accumulator_LIST.append(char)
                    WRKHRS2 = ''.join(WRKHRS2_accumulator_LIST)
                elif 801 < cdx < 803:
                    WRKFTALL_accumulator_LIST.append(char)
                    WRKFTALL = ''.join(WRKFTALL_accumulator_LIST)
                elif 802 < cdx < 804:
                    WRKLYR1_accumulator_LIST.append(char)
                    WRKLYR1 = ''.join(WRKLYR1_accumulator_LIST)
                elif 803 < cdx < 806:
                    WRKMYR_accumulator_LIST.append(char)
                    WRKMYR = ''.join(WRKMYR_accumulator_LIST)
                elif 805 < cdx < 808:
                    ERNYR_P_accumulator_LIST.append(char)
                    ERNYR_P = ''.join(ERNYR_P_accumulator_LIST)
                elif 807 < cdx < 809:
                    HIEMPOF_accumulator_LIST.append(char)
                    HIEMPOF = ''.join(HIEMPOF_accumulator_LIST)
                elif 808 < cdx < 810:
                    FINCINT_accumulator_LIST.append(char)
                    FINCINT = ''.join(FINCINT_accumulator_LIST)
                elif 809 < cdx < 811:
                    PSAL_accumulator_LIST.append(char)
                    PSAL = ''.join(PSAL_accumulator_LIST)
                elif 810 < cdx < 812:
                    PSEINC_accumulator_LIST.append(char)
                    PSEINC = ''.join(PSEINC_accumulator_LIST)
                elif 811 < cdx < 813:
                    PSSRR_accumulator_LIST.append(char)
                    PSSRR = ''.join(PSSRR_accumulator_LIST)
                elif 812 < cdx < 814:
                    PSSRRDB_accumulator_LIST.append(char)
                    PSSRRDB = ''.join(PSSRRDB_accumulator_LIST)
                elif 813 < cdx < 815:
                    PSSRRD_accumulator_LIST.append(char)
                    PSSRRD = ''.join(PSSRRD_accumulator_LIST)
                elif 814 < cdx < 816:
                    PPENS_accumulator_LIST.append(char)
                    PPENS = ''.join(PPENS_accumulator_LIST)
                elif 815 < cdx < 817:
                    POPENS_accumulator_LIST.append(char)
                    POPENS = ''.join(POPENS_accumulator_LIST)
                elif 816 < cdx < 818:
                    PSSI_accumulator_LIST.append(char)
                    PSSI = ''.join(PSSI_accumulator_LIST)
                elif 817 < cdx < 819:
                    PSSID_accumulator_LIST.append(char)
                    PSSID = ''.join(PSSID_accumulator_LIST)
                elif 818 < cdx < 820:
                    PTANF_accumulator_LIST.append(char)
                    PTANF = ''.join(PTANF_accumulator_LIST)
                elif 819 < cdx < 821:
                    POWBEN_accumulator_LIST.append(char)
                    POWBEN = ''.join(POWBEN_accumulator_LIST)
                elif 820 < cdx < 822:
                    PINTRSTR_accumulator_LIST.append(char)
                    PINTRSTR = ''.join(PINTRSTR_accumulator_LIST)
                elif 821 < cdx < 823:
                    PDIVD_accumulator_LIST.append(char)
                    PDIVD = ''.join(PDIVD_accumulator_LIST)
                elif 822 < cdx < 824:
                    PCHLDSP_accumulator_LIST.append(char)
                    PCHLDSP = ''.join(PCHLDSP_accumulator_LIST)
                elif 823 < cdx < 825:
                    PINCOT_accumulator_LIST.append(char)
                    PINCOT = ''.join(PINCOT_accumulator_LIST)
                elif 824 < cdx < 826:
                    PSSAPL_accumulator_LIST.append(char)
                    PSSAPL = ''.join(PSSAPL_accumulator_LIST)
                elif 825 < cdx < 827:
                    PSDAPL_accumulator_LIST.append(char)
                    PSDAPL = ''.join(PSDAPL_accumulator_LIST)
                elif 826 < cdx < 829:
                    TANFMYR_accumulator_LIST.append(char)
                    TANFMYR = ''.join(TANFMYR_accumulator_LIST)
                elif 828 < cdx < 830:
                    ELIGPWIC_accumulator_LIST.append(char)
                    ELIGPWIC = ''.join(ELIGPWIC_accumulator_LIST)
                elif 829 < cdx < 831:
                    PWIC_accumulator_LIST.append(char)
                    PWIC = ''.join(PWIC_accumulator_LIST)
                elif 830 < cdx < 832:
                    WIC_FLAG_accumulator_LIST.append(char)
                    WIC_FLAG = ''.join(WIC_FLAG_accumulator_LIST)
                elif 831 < cdx < 833:
                    ENGLANG_accumulator_LIST.append(char)
                    ENGLANG = ''.join(ENGLANG_accumulator_LIST)
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
        WTIA_LIST.append(WTIA)
        WTFA_LIST.append(WTFA)
        REGION_LIST.append(REGION)
        STRAT_P_LIST.append(STRAT_P)
        PSU_P_LIST.append(PSU_P)
        SEX_LIST.append(SEX)
        ORIGIN_I_LIST.append(ORIGIN_I)
        ORIGIMPT_LIST.append(ORIGIMPT)
        HISPAN_I_LIST.append(HISPAN_I)
        HISPIMPT_LIST.append(HISPIMPT)
        RACERPI2_LIST.append(RACERPI2)
        RACEIMP2_LIST.append(RACEIMP2)
        MRACRPI2_LIST.append(MRACRPI2)
        MRACBPI2_LIST.append(MRACBPI2)
        RACRECI3_LIST.append(RACRECI3)
        HISCODI3_LIST.append(HISCODI3)
        ERIMPFLG_LIST.append(ERIMPFLG)
        NOWAF_LIST.append(NOWAF)
        RRP_LIST.append(RRP)
        HHREFLG_LIST.append(HHREFLG)
        FRRP_LIST.append(FRRP)
        DOB_M_LIST.append(DOB_M)
        DOB_Y_P_LIST.append(DOB_Y_P)
        AGE_P_LIST.append(AGE_P)
        AGE_CHG_LIST.append(AGE_CHG)
        FMRPFLG_LIST.append(FMRPFLG)
        FMREFLG_LIST.append(FMREFLG)
        R_MARITL_LIST.append(R_MARITL)
        FSPOUS2_LIST.append(FSPOUS2)
        COHAB1_LIST.append(COHAB1)
        COHAB2_LIST.append(COHAB2)
        FCOHAB3_LIST.append(FCOHAB3)
        CDCMSTAT_LIST.append(CDCMSTAT)
        SIB_DEGP_LIST.append(SIB_DEGP)
        FMOTHER1_LIST.append(FMOTHER1)
        MOM_DEGP_LIST.append(MOM_DEGP)
        FFATHER1_LIST.append(FFATHER1)
        DAD_DEGP_LIST.append(DAD_DEGP)
        PARENTS_LIST.append(PARENTS)
        MOM_ED_LIST.append(MOM_ED)
        DAD_ED_LIST.append(DAD_ED)
        ASTATFLG_LIST.append(ASTATFLG)
        CSTATFLG_LIST.append(CSTATFLG)
        QCADULT_LIST.append(QCADULT)
        QCCHILD_LIST.append(QCCHILD)
        FDRN_FLG_LIST.append(FDRN_FLG)
        PLAPLYLM_LIST.append(PLAPLYLM)
        PLAPLYUN_LIST.append(PLAPLYUN)
        PSPEDEIS_LIST.append(PSPEDEIS)
        PSPEDEM_LIST.append(PSPEDEM)
        PLAADL_LIST.append(PLAADL)
        LABATH_LIST.append(LABATH)
        LADRESS_LIST.append(LADRESS)
        LAEAT_LIST.append(LAEAT)
        LABED_LIST.append(LABED)
        LATOILT_LIST.append(LATOILT)
        LAHOME_LIST.append(LAHOME)
        PLAIADL_LIST.append(PLAIADL)
        PLAWKNOW_LIST.append(PLAWKNOW)
        PLAWKLIM_LIST.append(PLAWKLIM)
        PLAWALK_LIST.append(PLAWALK)
        PLAREMEM_LIST.append(PLAREMEM)
        PLIMANY_LIST.append(PLIMANY)
        LA1AR_LIST.append(LA1AR)
        LAHCC1_LIST.append(LAHCC1)
        LAHCC2_LIST.append(LAHCC2)
        LAHCC3_LIST.append(LAHCC3)
        LAHCC4_LIST.append(LAHCC4)
        LAHCC5_LIST.append(LAHCC5)
        LAHCC6_LIST.append(LAHCC6)
        LAHCC7A_LIST.append(LAHCC7A)
        LAHCC8_LIST.append(LAHCC8)
        LAHCC9_LIST.append(LAHCC9)
        LAHCC10_LIST.append(LAHCC10)
        LAHCC11_LIST.append(LAHCC11)
        LAHCC12_LIST.append(LAHCC12)
        LAHCC13_LIST.append(LAHCC13)
        LAHCC90_LIST.append(LAHCC90)
        LAHCC91_LIST.append(LAHCC91)
        LCTIME1_LIST.append(LCTIME1)
        LCUNIT1_LIST.append(LCUNIT1)
        LCDURA1_LIST.append(LCDURA1)
        LCDURB1_LIST.append(LCDURB1)
        LCCHRC1_LIST.append(LCCHRC1)
        LCTIME2_LIST.append(LCTIME2)
        LCUNIT2_LIST.append(LCUNIT2)
        LCDURA2_LIST.append(LCDURA2)
        LCDURB2_LIST.append(LCDURB2)
        LCCHRC2_LIST.append(LCCHRC2)
        LCTIME3_LIST.append(LCTIME3)
        LCUNIT3_LIST.append(LCUNIT3)
        LCDURA3_LIST.append(LCDURA3)
        LCDURB3_LIST.append(LCDURB3)
        LCCHRC3_LIST.append(LCCHRC3)
        LCTIME4_LIST.append(LCTIME4)
        LCUNIT4_LIST.append(LCUNIT4)
        LCDURA4_LIST.append(LCDURA4)
        LCDURB4_LIST.append(LCDURB4)
        LCCHRC4_LIST.append(LCCHRC4)
        LCTIME5_LIST.append(LCTIME5)
        LCUNIT5_LIST.append(LCUNIT5)
        LCDURA5_LIST.append(LCDURA5)
        LCDURB5_LIST.append(LCDURB5)
        LCCHRC5_LIST.append(LCCHRC5)
        LCTIME6_LIST.append(LCTIME6)
        LCUNIT6_LIST.append(LCUNIT6)
        LCDURA6_LIST.append(LCDURA6)
        LCDURB6_LIST.append(LCDURB6)
        LCCHRC6_LIST.append(LCCHRC6)
        LCTIME7A_LIST.append(LCTIME7A)
        LCUNIT7A_LIST.append(LCUNIT7A)
        LCDURA7A_LIST.append(LCDURA7A)
        LCDURB7A_LIST.append(LCDURB7A)
        LCCHRC7A_LIST.append(LCCHRC7A)
        LCTIME8_LIST.append(LCTIME8)
        LCUNIT8_LIST.append(LCUNIT8)
        LCDURA8_LIST.append(LCDURA8)
        LCDURB8_LIST.append(LCDURB8)
        LCCHRC8_LIST.append(LCCHRC8)
        LCTIME9_LIST.append(LCTIME9)
        LCUNIT9_LIST.append(LCUNIT9)
        LCDURA9_LIST.append(LCDURA9)
        LCDURB9_LIST.append(LCDURB9)
        LCCHRC9_LIST.append(LCCHRC9)
        LCTIME10_LIST.append(LCTIME10)
        LCUNIT10_LIST.append(LCUNIT10)
        LCDURA10_LIST.append(LCDURA10)
        LCDURB10_LIST.append(LCDURB10)
        LCCHRC10_LIST.append(LCCHRC10)
        LCTIME11_LIST.append(LCTIME11)
        LCUNIT11_LIST.append(LCUNIT11)
        LCDURA11_LIST.append(LCDURA11)
        LCDURB11_LIST.append(LCDURB11)
        LCCHRC11_LIST.append(LCCHRC11)
        LCTIME12_LIST.append(LCTIME12)
        LCUNIT12_LIST.append(LCUNIT12)
        LCDURA12_LIST.append(LCDURA12)
        LCDURB12_LIST.append(LCDURB12)
        LCCHRC12_LIST.append(LCCHRC12)
        LCTIME13_LIST.append(LCTIME13)
        LCUNIT13_LIST.append(LCUNIT13)
        LCDURA13_LIST.append(LCDURA13)
        LCDURB13_LIST.append(LCDURB13)
        LCCHRC13_LIST.append(LCCHRC13)
        LCTIME90_LIST.append(LCTIME90)
        LCUNIT90_LIST.append(LCUNIT90)
        LCDURA90_LIST.append(LCDURA90)
        LCDURB90_LIST.append(LCDURB90)
        LCCHRC90_LIST.append(LCCHRC90)
        LCTIME91_LIST.append(LCTIME91)
        LCUNIT91_LIST.append(LCUNIT91)
        LCDURA91_LIST.append(LCDURA91)
        LCDURB91_LIST.append(LCDURB91)
        LCCHRC91_LIST.append(LCCHRC91)
        LAHCA1_LIST.append(LAHCA1)
        LAHCA2_LIST.append(LAHCA2)
        LAHCA3_LIST.append(LAHCA3)
        LAHCA4_LIST.append(LAHCA4)
        LAHCA5_LIST.append(LAHCA5)
        LAHCA6_LIST.append(LAHCA6)
        LAHCA7_LIST.append(LAHCA7)
        LAHCA8_LIST.append(LAHCA8)
        LAHCA9_LIST.append(LAHCA9)
        LAHCA10_LIST.append(LAHCA10)
        LAHCA11_LIST.append(LAHCA11)
        LAHCA12_LIST.append(LAHCA12)
        LAHCA13_LIST.append(LAHCA13)
        LAHCA14A_LIST.append(LAHCA14A)
        LAHCA15_LIST.append(LAHCA15)
        LAHCA16_LIST.append(LAHCA16)
        LAHCA17_LIST.append(LAHCA17)
        LAHCA18_LIST.append(LAHCA18)
        LAHCA19__LIST.append(LAHCA19_)
        LAHCA20__LIST.append(LAHCA20_)
        LAHCA21__LIST.append(LAHCA21_)
        LAHCA22__LIST.append(LAHCA22_)
        LAHCA23__LIST.append(LAHCA23_)
        LAHCA24__LIST.append(LAHCA24_)
        LAHCA25__LIST.append(LAHCA25_)
        LAHCA26__LIST.append(LAHCA26_)
        LAHCA27__LIST.append(LAHCA27_)
        LAHCA28__LIST.append(LAHCA28_)
        LAHCA29__LIST.append(LAHCA29_)
        LAHCA30__LIST.append(LAHCA30_)
        LAHCA31__LIST.append(LAHCA31_)
        LAHCA32__LIST.append(LAHCA32_)
        LAHCA33__LIST.append(LAHCA33_)
        LAHCA34__LIST.append(LAHCA34_)
        LAHCA90_LIST.append(LAHCA90)
        LAHCA91_LIST.append(LAHCA91)
        LATIME1_LIST.append(LATIME1)
        LAUNIT1_LIST.append(LAUNIT1)
        LADURA1_LIST.append(LADURA1)
        LADURB1_LIST.append(LADURB1)
        LACHRC1_LIST.append(LACHRC1)
        LATIME2_LIST.append(LATIME2)
        LAUNIT2_LIST.append(LAUNIT2)
        LADURA2_LIST.append(LADURA2)
        LADURB2_LIST.append(LADURB2)
        LACHRC2_LIST.append(LACHRC2)
        LATIME3_LIST.append(LATIME3)
        LAUNIT3_LIST.append(LAUNIT3)
        LADURA3_LIST.append(LADURA3)
        LADURB3_LIST.append(LADURB3)
        LACHRC3_LIST.append(LACHRC3)
        LATIME4_LIST.append(LATIME4)
        LAUNIT4_LIST.append(LAUNIT4)
        LADURA4_LIST.append(LADURA4)
        LADURB4_LIST.append(LADURB4)
        LACHRC4_LIST.append(LACHRC4)
        LATIME5_LIST.append(LATIME5)
        LAUNIT5_LIST.append(LAUNIT5)
        LADURA5_LIST.append(LADURA5)
        LADURB5_LIST.append(LADURB5)
        LACHRC5_LIST.append(LACHRC5)
        LATIME6_LIST.append(LATIME6)
        LAUNIT6_LIST.append(LAUNIT6)
        LADURA6_LIST.append(LADURA6)
        LADURB6_LIST.append(LADURB6)
        LACHRC6_LIST.append(LACHRC6)
        LATIME7_LIST.append(LATIME7)
        LAUNIT7_LIST.append(LAUNIT7)
        LADURA7_LIST.append(LADURA7)
        LADURB7_LIST.append(LADURB7)
        LACHRC7_LIST.append(LACHRC7)
        LATIME8_LIST.append(LATIME8)
        LAUNIT8_LIST.append(LAUNIT8)
        LADURA8_LIST.append(LADURA8)
        LADURB8_LIST.append(LADURB8)
        LACHRC8_LIST.append(LACHRC8)
        LATIME9_LIST.append(LATIME9)
        LAUNIT9_LIST.append(LAUNIT9)
        LADURA9_LIST.append(LADURA9)
        LADURB9_LIST.append(LADURB9)
        LACHRC9_LIST.append(LACHRC9)
        LATIME10_LIST.append(LATIME10)
        LAUNIT10_LIST.append(LAUNIT10)
        LADURA10_LIST.append(LADURA10)
        LADURB10_LIST.append(LADURB10)
        LACHRC10_LIST.append(LACHRC10)
        LATIME11_LIST.append(LATIME11)
        LAUNIT11_LIST.append(LAUNIT11)
        LADURA11_LIST.append(LADURA11)
        LADURB11_LIST.append(LADURB11)
        LACHRC11_LIST.append(LACHRC11)
        LATIME12_LIST.append(LATIME12)
        LAUNIT12_LIST.append(LAUNIT12)
        LADURA12_LIST.append(LADURA12)
        LADURB12_LIST.append(LADURB12)
        LACHRC12_LIST.append(LACHRC12)
        LATIME13_LIST.append(LATIME13)
        LAUNIT13_LIST.append(LAUNIT13)
        LADURA13_LIST.append(LADURA13)
        LADURB13_LIST.append(LADURB13)
        LACHRC13_LIST.append(LACHRC13)
        LTIME14A_LIST.append(LTIME14A)
        LUNIT14A_LIST.append(LUNIT14A)
        LDURA14A_LIST.append(LDURA14A)
        LDURB14A_LIST.append(LDURB14A)
        LCHRC14A_LIST.append(LCHRC14A)
        LATIME15_LIST.append(LATIME15)
        LAUNIT15_LIST.append(LAUNIT15)
        LADURA15_LIST.append(LADURA15)
        LADURB15_LIST.append(LADURB15)
        LACHRC15_LIST.append(LACHRC15)
        LATIME16_LIST.append(LATIME16)
        LAUNIT16_LIST.append(LAUNIT16)
        LADURA16_LIST.append(LADURA16)
        LADURB16_LIST.append(LADURB16)
        LACHRC16_LIST.append(LACHRC16)
        LATIME17_LIST.append(LATIME17)
        LAUNIT17_LIST.append(LAUNIT17)
        LADURA17_LIST.append(LADURA17)
        LADURB17_LIST.append(LADURB17)
        LACHRC17_LIST.append(LACHRC17)
        LATIME18_LIST.append(LATIME18)
        LAUNIT18_LIST.append(LAUNIT18)
        LADURA18_LIST.append(LADURA18)
        LADURB18_LIST.append(LADURB18)
        LACHRC18_LIST.append(LACHRC18)
        LATIME19_LIST.append(LATIME19)
        LAUNIT19_LIST.append(LAUNIT19)
        LADURA19_LIST.append(LADURA19)
        LADURB19_LIST.append(LADURB19)
        LACHRC19_LIST.append(LACHRC19)
        LATIME20_LIST.append(LATIME20)
        LAUNIT20_LIST.append(LAUNIT20)
        LADURA20_LIST.append(LADURA20)
        LADURB20_LIST.append(LADURB20)
        LACHRC20_LIST.append(LACHRC20)
        LATIME21_LIST.append(LATIME21)
        LAUNIT21_LIST.append(LAUNIT21)
        LADURA21_LIST.append(LADURA21)
        LADURB21_LIST.append(LADURB21)
        LACHRC21_LIST.append(LACHRC21)
        LATIME22_LIST.append(LATIME22)
        LAUNIT22_LIST.append(LAUNIT22)
        LADURA22_LIST.append(LADURA22)
        LADURB22_LIST.append(LADURB22)
        LACHRC22_LIST.append(LACHRC22)
        LATIME23_LIST.append(LATIME23)
        LAUNIT23_LIST.append(LAUNIT23)
        LADURA23_LIST.append(LADURA23)
        LADURB23_LIST.append(LADURB23)
        LACHRC23_LIST.append(LACHRC23)
        LATIME24_LIST.append(LATIME24)
        LAUNIT24_LIST.append(LAUNIT24)
        LADURA24_LIST.append(LADURA24)
        LADURB24_LIST.append(LADURB24)
        LACHRC24_LIST.append(LACHRC24)
        LATIME25_LIST.append(LATIME25)
        LAUNIT25_LIST.append(LAUNIT25)
        LADURA25_LIST.append(LADURA25)
        LADURB25_LIST.append(LADURB25)
        LACHRC25_LIST.append(LACHRC25)
        LATIME26_LIST.append(LATIME26)
        LAUNIT26_LIST.append(LAUNIT26)
        LADURA26_LIST.append(LADURA26)
        LADURB26_LIST.append(LADURB26)
        LACHRC26_LIST.append(LACHRC26)
        LATIME27_LIST.append(LATIME27)
        LAUNIT27_LIST.append(LAUNIT27)
        LADURA27_LIST.append(LADURA27)
        LADURB27_LIST.append(LADURB27)
        LACHRC27_LIST.append(LACHRC27)
        LATIME28_LIST.append(LATIME28)
        LAUNIT28_LIST.append(LAUNIT28)
        LADURA28_LIST.append(LADURA28)
        LADURB28_LIST.append(LADURB28)
        LACHRC28_LIST.append(LACHRC28)
        LATIME29_LIST.append(LATIME29)
        LAUNIT29_LIST.append(LAUNIT29)
        LADURA29_LIST.append(LADURA29)
        LADURB29_LIST.append(LADURB29)
        LACHRC29_LIST.append(LACHRC29)
        LATIME30_LIST.append(LATIME30)
        LAUNIT30_LIST.append(LAUNIT30)
        LADURA30_LIST.append(LADURA30)
        LADURB30_LIST.append(LADURB30)
        LACHRC30_LIST.append(LACHRC30)
        LATIME31_LIST.append(LATIME31)
        LAUNIT31_LIST.append(LAUNIT31)
        LADURA31_LIST.append(LADURA31)
        LADURB31_LIST.append(LADURB31)
        LACHRC31_LIST.append(LACHRC31)
        LATIME32_LIST.append(LATIME32)
        LAUNIT32_LIST.append(LAUNIT32)
        LADURA32_LIST.append(LADURA32)
        LADURB32_LIST.append(LADURB32)
        LACHRC32_LIST.append(LACHRC32)
        LATIME33_LIST.append(LATIME33)
        LAUNIT33_LIST.append(LAUNIT33)
        LADURA33_LIST.append(LADURA33)
        LADURB33_LIST.append(LADURB33)
        LACHRC33_LIST.append(LACHRC33)
        LATIME34_LIST.append(LATIME34)
        LAUNIT34_LIST.append(LAUNIT34)
        LADURA34_LIST.append(LADURA34)
        LADURB34_LIST.append(LADURB34)
        LACHRC34_LIST.append(LACHRC34)
        LATIME90_LIST.append(LATIME90)
        LAUNIT90_LIST.append(LAUNIT90)
        LADURA90_LIST.append(LADURA90)
        LADURB90_LIST.append(LADURB90)
        LACHRC90_LIST.append(LACHRC90)
        LATIME91_LIST.append(LATIME91)
        LAUNIT91_LIST.append(LAUNIT91)
        LADURA91_LIST.append(LADURA91)
        LADURB91_LIST.append(LADURB91)
        LACHRC91_LIST.append(LACHRC91)
        LCONDRT_LIST.append(LCONDRT)
        LACHRONR_LIST.append(LACHRONR)
        PHSTAT_LIST.append(PHSTAT)
        PDMED12M_LIST.append(PDMED12M)
        PNMED12M_LIST.append(PNMED12M)
        PHOSPYR2_LIST.append(PHOSPYR2)
        HOSPNO_LIST.append(HOSPNO)
        HPNITE_LIST.append(HPNITE)
        PHCHM2W_LIST.append(PHCHM2W)
        PHCHMN2W_LIST.append(PHCHMN2W)
        PHCPH2WR_LIST.append(PHCPH2WR)
        PHCPHN2W_LIST.append(PHCPHN2W)
        PHCDV2W_LIST.append(PHCDV2W)
        PHCDVN2W_LIST.append(PHCDVN2W)
        P10DVYR_LIST.append(P10DVYR)
        NOTCOV_LIST.append(NOTCOV)
        MEDICARE_LIST.append(MEDICARE)
        MCPART_LIST.append(MCPART)
        MCCHOICE_LIST.append(MCCHOICE)
        MCHMO_LIST.append(MCHMO)
        MCADVR_LIST.append(MCADVR)
        MCPREM_LIST.append(MCPREM)
        MCREF_LIST.append(MCREF)
        MCPARTD_LIST.append(MCPARTD)
        MEDICAID_LIST.append(MEDICAID)
        MAFLG_LIST.append(MAFLG)
        MACHMD_LIST.append(MACHMD)
        MXCHNG_LIST.append(MXCHNG)
        MEDPREM_LIST.append(MEDPREM)
        MDPRINC_LIST.append(MDPRINC)
        MAPCMD_LIST.append(MAPCMD)
        MAREF_LIST.append(MAREF)
        SINGLE_LIST.append(SINGLE)
        SSTYPEA_LIST.append(SSTYPEA)
        SSTYPEB_LIST.append(SSTYPEB)
        SSTYPEC_LIST.append(SSTYPEC)
        SSTYPED_LIST.append(SSTYPED)
        SSTYPEE_LIST.append(SSTYPEE)
        SSTYPEF_LIST.append(SSTYPEF)
        SSTYPEG_LIST.append(SSTYPEG)
        SSTYPEH_LIST.append(SSTYPEH)
        SSTYPEI_LIST.append(SSTYPEI)
        SSTYPEJ_LIST.append(SSTYPEJ)
        SSTYPEK_LIST.append(SSTYPEK)
        SSTYPEL_LIST.append(SSTYPEL)
        PRIVATE_LIST.append(PRIVATE)
        PRFLG_LIST.append(PRFLG)
        EXCHANGE_LIST.append(EXCHANGE)
        WHONAM1_LIST.append(WHONAM1)
        PRPOLH1_LIST.append(PRPOLH1)
        PRCOOH1_LIST.append(PRCOOH1)
        PRCTOH1_LIST.append(PRCTOH1)
        PRRLOH11_LIST.append(PRRLOH11)
        PRRLOH21_LIST.append(PRRLOH21)
        PRRLOH31_LIST.append(PRRLOH31)
        PRRLOH41_LIST.append(PRRLOH41)
        PRCNUM1_LIST.append(PRCNUM1)
        COHU191_LIST.append(COHU191)
        COH19251_LIST.append(COH19251)
        COHO251_LIST.append(COHO251)
        PLNWRKR1_LIST.append(PLNWRKR1)
        PLNEXCH1_LIST.append(PLNEXCH1)
        EXCHPR1_LIST.append(EXCHPR1)
        PLNPAY11_LIST.append(PLNPAY11)
        PLNPAY21_LIST.append(PLNPAY21)
        PLNPAY31_LIST.append(PLNPAY31)
        PLNPAY41_LIST.append(PLNPAY41)
        PLNPAY51_LIST.append(PLNPAY51)
        PLNPAY61_LIST.append(PLNPAY61)
        PLNPAY71_LIST.append(PLNPAY71)
        PLNPRE1_LIST.append(PLNPRE1)
        HICOSTR1_LIST.append(HICOSTR1)
        EMPPAY1_LIST.append(EMPPAY1)
        ECOSTR1_LIST.append(ECOSTR1)
        EMPCSTP1_LIST.append(EMPCSTP1)
        PLNMGD1_LIST.append(PLNMGD1)
        HDHP1_LIST.append(HDHP1)
        HSAHRA1_LIST.append(HSAHRA1)
        MGCHMD1_LIST.append(MGCHMD1)
        MGPRMD1_LIST.append(MGPRMD1)
        MGPYMD1_LIST.append(MGPYMD1)
        MGPREF1_LIST.append(MGPREF1)
        PCPREQ1_LIST.append(PCPREQ1)
        PRRXCOV1_LIST.append(PRRXCOV1)
        PRDNCOV1_LIST.append(PRDNCOV1)
        PXCHNG_LIST.append(PXCHNG)
        PLEXCHPR_LIST.append(PLEXCHPR)
        PSTRFPRM_LIST.append(PSTRFPRM)
        PSSPRINC_LIST.append(PSSPRINC)
        PSTDOC_LIST.append(PSTDOC)
        PSTCMD_LIST.append(PSTCMD)
        PSTREF_LIST.append(PSTREF)
        WHONAM2_LIST.append(WHONAM2)
        PRPOLH2_LIST.append(PRPOLH2)
        PRCOOH2_LIST.append(PRCOOH2)
        PRCTOH2_LIST.append(PRCTOH2)
        PRRLOH12_LIST.append(PRRLOH12)
        PRRLOH22_LIST.append(PRRLOH22)
        PRRLOH32_LIST.append(PRRLOH32)
        PRRLOH42_LIST.append(PRRLOH42)
        PRCNUM2_LIST.append(PRCNUM2)
        COHU192_LIST.append(COHU192)
        COH19252_LIST.append(COH19252)
        COHO252_LIST.append(COHO252)
        PLNWRKR2_LIST.append(PLNWRKR2)
        PLNEXCH2_LIST.append(PLNEXCH2)
        EXCHPR2_LIST.append(EXCHPR2)
        PLNPAY12_LIST.append(PLNPAY12)
        PLNPAY22_LIST.append(PLNPAY22)
        PLNPAY32_LIST.append(PLNPAY32)
        PLNPAY42_LIST.append(PLNPAY42)
        PLNPAY52_LIST.append(PLNPAY52)
        PLNPAY62_LIST.append(PLNPAY62)
        PLNPAY72_LIST.append(PLNPAY72)
        PLNPRE2_LIST.append(PLNPRE2)
        HICOSTR2_LIST.append(HICOSTR2)
        EMPPAY2_LIST.append(EMPPAY2)
        ECOSTR2_LIST.append(ECOSTR2)
        EMPCSTP2_LIST.append(EMPCSTP2)
        PLNMGD2_LIST.append(PLNMGD2)
        HDHP2_LIST.append(HDHP2)
        HSAHRA2_LIST.append(HSAHRA2)
        MGCHMD2_LIST.append(MGCHMD2)
        MGPRMD2_LIST.append(MGPRMD2)
        MGPYMD2_LIST.append(MGPYMD2)
        MGPREF2_LIST.append(MGPREF2)
        PCPREQ2_LIST.append(PCPREQ2)
        PRRXCOV2_LIST.append(PRRXCOV2)
        PRDNCOV2_LIST.append(PRDNCOV2)
        PRPLPLUS_LIST.append(PRPLPLUS)
        FCOVCONF_LIST.append(FCOVCONF)
        SCHIP_LIST.append(SCHIP)
        CHFLG_LIST.append(CHFLG)
        CHXCHNG_LIST.append(CHXCHNG)
        STRFPRM1_LIST.append(STRFPRM1)
        CHPRINC_LIST.append(CHPRINC)
        STDOC1_LIST.append(STDOC1)
        STPCMD1_LIST.append(STPCMD1)
        STREF1_LIST.append(STREF1)
        OTHPUB_LIST.append(OTHPUB)
        OPFLG_LIST.append(OPFLG)
        OPXCHNG_LIST.append(OPXCHNG)
        PLEXCHOP_LIST.append(PLEXCHOP)
        STRFPRM2_LIST.append(STRFPRM2)
        SSPRINC_LIST.append(SSPRINC)
        STDOC2_LIST.append(STDOC2)
        STPCMD2_LIST.append(STPCMD2)
        STREF2_LIST.append(STREF2)
        OTHGOV_LIST.append(OTHGOV)
        OGFLG_LIST.append(OGFLG)
        OGXCHNG_LIST.append(OGXCHNG)
        PLEXCHOG_LIST.append(PLEXCHOG)
        STRFPRM3_LIST.append(STRFPRM3)
        OGPRINC_LIST.append(OGPRINC)
        STDOC3_LIST.append(STDOC3)
        STPCMD3_LIST.append(STPCMD3)
        STREF3_LIST.append(STREF3)
        MILCARE_LIST.append(MILCARE)
        MILSPC1_LIST.append(MILSPC1)
        MILSPC2_LIST.append(MILSPC2)
        MILSPC3_LIST.append(MILSPC3)
        MILSPC4_LIST.append(MILSPC4)
        MILMAN_LIST.append(MILMAN)
        IHS_LIST.append(IHS)
        HILAST_LIST.append(HILAST)
        HISTOP1_LIST.append(HISTOP1)
        HISTOP2_LIST.append(HISTOP2)
        HISTOP3_LIST.append(HISTOP3)
        HISTOP4_LIST.append(HISTOP4)
        HISTOP5_LIST.append(HISTOP5)
        HISTOP6_LIST.append(HISTOP6)
        HISTOP7_LIST.append(HISTOP7)
        HISTOP8_LIST.append(HISTOP8)
        HISTOP9_LIST.append(HISTOP9)
        HISTOP10_LIST.append(HISTOP10)
        HISTOP11_LIST.append(HISTOP11)
        HISTOP12_LIST.append(HISTOP12)
        HISTOP13_LIST.append(HISTOP13)
        HISTOP14_LIST.append(HISTOP14)
        HISTOP15_LIST.append(HISTOP15)
        HINOTYR_LIST.append(HINOTYR)
        HINOTMYR_LIST.append(HINOTMYR)
        FHICHNG_LIST.append(FHICHNG)
        FHIKDBA_LIST.append(FHIKDBA)
        FHIKDBB_LIST.append(FHIKDBB)
        FHIKDBC_LIST.append(FHIKDBC)
        FHIKDBD_LIST.append(FHIKDBD)
        FHIKDBE_LIST.append(FHIKDBE)
        FHIKDBF_LIST.append(FHIKDBF)
        FHIKDBG_LIST.append(FHIKDBG)
        FHIKDBH_LIST.append(FHIKDBH)
        FHIKDBI_LIST.append(FHIKDBI)
        FHIKDBJ_LIST.append(FHIKDBJ)
        FHIKDBK_LIST.append(FHIKDBK)
        PWRKBR1_LIST.append(PWRKBR1)
        HCSPFYR_LIST.append(HCSPFYR)
        MEDBILL_LIST.append(MEDBILL)
        MEDBPAY_LIST.append(MEDBPAY)
        MEDBNOP_LIST.append(MEDBNOP)
        FSA_LIST.append(FSA)
        HIKINDNA_LIST.append(HIKINDNA)
        HIKINDNB_LIST.append(HIKINDNB)
        HIKINDNC_LIST.append(HIKINDNC)
        HIKINDND_LIST.append(HIKINDND)
        HIKINDNE_LIST.append(HIKINDNE)
        HIKINDNF_LIST.append(HIKINDNF)
        HIKINDNG_LIST.append(HIKINDNG)
        HIKINDNH_LIST.append(HIKINDNH)
        HIKINDNI_LIST.append(HIKINDNI)
        HIKINDNJ_LIST.append(HIKINDNJ)
        HIKINDNK_LIST.append(HIKINDNK)
        MCAREPRB_LIST.append(MCAREPRB)
        MCAIDPRB_LIST.append(MCAIDPRB)
        SINCOV_LIST.append(SINCOV)
        PLBORN_LIST.append(PLBORN)
        REGIONBR_LIST.append(REGIONBR)
        GEOBRTH_LIST.append(GEOBRTH)
        YRSINUS_LIST.append(YRSINUS)
        CITIZENP_LIST.append(CITIZENP)
        HEADST_LIST.append(HEADST)
        HEADSTV1_LIST.append(HEADSTV1)
        EDUC1_LIST.append(EDUC1)
        ARMFVER_LIST.append(ARMFVER)
        ARMFEV_LIST.append(ARMFEV)
        ARMFFC_LIST.append(ARMFFC)
        ARMFTM1P_LIST.append(ARMFTM1P)
        ARMFTM2P_LIST.append(ARMFTM2P)
        ARMFTM3P_LIST.append(ARMFTM3P)
        ARMFTM4P_LIST.append(ARMFTM4P)
        ARMFTM5P_LIST.append(ARMFTM5P)
        ARMFTM6P_LIST.append(ARMFTM6P)
        ARMFTM7P_LIST.append(ARMFTM7P)
        ARMFDS2P_LIST.append(ARMFDS2P)
        DOINGLWP_LIST.append(DOINGLWP)
        WHYNOWKP_LIST.append(WHYNOWKP)
        WRKHRS2_LIST.append(WRKHRS2)
        WRKFTALL_LIST.append(WRKFTALL)
        WRKLYR1_LIST.append(WRKLYR1)
        WRKMYR_LIST.append(WRKMYR)
        ERNYR_P_LIST.append(ERNYR_P)
        HIEMPOF_LIST.append(HIEMPOF)
        FINCINT_LIST.append(FINCINT)
        PSAL_LIST.append(PSAL)
        PSEINC_LIST.append(PSEINC)
        PSSRR_LIST.append(PSSRR)
        PSSRRDB_LIST.append(PSSRRDB)
        PSSRRD_LIST.append(PSSRRD)
        PPENS_LIST.append(PPENS)
        POPENS_LIST.append(POPENS)
        PSSI_LIST.append(PSSI)
        PSSID_LIST.append(PSSID)
        PTANF_LIST.append(PTANF)
        POWBEN_LIST.append(POWBEN)
        PINTRSTR_LIST.append(PINTRSTR)
        PDIVD_LIST.append(PDIVD)
        PCHLDSP_LIST.append(PCHLDSP)
        PINCOT_LIST.append(PINCOT)
        PSSAPL_LIST.append(PSSAPL)
        PSDAPL_LIST.append(PSDAPL)
        TANFMYR_LIST.append(TANFMYR)
        ELIGPWIC_LIST.append(ELIGPWIC)
        PWIC_LIST.append(PWIC)
        WIC_FLAG_LIST.append(WIC_FLAG)
        ENGLANG_LIST.append(ENGLANG)

df = pd.DataFrame(columns=(
                            'RECTYPE',
                            'SRVY_YR',
                            'HHX',
                            'INTV_QRT',
                            'INTV_MON',
                            'FMX',
                            'FPX',
                            'WTIA',
                            'WTFA',
                            'REGION',
                            'STRAT_P',
                            'PSU_P',
                            'SEX',
                            'ORIGIN_I',
                            'ORIGIMPT',
                            'HISPAN_I',
                            'HISPIMPT',
                            'RACERPI2',
                            'RACEIMP2',
                            'MRACRPI2',
                            'MRACBPI2',
                            'RACRECI3',
                            'HISCODI3',
                            'ERIMPFLG',
                            'NOWAF',
                            'RRP',
                            'HHREFLG',
                            'FRRP',
                            'DOB_M',
                            'DOB_Y_P',
                            'AGE_P',
                            'AGE_CHG',
                            'FMRPFLG',
                            'FMREFLG',
                            'R_MARITL',
                            'FSPOUS2',
                            'COHAB1',
                            'COHAB2',
                            'FCOHAB3',
                            'CDCMSTAT',
                            'SIB_DEGP',
                            'FMOTHER1',
                            'MOM_DEGP',
                            'FFATHER1',
                            'DAD_DEGP',
                            'PARENTS',
                            'MOM_ED',
                            'DAD_ED',
                            'ASTATFLG',
                            'CSTATFLG',
                            'QCADULT',
                            'QCCHILD',
                            'FDRN_FLG',
                            'PLAPLYLM',
                            'PLAPLYUN',
                            'PSPEDEIS',
                            'PSPEDEM',
                            'PLAADL',
                            'LABATH',
                            'LADRESS',
                            'LAEAT',
                            'LABED',
                            'LATOILT',
                            'LAHOME',
                            'PLAIADL',
                            'PLAWKNOW',
                            'PLAWKLIM',
                            'PLAWALK',
                            'PLAREMEM',
                            'PLIMANY',
                            'LA1AR',
                            'LAHCC1',
                            'LAHCC2',
                            'LAHCC3',
                            'LAHCC4',
                            'LAHCC5',
                            'LAHCC6',
                            'LAHCC7A',
                            'LAHCC8',
                            'LAHCC9',
                            'LAHCC10',
                            'LAHCC11',
                            'LAHCC12',
                            'LAHCC13',
                            'LAHCC90',
                            'LAHCC91',
                            'LCTIME1',
                            'LCUNIT1',
                            'LCDURA1',
                            'LCDURB1',
                            'LCCHRC1',
                            'LCTIME2',
                            'LCUNIT2',
                            'LCDURA2',
                            'LCDURB2',
                            'LCCHRC2',
                            'LCTIME3',
                            'LCUNIT3',
                            'LCDURA3',
                            'LCDURB3',
                            'LCCHRC3',
                            'LCTIME4',
                            'LCUNIT4',
                            'LCDURA4',
                            'LCDURB4',
                            'LCCHRC4',
                            'LCTIME5',
                            'LCUNIT5',
                            'LCDURA5',
                            'LCDURB5',
                            'LCCHRC5',
                            'LCTIME6',
                            'LCUNIT6',
                            'LCDURA6',
                            'LCDURB6',
                            'LCCHRC6',
                            'LCTIME7A',
                            'LCUNIT7A',
                            'LCDURA7A',
                            'LCDURB7A',
                            'LCCHRC7A',
                            'LCTIME8',
                            'LCUNIT8',
                            'LCDURA8',
                            'LCDURB8',
                            'LCCHRC8',
                            'LCTIME9',
                            'LCUNIT9',
                            'LCDURA9',
                            'LCDURB9',
                            'LCCHRC9',
                            'LCTIME10',
                            'LCUNIT10',
                            'LCDURA10',
                            'LCDURB10',
                            'LCCHRC10',
                            'LCTIME11',
                            'LCUNIT11',
                            'LCDURA11',
                            'LCDURB11',
                            'LCCHRC11',
                            'LCTIME12',
                            'LCUNIT12',
                            'LCDURA12',
                            'LCDURB12',
                            'LCCHRC12',
                            'LCTIME13',
                            'LCUNIT13',
                            'LCDURA13',
                            'LCDURB13',
                            'LCCHRC13',
                            'LCTIME90',
                            'LCUNIT90',
                            'LCDURA90',
                            'LCDURB90',
                            'LCCHRC90',
                            'LCTIME91',
                            'LCUNIT91',
                            'LCDURA91',
                            'LCDURB91',
                            'LCCHRC91',
                            'LAHCA1',
                            'LAHCA2',
                            'LAHCA3',
                            'LAHCA4',
                            'LAHCA5',
                            'LAHCA6',
                            'LAHCA7',
                            'LAHCA8',
                            'LAHCA9',
                            'LAHCA10',
                            'LAHCA11',
                            'LAHCA12',
                            'LAHCA13',
                            'LAHCA14A',
                            'LAHCA15',
                            'LAHCA16',
                            'LAHCA17',
                            'LAHCA18',
                            'LAHCA19_',
                            'LAHCA20_',
                            'LAHCA21_',
                            'LAHCA22_',
                            'LAHCA23_',
                            'LAHCA24_',
                            'LAHCA25_',
                            'LAHCA26_',
                            'LAHCA27_',
                            'LAHCA28_',
                            'LAHCA29_',
                            'LAHCA30_',
                            'LAHCA31_',
                            'LAHCA32_',
                            'LAHCA33_',
                            'LAHCA34_',
                            'LAHCA90',
                            'LAHCA91',
                            'LATIME1',
                            'LAUNIT1',
                            'LADURA1',
                            'LADURB1',
                            'LACHRC1',
                            'LATIME2',
                            'LAUNIT2',
                            'LADURA2',
                            'LADURB2',
                            'LACHRC2',
                            'LATIME3',
                            'LAUNIT3',
                            'LADURA3',
                            'LADURB3',
                            'LACHRC3',
                            'LATIME4',
                            'LAUNIT4',
                            'LADURA4',
                            'LADURB4',
                            'LACHRC4',
                            'LATIME5',
                            'LAUNIT5',
                            'LADURA5',
                            'LADURB5',
                            'LACHRC5',
                            'LATIME6',
                            'LAUNIT6',
                            'LADURA6',
                            'LADURB6',
                            'LACHRC6',
                            'LATIME7',
                            'LAUNIT7',
                            'LADURA7',
                            'LADURB7',
                            'LACHRC7',
                            'LATIME8',
                            'LAUNIT8',
                            'LADURA8',
                            'LADURB8',
                            'LACHRC8',
                            'LATIME9',
                            'LAUNIT9',
                            'LADURA9',
                            'LADURB9',
                            'LACHRC9',
                            'LATIME10',
                            'LAUNIT10',
                            'LADURA10',
                            'LADURB10',
                            'LACHRC10',
                            'LATIME11',
                            'LAUNIT11',
                            'LADURA11',
                            'LADURB11',
                            'LACHRC11',
                            'LATIME12',
                            'LAUNIT12',
                            'LADURA12',
                            'LADURB12',
                            'LACHRC12',
                            'LATIME13',
                            'LAUNIT13',
                            'LADURA13',
                            'LADURB13',
                            'LACHRC13',
                            'LTIME14A',
                            'LUNIT14A',
                            'LDURA14A',
                            'LDURB14A',
                            'LCHRC14A',
                            'LATIME15',
                            'LAUNIT15',
                            'LADURA15',
                            'LADURB15',
                            'LACHRC15',
                            'LATIME16',
                            'LAUNIT16',
                            'LADURA16',
                            'LADURB16',
                            'LACHRC16',
                            'LATIME17',
                            'LAUNIT17',
                            'LADURA17',
                            'LADURB17',
                            'LACHRC17',
                            'LATIME18',
                            'LAUNIT18',
                            'LADURA18',
                            'LADURB18',
                            'LACHRC18',
                            'LATIME19',
                            'LAUNIT19',
                            'LADURA19',
                            'LADURB19',
                            'LACHRC19',
                            'LATIME20',
                            'LAUNIT20',
                            'LADURA20',
                            'LADURB20',
                            'LACHRC20',
                            'LATIME21',
                            'LAUNIT21',
                            'LADURA21',
                            'LADURB21',
                            'LACHRC21',
                            'LATIME22',
                            'LAUNIT22',
                            'LADURA22',
                            'LADURB22',
                            'LACHRC22',
                            'LATIME23',
                            'LAUNIT23',
                            'LADURA23',
                            'LADURB23',
                            'LACHRC23',
                            'LATIME24',
                            'LAUNIT24',
                            'LADURA24',
                            'LADURB24',
                            'LACHRC24',
                            'LATIME25',
                            'LAUNIT25',
                            'LADURA25',
                            'LADURB25',
                            'LACHRC25',
                            'LATIME26',
                            'LAUNIT26',
                            'LADURA26',
                            'LADURB26',
                            'LACHRC26',
                            'LATIME27',
                            'LAUNIT27',
                            'LADURA27',
                            'LADURB27',
                            'LACHRC27',
                            'LATIME28',
                            'LAUNIT28',
                            'LADURA28',
                            'LADURB28',
                            'LACHRC28',
                            'LATIME29',
                            'LAUNIT29',
                            'LADURA29',
                            'LADURB29',
                            'LACHRC29',
                            'LATIME30',
                            'LAUNIT30',
                            'LADURA30',
                            'LADURB30',
                            'LACHRC30',
                            'LATIME31',
                            'LAUNIT31',
                            'LADURA31',
                            'LADURB31',
                            'LACHRC31',
                            'LATIME32',
                            'LAUNIT32',
                            'LADURA32',
                            'LADURB32',
                            'LACHRC32',
                            'LATIME33',
                            'LAUNIT33',
                            'LADURA33',
                            'LADURB33',
                            'LACHRC33',
                            'LATIME34',
                            'LAUNIT34',
                            'LADURA34',
                            'LADURB34',
                            'LACHRC34',
                            'LATIME90',
                            'LAUNIT90',
                            'LADURA90',
                            'LADURB90',
                            'LACHRC90',
                            'LATIME91',
                            'LAUNIT91',
                            'LADURA91',
                            'LADURB91',
                            'LACHRC91',
                            'LCONDRT',
                            'LACHRONR',
                            'PHSTAT',
                            'PDMED12M',
                            'PNMED12M',
                            'PHOSPYR2',
                            'HOSPNO',
                            'HPNITE',
                            'PHCHM2W',
                            'PHCHMN2W',
                            'PHCPH2WR',
                            'PHCPHN2W',
                            'PHCDV2W',
                            'PHCDVN2W',
                            'P10DVYR',
                            'NOTCOV',
                            'MEDICARE',
                            'MCPART',
                            'MCCHOICE',
                            'MCHMO',
                            'MCADVR',
                            'MCPREM',
                            'MCREF',
                            'MCPARTD',
                            'MEDICAID',
                            'MAFLG',
                            'MACHMD',
                            'MXCHNG',
                            'MEDPREM',
                            'MDPRINC',
                            'MAPCMD',
                            'MAREF',
                            'SINGLE',
                            'SSTYPEA',
                            'SSTYPEB',
                            'SSTYPEC',
                            'SSTYPED',
                            'SSTYPEE',
                            'SSTYPEF',
                            'SSTYPEG',
                            'SSTYPEH',
                            'SSTYPEI',
                            'SSTYPEJ',
                            'SSTYPEK',
                            'SSTYPEL',
                            'PRIVATE',
                            'PRFLG',
                            'EXCHANGE',
                            'WHONAM1',
                            'PRPOLH1',
                            'PRCOOH1',
                            'PRCTOH1',
                            'PRRLOH11',
                            'PRRLOH21',
                            'PRRLOH31',
                            'PRRLOH41',
                            'PRCNUM1',
                            'COHU191',
                            'COH19251',
                            'COHO251',
                            'PLNWRKR1',
                            'PLNEXCH1',
                            'EXCHPR1',
                            'PLNPAY11',
                            'PLNPAY21',
                            'PLNPAY31',
                            'PLNPAY41',
                            'PLNPAY51',
                            'PLNPAY61',
                            'PLNPAY71',
                            'PLNPRE1',
                            'HICOSTR1',
                            'EMPPAY1',
                            'ECOSTR1',
                            'EMPCSTP1',
                            'PLNMGD1',
                            'HDHP1',
                            'HSAHRA1',
                            'MGCHMD1',
                            'MGPRMD1',
                            'MGPYMD1',
                            'MGPREF1',
                            'PCPREQ1',
                            'PRRXCOV1',
                            'PRDNCOV1',
                            'PXCHNG',
                            'PLEXCHPR',
                            'PSTRFPRM',
                            'PSSPRINC',
                            'PSTDOC',
                            'PSTCMD',
                            'PSTREF',
                            'WHONAM2',
                            'PRPOLH2',
                            'PRCOOH2',
                            'PRCTOH2',
                            'PRRLOH12',
                            'PRRLOH22',
                            'PRRLOH32',
                            'PRRLOH42',
                            'PRCNUM2',
                            'COHU192',
                            'COH19252',
                            'COHO252',
                            'PLNWRKR2',
                            'PLNEXCH2',
                            'EXCHPR2',
                            'PLNPAY12',
                            'PLNPAY22',
                            'PLNPAY32',
                            'PLNPAY42',
                            'PLNPAY52',
                            'PLNPAY62',
                            'PLNPAY72',
                            'PLNPRE2',
                            'HICOSTR2',
                            'EMPPAY2',
                            'ECOSTR2',
                            'EMPCSTP2',
                            'PLNMGD2',
                            'HDHP2',
                            'HSAHRA2',
                            'MGCHMD2',
                            'MGPRMD2',
                            'MGPYMD2',
                            'MGPREF2',
                            'PCPREQ2',
                            'PRRXCOV2',
                            'PRDNCOV2',
                            'PRPLPLUS',
                            'FCOVCONF',
                            'SCHIP',
                            'CHFLG',
                            'CHXCHNG',
                            'STRFPRM1',
                            'CHPRINC',
                            'STDOC1',
                            'STPCMD1',
                            'STREF1',
                            'OTHPUB',
                            'OPFLG',
                            'OPXCHNG',
                            'PLEXCHOP',
                            'STRFPRM2',
                            'SSPRINC',
                            'STDOC2',
                            'STPCMD2',
                            'STREF2',
                            'OTHGOV',
                            'OGFLG',
                            'OGXCHNG',
                            'PLEXCHOG',
                            'STRFPRM3',
                            'OGPRINC',
                            'STDOC3',
                            'STPCMD3',
                            'STREF3',
                            'MILCARE',
                            'MILSPC1',
                            'MILSPC2',
                            'MILSPC3',
                            'MILSPC4',
                            'MILMAN',
                            'IHS',
                            'HILAST',
                            'HISTOP1',
                            'HISTOP2',
                            'HISTOP3',
                            'HISTOP4',
                            'HISTOP5',
                            'HISTOP6',
                            'HISTOP7',
                            'HISTOP8',
                            'HISTOP9',
                            'HISTOP10',
                            'HISTOP11',
                            'HISTOP12',
                            'HISTOP13',
                            'HISTOP14',
                            'HISTOP15',
                            'HINOTYR',
                            'HINOTMYR',
                            'FHICHNG',
                            'FHIKDBA',
                            'FHIKDBB',
                            'FHIKDBC',
                            'FHIKDBD',
                            'FHIKDBE',
                            'FHIKDBF',
                            'FHIKDBG',
                            'FHIKDBH',
                            'FHIKDBI',
                            'FHIKDBJ',
                            'FHIKDBK',
                            'PWRKBR1',
                            'HCSPFYR',
                            'MEDBILL',
                            'MEDBPAY',
                            'MEDBNOP',
                            'FSA',
                            'HIKINDNA',
                            'HIKINDNB',
                            'HIKINDNC',
                            'HIKINDND',
                            'HIKINDNE',
                            'HIKINDNF',
                            'HIKINDNG',
                            'HIKINDNH',
                            'HIKINDNI',
                            'HIKINDNJ',
                            'HIKINDNK',
                            'MCAREPRB',
                            'MCAIDPRB',
                            'SINCOV',
                            'PLBORN',
                            'REGIONBR',
                            'GEOBRTH',
                            'YRSINUS',
                            'CITIZENP',
                            'HEADST',
                            'HEADSTV1',
                            'EDUC1',
                            'ARMFVER',
                            'ARMFEV',
                            'ARMFFC',
                            'ARMFTM1P',
                            'ARMFTM2P',
                            'ARMFTM3P',
                            'ARMFTM4P',
                            'ARMFTM5P',
                            'ARMFTM6P',
                            'ARMFTM7P',
                            'ARMFDS2P',
                            'DOINGLWP',
                            'WHYNOWKP',
                            'WRKHRS2',
                            'WRKFTALL',
                            'WRKLYR1',
                            'WRKMYR',
                            'ERNYR_P',
                            'HIEMPOF',
                            'FINCINT',
                            'PSAL',
                            'PSEINC',
                            'PSSRR',
                            'PSSRRDB',
                            'PSSRRD',
                            'PPENS',
                            'POPENS',
                            'PSSI',
                            'PSSID',
                            'PTANF',
                            'POWBEN',
                            'PINTRSTR',
                            'PDIVD',
                            'PCHLDSP',
                            'PINCOT',
                            'PSSAPL',
                            'PSDAPL',
                            'TANFMYR',
                            'ELIGPWIC',
                            'PWIC',
                            'WIC_FLAG',
                            'ENGLANG'
                                    ))

for i in range(112052):
    df.loc[i] = [
                    RECTYPE_LIST[i],
                    SRVY_YR_LIST[i],
                    HHX_LIST[i],
                    INTV_QRT_LIST[i],
                    INTV_MON_LIST[i],
                    FMX_LIST[i],
                    FPX_LIST[i],
                    WTIA_LIST[i],
                    WTFA_LIST[i],
                    REGION_LIST[i],
                    STRAT_P_LIST[i],
                    PSU_P_LIST[i],
                    SEX_LIST[i],
                    ORIGIN_I_LIST[i],
                    ORIGIMPT_LIST[i],
                    HISPAN_I_LIST[i],
                    HISPIMPT_LIST[i],
                    RACERPI2_LIST[i],
                    RACEIMP2_LIST[i],
                    MRACRPI2_LIST[i],
                    MRACBPI2_LIST[i],
                    RACRECI3_LIST[i],
                    HISCODI3_LIST[i],
                    ERIMPFLG_LIST[i],
                    NOWAF_LIST[i],
                    RRP_LIST[i],
                    HHREFLG_LIST[i],
                    FRRP_LIST[i],
                    DOB_M_LIST[i],
                    DOB_Y_P_LIST[i],
                    AGE_P_LIST[i],
                    AGE_CHG_LIST[i],
                    FMRPFLG_LIST[i],
                    FMREFLG_LIST[i],
                    R_MARITL_LIST[i],
                    FSPOUS2_LIST[i],
                    COHAB1_LIST[i],
                    COHAB2_LIST[i],
                    FCOHAB3_LIST[i],
                    CDCMSTAT_LIST[i],
                    SIB_DEGP_LIST[i],
                    FMOTHER1_LIST[i],
                    MOM_DEGP_LIST[i],
                    FFATHER1_LIST[i],
                    DAD_DEGP_LIST[i],
                    PARENTS_LIST[i],
                    MOM_ED_LIST[i],
                    DAD_ED_LIST[i],
                    ASTATFLG_LIST[i],
                    CSTATFLG_LIST[i],
                    QCADULT_LIST[i],
                    QCCHILD_LIST[i],
                    FDRN_FLG_LIST[i],
                    PLAPLYLM_LIST[i],
                    PLAPLYUN_LIST[i],
                    PSPEDEIS_LIST[i],
                    PSPEDEM_LIST[i],
                    PLAADL_LIST[i],
                    LABATH_LIST[i],
                    LADRESS_LIST[i],
                    LAEAT_LIST[i],
                    LABED_LIST[i],
                    LATOILT_LIST[i],
                    LAHOME_LIST[i],
                    PLAIADL_LIST[i],
                    PLAWKNOW_LIST[i],
                    PLAWKLIM_LIST[i],
                    PLAWALK_LIST[i],
                    PLAREMEM_LIST[i],
                    PLIMANY_LIST[i],
                    LA1AR_LIST[i],
                    LAHCC1_LIST[i],
                    LAHCC2_LIST[i],
                    LAHCC3_LIST[i],
                    LAHCC4_LIST[i],
                    LAHCC5_LIST[i],
                    LAHCC6_LIST[i],
                    LAHCC7A_LIST[i],
                    LAHCC8_LIST[i],
                    LAHCC9_LIST[i],
                    LAHCC10_LIST[i],
                    LAHCC11_LIST[i],
                    LAHCC12_LIST[i],
                    LAHCC13_LIST[i],
                    LAHCC90_LIST[i],
                    LAHCC91_LIST[i],
                    LCTIME1_LIST[i],
                    LCUNIT1_LIST[i],
                    LCDURA1_LIST[i],
                    LCDURB1_LIST[i],
                    LCCHRC1_LIST[i],
                    LCTIME2_LIST[i],
                    LCUNIT2_LIST[i],
                    LCDURA2_LIST[i],
                    LCDURB2_LIST[i],
                    LCCHRC2_LIST[i],
                    LCTIME3_LIST[i],
                    LCUNIT3_LIST[i],
                    LCDURA3_LIST[i],
                    LCDURB3_LIST[i],
                    LCCHRC3_LIST[i],
                    LCTIME4_LIST[i],
                    LCUNIT4_LIST[i],
                    LCDURA4_LIST[i],
                    LCDURB4_LIST[i],
                    LCCHRC4_LIST[i],
                    LCTIME5_LIST[i],
                    LCUNIT5_LIST[i],
                    LCDURA5_LIST[i],
                    LCDURB5_LIST[i],
                    LCCHRC5_LIST[i],
                    LCTIME6_LIST[i],
                    LCUNIT6_LIST[i],
                    LCDURA6_LIST[i],
                    LCDURB6_LIST[i],
                    LCCHRC6_LIST[i],
                    LCTIME7A_LIST[i],
                    LCUNIT7A_LIST[i],
                    LCDURA7A_LIST[i],
                    LCDURB7A_LIST[i],
                    LCCHRC7A_LIST[i],
                    LCTIME8_LIST[i],
                    LCUNIT8_LIST[i],
                    LCDURA8_LIST[i],
                    LCDURB8_LIST[i],
                    LCCHRC8_LIST[i],
                    LCTIME9_LIST[i],
                    LCUNIT9_LIST[i],
                    LCDURA9_LIST[i],
                    LCDURB9_LIST[i],
                    LCCHRC9_LIST[i],
                    LCTIME10_LIST[i],
                    LCUNIT10_LIST[i],
                    LCDURA10_LIST[i],
                    LCDURB10_LIST[i],
                    LCCHRC10_LIST[i],
                    LCTIME11_LIST[i],
                    LCUNIT11_LIST[i],
                    LCDURA11_LIST[i],
                    LCDURB11_LIST[i],
                    LCCHRC11_LIST[i],
                    LCTIME12_LIST[i],
                    LCUNIT12_LIST[i],
                    LCDURA12_LIST[i],
                    LCDURB12_LIST[i],
                    LCCHRC12_LIST[i],
                    LCTIME13_LIST[i],
                    LCUNIT13_LIST[i],
                    LCDURA13_LIST[i],
                    LCDURB13_LIST[i],
                    LCCHRC13_LIST[i],
                    LCTIME90_LIST[i],
                    LCUNIT90_LIST[i],
                    LCDURA90_LIST[i],
                    LCDURB90_LIST[i],
                    LCCHRC90_LIST[i],
                    LCTIME91_LIST[i],
                    LCUNIT91_LIST[i],
                    LCDURA91_LIST[i],
                    LCDURB91_LIST[i],
                    LCCHRC91_LIST[i],
                    LAHCA1_LIST[i],
                    LAHCA2_LIST[i],
                    LAHCA3_LIST[i],
                    LAHCA4_LIST[i],
                    LAHCA5_LIST[i],
                    LAHCA6_LIST[i],
                    LAHCA7_LIST[i],
                    LAHCA8_LIST[i],
                    LAHCA9_LIST[i],
                    LAHCA10_LIST[i],
                    LAHCA11_LIST[i],
                    LAHCA12_LIST[i],
                    LAHCA13_LIST[i],
                    LAHCA14A_LIST[i],
                    LAHCA15_LIST[i],
                    LAHCA16_LIST[i],
                    LAHCA17_LIST[i],
                    LAHCA18_LIST[i],
                    LAHCA19__LIST[i],
                    LAHCA20__LIST[i],
                    LAHCA21__LIST[i],
                    LAHCA22__LIST[i],
                    LAHCA23__LIST[i],
                    LAHCA24__LIST[i],
                    LAHCA25__LIST[i],
                    LAHCA26__LIST[i],
                    LAHCA27__LIST[i],
                    LAHCA28__LIST[i],
                    LAHCA29__LIST[i],
                    LAHCA30__LIST[i],
                    LAHCA31__LIST[i],
                    LAHCA32__LIST[i],
                    LAHCA33__LIST[i],
                    LAHCA34__LIST[i],
                    LAHCA90_LIST[i],
                    LAHCA91_LIST[i],
                    LATIME1_LIST[i],
                    LAUNIT1_LIST[i],
                    LADURA1_LIST[i],
                    LADURB1_LIST[i],
                    LACHRC1_LIST[i],
                    LATIME2_LIST[i],
                    LAUNIT2_LIST[i],
                    LADURA2_LIST[i],
                    LADURB2_LIST[i],
                    LACHRC2_LIST[i],
                    LATIME3_LIST[i],
                    LAUNIT3_LIST[i],
                    LADURA3_LIST[i],
                    LADURB3_LIST[i],
                    LACHRC3_LIST[i],
                    LATIME4_LIST[i],
                    LAUNIT4_LIST[i],
                    LADURA4_LIST[i],
                    LADURB4_LIST[i],
                    LACHRC4_LIST[i],
                    LATIME5_LIST[i],
                    LAUNIT5_LIST[i],
                    LADURA5_LIST[i],
                    LADURB5_LIST[i],
                    LACHRC5_LIST[i],
                    LATIME6_LIST[i],
                    LAUNIT6_LIST[i],
                    LADURA6_LIST[i],
                    LADURB6_LIST[i],
                    LACHRC6_LIST[i],
                    LATIME7_LIST[i],
                    LAUNIT7_LIST[i],
                    LADURA7_LIST[i],
                    LADURB7_LIST[i],
                    LACHRC7_LIST[i],
                    LATIME8_LIST[i],
                    LAUNIT8_LIST[i],
                    LADURA8_LIST[i],
                    LADURB8_LIST[i],
                    LACHRC8_LIST[i],
                    LATIME9_LIST[i],
                    LAUNIT9_LIST[i],
                    LADURA9_LIST[i],
                    LADURB9_LIST[i],
                    LACHRC9_LIST[i],
                    LATIME10_LIST[i],
                    LAUNIT10_LIST[i],
                    LADURA10_LIST[i],
                    LADURB10_LIST[i],
                    LACHRC10_LIST[i],
                    LATIME11_LIST[i],
                    LAUNIT11_LIST[i],
                    LADURA11_LIST[i],
                    LADURB11_LIST[i],
                    LACHRC11_LIST[i],
                    LATIME12_LIST[i],
                    LAUNIT12_LIST[i],
                    LADURA12_LIST[i],
                    LADURB12_LIST[i],
                    LACHRC12_LIST[i],
                    LATIME13_LIST[i],
                    LAUNIT13_LIST[i],
                    LADURA13_LIST[i],
                    LADURB13_LIST[i],
                    LACHRC13_LIST[i],
                    LTIME14A_LIST[i],
                    LUNIT14A_LIST[i],
                    LDURA14A_LIST[i],
                    LDURB14A_LIST[i],
                    LCHRC14A_LIST[i],
                    LATIME15_LIST[i],
                    LAUNIT15_LIST[i],
                    LADURA15_LIST[i],
                    LADURB15_LIST[i],
                    LACHRC15_LIST[i],
                    LATIME16_LIST[i],
                    LAUNIT16_LIST[i],
                    LADURA16_LIST[i],
                    LADURB16_LIST[i],
                    LACHRC16_LIST[i],
                    LATIME17_LIST[i],
                    LAUNIT17_LIST[i],
                    LADURA17_LIST[i],
                    LADURB17_LIST[i],
                    LACHRC17_LIST[i],
                    LATIME18_LIST[i],
                    LAUNIT18_LIST[i],
                    LADURA18_LIST[i],
                    LADURB18_LIST[i],
                    LACHRC18_LIST[i],
                    LATIME19_LIST[i],
                    LAUNIT19_LIST[i],
                    LADURA19_LIST[i],
                    LADURB19_LIST[i],
                    LACHRC19_LIST[i],
                    LATIME20_LIST[i],
                    LAUNIT20_LIST[i],
                    LADURA20_LIST[i],
                    LADURB20_LIST[i],
                    LACHRC20_LIST[i],
                    LATIME21_LIST[i],
                    LAUNIT21_LIST[i],
                    LADURA21_LIST[i],
                    LADURB21_LIST[i],
                    LACHRC21_LIST[i],
                    LATIME22_LIST[i],
                    LAUNIT22_LIST[i],
                    LADURA22_LIST[i],
                    LADURB22_LIST[i],
                    LACHRC22_LIST[i],
                    LATIME23_LIST[i],
                    LAUNIT23_LIST[i],
                    LADURA23_LIST[i],
                    LADURB23_LIST[i],
                    LACHRC23_LIST[i],
                    LATIME24_LIST[i],
                    LAUNIT24_LIST[i],
                    LADURA24_LIST[i],
                    LADURB24_LIST[i],
                    LACHRC24_LIST[i],
                    LATIME25_LIST[i],
                    LAUNIT25_LIST[i],
                    LADURA25_LIST[i],
                    LADURB25_LIST[i],
                    LACHRC25_LIST[i],
                    LATIME26_LIST[i],
                    LAUNIT26_LIST[i],
                    LADURA26_LIST[i],
                    LADURB26_LIST[i],
                    LACHRC26_LIST[i],
                    LATIME27_LIST[i],
                    LAUNIT27_LIST[i],
                    LADURA27_LIST[i],
                    LADURB27_LIST[i],
                    LACHRC27_LIST[i],
                    LATIME28_LIST[i],
                    LAUNIT28_LIST[i],
                    LADURA28_LIST[i],
                    LADURB28_LIST[i],
                    LACHRC28_LIST[i],
                    LATIME29_LIST[i],
                    LAUNIT29_LIST[i],
                    LADURA29_LIST[i],
                    LADURB29_LIST[i],
                    LACHRC29_LIST[i],
                    LATIME30_LIST[i],
                    LAUNIT30_LIST[i],
                    LADURA30_LIST[i],
                    LADURB30_LIST[i],
                    LACHRC30_LIST[i],
                    LATIME31_LIST[i],
                    LAUNIT31_LIST[i],
                    LADURA31_LIST[i],
                    LADURB31_LIST[i],
                    LACHRC31_LIST[i],
                    LATIME32_LIST[i],
                    LAUNIT32_LIST[i],
                    LADURA32_LIST[i],
                    LADURB32_LIST[i],
                    LACHRC32_LIST[i],
                    LATIME33_LIST[i],
                    LAUNIT33_LIST[i],
                    LADURA33_LIST[i],
                    LADURB33_LIST[i],
                    LACHRC33_LIST[i],
                    LATIME34_LIST[i],
                    LAUNIT34_LIST[i],
                    LADURA34_LIST[i],
                    LADURB34_LIST[i],
                    LACHRC34_LIST[i],
                    LATIME90_LIST[i],
                    LAUNIT90_LIST[i],
                    LADURA90_LIST[i],
                    LADURB90_LIST[i],
                    LACHRC90_LIST[i],
                    LATIME91_LIST[i],
                    LAUNIT91_LIST[i],
                    LADURA91_LIST[i],
                    LADURB91_LIST[i],
                    LACHRC91_LIST[i],
                    LCONDRT_LIST[i],
                    LACHRONR_LIST[i],
                    PHSTAT_LIST[i],
                    PDMED12M_LIST[i],
                    PNMED12M_LIST[i],
                    PHOSPYR2_LIST[i],
                    HOSPNO_LIST[i],
                    HPNITE_LIST[i],
                    PHCHM2W_LIST[i],
                    PHCHMN2W_LIST[i],
                    PHCPH2WR_LIST[i],
                    PHCPHN2W_LIST[i],
                    PHCDV2W_LIST[i],
                    PHCDVN2W_LIST[i],
                    P10DVYR_LIST[i],
                    NOTCOV_LIST[i],
                    MEDICARE_LIST[i],
                    MCPART_LIST[i],
                    MCCHOICE_LIST[i],
                    MCHMO_LIST[i],
                    MCADVR_LIST[i],
                    MCPREM_LIST[i],
                    MCREF_LIST[i],
                    MCPARTD_LIST[i],
                    MEDICAID_LIST[i],
                    MAFLG_LIST[i],
                    MACHMD_LIST[i],
                    MXCHNG_LIST[i],
                    MEDPREM_LIST[i],
                    MDPRINC_LIST[i],
                    MAPCMD_LIST[i],
                    MAREF_LIST[i],
                    SINGLE_LIST[i],
                    SSTYPEA_LIST[i],
                    SSTYPEB_LIST[i],
                    SSTYPEC_LIST[i],
                    SSTYPED_LIST[i],
                    SSTYPEE_LIST[i],
                    SSTYPEF_LIST[i],
                    SSTYPEG_LIST[i],
                    SSTYPEH_LIST[i],
                    SSTYPEI_LIST[i],
                    SSTYPEJ_LIST[i],
                    SSTYPEK_LIST[i],
                    SSTYPEL_LIST[i],
                    PRIVATE_LIST[i],
                    PRFLG_LIST[i],
                    EXCHANGE_LIST[i],
                    WHONAM1_LIST[i],
                    PRPOLH1_LIST[i],
                    PRCOOH1_LIST[i],
                    PRCTOH1_LIST[i],
                    PRRLOH11_LIST[i],
                    PRRLOH21_LIST[i],
                    PRRLOH31_LIST[i],
                    PRRLOH41_LIST[i],
                    PRCNUM1_LIST[i],
                    COHU191_LIST[i],
                    COH19251_LIST[i],
                    COHO251_LIST[i],
                    PLNWRKR1_LIST[i],
                    PLNEXCH1_LIST[i],
                    EXCHPR1_LIST[i],
                    PLNPAY11_LIST[i],
                    PLNPAY21_LIST[i],
                    PLNPAY31_LIST[i],
                    PLNPAY41_LIST[i],
                    PLNPAY51_LIST[i],
                    PLNPAY61_LIST[i],
                    PLNPAY71_LIST[i],
                    PLNPRE1_LIST[i],
                    HICOSTR1_LIST[i],
                    EMPPAY1_LIST[i],
                    ECOSTR1_LIST[i],
                    EMPCSTP1_LIST[i],
                    PLNMGD1_LIST[i],
                    HDHP1_LIST[i],
                    HSAHRA1_LIST[i],
                    MGCHMD1_LIST[i],
                    MGPRMD1_LIST[i],
                    MGPYMD1_LIST[i],
                    MGPREF1_LIST[i],
                    PCPREQ1_LIST[i],
                    PRRXCOV1_LIST[i],
                    PRDNCOV1_LIST[i],
                    PXCHNG_LIST[i],
                    PLEXCHPR_LIST[i],
                    PSTRFPRM_LIST[i],
                    PSSPRINC_LIST[i],
                    PSTDOC_LIST[i],
                    PSTCMD_LIST[i],
                    PSTREF_LIST[i],
                    WHONAM2_LIST[i],
                    PRPOLH2_LIST[i],
                    PRCOOH2_LIST[i],
                    PRCTOH2_LIST[i],
                    PRRLOH12_LIST[i],
                    PRRLOH22_LIST[i],
                    PRRLOH32_LIST[i],
                    PRRLOH42_LIST[i],
                    PRCNUM2_LIST[i],
                    COHU192_LIST[i],
                    COH19252_LIST[i],
                    COHO252_LIST[i],
                    PLNWRKR2_LIST[i],
                    PLNEXCH2_LIST[i],
                    EXCHPR2_LIST[i],
                    PLNPAY12_LIST[i],
                    PLNPAY22_LIST[i],
                    PLNPAY32_LIST[i],
                    PLNPAY42_LIST[i],
                    PLNPAY52_LIST[i],
                    PLNPAY62_LIST[i],
                    PLNPAY72_LIST[i],
                    PLNPRE2_LIST[i],
                    HICOSTR2_LIST[i],
                    EMPPAY2_LIST[i],
                    ECOSTR2_LIST[i],
                    EMPCSTP2_LIST[i],
                    PLNMGD2_LIST[i],
                    HDHP2_LIST[i],
                    HSAHRA2_LIST[i],
                    MGCHMD2_LIST[i],
                    MGPRMD2_LIST[i],
                    MGPYMD2_LIST[i],
                    MGPREF2_LIST[i],
                    PCPREQ2_LIST[i],
                    PRRXCOV2_LIST[i],
                    PRDNCOV2_LIST[i],
                    PRPLPLUS_LIST[i],
                    FCOVCONF_LIST[i],
                    SCHIP_LIST[i],
                    CHFLG_LIST[i],
                    CHXCHNG_LIST[i],
                    STRFPRM1_LIST[i],
                    CHPRINC_LIST[i],
                    STDOC1_LIST[i],
                    STPCMD1_LIST[i],
                    STREF1_LIST[i],
                    OTHPUB_LIST[i],
                    OPFLG_LIST[i],
                    OPXCHNG_LIST[i],
                    PLEXCHOP_LIST[i],
                    STRFPRM2_LIST[i],
                    SSPRINC_LIST[i],
                    STDOC2_LIST[i],
                    STPCMD2_LIST[i],
                    STREF2_LIST[i],
                    OTHGOV_LIST[i],
                    OGFLG_LIST[i],
                    OGXCHNG_LIST[i],
                    PLEXCHOG_LIST[i],
                    STRFPRM3_LIST[i],
                    OGPRINC_LIST[i],
                    STDOC3_LIST[i],
                    STPCMD3_LIST[i],
                    STREF3_LIST[i],
                    MILCARE_LIST[i],
                    MILSPC1_LIST[i],
                    MILSPC2_LIST[i],
                    MILSPC3_LIST[i],
                    MILSPC4_LIST[i],
                    MILMAN_LIST[i],
                    IHS_LIST[i],
                    HILAST_LIST[i],
                    HISTOP1_LIST[i],
                    HISTOP2_LIST[i],
                    HISTOP3_LIST[i],
                    HISTOP4_LIST[i],
                    HISTOP5_LIST[i],
                    HISTOP6_LIST[i],
                    HISTOP7_LIST[i],
                    HISTOP8_LIST[i],
                    HISTOP9_LIST[i],
                    HISTOP10_LIST[i],
                    HISTOP11_LIST[i],
                    HISTOP12_LIST[i],
                    HISTOP13_LIST[i],
                    HISTOP14_LIST[i],
                    HISTOP15_LIST[i],
                    HINOTYR_LIST[i],
                    HINOTMYR_LIST[i],
                    FHICHNG_LIST[i],
                    FHIKDBA_LIST[i],
                    FHIKDBB_LIST[i],
                    FHIKDBC_LIST[i],
                    FHIKDBD_LIST[i],
                    FHIKDBE_LIST[i],
                    FHIKDBF_LIST[i],
                    FHIKDBG_LIST[i],
                    FHIKDBH_LIST[i],
                    FHIKDBI_LIST[i],
                    FHIKDBJ_LIST[i],
                    FHIKDBK_LIST[i],
                    PWRKBR1_LIST[i],
                    HCSPFYR_LIST[i],
                    MEDBILL_LIST[i],
                    MEDBPAY_LIST[i],
                    MEDBNOP_LIST[i],
                    FSA_LIST[i],
                    HIKINDNA_LIST[i],
                    HIKINDNB_LIST[i],
                    HIKINDNC_LIST[i],
                    HIKINDND_LIST[i],
                    HIKINDNE_LIST[i],
                    HIKINDNF_LIST[i],
                    HIKINDNG_LIST[i],
                    HIKINDNH_LIST[i],
                    HIKINDNI_LIST[i],
                    HIKINDNJ_LIST[i],
                    HIKINDNK_LIST[i],
                    MCAREPRB_LIST[i],
                    MCAIDPRB_LIST[i],
                    SINCOV_LIST[i],
                    PLBORN_LIST[i],
                    REGIONBR_LIST[i],
                    GEOBRTH_LIST[i],
                    YRSINUS_LIST[i],
                    CITIZENP_LIST[i],
                    HEADST_LIST[i],
                    HEADSTV1_LIST[i],
                    EDUC1_LIST[i],
                    ARMFVER_LIST[i],
                    ARMFEV_LIST[i],
                    ARMFFC_LIST[i],
                    ARMFTM1P_LIST[i],
                    ARMFTM2P_LIST[i],
                    ARMFTM3P_LIST[i],
                    ARMFTM4P_LIST[i],
                    ARMFTM5P_LIST[i],
                    ARMFTM6P_LIST[i],
                    ARMFTM7P_LIST[i],
                    ARMFDS2P_LIST[i],
                    DOINGLWP_LIST[i],
                    WHYNOWKP_LIST[i],
                    WRKHRS2_LIST[i],
                    WRKFTALL_LIST[i],
                    WRKLYR1_LIST[i],
                    WRKMYR_LIST[i],
                    ERNYR_P_LIST[i],
                    HIEMPOF_LIST[i],
                    FINCINT_LIST[i],
                    PSAL_LIST[i],
                    PSEINC_LIST[i],
                    PSSRR_LIST[i],
                    PSSRRDB_LIST[i],
                    PSSRRD_LIST[i],
                    PPENS_LIST[i],
                    POPENS_LIST[i],
                    PSSI_LIST[i],
                    PSSID_LIST[i],
                    PTANF_LIST[i],
                    POWBEN_LIST[i],
                    PINTRSTR_LIST[i],
                    PDIVD_LIST[i],
                    PCHLDSP_LIST[i],
                    PINCOT_LIST[i],
                    PSSAPL_LIST[i],
                    PSDAPL_LIST[i],
                    TANFMYR_LIST[i],
                    ELIGPWIC_LIST[i],
                    PWIC_LIST[i],
                    WIC_FLAG_LIST[i],
                    ENGLANG_LIST[i]
                                    ]
df = df.applymap(lambda x: np.nan if str(x).isspace() else x)
df.to_csv("nhis_2014_personsx.csv")
