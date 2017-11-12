import java.util.Date;

public class prob4 {
	public static void main( String [] args)
	{
		
		int i = Integer.parseInt(args[0]);
		Date currentTime = new Date();
		long milliSec = currentTime.getTime();
		
		switch (i)
		{
		case 0:
			System.out.print("milliseconds since January 1, 1970: " + milliSec + " milliseconds");
			break;
		case 1:
			System.out.print("seconds since January 1, 1970: " + milliSec/1000 + " seconds");
			break;
		case 2:
			System.out.print("days since January 1, 1970: " + milliSec/(1000*3600*24) + " days");
			break;
		case 3:
			System.out.print("Current date and time: " + currentTime.toString());
			break;
		}
		
	}
}
