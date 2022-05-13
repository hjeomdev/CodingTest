//BaekJoon10039
//�ۼ��� : yazbyz
//20200603

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ10039 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] price = new int[5];
		int cheapest = 0;
		int total = 0;
		
		for(int i = 0; i < 5 ; i++)
		{ 
			price[i] = Integer.parseInt(br.readLine());
			
			//ǰ�� ���ݱ��� ���ϱ�
			if(i == 0)
			{
				cheapest = price[0];
			} else if(i == 3) {
				total += cheapest;
				cheapest = price[3];
			}
			
			//���� �����Ѱ� ã��
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
