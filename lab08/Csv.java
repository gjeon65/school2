import java.io.*;
import java.util.*;

public class Csv
{
	public static void main(String[] args)
	{
		try
		{
			FileReader reader = new FileReader(new File("test.csv"));
			Scanner scan = new Scanner(reader);
			scan.useDelimiter(",");
			while(scan.hasNext())
			{
				System.out.println("'"+scan.next()+"'");
			}
			scan.close();
		} catch (FileNotFoundException e)
		{
			System.out.println("Error reading file");
			e.printStackTrace();
		}

	}
}
