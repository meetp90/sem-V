data segment
arr db 0x77, 0x27, 0x99, 0x80 
data ends

code segment
assume cs:code, ds:data
start:
    mov ax, data 
    mov ds, ax 
    lea si, arr 
    mov cl, 0x03 
    mov al, [si] 
    inc si
loop_:
    mov bl, [si] 
    cmp al, bl 
    jc cleanup 
    mov al, bl
cleanup: 
    inc si
    dec cl 
    jnz loop_
code ends
end start
