#include <stdlib.h>
#include <string.h>
#include <stdio.h>
int main(char* argv) {
    char * flag = "utctf{plaintext_str1ngs_aRe_b3St_Str1ngs}";
    char buf[256];
    puts("enter the flag:");
    fgets(buf,256,stdin);
    if (strlen(buf)!=strlen(flag)+1){
   	 puts("try again");
   	 return 0;
    }
    if (strncmp(buf,flag,strlen(flag)) == 0)
        puts("correct!");
    else
        puts("try again!");
    return 0;
}
