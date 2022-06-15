import java.rmi.*;  
import java.rmi.registry.*;  
import java.rmi.registry.LocateRegistry;
public class Server{
    public static void main(String[] args) throws Exception{
        System.setProperty("java.rmi.server.hostname", "192.168.112.236");
        Addi obj = new Add();   
        Naming.rebind("rmi://0.0.0.0:1800/sono", obj);
    }
}
