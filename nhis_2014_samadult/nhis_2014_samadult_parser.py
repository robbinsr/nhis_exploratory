import pandas as pd
import numpy as np

input_data_FILE = "nhis_2014_samadult.dat"

RECTYPE = ''
SRVY_YR = ''
HHX = ''
INTV_QRT = ''
INTV_MON = ''
FMX = ''
FPX = ''
WTIA_SA = ''
WTFA_SA = ''
REGION = ''
STRAT_P = ''
PSU_P = ''
SEX = ''
HISPAN_I = ''
RACERPI2 = ''
MRACRPI2 = ''
MRACBPI2 = ''
AGE_P = ''
R_MARITL = ''
PROXYSA = ''
PROX1 = ''
PROX2 = ''
LATEINTA = ''
FDRN_FLG = ''
DOINGLWA = ''
WHYNOWKA = ''
EVERWRK = ''
INDSTRN1 = ''
INDSTRN2 = ''
OCCUPN1 = ''
OCCUPN2 = ''
WRKCATA = ''
BUSINC1A = ''
LOCALL1A = ''
YRSWRKPA = ''
WRKLONGH = ''
HOURPDA = ''
PDSICKA = ''
ONEJOB = ''
WRKLYR4 = ''
HYPEV = ''
HYPDIFV = ''
HYPYR1 = ''
HYBPCKNO = ''
HYBPCKTP = ''
HYBPLEV = ''
HYPMDEV2 = ''
HYPMED2 = ''
CHLEV = ''
CHLYR = ''
CLCKNO = ''
CLCKTP = ''
CHLMDEV2 = ''
CHLMDNW2 = ''
CHDEV = ''
ANGEV = ''
MIEV = ''
HRTEV = ''
STREV = ''
EPHEV = ''
JAWP = ''
WEA = ''
CHE = ''
ARM = ''
BRTH = ''
AHADO = ''
FACE = ''
SPEAKING = ''
EYE = ''
WALKING = ''
HEADACHE = ''
ASTDO = ''
COPDEV = ''
ASPMEDEV = ''
ASPMEDAD = ''
ASPMDMED = ''
ASPONOWN = ''
AASMEV = ''
AASSTILL = ''
AASMYR = ''
AASERYR1 = ''
ULCEV = ''
ULCYR = ''
CANEV = ''
CNKIND1 = ''
CNKIND2 = ''
CNKIND3 = ''
CNKIND4 = ''
CNKIND5 = ''
CNKIND6 = ''
CNKIND7 = ''
CNKIND8 = ''
CNKIND9 = ''
CNKIND10 = ''
CNKIND11 = ''
CNKIND12 = ''
CNKIND13 = ''
CNKIND14 = ''
CNKIND15 = ''
CNKIND16 = ''
CNKIND17 = ''
CNKIND18 = ''
CNKIND19 = ''
CNKIND20 = ''
CNKIND21 = ''
CNKIND22 = ''
CNKIND23 = ''
CNKIND24 = ''
CNKIND25 = ''
CNKIND26 = ''
CNKIND27 = ''
CNKIND28 = ''
CNKIND29 = ''
CNKIND30 = ''
CNKIND31 = ''
CANAGE1 = ''
CANAGE2 = ''
CANAGE3 = ''
CANAGE4 = ''
CANAGE5 = ''
CANAGE6 = ''
CANAGE7 = ''
CANAGE8 = ''
CANAGE9 = ''
CANAGE10 = ''
CANAGE11 = ''
CANAGE12 = ''
CANAGE13 = ''
CANAGE14 = ''
CANAGE15 = ''
CANAGE16 = ''
CANAGE17 = ''
CANAGE18 = ''
CANAGE19 = ''
CANAGE20 = ''
CANAGE21 = ''
CANAGE22 = ''
CANAGE23 = ''
CANAGE24 = ''
CANAGE25 = ''
CANAGE26 = ''
CANAGE27 = ''
CANAGE28 = ''
CANAGE29 = ''
CANAGE30 = ''
DIBEV = ''
DIBPRE1 = ''
DIBAGE = ''
DIFAGE2 = ''
INSLN = ''
DIBPILL = ''
AHAYFYR = ''
SINYR = ''
CBRCHYR = ''
KIDWKYR = ''
LIVYR = ''
JNTSYMP = ''
JMTHP1 = ''
JMTHP2 = ''
JMTHP3 = ''
JMTHP4 = ''
JMTHP5 = ''
JMTHP6 = ''
JMTHP7 = ''
JMTHP8 = ''
JMTHP9 = ''
JMTHP10 = ''
JMTHP11 = ''
JMTHP12 = ''
JMTHP13 = ''
JMTHP14 = ''
JMTHP15 = ''
JMTHP16 = ''
JMTHP17 = ''
JNTPN = ''
JNTCHR = ''
JNTHP = ''
ARTH1 = ''
ARTHWT = ''
ARTHPH = ''
ARTHCLS = ''
ARTHLMT = ''
ARTHWRK = ''
PAINECK = ''
PAINLB = ''
PAINLEG = ''
PAINFACE = ''
AMIGR = ''
ACOLD2W = ''
AINTIL2W = ''
PREGNOW = ''
PREGFLYR = ''
AHEARST2 = ''
HRWORS = ''
HRWHICH = ''
HRRIGHT = ''
HRLEFT = ''
HRWHISP1 = ''
HRTALK1 = ''
HRSHOUT1 = ''
HRSPEAK1 = ''
HRCOCRE1 = ''
HRCOCIM1 = ''
HRFAM = ''
HRBACK = ''
HRFRUST = ''
HRSAFETY = ''
HEARAGE1 = ''
HRCAUS1 = ''
HRPROBHP = ''
HRENT = ''
HRAUD = ''
HRTEST = ''
HRAIDNOW = ''
HRAIDLNG = ''
HRAID2WK = ''
HRAIDHLP = ''
HRAIDEV = ''
HRAIDREC = ''
HRAIDLGP = ''
HRAIDOF2 = ''
HRAIDN01 = ''
HRAIDN02 = ''
HRAIDN03 = ''
HRAIDN04 = ''
HRAIDN05 = ''
HRAIDN06 = ''
HRAIDN07 = ''
HRAIDN08 = ''
HRAIDN09 = ''
HRAIDN10 = ''
HRAIDN11 = ''
HRAUDTRN = ''
HRALDS = ''
HRALDT01 = ''
HRALDT02 = ''
HRALDT03 = ''
HRALDT04 = ''
HRALDT05 = ''
HRALDT06 = ''
HRALDT07 = ''
HRALDT08 = ''
HRALDT09 = ''
HRALDT10 = ''
HRALDT11 = ''
HRBDIZZ = ''
HRTIN = ''
HRTINOFT = ''
HRTINLNG = ''
HRTINMUS = ''
HRTINSLP = ''
HRTINPRO = ''
HRTINDIS = ''
HRTINDOC = ''
HRTINRM = ''
HREMTY01 = ''
HREMTY02 = ''
HREMTY03 = ''
HREMTY04 = ''
HREMTY05 = ''
HREMTY06 = ''
HREMTY07 = ''
HREMTY08 = ''
HREMTY09 = ''
HREMTY10 = ''
HREMTY11 = ''
HREMTY12 = ''
HRTNRMHP = ''
HRHCUSIS = ''
HRHCPROB = ''
HRFIRE = ''
HRFIRTYP = ''
HRFRTIM = ''
HR12MR = ''
HRFRPROT = ''
HRTOTR = ''
HRFRPRT2 = ''
HRWKVLNS = ''
HRWKLNS = ''
HRWKVLNT = ''
HRWKVLEX = ''
HRWKVLP1 = ''
HRWKVLP2 = ''
HRWRLNS = ''
HRWKLEX = ''
HRWKLP1 = ''
HRWKLP2 = ''
HRLSVLNS = ''
HRVLTP01 = ''
HRVLTP02 = ''
HRVLTP03 = ''
HRVLTP04 = ''
HRVLTP05 = ''
HRVLTP06 = ''
HRVLTP07 = ''
HRVLTP08 = ''
HRVLTP09 = ''
HRVLTP10 = ''
HRLNOS = ''
HRLTP01 = ''
HRLTP02 = ''
HRLTP03 = ''
HRLTP04 = ''
HRLTP05 = ''
HRLTP06 = ''
HRLTP07 = ''
HRLTP08 = ''
HRLTP09 = ''
HRLTP10 = ''
HRNOSEXP = ''
HRLSP1 = ''
HRLSP2 = ''
HRINTNET = ''
HRINTHL = ''
HRINTHA = ''
HRINTTN = ''
HRINTDZ = ''
HRINTHP = ''
HRINTHPR = ''
AVISION = ''
ABLIND = ''
LUPPRT = ''
WKDAYR = ''
BEDDAYR = ''
AHSTATYR = ''
SPECEQ = ''
FLWALK = ''
FLCLIMB = ''
FLSTAND = ''
FLSIT = ''
FLSTOOP = ''
FLREACH = ''
FLGRASP = ''
FLCARRY = ''
FLPUSH = ''
FLSHOP = ''
FLSOCL = ''
FLRELAX = ''
FLA1AR = ''
AFLHCA1 = ''
AFLHCA2 = ''
AFLHCA3 = ''
AFLHCA4 = ''
AFLHCA5 = ''
AFLHCA6 = ''
AFLHCA7 = ''
AFLHCA8 = ''
AFLHCA9 = ''
AFLHCA10 = ''
AFLHCA11 = ''
AFLHCA12 = ''
AFLHCA13 = ''
ALHCA14A = ''
AFLHCA15 = ''
AFLHCA16 = ''
AFLHCA17 = ''
AFLHCA18 = ''
AFLHC19_ = ''
AFLHC20_ = ''
AFLHC21_ = ''
AFLHC22_ = ''
AFLHC23_ = ''
AFLHC24_ = ''
AFLHC25_ = ''
AFLHC26_ = ''
AFLHC27_ = ''
AFLHC28_ = ''
AFLHC29_ = ''
AFLHC30_ = ''
AFLHC31_ = ''
AFLHC32_ = ''
AFLHC33_ = ''
AFLHC34_ = ''
AFLHCA90 = ''
AFLHCA91 = ''
ALTIME1 = ''
ALUNIT1 = ''
ALDURA1 = ''
ALDURB1 = ''
ALCHRC1 = ''
ALTIME2 = ''
ALUNIT2 = ''
ALDURA2 = ''
ALDURB2 = ''
ALCHRC2 = ''
ALTIME3 = ''
ALUNIT3 = ''
ALDURA3 = ''
ALDURB3 = ''
ALCHRC3 = ''
ALTIME4 = ''
ALUNIT4 = ''
ALDURA4 = ''
ALDURB4 = ''
ALCHRC4 = ''
ALTIME5 = ''
ALUNIT5 = ''
ALDURA5 = ''
ALDURB5 = ''
ALCHRC5 = ''
ALTIME6 = ''
ALUNIT6 = ''
ALDURA6 = ''
ALDURB6 = ''
ALCHRC6 = ''
ALTIME7 = ''
ALUNIT7 = ''
ALDURA7 = ''
ALDURB7 = ''
ALCHRC7 = ''
ALTIME8 = ''
ALUNIT8 = ''
ALDURA8 = ''
ALDURB8 = ''
ALCHRC8 = ''
ALTIME9 = ''
ALUNIT9 = ''
ALDURA9 = ''
ALDURB9 = ''
ALCHRC9 = ''
ALTIME10 = ''
ALUNIT10 = ''
ALDURA10 = ''
ALDURB10 = ''
ALCHRC10 = ''
ALTIME11 = ''
ALUNIT11 = ''
ALDURA11 = ''
ALDURB11 = ''
ALCHRC11 = ''
ALTIME12 = ''
ALUNIT12 = ''
ALDURA12 = ''
ALDURB12 = ''
ALCHRC12 = ''
ALTIME13 = ''
ALUNIT13 = ''
ALDURA13 = ''
ALDURB13 = ''
ALCHRC13 = ''
ATIME14A = ''
AUNIT14A = ''
ADURA14A = ''
ADURB14A = ''
ACHRC14A = ''
ALTIME15 = ''
ALUNIT15 = ''
ALDURA15 = ''
ALDURB15 = ''
ALCHRC15 = ''
ALTIME16 = ''
ALUNIT16 = ''
ALDURA16 = ''
ALDURB16 = ''
ALCHRC16 = ''
ALTIME17 = ''
ALUNIT17 = ''
ALDURA17 = ''
ALDURB17 = ''
ALCHRC17 = ''
ALTIME18 = ''
ALUNIT18 = ''
ALDURA18 = ''
ALDURB18 = ''
ALCHRC18 = ''
ALTIME19 = ''
ALUNIT19 = ''
ALDURA19 = ''
ALDURB19 = ''
ALCHRC19 = ''
ALTIME20 = ''
ALUNIT20 = ''
ALDURA20 = ''
ALDURB20 = ''
ALCHRC20 = ''
ALTIME21 = ''
ALUNIT21 = ''
ALDURA21 = ''
ALDURB21 = ''
ALCHRC21 = ''
ALTIME22 = ''
ALUNIT22 = ''
ALDURA22 = ''
ALDURB22 = ''
ALCHRC22 = ''
ALTIME23 = ''
ALUNIT23 = ''
ALDURA23 = ''
ALDURB23 = ''
ALCHRC23 = ''
ALTIME24 = ''
ALUNIT24 = ''
ALDURA24 = ''
ALDURB24 = ''
ALCHRC24 = ''
ALTIME25 = ''
ALUNIT25 = ''
ALDURA25 = ''
ALDURB25 = ''
ALCHRC25 = ''
ALTIME26 = ''
ALUNIT26 = ''
ALDURA26 = ''
ALDURB26 = ''
ALCHRC26 = ''
ALTIME27 = ''
ALUNIT27 = ''
ALDURA27 = ''
ALDURB27 = ''
ALCHRC27 = ''
ALTIME28 = ''
ALUNIT28 = ''
ALDURA28 = ''
ALDURB28 = ''
ALCHRC28 = ''
ALTIME29 = ''
ALUNIT29 = ''
ALDURA29 = ''
ALDURB29 = ''
ALCHRC29 = ''
ALTIME30 = ''
ALUNIT30 = ''
ALDURA30 = ''
ALDURB30 = ''
ALCHRC30 = ''
ALTIME31 = ''
ALUNIT31 = ''
ALDURA31 = ''
ALDURB31 = ''
ALCHRC31 = ''
ALTIME32 = ''
ALUNIT32 = ''
ALDURA32 = ''
ALDURB32 = ''
ALCHRC32 = ''
ALTIME33 = ''
ALUNIT33 = ''
ALDURA33 = ''
ALDURB33 = ''
ALCHRC33 = ''
ALTIME34 = ''
ALUNIT34 = ''
ALDURA34 = ''
ALDURB34 = ''
ALCHRC34 = ''
ALTIME90 = ''
ALUNIT90 = ''
ALDURA90 = ''
ALDURB90 = ''
ALCHRC90 = ''
ALTIME91 = ''
ALUNIT91 = ''
ALDURA91 = ''
ALDURB91 = ''
ALCHRC91 = ''
ALCNDRT = ''
ALCHRONR = ''
SMKEV = ''
SMKREG = ''
SMKNOW = ''
SMKSTAT2 = ''
SMKQTNO = ''
SMKQTTP = ''
SMKQTY = ''
CIGSDA1 = ''
CIGDAMO = ''
CIGSDA2 = ''
CIGSDAY = ''
CIGQTYR = ''
OTHCIGEV = ''
OTHCIGED = ''
SMKLESEV = ''
SMKLESED = ''
TOBLASYR = ''
TOBQTYR = ''
ECIGEV = ''
ECIGED = ''
VIGNO = ''
VIGTP = ''
VIGFREQW = ''
VIGLNGNO = ''
VIGLNGTP = ''
VIGMIN = ''
MODNO = ''
MODTP = ''
MODFREQW = ''
MODLNGNO = ''
MODLNGTP = ''
MODMIN = ''
STRNGNO = ''
STRNGTP = ''
STRFREQW = ''
ALC1YR = ''
ALCLIFE = ''
ALC12MNO = ''
ALC12MTP = ''
ALC12MWK = ''
ALC12MYR = ''
ALCAMT = ''
ALCSTAT = ''
ALC5UPN1 = ''
ALC5UPT1 = ''
ALC5UPY1 = ''
AHEIGHT = ''
AWEIGHTP = ''
BMI = ''
AUSUALPL = ''
APLKIND = ''
AHCPLROU = ''
AHCPLKND = ''
AHCCHGYR = ''
AHCCHGHI = ''
ANOUSPL1 = ''
ANOUSPL2 = ''
ANOUSPL3 = ''
ANOUSPL4 = ''
ANOUSPL5 = ''
ANOUSPL6 = ''
ANOUSPL7 = ''
ANOUSPL8 = ''
ANOUSPL9 = ''
APRVTRYR = ''
APRVTRFD = ''
ADRNANP = ''
ADRNAI = ''
AHCDLYR1 = ''
AHCDLYR2 = ''
AHCDLYR3 = ''
AHCDLYR4 = ''
AHCDLYR5 = ''
AHCAFYR1 = ''
AHCAFYR2 = ''
AHCAFYR3 = ''
AHCAFYR4 = ''
AHCAFYR5 = ''
AHCAFYR6 = ''
AWORPAY = ''
AHICOMP = ''
ARX12MO = ''
ARX12_1 = ''
ARX12_2 = ''
ARX12_3 = ''
ARX12_4 = ''
ARX12_5 = ''
ARX12_6 = ''
ADNLONG2 = ''
AHCSYR1 = ''
AHCSYR2 = ''
AHCSYR3 = ''
AHCSYR4 = ''
AHCSYR5 = ''
AHCSYR6 = ''
AHCSYR7 = ''
AHCSYR8 = ''
AHCSYR9 = ''
AHCSYR10 = ''
AHERNOY2 = ''
AERVISND = ''
AERHOS = ''
AERREA1R = ''
AERREA2R = ''
AERREA3R = ''
AERREA4R = ''
AERREA5R = ''
AERREA6R = ''
AERREA7R = ''
AERREA8R = ''
AHCHYR = ''
AHCHMOYR = ''
AHCHNOY2 = ''
AHCNOYR2 = ''
ASRGYR = ''
ASRGNOYR = ''
AMDLONGR = ''
AVISLAST = ''
ALASTYP1 = ''
ALASTYP2 = ''
ALASTYP3 = ''
ALASTYP4 = ''
ALASTVRB = ''
AVISAPN2 = ''
AVISAPT2 = ''
AWAITRMN = ''
AWAITRMT = ''
HIT1A = ''
HIT2A = ''
HIT3A = ''
HIT4A = ''
HIT5A = ''
SHTFLU2 = ''
ASHFLUM2 = ''
ASHFLUY2 = ''
FLUSHPG1 = ''
FLUSHPG2 = ''
SPRFLU2 = ''
ASPFLUM2 = ''
ASPFLUY2 = ''
SHTPNUYR = ''
APOX = ''
APOX12MO = ''
AHEP = ''
AHEPLIV = ''
AHEPBTST = ''
SHTHEPB = ''
SHEPDOS = ''
SHTHEPA = ''
SHEPANUM = ''
AHEPCTST = ''
AHEPCRES = ''
SHINGLES = ''
SHTTD = ''
SHTTD05 = ''
SHTTDAP2 = ''
SHTHPV2 = ''
SHHPVDOS = ''
AHPVAGE = ''
LIVEV = ''
TRAVEL = ''
WRKHLTH2 = ''
WRKDIR = ''
APSBPCH1 = ''
APSCHCH1 = ''
APSBSCH1 = ''
APSPAP = ''
APSMAM = ''
APSCOL = ''
APSDIET = ''
APSSMKC = ''
LTCFAM = ''
LTCHELP = ''
LTCWHO1 = ''
LTCWHO2 = ''
LTCWHO3 = ''
LTCWHO4 = ''
LTCWHO5 = ''
AINDINS = ''
AINDPRCH = ''
AINDWHO = ''
AINDDIF1 = ''
AINDDIF2 = ''
AINDENY1 = ''
AINDENY2 = ''
AINDENY3 = ''
AINDNOT1 = ''
AINDNOT2 = ''
AINDNOT3 = ''
AINDNOT4 = ''
AINDNOT5 = ''
AEXCHNG = ''
ASICPUSE = ''
ASISATHC = ''
ASITENUR = ''
ASINHELP = ''
ASINCNTO = ''
ASINTRU = ''
ASINKNT = ''
ASISIM = ''
ASISIF = ''
ASIRETR = ''
ASIMEDC = ''
ASISTLV = ''
ASICNHC = ''
ASICCOLL = ''
ASINBILL = ''
ASIHCST = ''
ASICCMP = ''
ASISLEEP = ''
ASISLPFL = ''
ASISLPST = ''
ASISLPMD = ''
ASIREST = ''
ASISAD = ''
ASINERV = ''
ASIRSTLS = ''
ASIHOPLS = ''
ASIEFFRT = ''
ASIWTHLS = ''
ASIMUCH = ''
ASIHIVT = ''
ASIHIVWN = ''
AWEBUSE = ''
AWEBOFNO = ''
AWEBOFTP = ''
AWEBORP = ''
AWEBEML = ''
AWEBMNO = ''
AWEBMTP = ''

RECTYPE_LIST = []
SRVY_YR_LIST = []
HHX_LIST = []
INTV_QRT_LIST = []
INTV_MON_LIST = []
FMX_LIST = []
FPX_LIST = []
WTIA_SA_LIST = []
WTFA_SA_LIST = []
REGION_LIST = []
STRAT_P_LIST = []
PSU_P_LIST = []
SEX_LIST = []
HISPAN_I_LIST = []
RACERPI2_LIST = []
MRACRPI2_LIST = []
MRACBPI2_LIST = []
AGE_P_LIST = []
R_MARITL_LIST = []
PROXYSA_LIST = []
PROX1_LIST = []
PROX2_LIST = []
LATEINTA_LIST = []
FDRN_FLG_LIST = []
DOINGLWA_LIST = []
WHYNOWKA_LIST = []
EVERWRK_LIST = []
INDSTRN1_LIST = []
INDSTRN2_LIST = []
OCCUPN1_LIST = []
OCCUPN2_LIST = []
WRKCATA_LIST = []
BUSINC1A_LIST = []
LOCALL1A_LIST = []
YRSWRKPA_LIST = []
WRKLONGH_LIST = []
HOURPDA_LIST = []
PDSICKA_LIST = []
ONEJOB_LIST = []
WRKLYR4_LIST = []
HYPEV_LIST = []
HYPDIFV_LIST = []
HYPYR1_LIST = []
HYBPCKNO_LIST = []
HYBPCKTP_LIST = []
HYBPLEV_LIST = []
HYPMDEV2_LIST = []
HYPMED2_LIST = []
CHLEV_LIST = []
CHLYR_LIST = []
CLCKNO_LIST = []
CLCKTP_LIST = []
CHLMDEV2_LIST = []
CHLMDNW2_LIST = []
CHDEV_LIST = []
ANGEV_LIST = []
MIEV_LIST = []
HRTEV_LIST = []
STREV_LIST = []
EPHEV_LIST = []
JAWP_LIST = []
WEA_LIST = []
CHE_LIST = []
ARM_LIST = []
BRTH_LIST = []
AHADO_LIST = []
FACE_LIST = []
SPEAKING_LIST = []
EYE_LIST = []
WALKING_LIST = []
HEADACHE_LIST = []
ASTDO_LIST = []
COPDEV_LIST = []
ASPMEDEV_LIST = []
ASPMEDAD_LIST = []
ASPMDMED_LIST = []
ASPONOWN_LIST = []
AASMEV_LIST = []
AASSTILL_LIST = []
AASMYR_LIST = []
AASERYR1_LIST = []
ULCEV_LIST = []
ULCYR_LIST = []
CANEV_LIST = []
CNKIND1_LIST = []
CNKIND2_LIST = []
CNKIND3_LIST = []
CNKIND4_LIST = []
CNKIND5_LIST = []
CNKIND6_LIST = []
CNKIND7_LIST = []
CNKIND8_LIST = []
CNKIND9_LIST = []
CNKIND10_LIST = []
CNKIND11_LIST = []
CNKIND12_LIST = []
CNKIND13_LIST = []
CNKIND14_LIST = []
CNKIND15_LIST = []
CNKIND16_LIST = []
CNKIND17_LIST = []
CNKIND18_LIST = []
CNKIND19_LIST = []
CNKIND20_LIST = []
CNKIND21_LIST = []
CNKIND22_LIST = []
CNKIND23_LIST = []
CNKIND24_LIST = []
CNKIND25_LIST = []
CNKIND26_LIST = []
CNKIND27_LIST = []
CNKIND28_LIST = []
CNKIND29_LIST = []
CNKIND30_LIST = []
CNKIND31_LIST = []
CANAGE1_LIST = []
CANAGE2_LIST = []
CANAGE3_LIST = []
CANAGE4_LIST = []
CANAGE5_LIST = []
CANAGE6_LIST = []
CANAGE7_LIST = []
CANAGE8_LIST = []
CANAGE9_LIST = []
CANAGE10_LIST = []
CANAGE11_LIST = []
CANAGE12_LIST = []
CANAGE13_LIST = []
CANAGE14_LIST = []
CANAGE15_LIST = []
CANAGE16_LIST = []
CANAGE17_LIST = []
CANAGE18_LIST = []
CANAGE19_LIST = []
CANAGE20_LIST = []
CANAGE21_LIST = []
CANAGE22_LIST = []
CANAGE23_LIST = []
CANAGE24_LIST = []
CANAGE25_LIST = []
CANAGE26_LIST = []
CANAGE27_LIST = []
CANAGE28_LIST = []
CANAGE29_LIST = []
CANAGE30_LIST = []
DIBEV_LIST = []
DIBPRE1_LIST = []
DIBAGE_LIST = []
DIFAGE2_LIST = []
INSLN_LIST = []
DIBPILL_LIST = []
AHAYFYR_LIST = []
SINYR_LIST = []
CBRCHYR_LIST = []
KIDWKYR_LIST = []
LIVYR_LIST = []
JNTSYMP_LIST = []
JMTHP1_LIST = []
JMTHP2_LIST = []
JMTHP3_LIST = []
JMTHP4_LIST = []
JMTHP5_LIST = []
JMTHP6_LIST = []
JMTHP7_LIST = []
JMTHP8_LIST = []
JMTHP9_LIST = []
JMTHP10_LIST = []
JMTHP11_LIST = []
JMTHP12_LIST = []
JMTHP13_LIST = []
JMTHP14_LIST = []
JMTHP15_LIST = []
JMTHP16_LIST = []
JMTHP17_LIST = []
JNTPN_LIST = []
JNTCHR_LIST = []
JNTHP_LIST = []
ARTH1_LIST = []
ARTHWT_LIST = []
ARTHPH_LIST = []
ARTHCLS_LIST = []
ARTHLMT_LIST = []
ARTHWRK_LIST = []
PAINECK_LIST = []
PAINLB_LIST = []
PAINLEG_LIST = []
PAINFACE_LIST = []
AMIGR_LIST = []
ACOLD2W_LIST = []
AINTIL2W_LIST = []
PREGNOW_LIST = []
PREGFLYR_LIST = []
AHEARST2_LIST = []
HRWORS_LIST = []
HRWHICH_LIST = []
HRRIGHT_LIST = []
HRLEFT_LIST = []
HRWHISP1_LIST = []
HRTALK1_LIST = []
HRSHOUT1_LIST = []
HRSPEAK1_LIST = []
HRCOCRE1_LIST = []
HRCOCIM1_LIST = []
HRFAM_LIST = []
HRBACK_LIST = []
HRFRUST_LIST = []
HRSAFETY_LIST = []
HEARAGE1_LIST = []
HRCAUS1_LIST = []
HRPROBHP_LIST = []
HRENT_LIST = []
HRAUD_LIST = []
HRTEST_LIST = []
HRAIDNOW_LIST = []
HRAIDLNG_LIST = []
HRAID2WK_LIST = []
HRAIDHLP_LIST = []
HRAIDEV_LIST = []
HRAIDREC_LIST = []
HRAIDLGP_LIST = []
HRAIDOF2_LIST = []
HRAIDN01_LIST = []
HRAIDN02_LIST = []
HRAIDN03_LIST = []
HRAIDN04_LIST = []
HRAIDN05_LIST = []
HRAIDN06_LIST = []
HRAIDN07_LIST = []
HRAIDN08_LIST = []
HRAIDN09_LIST = []
HRAIDN10_LIST = []
HRAIDN11_LIST = []
HRAUDTRN_LIST = []
HRALDS_LIST = []
HRALDT01_LIST = []
HRALDT02_LIST = []
HRALDT03_LIST = []
HRALDT04_LIST = []
HRALDT05_LIST = []
HRALDT06_LIST = []
HRALDT07_LIST = []
HRALDT08_LIST = []
HRALDT09_LIST = []
HRALDT10_LIST = []
HRALDT11_LIST = []
HRBDIZZ_LIST = []
HRTIN_LIST = []
HRTINOFT_LIST = []
HRTINLNG_LIST = []
HRTINMUS_LIST = []
HRTINSLP_LIST = []
HRTINPRO_LIST = []
HRTINDIS_LIST = []
HRTINDOC_LIST = []
HRTINRM_LIST = []
HREMTY01_LIST = []
HREMTY02_LIST = []
HREMTY03_LIST = []
HREMTY04_LIST = []
HREMTY05_LIST = []
HREMTY06_LIST = []
HREMTY07_LIST = []
HREMTY08_LIST = []
HREMTY09_LIST = []
HREMTY10_LIST = []
HREMTY11_LIST = []
HREMTY12_LIST = []
HRTNRMHP_LIST = []
HRHCUSIS_LIST = []
HRHCPROB_LIST = []
HRFIRE_LIST = []
HRFIRTYP_LIST = []
HRFRTIM_LIST = []
HR12MR_LIST = []
HRFRPROT_LIST = []
HRTOTR_LIST = []
HRFRPRT2_LIST = []
HRWKVLNS_LIST = []
HRWKLNS_LIST = []
HRWKVLNT_LIST = []
HRWKVLEX_LIST = []
HRWKVLP1_LIST = []
HRWKVLP2_LIST = []
HRWRLNS_LIST = []
HRWKLEX_LIST = []
HRWKLP1_LIST = []
HRWKLP2_LIST = []
HRLSVLNS_LIST = []
HRVLTP01_LIST = []
HRVLTP02_LIST = []
HRVLTP03_LIST = []
HRVLTP04_LIST = []
HRVLTP05_LIST = []
HRVLTP06_LIST = []
HRVLTP07_LIST = []
HRVLTP08_LIST = []
HRVLTP09_LIST = []
HRVLTP10_LIST = []
HRLNOS_LIST = []
HRLTP01_LIST = []
HRLTP02_LIST = []
HRLTP03_LIST = []
HRLTP04_LIST = []
HRLTP05_LIST = []
HRLTP06_LIST = []
HRLTP07_LIST = []
HRLTP08_LIST = []
HRLTP09_LIST = []
HRLTP10_LIST = []
HRNOSEXP_LIST = []
HRLSP1_LIST = []
HRLSP2_LIST = []
HRINTNET_LIST = []
HRINTHL_LIST = []
HRINTHA_LIST = []
HRINTTN_LIST = []
HRINTDZ_LIST = []
HRINTHP_LIST = []
HRINTHPR_LIST = []
AVISION_LIST = []
ABLIND_LIST = []
LUPPRT_LIST = []
WKDAYR_LIST = []
BEDDAYR_LIST = []
AHSTATYR_LIST = []
SPECEQ_LIST = []
FLWALK_LIST = []
FLCLIMB_LIST = []
FLSTAND_LIST = []
FLSIT_LIST = []
FLSTOOP_LIST = []
FLREACH_LIST = []
FLGRASP_LIST = []
FLCARRY_LIST = []
FLPUSH_LIST = []
FLSHOP_LIST = []
FLSOCL_LIST = []
FLRELAX_LIST = []
FLA1AR_LIST = []
AFLHCA1_LIST = []
AFLHCA2_LIST = []
AFLHCA3_LIST = []
AFLHCA4_LIST = []
AFLHCA5_LIST = []
AFLHCA6_LIST = []
AFLHCA7_LIST = []
AFLHCA8_LIST = []
AFLHCA9_LIST = []
AFLHCA10_LIST = []
AFLHCA11_LIST = []
AFLHCA12_LIST = []
AFLHCA13_LIST = []
ALHCA14A_LIST = []
AFLHCA15_LIST = []
AFLHCA16_LIST = []
AFLHCA17_LIST = []
AFLHCA18_LIST = []
AFLHC19__LIST = []
AFLHC20__LIST = []
AFLHC21__LIST = []
AFLHC22__LIST = []
AFLHC23__LIST = []
AFLHC24__LIST = []
AFLHC25__LIST = []
AFLHC26__LIST = []
AFLHC27__LIST = []
AFLHC28__LIST = []
AFLHC29__LIST = []
AFLHC30__LIST = []
AFLHC31__LIST = []
AFLHC32__LIST = []
AFLHC33__LIST = []
AFLHC34__LIST = []
AFLHCA90_LIST = []
AFLHCA91_LIST = []
ALTIME1_LIST = []
ALUNIT1_LIST = []
ALDURA1_LIST = []
ALDURB1_LIST = []
ALCHRC1_LIST = []
ALTIME2_LIST = []
ALUNIT2_LIST = []
ALDURA2_LIST = []
ALDURB2_LIST = []
ALCHRC2_LIST = []
ALTIME3_LIST = []
ALUNIT3_LIST = []
ALDURA3_LIST = []
ALDURB3_LIST = []
ALCHRC3_LIST = []
ALTIME4_LIST = []
ALUNIT4_LIST = []
ALDURA4_LIST = []
ALDURB4_LIST = []
ALCHRC4_LIST = []
ALTIME5_LIST = []
ALUNIT5_LIST = []
ALDURA5_LIST = []
ALDURB5_LIST = []
ALCHRC5_LIST = []
ALTIME6_LIST = []
ALUNIT6_LIST = []
ALDURA6_LIST = []
ALDURB6_LIST = []
ALCHRC6_LIST = []
ALTIME7_LIST = []
ALUNIT7_LIST = []
ALDURA7_LIST = []
ALDURB7_LIST = []
ALCHRC7_LIST = []
ALTIME8_LIST = []
ALUNIT8_LIST = []
ALDURA8_LIST = []
ALDURB8_LIST = []
ALCHRC8_LIST = []
ALTIME9_LIST = []
ALUNIT9_LIST = []
ALDURA9_LIST = []
ALDURB9_LIST = []
ALCHRC9_LIST = []
ALTIME10_LIST = []
ALUNIT10_LIST = []
ALDURA10_LIST = []
ALDURB10_LIST = []
ALCHRC10_LIST = []
ALTIME11_LIST = []
ALUNIT11_LIST = []
ALDURA11_LIST = []
ALDURB11_LIST = []
ALCHRC11_LIST = []
ALTIME12_LIST = []
ALUNIT12_LIST = []
ALDURA12_LIST = []
ALDURB12_LIST = []
ALCHRC12_LIST = []
ALTIME13_LIST = []
ALUNIT13_LIST = []
ALDURA13_LIST = []
ALDURB13_LIST = []
ALCHRC13_LIST = []
ATIME14A_LIST = []
AUNIT14A_LIST = []
ADURA14A_LIST = []
ADURB14A_LIST = []
ACHRC14A_LIST = []
ALTIME15_LIST = []
ALUNIT15_LIST = []
ALDURA15_LIST = []
ALDURB15_LIST = []
ALCHRC15_LIST = []
ALTIME16_LIST = []
ALUNIT16_LIST = []
ALDURA16_LIST = []
ALDURB16_LIST = []
ALCHRC16_LIST = []
ALTIME17_LIST = []
ALUNIT17_LIST = []
ALDURA17_LIST = []
ALDURB17_LIST = []
ALCHRC17_LIST = []
ALTIME18_LIST = []
ALUNIT18_LIST = []
ALDURA18_LIST = []
ALDURB18_LIST = []
ALCHRC18_LIST = []
ALTIME19_LIST = []
ALUNIT19_LIST = []
ALDURA19_LIST = []
ALDURB19_LIST = []
ALCHRC19_LIST = []
ALTIME20_LIST = []
ALUNIT20_LIST = []
ALDURA20_LIST = []
ALDURB20_LIST = []
ALCHRC20_LIST = []
ALTIME21_LIST = []
ALUNIT21_LIST = []
ALDURA21_LIST = []
ALDURB21_LIST = []
ALCHRC21_LIST = []
ALTIME22_LIST = []
ALUNIT22_LIST = []
ALDURA22_LIST = []
ALDURB22_LIST = []
ALCHRC22_LIST = []
ALTIME23_LIST = []
ALUNIT23_LIST = []
ALDURA23_LIST = []
ALDURB23_LIST = []
ALCHRC23_LIST = []
ALTIME24_LIST = []
ALUNIT24_LIST = []
ALDURA24_LIST = []
ALDURB24_LIST = []
ALCHRC24_LIST = []
ALTIME25_LIST = []
ALUNIT25_LIST = []
ALDURA25_LIST = []
ALDURB25_LIST = []
ALCHRC25_LIST = []
ALTIME26_LIST = []
ALUNIT26_LIST = []
ALDURA26_LIST = []
ALDURB26_LIST = []
ALCHRC26_LIST = []
ALTIME27_LIST = []
ALUNIT27_LIST = []
ALDURA27_LIST = []
ALDURB27_LIST = []
ALCHRC27_LIST = []
ALTIME28_LIST = []
ALUNIT28_LIST = []
ALDURA28_LIST = []
ALDURB28_LIST = []
ALCHRC28_LIST = []
ALTIME29_LIST = []
ALUNIT29_LIST = []
ALDURA29_LIST = []
ALDURB29_LIST = []
ALCHRC29_LIST = []
ALTIME30_LIST = []
ALUNIT30_LIST = []
ALDURA30_LIST = []
ALDURB30_LIST = []
ALCHRC30_LIST = []
ALTIME31_LIST = []
ALUNIT31_LIST = []
ALDURA31_LIST = []
ALDURB31_LIST = []
ALCHRC31_LIST = []
ALTIME32_LIST = []
ALUNIT32_LIST = []
ALDURA32_LIST = []
ALDURB32_LIST = []
ALCHRC32_LIST = []
ALTIME33_LIST = []
ALUNIT33_LIST = []
ALDURA33_LIST = []
ALDURB33_LIST = []
ALCHRC33_LIST = []
ALTIME34_LIST = []
ALUNIT34_LIST = []
ALDURA34_LIST = []
ALDURB34_LIST = []
ALCHRC34_LIST = []
ALTIME90_LIST = []
ALUNIT90_LIST = []
ALDURA90_LIST = []
ALDURB90_LIST = []
ALCHRC90_LIST = []
ALTIME91_LIST = []
ALUNIT91_LIST = []
ALDURA91_LIST = []
ALDURB91_LIST = []
ALCHRC91_LIST = []
ALCNDRT_LIST = []
ALCHRONR_LIST = []
SMKEV_LIST = []
SMKREG_LIST = []
SMKNOW_LIST = []
SMKSTAT2_LIST = []
SMKQTNO_LIST = []
SMKQTTP_LIST = []
SMKQTY_LIST = []
CIGSDA1_LIST = []
CIGDAMO_LIST = []
CIGSDA2_LIST = []
CIGSDAY_LIST = []
CIGQTYR_LIST = []
OTHCIGEV_LIST = []
OTHCIGED_LIST = []
SMKLESEV_LIST = []
SMKLESED_LIST = []
TOBLASYR_LIST = []
TOBQTYR_LIST = []
ECIGEV_LIST = []
ECIGED_LIST = []
VIGNO_LIST = []
VIGTP_LIST = []
VIGFREQW_LIST = []
VIGLNGNO_LIST = []
VIGLNGTP_LIST = []
VIGMIN_LIST = []
MODNO_LIST = []
MODTP_LIST = []
MODFREQW_LIST = []
MODLNGNO_LIST = []
MODLNGTP_LIST = []
MODMIN_LIST = []
STRNGNO_LIST = []
STRNGTP_LIST = []
STRFREQW_LIST = []
ALC1YR_LIST = []
ALCLIFE_LIST = []
ALC12MNO_LIST = []
ALC12MTP_LIST = []
ALC12MWK_LIST = []
ALC12MYR_LIST = []
ALCAMT_LIST = []
ALCSTAT_LIST = []
ALC5UPN1_LIST = []
ALC5UPT1_LIST = []
ALC5UPY1_LIST = []
AHEIGHT_LIST = []
AWEIGHTP_LIST = []
BMI_LIST = []
AUSUALPL_LIST = []
APLKIND_LIST = []
AHCPLROU_LIST = []
AHCPLKND_LIST = []
AHCCHGYR_LIST = []
AHCCHGHI_LIST = []
ANOUSPL1_LIST = []
ANOUSPL2_LIST = []
ANOUSPL3_LIST = []
ANOUSPL4_LIST = []
ANOUSPL5_LIST = []
ANOUSPL6_LIST = []
ANOUSPL7_LIST = []
ANOUSPL8_LIST = []
ANOUSPL9_LIST = []
APRVTRYR_LIST = []
APRVTRFD_LIST = []
ADRNANP_LIST = []
ADRNAI_LIST = []
AHCDLYR1_LIST = []
AHCDLYR2_LIST = []
AHCDLYR3_LIST = []
AHCDLYR4_LIST = []
AHCDLYR5_LIST = []
AHCAFYR1_LIST = []
AHCAFYR2_LIST = []
AHCAFYR3_LIST = []
AHCAFYR4_LIST = []
AHCAFYR5_LIST = []
AHCAFYR6_LIST = []
AWORPAY_LIST = []
AHICOMP_LIST = []
ARX12MO_LIST = []
ARX12_1_LIST = []
ARX12_2_LIST = []
ARX12_3_LIST = []
ARX12_4_LIST = []
ARX12_5_LIST = []
ARX12_6_LIST = []
ADNLONG2_LIST = []
AHCSYR1_LIST = []
AHCSYR2_LIST = []
AHCSYR3_LIST = []
AHCSYR4_LIST = []
AHCSYR5_LIST = []
AHCSYR6_LIST = []
AHCSYR7_LIST = []
AHCSYR8_LIST = []
AHCSYR9_LIST = []
AHCSYR10_LIST = []
AHERNOY2_LIST = []
AERVISND_LIST = []
AERHOS_LIST = []
AERREA1R_LIST = []
AERREA2R_LIST = []
AERREA3R_LIST = []
AERREA4R_LIST = []
AERREA5R_LIST = []
AERREA6R_LIST = []
AERREA7R_LIST = []
AERREA8R_LIST = []
AHCHYR_LIST = []
AHCHMOYR_LIST = []
AHCHNOY2_LIST = []
AHCNOYR2_LIST = []
ASRGYR_LIST = []
ASRGNOYR_LIST = []
AMDLONGR_LIST = []
AVISLAST_LIST = []
ALASTYP1_LIST = []
ALASTYP2_LIST = []
ALASTYP3_LIST = []
ALASTYP4_LIST = []
ALASTVRB_LIST = []
AVISAPN2_LIST = []
AVISAPT2_LIST = []
AWAITRMN_LIST = []
AWAITRMT_LIST = []
HIT1A_LIST = []
HIT2A_LIST = []
HIT3A_LIST = []
HIT4A_LIST = []
HIT5A_LIST = []
SHTFLU2_LIST = []
ASHFLUM2_LIST = []
ASHFLUY2_LIST = []
FLUSHPG1_LIST = []
FLUSHPG2_LIST = []
SPRFLU2_LIST = []
ASPFLUM2_LIST = []
ASPFLUY2_LIST = []
SHTPNUYR_LIST = []
APOX_LIST = []
APOX12MO_LIST = []
AHEP_LIST = []
AHEPLIV_LIST = []
AHEPBTST_LIST = []
SHTHEPB_LIST = []
SHEPDOS_LIST = []
SHTHEPA_LIST = []
SHEPANUM_LIST = []
AHEPCTST_LIST = []
AHEPCRES_LIST = []
SHINGLES_LIST = []
SHTTD_LIST = []
SHTTD05_LIST = []
SHTTDAP2_LIST = []
SHTHPV2_LIST = []
SHHPVDOS_LIST = []
AHPVAGE_LIST = []
LIVEV_LIST = []
TRAVEL_LIST = []
WRKHLTH2_LIST = []
WRKDIR_LIST = []
APSBPCH1_LIST = []
APSCHCH1_LIST = []
APSBSCH1_LIST = []
APSPAP_LIST = []
APSMAM_LIST = []
APSCOL_LIST = []
APSDIET_LIST = []
APSSMKC_LIST = []
LTCFAM_LIST = []
LTCHELP_LIST = []
LTCWHO1_LIST = []
LTCWHO2_LIST = []
LTCWHO3_LIST = []
LTCWHO4_LIST = []
LTCWHO5_LIST = []
AINDINS_LIST = []
AINDPRCH_LIST = []
AINDWHO_LIST = []
AINDDIF1_LIST = []
AINDDIF2_LIST = []
AINDENY1_LIST = []
AINDENY2_LIST = []
AINDENY3_LIST = []
AINDNOT1_LIST = []
AINDNOT2_LIST = []
AINDNOT3_LIST = []
AINDNOT4_LIST = []
AINDNOT5_LIST = []
AEXCHNG_LIST = []
ASICPUSE_LIST = []
ASISATHC_LIST = []
ASITENUR_LIST = []
ASINHELP_LIST = []
ASINCNTO_LIST = []
ASINTRU_LIST = []
ASINKNT_LIST = []
ASISIM_LIST = []
ASISIF_LIST = []
ASIRETR_LIST = []
ASIMEDC_LIST = []
ASISTLV_LIST = []
ASICNHC_LIST = []
ASICCOLL_LIST = []
ASINBILL_LIST = []
ASIHCST_LIST = []
ASICCMP_LIST = []
ASISLEEP_LIST = []
ASISLPFL_LIST = []
ASISLPST_LIST = []
ASISLPMD_LIST = []
ASIREST_LIST = []
ASISAD_LIST = []
ASINERV_LIST = []
ASIRSTLS_LIST = []
ASIHOPLS_LIST = []
ASIEFFRT_LIST = []
ASIWTHLS_LIST = []
ASIMUCH_LIST = []
ASIHIVT_LIST = []
ASIHIVWN_LIST = []
AWEBUSE_LIST = []
AWEBOFNO_LIST = []
AWEBOFTP_LIST = []
AWEBORP_LIST = []
AWEBEML_LIST = []
AWEBMNO_LIST = []
AWEBMTP_LIST = []

