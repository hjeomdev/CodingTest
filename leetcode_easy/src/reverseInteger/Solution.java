package reverseInteger;

class Solution {
	public int reverse(int x) {

		/*
		// < 내 코드 전체 요약 : x를 문자열로 형변환해서 이용 >
		// 음수인지 확인
		boolean minus = false;
		if(x < 0) {
			x *= -1;
			minus = true;
		}

		// 문자열로 형변환 후 자르기
		String[] result = Integer.toString(x).split("");

		// 거꾸로 조합
		String temp = "";
		for(int i = result.length - 1; i >= 0; i--) {
			temp += result[i];
		}

		// int로 형변환
		// java.lang.NumberFormatException: For input string: "9646324351" 예외 발생 시 0 반환
		int answer;
		try {
			answer = Integer.parseInt(temp);
		} catch (Exception e) {
			return 0;
		}

		// 음수 표현
		if(minus) {
			answer *= -1;
		}

		return answer;
		*/

		// another code from leetcode 
		int rev = 0;
		while (x != 0) {
			int pop = x % 10;
			x /= 10;
			if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
			if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
			rev = rev * 10 + pop;
		}
		return rev;
	}
}
