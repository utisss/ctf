#include <stdio.h>

void pog() {
  printf("flag in stream: utflag{thank_for_fixing_stream}\n");
}

void fix_stream() {
  char streamername[14];
  printf("Type in chat to try to fix stream!\n");
  gets(streamername);
  printf("Chat> %s!\n",streamername);
}

int main(int argc) {
  fix_stream();
  return 0;
}