with open(input_data_FILE, encoding="utf8", mode="r") as f_data:
    for ldx, line in enumerate(f_data):
        if ldx < 36696:
            RECTYPE_accumulator_LIST = []
            SRVY_YR_accumulator_LIST = []
            HHX_accumulator_LIST = []
            INTV_QRT_accumulator_LIST = []
            INTV_MON_accumulator_LIST = []
            FMX_accumulator_LIST = []
            FPX_accumulator_LIST = []
            WTIA_SA_accumulator_LIST = []
            WTFA_SA_accumulator_LIST = []
            REGION_accumulator_LIST = []
            STRAT_P_accumulator_LIST = []
            PSU_P_accumulator_LIST = []
            SEX_accumulator_LIST = []
            HISPAN_I_accumulator_LIST = []
            RACERPI2_accumulator_LIST = []
            MRACRPI2_accumulator_LIST = []
            MRACBPI2_accumulator_LIST = []
            AGE_P_accumulator_LIST = []
            R_MARITL_accumulator_LIST = []
            PROXYSA_accumulator_LIST = []
            PROX1_accumulator_LIST = []
            PROX2_accumulator_LIST = []
            LATEINTA_accumulator_LIST = []
            FDRN_FLG_accumulator_LIST = []
            DOINGLWA_accumulator_LIST = []
            WHYNOWKA_accumulator_LIST = []
            EVERWRK_accumulator_LIST = []
            INDSTRN1_accumulator_LIST = []
            INDSTRN2_accumulator_LIST = []
            OCCUPN1_accumulator_LIST = []
            OCCUPN2_accumulator_LIST = []
            WRKCATA_accumulator_LIST = []
            BUSINC1A_accumulator_LIST = []
            LOCALL1A_accumulator_LIST = []
            YRSWRKPA_accumulator_LIST = []
            WRKLONGH_accumulator_LIST = []
            HOURPDA_accumulator_LIST = []
            PDSICKA_accumulator_LIST = []
            ONEJOB_accumulator_LIST = []
            WRKLYR4_accumulator_LIST = []
            HYPEV_accumulator_LIST = []
            HYPDIFV_accumulator_LIST = []
            HYPYR1_accumulator_LIST = []
            HYBPCKNO_accumulator_LIST = []
            HYBPCKTP_accumulator_LIST = []
            HYBPLEV_accumulator_LIST = []
            HYPMDEV2_accumulator_LIST = []
            HYPMED2_accumulator_LIST = []
            CHLEV_accumulator_LIST = []
            CHLYR_accumulator_LIST = []
            CLCKNO_accumulator_LIST = []
            CLCKTP_accumulator_LIST = []
            CHLMDEV2_accumulator_LIST = []
            CHLMDNW2_accumulator_LIST = []
            CHDEV_accumulator_LIST = []
            ANGEV_accumulator_LIST = []
            MIEV_accumulator_LIST = []
            HRTEV_accumulator_LIST = []
            STREV_accumulator_LIST = []
            EPHEV_accumulator_LIST = []
            JAWP_accumulator_LIST = []
            WEA_accumulator_LIST = []
            CHE_accumulator_LIST = []
            ARM_accumulator_LIST = []
            BRTH_accumulator_LIST = []
            AHADO_accumulator_LIST = []
            FACE_accumulator_LIST = []
            SPEAKING_accumulator_LIST = []
            EYE_accumulator_LIST = []
            WALKING_accumulator_LIST = []
            HEADACHE_accumulator_LIST = []
            ASTDO_accumulator_LIST = []
            COPDEV_accumulator_LIST = []
            ASPMEDEV_accumulator_LIST = []
            ASPMEDAD_accumulator_LIST = []
            ASPMDMED_accumulator_LIST = []
            ASPONOWN_accumulator_LIST = []
            AASMEV_accumulator_LIST = []
            AASSTILL_accumulator_LIST = []
            AASMYR_accumulator_LIST = []
            AASERYR1_accumulator_LIST = []
            ULCEV_accumulator_LIST = []
            ULCYR_accumulator_LIST = []
            CANEV_accumulator_LIST = []
            CNKIND1_accumulator_LIST = []
            CNKIND2_accumulator_LIST = []
            CNKIND3_accumulator_LIST = []
            CNKIND4_accumulator_LIST = []
            CNKIND5_accumulator_LIST = []
            CNKIND6_accumulator_LIST = []
            CNKIND7_accumulator_LIST = []
            CNKIND8_accumulator_LIST = []
            CNKIND9_accumulator_LIST = []
            CNKIND10_accumulator_LIST = []
            CNKIND11_accumulator_LIST = []
            CNKIND12_accumulator_LIST = []
            CNKIND13_accumulator_LIST = []
            CNKIND14_accumulator_LIST = []
            CNKIND15_accumulator_LIST = []
            CNKIND16_accumulator_LIST = []
            CNKIND17_accumulator_LIST = []
            CNKIND18_accumulator_LIST = []
            CNKIND19_accumulator_LIST = []
            CNKIND20_accumulator_LIST = []
            CNKIND21_accumulator_LIST = []
            CNKIND22_accumulator_LIST = []
            CNKIND23_accumulator_LIST = []
            CNKIND24_accumulator_LIST = []
            CNKIND25_accumulator_LIST = []
            CNKIND26_accumulator_LIST = []
            CNKIND27_accumulator_LIST = []
            CNKIND28_accumulator_LIST = []
            CNKIND29_accumulator_LIST = []
            CNKIND30_accumulator_LIST = []
            CNKIND31_accumulator_LIST = []
            CANAGE1_accumulator_LIST = []
            CANAGE2_accumulator_LIST = []
            CANAGE3_accumulator_LIST = []
            CANAGE4_accumulator_LIST = []
            CANAGE5_accumulator_LIST = []
            CANAGE6_accumulator_LIST = []
            CANAGE7_accumulator_LIST = []
            CANAGE8_accumulator_LIST = []
            CANAGE9_accumulator_LIST = []
            CANAGE10_accumulator_LIST = []
            CANAGE11_accumulator_LIST = []
            CANAGE12_accumulator_LIST = []
            CANAGE13_accumulator_LIST = []
            CANAGE14_accumulator_LIST = []
            CANAGE15_accumulator_LIST = []
            CANAGE16_accumulator_LIST = []
            CANAGE17_accumulator_LIST = []
            CANAGE18_accumulator_LIST = []
            CANAGE19_accumulator_LIST = []
            CANAGE20_accumulator_LIST = []
            CANAGE21_accumulator_LIST = []
            CANAGE22_accumulator_LIST = []
            CANAGE23_accumulator_LIST = []
            CANAGE24_accumulator_LIST = []
            CANAGE25_accumulator_LIST = []
            CANAGE26_accumulator_LIST = []
            CANAGE27_accumulator_LIST = []
            CANAGE28_accumulator_LIST = []
            CANAGE29_accumulator_LIST = []
            CANAGE30_accumulator_LIST = []
            DIBEV_accumulator_LIST = []
            DIBPRE1_accumulator_LIST = []
            DIBAGE_accumulator_LIST = []
            DIFAGE2_accumulator_LIST = []
            INSLN_accumulator_LIST = []
            DIBPILL_accumulator_LIST = []
            AHAYFYR_accumulator_LIST = []
            SINYR_accumulator_LIST = []
            CBRCHYR_accumulator_LIST = []
            KIDWKYR_accumulator_LIST = []
            LIVYR_accumulator_LIST = []
            JNTSYMP_accumulator_LIST = []
            JMTHP1_accumulator_LIST = []
            JMTHP2_accumulator_LIST = []
            JMTHP3_accumulator_LIST = []
            JMTHP4_accumulator_LIST = []
            JMTHP5_accumulator_LIST = []
            JMTHP6_accumulator_LIST = []
            JMTHP7_accumulator_LIST = []
            JMTHP8_accumulator_LIST = []
            JMTHP9_accumulator_LIST = []
            JMTHP10_accumulator_LIST = []
            JMTHP11_accumulator_LIST = []
            JMTHP12_accumulator_LIST = []
            JMTHP13_accumulator_LIST = []
            JMTHP14_accumulator_LIST = []
            JMTHP15_accumulator_LIST = []
            JMTHP16_accumulator_LIST = []
            JMTHP17_accumulator_LIST = []
            JNTPN_accumulator_LIST = []
            JNTCHR_accumulator_LIST = []
            JNTHP_accumulator_LIST = []
            ARTH1_accumulator_LIST = []
            ARTHWT_accumulator_LIST = []
            ARTHPH_accumulator_LIST = []
            ARTHCLS_accumulator_LIST = []
            ARTHLMT_accumulator_LIST = []
            ARTHWRK_accumulator_LIST = []
            PAINECK_accumulator_LIST = []
            PAINLB_accumulator_LIST = []
            PAINLEG_accumulator_LIST = []
            PAINFACE_accumulator_LIST = []
            AMIGR_accumulator_LIST = []
            ACOLD2W_accumulator_LIST = []
            AINTIL2W_accumulator_LIST = []
            PREGNOW_accumulator_LIST = []
            PREGFLYR_accumulator_LIST = []
            AHEARST2_accumulator_LIST = []
            HRWORS_accumulator_LIST = []
            HRWHICH_accumulator_LIST = []
            HRRIGHT_accumulator_LIST = []
            HRLEFT_accumulator_LIST = []
            HRWHISP1_accumulator_LIST = []
            HRTALK1_accumulator_LIST = []
            HRSHOUT1_accumulator_LIST = []
            HRSPEAK1_accumulator_LIST = []
            HRCOCRE1_accumulator_LIST = []
            HRCOCIM1_accumulator_LIST = []
            HRFAM_accumulator_LIST = []
            HRBACK_accumulator_LIST = []
            HRFRUST_accumulator_LIST = []
            HRSAFETY_accumulator_LIST = []
            HEARAGE1_accumulator_LIST = []
            HRCAUS1_accumulator_LIST = []
            HRPROBHP_accumulator_LIST = []
            HRENT_accumulator_LIST = []
            HRAUD_accumulator_LIST = []
            HRTEST_accumulator_LIST = []
            HRAIDNOW_accumulator_LIST = []
            HRAIDLNG_accumulator_LIST = []
            HRAID2WK_accumulator_LIST = []
            HRAIDHLP_accumulator_LIST = []
            HRAIDEV_accumulator_LIST = []
            HRAIDREC_accumulator_LIST = []
            HRAIDLGP_accumulator_LIST = []
            HRAIDOF2_accumulator_LIST = []
            HRAIDN01_accumulator_LIST = []
            HRAIDN02_accumulator_LIST = []
            HRAIDN03_accumulator_LIST = []
            HRAIDN04_accumulator_LIST = []
            HRAIDN05_accumulator_LIST = []
            HRAIDN06_accumulator_LIST = []
            HRAIDN07_accumulator_LIST = []
            HRAIDN08_accumulator_LIST = []
            HRAIDN09_accumulator_LIST = []
            HRAIDN10_accumulator_LIST = []
            HRAIDN11_accumulator_LIST = []
            HRAUDTRN_accumulator_LIST = []
            HRALDS_accumulator_LIST = []
            HRALDT01_accumulator_LIST = []
            HRALDT02_accumulator_LIST = []
            HRALDT03_accumulator_LIST = []
            HRALDT04_accumulator_LIST = []
            HRALDT05_accumulator_LIST = []
            HRALDT06_accumulator_LIST = []
            HRALDT07_accumulator_LIST = []
            HRALDT08_accumulator_LIST = []
            HRALDT09_accumulator_LIST = []
            HRALDT10_accumulator_LIST = []
            HRALDT11_accumulator_LIST = []
            HRBDIZZ_accumulator_LIST = []
            HRTIN_accumulator_LIST = []
            HRTINOFT_accumulator_LIST = []
            HRTINLNG_accumulator_LIST = []
            HRTINMUS_accumulator_LIST = []
            HRTINSLP_accumulator_LIST = []
            HRTINPRO_accumulator_LIST = []
            HRTINDIS_accumulator_LIST = []
            HRTINDOC_accumulator_LIST = []
            HRTINRM_accumulator_LIST = []
            HREMTY01_accumulator_LIST = []
            HREMTY02_accumulator_LIST = []
            HREMTY03_accumulator_LIST = []
            HREMTY04_accumulator_LIST = []
            HREMTY05_accumulator_LIST = []
            HREMTY06_accumulator_LIST = []
            HREMTY07_accumulator_LIST = []
            HREMTY08_accumulator_LIST = []
            HREMTY09_accumulator_LIST = []
            HREMTY10_accumulator_LIST = []
            HREMTY11_accumulator_LIST = []
            HREMTY12_accumulator_LIST = []
            HRTNRMHP_accumulator_LIST = []
            HRHCUSIS_accumulator_LIST = []
            HRHCPROB_accumulator_LIST = []
            HRFIRE_accumulator_LIST = []
            HRFIRTYP_accumulator_LIST = []
            HRFRTIM_accumulator_LIST = []
            HR12MR_accumulator_LIST = []
            HRFRPROT_accumulator_LIST = []
            HRTOTR_accumulator_LIST = []
            HRFRPRT2_accumulator_LIST = []
            HRWKVLNS_accumulator_LIST = []
            HRWKLNS_accumulator_LIST = []
            HRWKVLNT_accumulator_LIST = []
            HRWKVLEX_accumulator_LIST = []
            HRWKVLP1_accumulator_LIST = []
            HRWKVLP2_accumulator_LIST = []
            HRWRLNS_accumulator_LIST = []
            HRWKLEX_accumulator_LIST = []
            HRWKLP1_accumulator_LIST = []
            HRWKLP2_accumulator_LIST = []
            HRLSVLNS_accumulator_LIST = []
            HRVLTP01_accumulator_LIST = []
            HRVLTP02_accumulator_LIST = []
            HRVLTP03_accumulator_LIST = []
            HRVLTP04_accumulator_LIST = []
            HRVLTP05_accumulator_LIST = []
            HRVLTP06_accumulator_LIST = []
            HRVLTP07_accumulator_LIST = []
            HRVLTP08_accumulator_LIST = []
            HRVLTP09_accumulator_LIST = []
            HRVLTP10_accumulator_LIST = []
            HRLNOS_accumulator_LIST = []
            HRLTP01_accumulator_LIST = []
            HRLTP02_accumulator_LIST = []
            HRLTP03_accumulator_LIST = []
            HRLTP04_accumulator_LIST = []
            HRLTP05_accumulator_LIST = []
            HRLTP06_accumulator_LIST = []
            HRLTP07_accumulator_LIST = []
            HRLTP08_accumulator_LIST = []
            HRLTP09_accumulator_LIST = []
            HRLTP10_accumulator_LIST = []
            HRNOSEXP_accumulator_LIST = []
            HRLSP1_accumulator_LIST = []
            HRLSP2_accumulator_LIST = []
            HRINTNET_accumulator_LIST = []
            HRINTHL_accumulator_LIST = []
            HRINTHA_accumulator_LIST = []
            HRINTTN_accumulator_LIST = []
            HRINTDZ_accumulator_LIST = []
            HRINTHP_accumulator_LIST = []
            HRINTHPR_accumulator_LIST = []
            AVISION_accumulator_LIST = []
            ABLIND_accumulator_LIST = []
            LUPPRT_accumulator_LIST = []
            WKDAYR_accumulator_LIST = []
            BEDDAYR_accumulator_LIST = []
            AHSTATYR_accumulator_LIST = []
            SPECEQ_accumulator_LIST = []
            FLWALK_accumulator_LIST = []
            FLCLIMB_accumulator_LIST = []
            FLSTAND_accumulator_LIST = []
            FLSIT_accumulator_LIST = []
            FLSTOOP_accumulator_LIST = []
            FLREACH_accumulator_LIST = []
            FLGRASP_accumulator_LIST = []
            FLCARRY_accumulator_LIST = []
            FLPUSH_accumulator_LIST = []
            FLSHOP_accumulator_LIST = []
            FLSOCL_accumulator_LIST = []
            FLRELAX_accumulator_LIST = []
            FLA1AR_accumulator_LIST = []
            AFLHCA1_accumulator_LIST = []
            AFLHCA2_accumulator_LIST = []
            AFLHCA3_accumulator_LIST = []
            AFLHCA4_accumulator_LIST = []
            AFLHCA5_accumulator_LIST = []
            AFLHCA6_accumulator_LIST = []
            AFLHCA7_accumulator_LIST = []
            AFLHCA8_accumulator_LIST = []
            AFLHCA9_accumulator_LIST = []
            AFLHCA10_accumulator_LIST = []
            AFLHCA11_accumulator_LIST = []
            AFLHCA12_accumulator_LIST = []
            AFLHCA13_accumulator_LIST = []
            ALHCA14A_accumulator_LIST = []
            AFLHCA15_accumulator_LIST = []
            AFLHCA16_accumulator_LIST = []
            AFLHCA17_accumulator_LIST = []
            AFLHCA18_accumulator_LIST = []
            AFLHC19__accumulator_LIST = []
            AFLHC20__accumulator_LIST = []
            AFLHC21__accumulator_LIST = []
            AFLHC22__accumulator_LIST = []
            AFLHC23__accumulator_LIST = []
            AFLHC24__accumulator_LIST = []
            AFLHC25__accumulator_LIST = []
            AFLHC26__accumulator_LIST = []
            AFLHC27__accumulator_LIST = []
            AFLHC28__accumulator_LIST = []
            AFLHC29__accumulator_LIST = []
            AFLHC30__accumulator_LIST = []
            AFLHC31__accumulator_LIST = []
            AFLHC32__accumulator_LIST = []
            AFLHC33__accumulator_LIST = []
            AFLHC34__accumulator_LIST = []
            AFLHCA90_accumulator_LIST = []
            AFLHCA91_accumulator_LIST = []
            ALTIME1_accumulator_LIST = []
            ALUNIT1_accumulator_LIST = []
            ALDURA1_accumulator_LIST = []
            ALDURB1_accumulator_LIST = []
            ALCHRC1_accumulator_LIST = []
            ALTIME2_accumulator_LIST = []
            ALUNIT2_accumulator_LIST = []
            ALDURA2_accumulator_LIST = []
            ALDURB2_accumulator_LIST = []
            ALCHRC2_accumulator_LIST = []
            ALTIME3_accumulator_LIST = []
            ALUNIT3_accumulator_LIST = []
            ALDURA3_accumulator_LIST = []
            ALDURB3_accumulator_LIST = []
            ALCHRC3_accumulator_LIST = []
            ALTIME4_accumulator_LIST = []
            ALUNIT4_accumulator_LIST = []
            ALDURA4_accumulator_LIST = []
            ALDURB4_accumulator_LIST = []
            ALCHRC4_accumulator_LIST = []
            ALTIME5_accumulator_LIST = []
            ALUNIT5_accumulator_LIST = []
            ALDURA5_accumulator_LIST = []
            ALDURB5_accumulator_LIST = []
            ALCHRC5_accumulator_LIST = []
            ALTIME6_accumulator_LIST = []
            ALUNIT6_accumulator_LIST = []
            ALDURA6_accumulator_LIST = []
            ALDURB6_accumulator_LIST = []
            ALCHRC6_accumulator_LIST = []
            ALTIME7_accumulator_LIST = []
            ALUNIT7_accumulator_LIST = []
            ALDURA7_accumulator_LIST = []
            ALDURB7_accumulator_LIST = []
            ALCHRC7_accumulator_LIST = []
            ALTIME8_accumulator_LIST = []
            ALUNIT8_accumulator_LIST = []
            ALDURA8_accumulator_LIST = []
            ALDURB8_accumulator_LIST = []
            ALCHRC8_accumulator_LIST = []
            ALTIME9_accumulator_LIST = []
            ALUNIT9_accumulator_LIST = []
            ALDURA9_accumulator_LIST = []
            ALDURB9_accumulator_LIST = []
            ALCHRC9_accumulator_LIST = []
            ALTIME10_accumulator_LIST = []
            ALUNIT10_accumulator_LIST = []
            ALDURA10_accumulator_LIST = []
            ALDURB10_accumulator_LIST = []
            ALCHRC10_accumulator_LIST = []
            ALTIME11_accumulator_LIST = []
            ALUNIT11_accumulator_LIST = []
            ALDURA11_accumulator_LIST = []
            ALDURB11_accumulator_LIST = []
            ALCHRC11_accumulator_LIST = []
            ALTIME12_accumulator_LIST = []
            ALUNIT12_accumulator_LIST = []
            ALDURA12_accumulator_LIST = []
            ALDURB12_accumulator_LIST = []
            ALCHRC12_accumulator_LIST = []
            ALTIME13_accumulator_LIST = []
            ALUNIT13_accumulator_LIST = []
            ALDURA13_accumulator_LIST = []
            ALDURB13_accumulator_LIST = []
            ALCHRC13_accumulator_LIST = []
            ATIME14A_accumulator_LIST = []
            AUNIT14A_accumulator_LIST = []
            ADURA14A_accumulator_LIST = []
            ADURB14A_accumulator_LIST = []
            ACHRC14A_accumulator_LIST = []
            ALTIME15_accumulator_LIST = []
            ALUNIT15_accumulator_LIST = []
            ALDURA15_accumulator_LIST = []
            ALDURB15_accumulator_LIST = []
            ALCHRC15_accumulator_LIST = []
            ALTIME16_accumulator_LIST = []
            ALUNIT16_accumulator_LIST = []
            ALDURA16_accumulator_LIST = []
            ALDURB16_accumulator_LIST = []
            ALCHRC16_accumulator_LIST = []
            ALTIME17_accumulator_LIST = []
            ALUNIT17_accumulator_LIST = []
            ALDURA17_accumulator_LIST = []
            ALDURB17_accumulator_LIST = []
            ALCHRC17_accumulator_LIST = []
            ALTIME18_accumulator_LIST = []
            ALUNIT18_accumulator_LIST = []
            ALDURA18_accumulator_LIST = []
            ALDURB18_accumulator_LIST = []
            ALCHRC18_accumulator_LIST = []
            ALTIME19_accumulator_LIST = []
            ALUNIT19_accumulator_LIST = []
            ALDURA19_accumulator_LIST = []
            ALDURB19_accumulator_LIST = []
            ALCHRC19_accumulator_LIST = []
            ALTIME20_accumulator_LIST = []
            ALUNIT20_accumulator_LIST = []
            ALDURA20_accumulator_LIST = []
            ALDURB20_accumulator_LIST = []
            ALCHRC20_accumulator_LIST = []
            ALTIME21_accumulator_LIST = []
            ALUNIT21_accumulator_LIST = []
            ALDURA21_accumulator_LIST = []
            ALDURB21_accumulator_LIST = []
            ALCHRC21_accumulator_LIST = []
            ALTIME22_accumulator_LIST = []
            ALUNIT22_accumulator_LIST = []
            ALDURA22_accumulator_LIST = []
            ALDURB22_accumulator_LIST = []
            ALCHRC22_accumulator_LIST = []
            ALTIME23_accumulator_LIST = []
            ALUNIT23_accumulator_LIST = []
            ALDURA23_accumulator_LIST = []
            ALDURB23_accumulator_LIST = []
            ALCHRC23_accumulator_LIST = []
            ALTIME24_accumulator_LIST = []
            ALUNIT24_accumulator_LIST = []
            ALDURA24_accumulator_LIST = []
            ALDURB24_accumulator_LIST = []
            ALCHRC24_accumulator_LIST = []
            ALTIME25_accumulator_LIST = []
            ALUNIT25_accumulator_LIST = []
            ALDURA25_accumulator_LIST = []
            ALDURB25_accumulator_LIST = []
            ALCHRC25_accumulator_LIST = []
            ALTIME26_accumulator_LIST = []
            ALUNIT26_accumulator_LIST = []
            ALDURA26_accumulator_LIST = []
            ALDURB26_accumulator_LIST = []
            ALCHRC26_accumulator_LIST = []
            ALTIME27_accumulator_LIST = []
            ALUNIT27_accumulator_LIST = []
            ALDURA27_accumulator_LIST = []
            ALDURB27_accumulator_LIST = []
            ALCHRC27_accumulator_LIST = []
            ALTIME28_accumulator_LIST = []
            ALUNIT28_accumulator_LIST = []
            ALDURA28_accumulator_LIST = []
            ALDURB28_accumulator_LIST = []
            ALCHRC28_accumulator_LIST = []
            ALTIME29_accumulator_LIST = []
            ALUNIT29_accumulator_LIST = []
            ALDURA29_accumulator_LIST = []
            ALDURB29_accumulator_LIST = []
            ALCHRC29_accumulator_LIST = []
            ALTIME30_accumulator_LIST = []
            ALUNIT30_accumulator_LIST = []
            ALDURA30_accumulator_LIST = []
            ALDURB30_accumulator_LIST = []
            ALCHRC30_accumulator_LIST = []
            ALTIME31_accumulator_LIST = []
            ALUNIT31_accumulator_LIST = []
            ALDURA31_accumulator_LIST = []
            ALDURB31_accumulator_LIST = []
            ALCHRC31_accumulator_LIST = []
            ALTIME32_accumulator_LIST = []
            ALUNIT32_accumulator_LIST = []
            ALDURA32_accumulator_LIST = []
            ALDURB32_accumulator_LIST = []
            ALCHRC32_accumulator_LIST = []
            ALTIME33_accumulator_LIST = []
            ALUNIT33_accumulator_LIST = []
            ALDURA33_accumulator_LIST = []
            ALDURB33_accumulator_LIST = []
            ALCHRC33_accumulator_LIST = []
            ALTIME34_accumulator_LIST = []
            ALUNIT34_accumulator_LIST = []
            ALDURA34_accumulator_LIST = []
            ALDURB34_accumulator_LIST = []
            ALCHRC34_accumulator_LIST = []
            ALTIME90_accumulator_LIST = []
            ALUNIT90_accumulator_LIST = []
            ALDURA90_accumulator_LIST = []
            ALDURB90_accumulator_LIST = []
            ALCHRC90_accumulator_LIST = []
            ALTIME91_accumulator_LIST = []
            ALUNIT91_accumulator_LIST = []
            ALDURA91_accumulator_LIST = []
            ALDURB91_accumulator_LIST = []
            ALCHRC91_accumulator_LIST = []
            ALCNDRT_accumulator_LIST = []
            ALCHRONR_accumulator_LIST = []
            SMKEV_accumulator_LIST = []
            SMKREG_accumulator_LIST = []
            SMKNOW_accumulator_LIST = []
            SMKSTAT2_accumulator_LIST = []
            SMKQTNO_accumulator_LIST = []
            SMKQTTP_accumulator_LIST = []
            SMKQTY_accumulator_LIST = []
            CIGSDA1_accumulator_LIST = []
            CIGDAMO_accumulator_LIST = []
            CIGSDA2_accumulator_LIST = []
            CIGSDAY_accumulator_LIST = []
            CIGQTYR_accumulator_LIST = []
            OTHCIGEV_accumulator_LIST = []
            OTHCIGED_accumulator_LIST = []
            SMKLESEV_accumulator_LIST = []
            SMKLESED_accumulator_LIST = []
            TOBLASYR_accumulator_LIST = []
            TOBQTYR_accumulator_LIST = []
            ECIGEV_accumulator_LIST = []
            ECIGED_accumulator_LIST = []
            VIGNO_accumulator_LIST = []
            VIGTP_accumulator_LIST = []
            VIGFREQW_accumulator_LIST = []
            VIGLNGNO_accumulator_LIST = []
            VIGLNGTP_accumulator_LIST = []
            VIGMIN_accumulator_LIST = []
            MODNO_accumulator_LIST = []
            MODTP_accumulator_LIST = []
            MODFREQW_accumulator_LIST = []
            MODLNGNO_accumulator_LIST = []
            MODLNGTP_accumulator_LIST = []
            MODMIN_accumulator_LIST = []
            STRNGNO_accumulator_LIST = []
            STRNGTP_accumulator_LIST = []
            STRFREQW_accumulator_LIST = []
            ALC1YR_accumulator_LIST = []
            ALCLIFE_accumulator_LIST = []
            ALC12MNO_accumulator_LIST = []
            ALC12MTP_accumulator_LIST = []
            ALC12MWK_accumulator_LIST = []
            ALC12MYR_accumulator_LIST = []
            ALCAMT_accumulator_LIST = []
            ALCSTAT_accumulator_LIST = []
            ALC5UPN1_accumulator_LIST = []
            ALC5UPT1_accumulator_LIST = []
            ALC5UPY1_accumulator_LIST = []
            AHEIGHT_accumulator_LIST = []
            AWEIGHTP_accumulator_LIST = []
            BMI_accumulator_LIST = []
            AUSUALPL_accumulator_LIST = []
            APLKIND_accumulator_LIST = []
            AHCPLROU_accumulator_LIST = []
            AHCPLKND_accumulator_LIST = []
            AHCCHGYR_accumulator_LIST = []
            AHCCHGHI_accumulator_LIST = []
            ANOUSPL1_accumulator_LIST = []
            ANOUSPL2_accumulator_LIST = []
            ANOUSPL3_accumulator_LIST = []
            ANOUSPL4_accumulator_LIST = []
            ANOUSPL5_accumulator_LIST = []
            ANOUSPL6_accumulator_LIST = []
            ANOUSPL7_accumulator_LIST = []
            ANOUSPL8_accumulator_LIST = []
            ANOUSPL9_accumulator_LIST = []
            APRVTRYR_accumulator_LIST = []
            APRVTRFD_accumulator_LIST = []
            ADRNANP_accumulator_LIST = []
            ADRNAI_accumulator_LIST = []
            AHCDLYR1_accumulator_LIST = []
            AHCDLYR2_accumulator_LIST = []
            AHCDLYR3_accumulator_LIST = []
            AHCDLYR4_accumulator_LIST = []
            AHCDLYR5_accumulator_LIST = []
            AHCAFYR1_accumulator_LIST = []
            AHCAFYR2_accumulator_LIST = []
            AHCAFYR3_accumulator_LIST = []
            AHCAFYR4_accumulator_LIST = []
            AHCAFYR5_accumulator_LIST = []
            AHCAFYR6_accumulator_LIST = []
            AWORPAY_accumulator_LIST = []
            AHICOMP_accumulator_LIST = []
            ARX12MO_accumulator_LIST = []
            ARX12_1_accumulator_LIST = []
            ARX12_2_accumulator_LIST = []
            ARX12_3_accumulator_LIST = []
            ARX12_4_accumulator_LIST = []
            ARX12_5_accumulator_LIST = []
            ARX12_6_accumulator_LIST = []
            ADNLONG2_accumulator_LIST = []
            AHCSYR1_accumulator_LIST = []
            AHCSYR2_accumulator_LIST = []
            AHCSYR3_accumulator_LIST = []
            AHCSYR4_accumulator_LIST = []
            AHCSYR5_accumulator_LIST = []
            AHCSYR6_accumulator_LIST = []
            AHCSYR7_accumulator_LIST = []
            AHCSYR8_accumulator_LIST = []
            AHCSYR9_accumulator_LIST = []
            AHCSYR10_accumulator_LIST = []
            AHERNOY2_accumulator_LIST = []
            AERVISND_accumulator_LIST = []
            AERHOS_accumulator_LIST = []
            AERREA1R_accumulator_LIST = []
            AERREA2R_accumulator_LIST = []
            AERREA3R_accumulator_LIST = []
            AERREA4R_accumulator_LIST = []
            AERREA5R_accumulator_LIST = []
            AERREA6R_accumulator_LIST = []
            AERREA7R_accumulator_LIST = []
            AERREA8R_accumulator_LIST = []
            AHCHYR_accumulator_LIST = []
            AHCHMOYR_accumulator_LIST = []
            AHCHNOY2_accumulator_LIST = []
            AHCNOYR2_accumulator_LIST = []
            ASRGYR_accumulator_LIST = []
            ASRGNOYR_accumulator_LIST = []
            AMDLONGR_accumulator_LIST = []
            AVISLAST_accumulator_LIST = []
            ALASTYP1_accumulator_LIST = []
            ALASTYP2_accumulator_LIST = []
            ALASTYP3_accumulator_LIST = []
            ALASTYP4_accumulator_LIST = []
            ALASTVRB_accumulator_LIST = []
            AVISAPN2_accumulator_LIST = []
            AVISAPT2_accumulator_LIST = []
            AWAITRMN_accumulator_LIST = []
            AWAITRMT_accumulator_LIST = []
            HIT1A_accumulator_LIST = []
            HIT2A_accumulator_LIST = []
            HIT3A_accumulator_LIST = []
            HIT4A_accumulator_LIST = []
            HIT5A_accumulator_LIST = []
            SHTFLU2_accumulator_LIST = []
            ASHFLUM2_accumulator_LIST = []
            ASHFLUY2_accumulator_LIST = []
            FLUSHPG1_accumulator_LIST = []
            FLUSHPG2_accumulator_LIST = []
            SPRFLU2_accumulator_LIST = []
            ASPFLUM2_accumulator_LIST = []
            ASPFLUY2_accumulator_LIST = []
            SHTPNUYR_accumulator_LIST = []
            APOX_accumulator_LIST = []
            APOX12MO_accumulator_LIST = []
            AHEP_accumulator_LIST = []
            AHEPLIV_accumulator_LIST = []
            AHEPBTST_accumulator_LIST = []
            SHTHEPB_accumulator_LIST = []
            SHEPDOS_accumulator_LIST = []
            SHTHEPA_accumulator_LIST = []
            SHEPANUM_accumulator_LIST = []
            AHEPCTST_accumulator_LIST = []
            AHEPCRES_accumulator_LIST = []
            SHINGLES_accumulator_LIST = []
            SHTTD_accumulator_LIST = []
            SHTTD05_accumulator_LIST = []
            SHTTDAP2_accumulator_LIST = []
            SHTHPV2_accumulator_LIST = []
            SHHPVDOS_accumulator_LIST = []
            AHPVAGE_accumulator_LIST = []
            LIVEV_accumulator_LIST = []
            TRAVEL_accumulator_LIST = []
            WRKHLTH2_accumulator_LIST = []
            WRKDIR_accumulator_LIST = []
            APSBPCH1_accumulator_LIST = []
            APSCHCH1_accumulator_LIST = []
            APSBSCH1_accumulator_LIST = []
            APSPAP_accumulator_LIST = []
            APSMAM_accumulator_LIST = []
            APSCOL_accumulator_LIST = []
            APSDIET_accumulator_LIST = []
            APSSMKC_accumulator_LIST = []
            LTCFAM_accumulator_LIST = []
            LTCHELP_accumulator_LIST = []
            LTCWHO1_accumulator_LIST = []
            LTCWHO2_accumulator_LIST = []
            LTCWHO3_accumulator_LIST = []
            LTCWHO4_accumulator_LIST = []
            LTCWHO5_accumulator_LIST = []
            AINDINS_accumulator_LIST = []
            AINDPRCH_accumulator_LIST = []
            AINDWHO_accumulator_LIST = []
            AINDDIF1_accumulator_LIST = []
            AINDDIF2_accumulator_LIST = []
            AINDENY1_accumulator_LIST = []
            AINDENY2_accumulator_LIST = []
            AINDENY3_accumulator_LIST = []
            AINDNOT1_accumulator_LIST = []
            AINDNOT2_accumulator_LIST = []
            AINDNOT3_accumulator_LIST = []
            AINDNOT4_accumulator_LIST = []
            AINDNOT5_accumulator_LIST = []
            AEXCHNG_accumulator_LIST = []
            ASICPUSE_accumulator_LIST = []
            ASISATHC_accumulator_LIST = []
            ASITENUR_accumulator_LIST = []
            ASINHELP_accumulator_LIST = []
            ASINCNTO_accumulator_LIST = []
            ASINTRU_accumulator_LIST = []
            ASINKNT_accumulator_LIST = []
            ASISIM_accumulator_LIST = []
            ASISIF_accumulator_LIST = []
            ASIRETR_accumulator_LIST = []
            ASIMEDC_accumulator_LIST = []
            ASISTLV_accumulator_LIST = []
            ASICNHC_accumulator_LIST = []
            ASICCOLL_accumulator_LIST = []
            ASINBILL_accumulator_LIST = []
            ASIHCST_accumulator_LIST = []
            ASICCMP_accumulator_LIST = []
            ASISLEEP_accumulator_LIST = []
            ASISLPFL_accumulator_LIST = []
            ASISLPST_accumulator_LIST = []
            ASISLPMD_accumulator_LIST = []
            ASIREST_accumulator_LIST = []
            ASISAD_accumulator_LIST = []
            ASINERV_accumulator_LIST = []
            ASIRSTLS_accumulator_LIST = []
            ASIHOPLS_accumulator_LIST = []
            ASIEFFRT_accumulator_LIST = []
            ASIWTHLS_accumulator_LIST = []
            ASIMUCH_accumulator_LIST = []
            ASIHIVT_accumulator_LIST = []
            ASIHIVWN_accumulator_LIST = []
            AWEBUSE_accumulator_LIST = []
            AWEBOFNO_accumulator_LIST = []
            AWEBOFTP_accumulator_LIST = []
            AWEBORP_accumulator_LIST = []
            AWEBEML_accumulator_LIST = []
            AWEBMNO_accumulator_LIST = []
            AWEBMTP_accumulator_LIST = []

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
                    WTIA_SA_accumulator_LIST.append(char)
                    WTIA_SA = ''.join(WTIA_SA_accumulator_LIST)
                elif 25 < cdx < 32:
                    WTFA_SA_accumulator_LIST.append(char)
                    WTFA_SA = ''.join(WTFA_SA_accumulator_LIST)
                elif 31 < cdx < 33:
                    REGION_accumulator_LIST.append(char)
                    REGION = ''.join(REGION_accumulator_LIST)
                elif 32 < cdx < 36:
                    STRAT_P_accumulator_LIST.append(char)
                    STRAT_P = ''.join(STRAT_P_accumulator_LIST)
                elif 35 < cdx < 38:
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
                elif 48 < cdx < 50:
                    R_MARITL_accumulator_LIST.append(char)
                    R_MARITL = ''.join(R_MARITL_accumulator_LIST)
                elif 49 < cdx < 51:
                    PROXYSA_accumulator_LIST.append(char)
                    PROXYSA = ''.join(PROXYSA_accumulator_LIST)
                elif 50 < cdx < 52:
                    PROX1_accumulator_LIST.append(char)
                    PROX1 = ''.join(PROX1_accumulator_LIST)
                elif 51 < cdx < 53:
                    PROX2_accumulator_LIST.append(char)
                    PROX2 = ''.join(PROX2_accumulator_LIST)
                elif 52 < cdx < 54:
                    LATEINTA_accumulator_LIST.append(char)
                    LATEINTA = ''.join(LATEINTA_accumulator_LIST)
                elif 53 < cdx < 55:
                    FDRN_FLG_accumulator_LIST.append(char)
                    FDRN_FLG = ''.join(FDRN_FLG_accumulator_LIST)
                elif 54 < cdx < 56:
                    DOINGLWA_accumulator_LIST.append(char)
                    DOINGLWA = ''.join(DOINGLWA_accumulator_LIST)
                elif 55 < cdx < 58:
                    WHYNOWKA_accumulator_LIST.append(char)
                    WHYNOWKA = ''.join(WHYNOWKA_accumulator_LIST)
                elif 57 < cdx < 59:
                    EVERWRK_accumulator_LIST.append(char)
                    EVERWRK = ''.join(EVERWRK_accumulator_LIST)
                elif 58 < cdx < 61:
                    INDSTRN1_accumulator_LIST.append(char)
                    INDSTRN1 = ''.join(INDSTRN1_accumulator_LIST)
                elif 60 < cdx < 63:
                    INDSTRN2_accumulator_LIST.append(char)
                    INDSTRN2 = ''.join(INDSTRN2_accumulator_LIST)
                elif 62 < cdx < 65:
                    OCCUPN1_accumulator_LIST.append(char)
                    OCCUPN1 = ''.join(OCCUPN1_accumulator_LIST)
                elif 64 < cdx < 67:
                    OCCUPN2_accumulator_LIST.append(char)
                    OCCUPN2 = ''.join(OCCUPN2_accumulator_LIST)
                elif 66 < cdx < 68:
                    WRKCATA_accumulator_LIST.append(char)
                    WRKCATA = ''.join(WRKCATA_accumulator_LIST)
                elif 67 < cdx < 69:
                    BUSINC1A_accumulator_LIST.append(char)
                    BUSINC1A = ''.join(BUSINC1A_accumulator_LIST)
                elif 68 < cdx < 71:
                    LOCALL1A_accumulator_LIST.append(char)
                    LOCALL1A = ''.join(LOCALL1A_accumulator_LIST)
                elif 70 < cdx < 73:
                    YRSWRKPA_accumulator_LIST.append(char)
                    YRSWRKPA = ''.join(YRSWRKPA_accumulator_LIST)
                elif 72 < cdx < 74:
                    WRKLONGH_accumulator_LIST.append(char)
                    WRKLONGH = ''.join(WRKLONGH_accumulator_LIST)
                elif 73 < cdx < 75:
                    HOURPDA_accumulator_LIST.append(char)
                    HOURPDA = ''.join(HOURPDA_accumulator_LIST)
                elif 74 < cdx < 76:
                    PDSICKA_accumulator_LIST.append(char)
                    PDSICKA = ''.join(PDSICKA_accumulator_LIST)
                elif 75 < cdx < 77:
                    ONEJOB_accumulator_LIST.append(char)
                    ONEJOB = ''.join(ONEJOB_accumulator_LIST)
                elif 76 < cdx < 78:
                    WRKLYR4_accumulator_LIST.append(char)
                    WRKLYR4 = ''.join(WRKLYR4_accumulator_LIST)
                elif 77 < cdx < 79:
                    HYPEV_accumulator_LIST.append(char)
                    HYPEV = ''.join(HYPEV_accumulator_LIST)
                elif 78 < cdx < 80:
                    HYPDIFV_accumulator_LIST.append(char)
                    HYPDIFV = ''.join(HYPDIFV_accumulator_LIST)
                elif 79 < cdx < 81:
                    HYPYR1_accumulator_LIST.append(char)
                    HYPYR1 = ''.join(HYPYR1_accumulator_LIST)
                elif 80 < cdx < 83:
                    HYBPCKNO_accumulator_LIST.append(char)
                    HYBPCKNO = ''.join(HYBPCKNO_accumulator_LIST)
                elif 82 < cdx < 84:
                    HYBPCKTP_accumulator_LIST.append(char)
                    HYBPCKTP = ''.join(HYBPCKTP_accumulator_LIST)
                elif 83 < cdx < 85:
                    HYBPLEV_accumulator_LIST.append(char)
                    HYBPLEV = ''.join(HYBPLEV_accumulator_LIST)
                elif 84 < cdx < 86:
                    HYPMDEV2_accumulator_LIST.append(char)
                    HYPMDEV2 = ''.join(HYPMDEV2_accumulator_LIST)
                elif 85 < cdx < 87:
                    HYPMED2_accumulator_LIST.append(char)
                    HYPMED2 = ''.join(HYPMED2_accumulator_LIST)
                elif 86 < cdx < 88:
                    CHLEV_accumulator_LIST.append(char)
                    CHLEV = ''.join(CHLEV_accumulator_LIST)
                elif 87 < cdx < 89:
                    CHLYR_accumulator_LIST.append(char)
                    CHLYR = ''.join(CHLYR_accumulator_LIST)
                elif 88 < cdx < 91:
                    CLCKNO_accumulator_LIST.append(char)
                    CLCKNO = ''.join(CLCKNO_accumulator_LIST)
                elif 90 < cdx < 92:
                    CLCKTP_accumulator_LIST.append(char)
                    CLCKTP = ''.join(CLCKTP_accumulator_LIST)
                elif 91 < cdx < 93:
                    CHLMDEV2_accumulator_LIST.append(char)
                    CHLMDEV2 = ''.join(CHLMDEV2_accumulator_LIST)
                elif 92 < cdx < 94:
                    CHLMDNW2_accumulator_LIST.append(char)
                    CHLMDNW2 = ''.join(CHLMDNW2_accumulator_LIST)
                elif 93 < cdx < 95:
                    CHDEV_accumulator_LIST.append(char)
                    CHDEV = ''.join(CHDEV_accumulator_LIST)
                elif 94 < cdx < 96:
                    ANGEV_accumulator_LIST.append(char)
                    ANGEV = ''.join(ANGEV_accumulator_LIST)
                elif 95 < cdx < 97:
                    MIEV_accumulator_LIST.append(char)
                    MIEV = ''.join(MIEV_accumulator_LIST)
                elif 96 < cdx < 98:
                    HRTEV_accumulator_LIST.append(char)
                    HRTEV = ''.join(HRTEV_accumulator_LIST)
                elif 97 < cdx < 99:
                    STREV_accumulator_LIST.append(char)
                    STREV = ''.join(STREV_accumulator_LIST)
                elif 98 < cdx < 100:
                    EPHEV_accumulator_LIST.append(char)
                    EPHEV = ''.join(EPHEV_accumulator_LIST)
                elif 99 < cdx < 101:
                    JAWP_accumulator_LIST.append(char)
                    JAWP = ''.join(JAWP_accumulator_LIST)
                elif 100 < cdx < 102:
                    WEA_accumulator_LIST.append(char)
                    WEA = ''.join(WEA_accumulator_LIST)
                elif 101 < cdx < 103:
                    CHE_accumulator_LIST.append(char)
                    CHE = ''.join(CHE_accumulator_LIST)
                elif 102 < cdx < 104:
                    ARM_accumulator_LIST.append(char)
                    ARM = ''.join(ARM_accumulator_LIST)
                elif 103 < cdx < 105:
                    BRTH_accumulator_LIST.append(char)
                    BRTH = ''.join(BRTH_accumulator_LIST)
                elif 104 < cdx < 106:
                    AHADO_accumulator_LIST.append(char)
                    AHADO = ''.join(AHADO_accumulator_LIST)
                elif 105 < cdx < 107:
                    FACE_accumulator_LIST.append(char)
                    FACE = ''.join(FACE_accumulator_LIST)
                elif 106 < cdx < 108:
                    SPEAKING_accumulator_LIST.append(char)
                    SPEAKING = ''.join(SPEAKING_accumulator_LIST)
                elif 107 < cdx < 109:
                    EYE_accumulator_LIST.append(char)
                    EYE = ''.join(EYE_accumulator_LIST)
                elif 108 < cdx < 110:
                    WALKING_accumulator_LIST.append(char)
                    WALKING = ''.join(WALKING_accumulator_LIST)
                elif 109 < cdx < 111:
                    HEADACHE_accumulator_LIST.append(char)
                    HEADACHE = ''.join(HEADACHE_accumulator_LIST)
                elif 110 < cdx < 112:
                    ASTDO_accumulator_LIST.append(char)
                    ASTDO = ''.join(ASTDO_accumulator_LIST)
                elif 111 < cdx < 113:
                    COPDEV_accumulator_LIST.append(char)
                    COPDEV = ''.join(COPDEV_accumulator_LIST)
                elif 112 < cdx < 114:
                    ASPMEDEV_accumulator_LIST.append(char)
                    ASPMEDEV = ''.join(ASPMEDEV_accumulator_LIST)
                elif 113 < cdx < 115:
                    ASPMEDAD_accumulator_LIST.append(char)
                    ASPMEDAD = ''.join(ASPMEDAD_accumulator_LIST)
                elif 114 < cdx < 116:
                    ASPMDMED_accumulator_LIST.append(char)
                    ASPMDMED = ''.join(ASPMDMED_accumulator_LIST)
                elif 115 < cdx < 117:
                    ASPONOWN_accumulator_LIST.append(char)
                    ASPONOWN = ''.join(ASPONOWN_accumulator_LIST)
                elif 116 < cdx < 118:
                    AASMEV_accumulator_LIST.append(char)
                    AASMEV = ''.join(AASMEV_accumulator_LIST)
                elif 117 < cdx < 119:
                    AASSTILL_accumulator_LIST.append(char)
                    AASSTILL = ''.join(AASSTILL_accumulator_LIST)
                elif 118 < cdx < 120:
                    AASMYR_accumulator_LIST.append(char)
                    AASMYR = ''.join(AASMYR_accumulator_LIST)
                elif 119 < cdx < 121:
                    AASERYR1_accumulator_LIST.append(char)
                    AASERYR1 = ''.join(AASERYR1_accumulator_LIST)
                elif 120 < cdx < 122:
                    ULCEV_accumulator_LIST.append(char)
                    ULCEV = ''.join(ULCEV_accumulator_LIST)
                elif 121 < cdx < 123:
                    ULCYR_accumulator_LIST.append(char)
                    ULCYR = ''.join(ULCYR_accumulator_LIST)
                elif 122 < cdx < 124:
                    CANEV_accumulator_LIST.append(char)
                    CANEV = ''.join(CANEV_accumulator_LIST)
                elif 123 < cdx < 125:
                    CNKIND1_accumulator_LIST.append(char)
                    CNKIND1 = ''.join(CNKIND1_accumulator_LIST)
                elif 124 < cdx < 126:
                    CNKIND2_accumulator_LIST.append(char)
                    CNKIND2 = ''.join(CNKIND2_accumulator_LIST)
                elif 125 < cdx < 127:
                    CNKIND3_accumulator_LIST.append(char)
                    CNKIND3 = ''.join(CNKIND3_accumulator_LIST)
                elif 126 < cdx < 128:
                    CNKIND4_accumulator_LIST.append(char)
                    CNKIND4 = ''.join(CNKIND4_accumulator_LIST)
                elif 127 < cdx < 129:
                    CNKIND5_accumulator_LIST.append(char)
                    CNKIND5 = ''.join(CNKIND5_accumulator_LIST)
                elif 128 < cdx < 130:
                    CNKIND6_accumulator_LIST.append(char)
                    CNKIND6 = ''.join(CNKIND6_accumulator_LIST)
                elif 129 < cdx < 131:
                    CNKIND7_accumulator_LIST.append(char)
                    CNKIND7 = ''.join(CNKIND7_accumulator_LIST)
                elif 130 < cdx < 132:
                    CNKIND8_accumulator_LIST.append(char)
                    CNKIND8 = ''.join(CNKIND8_accumulator_LIST)
                elif 131 < cdx < 133:
                    CNKIND9_accumulator_LIST.append(char)
                    CNKIND9 = ''.join(CNKIND9_accumulator_LIST)
                elif 132 < cdx < 134:
                    CNKIND10_accumulator_LIST.append(char)
                    CNKIND10 = ''.join(CNKIND10_accumulator_LIST)
                elif 133 < cdx < 135:
                    CNKIND11_accumulator_LIST.append(char)
                    CNKIND11 = ''.join(CNKIND11_accumulator_LIST)
                elif 134 < cdx < 136:
                    CNKIND12_accumulator_LIST.append(char)
                    CNKIND12 = ''.join(CNKIND12_accumulator_LIST)
                elif 135 < cdx < 137:
                    CNKIND13_accumulator_LIST.append(char)
                    CNKIND13 = ''.join(CNKIND13_accumulator_LIST)
                elif 136 < cdx < 138:
                    CNKIND14_accumulator_LIST.append(char)
                    CNKIND14 = ''.join(CNKIND14_accumulator_LIST)
                elif 137 < cdx < 139:
                    CNKIND15_accumulator_LIST.append(char)
                    CNKIND15 = ''.join(CNKIND15_accumulator_LIST)
                elif 138 < cdx < 140:
                    CNKIND16_accumulator_LIST.append(char)
                    CNKIND16 = ''.join(CNKIND16_accumulator_LIST)
                elif 139 < cdx < 141:
                    CNKIND17_accumulator_LIST.append(char)
                    CNKIND17 = ''.join(CNKIND17_accumulator_LIST)
                elif 140 < cdx < 142:
                    CNKIND18_accumulator_LIST.append(char)
                    CNKIND18 = ''.join(CNKIND18_accumulator_LIST)
                elif 141 < cdx < 143:
                    CNKIND19_accumulator_LIST.append(char)
                    CNKIND19 = ''.join(CNKIND19_accumulator_LIST)
                elif 142 < cdx < 144:
                    CNKIND20_accumulator_LIST.append(char)
                    CNKIND20 = ''.join(CNKIND20_accumulator_LIST)
                elif 143 < cdx < 145:
                    CNKIND21_accumulator_LIST.append(char)
                    CNKIND21 = ''.join(CNKIND21_accumulator_LIST)
                elif 144 < cdx < 146:
                    CNKIND22_accumulator_LIST.append(char)
                    CNKIND22 = ''.join(CNKIND22_accumulator_LIST)
                elif 145 < cdx < 147:
                    CNKIND23_accumulator_LIST.append(char)
                    CNKIND23 = ''.join(CNKIND23_accumulator_LIST)
                elif 146 < cdx < 148:
                    CNKIND24_accumulator_LIST.append(char)
                    CNKIND24 = ''.join(CNKIND24_accumulator_LIST)
                elif 147 < cdx < 149:
                    CNKIND25_accumulator_LIST.append(char)
                    CNKIND25 = ''.join(CNKIND25_accumulator_LIST)
                elif 148 < cdx < 150:
                    CNKIND26_accumulator_LIST.append(char)
                    CNKIND26 = ''.join(CNKIND26_accumulator_LIST)
                elif 149 < cdx < 151:
                    CNKIND27_accumulator_LIST.append(char)
                    CNKIND27 = ''.join(CNKIND27_accumulator_LIST)
                elif 150 < cdx < 152:
                    CNKIND28_accumulator_LIST.append(char)
                    CNKIND28 = ''.join(CNKIND28_accumulator_LIST)
                elif 151 < cdx < 153:
                    CNKIND29_accumulator_LIST.append(char)
                    CNKIND29 = ''.join(CNKIND29_accumulator_LIST)
                elif 152 < cdx < 154:
                    CNKIND30_accumulator_LIST.append(char)
                    CNKIND30 = ''.join(CNKIND30_accumulator_LIST)
                elif 153 < cdx < 155:
                    CNKIND31_accumulator_LIST.append(char)
                    CNKIND31 = ''.join(CNKIND31_accumulator_LIST)
                elif 154 < cdx < 158:
                    CANAGE1_accumulator_LIST.append(char)
                    CANAGE1 = ''.join(CANAGE1_accumulator_LIST)
                elif 157 < cdx < 161:
                    CANAGE2_accumulator_LIST.append(char)
                    CANAGE2 = ''.join(CANAGE2_accumulator_LIST)
                elif 160 < cdx < 164:
                    CANAGE3_accumulator_LIST.append(char)
                    CANAGE3 = ''.join(CANAGE3_accumulator_LIST)
                elif 163 < cdx < 167:
                    CANAGE4_accumulator_LIST.append(char)
                    CANAGE4 = ''.join(CANAGE4_accumulator_LIST)
                elif 166 < cdx < 170:
                    CANAGE5_accumulator_LIST.append(char)
                    CANAGE5 = ''.join(CANAGE5_accumulator_LIST)
                elif 169 < cdx < 173:
                    CANAGE6_accumulator_LIST.append(char)
                    CANAGE6 = ''.join(CANAGE6_accumulator_LIST)
                elif 172 < cdx < 176:
                    CANAGE7_accumulator_LIST.append(char)
                    CANAGE7 = ''.join(CANAGE7_accumulator_LIST)
                elif 175 < cdx < 179:
                    CANAGE8_accumulator_LIST.append(char)
                    CANAGE8 = ''.join(CANAGE8_accumulator_LIST)
                elif 178 < cdx < 182:
                    CANAGE9_accumulator_LIST.append(char)
                    CANAGE9 = ''.join(CANAGE9_accumulator_LIST)
                elif 181 < cdx < 185:
                    CANAGE10_accumulator_LIST.append(char)
                    CANAGE10 = ''.join(CANAGE10_accumulator_LIST)
                elif 184 < cdx < 188:
                    CANAGE11_accumulator_LIST.append(char)
                    CANAGE11 = ''.join(CANAGE11_accumulator_LIST)
                elif 187 < cdx < 191:
                    CANAGE12_accumulator_LIST.append(char)
                    CANAGE12 = ''.join(CANAGE12_accumulator_LIST)
                elif 190 < cdx < 194:
                    CANAGE13_accumulator_LIST.append(char)
                    CANAGE13 = ''.join(CANAGE13_accumulator_LIST)
                elif 193 < cdx < 197:
                    CANAGE14_accumulator_LIST.append(char)
                    CANAGE14 = ''.join(CANAGE14_accumulator_LIST)
                elif 196 < cdx < 200:
                    CANAGE15_accumulator_LIST.append(char)
                    CANAGE15 = ''.join(CANAGE15_accumulator_LIST)
                elif 199 < cdx < 203:
                    CANAGE16_accumulator_LIST.append(char)
                    CANAGE16 = ''.join(CANAGE16_accumulator_LIST)
                elif 202 < cdx < 206:
                    CANAGE17_accumulator_LIST.append(char)
                    CANAGE17 = ''.join(CANAGE17_accumulator_LIST)
                elif 205 < cdx < 209:
                    CANAGE18_accumulator_LIST.append(char)
                    CANAGE18 = ''.join(CANAGE18_accumulator_LIST)
                elif 208 < cdx < 212:
                    CANAGE19_accumulator_LIST.append(char)
                    CANAGE19 = ''.join(CANAGE19_accumulator_LIST)
                elif 211 < cdx < 215:
                    CANAGE20_accumulator_LIST.append(char)
                    CANAGE20 = ''.join(CANAGE20_accumulator_LIST)
                elif 214 < cdx < 218:
                    CANAGE21_accumulator_LIST.append(char)
                    CANAGE21 = ''.join(CANAGE21_accumulator_LIST)
                elif 217 < cdx < 221:
                    CANAGE22_accumulator_LIST.append(char)
                    CANAGE22 = ''.join(CANAGE22_accumulator_LIST)
                elif 220 < cdx < 224:
                    CANAGE23_accumulator_LIST.append(char)
                    CANAGE23 = ''.join(CANAGE23_accumulator_LIST)
                elif 223 < cdx < 227:
                    CANAGE24_accumulator_LIST.append(char)
                    CANAGE24 = ''.join(CANAGE24_accumulator_LIST)
                elif 226 < cdx < 230:
                    CANAGE25_accumulator_LIST.append(char)
                    CANAGE25 = ''.join(CANAGE25_accumulator_LIST)
                elif 229 < cdx < 233:
                    CANAGE26_accumulator_LIST.append(char)
                    CANAGE26 = ''.join(CANAGE26_accumulator_LIST)
                elif 232 < cdx < 236:
                    CANAGE27_accumulator_LIST.append(char)
                    CANAGE27 = ''.join(CANAGE27_accumulator_LIST)
                elif 235 < cdx < 239:
                    CANAGE28_accumulator_LIST.append(char)
                    CANAGE28 = ''.join(CANAGE28_accumulator_LIST)
                elif 238 < cdx < 242:
                    CANAGE29_accumulator_LIST.append(char)
                    CANAGE29 = ''.join(CANAGE29_accumulator_LIST)
                elif 241 < cdx < 245:
                    CANAGE30_accumulator_LIST.append(char)
                    CANAGE30 = ''.join(CANAGE30_accumulator_LIST)
                elif 244 < cdx < 246:
                    DIBEV_accumulator_LIST.append(char)
                    DIBEV = ''.join(DIBEV_accumulator_LIST)
                elif 245 < cdx < 247:
                    DIBPRE1_accumulator_LIST.append(char)
                    DIBPRE1 = ''.join(DIBPRE1_accumulator_LIST)
                elif 246 < cdx < 249:
                    DIBAGE_accumulator_LIST.append(char)
                    DIBAGE = ''.join(DIBAGE_accumulator_LIST)
                elif 248 < cdx < 251:
                    DIFAGE2_accumulator_LIST.append(char)
                    DIFAGE2 = ''.join(DIFAGE2_accumulator_LIST)
                elif 250 < cdx < 252:
                    INSLN_accumulator_LIST.append(char)
                    INSLN = ''.join(INSLN_accumulator_LIST)
                elif 251 < cdx < 253:
                    DIBPILL_accumulator_LIST.append(char)
                    DIBPILL = ''.join(DIBPILL_accumulator_LIST)
                elif 252 < cdx < 254:
                    AHAYFYR_accumulator_LIST.append(char)
                    AHAYFYR = ''.join(AHAYFYR_accumulator_LIST)
                elif 253 < cdx < 255:
                    SINYR_accumulator_LIST.append(char)
                    SINYR = ''.join(SINYR_accumulator_LIST)
                elif 254 < cdx < 256:
                    CBRCHYR_accumulator_LIST.append(char)
                    CBRCHYR = ''.join(CBRCHYR_accumulator_LIST)
                elif 255 < cdx < 257:
                    KIDWKYR_accumulator_LIST.append(char)
                    KIDWKYR = ''.join(KIDWKYR_accumulator_LIST)
                elif 256 < cdx < 258:
                    LIVYR_accumulator_LIST.append(char)
                    LIVYR = ''.join(LIVYR_accumulator_LIST)
                elif 257 < cdx < 259:
                    JNTSYMP_accumulator_LIST.append(char)
                    JNTSYMP = ''.join(JNTSYMP_accumulator_LIST)
                elif 258 < cdx < 260:
                    JMTHP1_accumulator_LIST.append(char)
                    JMTHP1 = ''.join(JMTHP1_accumulator_LIST)
                elif 259 < cdx < 261:
                    JMTHP2_accumulator_LIST.append(char)
                    JMTHP2 = ''.join(JMTHP2_accumulator_LIST)
                elif 260 < cdx < 262:
                    JMTHP3_accumulator_LIST.append(char)
                    JMTHP3 = ''.join(JMTHP3_accumulator_LIST)
                elif 261 < cdx < 263:
                    JMTHP4_accumulator_LIST.append(char)
                    JMTHP4 = ''.join(JMTHP4_accumulator_LIST)
                elif 262 < cdx < 264:
                    JMTHP5_accumulator_LIST.append(char)
                    JMTHP5 = ''.join(JMTHP5_accumulator_LIST)
                elif 263 < cdx < 265:
                    JMTHP6_accumulator_LIST.append(char)
                    JMTHP6 = ''.join(JMTHP6_accumulator_LIST)
                elif 264 < cdx < 266:
                    JMTHP7_accumulator_LIST.append(char)
                    JMTHP7 = ''.join(JMTHP7_accumulator_LIST)
                elif 265 < cdx < 267:
                    JMTHP8_accumulator_LIST.append(char)
                    JMTHP8 = ''.join(JMTHP8_accumulator_LIST)
                elif 266 < cdx < 268:
                    JMTHP9_accumulator_LIST.append(char)
                    JMTHP9 = ''.join(JMTHP9_accumulator_LIST)
                elif 267 < cdx < 269:
                    JMTHP10_accumulator_LIST.append(char)
                    JMTHP10 = ''.join(JMTHP10_accumulator_LIST)
                elif 268 < cdx < 270:
                    JMTHP11_accumulator_LIST.append(char)
                    JMTHP11 = ''.join(JMTHP11_accumulator_LIST)
                elif 269 < cdx < 271:
                    JMTHP12_accumulator_LIST.append(char)
                    JMTHP12 = ''.join(JMTHP12_accumulator_LIST)
                elif 270 < cdx < 272:
                    JMTHP13_accumulator_LIST.append(char)
                    JMTHP13 = ''.join(JMTHP13_accumulator_LIST)
                elif 271 < cdx < 273:
                    JMTHP14_accumulator_LIST.append(char)
                    JMTHP14 = ''.join(JMTHP14_accumulator_LIST)
                elif 272 < cdx < 274:
                    JMTHP15_accumulator_LIST.append(char)
                    JMTHP15 = ''.join(JMTHP15_accumulator_LIST)
                elif 273 < cdx < 275:
                    JMTHP16_accumulator_LIST.append(char)
                    JMTHP16 = ''.join(JMTHP16_accumulator_LIST)
                elif 274 < cdx < 276:
                    JMTHP17_accumulator_LIST.append(char)
                    JMTHP17 = ''.join(JMTHP17_accumulator_LIST)
                elif 275 < cdx < 278:
                    JNTPN_accumulator_LIST.append(char)
                    JNTPN = ''.join(JNTPN_accumulator_LIST)
                elif 277 < cdx < 279:
                    JNTCHR_accumulator_LIST.append(char)
                    JNTCHR = ''.join(JNTCHR_accumulator_LIST)
                elif 278 < cdx < 280:
                    JNTHP_accumulator_LIST.append(char)
                    JNTHP = ''.join(JNTHP_accumulator_LIST)
                elif 279 < cdx < 281:
                    ARTH1_accumulator_LIST.append(char)
                    ARTH1 = ''.join(ARTH1_accumulator_LIST)
                elif 280 < cdx < 282:
                    ARTHWT_accumulator_LIST.append(char)
                    ARTHWT = ''.join(ARTHWT_accumulator_LIST)
                elif 281 < cdx < 283:
                    ARTHPH_accumulator_LIST.append(char)
                    ARTHPH = ''.join(ARTHPH_accumulator_LIST)
                elif 282 < cdx < 284:
                    ARTHCLS_accumulator_LIST.append(char)
                    ARTHCLS = ''.join(ARTHCLS_accumulator_LIST)
                elif 283 < cdx < 285:
                    ARTHLMT_accumulator_LIST.append(char)
                    ARTHLMT = ''.join(ARTHLMT_accumulator_LIST)
                elif 284 < cdx < 286:
                    ARTHWRK_accumulator_LIST.append(char)
                    ARTHWRK = ''.join(ARTHWRK_accumulator_LIST)
                elif 285 < cdx < 287:
                    PAINECK_accumulator_LIST.append(char)
                    PAINECK = ''.join(PAINECK_accumulator_LIST)
                elif 286 < cdx < 288:
                    PAINLB_accumulator_LIST.append(char)
                    PAINLB = ''.join(PAINLB_accumulator_LIST)
                elif 287 < cdx < 289:
                    PAINLEG_accumulator_LIST.append(char)
                    PAINLEG = ''.join(PAINLEG_accumulator_LIST)
                elif 288 < cdx < 290:
                    PAINFACE_accumulator_LIST.append(char)
                    PAINFACE = ''.join(PAINFACE_accumulator_LIST)
                elif 289 < cdx < 291:
                    AMIGR_accumulator_LIST.append(char)
                    AMIGR = ''.join(AMIGR_accumulator_LIST)
                elif 290 < cdx < 292:
                    ACOLD2W_accumulator_LIST.append(char)
                    ACOLD2W = ''.join(ACOLD2W_accumulator_LIST)
                elif 291 < cdx < 293:
                    AINTIL2W_accumulator_LIST.append(char)
                    AINTIL2W = ''.join(AINTIL2W_accumulator_LIST)
                elif 292 < cdx < 294:
                    PREGNOW_accumulator_LIST.append(char)
                    PREGNOW = ''.join(PREGNOW_accumulator_LIST)
                elif 293 < cdx < 295:
                    PREGFLYR_accumulator_LIST.append(char)
                    PREGFLYR = ''.join(PREGFLYR_accumulator_LIST)
                elif 294 < cdx < 296:
                    AHEARST2_accumulator_LIST.append(char)
                    AHEARST2 = ''.join(AHEARST2_accumulator_LIST)
                elif 295 < cdx < 297:
                    HRWORS_accumulator_LIST.append(char)
                    HRWORS = ''.join(HRWORS_accumulator_LIST)
                elif 296 < cdx < 298:
                    HRWHICH_accumulator_LIST.append(char)
                    HRWHICH = ''.join(HRWHICH_accumulator_LIST)
                elif 297 < cdx < 299:
                    HRRIGHT_accumulator_LIST.append(char)
                    HRRIGHT = ''.join(HRRIGHT_accumulator_LIST)
                elif 298 < cdx < 300:
                    HRLEFT_accumulator_LIST.append(char)
                    HRLEFT = ''.join(HRLEFT_accumulator_LIST)
                elif 299 < cdx < 301:
                    HRWHISP1_accumulator_LIST.append(char)
                    HRWHISP1 = ''.join(HRWHISP1_accumulator_LIST)
                elif 300 < cdx < 302:
                    HRTALK1_accumulator_LIST.append(char)
                    HRTALK1 = ''.join(HRTALK1_accumulator_LIST)
                elif 301 < cdx < 303:
                    HRSHOUT1_accumulator_LIST.append(char)
                    HRSHOUT1 = ''.join(HRSHOUT1_accumulator_LIST)
                elif 302 < cdx < 304:
                    HRSPEAK1_accumulator_LIST.append(char)
                    HRSPEAK1 = ''.join(HRSPEAK1_accumulator_LIST)
                elif 303 < cdx < 305:
                    HRCOCRE1_accumulator_LIST.append(char)
                    HRCOCRE1 = ''.join(HRCOCRE1_accumulator_LIST)
                elif 304 < cdx < 306:
                    HRCOCIM1_accumulator_LIST.append(char)
                    HRCOCIM1 = ''.join(HRCOCIM1_accumulator_LIST)
                elif 305 < cdx < 307:
                    HRFAM_accumulator_LIST.append(char)
                    HRFAM = ''.join(HRFAM_accumulator_LIST)
                elif 306 < cdx < 308:
                    HRBACK_accumulator_LIST.append(char)
                    HRBACK = ''.join(HRBACK_accumulator_LIST)
                elif 307 < cdx < 309:
                    HRFRUST_accumulator_LIST.append(char)
                    HRFRUST = ''.join(HRFRUST_accumulator_LIST)
                elif 308 < cdx < 310:
                    HRSAFETY_accumulator_LIST.append(char)
                    HRSAFETY = ''.join(HRSAFETY_accumulator_LIST)
                elif 309 < cdx < 312:
                    HEARAGE1_accumulator_LIST.append(char)
                    HEARAGE1 = ''.join(HEARAGE1_accumulator_LIST)
                elif 311 < cdx < 314:
                    HRCAUS1_accumulator_LIST.append(char)
                    HRCAUS1 = ''.join(HRCAUS1_accumulator_LIST)
                elif 313 < cdx < 315:
                    HRPROBHP_accumulator_LIST.append(char)
                    HRPROBHP = ''.join(HRPROBHP_accumulator_LIST)
                elif 314 < cdx < 316:
                    HRENT_accumulator_LIST.append(char)
                    HRENT = ''.join(HRENT_accumulator_LIST)
                elif 315 < cdx < 317:
                    HRAUD_accumulator_LIST.append(char)
                    HRAUD = ''.join(HRAUD_accumulator_LIST)
                elif 316 < cdx < 318:
                    HRTEST_accumulator_LIST.append(char)
                    HRTEST = ''.join(HRTEST_accumulator_LIST)
                elif 317 < cdx < 319:
                    HRAIDNOW_accumulator_LIST.append(char)
                    HRAIDNOW = ''.join(HRAIDNOW_accumulator_LIST)
                elif 318 < cdx < 321:
                    HRAIDLNG_accumulator_LIST.append(char)
                    HRAIDLNG = ''.join(HRAIDLNG_accumulator_LIST)
                elif 320 < cdx < 322:
                    HRAID2WK_accumulator_LIST.append(char)
                    HRAID2WK = ''.join(HRAID2WK_accumulator_LIST)
                elif 321 < cdx < 323:
                    HRAIDHLP_accumulator_LIST.append(char)
                    HRAIDHLP = ''.join(HRAIDHLP_accumulator_LIST)
                elif 322 < cdx < 324:
                    HRAIDEV_accumulator_LIST.append(char)
                    HRAIDEV = ''.join(HRAIDEV_accumulator_LIST)
                elif 323 < cdx < 325:
                    HRAIDREC_accumulator_LIST.append(char)
                    HRAIDREC = ''.join(HRAIDREC_accumulator_LIST)
                elif 324 < cdx < 327:
                    HRAIDLGP_accumulator_LIST.append(char)
                    HRAIDLGP = ''.join(HRAIDLGP_accumulator_LIST)
                elif 326 < cdx < 328:
                    HRAIDOF2_accumulator_LIST.append(char)
                    HRAIDOF2 = ''.join(HRAIDOF2_accumulator_LIST)
                elif 327 < cdx < 329:
                    HRAIDN01_accumulator_LIST.append(char)
                    HRAIDN01 = ''.join(HRAIDN01_accumulator_LIST)
                elif 328 < cdx < 330:
                    HRAIDN02_accumulator_LIST.append(char)
                    HRAIDN02 = ''.join(HRAIDN02_accumulator_LIST)
                elif 329 < cdx < 331:
                    HRAIDN03_accumulator_LIST.append(char)
                    HRAIDN03 = ''.join(HRAIDN03_accumulator_LIST)
                elif 330 < cdx < 332:
                    HRAIDN04_accumulator_LIST.append(char)
                    HRAIDN04 = ''.join(HRAIDN04_accumulator_LIST)
                elif 331 < cdx < 333:
                    HRAIDN05_accumulator_LIST.append(char)
                    HRAIDN05 = ''.join(HRAIDN05_accumulator_LIST)
                elif 332 < cdx < 334:
                    HRAIDN06_accumulator_LIST.append(char)
                    HRAIDN06 = ''.join(HRAIDN06_accumulator_LIST)
                elif 333 < cdx < 335:
                    HRAIDN07_accumulator_LIST.append(char)
                    HRAIDN07 = ''.join(HRAIDN07_accumulator_LIST)
                elif 334 < cdx < 336:
                    HRAIDN08_accumulator_LIST.append(char)
                    HRAIDN08 = ''.join(HRAIDN08_accumulator_LIST)
                elif 335 < cdx < 337:
                    HRAIDN09_accumulator_LIST.append(char)
                    HRAIDN09 = ''.join(HRAIDN09_accumulator_LIST)
                elif 336 < cdx < 338:
                    HRAIDN10_accumulator_LIST.append(char)
                    HRAIDN10 = ''.join(HRAIDN10_accumulator_LIST)
                elif 337 < cdx < 339:
                    HRAIDN11_accumulator_LIST.append(char)
                    HRAIDN11 = ''.join(HRAIDN11_accumulator_LIST)
                elif 338 < cdx < 340:
                    HRAUDTRN_accumulator_LIST.append(char)
                    HRAUDTRN = ''.join(HRAUDTRN_accumulator_LIST)
                elif 339 < cdx < 341:
                    HRALDS_accumulator_LIST.append(char)
                    HRALDS = ''.join(HRALDS_accumulator_LIST)
                elif 340 < cdx < 342:
                    HRALDT01_accumulator_LIST.append(char)
                    HRALDT01 = ''.join(HRALDT01_accumulator_LIST)
                elif 341 < cdx < 343:
                    HRALDT02_accumulator_LIST.append(char)
                    HRALDT02 = ''.join(HRALDT02_accumulator_LIST)
                elif 342 < cdx < 344:
                    HRALDT03_accumulator_LIST.append(char)
                    HRALDT03 = ''.join(HRALDT03_accumulator_LIST)
                elif 343 < cdx < 345:
                    HRALDT04_accumulator_LIST.append(char)
                    HRALDT04 = ''.join(HRALDT04_accumulator_LIST)
                elif 344 < cdx < 346:
                    HRALDT05_accumulator_LIST.append(char)
                    HRALDT05 = ''.join(HRALDT05_accumulator_LIST)
                elif 345 < cdx < 347:
                    HRALDT06_accumulator_LIST.append(char)
                    HRALDT06 = ''.join(HRALDT06_accumulator_LIST)
                elif 346 < cdx < 348:
                    HRALDT07_accumulator_LIST.append(char)
                    HRALDT07 = ''.join(HRALDT07_accumulator_LIST)
                elif 347 < cdx < 349:
                    HRALDT08_accumulator_LIST.append(char)
                    HRALDT08 = ''.join(HRALDT08_accumulator_LIST)
                elif 348 < cdx < 350:
                    HRALDT09_accumulator_LIST.append(char)
                    HRALDT09 = ''.join(HRALDT09_accumulator_LIST)
                elif 349 < cdx < 351:
                    HRALDT10_accumulator_LIST.append(char)
                    HRALDT10 = ''.join(HRALDT10_accumulator_LIST)
                elif 350 < cdx < 352:
                    HRALDT11_accumulator_LIST.append(char)
                    HRALDT11 = ''.join(HRALDT11_accumulator_LIST)
                elif 351 < cdx < 353:
                    HRBDIZZ_accumulator_LIST.append(char)
                    HRBDIZZ = ''.join(HRBDIZZ_accumulator_LIST)
                elif 352 < cdx < 354:
                    HRTIN_accumulator_LIST.append(char)
                    HRTIN = ''.join(HRTIN_accumulator_LIST)
                elif 353 < cdx < 355:
                    HRTINOFT_accumulator_LIST.append(char)
                    HRTINOFT = ''.join(HRTINOFT_accumulator_LIST)
                elif 354 < cdx < 357:
                    HRTINLNG_accumulator_LIST.append(char)
                    HRTINLNG = ''.join(HRTINLNG_accumulator_LIST)
                elif 356 < cdx < 358:
                    HRTINMUS_accumulator_LIST.append(char)
                    HRTINMUS = ''.join(HRTINMUS_accumulator_LIST)
                elif 357 < cdx < 359:
                    HRTINSLP_accumulator_LIST.append(char)
                    HRTINSLP = ''.join(HRTINSLP_accumulator_LIST)
                elif 358 < cdx < 360:
                    HRTINPRO_accumulator_LIST.append(char)
                    HRTINPRO = ''.join(HRTINPRO_accumulator_LIST)
                elif 359 < cdx < 361:
                    HRTINDIS_accumulator_LIST.append(char)
                    HRTINDIS = ''.join(HRTINDIS_accumulator_LIST)
                elif 360 < cdx < 362:
                    HRTINDOC_accumulator_LIST.append(char)
                    HRTINDOC = ''.join(HRTINDOC_accumulator_LIST)
                elif 361 < cdx < 363:
                    HRTINRM_accumulator_LIST.append(char)
                    HRTINRM = ''.join(HRTINRM_accumulator_LIST)
                elif 362 < cdx < 364:
                    HREMTY01_accumulator_LIST.append(char)
                    HREMTY01 = ''.join(HREMTY01_accumulator_LIST)
                elif 363 < cdx < 365:
                    HREMTY02_accumulator_LIST.append(char)
                    HREMTY02 = ''.join(HREMTY02_accumulator_LIST)
                elif 364 < cdx < 366:
                    HREMTY03_accumulator_LIST.append(char)
                    HREMTY03 = ''.join(HREMTY03_accumulator_LIST)
                elif 365 < cdx < 367:
                    HREMTY04_accumulator_LIST.append(char)
                    HREMTY04 = ''.join(HREMTY04_accumulator_LIST)
                elif 366 < cdx < 368:
                    HREMTY05_accumulator_LIST.append(char)
                    HREMTY05 = ''.join(HREMTY05_accumulator_LIST)
                elif 367 < cdx < 369:
                    HREMTY06_accumulator_LIST.append(char)
                    HREMTY06 = ''.join(HREMTY06_accumulator_LIST)
                elif 368 < cdx < 370:
                    HREMTY07_accumulator_LIST.append(char)
                    HREMTY07 = ''.join(HREMTY07_accumulator_LIST)
                elif 369 < cdx < 371:
                    HREMTY08_accumulator_LIST.append(char)
                    HREMTY08 = ''.join(HREMTY08_accumulator_LIST)
                elif 370 < cdx < 372:
                    HREMTY09_accumulator_LIST.append(char)
                    HREMTY09 = ''.join(HREMTY09_accumulator_LIST)
                elif 371 < cdx < 373:
                    HREMTY10_accumulator_LIST.append(char)
                    HREMTY10 = ''.join(HREMTY10_accumulator_LIST)
                elif 372 < cdx < 374:
                    HREMTY11_accumulator_LIST.append(char)
                    HREMTY11 = ''.join(HREMTY11_accumulator_LIST)
                elif 373 < cdx < 375:
                    HREMTY12_accumulator_LIST.append(char)
                    HREMTY12 = ''.join(HREMTY12_accumulator_LIST)
                elif 374 < cdx < 376:
                    HRTNRMHP_accumulator_LIST.append(char)
                    HRTNRMHP = ''.join(HRTNRMHP_accumulator_LIST)
                elif 375 < cdx < 377:
                    HRHCUSIS_accumulator_LIST.append(char)
                    HRHCUSIS = ''.join(HRHCUSIS_accumulator_LIST)
                elif 376 < cdx < 378:
                    HRHCPROB_accumulator_LIST.append(char)
                    HRHCPROB = ''.join(HRHCPROB_accumulator_LIST)
                elif 377 < cdx < 379:
                    HRFIRE_accumulator_LIST.append(char)
                    HRFIRE = ''.join(HRFIRE_accumulator_LIST)
                elif 378 < cdx < 380:
                    HRFIRTYP_accumulator_LIST.append(char)
                    HRFIRTYP = ''.join(HRFIRTYP_accumulator_LIST)
                elif 379 < cdx < 381:
                    HRFRTIM_accumulator_LIST.append(char)
                    HRFRTIM = ''.join(HRFRTIM_accumulator_LIST)
                elif 380 < cdx < 382:
                    HR12MR_accumulator_LIST.append(char)
                    HR12MR = ''.join(HR12MR_accumulator_LIST)
                elif 381 < cdx < 383:
                    HRFRPROT_accumulator_LIST.append(char)
                    HRFRPROT = ''.join(HRFRPROT_accumulator_LIST)
                elif 382 < cdx < 384:
                    HRTOTR_accumulator_LIST.append(char)
                    HRTOTR = ''.join(HRTOTR_accumulator_LIST)
                elif 383 < cdx < 385:
                    HRFRPRT2_accumulator_LIST.append(char)
                    HRFRPRT2 = ''.join(HRFRPRT2_accumulator_LIST)
                elif 384 < cdx < 386:
                    HRWKVLNS_accumulator_LIST.append(char)
                    HRWKVLNS = ''.join(HRWKVLNS_accumulator_LIST)
                elif 385 < cdx < 387:
                    HRWKLNS_accumulator_LIST.append(char)
                    HRWKLNS = ''.join(HRWKLNS_accumulator_LIST)
                elif 386 < cdx < 389:
                    HRWKVLNT_accumulator_LIST.append(char)
                    HRWKVLNT = ''.join(HRWKVLNT_accumulator_LIST)
                elif 388 < cdx < 390:
                    HRWKVLEX_accumulator_LIST.append(char)
                    HRWKVLEX = ''.join(HRWKVLEX_accumulator_LIST)
                elif 389 < cdx < 391:
                    HRWKVLP1_accumulator_LIST.append(char)
                    HRWKVLP1 = ''.join(HRWKVLP1_accumulator_LIST)
                elif 390 < cdx < 392:
                    HRWKVLP2_accumulator_LIST.append(char)
                    HRWKVLP2 = ''.join(HRWKVLP2_accumulator_LIST)
                elif 391 < cdx < 394:
                    HRWRLNS_accumulator_LIST.append(char)
                    HRWRLNS = ''.join(HRWRLNS_accumulator_LIST)
                elif 393 < cdx < 395:
                    HRWKLEX_accumulator_LIST.append(char)
                    HRWKLEX = ''.join(HRWKLEX_accumulator_LIST)
                elif 394 < cdx < 396:
                    HRWKLP1_accumulator_LIST.append(char)
                    HRWKLP1 = ''.join(HRWKLP1_accumulator_LIST)
                elif 395 < cdx < 397:
                    HRWKLP2_accumulator_LIST.append(char)
                    HRWKLP2 = ''.join(HRWKLP2_accumulator_LIST)
                elif 396 < cdx < 398:
                    HRLSVLNS_accumulator_LIST.append(char)
                    HRLSVLNS = ''.join(HRLSVLNS_accumulator_LIST)
                elif 397 < cdx < 399:
                    HRVLTP01_accumulator_LIST.append(char)
                    HRVLTP01 = ''.join(HRVLTP01_accumulator_LIST)
                elif 398 < cdx < 400:
                    HRVLTP02_accumulator_LIST.append(char)
                    HRVLTP02 = ''.join(HRVLTP02_accumulator_LIST)
                elif 399 < cdx < 401:
                    HRVLTP03_accumulator_LIST.append(char)
                    HRVLTP03 = ''.join(HRVLTP03_accumulator_LIST)
                elif 400 < cdx < 402:
                    HRVLTP04_accumulator_LIST.append(char)
                    HRVLTP04 = ''.join(HRVLTP04_accumulator_LIST)
                elif 401 < cdx < 403:
                    HRVLTP05_accumulator_LIST.append(char)
                    HRVLTP05 = ''.join(HRVLTP05_accumulator_LIST)
                elif 402 < cdx < 404:
                    HRVLTP06_accumulator_LIST.append(char)
                    HRVLTP06 = ''.join(HRVLTP06_accumulator_LIST)
                elif 403 < cdx < 405:
                    HRVLTP07_accumulator_LIST.append(char)
                    HRVLTP07 = ''.join(HRVLTP07_accumulator_LIST)
                elif 404 < cdx < 406:
                    HRVLTP08_accumulator_LIST.append(char)
                    HRVLTP08 = ''.join(HRVLTP08_accumulator_LIST)
                elif 405 < cdx < 407:
                    HRVLTP09_accumulator_LIST.append(char)
                    HRVLTP09 = ''.join(HRVLTP09_accumulator_LIST)
                elif 406 < cdx < 408:
                    HRVLTP10_accumulator_LIST.append(char)
                    HRVLTP10 = ''.join(HRVLTP10_accumulator_LIST)
                elif 407 < cdx < 409:
                    HRLNOS_accumulator_LIST.append(char)
                    HRLNOS = ''.join(HRLNOS_accumulator_LIST)
                elif 408 < cdx < 410:
                    HRLTP01_accumulator_LIST.append(char)
                    HRLTP01 = ''.join(HRLTP01_accumulator_LIST)
                elif 409 < cdx < 411:
                    HRLTP02_accumulator_LIST.append(char)
                    HRLTP02 = ''.join(HRLTP02_accumulator_LIST)
                elif 410 < cdx < 412:
                    HRLTP03_accumulator_LIST.append(char)
                    HRLTP03 = ''.join(HRLTP03_accumulator_LIST)
                elif 411 < cdx < 413:
                    HRLTP04_accumulator_LIST.append(char)
                    HRLTP04 = ''.join(HRLTP04_accumulator_LIST)
                elif 412 < cdx < 414:
                    HRLTP05_accumulator_LIST.append(char)
                    HRLTP05 = ''.join(HRLTP05_accumulator_LIST)
                elif 413 < cdx < 415:
                    HRLTP06_accumulator_LIST.append(char)
                    HRLTP06 = ''.join(HRLTP06_accumulator_LIST)
                elif 414 < cdx < 416:
                    HRLTP07_accumulator_LIST.append(char)
                    HRLTP07 = ''.join(HRLTP07_accumulator_LIST)
                elif 415 < cdx < 417:
                    HRLTP08_accumulator_LIST.append(char)
                    HRLTP08 = ''.join(HRLTP08_accumulator_LIST)
                elif 416 < cdx < 418:
                    HRLTP09_accumulator_LIST.append(char)
                    HRLTP09 = ''.join(HRLTP09_accumulator_LIST)
                elif 417 < cdx < 419:
                    HRLTP10_accumulator_LIST.append(char)
                    HRLTP10 = ''.join(HRLTP10_accumulator_LIST)
                elif 418 < cdx < 420:
                    HRNOSEXP_accumulator_LIST.append(char)
                    HRNOSEXP = ''.join(HRNOSEXP_accumulator_LIST)
                elif 419 < cdx < 421:
                    HRLSP1_accumulator_LIST.append(char)
                    HRLSP1 = ''.join(HRLSP1_accumulator_LIST)
                elif 420 < cdx < 422:
                    HRLSP2_accumulator_LIST.append(char)
                    HRLSP2 = ''.join(HRLSP2_accumulator_LIST)
                elif 421 < cdx < 423:
                    HRINTNET_accumulator_LIST.append(char)
                    HRINTNET = ''.join(HRINTNET_accumulator_LIST)
                elif 422 < cdx < 424:
                    HRINTHL_accumulator_LIST.append(char)
                    HRINTHL = ''.join(HRINTHL_accumulator_LIST)
                elif 423 < cdx < 425:
                    HRINTHA_accumulator_LIST.append(char)
                    HRINTHA = ''.join(HRINTHA_accumulator_LIST)
                elif 424 < cdx < 426:
                    HRINTTN_accumulator_LIST.append(char)
                    HRINTTN = ''.join(HRINTTN_accumulator_LIST)
                elif 425 < cdx < 427:
                    HRINTDZ_accumulator_LIST.append(char)
                    HRINTDZ = ''.join(HRINTDZ_accumulator_LIST)
                elif 426 < cdx < 428:
                    HRINTHP_accumulator_LIST.append(char)
                    HRINTHP = ''.join(HRINTHP_accumulator_LIST)
                elif 427 < cdx < 429:
                    HRINTHPR_accumulator_LIST.append(char)
                    HRINTHPR = ''.join(HRINTHPR_accumulator_LIST)
                elif 428 < cdx < 430:
                    AVISION_accumulator_LIST.append(char)
                    AVISION = ''.join(AVISION_accumulator_LIST)
                elif 429 < cdx < 431:
                    ABLIND_accumulator_LIST.append(char)
                    ABLIND = ''.join(ABLIND_accumulator_LIST)
                elif 430 < cdx < 432:
                    LUPPRT_accumulator_LIST.append(char)
                    LUPPRT = ''.join(LUPPRT_accumulator_LIST)
                elif 431 < cdx < 435:
                    WKDAYR_accumulator_LIST.append(char)
                    WKDAYR = ''.join(WKDAYR_accumulator_LIST)
                elif 434 < cdx < 438:
                    BEDDAYR_accumulator_LIST.append(char)
                    BEDDAYR = ''.join(BEDDAYR_accumulator_LIST)
                elif 437 < cdx < 439:
                    AHSTATYR_accumulator_LIST.append(char)
                    AHSTATYR = ''.join(AHSTATYR_accumulator_LIST)
                elif 438 < cdx < 440:
                    SPECEQ_accumulator_LIST.append(char)
                    SPECEQ = ''.join(SPECEQ_accumulator_LIST)
                elif 439 < cdx < 441:
                    FLWALK_accumulator_LIST.append(char)
                    FLWALK = ''.join(FLWALK_accumulator_LIST)
                elif 440 < cdx < 442:
                    FLCLIMB_accumulator_LIST.append(char)
                    FLCLIMB = ''.join(FLCLIMB_accumulator_LIST)
                elif 441 < cdx < 443:
                    FLSTAND_accumulator_LIST.append(char)
                    FLSTAND = ''.join(FLSTAND_accumulator_LIST)
                elif 442 < cdx < 444:
                    FLSIT_accumulator_LIST.append(char)
                    FLSIT = ''.join(FLSIT_accumulator_LIST)
                elif 443 < cdx < 445:
                    FLSTOOP_accumulator_LIST.append(char)
                    FLSTOOP = ''.join(FLSTOOP_accumulator_LIST)
                elif 444 < cdx < 446:
                    FLREACH_accumulator_LIST.append(char)
                    FLREACH = ''.join(FLREACH_accumulator_LIST)
                elif 445 < cdx < 447:
                    FLGRASP_accumulator_LIST.append(char)
                    FLGRASP = ''.join(FLGRASP_accumulator_LIST)
                elif 446 < cdx < 448:
                    FLCARRY_accumulator_LIST.append(char)
                    FLCARRY = ''.join(FLCARRY_accumulator_LIST)
                elif 447 < cdx < 449:
                    FLPUSH_accumulator_LIST.append(char)
                    FLPUSH = ''.join(FLPUSH_accumulator_LIST)
                elif 448 < cdx < 450:
                    FLSHOP_accumulator_LIST.append(char)
                    FLSHOP = ''.join(FLSHOP_accumulator_LIST)
                elif 449 < cdx < 451:
                    FLSOCL_accumulator_LIST.append(char)
                    FLSOCL = ''.join(FLSOCL_accumulator_LIST)
                elif 450 < cdx < 452:
                    FLRELAX_accumulator_LIST.append(char)
                    FLRELAX = ''.join(FLRELAX_accumulator_LIST)
                elif 451 < cdx < 453:
                    FLA1AR_accumulator_LIST.append(char)
                    FLA1AR = ''.join(FLA1AR_accumulator_LIST)
                elif 452 < cdx < 454:
                    AFLHCA1_accumulator_LIST.append(char)
                    AFLHCA1 = ''.join(AFLHCA1_accumulator_LIST)
                elif 453 < cdx < 455:
                    AFLHCA2_accumulator_LIST.append(char)
                    AFLHCA2 = ''.join(AFLHCA2_accumulator_LIST)
                elif 454 < cdx < 456:
                    AFLHCA3_accumulator_LIST.append(char)
                    AFLHCA3 = ''.join(AFLHCA3_accumulator_LIST)
                elif 455 < cdx < 457:
                    AFLHCA4_accumulator_LIST.append(char)
                    AFLHCA4 = ''.join(AFLHCA4_accumulator_LIST)
                elif 456 < cdx < 458:
                    AFLHCA5_accumulator_LIST.append(char)
                    AFLHCA5 = ''.join(AFLHCA5_accumulator_LIST)
                elif 457 < cdx < 459:
                    AFLHCA6_accumulator_LIST.append(char)
                    AFLHCA6 = ''.join(AFLHCA6_accumulator_LIST)
                elif 458 < cdx < 460:
                    AFLHCA7_accumulator_LIST.append(char)
                    AFLHCA7 = ''.join(AFLHCA7_accumulator_LIST)
                elif 459 < cdx < 461:
                    AFLHCA8_accumulator_LIST.append(char)
                    AFLHCA8 = ''.join(AFLHCA8_accumulator_LIST)
                elif 460 < cdx < 462:
                    AFLHCA9_accumulator_LIST.append(char)
                    AFLHCA9 = ''.join(AFLHCA9_accumulator_LIST)
                elif 461 < cdx < 463:
                    AFLHCA10_accumulator_LIST.append(char)
                    AFLHCA10 = ''.join(AFLHCA10_accumulator_LIST)
                elif 462 < cdx < 464:
                    AFLHCA11_accumulator_LIST.append(char)
                    AFLHCA11 = ''.join(AFLHCA11_accumulator_LIST)
                elif 463 < cdx < 465:
                    AFLHCA12_accumulator_LIST.append(char)
                    AFLHCA12 = ''.join(AFLHCA12_accumulator_LIST)
                elif 464 < cdx < 466:
                    AFLHCA13_accumulator_LIST.append(char)
                    AFLHCA13 = ''.join(AFLHCA13_accumulator_LIST)
                elif 465 < cdx < 467:
                    ALHCA14A_accumulator_LIST.append(char)
                    ALHCA14A = ''.join(ALHCA14A_accumulator_LIST)
                elif 466 < cdx < 468:
                    AFLHCA15_accumulator_LIST.append(char)
                    AFLHCA15 = ''.join(AFLHCA15_accumulator_LIST)
                elif 467 < cdx < 469:
                    AFLHCA16_accumulator_LIST.append(char)
                    AFLHCA16 = ''.join(AFLHCA16_accumulator_LIST)
                elif 468 < cdx < 470:
                    AFLHCA17_accumulator_LIST.append(char)
                    AFLHCA17 = ''.join(AFLHCA17_accumulator_LIST)
                elif 469 < cdx < 471:
                    AFLHCA18_accumulator_LIST.append(char)
                    AFLHCA18 = ''.join(AFLHCA18_accumulator_LIST)
                elif 470 < cdx < 472:
                    AFLHC19__accumulator_LIST.append(char)
                    AFLHC19_ = ''.join(AFLHC19__accumulator_LIST)
                elif 471 < cdx < 473:
                    AFLHC20__accumulator_LIST.append(char)
                    AFLHC20_ = ''.join(AFLHC20__accumulator_LIST)
                elif 472 < cdx < 474:
                    AFLHC21__accumulator_LIST.append(char)
                    AFLHC21_ = ''.join(AFLHC21__accumulator_LIST)
                elif 473 < cdx < 475:
                    AFLHC22__accumulator_LIST.append(char)
                    AFLHC22_ = ''.join(AFLHC22__accumulator_LIST)
                elif 474 < cdx < 476:
                    AFLHC23__accumulator_LIST.append(char)
                    AFLHC23_ = ''.join(AFLHC23__accumulator_LIST)
                elif 475 < cdx < 477:
                    AFLHC24__accumulator_LIST.append(char)
                    AFLHC24_ = ''.join(AFLHC24__accumulator_LIST)
                elif 476 < cdx < 478:
                    AFLHC25__accumulator_LIST.append(char)
                    AFLHC25_ = ''.join(AFLHC25__accumulator_LIST)
                elif 477 < cdx < 479:
                    AFLHC26__accumulator_LIST.append(char)
                    AFLHC26_ = ''.join(AFLHC26__accumulator_LIST)
                elif 478 < cdx < 480:
                    AFLHC27__accumulator_LIST.append(char)
                    AFLHC27_ = ''.join(AFLHC27__accumulator_LIST)
                elif 479 < cdx < 481:
                    AFLHC28__accumulator_LIST.append(char)
                    AFLHC28_ = ''.join(AFLHC28__accumulator_LIST)
                elif 480 < cdx < 482:
                    AFLHC29__accumulator_LIST.append(char)
                    AFLHC29_ = ''.join(AFLHC29__accumulator_LIST)
                elif 481 < cdx < 483:
                    AFLHC30__accumulator_LIST.append(char)
                    AFLHC30_ = ''.join(AFLHC30__accumulator_LIST)
                elif 482 < cdx < 484:
                    AFLHC31__accumulator_LIST.append(char)
                    AFLHC31_ = ''.join(AFLHC31__accumulator_LIST)
                elif 483 < cdx < 485:
                    AFLHC32__accumulator_LIST.append(char)
                    AFLHC32_ = ''.join(AFLHC32__accumulator_LIST)
                elif 484 < cdx < 486:
                    AFLHC33__accumulator_LIST.append(char)
                    AFLHC33_ = ''.join(AFLHC33__accumulator_LIST)
                elif 485 < cdx < 487:
                    AFLHC34__accumulator_LIST.append(char)
                    AFLHC34_ = ''.join(AFLHC34__accumulator_LIST)
                elif 486 < cdx < 488:
                    AFLHCA90_accumulator_LIST.append(char)
                    AFLHCA90 = ''.join(AFLHCA90_accumulator_LIST)
                elif 487 < cdx < 489:
                    AFLHCA91_accumulator_LIST.append(char)
                    AFLHCA91 = ''.join(AFLHCA91_accumulator_LIST)
                elif 488 < cdx < 491:
                    ALTIME1_accumulator_LIST.append(char)
                    ALTIME1 = ''.join(ALTIME1_accumulator_LIST)
                elif 490 < cdx < 492:
                    ALUNIT1_accumulator_LIST.append(char)
                    ALUNIT1 = ''.join(ALUNIT1_accumulator_LIST)
                elif 491 < cdx < 494:
                    ALDURA1_accumulator_LIST.append(char)
                    ALDURA1 = ''.join(ALDURA1_accumulator_LIST)
                elif 493 < cdx < 495:
                    ALDURB1_accumulator_LIST.append(char)
                    ALDURB1 = ''.join(ALDURB1_accumulator_LIST)
                elif 494 < cdx < 496:
                    ALCHRC1_accumulator_LIST.append(char)
                    ALCHRC1 = ''.join(ALCHRC1_accumulator_LIST)
                elif 495 < cdx < 498:
                    ALTIME2_accumulator_LIST.append(char)
                    ALTIME2 = ''.join(ALTIME2_accumulator_LIST)
                elif 497 < cdx < 499:
                    ALUNIT2_accumulator_LIST.append(char)
                    ALUNIT2 = ''.join(ALUNIT2_accumulator_LIST)
                elif 498 < cdx < 501:
                    ALDURA2_accumulator_LIST.append(char)
                    ALDURA2 = ''.join(ALDURA2_accumulator_LIST)
                elif 500 < cdx < 502:
                    ALDURB2_accumulator_LIST.append(char)
                    ALDURB2 = ''.join(ALDURB2_accumulator_LIST)
                elif 501 < cdx < 503:
                    ALCHRC2_accumulator_LIST.append(char)
                    ALCHRC2 = ''.join(ALCHRC2_accumulator_LIST)
                elif 502 < cdx < 505:
                    ALTIME3_accumulator_LIST.append(char)
                    ALTIME3 = ''.join(ALTIME3_accumulator_LIST)
                elif 504 < cdx < 506:
                    ALUNIT3_accumulator_LIST.append(char)
                    ALUNIT3 = ''.join(ALUNIT3_accumulator_LIST)
                elif 505 < cdx < 508:
                    ALDURA3_accumulator_LIST.append(char)
                    ALDURA3 = ''.join(ALDURA3_accumulator_LIST)
                elif 507 < cdx < 509:
                    ALDURB3_accumulator_LIST.append(char)
                    ALDURB3 = ''.join(ALDURB3_accumulator_LIST)
                elif 508 < cdx < 510:
                    ALCHRC3_accumulator_LIST.append(char)
                    ALCHRC3 = ''.join(ALCHRC3_accumulator_LIST)
                elif 509 < cdx < 512:
                    ALTIME4_accumulator_LIST.append(char)
                    ALTIME4 = ''.join(ALTIME4_accumulator_LIST)
                elif 511 < cdx < 513:
                    ALUNIT4_accumulator_LIST.append(char)
                    ALUNIT4 = ''.join(ALUNIT4_accumulator_LIST)
                elif 512 < cdx < 515:
                    ALDURA4_accumulator_LIST.append(char)
                    ALDURA4 = ''.join(ALDURA4_accumulator_LIST)
                elif 514 < cdx < 516:
                    ALDURB4_accumulator_LIST.append(char)
                    ALDURB4 = ''.join(ALDURB4_accumulator_LIST)
                elif 515 < cdx < 517:
                    ALCHRC4_accumulator_LIST.append(char)
                    ALCHRC4 = ''.join(ALCHRC4_accumulator_LIST)
                elif 516 < cdx < 519:
                    ALTIME5_accumulator_LIST.append(char)
                    ALTIME5 = ''.join(ALTIME5_accumulator_LIST)
                elif 518 < cdx < 520:
                    ALUNIT5_accumulator_LIST.append(char)
                    ALUNIT5 = ''.join(ALUNIT5_accumulator_LIST)
                elif 519 < cdx < 522:
                    ALDURA5_accumulator_LIST.append(char)
                    ALDURA5 = ''.join(ALDURA5_accumulator_LIST)
                elif 521 < cdx < 523:
                    ALDURB5_accumulator_LIST.append(char)
                    ALDURB5 = ''.join(ALDURB5_accumulator_LIST)
                elif 522 < cdx < 524:
                    ALCHRC5_accumulator_LIST.append(char)
                    ALCHRC5 = ''.join(ALCHRC5_accumulator_LIST)
                elif 523 < cdx < 526:
                    ALTIME6_accumulator_LIST.append(char)
                    ALTIME6 = ''.join(ALTIME6_accumulator_LIST)
                elif 525 < cdx < 527:
                    ALUNIT6_accumulator_LIST.append(char)
                    ALUNIT6 = ''.join(ALUNIT6_accumulator_LIST)
                elif 526 < cdx < 529:
                    ALDURA6_accumulator_LIST.append(char)
                    ALDURA6 = ''.join(ALDURA6_accumulator_LIST)
                elif 528 < cdx < 530:
                    ALDURB6_accumulator_LIST.append(char)
                    ALDURB6 = ''.join(ALDURB6_accumulator_LIST)
                elif 529 < cdx < 531:
                    ALCHRC6_accumulator_LIST.append(char)
                    ALCHRC6 = ''.join(ALCHRC6_accumulator_LIST)
                elif 530 < cdx < 533:
                    ALTIME7_accumulator_LIST.append(char)
                    ALTIME7 = ''.join(ALTIME7_accumulator_LIST)
                elif 532 < cdx < 534:
                    ALUNIT7_accumulator_LIST.append(char)
                    ALUNIT7 = ''.join(ALUNIT7_accumulator_LIST)
                elif 533 < cdx < 536:
                    ALDURA7_accumulator_LIST.append(char)
                    ALDURA7 = ''.join(ALDURA7_accumulator_LIST)
                elif 535 < cdx < 537:
                    ALDURB7_accumulator_LIST.append(char)
                    ALDURB7 = ''.join(ALDURB7_accumulator_LIST)
                elif 536 < cdx < 538:
                    ALCHRC7_accumulator_LIST.append(char)
                    ALCHRC7 = ''.join(ALCHRC7_accumulator_LIST)
                elif 537 < cdx < 540:
                    ALTIME8_accumulator_LIST.append(char)
                    ALTIME8 = ''.join(ALTIME8_accumulator_LIST)
                elif 539 < cdx < 541:
                    ALUNIT8_accumulator_LIST.append(char)
                    ALUNIT8 = ''.join(ALUNIT8_accumulator_LIST)
                elif 540 < cdx < 543:
                    ALDURA8_accumulator_LIST.append(char)
                    ALDURA8 = ''.join(ALDURA8_accumulator_LIST)
                elif 542 < cdx < 544:
                    ALDURB8_accumulator_LIST.append(char)
                    ALDURB8 = ''.join(ALDURB8_accumulator_LIST)
                elif 543 < cdx < 545:
                    ALCHRC8_accumulator_LIST.append(char)
                    ALCHRC8 = ''.join(ALCHRC8_accumulator_LIST)
                elif 544 < cdx < 547:
                    ALTIME9_accumulator_LIST.append(char)
                    ALTIME9 = ''.join(ALTIME9_accumulator_LIST)
                elif 546 < cdx < 548:
                    ALUNIT9_accumulator_LIST.append(char)
                    ALUNIT9 = ''.join(ALUNIT9_accumulator_LIST)
                elif 547 < cdx < 550:
                    ALDURA9_accumulator_LIST.append(char)
                    ALDURA9 = ''.join(ALDURA9_accumulator_LIST)
                elif 549 < cdx < 551:
                    ALDURB9_accumulator_LIST.append(char)
                    ALDURB9 = ''.join(ALDURB9_accumulator_LIST)
                elif 550 < cdx < 552:
                    ALCHRC9_accumulator_LIST.append(char)
                    ALCHRC9 = ''.join(ALCHRC9_accumulator_LIST)
                elif 551 < cdx < 554:
                    ALTIME10_accumulator_LIST.append(char)
                    ALTIME10 = ''.join(ALTIME10_accumulator_LIST)
                elif 553 < cdx < 555:
                    ALUNIT10_accumulator_LIST.append(char)
                    ALUNIT10 = ''.join(ALUNIT10_accumulator_LIST)
                elif 554 < cdx < 557:
                    ALDURA10_accumulator_LIST.append(char)
                    ALDURA10 = ''.join(ALDURA10_accumulator_LIST)
                elif 556 < cdx < 558:
                    ALDURB10_accumulator_LIST.append(char)
                    ALDURB10 = ''.join(ALDURB10_accumulator_LIST)
                elif 557 < cdx < 559:
                    ALCHRC10_accumulator_LIST.append(char)
                    ALCHRC10 = ''.join(ALCHRC10_accumulator_LIST)
                elif 558 < cdx < 561:
                    ALTIME11_accumulator_LIST.append(char)
                    ALTIME11 = ''.join(ALTIME11_accumulator_LIST)
                elif 560 < cdx < 562:
                    ALUNIT11_accumulator_LIST.append(char)
                    ALUNIT11 = ''.join(ALUNIT11_accumulator_LIST)
                elif 561 < cdx < 564:
                    ALDURA11_accumulator_LIST.append(char)
                    ALDURA11 = ''.join(ALDURA11_accumulator_LIST)
                elif 563 < cdx < 565:
                    ALDURB11_accumulator_LIST.append(char)
                    ALDURB11 = ''.join(ALDURB11_accumulator_LIST)
                elif 564 < cdx < 566:
                    ALCHRC11_accumulator_LIST.append(char)
                    ALCHRC11 = ''.join(ALCHRC11_accumulator_LIST)
                elif 565 < cdx < 568:
                    ALTIME12_accumulator_LIST.append(char)
                    ALTIME12 = ''.join(ALTIME12_accumulator_LIST)
                elif 567 < cdx < 569:
                    ALUNIT12_accumulator_LIST.append(char)
                    ALUNIT12 = ''.join(ALUNIT12_accumulator_LIST)
                elif 568 < cdx < 571:
                    ALDURA12_accumulator_LIST.append(char)
                    ALDURA12 = ''.join(ALDURA12_accumulator_LIST)
                elif 570 < cdx < 572:
                    ALDURB12_accumulator_LIST.append(char)
                    ALDURB12 = ''.join(ALDURB12_accumulator_LIST)
                elif 571 < cdx < 573:
                    ALCHRC12_accumulator_LIST.append(char)
                    ALCHRC12 = ''.join(ALCHRC12_accumulator_LIST)
                elif 572 < cdx < 575:
                    ALTIME13_accumulator_LIST.append(char)
                    ALTIME13 = ''.join(ALTIME13_accumulator_LIST)
                elif 574 < cdx < 576:
                    ALUNIT13_accumulator_LIST.append(char)
                    ALUNIT13 = ''.join(ALUNIT13_accumulator_LIST)
                elif 575 < cdx < 578:
                    ALDURA13_accumulator_LIST.append(char)
                    ALDURA13 = ''.join(ALDURA13_accumulator_LIST)
                elif 577 < cdx < 579:
                    ALDURB13_accumulator_LIST.append(char)
                    ALDURB13 = ''.join(ALDURB13_accumulator_LIST)
                elif 578 < cdx < 580:
                    ALCHRC13_accumulator_LIST.append(char)
                    ALCHRC13 = ''.join(ALCHRC13_accumulator_LIST)
                elif 579 < cdx < 582:
                    ATIME14A_accumulator_LIST.append(char)
                    ATIME14A = ''.join(ATIME14A_accumulator_LIST)
                elif 581 < cdx < 583:
                    AUNIT14A_accumulator_LIST.append(char)
                    AUNIT14A = ''.join(AUNIT14A_accumulator_LIST)
                elif 582 < cdx < 585:
                    ADURA14A_accumulator_LIST.append(char)
                    ADURA14A = ''.join(ADURA14A_accumulator_LIST)
                elif 584 < cdx < 586:
                    ADURB14A_accumulator_LIST.append(char)
                    ADURB14A = ''.join(ADURB14A_accumulator_LIST)
                elif 585 < cdx < 587:
                    ACHRC14A_accumulator_LIST.append(char)
                    ACHRC14A = ''.join(ACHRC14A_accumulator_LIST)
                elif 586 < cdx < 589:
                    ALTIME15_accumulator_LIST.append(char)
                    ALTIME15 = ''.join(ALTIME15_accumulator_LIST)
                elif 588 < cdx < 590:
                    ALUNIT15_accumulator_LIST.append(char)
                    ALUNIT15 = ''.join(ALUNIT15_accumulator_LIST)
                elif 589 < cdx < 592:
                    ALDURA15_accumulator_LIST.append(char)
                    ALDURA15 = ''.join(ALDURA15_accumulator_LIST)
                elif 591 < cdx < 593:
                    ALDURB15_accumulator_LIST.append(char)
                    ALDURB15 = ''.join(ALDURB15_accumulator_LIST)
                elif 592 < cdx < 594:
                    ALCHRC15_accumulator_LIST.append(char)
                    ALCHRC15 = ''.join(ALCHRC15_accumulator_LIST)
                elif 593 < cdx < 596:
                    ALTIME16_accumulator_LIST.append(char)
                    ALTIME16 = ''.join(ALTIME16_accumulator_LIST)
                elif 595 < cdx < 597:
                    ALUNIT16_accumulator_LIST.append(char)
                    ALUNIT16 = ''.join(ALUNIT16_accumulator_LIST)
                elif 596 < cdx < 599:
                    ALDURA16_accumulator_LIST.append(char)
                    ALDURA16 = ''.join(ALDURA16_accumulator_LIST)
                elif 598 < cdx < 600:
                    ALDURB16_accumulator_LIST.append(char)
                    ALDURB16 = ''.join(ALDURB16_accumulator_LIST)
                elif 599 < cdx < 601:
                    ALCHRC16_accumulator_LIST.append(char)
                    ALCHRC16 = ''.join(ALCHRC16_accumulator_LIST)
                elif 600 < cdx < 603:
                    ALTIME17_accumulator_LIST.append(char)
                    ALTIME17 = ''.join(ALTIME17_accumulator_LIST)
                elif 602 < cdx < 604:
                    ALUNIT17_accumulator_LIST.append(char)
                    ALUNIT17 = ''.join(ALUNIT17_accumulator_LIST)
                elif 603 < cdx < 606:
                    ALDURA17_accumulator_LIST.append(char)
                    ALDURA17 = ''.join(ALDURA17_accumulator_LIST)
                elif 605 < cdx < 607:
                    ALDURB17_accumulator_LIST.append(char)
                    ALDURB17 = ''.join(ALDURB17_accumulator_LIST)
                elif 606 < cdx < 608:
                    ALCHRC17_accumulator_LIST.append(char)
                    ALCHRC17 = ''.join(ALCHRC17_accumulator_LIST)
                elif 607 < cdx < 610:
                    ALTIME18_accumulator_LIST.append(char)
                    ALTIME18 = ''.join(ALTIME18_accumulator_LIST)
                elif 609 < cdx < 611:
                    ALUNIT18_accumulator_LIST.append(char)
                    ALUNIT18 = ''.join(ALUNIT18_accumulator_LIST)
                elif 610 < cdx < 613:
                    ALDURA18_accumulator_LIST.append(char)
                    ALDURA18 = ''.join(ALDURA18_accumulator_LIST)
                elif 612 < cdx < 614:
                    ALDURB18_accumulator_LIST.append(char)
                    ALDURB18 = ''.join(ALDURB18_accumulator_LIST)
                elif 613 < cdx < 615:
                    ALCHRC18_accumulator_LIST.append(char)
                    ALCHRC18 = ''.join(ALCHRC18_accumulator_LIST)
                elif 614 < cdx < 617:
                    ALTIME19_accumulator_LIST.append(char)
                    ALTIME19 = ''.join(ALTIME19_accumulator_LIST)
                elif 616 < cdx < 618:
                    ALUNIT19_accumulator_LIST.append(char)
                    ALUNIT19 = ''.join(ALUNIT19_accumulator_LIST)
                elif 617 < cdx < 620:
                    ALDURA19_accumulator_LIST.append(char)
                    ALDURA19 = ''.join(ALDURA19_accumulator_LIST)
                elif 619 < cdx < 621:
                    ALDURB19_accumulator_LIST.append(char)
                    ALDURB19 = ''.join(ALDURB19_accumulator_LIST)
                elif 620 < cdx < 622:
                    ALCHRC19_accumulator_LIST.append(char)
                    ALCHRC19 = ''.join(ALCHRC19_accumulator_LIST)
                elif 621 < cdx < 624:
                    ALTIME20_accumulator_LIST.append(char)
                    ALTIME20 = ''.join(ALTIME20_accumulator_LIST)
                elif 623 < cdx < 625:
                    ALUNIT20_accumulator_LIST.append(char)
                    ALUNIT20 = ''.join(ALUNIT20_accumulator_LIST)
                elif 624 < cdx < 627:
                    ALDURA20_accumulator_LIST.append(char)
                    ALDURA20 = ''.join(ALDURA20_accumulator_LIST)
                elif 626 < cdx < 628:
                    ALDURB20_accumulator_LIST.append(char)
                    ALDURB20 = ''.join(ALDURB20_accumulator_LIST)
                elif 627 < cdx < 629:
                    ALCHRC20_accumulator_LIST.append(char)
                    ALCHRC20 = ''.join(ALCHRC20_accumulator_LIST)
                elif 628 < cdx < 631:
                    ALTIME21_accumulator_LIST.append(char)
                    ALTIME21 = ''.join(ALTIME21_accumulator_LIST)
                elif 630 < cdx < 632:
                    ALUNIT21_accumulator_LIST.append(char)
                    ALUNIT21 = ''.join(ALUNIT21_accumulator_LIST)
                elif 631 < cdx < 634:
                    ALDURA21_accumulator_LIST.append(char)
                    ALDURA21 = ''.join(ALDURA21_accumulator_LIST)
                elif 633 < cdx < 635:
                    ALDURB21_accumulator_LIST.append(char)
                    ALDURB21 = ''.join(ALDURB21_accumulator_LIST)
                elif 634 < cdx < 636:
                    ALCHRC21_accumulator_LIST.append(char)
                    ALCHRC21 = ''.join(ALCHRC21_accumulator_LIST)
                elif 635 < cdx < 638:
                    ALTIME22_accumulator_LIST.append(char)
                    ALTIME22 = ''.join(ALTIME22_accumulator_LIST)
                elif 637 < cdx < 639:
                    ALUNIT22_accumulator_LIST.append(char)
                    ALUNIT22 = ''.join(ALUNIT22_accumulator_LIST)
                elif 638 < cdx < 641:
                    ALDURA22_accumulator_LIST.append(char)
                    ALDURA22 = ''.join(ALDURA22_accumulator_LIST)
                elif 640 < cdx < 642:
                    ALDURB22_accumulator_LIST.append(char)
                    ALDURB22 = ''.join(ALDURB22_accumulator_LIST)
                elif 641 < cdx < 643:
                    ALCHRC22_accumulator_LIST.append(char)
                    ALCHRC22 = ''.join(ALCHRC22_accumulator_LIST)
                elif 642 < cdx < 645:
                    ALTIME23_accumulator_LIST.append(char)
                    ALTIME23 = ''.join(ALTIME23_accumulator_LIST)
                elif 644 < cdx < 646:
                    ALUNIT23_accumulator_LIST.append(char)
                    ALUNIT23 = ''.join(ALUNIT23_accumulator_LIST)
                elif 645 < cdx < 648:
                    ALDURA23_accumulator_LIST.append(char)
                    ALDURA23 = ''.join(ALDURA23_accumulator_LIST)
                elif 647 < cdx < 649:
                    ALDURB23_accumulator_LIST.append(char)
                    ALDURB23 = ''.join(ALDURB23_accumulator_LIST)
                elif 648 < cdx < 650:
                    ALCHRC23_accumulator_LIST.append(char)
                    ALCHRC23 = ''.join(ALCHRC23_accumulator_LIST)
                elif 649 < cdx < 652:
                    ALTIME24_accumulator_LIST.append(char)
                    ALTIME24 = ''.join(ALTIME24_accumulator_LIST)
                elif 651 < cdx < 653:
                    ALUNIT24_accumulator_LIST.append(char)
                    ALUNIT24 = ''.join(ALUNIT24_accumulator_LIST)
                elif 652 < cdx < 655:
                    ALDURA24_accumulator_LIST.append(char)
                    ALDURA24 = ''.join(ALDURA24_accumulator_LIST)
                elif 654 < cdx < 656:
                    ALDURB24_accumulator_LIST.append(char)
                    ALDURB24 = ''.join(ALDURB24_accumulator_LIST)
                elif 655 < cdx < 657:
                    ALCHRC24_accumulator_LIST.append(char)
                    ALCHRC24 = ''.join(ALCHRC24_accumulator_LIST)
                elif 656 < cdx < 659:
                    ALTIME25_accumulator_LIST.append(char)
                    ALTIME25 = ''.join(ALTIME25_accumulator_LIST)
                elif 658 < cdx < 660:
                    ALUNIT25_accumulator_LIST.append(char)
                    ALUNIT25 = ''.join(ALUNIT25_accumulator_LIST)
                elif 659 < cdx < 662:
                    ALDURA25_accumulator_LIST.append(char)
                    ALDURA25 = ''.join(ALDURA25_accumulator_LIST)
                elif 661 < cdx < 663:
                    ALDURB25_accumulator_LIST.append(char)
                    ALDURB25 = ''.join(ALDURB25_accumulator_LIST)
                elif 662 < cdx < 664:
                    ALCHRC25_accumulator_LIST.append(char)
                    ALCHRC25 = ''.join(ALCHRC25_accumulator_LIST)
                elif 663 < cdx < 666:
                    ALTIME26_accumulator_LIST.append(char)
                    ALTIME26 = ''.join(ALTIME26_accumulator_LIST)
                elif 665 < cdx < 667:
                    ALUNIT26_accumulator_LIST.append(char)
                    ALUNIT26 = ''.join(ALUNIT26_accumulator_LIST)
                elif 666 < cdx < 669:
                    ALDURA26_accumulator_LIST.append(char)
                    ALDURA26 = ''.join(ALDURA26_accumulator_LIST)
                elif 668 < cdx < 670:
                    ALDURB26_accumulator_LIST.append(char)
                    ALDURB26 = ''.join(ALDURB26_accumulator_LIST)
                elif 669 < cdx < 671:
                    ALCHRC26_accumulator_LIST.append(char)
                    ALCHRC26 = ''.join(ALCHRC26_accumulator_LIST)
                elif 670 < cdx < 673:
                    ALTIME27_accumulator_LIST.append(char)
                    ALTIME27 = ''.join(ALTIME27_accumulator_LIST)
                elif 672 < cdx < 674:
                    ALUNIT27_accumulator_LIST.append(char)
                    ALUNIT27 = ''.join(ALUNIT27_accumulator_LIST)
                elif 673 < cdx < 676:
                    ALDURA27_accumulator_LIST.append(char)
                    ALDURA27 = ''.join(ALDURA27_accumulator_LIST)
                elif 675 < cdx < 677:
                    ALDURB27_accumulator_LIST.append(char)
                    ALDURB27 = ''.join(ALDURB27_accumulator_LIST)
                elif 676 < cdx < 678:
                    ALCHRC27_accumulator_LIST.append(char)
                    ALCHRC27 = ''.join(ALCHRC27_accumulator_LIST)
                elif 677 < cdx < 680:
                    ALTIME28_accumulator_LIST.append(char)
                    ALTIME28 = ''.join(ALTIME28_accumulator_LIST)
                elif 679 < cdx < 681:
                    ALUNIT28_accumulator_LIST.append(char)
                    ALUNIT28 = ''.join(ALUNIT28_accumulator_LIST)
                elif 680 < cdx < 683:
                    ALDURA28_accumulator_LIST.append(char)
                    ALDURA28 = ''.join(ALDURA28_accumulator_LIST)
                elif 682 < cdx < 684:
                    ALDURB28_accumulator_LIST.append(char)
                    ALDURB28 = ''.join(ALDURB28_accumulator_LIST)
                elif 683 < cdx < 685:
                    ALCHRC28_accumulator_LIST.append(char)
                    ALCHRC28 = ''.join(ALCHRC28_accumulator_LIST)
                elif 684 < cdx < 687:
                    ALTIME29_accumulator_LIST.append(char)
                    ALTIME29 = ''.join(ALTIME29_accumulator_LIST)
                elif 686 < cdx < 688:
                    ALUNIT29_accumulator_LIST.append(char)
                    ALUNIT29 = ''.join(ALUNIT29_accumulator_LIST)
                elif 687 < cdx < 690:
                    ALDURA29_accumulator_LIST.append(char)
                    ALDURA29 = ''.join(ALDURA29_accumulator_LIST)
                elif 689 < cdx < 691:
                    ALDURB29_accumulator_LIST.append(char)
                    ALDURB29 = ''.join(ALDURB29_accumulator_LIST)
                elif 690 < cdx < 692:
                    ALCHRC29_accumulator_LIST.append(char)
                    ALCHRC29 = ''.join(ALCHRC29_accumulator_LIST)
                elif 691 < cdx < 694:
                    ALTIME30_accumulator_LIST.append(char)
                    ALTIME30 = ''.join(ALTIME30_accumulator_LIST)
                elif 693 < cdx < 695:
                    ALUNIT30_accumulator_LIST.append(char)
                    ALUNIT30 = ''.join(ALUNIT30_accumulator_LIST)
                elif 694 < cdx < 697:
                    ALDURA30_accumulator_LIST.append(char)
                    ALDURA30 = ''.join(ALDURA30_accumulator_LIST)
                elif 696 < cdx < 698:
                    ALDURB30_accumulator_LIST.append(char)
                    ALDURB30 = ''.join(ALDURB30_accumulator_LIST)
                elif 697 < cdx < 699:
                    ALCHRC30_accumulator_LIST.append(char)
                    ALCHRC30 = ''.join(ALCHRC30_accumulator_LIST)
                elif 698 < cdx < 701:
                    ALTIME31_accumulator_LIST.append(char)
                    ALTIME31 = ''.join(ALTIME31_accumulator_LIST)
                elif 700 < cdx < 702:
                    ALUNIT31_accumulator_LIST.append(char)
                    ALUNIT31 = ''.join(ALUNIT31_accumulator_LIST)
                elif 701 < cdx < 704:
                    ALDURA31_accumulator_LIST.append(char)
                    ALDURA31 = ''.join(ALDURA31_accumulator_LIST)
                elif 703 < cdx < 705:
                    ALDURB31_accumulator_LIST.append(char)
                    ALDURB31 = ''.join(ALDURB31_accumulator_LIST)
                elif 704 < cdx < 706:
                    ALCHRC31_accumulator_LIST.append(char)
                    ALCHRC31 = ''.join(ALCHRC31_accumulator_LIST)
                elif 705 < cdx < 708:
                    ALTIME32_accumulator_LIST.append(char)
                    ALTIME32 = ''.join(ALTIME32_accumulator_LIST)
                elif 707 < cdx < 709:
                    ALUNIT32_accumulator_LIST.append(char)
                    ALUNIT32 = ''.join(ALUNIT32_accumulator_LIST)
                elif 708 < cdx < 711:
                    ALDURA32_accumulator_LIST.append(char)
                    ALDURA32 = ''.join(ALDURA32_accumulator_LIST)
                elif 710 < cdx < 712:
                    ALDURB32_accumulator_LIST.append(char)
                    ALDURB32 = ''.join(ALDURB32_accumulator_LIST)
                elif 711 < cdx < 713:
                    ALCHRC32_accumulator_LIST.append(char)
                    ALCHRC32 = ''.join(ALCHRC32_accumulator_LIST)
                elif 712 < cdx < 715:
                    ALTIME33_accumulator_LIST.append(char)
                    ALTIME33 = ''.join(ALTIME33_accumulator_LIST)
                elif 714 < cdx < 716:
                    ALUNIT33_accumulator_LIST.append(char)
                    ALUNIT33 = ''.join(ALUNIT33_accumulator_LIST)
                elif 715 < cdx < 718:
                    ALDURA33_accumulator_LIST.append(char)
                    ALDURA33 = ''.join(ALDURA33_accumulator_LIST)
                elif 717 < cdx < 719:
                    ALDURB33_accumulator_LIST.append(char)
                    ALDURB33 = ''.join(ALDURB33_accumulator_LIST)
                elif 718 < cdx < 720:
                    ALCHRC33_accumulator_LIST.append(char)
                    ALCHRC33 = ''.join(ALCHRC33_accumulator_LIST)
                elif 719 < cdx < 722:
                    ALTIME34_accumulator_LIST.append(char)
                    ALTIME34 = ''.join(ALTIME34_accumulator_LIST)
                elif 721 < cdx < 723:
                    ALUNIT34_accumulator_LIST.append(char)
                    ALUNIT34 = ''.join(ALUNIT34_accumulator_LIST)
                elif 722 < cdx < 725:
                    ALDURA34_accumulator_LIST.append(char)
                    ALDURA34 = ''.join(ALDURA34_accumulator_LIST)
                elif 724 < cdx < 726:
                    ALDURB34_accumulator_LIST.append(char)
                    ALDURB34 = ''.join(ALDURB34_accumulator_LIST)
                elif 725 < cdx < 727:
                    ALCHRC34_accumulator_LIST.append(char)
                    ALCHRC34 = ''.join(ALCHRC34_accumulator_LIST)
                elif 726 < cdx < 729:
                    ALTIME90_accumulator_LIST.append(char)
                    ALTIME90 = ''.join(ALTIME90_accumulator_LIST)
                elif 728 < cdx < 730:
                    ALUNIT90_accumulator_LIST.append(char)
                    ALUNIT90 = ''.join(ALUNIT90_accumulator_LIST)
                elif 729 < cdx < 732:
                    ALDURA90_accumulator_LIST.append(char)
                    ALDURA90 = ''.join(ALDURA90_accumulator_LIST)
                elif 731 < cdx < 733:
                    ALDURB90_accumulator_LIST.append(char)
                    ALDURB90 = ''.join(ALDURB90_accumulator_LIST)
                elif 732 < cdx < 734:
                    ALCHRC90_accumulator_LIST.append(char)
                    ALCHRC90 = ''.join(ALCHRC90_accumulator_LIST)
                elif 733 < cdx < 736:
                    ALTIME91_accumulator_LIST.append(char)
                    ALTIME91 = ''.join(ALTIME91_accumulator_LIST)
                elif 735 < cdx < 737:
                    ALUNIT91_accumulator_LIST.append(char)
                    ALUNIT91 = ''.join(ALUNIT91_accumulator_LIST)
                elif 736 < cdx < 739:
                    ALDURA91_accumulator_LIST.append(char)
                    ALDURA91 = ''.join(ALDURA91_accumulator_LIST)
                elif 738 < cdx < 740:
                    ALDURB91_accumulator_LIST.append(char)
                    ALDURB91 = ''.join(ALDURB91_accumulator_LIST)
                elif 739 < cdx < 741:
                    ALCHRC91_accumulator_LIST.append(char)
                    ALCHRC91 = ''.join(ALCHRC91_accumulator_LIST)
                elif 740 < cdx < 742:
                    ALCNDRT_accumulator_LIST.append(char)
                    ALCNDRT = ''.join(ALCNDRT_accumulator_LIST)
                elif 741 < cdx < 743:
                    ALCHRONR_accumulator_LIST.append(char)
                    ALCHRONR = ''.join(ALCHRONR_accumulator_LIST)
                elif 742 < cdx < 744:
                    SMKEV_accumulator_LIST.append(char)
                    SMKEV = ''.join(SMKEV_accumulator_LIST)
                elif 743 < cdx < 746:
                    SMKREG_accumulator_LIST.append(char)
                    SMKREG = ''.join(SMKREG_accumulator_LIST)
                elif 745 < cdx < 747:
                    SMKNOW_accumulator_LIST.append(char)
                    SMKNOW = ''.join(SMKNOW_accumulator_LIST)
                elif 746 < cdx < 748:
                    SMKSTAT2_accumulator_LIST.append(char)
                    SMKSTAT2 = ''.join(SMKSTAT2_accumulator_LIST)
                elif 747 < cdx < 750:
                    SMKQTNO_accumulator_LIST.append(char)
                    SMKQTNO = ''.join(SMKQTNO_accumulator_LIST)
                elif 749 < cdx < 751:
                    SMKQTTP_accumulator_LIST.append(char)
                    SMKQTTP = ''.join(SMKQTTP_accumulator_LIST)
                elif 750 < cdx < 753:
                    SMKQTY_accumulator_LIST.append(char)
                    SMKQTY = ''.join(SMKQTY_accumulator_LIST)
                elif 752 < cdx < 755:
                    CIGSDA1_accumulator_LIST.append(char)
                    CIGSDA1 = ''.join(CIGSDA1_accumulator_LIST)
                elif 754 < cdx < 757:
                    CIGDAMO_accumulator_LIST.append(char)
                    CIGDAMO = ''.join(CIGDAMO_accumulator_LIST)
                elif 756 < cdx < 759:
                    CIGSDA2_accumulator_LIST.append(char)
                    CIGSDA2 = ''.join(CIGSDA2_accumulator_LIST)
                elif 758 < cdx < 761:
                    CIGSDAY_accumulator_LIST.append(char)
                    CIGSDAY = ''.join(CIGSDAY_accumulator_LIST)
                elif 760 < cdx < 762:
                    CIGQTYR_accumulator_LIST.append(char)
                    CIGQTYR = ''.join(CIGQTYR_accumulator_LIST)
                elif 761 < cdx < 763:
                    OTHCIGEV_accumulator_LIST.append(char)
                    OTHCIGEV = ''.join(OTHCIGEV_accumulator_LIST)
                elif 762 < cdx < 764:
                    OTHCIGED_accumulator_LIST.append(char)
                    OTHCIGED = ''.join(OTHCIGED_accumulator_LIST)
                elif 763 < cdx < 765:
                    SMKLESEV_accumulator_LIST.append(char)
                    SMKLESEV = ''.join(SMKLESEV_accumulator_LIST)
                elif 764 < cdx < 766:
                    SMKLESED_accumulator_LIST.append(char)
                    SMKLESED = ''.join(SMKLESED_accumulator_LIST)
                elif 765 < cdx < 767:
                    TOBLASYR_accumulator_LIST.append(char)
                    TOBLASYR = ''.join(TOBLASYR_accumulator_LIST)
                elif 766 < cdx < 768:
                    TOBQTYR_accumulator_LIST.append(char)
                    TOBQTYR = ''.join(TOBQTYR_accumulator_LIST)
                elif 767 < cdx < 769:
                    ECIGEV_accumulator_LIST.append(char)
                    ECIGEV = ''.join(ECIGEV_accumulator_LIST)
                elif 768 < cdx < 770:
                    ECIGED_accumulator_LIST.append(char)
                    ECIGED = ''.join(ECIGED_accumulator_LIST)
                elif 769 < cdx < 773:
                    VIGNO_accumulator_LIST.append(char)
                    VIGNO = ''.join(VIGNO_accumulator_LIST)
                elif 772 < cdx < 774:
                    VIGTP_accumulator_LIST.append(char)
                    VIGTP = ''.join(VIGTP_accumulator_LIST)
                elif 773 < cdx < 776:
                    VIGFREQW_accumulator_LIST.append(char)
                    VIGFREQW = ''.join(VIGFREQW_accumulator_LIST)
                elif 775 < cdx < 779:
                    VIGLNGNO_accumulator_LIST.append(char)
                    VIGLNGNO = ''.join(VIGLNGNO_accumulator_LIST)
                elif 778 < cdx < 780:
                    VIGLNGTP_accumulator_LIST.append(char)
                    VIGLNGTP = ''.join(VIGLNGTP_accumulator_LIST)
                elif 779 < cdx < 783:
                    VIGMIN_accumulator_LIST.append(char)
                    VIGMIN = ''.join(VIGMIN_accumulator_LIST)
                elif 782 < cdx < 786:
                    MODNO_accumulator_LIST.append(char)
                    MODNO = ''.join(MODNO_accumulator_LIST)
                elif 785 < cdx < 787:
                    MODTP_accumulator_LIST.append(char)
                    MODTP = ''.join(MODTP_accumulator_LIST)
                elif 786 < cdx < 789:
                    MODFREQW_accumulator_LIST.append(char)
                    MODFREQW = ''.join(MODFREQW_accumulator_LIST)
                elif 788 < cdx < 792:
                    MODLNGNO_accumulator_LIST.append(char)
                    MODLNGNO = ''.join(MODLNGNO_accumulator_LIST)
                elif 791 < cdx < 793:
                    MODLNGTP_accumulator_LIST.append(char)
                    MODLNGTP = ''.join(MODLNGTP_accumulator_LIST)
                elif 792 < cdx < 796:
                    MODMIN_accumulator_LIST.append(char)
                    MODMIN = ''.join(MODMIN_accumulator_LIST)
                elif 795 < cdx < 799:
                    STRNGNO_accumulator_LIST.append(char)
                    STRNGNO = ''.join(STRNGNO_accumulator_LIST)
                elif 798 < cdx < 800:
                    STRNGTP_accumulator_LIST.append(char)
                    STRNGTP = ''.join(STRNGTP_accumulator_LIST)
                elif 799 < cdx < 802:
                    STRFREQW_accumulator_LIST.append(char)
                    STRFREQW = ''.join(STRFREQW_accumulator_LIST)
                elif 801 < cdx < 803:
                    ALC1YR_accumulator_LIST.append(char)
                    ALC1YR = ''.join(ALC1YR_accumulator_LIST)
                elif 802 < cdx < 804:
                    ALCLIFE_accumulator_LIST.append(char)
                    ALCLIFE = ''.join(ALCLIFE_accumulator_LIST)
                elif 803 < cdx < 807:
                    ALC12MNO_accumulator_LIST.append(char)
                    ALC12MNO = ''.join(ALC12MNO_accumulator_LIST)
                elif 806 < cdx < 808:
                    ALC12MTP_accumulator_LIST.append(char)
                    ALC12MTP = ''.join(ALC12MTP_accumulator_LIST)
                elif 807 < cdx < 810:
                    ALC12MWK_accumulator_LIST.append(char)
                    ALC12MWK = ''.join(ALC12MWK_accumulator_LIST)
                elif 809 < cdx < 813:
                    ALC12MYR_accumulator_LIST.append(char)
                    ALC12MYR = ''.join(ALC12MYR_accumulator_LIST)
                elif 812 < cdx < 815:
                    ALCAMT_accumulator_LIST.append(char)
                    ALCAMT = ''.join(ALCAMT_accumulator_LIST)
                elif 814 < cdx < 817:
                    ALCSTAT_accumulator_LIST.append(char)
                    ALCSTAT = ''.join(ALCSTAT_accumulator_LIST)
                elif 816 < cdx < 820:
                    ALC5UPN1_accumulator_LIST.append(char)
                    ALC5UPN1 = ''.join(ALC5UPN1_accumulator_LIST)
                elif 819 < cdx < 821:
                    ALC5UPT1_accumulator_LIST.append(char)
                    ALC5UPT1 = ''.join(ALC5UPT1_accumulator_LIST)
                elif 820 < cdx < 824:
                    ALC5UPY1_accumulator_LIST.append(char)
                    ALC5UPY1 = ''.join(ALC5UPY1_accumulator_LIST)
                elif 823 < cdx < 826:
                    AHEIGHT_accumulator_LIST.append(char)
                    AHEIGHT = ''.join(AHEIGHT_accumulator_LIST)
                elif 825 < cdx < 829:
                    AWEIGHTP_accumulator_LIST.append(char)
                    AWEIGHTP = ''.join(AWEIGHTP_accumulator_LIST)
                elif 828 < cdx < 833:
                    BMI_accumulator_LIST.append(char)
                    BMI = ''.join(BMI_accumulator_LIST)
                elif 832 < cdx < 834:
                    AUSUALPL_accumulator_LIST.append(char)
                    AUSUALPL = ''.join(AUSUALPL_accumulator_LIST)
                elif 833 < cdx < 835:
                    APLKIND_accumulator_LIST.append(char)
                    APLKIND = ''.join(APLKIND_accumulator_LIST)
                elif 834 < cdx < 836:
                    AHCPLROU_accumulator_LIST.append(char)
                    AHCPLROU = ''.join(AHCPLROU_accumulator_LIST)
                elif 835 < cdx < 837:
                    AHCPLKND_accumulator_LIST.append(char)
                    AHCPLKND = ''.join(AHCPLKND_accumulator_LIST)
                elif 836 < cdx < 838:
                    AHCCHGYR_accumulator_LIST.append(char)
                    AHCCHGYR = ''.join(AHCCHGYR_accumulator_LIST)
                elif 837 < cdx < 839:
                    AHCCHGHI_accumulator_LIST.append(char)
                    AHCCHGHI = ''.join(AHCCHGHI_accumulator_LIST)
                elif 838 < cdx < 840:
                    ANOUSPL1_accumulator_LIST.append(char)
                    ANOUSPL1 = ''.join(ANOUSPL1_accumulator_LIST)
                elif 839 < cdx < 841:
                    ANOUSPL2_accumulator_LIST.append(char)
                    ANOUSPL2 = ''.join(ANOUSPL2_accumulator_LIST)
                elif 840 < cdx < 842:
                    ANOUSPL3_accumulator_LIST.append(char)
                    ANOUSPL3 = ''.join(ANOUSPL3_accumulator_LIST)
                elif 841 < cdx < 843:
                    ANOUSPL4_accumulator_LIST.append(char)
                    ANOUSPL4 = ''.join(ANOUSPL4_accumulator_LIST)
                elif 842 < cdx < 844:
                    ANOUSPL5_accumulator_LIST.append(char)
                    ANOUSPL5 = ''.join(ANOUSPL5_accumulator_LIST)
                elif 843 < cdx < 845:
                    ANOUSPL6_accumulator_LIST.append(char)
                    ANOUSPL6 = ''.join(ANOUSPL6_accumulator_LIST)
                elif 844 < cdx < 846:
                    ANOUSPL7_accumulator_LIST.append(char)
                    ANOUSPL7 = ''.join(ANOUSPL7_accumulator_LIST)
                elif 845 < cdx < 847:
                    ANOUSPL8_accumulator_LIST.append(char)
                    ANOUSPL8 = ''.join(ANOUSPL8_accumulator_LIST)
                elif 846 < cdx < 848:
                    ANOUSPL9_accumulator_LIST.append(char)
                    ANOUSPL9 = ''.join(ANOUSPL9_accumulator_LIST)
                elif 847 < cdx < 849:
                    APRVTRYR_accumulator_LIST.append(char)
                    APRVTRYR = ''.join(APRVTRYR_accumulator_LIST)
                elif 848 < cdx < 850:
                    APRVTRFD_accumulator_LIST.append(char)
                    APRVTRFD = ''.join(APRVTRFD_accumulator_LIST)
                elif 849 < cdx < 851:
                    ADRNANP_accumulator_LIST.append(char)
                    ADRNANP = ''.join(ADRNANP_accumulator_LIST)
                elif 850 < cdx < 852:
                    ADRNAI_accumulator_LIST.append(char)
                    ADRNAI = ''.join(ADRNAI_accumulator_LIST)
                elif 851 < cdx < 853:
                    AHCDLYR1_accumulator_LIST.append(char)
                    AHCDLYR1 = ''.join(AHCDLYR1_accumulator_LIST)
                elif 852 < cdx < 854:
                    AHCDLYR2_accumulator_LIST.append(char)
                    AHCDLYR2 = ''.join(AHCDLYR2_accumulator_LIST)
                elif 853 < cdx < 855:
                    AHCDLYR3_accumulator_LIST.append(char)
                    AHCDLYR3 = ''.join(AHCDLYR3_accumulator_LIST)
                elif 854 < cdx < 856:
                    AHCDLYR4_accumulator_LIST.append(char)
                    AHCDLYR4 = ''.join(AHCDLYR4_accumulator_LIST)
                elif 855 < cdx < 857:
                    AHCDLYR5_accumulator_LIST.append(char)
                    AHCDLYR5 = ''.join(AHCDLYR5_accumulator_LIST)
                elif 856 < cdx < 858:
                    AHCAFYR1_accumulator_LIST.append(char)
                    AHCAFYR1 = ''.join(AHCAFYR1_accumulator_LIST)
                elif 857 < cdx < 859:
                    AHCAFYR2_accumulator_LIST.append(char)
                    AHCAFYR2 = ''.join(AHCAFYR2_accumulator_LIST)
                elif 858 < cdx < 860:
                    AHCAFYR3_accumulator_LIST.append(char)
                    AHCAFYR3 = ''.join(AHCAFYR3_accumulator_LIST)
                elif 859 < cdx < 861:
                    AHCAFYR4_accumulator_LIST.append(char)
                    AHCAFYR4 = ''.join(AHCAFYR4_accumulator_LIST)
                elif 860 < cdx < 862:
                    AHCAFYR5_accumulator_LIST.append(char)
                    AHCAFYR5 = ''.join(AHCAFYR5_accumulator_LIST)
                elif 861 < cdx < 863:
                    AHCAFYR6_accumulator_LIST.append(char)
                    AHCAFYR6 = ''.join(AHCAFYR6_accumulator_LIST)
                elif 862 < cdx < 864:
                    AWORPAY_accumulator_LIST.append(char)
                    AWORPAY = ''.join(AWORPAY_accumulator_LIST)
                elif 863 < cdx < 865:
                    AHICOMP_accumulator_LIST.append(char)
                    AHICOMP = ''.join(AHICOMP_accumulator_LIST)
                elif 864 < cdx < 866:
                    ARX12MO_accumulator_LIST.append(char)
                    ARX12MO = ''.join(ARX12MO_accumulator_LIST)
                elif 865 < cdx < 867:
                    ARX12_1_accumulator_LIST.append(char)
                    ARX12_1 = ''.join(ARX12_1_accumulator_LIST)
                elif 866 < cdx < 868:
                    ARX12_2_accumulator_LIST.append(char)
                    ARX12_2 = ''.join(ARX12_2_accumulator_LIST)
                elif 867 < cdx < 869:
                    ARX12_3_accumulator_LIST.append(char)
                    ARX12_3 = ''.join(ARX12_3_accumulator_LIST)
                elif 868 < cdx < 870:
                    ARX12_4_accumulator_LIST.append(char)
                    ARX12_4 = ''.join(ARX12_4_accumulator_LIST)
                elif 869 < cdx < 871:
                    ARX12_5_accumulator_LIST.append(char)
                    ARX12_5 = ''.join(ARX12_5_accumulator_LIST)
                elif 870 < cdx < 872:
                    ARX12_6_accumulator_LIST.append(char)
                    ARX12_6 = ''.join(ARX12_6_accumulator_LIST)
                elif 871 < cdx < 873:
                    ADNLONG2_accumulator_LIST.append(char)
                    ADNLONG2 = ''.join(ADNLONG2_accumulator_LIST)
                elif 872 < cdx < 874:
                    AHCSYR1_accumulator_LIST.append(char)
                    AHCSYR1 = ''.join(AHCSYR1_accumulator_LIST)
                elif 873 < cdx < 875:
                    AHCSYR2_accumulator_LIST.append(char)
                    AHCSYR2 = ''.join(AHCSYR2_accumulator_LIST)
                elif 874 < cdx < 876:
                    AHCSYR3_accumulator_LIST.append(char)
                    AHCSYR3 = ''.join(AHCSYR3_accumulator_LIST)
                elif 875 < cdx < 877:
                    AHCSYR4_accumulator_LIST.append(char)
                    AHCSYR4 = ''.join(AHCSYR4_accumulator_LIST)
                elif 876 < cdx < 878:
                    AHCSYR5_accumulator_LIST.append(char)
                    AHCSYR5 = ''.join(AHCSYR5_accumulator_LIST)
                elif 877 < cdx < 879:
                    AHCSYR6_accumulator_LIST.append(char)
                    AHCSYR6 = ''.join(AHCSYR6_accumulator_LIST)
                elif 878 < cdx < 880:
                    AHCSYR7_accumulator_LIST.append(char)
                    AHCSYR7 = ''.join(AHCSYR7_accumulator_LIST)
                elif 879 < cdx < 881:
                    AHCSYR8_accumulator_LIST.append(char)
                    AHCSYR8 = ''.join(AHCSYR8_accumulator_LIST)
                elif 880 < cdx < 882:
                    AHCSYR9_accumulator_LIST.append(char)
                    AHCSYR9 = ''.join(AHCSYR9_accumulator_LIST)
                elif 881 < cdx < 883:
                    AHCSYR10_accumulator_LIST.append(char)
                    AHCSYR10 = ''.join(AHCSYR10_accumulator_LIST)
                elif 882 < cdx < 885:
                    AHERNOY2_accumulator_LIST.append(char)
                    AHERNOY2 = ''.join(AHERNOY2_accumulator_LIST)
                elif 884 < cdx < 886:
                    AERVISND_accumulator_LIST.append(char)
                    AERVISND = ''.join(AERVISND_accumulator_LIST)
                elif 885 < cdx < 887:
                    AERHOS_accumulator_LIST.append(char)
                    AERHOS = ''.join(AERHOS_accumulator_LIST)
                elif 886 < cdx < 888:
                    AERREA1R_accumulator_LIST.append(char)
                    AERREA1R = ''.join(AERREA1R_accumulator_LIST)
                elif 887 < cdx < 889:
                    AERREA2R_accumulator_LIST.append(char)
                    AERREA2R = ''.join(AERREA2R_accumulator_LIST)
                elif 888 < cdx < 890:
                    AERREA3R_accumulator_LIST.append(char)
                    AERREA3R = ''.join(AERREA3R_accumulator_LIST)
                elif 889 < cdx < 891:
                    AERREA4R_accumulator_LIST.append(char)
                    AERREA4R = ''.join(AERREA4R_accumulator_LIST)
                elif 890 < cdx < 892:
                    AERREA5R_accumulator_LIST.append(char)
                    AERREA5R = ''.join(AERREA5R_accumulator_LIST)
                elif 891 < cdx < 893:
                    AERREA6R_accumulator_LIST.append(char)
                    AERREA6R = ''.join(AERREA6R_accumulator_LIST)
                elif 892 < cdx < 894:
                    AERREA7R_accumulator_LIST.append(char)
                    AERREA7R = ''.join(AERREA7R_accumulator_LIST)
                elif 893 < cdx < 895:
                    AERREA8R_accumulator_LIST.append(char)
                    AERREA8R = ''.join(AERREA8R_accumulator_LIST)
                elif 894 < cdx < 896:
                    AHCHYR_accumulator_LIST.append(char)
                    AHCHYR = ''.join(AHCHYR_accumulator_LIST)
                elif 895 < cdx < 898:
                    AHCHMOYR_accumulator_LIST.append(char)
                    AHCHMOYR = ''.join(AHCHMOYR_accumulator_LIST)
                elif 897 < cdx < 900:
                    AHCHNOY2_accumulator_LIST.append(char)
                    AHCHNOY2 = ''.join(AHCHNOY2_accumulator_LIST)
                elif 899 < cdx < 902:
                    AHCNOYR2_accumulator_LIST.append(char)
                    AHCNOYR2 = ''.join(AHCNOYR2_accumulator_LIST)
                elif 901 < cdx < 903:
                    ASRGYR_accumulator_LIST.append(char)
                    ASRGYR = ''.join(ASRGYR_accumulator_LIST)
                elif 902 < cdx < 905:
                    ASRGNOYR_accumulator_LIST.append(char)
                    ASRGNOYR = ''.join(ASRGNOYR_accumulator_LIST)
                elif 904 < cdx < 906:
                    AMDLONGR_accumulator_LIST.append(char)
                    AMDLONGR = ''.join(AMDLONGR_accumulator_LIST)
                elif 905 < cdx < 907:
                    AVISLAST_accumulator_LIST.append(char)
                    AVISLAST = ''.join(AVISLAST_accumulator_LIST)
                elif 906 < cdx < 908:
                    ALASTYP1_accumulator_LIST.append(char)
                    ALASTYP1 = ''.join(ALASTYP1_accumulator_LIST)
                elif 907 < cdx < 909:
                    ALASTYP2_accumulator_LIST.append(char)
                    ALASTYP2 = ''.join(ALASTYP2_accumulator_LIST)
                elif 908 < cdx < 910:
                    ALASTYP3_accumulator_LIST.append(char)
                    ALASTYP3 = ''.join(ALASTYP3_accumulator_LIST)
                elif 909 < cdx < 911:
                    ALASTYP4_accumulator_LIST.append(char)
                    ALASTYP4 = ''.join(ALASTYP4_accumulator_LIST)
                elif 910 < cdx < 956:
                    ALASTVRB_accumulator_LIST.append(char)
                    ALASTVRB = ''.join(ALASTVRB_accumulator_LIST)
                elif 955 < cdx < 958:
                    AVISAPN2_accumulator_LIST.append(char)
                    AVISAPN2 = ''.join(AVISAPN2_accumulator_LIST)
                elif 957 < cdx < 959:
                    AVISAPT2_accumulator_LIST.append(char)
                    AVISAPT2 = ''.join(AVISAPT2_accumulator_LIST)
                elif 958 < cdx < 961:
                    AWAITRMN_accumulator_LIST.append(char)
                    AWAITRMN = ''.join(AWAITRMN_accumulator_LIST)
                elif 960 < cdx < 962:
                    AWAITRMT_accumulator_LIST.append(char)
                    AWAITRMT = ''.join(AWAITRMT_accumulator_LIST)
                elif 961 < cdx < 963:
                    HIT1A_accumulator_LIST.append(char)
                    HIT1A = ''.join(HIT1A_accumulator_LIST)
                elif 962 < cdx < 964:
                    HIT2A_accumulator_LIST.append(char)
                    HIT2A = ''.join(HIT2A_accumulator_LIST)
                elif 963 < cdx < 965:
                    HIT3A_accumulator_LIST.append(char)
                    HIT3A = ''.join(HIT3A_accumulator_LIST)
                elif 964 < cdx < 966:
                    HIT4A_accumulator_LIST.append(char)
                    HIT4A = ''.join(HIT4A_accumulator_LIST)
                elif 965 < cdx < 967:
                    HIT5A_accumulator_LIST.append(char)
                    HIT5A = ''.join(HIT5A_accumulator_LIST)
                elif 966 < cdx < 968:
                    SHTFLU2_accumulator_LIST.append(char)
                    SHTFLU2 = ''.join(SHTFLU2_accumulator_LIST)
                elif 967 < cdx < 970:
                    ASHFLUM2_accumulator_LIST.append(char)
                    ASHFLUM2 = ''.join(ASHFLUM2_accumulator_LIST)
                elif 969 < cdx < 974:
                    ASHFLUY2_accumulator_LIST.append(char)
                    ASHFLUY2 = ''.join(ASHFLUY2_accumulator_LIST)
                elif 973 < cdx < 975:
                    FLUSHPG1_accumulator_LIST.append(char)
                    FLUSHPG1 = ''.join(FLUSHPG1_accumulator_LIST)
                elif 974 < cdx < 976:
                    FLUSHPG2_accumulator_LIST.append(char)
                    FLUSHPG2 = ''.join(FLUSHPG2_accumulator_LIST)
                elif 975 < cdx < 977:
                    SPRFLU2_accumulator_LIST.append(char)
                    SPRFLU2 = ''.join(SPRFLU2_accumulator_LIST)
                elif 976 < cdx < 979:
                    ASPFLUM2_accumulator_LIST.append(char)
                    ASPFLUM2 = ''.join(ASPFLUM2_accumulator_LIST)
                elif 978 < cdx < 983:
                    ASPFLUY2_accumulator_LIST.append(char)
                    ASPFLUY2 = ''.join(ASPFLUY2_accumulator_LIST)
                elif 982 < cdx < 984:
                    SHTPNUYR_accumulator_LIST.append(char)
                    SHTPNUYR = ''.join(SHTPNUYR_accumulator_LIST)
                elif 983 < cdx < 985:
                    APOX_accumulator_LIST.append(char)
                    APOX = ''.join(APOX_accumulator_LIST)
                elif 984 < cdx < 986:
                    APOX12MO_accumulator_LIST.append(char)
                    APOX12MO = ''.join(APOX12MO_accumulator_LIST)
                elif 985 < cdx < 987:
                    AHEP_accumulator_LIST.append(char)
                    AHEP = ''.join(AHEP_accumulator_LIST)
                elif 986 < cdx < 988:
                    AHEPLIV_accumulator_LIST.append(char)
                    AHEPLIV = ''.join(AHEPLIV_accumulator_LIST)
                elif 987 < cdx < 989:
                    AHEPBTST_accumulator_LIST.append(char)
                    AHEPBTST = ''.join(AHEPBTST_accumulator_LIST)
                elif 988 < cdx < 990:
                    SHTHEPB_accumulator_LIST.append(char)
                    SHTHEPB = ''.join(SHTHEPB_accumulator_LIST)
                elif 989 < cdx < 991:
                    SHEPDOS_accumulator_LIST.append(char)
                    SHEPDOS = ''.join(SHEPDOS_accumulator_LIST)
                elif 990 < cdx < 992:
                    SHTHEPA_accumulator_LIST.append(char)
                    SHTHEPA = ''.join(SHTHEPA_accumulator_LIST)
                elif 991 < cdx < 994:
                    SHEPANUM_accumulator_LIST.append(char)
                    SHEPANUM = ''.join(SHEPANUM_accumulator_LIST)
                elif 993 < cdx < 995:
                    AHEPCTST_accumulator_LIST.append(char)
                    AHEPCTST = ''.join(AHEPCTST_accumulator_LIST)
                elif 994 < cdx < 996:
                    AHEPCRES_accumulator_LIST.append(char)
                    AHEPCRES = ''.join(AHEPCRES_accumulator_LIST)
                elif 995 < cdx < 997:
                    SHINGLES_accumulator_LIST.append(char)
                    SHINGLES = ''.join(SHINGLES_accumulator_LIST)
                elif 996 < cdx < 998:
                    SHTTD_accumulator_LIST.append(char)
                    SHTTD = ''.join(SHTTD_accumulator_LIST)
                elif 997 < cdx < 999:
                    SHTTD05_accumulator_LIST.append(char)
                    SHTTD05 = ''.join(SHTTD05_accumulator_LIST)
                elif 998 < cdx < 1000:
                    SHTTDAP2_accumulator_LIST.append(char)
                    SHTTDAP2 = ''.join(SHTTDAP2_accumulator_LIST)
                elif 999 < cdx < 1001:
                    SHTHPV2_accumulator_LIST.append(char)
                    SHTHPV2 = ''.join(SHTHPV2_accumulator_LIST)
                elif 1000 < cdx < 1003:
                    SHHPVDOS_accumulator_LIST.append(char)
                    SHHPVDOS = ''.join(SHHPVDOS_accumulator_LIST)
                elif 1002 < cdx < 1006:
                    AHPVAGE_accumulator_LIST.append(char)
                    AHPVAGE = ''.join(AHPVAGE_accumulator_LIST)
                elif 1005 < cdx < 1007:
                    LIVEV_accumulator_LIST.append(char)
                    LIVEV = ''.join(LIVEV_accumulator_LIST)
                elif 1006 < cdx < 1008:
                    TRAVEL_accumulator_LIST.append(char)
                    TRAVEL = ''.join(TRAVEL_accumulator_LIST)
                elif 1007 < cdx < 1009:
                    WRKHLTH2_accumulator_LIST.append(char)
                    WRKHLTH2 = ''.join(WRKHLTH2_accumulator_LIST)
                elif 1008 < cdx < 1010:
                    WRKDIR_accumulator_LIST.append(char)
                    WRKDIR = ''.join(WRKDIR_accumulator_LIST)
                elif 1009 < cdx < 1011:
                    APSBPCH1_accumulator_LIST.append(char)
                    APSBPCH1 = ''.join(APSBPCH1_accumulator_LIST)
                elif 1010 < cdx < 1012:
                    APSCHCH1_accumulator_LIST.append(char)
                    APSCHCH1 = ''.join(APSCHCH1_accumulator_LIST)
                elif 1011 < cdx < 1013:
                    APSBSCH1_accumulator_LIST.append(char)
                    APSBSCH1 = ''.join(APSBSCH1_accumulator_LIST)
                elif 1012 < cdx < 1014:
                    APSPAP_accumulator_LIST.append(char)
                    APSPAP = ''.join(APSPAP_accumulator_LIST)
                elif 1013 < cdx < 1015:
                    APSMAM_accumulator_LIST.append(char)
                    APSMAM = ''.join(APSMAM_accumulator_LIST)
                elif 1014 < cdx < 1016:
                    APSCOL_accumulator_LIST.append(char)
                    APSCOL = ''.join(APSCOL_accumulator_LIST)
                elif 1015 < cdx < 1017:
                    APSDIET_accumulator_LIST.append(char)
                    APSDIET = ''.join(APSDIET_accumulator_LIST)
                elif 1016 < cdx < 1018:
                    APSSMKC_accumulator_LIST.append(char)
                    APSSMKC = ''.join(APSSMKC_accumulator_LIST)
                elif 1017 < cdx < 1019:
                    LTCFAM_accumulator_LIST.append(char)
                    LTCFAM = ''.join(LTCFAM_accumulator_LIST)
                elif 1018 < cdx < 1020:
                    LTCHELP_accumulator_LIST.append(char)
                    LTCHELP = ''.join(LTCHELP_accumulator_LIST)
                elif 1019 < cdx < 1021:
                    LTCWHO1_accumulator_LIST.append(char)
                    LTCWHO1 = ''.join(LTCWHO1_accumulator_LIST)
                elif 1020 < cdx < 1022:
                    LTCWHO2_accumulator_LIST.append(char)
                    LTCWHO2 = ''.join(LTCWHO2_accumulator_LIST)
                elif 1021 < cdx < 1023:
                    LTCWHO3_accumulator_LIST.append(char)
                    LTCWHO3 = ''.join(LTCWHO3_accumulator_LIST)
                elif 1022 < cdx < 1024:
                    LTCWHO4_accumulator_LIST.append(char)
                    LTCWHO4 = ''.join(LTCWHO4_accumulator_LIST)
                elif 1023 < cdx < 1025:
                    LTCWHO5_accumulator_LIST.append(char)
                    LTCWHO5 = ''.join(LTCWHO5_accumulator_LIST)
                elif 1024 < cdx < 1026:
                    AINDINS_accumulator_LIST.append(char)
                    AINDINS = ''.join(AINDINS_accumulator_LIST)
                elif 1025 < cdx < 1027:
                    AINDPRCH_accumulator_LIST.append(char)
                    AINDPRCH = ''.join(AINDPRCH_accumulator_LIST)
                elif 1026 < cdx < 1028:
                    AINDWHO_accumulator_LIST.append(char)
                    AINDWHO = ''.join(AINDWHO_accumulator_LIST)
                elif 1027 < cdx < 1029:
                    AINDDIF1_accumulator_LIST.append(char)
                    AINDDIF1 = ''.join(AINDDIF1_accumulator_LIST)
                elif 1028 < cdx < 1030:
                    AINDDIF2_accumulator_LIST.append(char)
                    AINDDIF2 = ''.join(AINDDIF2_accumulator_LIST)
                elif 1029 < cdx < 1031:
                    AINDENY1_accumulator_LIST.append(char)
                    AINDENY1 = ''.join(AINDENY1_accumulator_LIST)
                elif 1030 < cdx < 1032:
                    AINDENY2_accumulator_LIST.append(char)
                    AINDENY2 = ''.join(AINDENY2_accumulator_LIST)
                elif 1031 < cdx < 1033:
                    AINDENY3_accumulator_LIST.append(char)
                    AINDENY3 = ''.join(AINDENY3_accumulator_LIST)
                elif 1032 < cdx < 1034:
                    AINDNOT1_accumulator_LIST.append(char)
                    AINDNOT1 = ''.join(AINDNOT1_accumulator_LIST)
                elif 1033 < cdx < 1035:
                    AINDNOT2_accumulator_LIST.append(char)
                    AINDNOT2 = ''.join(AINDNOT2_accumulator_LIST)
                elif 1034 < cdx < 1036:
                    AINDNOT3_accumulator_LIST.append(char)
                    AINDNOT3 = ''.join(AINDNOT3_accumulator_LIST)
                elif 1035 < cdx < 1037:
                    AINDNOT4_accumulator_LIST.append(char)
                    AINDNOT4 = ''.join(AINDNOT4_accumulator_LIST)
                elif 1036 < cdx < 1038:
                    AINDNOT5_accumulator_LIST.append(char)
                    AINDNOT5 = ''.join(AINDNOT5_accumulator_LIST)
                elif 1037 < cdx < 1039:
                    AEXCHNG_accumulator_LIST.append(char)
                    AEXCHNG = ''.join(AEXCHNG_accumulator_LIST)
                elif 1038 < cdx < 1040:
                    ASICPUSE_accumulator_LIST.append(char)
                    ASICPUSE = ''.join(ASICPUSE_accumulator_LIST)
                elif 1039 < cdx < 1041:
                    ASISATHC_accumulator_LIST.append(char)
                    ASISATHC = ''.join(ASISATHC_accumulator_LIST)
                elif 1040 < cdx < 1042:
                    ASITENUR_accumulator_LIST.append(char)
                    ASITENUR = ''.join(ASITENUR_accumulator_LIST)
                elif 1041 < cdx < 1043:
                    ASINHELP_accumulator_LIST.append(char)
                    ASINHELP = ''.join(ASINHELP_accumulator_LIST)
                elif 1042 < cdx < 1044:
                    ASINCNTO_accumulator_LIST.append(char)
                    ASINCNTO = ''.join(ASINCNTO_accumulator_LIST)
                elif 1043 < cdx < 1045:
                    ASINTRU_accumulator_LIST.append(char)
                    ASINTRU = ''.join(ASINTRU_accumulator_LIST)
                elif 1044 < cdx < 1046:
                    ASINKNT_accumulator_LIST.append(char)
                    ASINKNT = ''.join(ASINKNT_accumulator_LIST)
                elif 1045 < cdx < 1047:
                    ASISIM_accumulator_LIST.append(char)
                    ASISIM = ''.join(ASISIM_accumulator_LIST)
                elif 1046 < cdx < 1048:
                    ASISIF_accumulator_LIST.append(char)
                    ASISIF = ''.join(ASISIF_accumulator_LIST)
                elif 1047 < cdx < 1049:
                    ASIRETR_accumulator_LIST.append(char)
                    ASIRETR = ''.join(ASIRETR_accumulator_LIST)
                elif 1048 < cdx < 1050:
                    ASIMEDC_accumulator_LIST.append(char)
                    ASIMEDC = ''.join(ASIMEDC_accumulator_LIST)
                elif 1049 < cdx < 1051:
                    ASISTLV_accumulator_LIST.append(char)
                    ASISTLV = ''.join(ASISTLV_accumulator_LIST)
                elif 1050 < cdx < 1052:
                    ASICNHC_accumulator_LIST.append(char)
                    ASICNHC = ''.join(ASICNHC_accumulator_LIST)
                elif 1051 < cdx < 1053:
                    ASICCOLL_accumulator_LIST.append(char)
                    ASICCOLL = ''.join(ASICCOLL_accumulator_LIST)
                elif 1052 < cdx < 1054:
                    ASINBILL_accumulator_LIST.append(char)
                    ASINBILL = ''.join(ASINBILL_accumulator_LIST)
                elif 1053 < cdx < 1055:
                    ASIHCST_accumulator_LIST.append(char)
                    ASIHCST = ''.join(ASIHCST_accumulator_LIST)
                elif 1054 < cdx < 1056:
                    ASICCMP_accumulator_LIST.append(char)
                    ASICCMP = ''.join(ASICCMP_accumulator_LIST)
                elif 1055 < cdx < 1058:
                    ASISLEEP_accumulator_LIST.append(char)
                    ASISLEEP = ''.join(ASISLEEP_accumulator_LIST)
                elif 1057 < cdx < 1060:
                    ASISLPFL_accumulator_LIST.append(char)
                    ASISLPFL = ''.join(ASISLPFL_accumulator_LIST)
                elif 1059 < cdx < 1062:
                    ASISLPST_accumulator_LIST.append(char)
                    ASISLPST = ''.join(ASISLPST_accumulator_LIST)
                elif 1061 < cdx < 1064:
                    ASISLPMD_accumulator_LIST.append(char)
                    ASISLPMD = ''.join(ASISLPMD_accumulator_LIST)
                elif 1063 < cdx < 1066:
                    ASIREST_accumulator_LIST.append(char)
                    ASIREST = ''.join(ASIREST_accumulator_LIST)
                elif 1065 < cdx < 1067:
                    ASISAD_accumulator_LIST.append(char)
                    ASISAD = ''.join(ASISAD_accumulator_LIST)
                elif 1066 < cdx < 1068:
                    ASINERV_accumulator_LIST.append(char)
                    ASINERV = ''.join(ASINERV_accumulator_LIST)
                elif 1067 < cdx < 1069:
                    ASIRSTLS_accumulator_LIST.append(char)
                    ASIRSTLS = ''.join(ASIRSTLS_accumulator_LIST)
                elif 1068 < cdx < 1070:
                    ASIHOPLS_accumulator_LIST.append(char)
                    ASIHOPLS = ''.join(ASIHOPLS_accumulator_LIST)
                elif 1069 < cdx < 1071:
                    ASIEFFRT_accumulator_LIST.append(char)
                    ASIEFFRT = ''.join(ASIEFFRT_accumulator_LIST)
                elif 1070 < cdx < 1072:
                    ASIWTHLS_accumulator_LIST.append(char)
                    ASIWTHLS = ''.join(ASIWTHLS_accumulator_LIST)
                elif 1071 < cdx < 1073:
                    ASIMUCH_accumulator_LIST.append(char)
                    ASIMUCH = ''.join(ASIMUCH_accumulator_LIST)
                elif 1072 < cdx < 1074:
                    ASIHIVT_accumulator_LIST.append(char)
                    ASIHIVT = ''.join(ASIHIVT_accumulator_LIST)
                elif 1073 < cdx < 1076:
                    ASIHIVWN_accumulator_LIST.append(char)
                    ASIHIVWN = ''.join(ASIHIVWN_accumulator_LIST)
                elif 1075 < cdx < 1077:
                    AWEBUSE_accumulator_LIST.append(char)
                    AWEBUSE = ''.join(AWEBUSE_accumulator_LIST)
                elif 1076 < cdx < 1080:
                    AWEBOFNO_accumulator_LIST.append(char)
                    AWEBOFNO = ''.join(AWEBOFNO_accumulator_LIST)
                elif 1079 < cdx < 1081:
                    AWEBOFTP_accumulator_LIST.append(char)
                    AWEBOFTP = ''.join(AWEBOFTP_accumulator_LIST)
                elif 1080 < cdx < 1082:
                    AWEBORP_accumulator_LIST.append(char)
                    AWEBORP = ''.join(AWEBORP_accumulator_LIST)
                elif 1081 < cdx < 1083:
                    AWEBEML_accumulator_LIST.append(char)
                    AWEBEML = ''.join(AWEBEML_accumulator_LIST)
                elif 1082 < cdx < 1086:
                    AWEBMNO_accumulator_LIST.append(char)
                    AWEBMNO = ''.join(AWEBMNO_accumulator_LIST)
                elif 1085 < cdx < 1087:
                    AWEBMTP_accumulator_LIST.append(char)
                    AWEBMTP = ''.join(AWEBMTP_accumulator_LIST)
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
        FPX_LIST.append(FPX)
        WTIA_SA_LIST.append(WTIA_SA)
        WTFA_SA_LIST.append(WTFA_SA)
        REGION_LIST.append(REGION)
        STRAT_P_LIST.append(STRAT_P)
        PSU_P_LIST.append(PSU_P)
        SEX_LIST.append(SEX)
        HISPAN_I_LIST.append(HISPAN_I)
        RACERPI2_LIST.append(RACERPI2)
        MRACRPI2_LIST.append(MRACRPI2)
        MRACBPI2_LIST.append(MRACBPI2)
        AGE_P_LIST.append(AGE_P)
        R_MARITL_LIST.append(R_MARITL)
        PROXYSA_LIST.append(PROXYSA)
        PROX1_LIST.append(PROX1)
        PROX2_LIST.append(PROX2)
        LATEINTA_LIST.append(LATEINTA)
        FDRN_FLG_LIST.append(FDRN_FLG)
        DOINGLWA_LIST.append(DOINGLWA)
        WHYNOWKA_LIST.append(WHYNOWKA)
        EVERWRK_LIST.append(EVERWRK)
        INDSTRN1_LIST.append(INDSTRN1)
        INDSTRN2_LIST.append(INDSTRN2)
        OCCUPN1_LIST.append(OCCUPN1)
        OCCUPN2_LIST.append(OCCUPN2)
        WRKCATA_LIST.append(WRKCATA)
        BUSINC1A_LIST.append(BUSINC1A)
        LOCALL1A_LIST.append(LOCALL1A)
        YRSWRKPA_LIST.append(YRSWRKPA)
        WRKLONGH_LIST.append(WRKLONGH)
        HOURPDA_LIST.append(HOURPDA)
        PDSICKA_LIST.append(PDSICKA)
        ONEJOB_LIST.append(ONEJOB)
        WRKLYR4_LIST.append(WRKLYR4)
        HYPEV_LIST.append(HYPEV)
        HYPDIFV_LIST.append(HYPDIFV)
        HYPYR1_LIST.append(HYPYR1)
        HYBPCKNO_LIST.append(HYBPCKNO)
        HYBPCKTP_LIST.append(HYBPCKTP)
        HYBPLEV_LIST.append(HYBPLEV)
        HYPMDEV2_LIST.append(HYPMDEV2)
        HYPMED2_LIST.append(HYPMED2)
        CHLEV_LIST.append(CHLEV)
        CHLYR_LIST.append(CHLYR)
        CLCKNO_LIST.append(CLCKNO)
        CLCKTP_LIST.append(CLCKTP)
        CHLMDEV2_LIST.append(CHLMDEV2)
        CHLMDNW2_LIST.append(CHLMDNW2)
        CHDEV_LIST.append(CHDEV)
        ANGEV_LIST.append(ANGEV)
        MIEV_LIST.append(MIEV)
        HRTEV_LIST.append(HRTEV)
        STREV_LIST.append(STREV)
        EPHEV_LIST.append(EPHEV)
        JAWP_LIST.append(JAWP)
        WEA_LIST.append(WEA)
        CHE_LIST.append(CHE)
        ARM_LIST.append(ARM)
        BRTH_LIST.append(BRTH)
        AHADO_LIST.append(AHADO)
        FACE_LIST.append(FACE)
        SPEAKING_LIST.append(SPEAKING)
        EYE_LIST.append(EYE)
        WALKING_LIST.append(WALKING)
        HEADACHE_LIST.append(HEADACHE)
        ASTDO_LIST.append(ASTDO)
        COPDEV_LIST.append(COPDEV)
        ASPMEDEV_LIST.append(ASPMEDEV)
        ASPMEDAD_LIST.append(ASPMEDAD)
        ASPMDMED_LIST.append(ASPMDMED)
        ASPONOWN_LIST.append(ASPONOWN)
        AASMEV_LIST.append(AASMEV)
        AASSTILL_LIST.append(AASSTILL)
        AASMYR_LIST.append(AASMYR)
        AASERYR1_LIST.append(AASERYR1)
        ULCEV_LIST.append(ULCEV)
        ULCYR_LIST.append(ULCYR)
        CANEV_LIST.append(CANEV)
        CNKIND1_LIST.append(CNKIND1)
        CNKIND2_LIST.append(CNKIND2)
        CNKIND3_LIST.append(CNKIND3)
        CNKIND4_LIST.append(CNKIND4)
        CNKIND5_LIST.append(CNKIND5)
        CNKIND6_LIST.append(CNKIND6)
        CNKIND7_LIST.append(CNKIND7)
        CNKIND8_LIST.append(CNKIND8)
        CNKIND9_LIST.append(CNKIND9)
        CNKIND10_LIST.append(CNKIND10)
        CNKIND11_LIST.append(CNKIND11)
        CNKIND12_LIST.append(CNKIND12)
        CNKIND13_LIST.append(CNKIND13)
        CNKIND14_LIST.append(CNKIND14)
        CNKIND15_LIST.append(CNKIND15)
        CNKIND16_LIST.append(CNKIND16)
        CNKIND17_LIST.append(CNKIND17)
        CNKIND18_LIST.append(CNKIND18)
        CNKIND19_LIST.append(CNKIND19)
        CNKIND20_LIST.append(CNKIND20)
        CNKIND21_LIST.append(CNKIND21)
        CNKIND22_LIST.append(CNKIND22)
        CNKIND23_LIST.append(CNKIND23)
        CNKIND24_LIST.append(CNKIND24)
        CNKIND25_LIST.append(CNKIND25)
        CNKIND26_LIST.append(CNKIND26)
        CNKIND27_LIST.append(CNKIND27)
        CNKIND28_LIST.append(CNKIND28)
        CNKIND29_LIST.append(CNKIND29)
        CNKIND30_LIST.append(CNKIND30)
        CNKIND31_LIST.append(CNKIND31)
        CANAGE1_LIST.append(CANAGE1)
        CANAGE2_LIST.append(CANAGE2)
        CANAGE3_LIST.append(CANAGE3)
        CANAGE4_LIST.append(CANAGE4)
        CANAGE5_LIST.append(CANAGE5)
        CANAGE6_LIST.append(CANAGE6)
        CANAGE7_LIST.append(CANAGE7)
        CANAGE8_LIST.append(CANAGE8)
        CANAGE9_LIST.append(CANAGE9)
        CANAGE10_LIST.append(CANAGE10)
        CANAGE11_LIST.append(CANAGE11)
        CANAGE12_LIST.append(CANAGE12)
        CANAGE13_LIST.append(CANAGE13)
        CANAGE14_LIST.append(CANAGE14)
        CANAGE15_LIST.append(CANAGE15)
        CANAGE16_LIST.append(CANAGE16)
        CANAGE17_LIST.append(CANAGE17)
        CANAGE18_LIST.append(CANAGE18)
        CANAGE19_LIST.append(CANAGE19)
        CANAGE20_LIST.append(CANAGE20)
        CANAGE21_LIST.append(CANAGE21)
        CANAGE22_LIST.append(CANAGE22)
        CANAGE23_LIST.append(CANAGE23)
        CANAGE24_LIST.append(CANAGE24)
        CANAGE25_LIST.append(CANAGE25)
        CANAGE26_LIST.append(CANAGE26)
        CANAGE27_LIST.append(CANAGE27)
        CANAGE28_LIST.append(CANAGE28)
        CANAGE29_LIST.append(CANAGE29)
        CANAGE30_LIST.append(CANAGE30)
        DIBEV_LIST.append(DIBEV)
        DIBPRE1_LIST.append(DIBPRE1)
        DIBAGE_LIST.append(DIBAGE)
        DIFAGE2_LIST.append(DIFAGE2)
        INSLN_LIST.append(INSLN)
        DIBPILL_LIST.append(DIBPILL)
        AHAYFYR_LIST.append(AHAYFYR)
        SINYR_LIST.append(SINYR)
        CBRCHYR_LIST.append(CBRCHYR)
        KIDWKYR_LIST.append(KIDWKYR)
        LIVYR_LIST.append(LIVYR)
        JNTSYMP_LIST.append(JNTSYMP)
        JMTHP1_LIST.append(JMTHP1)
        JMTHP2_LIST.append(JMTHP2)
        JMTHP3_LIST.append(JMTHP3)
        JMTHP4_LIST.append(JMTHP4)
        JMTHP5_LIST.append(JMTHP5)
        JMTHP6_LIST.append(JMTHP6)
        JMTHP7_LIST.append(JMTHP7)
        JMTHP8_LIST.append(JMTHP8)
        JMTHP9_LIST.append(JMTHP9)
        JMTHP10_LIST.append(JMTHP10)
        JMTHP11_LIST.append(JMTHP11)
        JMTHP12_LIST.append(JMTHP12)
        JMTHP13_LIST.append(JMTHP13)
        JMTHP14_LIST.append(JMTHP14)
        JMTHP15_LIST.append(JMTHP15)
        JMTHP16_LIST.append(JMTHP16)
        JMTHP17_LIST.append(JMTHP17)
        JNTPN_LIST.append(JNTPN)
        JNTCHR_LIST.append(JNTCHR)
        JNTHP_LIST.append(JNTHP)
        ARTH1_LIST.append(ARTH1)
        ARTHWT_LIST.append(ARTHWT)
        ARTHPH_LIST.append(ARTHPH)
        ARTHCLS_LIST.append(ARTHCLS)
        ARTHLMT_LIST.append(ARTHLMT)
        ARTHWRK_LIST.append(ARTHWRK)
        PAINECK_LIST.append(PAINECK)
        PAINLB_LIST.append(PAINLB)
        PAINLEG_LIST.append(PAINLEG)
        PAINFACE_LIST.append(PAINFACE)
        AMIGR_LIST.append(AMIGR)
        ACOLD2W_LIST.append(ACOLD2W)
        AINTIL2W_LIST.append(AINTIL2W)
        PREGNOW_LIST.append(PREGNOW)
        PREGFLYR_LIST.append(PREGFLYR)
        AHEARST2_LIST.append(AHEARST2)
        HRWORS_LIST.append(HRWORS)
        HRWHICH_LIST.append(HRWHICH)
        HRRIGHT_LIST.append(HRRIGHT)
        HRLEFT_LIST.append(HRLEFT)
        HRWHISP1_LIST.append(HRWHISP1)
        HRTALK1_LIST.append(HRTALK1)
        HRSHOUT1_LIST.append(HRSHOUT1)
        HRSPEAK1_LIST.append(HRSPEAK1)
        HRCOCRE1_LIST.append(HRCOCRE1)
        HRCOCIM1_LIST.append(HRCOCIM1)
        HRFAM_LIST.append(HRFAM)
        HRBACK_LIST.append(HRBACK)
        HRFRUST_LIST.append(HRFRUST)
        HRSAFETY_LIST.append(HRSAFETY)
        HEARAGE1_LIST.append(HEARAGE1)
        HRCAUS1_LIST.append(HRCAUS1)
        HRPROBHP_LIST.append(HRPROBHP)
        HRENT_LIST.append(HRENT)
        HRAUD_LIST.append(HRAUD)
        HRTEST_LIST.append(HRTEST)
        HRAIDNOW_LIST.append(HRAIDNOW)
        HRAIDLNG_LIST.append(HRAIDLNG)
        HRAID2WK_LIST.append(HRAID2WK)
        HRAIDHLP_LIST.append(HRAIDHLP)
        HRAIDEV_LIST.append(HRAIDEV)
        HRAIDREC_LIST.append(HRAIDREC)
        HRAIDLGP_LIST.append(HRAIDLGP)
        HRAIDOF2_LIST.append(HRAIDOF2)
        HRAIDN01_LIST.append(HRAIDN01)
        HRAIDN02_LIST.append(HRAIDN02)
        HRAIDN03_LIST.append(HRAIDN03)
        HRAIDN04_LIST.append(HRAIDN04)
        HRAIDN05_LIST.append(HRAIDN05)
        HRAIDN06_LIST.append(HRAIDN06)
        HRAIDN07_LIST.append(HRAIDN07)
        HRAIDN08_LIST.append(HRAIDN08)
        HRAIDN09_LIST.append(HRAIDN09)
        HRAIDN10_LIST.append(HRAIDN10)
        HRAIDN11_LIST.append(HRAIDN11)
        HRAUDTRN_LIST.append(HRAUDTRN)
        HRALDS_LIST.append(HRALDS)
        HRALDT01_LIST.append(HRALDT01)
        HRALDT02_LIST.append(HRALDT02)
        HRALDT03_LIST.append(HRALDT03)
        HRALDT04_LIST.append(HRALDT04)
        HRALDT05_LIST.append(HRALDT05)
        HRALDT06_LIST.append(HRALDT06)
        HRALDT07_LIST.append(HRALDT07)
        HRALDT08_LIST.append(HRALDT08)
        HRALDT09_LIST.append(HRALDT09)
        HRALDT10_LIST.append(HRALDT10)
        HRALDT11_LIST.append(HRALDT11)
        HRBDIZZ_LIST.append(HRBDIZZ)
        HRTIN_LIST.append(HRTIN)
        HRTINOFT_LIST.append(HRTINOFT)
        HRTINLNG_LIST.append(HRTINLNG)
        HRTINMUS_LIST.append(HRTINMUS)
        HRTINSLP_LIST.append(HRTINSLP)
        HRTINPRO_LIST.append(HRTINPRO)
        HRTINDIS_LIST.append(HRTINDIS)
        HRTINDOC_LIST.append(HRTINDOC)
        HRTINRM_LIST.append(HRTINRM)
        HREMTY01_LIST.append(HREMTY01)
        HREMTY02_LIST.append(HREMTY02)
        HREMTY03_LIST.append(HREMTY03)
        HREMTY04_LIST.append(HREMTY04)
        HREMTY05_LIST.append(HREMTY05)
        HREMTY06_LIST.append(HREMTY06)
        HREMTY07_LIST.append(HREMTY07)
        HREMTY08_LIST.append(HREMTY08)
        HREMTY09_LIST.append(HREMTY09)
        HREMTY10_LIST.append(HREMTY10)
        HREMTY11_LIST.append(HREMTY11)
        HREMTY12_LIST.append(HREMTY12)
        HRTNRMHP_LIST.append(HRTNRMHP)
        HRHCUSIS_LIST.append(HRHCUSIS)
        HRHCPROB_LIST.append(HRHCPROB)
        HRFIRE_LIST.append(HRFIRE)
        HRFIRTYP_LIST.append(HRFIRTYP)
        HRFRTIM_LIST.append(HRFRTIM)
        HR12MR_LIST.append(HR12MR)
        HRFRPROT_LIST.append(HRFRPROT)
        HRTOTR_LIST.append(HRTOTR)
        HRFRPRT2_LIST.append(HRFRPRT2)
        HRWKVLNS_LIST.append(HRWKVLNS)
        HRWKLNS_LIST.append(HRWKLNS)
        HRWKVLNT_LIST.append(HRWKVLNT)
        HRWKVLEX_LIST.append(HRWKVLEX)
        HRWKVLP1_LIST.append(HRWKVLP1)
        HRWKVLP2_LIST.append(HRWKVLP2)
        HRWRLNS_LIST.append(HRWRLNS)
        HRWKLEX_LIST.append(HRWKLEX)
        HRWKLP1_LIST.append(HRWKLP1)
        HRWKLP2_LIST.append(HRWKLP2)
        HRLSVLNS_LIST.append(HRLSVLNS)
        HRVLTP01_LIST.append(HRVLTP01)
        HRVLTP02_LIST.append(HRVLTP02)
        HRVLTP03_LIST.append(HRVLTP03)
        HRVLTP04_LIST.append(HRVLTP04)
        HRVLTP05_LIST.append(HRVLTP05)
        HRVLTP06_LIST.append(HRVLTP06)
        HRVLTP07_LIST.append(HRVLTP07)
        HRVLTP08_LIST.append(HRVLTP08)
        HRVLTP09_LIST.append(HRVLTP09)
        HRVLTP10_LIST.append(HRVLTP10)
        HRLNOS_LIST.append(HRLNOS)
        HRLTP01_LIST.append(HRLTP01)
        HRLTP02_LIST.append(HRLTP02)
        HRLTP03_LIST.append(HRLTP03)
        HRLTP04_LIST.append(HRLTP04)
        HRLTP05_LIST.append(HRLTP05)
        HRLTP06_LIST.append(HRLTP06)
        HRLTP07_LIST.append(HRLTP07)
        HRLTP08_LIST.append(HRLTP08)
        HRLTP09_LIST.append(HRLTP09)
        HRLTP10_LIST.append(HRLTP10)
        HRNOSEXP_LIST.append(HRNOSEXP)
        HRLSP1_LIST.append(HRLSP1)
        HRLSP2_LIST.append(HRLSP2)
        HRINTNET_LIST.append(HRINTNET)
        HRINTHL_LIST.append(HRINTHL)
        HRINTHA_LIST.append(HRINTHA)
        HRINTTN_LIST.append(HRINTTN)
        HRINTDZ_LIST.append(HRINTDZ)
        HRINTHP_LIST.append(HRINTHP)
        HRINTHPR_LIST.append(HRINTHPR)
        AVISION_LIST.append(AVISION)
        ABLIND_LIST.append(ABLIND)
        LUPPRT_LIST.append(LUPPRT)
        WKDAYR_LIST.append(WKDAYR)
        BEDDAYR_LIST.append(BEDDAYR)
        AHSTATYR_LIST.append(AHSTATYR)
        SPECEQ_LIST.append(SPECEQ)
        FLWALK_LIST.append(FLWALK)
        FLCLIMB_LIST.append(FLCLIMB)
        FLSTAND_LIST.append(FLSTAND)
        FLSIT_LIST.append(FLSIT)
        FLSTOOP_LIST.append(FLSTOOP)
        FLREACH_LIST.append(FLREACH)
        FLGRASP_LIST.append(FLGRASP)
        FLCARRY_LIST.append(FLCARRY)
        FLPUSH_LIST.append(FLPUSH)
        FLSHOP_LIST.append(FLSHOP)
        FLSOCL_LIST.append(FLSOCL)
        FLRELAX_LIST.append(FLRELAX)
        FLA1AR_LIST.append(FLA1AR)
        AFLHCA1_LIST.append(AFLHCA1)
        AFLHCA2_LIST.append(AFLHCA2)
        AFLHCA3_LIST.append(AFLHCA3)
        AFLHCA4_LIST.append(AFLHCA4)
        AFLHCA5_LIST.append(AFLHCA5)
        AFLHCA6_LIST.append(AFLHCA6)
        AFLHCA7_LIST.append(AFLHCA7)
        AFLHCA8_LIST.append(AFLHCA8)
        AFLHCA9_LIST.append(AFLHCA9)
        AFLHCA10_LIST.append(AFLHCA10)
        AFLHCA11_LIST.append(AFLHCA11)
        AFLHCA12_LIST.append(AFLHCA12)
        AFLHCA13_LIST.append(AFLHCA13)
        ALHCA14A_LIST.append(ALHCA14A)
        AFLHCA15_LIST.append(AFLHCA15)
        AFLHCA16_LIST.append(AFLHCA16)
        AFLHCA17_LIST.append(AFLHCA17)
        AFLHCA18_LIST.append(AFLHCA18)
        AFLHC19__LIST.append(AFLHC19_)
        AFLHC20__LIST.append(AFLHC20_)
        AFLHC21__LIST.append(AFLHC21_)
        AFLHC22__LIST.append(AFLHC22_)
        AFLHC23__LIST.append(AFLHC23_)
        AFLHC24__LIST.append(AFLHC24_)
        AFLHC25__LIST.append(AFLHC25_)
        AFLHC26__LIST.append(AFLHC26_)
        AFLHC27__LIST.append(AFLHC27_)
        AFLHC28__LIST.append(AFLHC28_)
        AFLHC29__LIST.append(AFLHC29_)
        AFLHC30__LIST.append(AFLHC30_)
        AFLHC31__LIST.append(AFLHC31_)
        AFLHC32__LIST.append(AFLHC32_)
        AFLHC33__LIST.append(AFLHC33_)
        AFLHC34__LIST.append(AFLHC34_)
        AFLHCA90_LIST.append(AFLHCA90)
        AFLHCA91_LIST.append(AFLHCA91)
        ALTIME1_LIST.append(ALTIME1)
        ALUNIT1_LIST.append(ALUNIT1)
        ALDURA1_LIST.append(ALDURA1)
        ALDURB1_LIST.append(ALDURB1)
        ALCHRC1_LIST.append(ALCHRC1)
        ALTIME2_LIST.append(ALTIME2)
        ALUNIT2_LIST.append(ALUNIT2)
        ALDURA2_LIST.append(ALDURA2)
        ALDURB2_LIST.append(ALDURB2)
        ALCHRC2_LIST.append(ALCHRC2)
        ALTIME3_LIST.append(ALTIME3)
        ALUNIT3_LIST.append(ALUNIT3)
        ALDURA3_LIST.append(ALDURA3)
        ALDURB3_LIST.append(ALDURB3)
        ALCHRC3_LIST.append(ALCHRC3)
        ALTIME4_LIST.append(ALTIME4)
        ALUNIT4_LIST.append(ALUNIT4)
        ALDURA4_LIST.append(ALDURA4)
        ALDURB4_LIST.append(ALDURB4)
        ALCHRC4_LIST.append(ALCHRC4)
        ALTIME5_LIST.append(ALTIME5)
        ALUNIT5_LIST.append(ALUNIT5)
        ALDURA5_LIST.append(ALDURA5)
        ALDURB5_LIST.append(ALDURB5)
        ALCHRC5_LIST.append(ALCHRC5)
        ALTIME6_LIST.append(ALTIME6)
        ALUNIT6_LIST.append(ALUNIT6)
        ALDURA6_LIST.append(ALDURA6)
        ALDURB6_LIST.append(ALDURB6)
        ALCHRC6_LIST.append(ALCHRC6)
        ALTIME7_LIST.append(ALTIME7)
        ALUNIT7_LIST.append(ALUNIT7)
        ALDURA7_LIST.append(ALDURA7)
        ALDURB7_LIST.append(ALDURB7)
        ALCHRC7_LIST.append(ALCHRC7)
        ALTIME8_LIST.append(ALTIME8)
        ALUNIT8_LIST.append(ALUNIT8)
        ALDURA8_LIST.append(ALDURA8)
        ALDURB8_LIST.append(ALDURB8)
        ALCHRC8_LIST.append(ALCHRC8)
        ALTIME9_LIST.append(ALTIME9)
        ALUNIT9_LIST.append(ALUNIT9)
        ALDURA9_LIST.append(ALDURA9)
        ALDURB9_LIST.append(ALDURB9)
        ALCHRC9_LIST.append(ALCHRC9)
        ALTIME10_LIST.append(ALTIME10)
        ALUNIT10_LIST.append(ALUNIT10)
        ALDURA10_LIST.append(ALDURA10)
        ALDURB10_LIST.append(ALDURB10)
        ALCHRC10_LIST.append(ALCHRC10)
        ALTIME11_LIST.append(ALTIME11)
        ALUNIT11_LIST.append(ALUNIT11)
        ALDURA11_LIST.append(ALDURA11)
        ALDURB11_LIST.append(ALDURB11)
        ALCHRC11_LIST.append(ALCHRC11)
        ALTIME12_LIST.append(ALTIME12)
        ALUNIT12_LIST.append(ALUNIT12)
        ALDURA12_LIST.append(ALDURA12)
        ALDURB12_LIST.append(ALDURB12)
        ALCHRC12_LIST.append(ALCHRC12)
        ALTIME13_LIST.append(ALTIME13)
        ALUNIT13_LIST.append(ALUNIT13)
        ALDURA13_LIST.append(ALDURA13)
        ALDURB13_LIST.append(ALDURB13)
        ALCHRC13_LIST.append(ALCHRC13)
        ATIME14A_LIST.append(ATIME14A)
        AUNIT14A_LIST.append(AUNIT14A)
        ADURA14A_LIST.append(ADURA14A)
        ADURB14A_LIST.append(ADURB14A)
        ACHRC14A_LIST.append(ACHRC14A)
        ALTIME15_LIST.append(ALTIME15)
        ALUNIT15_LIST.append(ALUNIT15)
        ALDURA15_LIST.append(ALDURA15)
        ALDURB15_LIST.append(ALDURB15)
        ALCHRC15_LIST.append(ALCHRC15)
        ALTIME16_LIST.append(ALTIME16)
        ALUNIT16_LIST.append(ALUNIT16)
        ALDURA16_LIST.append(ALDURA16)
        ALDURB16_LIST.append(ALDURB16)
        ALCHRC16_LIST.append(ALCHRC16)
        ALTIME17_LIST.append(ALTIME17)
        ALUNIT17_LIST.append(ALUNIT17)
        ALDURA17_LIST.append(ALDURA17)
        ALDURB17_LIST.append(ALDURB17)
        ALCHRC17_LIST.append(ALCHRC17)
        ALTIME18_LIST.append(ALTIME18)
        ALUNIT18_LIST.append(ALUNIT18)
        ALDURA18_LIST.append(ALDURA18)
        ALDURB18_LIST.append(ALDURB18)
        ALCHRC18_LIST.append(ALCHRC18)
        ALTIME19_LIST.append(ALTIME19)
        ALUNIT19_LIST.append(ALUNIT19)
        ALDURA19_LIST.append(ALDURA19)
        ALDURB19_LIST.append(ALDURB19)
        ALCHRC19_LIST.append(ALCHRC19)
        ALTIME20_LIST.append(ALTIME20)
        ALUNIT20_LIST.append(ALUNIT20)
        ALDURA20_LIST.append(ALDURA20)
        ALDURB20_LIST.append(ALDURB20)
        ALCHRC20_LIST.append(ALCHRC20)
        ALTIME21_LIST.append(ALTIME21)
        ALUNIT21_LIST.append(ALUNIT21)
        ALDURA21_LIST.append(ALDURA21)
        ALDURB21_LIST.append(ALDURB21)
        ALCHRC21_LIST.append(ALCHRC21)
        ALTIME22_LIST.append(ALTIME22)
        ALUNIT22_LIST.append(ALUNIT22)
        ALDURA22_LIST.append(ALDURA22)
        ALDURB22_LIST.append(ALDURB22)
        ALCHRC22_LIST.append(ALCHRC22)
        ALTIME23_LIST.append(ALTIME23)
        ALUNIT23_LIST.append(ALUNIT23)
        ALDURA23_LIST.append(ALDURA23)
        ALDURB23_LIST.append(ALDURB23)
        ALCHRC23_LIST.append(ALCHRC23)
        ALTIME24_LIST.append(ALTIME24)
        ALUNIT24_LIST.append(ALUNIT24)
        ALDURA24_LIST.append(ALDURA24)
        ALDURB24_LIST.append(ALDURB24)
        ALCHRC24_LIST.append(ALCHRC24)
        ALTIME25_LIST.append(ALTIME25)
        ALUNIT25_LIST.append(ALUNIT25)
        ALDURA25_LIST.append(ALDURA25)
        ALDURB25_LIST.append(ALDURB25)
        ALCHRC25_LIST.append(ALCHRC25)
        ALTIME26_LIST.append(ALTIME26)
        ALUNIT26_LIST.append(ALUNIT26)
        ALDURA26_LIST.append(ALDURA26)
        ALDURB26_LIST.append(ALDURB26)
        ALCHRC26_LIST.append(ALCHRC26)
        ALTIME27_LIST.append(ALTIME27)
        ALUNIT27_LIST.append(ALUNIT27)
        ALDURA27_LIST.append(ALDURA27)
        ALDURB27_LIST.append(ALDURB27)
        ALCHRC27_LIST.append(ALCHRC27)
        ALTIME28_LIST.append(ALTIME28)
        ALUNIT28_LIST.append(ALUNIT28)
        ALDURA28_LIST.append(ALDURA28)
        ALDURB28_LIST.append(ALDURB28)
        ALCHRC28_LIST.append(ALCHRC28)
        ALTIME29_LIST.append(ALTIME29)
        ALUNIT29_LIST.append(ALUNIT29)
        ALDURA29_LIST.append(ALDURA29)
        ALDURB29_LIST.append(ALDURB29)
        ALCHRC29_LIST.append(ALCHRC29)
        ALTIME30_LIST.append(ALTIME30)
        ALUNIT30_LIST.append(ALUNIT30)
        ALDURA30_LIST.append(ALDURA30)
        ALDURB30_LIST.append(ALDURB30)
        ALCHRC30_LIST.append(ALCHRC30)
        ALTIME31_LIST.append(ALTIME31)
        ALUNIT31_LIST.append(ALUNIT31)
        ALDURA31_LIST.append(ALDURA31)
        ALDURB31_LIST.append(ALDURB31)
        ALCHRC31_LIST.append(ALCHRC31)
        ALTIME32_LIST.append(ALTIME32)
        ALUNIT32_LIST.append(ALUNIT32)
        ALDURA32_LIST.append(ALDURA32)
        ALDURB32_LIST.append(ALDURB32)
        ALCHRC32_LIST.append(ALCHRC32)
        ALTIME33_LIST.append(ALTIME33)
        ALUNIT33_LIST.append(ALUNIT33)
        ALDURA33_LIST.append(ALDURA33)
        ALDURB33_LIST.append(ALDURB33)
        ALCHRC33_LIST.append(ALCHRC33)
        ALTIME34_LIST.append(ALTIME34)
        ALUNIT34_LIST.append(ALUNIT34)
        ALDURA34_LIST.append(ALDURA34)
        ALDURB34_LIST.append(ALDURB34)
        ALCHRC34_LIST.append(ALCHRC34)
        ALTIME90_LIST.append(ALTIME90)
        ALUNIT90_LIST.append(ALUNIT90)
        ALDURA90_LIST.append(ALDURA90)
        ALDURB90_LIST.append(ALDURB90)
        ALCHRC90_LIST.append(ALCHRC90)
        ALTIME91_LIST.append(ALTIME91)
        ALUNIT91_LIST.append(ALUNIT91)
        ALDURA91_LIST.append(ALDURA91)
        ALDURB91_LIST.append(ALDURB91)
        ALCHRC91_LIST.append(ALCHRC91)
        ALCNDRT_LIST.append(ALCNDRT)
        ALCHRONR_LIST.append(ALCHRONR)
        SMKEV_LIST.append(SMKEV)
        SMKREG_LIST.append(SMKREG)
        SMKNOW_LIST.append(SMKNOW)
        SMKSTAT2_LIST.append(SMKSTAT2)
        SMKQTNO_LIST.append(SMKQTNO)
        SMKQTTP_LIST.append(SMKQTTP)
        SMKQTY_LIST.append(SMKQTY)
        CIGSDA1_LIST.append(CIGSDA1)
        CIGDAMO_LIST.append(CIGDAMO)
        CIGSDA2_LIST.append(CIGSDA2)
        CIGSDAY_LIST.append(CIGSDAY)
        CIGQTYR_LIST.append(CIGQTYR)
        OTHCIGEV_LIST.append(OTHCIGEV)
        OTHCIGED_LIST.append(OTHCIGED)
        SMKLESEV_LIST.append(SMKLESEV)
        SMKLESED_LIST.append(SMKLESED)
        TOBLASYR_LIST.append(TOBLASYR)
        TOBQTYR_LIST.append(TOBQTYR)
        ECIGEV_LIST.append(ECIGEV)
        ECIGED_LIST.append(ECIGED)
        VIGNO_LIST.append(VIGNO)
        VIGTP_LIST.append(VIGTP)
        VIGFREQW_LIST.append(VIGFREQW)
        VIGLNGNO_LIST.append(VIGLNGNO)
        VIGLNGTP_LIST.append(VIGLNGTP)
        VIGMIN_LIST.append(VIGMIN)
        MODNO_LIST.append(MODNO)
        MODTP_LIST.append(MODTP)
        MODFREQW_LIST.append(MODFREQW)
        MODLNGNO_LIST.append(MODLNGNO)
        MODLNGTP_LIST.append(MODLNGTP)
        MODMIN_LIST.append(MODMIN)
        STRNGNO_LIST.append(STRNGNO)
        STRNGTP_LIST.append(STRNGTP)
        STRFREQW_LIST.append(STRFREQW)
        ALC1YR_LIST.append(ALC1YR)
        ALCLIFE_LIST.append(ALCLIFE)
        ALC12MNO_LIST.append(ALC12MNO)
        ALC12MTP_LIST.append(ALC12MTP)
        ALC12MWK_LIST.append(ALC12MWK)
        ALC12MYR_LIST.append(ALC12MYR)
        ALCAMT_LIST.append(ALCAMT)
        ALCSTAT_LIST.append(ALCSTAT)
        ALC5UPN1_LIST.append(ALC5UPN1)
        ALC5UPT1_LIST.append(ALC5UPT1)
        ALC5UPY1_LIST.append(ALC5UPY1)
        AHEIGHT_LIST.append(AHEIGHT)
        AWEIGHTP_LIST.append(AWEIGHTP)
        BMI_LIST.append(BMI)
        AUSUALPL_LIST.append(AUSUALPL)
        APLKIND_LIST.append(APLKIND)
        AHCPLROU_LIST.append(AHCPLROU)
        AHCPLKND_LIST.append(AHCPLKND)
        AHCCHGYR_LIST.append(AHCCHGYR)
        AHCCHGHI_LIST.append(AHCCHGHI)
        ANOUSPL1_LIST.append(ANOUSPL1)
        ANOUSPL2_LIST.append(ANOUSPL2)
        ANOUSPL3_LIST.append(ANOUSPL3)
        ANOUSPL4_LIST.append(ANOUSPL4)
        ANOUSPL5_LIST.append(ANOUSPL5)
        ANOUSPL6_LIST.append(ANOUSPL6)
        ANOUSPL7_LIST.append(ANOUSPL7)
        ANOUSPL8_LIST.append(ANOUSPL8)
        ANOUSPL9_LIST.append(ANOUSPL9)
        APRVTRYR_LIST.append(APRVTRYR)
        APRVTRFD_LIST.append(APRVTRFD)
        ADRNANP_LIST.append(ADRNANP)
        ADRNAI_LIST.append(ADRNAI)
        AHCDLYR1_LIST.append(AHCDLYR1)
        AHCDLYR2_LIST.append(AHCDLYR2)
        AHCDLYR3_LIST.append(AHCDLYR3)
        AHCDLYR4_LIST.append(AHCDLYR4)
        AHCDLYR5_LIST.append(AHCDLYR5)
        AHCAFYR1_LIST.append(AHCAFYR1)
        AHCAFYR2_LIST.append(AHCAFYR2)
        AHCAFYR3_LIST.append(AHCAFYR3)
        AHCAFYR4_LIST.append(AHCAFYR4)
        AHCAFYR5_LIST.append(AHCAFYR5)
        AHCAFYR6_LIST.append(AHCAFYR6)
        AWORPAY_LIST.append(AWORPAY)
        AHICOMP_LIST.append(AHICOMP)
        ARX12MO_LIST.append(ARX12MO)
        ARX12_1_LIST.append(ARX12_1)
        ARX12_2_LIST.append(ARX12_2)
        ARX12_3_LIST.append(ARX12_3)
        ARX12_4_LIST.append(ARX12_4)
        ARX12_5_LIST.append(ARX12_5)
        ARX12_6_LIST.append(ARX12_6)
        ADNLONG2_LIST.append(ADNLONG2)
        AHCSYR1_LIST.append(AHCSYR1)
        AHCSYR2_LIST.append(AHCSYR2)
        AHCSYR3_LIST.append(AHCSYR3)
        AHCSYR4_LIST.append(AHCSYR4)
        AHCSYR5_LIST.append(AHCSYR5)
        AHCSYR6_LIST.append(AHCSYR6)
        AHCSYR7_LIST.append(AHCSYR7)
        AHCSYR8_LIST.append(AHCSYR8)
        AHCSYR9_LIST.append(AHCSYR9)
        AHCSYR10_LIST.append(AHCSYR10)
        AHERNOY2_LIST.append(AHERNOY2)
        AERVISND_LIST.append(AERVISND)
        AERHOS_LIST.append(AERHOS)
        AERREA1R_LIST.append(AERREA1R)
        AERREA2R_LIST.append(AERREA2R)
        AERREA3R_LIST.append(AERREA3R)
        AERREA4R_LIST.append(AERREA4R)
        AERREA5R_LIST.append(AERREA5R)
        AERREA6R_LIST.append(AERREA6R)
        AERREA7R_LIST.append(AERREA7R)
        AERREA8R_LIST.append(AERREA8R)
        AHCHYR_LIST.append(AHCHYR)
        AHCHMOYR_LIST.append(AHCHMOYR)
        AHCHNOY2_LIST.append(AHCHNOY2)
        AHCNOYR2_LIST.append(AHCNOYR2)
        ASRGYR_LIST.append(ASRGYR)
        ASRGNOYR_LIST.append(ASRGNOYR)
        AMDLONGR_LIST.append(AMDLONGR)
        AVISLAST_LIST.append(AVISLAST)
        ALASTYP1_LIST.append(ALASTYP1)
        ALASTYP2_LIST.append(ALASTYP2)
        ALASTYP3_LIST.append(ALASTYP3)
        ALASTYP4_LIST.append(ALASTYP4)
        ALASTVRB_LIST.append(ALASTVRB)
        AVISAPN2_LIST.append(AVISAPN2)
        AVISAPT2_LIST.append(AVISAPT2)
        AWAITRMN_LIST.append(AWAITRMN)
        AWAITRMT_LIST.append(AWAITRMT)
        HIT1A_LIST.append(HIT1A)
        HIT2A_LIST.append(HIT2A)
        HIT3A_LIST.append(HIT3A)
        HIT4A_LIST.append(HIT4A)
        HIT5A_LIST.append(HIT5A)
        SHTFLU2_LIST.append(SHTFLU2)
        ASHFLUM2_LIST.append(ASHFLUM2)
        ASHFLUY2_LIST.append(ASHFLUY2)
        FLUSHPG1_LIST.append(FLUSHPG1)
        FLUSHPG2_LIST.append(FLUSHPG2)
        SPRFLU2_LIST.append(SPRFLU2)
        ASPFLUM2_LIST.append(ASPFLUM2)
        ASPFLUY2_LIST.append(ASPFLUY2)
        SHTPNUYR_LIST.append(SHTPNUYR)
        APOX_LIST.append(APOX)
        APOX12MO_LIST.append(APOX12MO)
        AHEP_LIST.append(AHEP)
        AHEPLIV_LIST.append(AHEPLIV)
        AHEPBTST_LIST.append(AHEPBTST)
        SHTHEPB_LIST.append(SHTHEPB)
        SHEPDOS_LIST.append(SHEPDOS)
        SHTHEPA_LIST.append(SHTHEPA)
        SHEPANUM_LIST.append(SHEPANUM)
        AHEPCTST_LIST.append(AHEPCTST)
        AHEPCRES_LIST.append(AHEPCRES)
        SHINGLES_LIST.append(SHINGLES)
        SHTTD_LIST.append(SHTTD)
        SHTTD05_LIST.append(SHTTD05)
        SHTTDAP2_LIST.append(SHTTDAP2)
        SHTHPV2_LIST.append(SHTHPV2)
        SHHPVDOS_LIST.append(SHHPVDOS)
        AHPVAGE_LIST.append(AHPVAGE)
        LIVEV_LIST.append(LIVEV)
        TRAVEL_LIST.append(TRAVEL)
        WRKHLTH2_LIST.append(WRKHLTH2)
        WRKDIR_LIST.append(WRKDIR)
        APSBPCH1_LIST.append(APSBPCH1)
        APSCHCH1_LIST.append(APSCHCH1)
        APSBSCH1_LIST.append(APSBSCH1)
        APSPAP_LIST.append(APSPAP)
        APSMAM_LIST.append(APSMAM)
        APSCOL_LIST.append(APSCOL)
        APSDIET_LIST.append(APSDIET)
        APSSMKC_LIST.append(APSSMKC)
        LTCFAM_LIST.append(LTCFAM)
        LTCHELP_LIST.append(LTCHELP)
        LTCWHO1_LIST.append(LTCWHO1)
        LTCWHO2_LIST.append(LTCWHO2)
        LTCWHO3_LIST.append(LTCWHO3)
        LTCWHO4_LIST.append(LTCWHO4)
        LTCWHO5_LIST.append(LTCWHO5)
        AINDINS_LIST.append(AINDINS)
        AINDPRCH_LIST.append(AINDPRCH)
        AINDWHO_LIST.append(AINDWHO)
        AINDDIF1_LIST.append(AINDDIF1)
        AINDDIF2_LIST.append(AINDDIF2)
        AINDENY1_LIST.append(AINDENY1)
        AINDENY2_LIST.append(AINDENY2)
        AINDENY3_LIST.append(AINDENY3)
        AINDNOT1_LIST.append(AINDNOT1)
        AINDNOT2_LIST.append(AINDNOT2)
        AINDNOT3_LIST.append(AINDNOT3)
        AINDNOT4_LIST.append(AINDNOT4)
        AINDNOT5_LIST.append(AINDNOT5)
        AEXCHNG_LIST.append(AEXCHNG)
        ASICPUSE_LIST.append(ASICPUSE)
        ASISATHC_LIST.append(ASISATHC)
        ASITENUR_LIST.append(ASITENUR)
        ASINHELP_LIST.append(ASINHELP)
        ASINCNTO_LIST.append(ASINCNTO)
        ASINTRU_LIST.append(ASINTRU)
        ASINKNT_LIST.append(ASINKNT)
        ASISIM_LIST.append(ASISIM)
        ASISIF_LIST.append(ASISIF)
        ASIRETR_LIST.append(ASIRETR)
        ASIMEDC_LIST.append(ASIMEDC)
        ASISTLV_LIST.append(ASISTLV)
        ASICNHC_LIST.append(ASICNHC)
        ASICCOLL_LIST.append(ASICCOLL)
        ASINBILL_LIST.append(ASINBILL)
        ASIHCST_LIST.append(ASIHCST)
        ASICCMP_LIST.append(ASICCMP)
        ASISLEEP_LIST.append(ASISLEEP)
        ASISLPFL_LIST.append(ASISLPFL)
        ASISLPST_LIST.append(ASISLPST)
        ASISLPMD_LIST.append(ASISLPMD)
        ASIREST_LIST.append(ASIREST)
        ASISAD_LIST.append(ASISAD)
        ASINERV_LIST.append(ASINERV)
        ASIRSTLS_LIST.append(ASIRSTLS)
        ASIHOPLS_LIST.append(ASIHOPLS)
        ASIEFFRT_LIST.append(ASIEFFRT)
        ASIWTHLS_LIST.append(ASIWTHLS)
        ASIMUCH_LIST.append(ASIMUCH)
        ASIHIVT_LIST.append(ASIHIVT)
        ASIHIVWN_LIST.append(ASIHIVWN)
        AWEBUSE_LIST.append(AWEBUSE)
        AWEBOFNO_LIST.append(AWEBOFNO)
        AWEBOFTP_LIST.append(AWEBOFTP)
        AWEBORP_LIST.append(AWEBORP)
        AWEBEML_LIST.append(AWEBEML)
        AWEBMNO_LIST.append(AWEBMNO)
        AWEBMTP_LIST.append(AWEBMTP)

