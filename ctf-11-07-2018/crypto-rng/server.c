#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv) {
  initstate(time(0), malloc(8), 8);

  int code = rand();
  int guess = 0;

  while (1) {
    printf("%s", "Pwease entew the vewification code sent to youw emaiw: asper@utexas.edu: ");
    guess = 0;
    int items_read = scanf("%d", &guess);
    if (items_read != 1) {
      printf("BOOO that's not a number\n");
      return 0;
    }
    if (guess == code) {
      printf("%s", "Vewification successfuw. Youw tempowawy passwowd is: utflag{someone_told_me_rand()_was_cryptographically_secure}\n");
      return 0;
    } else {
      printf("Sowwy, that's incowwect. The actuaw code was %d. Genyewating nyew secuwe wandom code...\n\n", code);
      code = rand();
    }
  }

}
