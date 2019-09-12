#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv) {
  int code = rand();
  int balance = 9000;
  int prices[] = {0, 1000, 9001};

  while (1) {
    printf("%s", "##################################\n\n");
    printf("%s", "Welcome to the Fortnite Item Shop! Where dreams are made and bank accounts are destroyed.\n");
    printf("Your balance is: %d V-Bucks\n\n", balance);

    printf("%s", "What would you like to buy?\n");
    printf("%s", "(1) - Rare outfit, 1000 V-Bucks\n");
    printf("%s", "(2) - Legendary outfit, 9001 V-Bucks\n");

    int choice = 0;
    int items_read = scanf("%d", &choice);
    while ((getchar()) != '\n');
    if (items_read != 1 || (choice != 1 && choice != 2)) {
      printf("Choose either 1 or 2, you dense no-skin.\n\n");
      continue;
    }

    printf("%s", "How many would you like to buy?\n");

    int quantity = 0;
    items_read = scanf("%d", &quantity);
    while ((getchar()) != '\n');
    if (items_read != 1) {
      printf("That's not a number. Try again.\n\n");
      continue;
    }

    if (quantity < 1) {
      printf("You can't less than one, nice try.\n\n");
      continue;
    }

    int new_balance = balance - prices[choice] * quantity;
    if (new_balance < 0) {
      printf("You need %d more V-Bucks. Maybe if you actually won a game for once...\n\n", -1 * new_balance);
      continue;
    }

    balance = new_balance;
    if (choice == 1) {
      printf("%s", "I guess rare outfits are better than nothing, but I'm not impressed.\n\n");
    } else {
      printf("%s", "Congrats on your new purchase! I got you a little something extra, too:\n");
      printf("%s", "utflag{1f_0n1y_i_us3d_pyth0n}\n");
      return 0;
    }
  }

}
