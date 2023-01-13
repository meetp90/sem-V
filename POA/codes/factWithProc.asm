DATA SEGMENT
    NUM DB 05H
DATA ENDS

CODE SEGMENT
    ASSUME DS:DATA,CS:CODE
start:
    MOV AX,DATA
    MOV DS,AX
    MOV AL,NUM
    MOV CL,01H
    CALL FACT
    INT 21H

    FACT PROC NEAR
    looper:
        DEC NUM
        MUL NUM
        CMP NUM,CL
        JNZ looper
        ret
    ENDP
END start
CODE ENDS
