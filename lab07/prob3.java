public class prob3 {
	public static void main(String [] args)
	{
		
		int i = Integer.parseInt(arg[0]);
		boolean isLeapYear = false;
		if (i%4 == 0)
		{
			isLeapYear = true;
		}
		if (i%100 == 0)
		{
			isLeapYear = false;
		}
		if (i%400 == 0)
		{
			isLeapYear = false;
		}
		System.out.print("Is it a leap year? " + isLeapYear);
	}
}
