#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <errno.h>

const char EMPTY = ' ';
const char X = 'X';
const char O = 'O';

bool get_move(char *buf, size_t buf_size) {
  printf("Enter a move: ");
  char *result = fgets(buf, buf_size, stdin);
  if (buf[buf_size-2] != 0 && buf[buf_size-1] == 0) {
    printf("Your string was too long! Please try again.\n");
    return false;
  }
  return result != NULL;
}

bool parse_move(char *buf, long *move) {
  errno = 0;
  char *end;
  *move = strtol(buf, &end, 10);
  if (buf == end) {
    // no digits entered
    printf("Invalid input! Please try again.\n");
    return false;
  }

  if (errno == ERANGE) {
    // range exceeded
    printf("That number was too large! Please try again.\n");
    return false;
  }

  if (*move < 0) {
    printf("Numbers must be greater than zero!\n");
    return false;
  }

  return true;
}

void print_board(char *board) {
  size_t i = 0;
  size_t r, c;
  printf("---|---|---\n");
  while (board[i]) {
    printf(" %c", board[i]);
    r = i / 3;
    c = i % 3;
    if (c < 2) {
      printf(" |");
    } else {
      printf("\n---|---|---\n");
    }
    i += 1;
  }
}

bool check_win(char *board) {
  size_t board_len = strlen(board);
  // check for row wins
  for (size_t i = 0; i < board_len-2; i += 3) {
    if (board[i] != EMPTY && board[i] == board[i+1] && board[i+1] == board[i+2]) {
      return true;
    }
  }
  // check for column wins
  for (size_t i = 0; i < board_len-6; i++) {
    if (board[i] != EMPTY && board[i] == board[i+3] && board[i+3] == board[i+6]) {
      return true;
    }
  }
  // check for diagonal wins
  return (board[0] != EMPTY && board[0] == board[4] && board[4] == board[8]) ||
         (board[2] != EMPTY && board[2] == board[4] && board[4] == board[6]);
}

bool check_tie(char *board) {
  size_t total = 0;
  for (size_t i = 0; i < 9; i++) {
    if (board[i] != EMPTY) {
      total++;
    }
  }
  return total == 9;
}

long get_ai_move(char *board) {
  for (size_t i = 0; i < 9; i++) {
    if (board[i] == EMPTY) {
      // simulate a move from the player
      char board_copy[10];
      strcpy(board_copy, board);
      board_copy[i] = X;
      // if the move ends the game, we should probably prevent it
      if (check_win(board_copy)) {
        return i;
      }
    }
  }
  long move_priority[] = {4, 0, 2, 6, 8, 1, 3, 5, 7};
  for (size_t i = 0; i < 9; i++) {
    size_t index = move_priority[i];
    if (board[index] == EMPTY) {
      return index;
    }
  }
  printf("No possible moves!\n");
  return -1;
}

int main(int argc, char** argv) {
  size_t buf_size = 16;
  char buf[buf_size];
  char *sample_board = "012345678";
  char board[10]; 
  memset(board, EMPTY, 9);
  board[10] = 0;

  printf("Welcome to the galactic man versus machine Tic-Tac-Toe showdown!\n");
  printf("If you can beat me, a galaxy brain AI, I will give you the flag.\n");
  printf("This board shows you which numbers map to which spots!\n");
  print_board(sample_board);
  while (get_move(buf, buf_size)) {
    // parse the move
    long move;
    if (!parse_move(buf, &move)) {
      continue;
    }

    // check that the move is legal
    if (board[move] == X || board[move] == O) {
      printf("Sorry, that space is taken already! Please try again.\n");
      continue;
    }

    // put the move on the board and print it
    printf("You entered %ld.\n", move);
    board[move] = X;
    print_board(board);

    // check for a win
    if (check_win(board)) {
      printf("You won! Congrats!\n");
      printf("utflag{gam3_th3ory_0pt1mal}\n");
      break;
    } else if (check_tie(board)) {
      printf("Tie game! Better luck next time.\n");
      break;
    }

    // take the AI's turn
    long ai_move = get_ai_move(board);
    printf("AI move %ld\n", ai_move);
    board[ai_move] = O;
    print_board(board);
    if (check_win(board)) {
      printf("The AI won :( Better luck next time!\n");
      break;
    }
  }
  return 0;
}
