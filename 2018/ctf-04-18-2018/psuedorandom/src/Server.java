import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;

public class Server implements Runnable {
    Socket csocket;
    Server(Socket csocket) {
        this.csocket = csocket;
    }
    public static void main(String args[]) throws Exception {
        ServerSocket ssock = new ServerSocket(4444);
        System.out.println("Listening");

        while (true) {
            Socket sock = ssock.accept();
            System.out.println("Connected");
            new Thread(new Server(sock)).start();
        }
    }

    public void writeOutput(PrintStream stream, String text) {
        stream.println(text);
    }

    public void run() {
        try {
            Random random = new Random();
            PrintStream pstream = new PrintStream(csocket.getOutputStream());
            writeOutput(pstream, "Welcome to the lottery! This server and lottery system was brought to you by " +
                    "the Oracle Corporation.");
            BufferedReader in = new BufferedReader(new InputStreamReader(csocket.getInputStream()));
            for (int i = 0; i < 5; i++) {
                writeOutput(pstream, "Enter a number between -2147483648 and 2147483647:");
                String line = in.readLine();
                int lotteryNumber = random.nextInt();
                writeOutput(pstream, "Your guess was: " + line);
                try {
                    int guess = Integer.parseInt(line);
                    if (guess == lotteryNumber) {
                        writeOutput(pstream, "Correct guess! Your flag is utflag{java_random_needs_improvement}");
                        csocket.close();
                    } else {
                        writeOutput(pstream,"Bad guess! The correct lottery number was " + lotteryNumber);
                    }
                } catch (Exception e) {
                    writeOutput(pstream, "Bad input!");
                    csocket.close();
                }
            }
            writeOutput(pstream, "You're out of guesses! Thanks for playing the lottery.");
            csocket.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
