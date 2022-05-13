//BaekJoon2753
//ÀÛ¼ºÀÚ : yazbyz
//20200530

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BJ_2753 {

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int year = 0;
		
		do{
			year = Integer.parseInt(br.readLine());
		}while(year < 1 || year > 4000);
		
		if(year % 4 == 0 && year % 100 != 0)
		{
			System.out.println("1");
		} else if(year % 400 == 0) {
			System.out.println("1");
		} else {
			System.out.println("0");
		}

	}

}
