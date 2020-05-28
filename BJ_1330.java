import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BJ_1330 {
    public static void main(String []args) throws Exception { 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int A, B;
        
        String s = br.readLine();
        
        String array[] = s.split(" ");
        
        A = Integer.parseInt(array[0]);
        B = Integer.parseInt(array[1]);

        
        if(A > B)
        {
        	System.out.println(">");
        } else if(A == B) {
        	System.out.println("==");
        } else {
        	System.out.println("<");
        }
       
    }
}