df = pd.DataFrame(columns=(
                            'RECTYPE',
                            'SRVY_YR',
                            'HHX',
                            'INTV_QRT',
                            'INTV_MON',
                            'FMX',
                            'FPX',
                            'WTIA_SA',
                            'WTFA_SA',
                            'REGION',
                            'STRAT_P',
                            'PSU_P',
                            'SEX',
                            'HISPAN_I',
                            'RACERPI2',
                            'MRACRPI2',
                            'MRACBPI2',
                            'AGE_P',
                            'R_MARITL',
                            'PROXYSA',
                            'PROX1',
                            'PROX2',
                            'LATEINTA',
                            'FDRN_FLG',
                            'DOINGLWA',
                            'WHYNOWKA',
                            'EVERWRK',
                            'INDSTRN1',
                            'INDSTRN2',
                            'OCCUPN1',
                            'OCCUPN2',
                            'WRKCATA',
                            'BUSINC1A',
                            'LOCALL1A',
                            'YRSWRKPA',
                            'WRKLONGH',
                            'HOURPDA',
                            'PDSICKA',
                            'ONEJOB',
                            'WRKLYR4',
                            'HYPEV',
                            'HYPDIFV',
                            'HYPYR1',
                            'HYBPCKNO',
                            'HYBPCKTP',
                            'HYBPLEV',
                            'HYPMDEV2',
                            'HYPMED2',
                            'CHLEV',
                            'CHLYR',
                            'CLCKNO',
                            'CLCKTP',
                            'CHLMDEV2',
                            'CHLMDNW2',
                            'CHDEV',
                            'ANGEV',
                            'MIEV',
                            'HRTEV',
                            'STREV',
                            'EPHEV',
                            'JAWP',
                            'WEA',
                            'CHE',
                            'ARM',
                            'BRTH',
                            'AHADO',
                            'FACE',
                            'SPEAKING',
                            'EYE',
                            'WALKING',
                            'HEADACHE',
                            'ASTDO',
                            'COPDEV',
                            'ASPMEDEV',
                            'ASPMEDAD',
                            'ASPMDMED',
                            'ASPONOWN',
                            'AASMEV',
                            'AASSTILL',
                            'AASMYR',
                            'AASERYR1',
                            'ULCEV',
                            'ULCYR',
                            'CANEV',
                            'CNKIND1',
                            'CNKIND2',
                            'CNKIND3',
                            'CNKIND4',
                            'CNKIND5',
                            'CNKIND6',
                            'CNKIND7',
                            'CNKIND8',
                            'CNKIND9',
                            'CNKIND10',
                            'CNKIND11',
                            'CNKIND12',
                            'CNKIND13',
                            'CNKIND14',
                            'CNKIND15',
                            'CNKIND16',
                            'CNKIND17',
                            'CNKIND18',
                            'CNKIND19',
                            'CNKIND20',
                            'CNKIND21',
                            'CNKIND22',
                            'CNKIND23',
                            'CNKIND24',
                            'CNKIND25',
                            'CNKIND26',
                            'CNKIND27',
                            'CNKIND28',
                            'CNKIND29',
                            'CNKIND30',
                            'CNKIND31',
                            'CANAGE1',
                            'CANAGE2',
                            'CANAGE3',
                            'CANAGE4',
                            'CANAGE5',
                            'CANAGE6',
                            'CANAGE7',
                            'CANAGE8',
                            'CANAGE9',
                            'CANAGE10',
                            'CANAGE11',
                            'CANAGE12',
                            'CANAGE13',
                            'CANAGE14',
                            'CANAGE15',
                            'CANAGE16',
                            'CANAGE17',
                            'CANAGE18',
                            'CANAGE19',
                            'CANAGE20',
                            'CANAGE21',
                            'CANAGE22',
                            'CANAGE23',
                            'CANAGE24',
                            'CANAGE25',
                            'CANAGE26',
                            'CANAGE27',
                            'CANAGE28',
                            'CANAGE29',
                            'CANAGE30',
                            'DIBEV',
                            'DIBPRE1',
                            'DIBAGE',
                            'DIFAGE2',
                            'INSLN',
                            'DIBPILL',
                            'AHAYFYR',
                            'SINYR',
                            'CBRCHYR',
                            'KIDWKYR',
                            'LIVYR',
                            'JNTSYMP',
                            'JMTHP1',
                            'JMTHP2',
                            'JMTHP3',
                            'JMTHP4',
                            'JMTHP5',
                            'JMTHP6',
                            'JMTHP7',
                            'JMTHP8',
                            'JMTHP9',
                            'JMTHP10',
                            'JMTHP11',
                            'JMTHP12',
                            'JMTHP13',
                            'JMTHP14',
                            'JMTHP15',
                            'JMTHP16',
                            'JMTHP17',
                            'JNTPN',
                            'JNTCHR',
                            'JNTHP',
                            'ARTH1',
                            'ARTHWT',
                            'ARTHPH',
                            'ARTHCLS',
                            'ARTHLMT',
                            'ARTHWRK',
                            'PAINECK',
                            'PAINLB',
                            'PAINLEG',
                            'PAINFACE',
                            'AMIGR',
                            'ACOLD2W',
                            'AINTIL2W',
                            'PREGNOW',
                            'PREGFLYR',
                            'AHEARST2',
                            'HRWORS',
                            'HRWHICH',
                            'HRRIGHT',
                            'HRLEFT',
                            'HRWHISP1',
                            'HRTALK1',
                            'HRSHOUT1',
                            'HRSPEAK1',
                            'HRCOCRE1',
                            'HRCOCIM1',
                            'HRFAM',
                            'HRBACK',
                            'HRFRUST',
                            'HRSAFETY',
                            'HEARAGE1',
                            'HRCAUS1',
                            'HRPROBHP',
                            'HRENT',
                            'HRAUD',
                            'HRTEST',
                            'HRAIDNOW',
                            'HRAIDLNG',
                            'HRAID2WK',
                            'HRAIDHLP',
                            'HRAIDEV',
                            'HRAIDREC',
                            'HRAIDLGP',
                            'HRAIDOF2',
                            'HRAIDN01',
                            'HRAIDN02',
                            'HRAIDN03',
                            'HRAIDN04',
                            'HRAIDN05',
                            'HRAIDN06',
                            'HRAIDN07',
                            'HRAIDN08',
                            'HRAIDN09',
                            'HRAIDN10',
                            'HRAIDN11',
                            'HRAUDTRN',
                            'HRALDS',
                            'HRALDT01',
                            'HRALDT02',
                            'HRALDT03',
                            'HRALDT04',
                            'HRALDT05',
                            'HRALDT06',
                            'HRALDT07',
                            'HRALDT08',
                            'HRALDT09',
                            'HRALDT10',
                            'HRALDT11',
                            'HRBDIZZ',
                            'HRTIN',
                            'HRTINOFT',
                            'HRTINLNG',
                            'HRTINMUS',
                            'HRTINSLP',
                            'HRTINPRO',
                            'HRTINDIS',
                            'HRTINDOC',
                            'HRTINRM',
                            'HREMTY01',
                            'HREMTY02',
                            'HREMTY03',
                            'HREMTY04',
                            'HREMTY05',
                            'HREMTY06',
                            'HREMTY07',
                            'HREMTY08',
                            'HREMTY09',
                            'HREMTY10',
                            'HREMTY11',
                            'HREMTY12',
                            'HRTNRMHP',
                            'HRHCUSIS',
                            'HRHCPROB',
                            'HRFIRE',
                            'HRFIRTYP',
                            'HRFRTIM',
                            'HR12MR',
                            'HRFRPROT',
                            'HRTOTR',
                            'HRFRPRT2',
                            'HRWKVLNS',
                            'HRWKLNS',
                            'HRWKVLNT',
                            'HRWKVLEX',
                            'HRWKVLP1',
                            'HRWKVLP2',
                            'HRWRLNS',
                            'HRWKLEX',
                            'HRWKLP1',
                            'HRWKLP2',
                            'HRLSVLNS',
                            'HRVLTP01',
                            'HRVLTP02',
                            'HRVLTP03',
                            'HRVLTP04',
                            'HRVLTP05',
                            'HRVLTP06',
                            'HRVLTP07',
                            'HRVLTP08',
                            'HRVLTP09',
                            'HRVLTP10',
                            'HRLNOS',
                            'HRLTP01',
                            'HRLTP02',
                            'HRLTP03',
                            'HRLTP04',
                            'HRLTP05',
                            'HRLTP06',
                            'HRLTP07',
                            'HRLTP08',
                            'HRLTP09',
                            'HRLTP10',
                            'HRNOSEXP',
                            'HRLSP1',
                            'HRLSP2',
                            'HRINTNET',
                            'HRINTHL',
                            'HRINTHA',
                            'HRINTTN',
                            'HRINTDZ',
                            'HRINTHP',
                            'HRINTHPR',
                            'AVISION',
                            'ABLIND',
                            'LUPPRT',
                            'WKDAYR',
                            'BEDDAYR',
                            'AHSTATYR',
                            'SPECEQ',
                            'FLWALK',
                            'FLCLIMB',
                            'FLSTAND',
                            'FLSIT',
                            'FLSTOOP',
                            'FLREACH',
                            'FLGRASP',
                            'FLCARRY',
                            'FLPUSH',
                            'FLSHOP',
                            'FLSOCL',
                            'FLRELAX',
                            'FLA1AR',
                            'AFLHCA1',
                            'AFLHCA2',
                            'AFLHCA3',
                            'AFLHCA4',
                            'AFLHCA5',
                            'AFLHCA6',
                            'AFLHCA7',
                            'AFLHCA8',
                            'AFLHCA9',
                            'AFLHCA10',
                            'AFLHCA11',
                            'AFLHCA12',
                            'AFLHCA13',
                            'ALHCA14A',
                            'AFLHCA15',
                            'AFLHCA16',
                            'AFLHCA17',
                            'AFLHCA18',
                            'AFLHC19_',
                            'AFLHC20_',
                            'AFLHC21_',
                            'AFLHC22_',
                            'AFLHC23_',
                            'AFLHC24_',
                            'AFLHC25_',
                            'AFLHC26_',
                            'AFLHC27_',
                            'AFLHC28_',
                            'AFLHC29_',
                            'AFLHC30_',
                            'AFLHC31_',
                            'AFLHC32_',
                            'AFLHC33_',
                            'AFLHC34_',
                            'AFLHCA90',
                            'AFLHCA91',
                            'ALTIME1',
                            'ALUNIT1',
                            'ALDURA1',
                            'ALDURB1',
                            'ALCHRC1',
                            'ALTIME2',
                            'ALUNIT2',
                            'ALDURA2',
                            'ALDURB2',
                            'ALCHRC2',
                            'ALTIME3',
                            'ALUNIT3',
                            'ALDURA3',
                            'ALDURB3',
                            'ALCHRC3',
                            'ALTIME4',
                            'ALUNIT4',
                            'ALDURA4',
                            'ALDURB4',
                            'ALCHRC4',
                            'ALTIME5',
                            'ALUNIT5',
                            'ALDURA5',
                            'ALDURB5',
                            'ALCHRC5',
                            'ALTIME6',
                            'ALUNIT6',
                            'ALDURA6',
                            'ALDURB6',
                            'ALCHRC6',
                            'ALTIME7',
                            'ALUNIT7',
                            'ALDURA7',
                            'ALDURB7',
                            'ALCHRC7',
                            'ALTIME8',
                            'ALUNIT8',
                            'ALDURA8',
                            'ALDURB8',
                            'ALCHRC8',
                            'ALTIME9',
                            'ALUNIT9',
                            'ALDURA9',
                            'ALDURB9',
                            'ALCHRC9',
                            'ALTIME10',
                            'ALUNIT10',
                            'ALDURA10',
                            'ALDURB10',
                            'ALCHRC10',
                            'ALTIME11',
                            'ALUNIT11',
                            'ALDURA11',
                            'ALDURB11',
                            'ALCHRC11',
                            'ALTIME12',
                            'ALUNIT12',
                            'ALDURA12',
                            'ALDURB12',
                            'ALCHRC12',
                            'ALTIME13',
                            'ALUNIT13',
                            'ALDURA13',
                            'ALDURB13',
                            'ALCHRC13',
                            'ATIME14A',
                            'AUNIT14A',
                            'ADURA14A',
                            'ADURB14A',
                            'ACHRC14A',
                            'ALTIME15',
                            'ALUNIT15',
                            'ALDURA15',
                            'ALDURB15',
                            'ALCHRC15',
                            'ALTIME16',
                            'ALUNIT16',
                            'ALDURA16',
                            'ALDURB16',
                            'ALCHRC16',
                            'ALTIME17',
                            'ALUNIT17',
                            'ALDURA17',
                            'ALDURB17',
                            'ALCHRC17',
                            'ALTIME18',
                            'ALUNIT18',
                            'ALDURA18',
                            'ALDURB18',
                            'ALCHRC18',
                            'ALTIME19',
                            'ALUNIT19',
                            'ALDURA19',
                            'ALDURB19',
                            'ALCHRC19',
                            'ALTIME20',
                            'ALUNIT20',
                            'ALDURA20',
                            'ALDURB20',
                            'ALCHRC20',
                            'ALTIME21',
                            'ALUNIT21',
                            'ALDURA21',
                            'ALDURB21',
                            'ALCHRC21',
                            'ALTIME22',
                            'ALUNIT22',
                            'ALDURA22',
                            'ALDURB22',
                            'ALCHRC22',
                            'ALTIME23',
                            'ALUNIT23',
                            'ALDURA23',
                            'ALDURB23',
                            'ALCHRC23',
                            'ALTIME24',
                            'ALUNIT24',
                            'ALDURA24',
                            'ALDURB24',
                            'ALCHRC24',
                            'ALTIME25',
                            'ALUNIT25',
                            'ALDURA25',
                            'ALDURB25',
                            'ALCHRC25',
                            'ALTIME26',
                            'ALUNIT26',
                            'ALDURA26',
                            'ALDURB26',
                            'ALCHRC26',
                            'ALTIME27',
                            'ALUNIT27',
                            'ALDURA27',
                            'ALDURB27',
                            'ALCHRC27',
                            'ALTIME28',
                            'ALUNIT28',
                            'ALDURA28',
                            'ALDURB28',
                            'ALCHRC28',
                            'ALTIME29',
                            'ALUNIT29',
                            'ALDURA29',
                            'ALDURB29',
                            'ALCHRC29',
                            'ALTIME30',
                            'ALUNIT30',
                            'ALDURA30',
                            'ALDURB30',
                            'ALCHRC30',
                            'ALTIME31',
                            'ALUNIT31',
                            'ALDURA31',
                            'ALDURB31',
                            'ALCHRC31',
                            'ALTIME32',
                            'ALUNIT32',
                            'ALDURA32',
                            'ALDURB32',
                            'ALCHRC32',
                            'ALTIME33',
                            'ALUNIT33',
                            'ALDURA33',
                            'ALDURB33',
                            'ALCHRC33',
                            'ALTIME34',
                            'ALUNIT34',
                            'ALDURA34',
                            'ALDURB34',
                            'ALCHRC34',
                            'ALTIME90',
                            'ALUNIT90',
                            'ALDURA90',
                            'ALDURB90',
                            'ALCHRC90',
                            'ALTIME91',
                            'ALUNIT91',
                            'ALDURA91',
                            'ALDURB91',
                            'ALCHRC91',
                            'ALCNDRT',
                            'ALCHRONR',
                            'SMKEV',
                            'SMKREG',
                            'SMKNOW',
                            'SMKSTAT2',
                            'SMKQTNO',
                            'SMKQTTP',
                            'SMKQTY',
                            'CIGSDA1',
                            'CIGDAMO',
                            'CIGSDA2',
                            'CIGSDAY',
                            'CIGQTYR',
                            'OTHCIGEV',
                            'OTHCIGED',
                            'SMKLESEV',
                            'SMKLESED',
                            'TOBLASYR',
                            'TOBQTYR',
                            'ECIGEV',
                            'ECIGED',
                            'VIGNO',
                            'VIGTP',
                            'VIGFREQW',
                            'VIGLNGNO',
                            'VIGLNGTP',
                            'VIGMIN',
                            'MODNO',
                            'MODTP',
                            'MODFREQW',
                            'MODLNGNO',
                            'MODLNGTP',
                            'MODMIN',
                            'STRNGNO',
                            'STRNGTP',
                            'STRFREQW',
                            'ALC1YR',
                            'ALCLIFE',
                            'ALC12MNO',
                            'ALC12MTP',
                            'ALC12MWK',
                            'ALC12MYR',
                            'ALCAMT',
                            'ALCSTAT',
                            'ALC5UPN1',
                            'ALC5UPT1',
                            'ALC5UPY1',
                            'AHEIGHT',
                            'AWEIGHTP',
                            'BMI',
                            'AUSUALPL',
                            'APLKIND',
                            'AHCPLROU',
                            'AHCPLKND',
                            'AHCCHGYR',
                            'AHCCHGHI',
                            'ANOUSPL1',
                            'ANOUSPL2',
                            'ANOUSPL3',
                            'ANOUSPL4',
                            'ANOUSPL5',
                            'ANOUSPL6',
                            'ANOUSPL7',
                            'ANOUSPL8',
                            'ANOUSPL9',
                            'APRVTRYR',
                            'APRVTRFD',
                            'ADRNANP',
                            'ADRNAI',
                            'AHCDLYR1',
                            'AHCDLYR2',
                            'AHCDLYR3',
                            'AHCDLYR4',
                            'AHCDLYR5',
                            'AHCAFYR1',
                            'AHCAFYR2',
                            'AHCAFYR3',
                            'AHCAFYR4',
                            'AHCAFYR5',
                            'AHCAFYR6',
                            'AWORPAY',
                            'AHICOMP',
                            'ARX12MO',
                            'ARX12_1',
                            'ARX12_2',
                            'ARX12_3',
                            'ARX12_4',
                            'ARX12_5',
                            'ARX12_6',
                            'ADNLONG2',
                            'AHCSYR1',
                            'AHCSYR2',
                            'AHCSYR3',
                            'AHCSYR4',
                            'AHCSYR5',
                            'AHCSYR6',
                            'AHCSYR7',
                            'AHCSYR8',
                            'AHCSYR9',
                            'AHCSYR10',
                            'AHERNOY2',
                            'AERVISND',
                            'AERHOS',
                            'AERREA1R',
                            'AERREA2R',
                            'AERREA3R',
                            'AERREA4R',
                            'AERREA5R',
                            'AERREA6R',
                            'AERREA7R',
                            'AERREA8R',
                            'AHCHYR',
                            'AHCHMOYR',
                            'AHCHNOY2',
                            'AHCNOYR2',
                            'ASRGYR',
                            'ASRGNOYR',
                            'AMDLONGR',
                            'AVISLAST',
                            'ALASTYP1',
                            'ALASTYP2',
                            'ALASTYP3',
                            'ALASTYP4',
                            'ALASTVRB',
                            'AVISAPN2',
                            'AVISAPT2',
                            'AWAITRMN',
                            'AWAITRMT',
                            'HIT1A',
                            'HIT2A',
                            'HIT3A',
                            'HIT4A',
                            'HIT5A',
                            'SHTFLU2',
                            'ASHFLUM2',
                            'ASHFLUY2',
                            'FLUSHPG1',
                            'FLUSHPG2',
                            'SPRFLU2',
                            'ASPFLUM2',
                            'ASPFLUY2',
                            'SHTPNUYR',
                            'APOX',
                            'APOX12MO',
                            'AHEP',
                            'AHEPLIV',
                            'AHEPBTST',
                            'SHTHEPB',
                            'SHEPDOS',
                            'SHTHEPA',
                            'SHEPANUM',
                            'AHEPCTST',
                            'AHEPCRES',
                            'SHINGLES',
                            'SHTTD',
                            'SHTTD05',
                            'SHTTDAP2',
                            'SHTHPV2',
                            'SHHPVDOS',
                            'AHPVAGE',
                            'LIVEV',
                            'TRAVEL',
                            'WRKHLTH2',
                            'WRKDIR',
                            'APSBPCH1',
                            'APSCHCH1',
                            'APSBSCH1',
                            'APSPAP',
                            'APSMAM',
                            'APSCOL',
                            'APSDIET',
                            'APSSMKC',
                            'LTCFAM',
                            'LTCHELP',
                            'LTCWHO1',
                            'LTCWHO2',
                            'LTCWHO3',
                            'LTCWHO4',
                            'LTCWHO5',
                            'AINDINS',
                            'AINDPRCH',
                            'AINDWHO',
                            'AINDDIF1',
                            'AINDDIF2',
                            'AINDENY1',
                            'AINDENY2',
                            'AINDENY3',
                            'AINDNOT1',
                            'AINDNOT2',
                            'AINDNOT3',
                            'AINDNOT4',
                            'AINDNOT5',
                            'AEXCHNG',
                            'ASICPUSE',
                            'ASISATHC',
                            'ASITENUR',
                            'ASINHELP',
                            'ASINCNTO',
                            'ASINTRU',
                            'ASINKNT',
                            'ASISIM',
                            'ASISIF',
                            'ASIRETR',
                            'ASIMEDC',
                            'ASISTLV',
                            'ASICNHC',
                            'ASICCOLL',
                            'ASINBILL',
                            'ASIHCST',
                            'ASICCMP',
                            'ASISLEEP',
                            'ASISLPFL',
                            'ASISLPST',
                            'ASISLPMD',
                            'ASIREST',
                            'ASISAD',
                            'ASINERV',
                            'ASIRSTLS',
                            'ASIHOPLS',
                            'ASIEFFRT',
                            'ASIWTHLS',
                            'ASIMUCH',
                            'ASIHIVT',
                            'ASIHIVWN',
                            'AWEBUSE',
                            'AWEBOFNO',
                            'AWEBOFTP',
                            'AWEBORP',
                            'AWEBEML',
                            'AWEBMNO',
                            'AWEBMTP'
                                    ))

