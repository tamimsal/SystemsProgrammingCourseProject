<-Label--> <-OPCode-> <----Operand----> <---------Comment------------>
SUM        START      0
FIRST      LDX        ZERO
           LDA        ZERO
LOOP       ADD        TABLE,X
           TIX        COUNT
           JLT        LOOP
           STA        TOTAL
           RSUB       
TABLE      RESW       128
COUNT      RESW       1
ZERO       WORD       0
TOTAL      RESW       1
           END        FIRST