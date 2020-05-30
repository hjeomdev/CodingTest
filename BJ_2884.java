//20200530 BaekJoon2753
//ÀÛ¼ºÀÚ : yazbyz

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BJ_2884 {
	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int H, M;
		String h, m;
		
		String HAndM = br.readLine();
		 
		String array[] = HAndM.split(" ");
		
	    H = Integer.parseInt(array[0]);
	    M = Integer.parseInt(array[1]);

		if(M < 45) {
			H -= 1;
			M += 60;
			
			if(H < 1) {
				H = 23;
			}	
		}
		M -= 45;
		
		h = Integer.toString(H);
		m = Integer.toString(M);
		if(M == 0) {
			m = "00";
		}
		
		System.out.println(h + " " + m);
		
		
	}
}
