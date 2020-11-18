import org.junit.Test;
import static org.junit.Assert.*;

public class Main_Tests {
   @Test
	public void test_ParseArguments_with_no_arguments() {
      var arguments = new String[] {};
      var result = Main.ParseArgument(arguments);
      assertEquals(100, result);
   }

   @Test
	public void test_ParseArguments_with_1_argument() {
      var arguments = new String[] { "20" };
      var result = Main.ParseArgument(arguments);
      assertEquals(20, result);
   }

   @Test
	public void test_ParseArguments_with_multiple_integer_argument() {
      var arguments = new String[] { "20", "100" };
      var result = Main.ParseArgument(arguments);
      assertEquals(20, result);
   }

   @Test
	public void test_ParseArguments_with_multiple_types_of_argument() {
      var arguments = new String[] { "20", "abc" };
      var result = Main.ParseArgument(arguments);
      assertEquals(20, result);
   }

   @Test
	public void test_ParseArguments_with_non_integer_argument() {
      var arguments = new String[] { "abc" };
      var result = Main.ParseArgument(arguments);
      assertEquals(100, result);
   }

   @Test
	public void test_ParseArguments_with_argument_of_0() {
      var arguments = new String[] { "0" };
      var result = Main.ParseArgument(arguments);
      assertEquals(100, result);
   }
   
   @Test
	public void test_ParseArguments_with_argument_of_1() {
      var arguments = new String[] { "1" };
      var result = Main.ParseArgument(arguments);
      assertEquals(100, result);
   }

   @Test
	public void test_TryParseInt_with_number() {
      var result = Main.TryParseInt("10");
      assertTrue(result);
   }

   @Test
	public void test_TryParseInt_with_non_number() {
      var result = Main.TryParseInt("aff10");
      assertFalse(result);
   }

}