for i in range(36696):
    df.loc[i] = [
                    RECTYPE_LIST[i],
                    SRVY_YR_LIST[i],
                    HHX_LIST[i],
                    INTV_QRT_LIST[i],
                    INTV_MON_LIST[i],
                    FMX_LIST[i],
                    FPX_LIST[i],
                    WTIA_SA_LIST[i],
                    WTFA_SA_LIST[i],
                    REGION_LIST[i],
                    STRAT_P_LIST[i],
                    PSU_P_LIST[i],
                    SEX_LIST[i],
                    HISPAN_I_LIST[i],
                    RACERPI2_LIST[i],
                    MRACRPI2_LIST[i],
                    MRACBPI2_LIST[i],
                    AGE_P_LIST[i],
                    R_MARITL_LIST[i],
                    PROXYSA_LIST[i],
                    PROX1_LIST[i],
                    PROX2_LIST[i],
                    LATEINTA_LIST[i],
                    FDRN_FLG_LIST[i],
                    DOINGLWA_LIST[i],
                    WHYNOWKA_LIST[i],
                    EVERWRK_LIST[i],
                    INDSTRN1_LIST[i],
                    INDSTRN2_LIST[i],
                    OCCUPN1_LIST[i],
                    OCCUPN2_LIST[i],
                    WRKCATA_LIST[i],
                    BUSINC1A_LIST[i],
                    LOCALL1A_LIST[i],
                    YRSWRKPA_LIST[i],
                    WRKLONGH_LIST[i],
                    HOURPDA_LIST[i],
                    PDSICKA_LIST[i],
                    ONEJOB_LIST[i],
                    WRKLYR4_LIST[i],
                    HYPEV_LIST[i],
                    HYPDIFV_LIST[i],
                    HYPYR1_LIST[i],
                    HYBPCKNO_LIST[i],
                    HYBPCKTP_LIST[i],
                    HYBPLEV_LIST[i],
                    HYPMDEV2_LIST[i],
                    HYPMED2_LIST[i],
                    CHLEV_LIST[i],
                    CHLYR_LIST[i],
                    CLCKNO_LIST[i],
                    CLCKTP_LIST[i],
                    CHLMDEV2_LIST[i],
                    CHLMDNW2_LIST[i],
                    CHDEV_LIST[i],
                    ANGEV_LIST[i],
                    MIEV_LIST[i],
                    HRTEV_LIST[i],
                    STREV_LIST[i],
                    EPHEV_LIST[i],
                    JAWP_LIST[i],
                    WEA_LIST[i],
                    CHE_LIST[i],
                    ARM_LIST[i],
                    BRTH_LIST[i],
                    AHADO_LIST[i],
                    FACE_LIST[i],
                    SPEAKING_LIST[i],
                    EYE_LIST[i],
                    WALKING_LIST[i],
                    HEADACHE_LIST[i],
                    ASTDO_LIST[i],
                    COPDEV_LIST[i],
                    ASPMEDEV_LIST[i],
                    ASPMEDAD_LIST[i],
                    ASPMDMED_LIST[i],
                    ASPONOWN_LIST[i],
                    AASMEV_LIST[i],
                    AASSTILL_LIST[i],
                    AASMYR_LIST[i],
                    AASERYR1_LIST[i],
                    ULCEV_LIST[i],
                    ULCYR_LIST[i],
                    CANEV_LIST[i],
                    CNKIND1_LIST[i],
                    CNKIND2_LIST[i],
                    CNKIND3_LIST[i],
                    CNKIND4_LIST[i],
                    CNKIND5_LIST[i],
                    CNKIND6_LIST[i],
                    CNKIND7_LIST[i],
                    CNKIND8_LIST[i],
                    CNKIND9_LIST[i],
                    CNKIND10_LIST[i],
                    CNKIND11_LIST[i],
                    CNKIND12_LIST[i],
                    CNKIND13_LIST[i],
                    CNKIND14_LIST[i],
                    CNKIND15_LIST[i],
                    CNKIND16_LIST[i],
                    CNKIND17_LIST[i],
                    CNKIND18_LIST[i],
                    CNKIND19_LIST[i],
                    CNKIND20_LIST[i],
                    CNKIND21_LIST[i],
                    CNKIND22_LIST[i],
                    CNKIND23_LIST[i],
                    CNKIND24_LIST[i],
                    CNKIND25_LIST[i],
                    CNKIND26_LIST[i],
                    CNKIND27_LIST[i],
                    CNKIND28_LIST[i],
                    CNKIND29_LIST[i],
                    CNKIND30_LIST[i],
                    CNKIND31_LIST[i],
                    CANAGE1_LIST[i],
                    CANAGE2_LIST[i],
                    CANAGE3_LIST[i],
                    CANAGE4_LIST[i],
                    CANAGE5_LIST[i],
                    CANAGE6_LIST[i],
                    CANAGE7_LIST[i],
                    CANAGE8_LIST[i],
                    CANAGE9_LIST[i],
                    CANAGE10_LIST[i],
                    CANAGE11_LIST[i],
                    CANAGE12_LIST[i],
                    CANAGE13_LIST[i],
                    CANAGE14_LIST[i],
                    CANAGE15_LIST[i],
                    CANAGE16_LIST[i],
                    CANAGE17_LIST[i],
                    CANAGE18_LIST[i],
                    CANAGE19_LIST[i],
                    CANAGE20_LIST[i],
                    CANAGE21_LIST[i],
                    CANAGE22_LIST[i],
                    CANAGE23_LIST[i],
                    CANAGE24_LIST[i],
                    CANAGE25_LIST[i],
                    CANAGE26_LIST[i],
                    CANAGE27_LIST[i],
                    CANAGE28_LIST[i],
                    CANAGE29_LIST[i],
                    CANAGE30_LIST[i],
                    DIBEV_LIST[i],
                    DIBPRE1_LIST[i],
                    DIBAGE_LIST[i],
                    DIFAGE2_LIST[i],
                    INSLN_LIST[i],
                    DIBPILL_LIST[i],
                    AHAYFYR_LIST[i],
                    SINYR_LIST[i],
                    CBRCHYR_LIST[i],
                    KIDWKYR_LIST[i],
                    LIVYR_LIST[i],
                    JNTSYMP_LIST[i],
                    JMTHP1_LIST[i],
                    JMTHP2_LIST[i],
                    JMTHP3_LIST[i],
                    JMTHP4_LIST[i],
                    JMTHP5_LIST[i],
                    JMTHP6_LIST[i],
                    JMTHP7_LIST[i],
                    JMTHP8_LIST[i],
                    JMTHP9_LIST[i],
                    JMTHP10_LIST[i],
                    JMTHP11_LIST[i],
                    JMTHP12_LIST[i],
                    JMTHP13_LIST[i],
                    JMTHP14_LIST[i],
                    JMTHP15_LIST[i],
                    JMTHP16_LIST[i],
                    JMTHP17_LIST[i],
                    JNTPN_LIST[i],
                    JNTCHR_LIST[i],
                    JNTHP_LIST[i],
                    ARTH1_LIST[i],
                    ARTHWT_LIST[i],
                    ARTHPH_LIST[i],
                    ARTHCLS_LIST[i],
                    ARTHLMT_LIST[i],
                    ARTHWRK_LIST[i],
                    PAINECK_LIST[i],
                    PAINLB_LIST[i],
                    PAINLEG_LIST[i],
                    PAINFACE_LIST[i],
                    AMIGR_LIST[i],
                    ACOLD2W_LIST[i],
                    AINTIL2W_LIST[i],
                    PREGNOW_LIST[i],
                    PREGFLYR_LIST[i],
                    AHEARST2_LIST[i],
                    HRWORS_LIST[i],
                    HRWHICH_LIST[i],
                    HRRIGHT_LIST[i],
                    HRLEFT_LIST[i],
                    HRWHISP1_LIST[i],
                    HRTALK1_LIST[i],
                    HRSHOUT1_LIST[i],
                    HRSPEAK1_LIST[i],
                    HRCOCRE1_LIST[i],
                    HRCOCIM1_LIST[i],
                    HRFAM_LIST[i],
                    HRBACK_LIST[i],
                    HRFRUST_LIST[i],
                    HRSAFETY_LIST[i],
                    HEARAGE1_LIST[i],
                    HRCAUS1_LIST[i],
                    HRPROBHP_LIST[i],
                    HRENT_LIST[i],
                    HRAUD_LIST[i],
                    HRTEST_LIST[i],
                    HRAIDNOW_LIST[i],
                    HRAIDLNG_LIST[i],
                    HRAID2WK_LIST[i],
                    HRAIDHLP_LIST[i],
                    HRAIDEV_LIST[i],
                    HRAIDREC_LIST[i],
                    HRAIDLGP_LIST[i],
                    HRAIDOF2_LIST[i],
                    HRAIDN01_LIST[i],
                    HRAIDN02_LIST[i],
                    HRAIDN03_LIST[i],
                    HRAIDN04_LIST[i],
                    HRAIDN05_LIST[i],
                    HRAIDN06_LIST[i],
                    HRAIDN07_LIST[i],
                    HRAIDN08_LIST[i],
                    HRAIDN09_LIST[i],
                    HRAIDN10_LIST[i],
                    HRAIDN11_LIST[i],
                    HRAUDTRN_LIST[i],
                    HRALDS_LIST[i],
                    HRALDT01_LIST[i],
                    HRALDT02_LIST[i],
                    HRALDT03_LIST[i],
                    HRALDT04_LIST[i],
                    HRALDT05_LIST[i],
                    HRALDT06_LIST[i],
                    HRALDT07_LIST[i],
                    HRALDT08_LIST[i],
                    HRALDT09_LIST[i],
                    HRALDT10_LIST[i],
                    HRALDT11_LIST[i],
                    HRBDIZZ_LIST[i],
                    HRTIN_LIST[i],
                    HRTINOFT_LIST[i],
                    HRTINLNG_LIST[i],
                    HRTINMUS_LIST[i],
                    HRTINSLP_LIST[i],
                    HRTINPRO_LIST[i],
                    HRTINDIS_LIST[i],
                    HRTINDOC_LIST[i],
                    HRTINRM_LIST[i],
                    HREMTY01_LIST[i],
                    HREMTY02_LIST[i],
                    HREMTY03_LIST[i],
                    HREMTY04_LIST[i],
                    HREMTY05_LIST[i],
                    HREMTY06_LIST[i],
                    HREMTY07_LIST[i],
                    HREMTY08_LIST[i],
                    HREMTY09_LIST[i],
                    HREMTY10_LIST[i],
                    HREMTY11_LIST[i],
                    HREMTY12_LIST[i],
                    HRTNRMHP_LIST[i],
                    HRHCUSIS_LIST[i],
                    HRHCPROB_LIST[i],
                    HRFIRE_LIST[i],
                    HRFIRTYP_LIST[i],
                    HRFRTIM_LIST[i],
                    HR12MR_LIST[i],
                    HRFRPROT_LIST[i],
                    HRTOTR_LIST[i],
                    HRFRPRT2_LIST[i],
                    HRWKVLNS_LIST[i],
                    HRWKLNS_LIST[i],
                    HRWKVLNT_LIST[i],
                    HRWKVLEX_LIST[i],
                    HRWKVLP1_LIST[i],
                    HRWKVLP2_LIST[i],
                    HRWRLNS_LIST[i],
                    HRWKLEX_LIST[i],
                    HRWKLP1_LIST[i],
                    HRWKLP2_LIST[i],
                    HRLSVLNS_LIST[i],
                    HRVLTP01_LIST[i],
                    HRVLTP02_LIST[i],
                    HRVLTP03_LIST[i],
                    HRVLTP04_LIST[i],
                    HRVLTP05_LIST[i],
                    HRVLTP06_LIST[i],
                    HRVLTP07_LIST[i],
                    HRVLTP08_LIST[i],
                    HRVLTP09_LIST[i],
                    HRVLTP10_LIST[i],
                    HRLNOS_LIST[i],
                    HRLTP01_LIST[i],
                    HRLTP02_LIST[i],
                    HRLTP03_LIST[i],
                    HRLTP04_LIST[i],
                    HRLTP05_LIST[i],
                    HRLTP06_LIST[i],
                    HRLTP07_LIST[i],
                    HRLTP08_LIST[i],
                    HRLTP09_LIST[i],
                    HRLTP10_LIST[i],
                    HRNOSEXP_LIST[i],
                    HRLSP1_LIST[i],
                    HRLSP2_LIST[i],
                    HRINTNET_LIST[i],
                    HRINTHL_LIST[i],
                    HRINTHA_LIST[i],
                    HRINTTN_LIST[i],
                    HRINTDZ_LIST[i],
                    HRINTHP_LIST[i],
                    HRINTHPR_LIST[i],
                    AVISION_LIST[i],
                    ABLIND_LIST[i],
                    LUPPRT_LIST[i],
                    WKDAYR_LIST[i],
                    BEDDAYR_LIST[i],
                    AHSTATYR_LIST[i],
                    SPECEQ_LIST[i],
                    FLWALK_LIST[i],
                    FLCLIMB_LIST[i],
                    FLSTAND_LIST[i],
                    FLSIT_LIST[i],
                    FLSTOOP_LIST[i],
                    FLREACH_LIST[i],
                    FLGRASP_LIST[i],
                    FLCARRY_LIST[i],
                    FLPUSH_LIST[i],
                    FLSHOP_LIST[i],
                    FLSOCL_LIST[i],
                    FLRELAX_LIST[i],
                    FLA1AR_LIST[i],
                    AFLHCA1_LIST[i],
                    AFLHCA2_LIST[i],
                    AFLHCA3_LIST[i],
                    AFLHCA4_LIST[i],
                    AFLHCA5_LIST[i],
                    AFLHCA6_LIST[i],
                    AFLHCA7_LIST[i],
                    AFLHCA8_LIST[i],
                    AFLHCA9_LIST[i],
                    AFLHCA10_LIST[i],
                    AFLHCA11_LIST[i],
                    AFLHCA12_LIST[i],
                    AFLHCA13_LIST[i],
                    ALHCA14A_LIST[i],
                    AFLHCA15_LIST[i],
                    AFLHCA16_LIST[i],
                    AFLHCA17_LIST[i],
                    AFLHCA18_LIST[i],
                    AFLHC19__LIST[i],
                    AFLHC20__LIST[i],
                    AFLHC21__LIST[i],
                    AFLHC22__LIST[i],
                    AFLHC23__LIST[i],
                    AFLHC24__LIST[i],
                    AFLHC25__LIST[i],
                    AFLHC26__LIST[i],
                    AFLHC27__LIST[i],
                    AFLHC28__LIST[i],
                    AFLHC29__LIST[i],
                    AFLHC30__LIST[i],
                    AFLHC31__LIST[i],
                    AFLHC32__LIST[i],
                    AFLHC33__LIST[i],
                    AFLHC34__LIST[i],
                    AFLHCA90_LIST[i],
                    AFLHCA91_LIST[i],
                    ALTIME1_LIST[i],
                    ALUNIT1_LIST[i],
                    ALDURA1_LIST[i],
                    ALDURB1_LIST[i],
                    ALCHRC1_LIST[i],
                    ALTIME2_LIST[i],
                    ALUNIT2_LIST[i],
                    ALDURA2_LIST[i],
                    ALDURB2_LIST[i],
                    ALCHRC2_LIST[i],
                    ALTIME3_LIST[i],
                    ALUNIT3_LIST[i],
                    ALDURA3_LIST[i],
                    ALDURB3_LIST[i],
                    ALCHRC3_LIST[i],
                    ALTIME4_LIST[i],
                    ALUNIT4_LIST[i],
                    ALDURA4_LIST[i],
                    ALDURB4_LIST[i],
                    ALCHRC4_LIST[i],
                    ALTIME5_LIST[i],
                    ALUNIT5_LIST[i],
                    ALDURA5_LIST[i],
                    ALDURB5_LIST[i],
                    ALCHRC5_LIST[i],
                    ALTIME6_LIST[i],
                    ALUNIT6_LIST[i],
                    ALDURA6_LIST[i],
                    ALDURB6_LIST[i],
                    ALCHRC6_LIST[i],
                    ALTIME7_LIST[i],
                    ALUNIT7_LIST[i],
                    ALDURA7_LIST[i],
                    ALDURB7_LIST[i],
                    ALCHRC7_LIST[i],
                    ALTIME8_LIST[i],
                    ALUNIT8_LIST[i],
                    ALDURA8_LIST[i],
                    ALDURB8_LIST[i],
                    ALCHRC8_LIST[i],
                    ALTIME9_LIST[i],
                    ALUNIT9_LIST[i],
                    ALDURA9_LIST[i],
                    ALDURB9_LIST[i],
                    ALCHRC9_LIST[i],
                    ALTIME10_LIST[i],
                    ALUNIT10_LIST[i],
                    ALDURA10_LIST[i],
                    ALDURB10_LIST[i],
                    ALCHRC10_LIST[i],
                    ALTIME11_LIST[i],
                    ALUNIT11_LIST[i],
                    ALDURA11_LIST[i],
                    ALDURB11_LIST[i],
                    ALCHRC11_LIST[i],
                    ALTIME12_LIST[i],
                    ALUNIT12_LIST[i],
                    ALDURA12_LIST[i],
                    ALDURB12_LIST[i],
                    ALCHRC12_LIST[i],
                    ALTIME13_LIST[i],
                    ALUNIT13_LIST[i],
                    ALDURA13_LIST[i],
                    ALDURB13_LIST[i],
                    ALCHRC13_LIST[i],
                    ATIME14A_LIST[i],
                    AUNIT14A_LIST[i],
                    ADURA14A_LIST[i],
                    ADURB14A_LIST[i],
                    ACHRC14A_LIST[i],
                    ALTIME15_LIST[i],
                    ALUNIT15_LIST[i],
                    ALDURA15_LIST[i],
                    ALDURB15_LIST[i],
                    ALCHRC15_LIST[i],
                    ALTIME16_LIST[i],
                    ALUNIT16_LIST[i],
                    ALDURA16_LIST[i],
                    ALDURB16_LIST[i],
                    ALCHRC16_LIST[i],
                    ALTIME17_LIST[i],
                    ALUNIT17_LIST[i],
                    ALDURA17_LIST[i],
                    ALDURB17_LIST[i],
                    ALCHRC17_LIST[i],
                    ALTIME18_LIST[i],
                    ALUNIT18_LIST[i],
                    ALDURA18_LIST[i],
                    ALDURB18_LIST[i],
                    ALCHRC18_LIST[i],
                    ALTIME19_LIST[i],
                    ALUNIT19_LIST[i],
                    ALDURA19_LIST[i],
                    ALDURB19_LIST[i],
                    ALCHRC19_LIST[i],
                    ALTIME20_LIST[i],
                    ALUNIT20_LIST[i],
                    ALDURA20_LIST[i],
                    ALDURB20_LIST[i],
                    ALCHRC20_LIST[i],
                    ALTIME21_LIST[i],
                    ALUNIT21_LIST[i],
                    ALDURA21_LIST[i],
                    ALDURB21_LIST[i],
                    ALCHRC21_LIST[i],
                    ALTIME22_LIST[i],
                    ALUNIT22_LIST[i],
                    ALDURA22_LIST[i],
                    ALDURB22_LIST[i],
                    ALCHRC22_LIST[i],
                    ALTIME23_LIST[i],
                    ALUNIT23_LIST[i],
                    ALDURA23_LIST[i],
                    ALDURB23_LIST[i],
                    ALCHRC23_LIST[i],
                    ALTIME24_LIST[i],
                    ALUNIT24_LIST[i],
                    ALDURA24_LIST[i],
                    ALDURB24_LIST[i],
                    ALCHRC24_LIST[i],
                    ALTIME25_LIST[i],
                    ALUNIT25_LIST[i],
                    ALDURA25_LIST[i],
                    ALDURB25_LIST[i],
                    ALCHRC25_LIST[i],
                    ALTIME26_LIST[i],
                    ALUNIT26_LIST[i],
                    ALDURA26_LIST[i],
                    ALDURB26_LIST[i],
                    ALCHRC26_LIST[i],
                    ALTIME27_LIST[i],
                    ALUNIT27_LIST[i],
                    ALDURA27_LIST[i],
                    ALDURB27_LIST[i],
                    ALCHRC27_LIST[i],
                    ALTIME28_LIST[i],
                    ALUNIT28_LIST[i],
                    ALDURA28_LIST[i],
                    ALDURB28_LIST[i],
                    ALCHRC28_LIST[i],
                    ALTIME29_LIST[i],
                    ALUNIT29_LIST[i],
                    ALDURA29_LIST[i],
                    ALDURB29_LIST[i],
                    ALCHRC29_LIST[i],
                    ALTIME30_LIST[i],
                    ALUNIT30_LIST[i],
                    ALDURA30_LIST[i],
                    ALDURB30_LIST[i],
                    ALCHRC30_LIST[i],
                    ALTIME31_LIST[i],
                    ALUNIT31_LIST[i],
                    ALDURA31_LIST[i],
                    ALDURB31_LIST[i],
                    ALCHRC31_LIST[i],
                    ALTIME32_LIST[i],
                    ALUNIT32_LIST[i],
                    ALDURA32_LIST[i],
                    ALDURB32_LIST[i],
                    ALCHRC32_LIST[i],
                    ALTIME33_LIST[i],
                    ALUNIT33_LIST[i],
                    ALDURA33_LIST[i],
                    ALDURB33_LIST[i],
                    ALCHRC33_LIST[i],
                    ALTIME34_LIST[i],
                    ALUNIT34_LIST[i],
                    ALDURA34_LIST[i],
                    ALDURB34_LIST[i],
                    ALCHRC34_LIST[i],
                    ALTIME90_LIST[i],
                    ALUNIT90_LIST[i],
                    ALDURA90_LIST[i],
                    ALDURB90_LIST[i],
                    ALCHRC90_LIST[i],
                    ALTIME91_LIST[i],
                    ALUNIT91_LIST[i],
                    ALDURA91_LIST[i],
                    ALDURB91_LIST[i],
                    ALCHRC91_LIST[i],
                    ALCNDRT_LIST[i],
                    ALCHRONR_LIST[i],
                    SMKEV_LIST[i],
                    SMKREG_LIST[i],
                    SMKNOW_LIST[i],
                    SMKSTAT2_LIST[i],
                    SMKQTNO_LIST[i],
                    SMKQTTP_LIST[i],
                    SMKQTY_LIST[i],
                    CIGSDA1_LIST[i],
                    CIGDAMO_LIST[i],
                    CIGSDA2_LIST[i],
                    CIGSDAY_LIST[i],
                    CIGQTYR_LIST[i],
                    OTHCIGEV_LIST[i],
                    OTHCIGED_LIST[i],
                    SMKLESEV_LIST[i],
                    SMKLESED_LIST[i],
                    TOBLASYR_LIST[i],
                    TOBQTYR_LIST[i],
                    ECIGEV_LIST[i],
                    ECIGED_LIST[i],
                    VIGNO_LIST[i],
                    VIGTP_LIST[i],
                    VIGFREQW_LIST[i],
                    VIGLNGNO_LIST[i],
                    VIGLNGTP_LIST[i],
                    VIGMIN_LIST[i],
                    MODNO_LIST[i],
                    MODTP_LIST[i],
                    MODFREQW_LIST[i],
                    MODLNGNO_LIST[i],
                    MODLNGTP_LIST[i],
                    MODMIN_LIST[i],
                    STRNGNO_LIST[i],
                    STRNGTP_LIST[i],
                    STRFREQW_LIST[i],
                    ALC1YR_LIST[i],
                    ALCLIFE_LIST[i],
                    ALC12MNO_LIST[i],
                    ALC12MTP_LIST[i],
                    ALC12MWK_LIST[i],
                    ALC12MYR_LIST[i],
                    ALCAMT_LIST[i],
                    ALCSTAT_LIST[i],
                    ALC5UPN1_LIST[i],
                    ALC5UPT1_LIST[i],
                    ALC5UPY1_LIST[i],
                    AHEIGHT_LIST[i],
                    AWEIGHTP_LIST[i],
                    BMI_LIST[i],
                    AUSUALPL_LIST[i],
                    APLKIND_LIST[i],
                    AHCPLROU_LIST[i],
                    AHCPLKND_LIST[i],
                    AHCCHGYR_LIST[i],
                    AHCCHGHI_LIST[i],
                    ANOUSPL1_LIST[i],
                    ANOUSPL2_LIST[i],
                    ANOUSPL3_LIST[i],
                    ANOUSPL4_LIST[i],
                    ANOUSPL5_LIST[i],
                    ANOUSPL6_LIST[i],
                    ANOUSPL7_LIST[i],
                    ANOUSPL8_LIST[i],
                    ANOUSPL9_LIST[i],
                    APRVTRYR_LIST[i],
                    APRVTRFD_LIST[i],
                    ADRNANP_LIST[i],
                    ADRNAI_LIST[i],
                    AHCDLYR1_LIST[i],
                    AHCDLYR2_LIST[i],
                    AHCDLYR3_LIST[i],
                    AHCDLYR4_LIST[i],
                    AHCDLYR5_LIST[i],
                    AHCAFYR1_LIST[i],
                    AHCAFYR2_LIST[i],
                    AHCAFYR3_LIST[i],
                    AHCAFYR4_LIST[i],
                    AHCAFYR5_LIST[i],
                    AHCAFYR6_LIST[i],
                    AWORPAY_LIST[i],
                    AHICOMP_LIST[i],
                    ARX12MO_LIST[i],
                    ARX12_1_LIST[i],
                    ARX12_2_LIST[i],
                    ARX12_3_LIST[i],
                    ARX12_4_LIST[i],
                    ARX12_5_LIST[i],
                    ARX12_6_LIST[i],
                    ADNLONG2_LIST[i],
                    AHCSYR1_LIST[i],
                    AHCSYR2_LIST[i],
                    AHCSYR3_LIST[i],
                    AHCSYR4_LIST[i],
                    AHCSYR5_LIST[i],
                    AHCSYR6_LIST[i],
                    AHCSYR7_LIST[i],
                    AHCSYR8_LIST[i],
                    AHCSYR9_LIST[i],
                    AHCSYR10_LIST[i],
                    AHERNOY2_LIST[i],
                    AERVISND_LIST[i],
                    AERHOS_LIST[i],
                    AERREA1R_LIST[i],
                    AERREA2R_LIST[i],
                    AERREA3R_LIST[i],
                    AERREA4R_LIST[i],
                    AERREA5R_LIST[i],
                    AERREA6R_LIST[i],
                    AERREA7R_LIST[i],
                    AERREA8R_LIST[i],
                    AHCHYR_LIST[i],
                    AHCHMOYR_LIST[i],
                    AHCHNOY2_LIST[i],
                    AHCNOYR2_LIST[i],
                    ASRGYR_LIST[i],
                    ASRGNOYR_LIST[i],
                    AMDLONGR_LIST[i],
                    AVISLAST_LIST[i],
                    ALASTYP1_LIST[i],
                    ALASTYP2_LIST[i],
                    ALASTYP3_LIST[i],
                    ALASTYP4_LIST[i],
                    ALASTVRB_LIST[i],
                    AVISAPN2_LIST[i],
                    AVISAPT2_LIST[i],
                    AWAITRMN_LIST[i],
                    AWAITRMT_LIST[i],
                    HIT1A_LIST[i],
                    HIT2A_LIST[i],
                    HIT3A_LIST[i],
                    HIT4A_LIST[i],
                    HIT5A_LIST[i],
                    SHTFLU2_LIST[i],
                    ASHFLUM2_LIST[i],
                    ASHFLUY2_LIST[i],
                    FLUSHPG1_LIST[i],
                    FLUSHPG2_LIST[i],
                    SPRFLU2_LIST[i],
                    ASPFLUM2_LIST[i],
                    ASPFLUY2_LIST[i],
                    SHTPNUYR_LIST[i],
                    APOX_LIST[i],
                    APOX12MO_LIST[i],
                    AHEP_LIST[i],
                    AHEPLIV_LIST[i],
                    AHEPBTST_LIST[i],
                    SHTHEPB_LIST[i],
                    SHEPDOS_LIST[i],
                    SHTHEPA_LIST[i],
                    SHEPANUM_LIST[i],
                    AHEPCTST_LIST[i],
                    AHEPCRES_LIST[i],
                    SHINGLES_LIST[i],
                    SHTTD_LIST[i],
                    SHTTD05_LIST[i],
                    SHTTDAP2_LIST[i],
                    SHTHPV2_LIST[i],
                    SHHPVDOS_LIST[i],
                    AHPVAGE_LIST[i],
                    LIVEV_LIST[i],
                    TRAVEL_LIST[i],
                    WRKHLTH2_LIST[i],
                    WRKDIR_LIST[i],
                    APSBPCH1_LIST[i],
                    APSCHCH1_LIST[i],
                    APSBSCH1_LIST[i],
                    APSPAP_LIST[i],
                    APSMAM_LIST[i],
                    APSCOL_LIST[i],
                    APSDIET_LIST[i],
                    APSSMKC_LIST[i],
                    LTCFAM_LIST[i],
                    LTCHELP_LIST[i],
                    LTCWHO1_LIST[i],
                    LTCWHO2_LIST[i],
                    LTCWHO3_LIST[i],
                    LTCWHO4_LIST[i],
                    LTCWHO5_LIST[i],
                    AINDINS_LIST[i],
                    AINDPRCH_LIST[i],
                    AINDWHO_LIST[i],
                    AINDDIF1_LIST[i],
                    AINDDIF2_LIST[i],
                    AINDENY1_LIST[i],
                    AINDENY2_LIST[i],
                    AINDENY3_LIST[i],
                    AINDNOT1_LIST[i],
                    AINDNOT2_LIST[i],
                    AINDNOT3_LIST[i],
                    AINDNOT4_LIST[i],
                    AINDNOT5_LIST[i],
                    AEXCHNG_LIST[i],
                    ASICPUSE_LIST[i],
                    ASISATHC_LIST[i],
                    ASITENUR_LIST[i],
                    ASINHELP_LIST[i],
                    ASINCNTO_LIST[i],
                    ASINTRU_LIST[i],
                    ASINKNT_LIST[i],
                    ASISIM_LIST[i],
                    ASISIF_LIST[i],
                    ASIRETR_LIST[i],
                    ASIMEDC_LIST[i],
                    ASISTLV_LIST[i],
                    ASICNHC_LIST[i],
                    ASICCOLL_LIST[i],
                    ASINBILL_LIST[i],
                    ASIHCST_LIST[i],
                    ASICCMP_LIST[i],
                    ASISLEEP_LIST[i],
                    ASISLPFL_LIST[i],
                    ASISLPST_LIST[i],
                    ASISLPMD_LIST[i],
                    ASIREST_LIST[i],
                    ASISAD_LIST[i],
                    ASINERV_LIST[i],
                    ASIRSTLS_LIST[i],
                    ASIHOPLS_LIST[i],
                    ASIEFFRT_LIST[i],
                    ASIWTHLS_LIST[i],
                    ASIMUCH_LIST[i],
                    ASIHIVT_LIST[i],
                    ASIHIVWN_LIST[i],
                    AWEBUSE_LIST[i],
                    AWEBOFNO_LIST[i],
                    AWEBOFTP_LIST[i],
                    AWEBORP_LIST[i],
                    AWEBEML_LIST[i],
                    AWEBMNO_LIST[i],
                    AWEBMTP_LIST[i]
                                    ]

df = df.applymap(lambda x: np.nan if str(x).isspace() else x)
df.to_csv("nhis_2014_samadult_data.csv")
