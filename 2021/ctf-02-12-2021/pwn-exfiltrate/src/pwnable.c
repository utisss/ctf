#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>


#define BUF_SIZE 1024
int main(int argc, char** argv) {
    char flag[50];
    FILE* flag_file = fopen("/home/exfiltrate/flag.txt", "r");
    fgets(flag,50,flag_file);

    int fd = memfd_create("prog", 0);

    int num_read;
    do {
        char buf[BUF_SIZE];
        num_read = read(0,buf,BUF_SIZE);
        int num_written = write(fd,buf,num_read);
    } while(num_read == BUF_SIZE);

    close(1);

    const char * const other_argv[] = {"prog", flag, NULL};
    const char * const envp[] = {NULL};
    fexecve(fd, (char * const *) other_argv, (char * const *) envp);
}
