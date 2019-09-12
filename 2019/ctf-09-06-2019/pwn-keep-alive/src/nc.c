#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int do_auth(char * pass);
void get_nums();
void get_flag();

int main() {
  printf("This challenge is to teach you the basics of pwning with netcat.\n");
  printf("To send input to netcat you can use a pipe on linux\n");
  printf("For example: python3 -c \"print(\'a\'*40)\" | nc ip port\n");
  printf("This sends 40 a's to the server on some port.\n");
  printf("Send me the integers [0,5000) each on a new line to spawn a shell.\n\n");
  get_nums();
  return 1;
}

void get_nums() {
  for(int i = 0; i < 5000; i++) {
    char str[50];
    fgets(str, 50, stdin);
    int x = 0;
    sscanf(str, "%d", &x);
    if(x != i)
      return;
  }
  printf("Yay you did input and spawned a shell on the target server!!\n");
  printf("But why did nothing happen??\n");
  printf("The command piped to netcat (python3 ...) ran out of output, so the connection to the server was killed.\n");
  printf("Try (python3 -c \"print(\'a\'*40)\"; cat -) | nc ip port\n");
  printf("The command cat - just writes anything received on stdin to stdout.\n");
  printf("This allows you to interact with the shell\n");
  get_flag();
}

void get_flag() {
  // replace the current process with a shell.
  char*  args[2] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}
