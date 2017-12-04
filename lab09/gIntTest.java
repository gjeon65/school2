import java.io.*;
import static org.junit.Assert.*;
import org.junit.*;
import junit.framework.*;

public class gIntTest
{
	private gInt addT1;
	private gInt addT2;
	private gInt multT1;
	private gInt multT2;
	private gInt normT;


	protected void setUp()
	{
		addT1 = new gInt(3,4);
		addT2 = new gInt(9,16);
		multT1 = new gInt(2,8);
		multT2 = new gInt(5,3);
		normT = new gInt(3,1);
	}

	public void testAdd()
	{
		gInt addTest = new gInt(12,20);
		gInt result = addT1.add(addT2);
		assertNotNull(addTest);
		assertEquals(addTest,result);
	}

	public void testMult()
	{
		gInt multTest = new gInt(-1,2);
		gInt result = multT1.multiply(multT2);
		assertEquals(multTest,result);
		assertNotNull(multTest);
	}
	
	public void testNorm()
	{
		float normTest = 10;
		float result = normT.norm();
		assertEquals(normTest, result);
	}
	

	public static Test Suite()
	{
		return new TestSuite(gIntTest.class);
	}


	public static void main(String args[])
	{
		org.junit.runner.JUnitCore.runClasses(gIntTest.class);
	}

}
