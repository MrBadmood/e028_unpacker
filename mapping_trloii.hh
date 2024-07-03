SIGNAL(TPAT1, main.tpat.tpat, DATA16);
SIGNAL(NO_INDEX_LIST: TPAT170);

/* Trigger logic lmu */
SIGNAL(TRLORAW_MAIN_1 , main.lmu.before_lmu     [ 0],
       TRLORAW_MAIN_16, main.lmu.before_lmu     [15], DATA32);
SIGNAL(TRLOBDT_MAIN_1 , main.lmu.before_dt      [ 0],
       TRLOBDT_MAIN_16, main.lmu.before_dt      [15], DATA32);
SIGNAL(TRLOADT_MAIN_1 , main.lmu.after_dt       [ 0],
       TRLOADT_MAIN_16, main.lmu.after_dt       [15], DATA32);
SIGNAL(TRLOARD_MAIN_1 , main.lmu.after_reduction[ 0],
       TRLOARD_MAIN_16, main.lmu.after_reduction[15], DATA32);
