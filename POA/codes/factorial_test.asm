DATA SEGMENT
A DB 5
FACT DB ?
DATA ENDS
CODE SEGMENT
    ASSUME CS:CODE, DS:DATA
start:
    MOV AX,DATA
    MOV DS,AX
    MOV AH,00
    MOV AL,A
looper:
    DEC A
    MUL A
    MOV CL,A
    CMP CL,01
    JNZ looper
    MOV FACT,AL
CODE ENDS
END START
