import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ_9498 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int score;
		
		do{
			score = Integer.parseInt(br.readLine());
		}while(score<0 || score>100);
		
		if(score>=90 && score<=100)
		{
			System.out.println("A");
		} else if (score>=80 && score <=89){
			System.out.println("B");
		} else if (score>=70 && score <=79){
			System.out.println("C");
		} else if (score>=60 && score <=69){
			System.out.println("D");
		} else {
			System.out.println("F");
		}
	}

}
