#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main(int argc, char** argv) {
    printf("Does this work?\n");
    int sock = socket(AF_INET,SOCK_STREAM,0);
    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(12213);
    server_addr.sin_addr.s_addr = inet_addr("73.232.225.55");
    connect(sock, (struct sockaddr*)&server_addr, sizeof(server_addr));
    send(sock, argv[1], strlen(argv[1]), 0);
    close(sock);
    return 0;
}
