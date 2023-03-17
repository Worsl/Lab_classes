package network;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

public class Rfc865UdpClient {
	public static void main(String[] argv) throws SocketException, UnknownHostException {
		// 1. Open UDP Socket
		DatagramSocket socket = new DatagramSocket();
		InetAddress address = InetAddress.getByName("hwlab1.scse.ntu.edu.sg"); // quote of the day server 

		//hwlab1.scse.ntu.edu.sg
		byte[] buffer = new byte[512];
		
		try {
			// 2. Send UDP Request to Server
			String message = new String("Cheng, LAB A58");
			buffer = message.getBytes();
			DatagramPacket request = new DatagramPacket(buffer, buffer.length, address, 17); // QOTD port 17
			socket.send(request);
			
			// 3. Receive UDP Reply from Server

			buffer = new byte[512];
			DatagramPacket reply = new DatagramPacket(buffer, buffer.length);
			socket.receive(reply);

            
			String received = new String(reply.getData(), 0, reply.getLength());
			System.out.println(received);
		} catch (IOException e) {} 
		
		System.out.println("Closing Socket...");
		socket.close();
	}
}