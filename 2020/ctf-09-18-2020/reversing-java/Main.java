import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner fin = new Scanner(System.in);
        System.out.print("What's the password? ");

        String s = fin.next();

        int[] flag = new int[] {172, 171, 157, 163, 152, 158, 178, 159, 152, 154, 159, 160, 170, 167, 160, 165, 150, 159, 152, 154, 159, 160, 174, 160, 165, 180};

        if(flag.length != s.length()) {
            System.out.println("Try again!");
            return;
        }

        for(int i = 0; i < s.length(); i++){
            if((s.charAt(i) + 55) % 256 != flag[i]) {
                System.out.println("Try again!");
                return;
            }
        }

        System.out.println("good password");
    }
}