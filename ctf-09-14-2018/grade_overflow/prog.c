// gcc -m32 -fno-stack-protector -o prog -z execstack prog.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct {
	char username[20];
	char password[16];
} Login;

char password[] = "follow_@wtfsper";

int check_password(Login *login) {

	int result = 0;
	char buff[16];

	printf("password: ");
	scanf("%s", buff);

	strcpy(login->password, buff);
	if(strncmp(buff, password, sizeof(password)) == 0){
		result = 1;
	}

	return result;	


}

int main(int argc, char** argv) {
	Login l;

	setbuf(stdout, NULL);
	printf("*****************************************************************\n");
	printf("*                WELCOME TO UNIVERSITY OF TEXAS(S)              *\n");
	printf("*                  GRADE REPORT SYSTEM - 3.2.1                  *\n");
	printf("*                                                               *\n");
	printf("*                      PLEASE LOGIN TO                          *\n");
	printf("*                       ACCESS GRADES                           *\n");
	printf("*****************************************************************\n");

	fflush(stdout);
	printf("username: ");

	scanf("%20s", l.username);
	int auth = check_password(&l);
	if (auth == 0) {
		printf("auth failed :( \n");
		return 0;
	} else if (auth == 1) {
		printf("Here are the grades! \n");
		FILE *fptr; 
		char c;
		// Open file 
		fptr = fopen("grades.txt", "r"); 
		if (fptr == NULL) 
		{ 
			printf("Cannot open file \n"); 
			exit(0); 
		} 

		// Read contents from file 
		c = fgetc(fptr); 
		while (c != EOF) 
		{ 
			printf ("%c", c); 
			c = fgetc(fptr); 
		} 

		fclose(fptr); 
	} else if (auth == 2) {
		FILE *fptr; 
		char c;
		// Open file 
		fptr = fopen("flag", "r"); 
		if (fptr == NULL) 
		{ 
			printf("Cannot open file \n"); 
			exit(0); 
		} 

		// Read contents from file 
		c = fgetc(fptr); 
		while (c != EOF) 
		{ 
			printf ("%c", c); 
			c = fgetc(fptr); 
		} 

		fclose(fptr); 
	}

	return 0;
}
