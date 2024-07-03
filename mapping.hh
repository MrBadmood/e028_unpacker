#include "mapping_trloii.hh"

//VMMR0 energies
SIGNAL(ZERO_SUPPRESS_MULTI(20): VMMR1_MMR1_E1);
SIGNAL(VMMR1_MMR1_E1  , main.vmmr8[0].data[0][0],
       VMMR1_MMR1_E128, main.vmmr8[0].data[0][127], DATA12);
SIGNAL(VMMR1_MMR2_E1  , main.vmmr8[0].data[1][0],
       VMMR1_MMR2_E128, main.vmmr8[0].data[1][127], DATA12);
SIGNAL(VMMR1_MMR3_E1  , main.vmmr8[0].data[2][0],
       VMMR1_MMR3_E128, main.vmmr8[0].data[2][127], DATA12);
SIGNAL(VMMR1_MMR4_E1  , main.vmmr8[0].data[3][0],
       VMMR1_MMR4_E128, main.vmmr8[0].data[3][127], DATA12);
SIGNAL(VMMR1_MMR5_E1  , main.vmmr8[0].data[4][0],
       VMMR1_MMR5_E128, main.vmmr8[0].data[4][127], DATA12);
SIGNAL(VMMR1_MMR6_E1  , main.vmmr8[0].data[5][0],
       VMMR1_MMR6_E128, main.vmmr8[0].data[5][127], DATA12);
SIGNAL(VMMR1_MMR7_E1  , main.vmmr8[0].data[6][0],
       VMMR1_MMR7_E128, main.vmmr8[0].data[6][127], DATA12);
SIGNAL(VMMR1_MMR8_E1  , main.vmmr8[0].data[7][0],
       VMMR1_MMR8_E128, main.vmmr8[0].data[7][127], DATA12);
//VMMR0 deltaT
SIGNAL(ZERO_SUPPRESS: VMMR1_DT1);
SIGNAL(VMMR1_DT1, main.vmmr8[0].time_diff[0],
       VMMR1_DT8, main.vmmr8[0].time_diff[7], DATA16);

//VMMR0 extended ts 
//SIGNAL(VMMR1T1, main.vmmr8[0].time_ext, DATA16);
//SIGNAL(NO_INDEX_LIST: VMMR1T1);

//VMMR1 energies
SIGNAL(ZERO_SUPPRESS_MULTI(20): VMMR2_MMR1_E1);
SIGNAL(VMMR2_MMR1_E1  , main.vmmr8[1].data[0][0],
       VMMR2_MMR1_E128, main.vmmr8[1].data[0][127], DATA12);
SIGNAL(VMMR2_MMR2_E1  , main.vmmr8[1].data[1][0],
       VMMR2_MMR2_E128, main.vmmr8[1].data[1][127], DATA12);
SIGNAL(VMMR2_MMR3_E1  , main.vmmr8[1].data[2][0],
       VMMR2_MMR3_E128, main.vmmr8[1].data[2][127], DATA12);
SIGNAL(VMMR2_MMR4_E1  , main.vmmr8[1].data[3][0],
       VMMR2_MMR4_E128, main.vmmr8[1].data[3][127], DATA12);
SIGNAL(VMMR2_MMR5_E1  , main.vmmr8[1].data[4][0],
       VMMR2_MMR5_E128, main.vmmr8[1].data[4][127], DATA12);
SIGNAL(VMMR2_MMR6_E1  , main.vmmr8[1].data[5][0],
       VMMR2_MMR6_E128, main.vmmr8[1].data[5][127], DATA12);
SIGNAL(VMMR2_MMR7_E1  , main.vmmr8[1].data[6][0],
       VMMR2_MMR7_E128, main.vmmr8[1].data[6][127], DATA12);
SIGNAL(VMMR2_MMR8_E1  , main.vmmr8[1].data[7][0],
       VMMR2_MMR8_E128, main.vmmr8[1].data[7][127], DATA12);

////VMMR1 deltaT
SIGNAL(ZERO_SUPPRESS: VMMR2_DT1);
SIGNAL(VMMR2_DT1, main.vmmr8[1].time_diff[0],
       VMMR2_DT8, main.vmmr8[1].time_diff[7], DATA16);
//VMMR1 extended ts
//SIGNAL(VMMR2T1, main.vmmr8[1].time_ext, DATA16);
//SIGNAL(NO_INDEX_LIST: VMMR2T2);

//MDPP energies
SIGNAL(ZERO_SUPPRESS_MULTI(20): MDPP1_E1);
SIGNAL(MDPP1_E1 , main.mdpp32.data[ 0],
       MDPP1_E32, main.mdpp32.data[31], DATA16_OVERFLOW);
//MDPP times
SIGNAL(ZERO_SUPPRESS_MULTI(20): MDPP1_T1);
SIGNAL(MDPP1_T1 , main.mdpp32.data[32],
       MDPP1_T34, main.mdpp32.data[65], DATA16_OVERFLOW);

//TDC times
SIGNAL(ZERO_SUPPRESS: TDC1);
SIGNAL(TDC1 , main.v775.data[0],
       TDC32, main.v775.data[31], DATA12_OVERFLOW);

//ADC energies
//SIGNAL(ZERO_SUPPRESS: ADC1);
SIGNAL(ADC1 , main.madc32.data[0],
       ADC32, main.madc32.data[31], DATA14);

//VSCALER counters
SIGNAL(ZERO_SUPPRESS: SCL1);
SIGNAL(SCL1 , main.vscal.data[0],
       SCL32, main.vscal.data[31], DATA32);
