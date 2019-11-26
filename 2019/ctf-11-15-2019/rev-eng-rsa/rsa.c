#include <stdio.h>

unsigned int modpow(unsigned int b, unsigned int e, unsigned int modulus) {
	unsigned int result = 1;
	for(int i = 0; i < e; i++){
		result *= b;
		result %= modulus;
	}

	return result;
}

int main() {
	unsigned int ctext[28] = {2272, 1423, 569, 2659, 1236, 784, 2132, 1467, 184, 1236, 2389, 1467, 184, 1236, 2389, 1467, 184, 1236, 2389, 1467, 184, 1236, 2389, 2650, 1236, 2650, 1236, 1058};
	char flag[29];

	printf("Enter the flag: ");
	scanf("%28s", flag);

	for(int i = 0; i < 28; i++){
		if(modpow(flag[i], 13, 2747) != ctext[i]) {
			printf("Wrong\n");
			return -1;
		}
	}

	printf("that's a pretty cool flag\n");

	return 0;
}