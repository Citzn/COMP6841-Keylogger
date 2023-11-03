#include <winternl.h>
#include <windows.h>
#include <stdio.h>


extern BYTE checkDebug(void);

int main(void) {

     if (checkDebug() != 0) {
          printf("Average program behavior\n");

          return 0;
     }


     printf("Malware payload activated mahahahahah!!!\n");

    return 0;
}