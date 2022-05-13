//BaekJoon10039
//작성자 : yazbyz
//20200603

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_10039 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] price = new int[5];
		int cheapest = 0;
		int total = 0;
		
		for(int i = 0; i < 5 ; i++)
		{ 
			price[i] = Integer.parseInt(br.readLine());
			
			//품목별 가격기준 정하기
			if(i == 0)
			{
				cheapest = price[0];
			} else if(i == 3) {
				total += cheapest;
				cheapest = price[3];
			}
			
			//가장 저렴한것 찾기
			if(cheapest > price[i])
			{
				cheapest = price[i];
			}			
		}
		total += cheapest;
		total -= 50;
			
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(total + "\n");
		bw.flush();
		bw.close();
	}
	
}
