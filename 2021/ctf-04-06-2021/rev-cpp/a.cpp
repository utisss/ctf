#include <string>
#include <iostream>

const char* flag = "_^LFKMQI\x01\x01uCYu]KIASuFEFW";

struct password_struct {
    std::string input;
    int shift;
};

bool check_password(password_struct & pass) {
    const char* internal = pass.input.c_str();
    int n = pass.input.length();
    if(n != 24) {
        return false;
    }
    for(int i = 0; i < n; i++) {
        if(flag[i] != (internal[i] ^ pass.shift)) {
            return false;
        }
    }
    return true;
}

int main() {
    password_struct password_check;
    std::cout << "What's the password?\n";
    std::cin >> password_check.input;

    std::cout << "Well, I bet you don't know the secret number\n";
    std::cin >> password_check.shift;

    if(check_password(password_check)) {
        std::cout << "Hey! How did you know that!\n";
    }
    else {
        std::cout << "See? I told you that you didn't know the number!\n";
    }
    return 0;
}
