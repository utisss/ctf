import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;
import java.util.Scanner;

public class Server implements Runnable {
	Socket csocket;
	Server(Socket csocket) {
		this.csocket = csocket;
	}
	public static void main(String args[]) throws Exception {
		ServerSocket ssock = new ServerSocket(1234);
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

	public String readMessage() {
		Scanner scanner = null;
		try {
			scanner = new Scanner(new File("message.txt"));
			String message = "";
			while (scanner.hasNextLine()) {
				message += scanner.nextLine();
			}
			return message;
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return "";
	}

	public String getKey(String message) {
		Random random = new Random(182128);
		String key = "";
		for (int i = 0; i < message.length(); i++) {
			key += (char) random.nextInt(26) + 65;
		}
		return key;
	}

	public String encrypt(String message) {
		String output = "";
		String key = getKey(message);
		for (int i = 0; i < message.length(); i++) {
			char character = message.charAt(i);
			int keyChar = (int) key.charAt(i);
			int result = (200 - (int) character);
			result = result >> 2;
			result = result ^ keyChar;
			output += String.valueOf(result);
			output += " ";
		}
		return output;
	}

	public void run() {
		try {
			PrintStream pstream = new PrintStream(csocket.getOutputStream());
			writeOutput(pstream, "Established connection to flag server!");

			String message = readMessage();
			String encrypted = encrypt(message);

			writeOutput(pstream, encrypted);

			csocket.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
