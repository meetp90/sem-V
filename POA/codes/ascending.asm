data segment
arr db 0x89, 0x45, 0x54, 0x10, 0x23 
data ends

code segment
    assume cs:code, ds:data
start:
    mov ax, data 
    mov ds, ax
    mov ch, 0x04 
    loop_1:
        mov cl, 0x04 
        lea si, arr
    loop_2:
        mov al, [si]
        mov bl, [si + 1] 
        cmp al, bl
        jc cleanup 
        mov dl, [si + 1] 
        xchg [si], dl 
        mov [si + 1], dl
    cleanup: 
        inc si
        dec cl
        jnz loop_2 
        dec ch
        jnz loop_1 
    code ends
end start
