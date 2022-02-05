import java.util.*;

public class Main {
    static int[] flag = new int[] {234, 232, 204, 216, 194, 206, 246, 232, 208, 202, 190, 238, 222, 228, 200, 190, 196, 202, 194, 220, 230, 190, 232, 222, 232, 194, 216, 216, 242, 190, 230, 232, 222, 224, 224, 202, 200, 190, 216, 222, 222, 214, 210, 220, 206, 190, 216, 210, 214, 202, 190, 194, 190, 238, 222, 228, 200, 190, 212, 234, 230, 232, 190, 220, 222, 238, 250};
    public static void main(String[] args) {
        Scanner fin = new Scanner(System.in);

        System.out.print("Guess the flag: ");
        
        String guess = fin.next();

        if(guess.length() != flag.length) {
            System.out.println("Wrong flag");
            System.exit(0);
        }

        for(int i = 0; i < flag.length; i++) {
            if(guess.charAt(i) * 2 != flag[i]) {
                System.out.println("Wrong flag");
                System.exit(0);
            }
        }

        System.out.println("Correct flag!");
    }
}