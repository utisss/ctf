#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int ** board;
int total_wins = 0;

#define HEIGHT 6
#define WIDTH 7

#define PLAYER -1
#define COMPUTER 1

int play(int x, int role) {
    if(x < 0 || x >= WIDTH){
        if (role == PLAYER) printf("Invalid move.\n");
        return -1;
    }

    int y;
    for(y = 0; y < HEIGHT; y++) {
        if(!board[y][x]){
            break;
        }
    }

    if(y == HEIGHT) {
        if(role == PLAYER) printf("Column is full\n");
        return -1;
    }

    board[y][x] = role;
    return 0;
}

int check_win() {
    for(int i = 0; i < HEIGHT; i++) {
        for(int j = 0; j < WIDTH; j++) {

            //check column
            int count = 0;
            for(int k = 0; k < 4; k++) {
                if(i + k >= HEIGHT) continue;
                count += board[i + k][j];
            }

            if(count == 4 * PLAYER) {
                return PLAYER;
            }else if(count == 4 * COMPUTER) {
                return COMPUTER;
            }

            //check row
            count = 0;
            for(int k = 0; k < 4; k++) {
                if(j + k >= WIDTH) continue;
                count += board[i][j + k];
            }

            if(count == 4 * PLAYER) {
                return PLAYER;
            }else if(count == 4 * COMPUTER) {
                return COMPUTER;
            }

            //check diagonal
            count = 0;
            for(int k = 0; k < 4; k++) {
                if(i + k >= HEIGHT) continue;
                if(j + k >= WIDTH) continue;
                count += board[i + k][j + k];
            }

            if(count == 4 * PLAYER) {
                return PLAYER;
            }else if(count == 4 * COMPUTER) {
                return COMPUTER;
            }
        }
    }
    return 0;
}

void game() {

    printf("**** New game ****\n");
    
    board = (int **) malloc(HEIGHT * sizeof(int*));
    for(int i = 0; i < HEIGHT; i++){
        board[i] = (int*)calloc(WIDTH, sizeof(int));
    }

    int total_moves = 0;

    while(total_moves < 42) {
        int x, y;
        printf("Make a move: ");
        scanf("%d", &x);

        if(play(x, PLAYER) != 0) {
            continue;
        }

        if(check_win() == PLAYER) {
            total_wins++;
            if(total_wins == 7) {
                system("/bin/cat /flag.txt");
                exit(0);
            }
            printf("You win!\n");
            break;
        }

        int move;

        do {
            move = x - 1 + (rand() % 3);
        }while(play(move, COMPUTER) != 0);

        printf("Computer plays %d\n", move);

        if(check_win() == COMPUTER) {
            printf("Computer wins!\n");
            exit(0);
            break;
        }
    }
}

int main() {
    srand(time(NULL));
    while(1) {
        game();
    }
}