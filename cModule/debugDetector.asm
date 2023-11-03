ifdef rax
else
.386
.model flat, C
endif


.code

ifdef rax

checkDebug PROC
    mov rax, qword ptr gs:[60h]
    movzx eax, byte ptr [rax + 2h]
    ret
checkDebug ENDP

endif

end