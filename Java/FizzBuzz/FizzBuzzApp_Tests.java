import org.junit.Test;
import static org.junit.Assert.*;

public class FizzBuzzApp_Tests {
   @Test
	public void test_DetermineFizzBuzz_15() {
      var fizzbuzz = new FizzBuzzApp();
      var result = fizzbuzz.process(15);
      assertEquals("fizzbuzz", result);
   }

   @Test
	public void test_DetermineFizzBuzz_5() {
      var fizzbuzz = new FizzBuzzApp();
      var result = fizzbuzz.process(5);
      assertEquals("buzz", result);
   }

   @Test
	public void test_DetermineFizzBuzz_3() {
      var fizzbuzz = new FizzBuzzApp();
      var result = fizzbuzz.process(3);      
      assertEquals("fizz", result);
   }

   @Test
	public void test_DetermineFizzBuzz_15_multiples() {
      var fizzbuzz = new FizzBuzzApp();
      var result = fizzbuzz.process(15 * 2);      
      assertEquals("fizzbuzz", result);
   }

   @Test
	public void test_DetermineFizzBuzz_5_multiples() {
      var fizzbuzz = new FizzBuzzApp();
      var result = fizzbuzz.process(5 * 4);
      assertEquals("buzz", result);
   }

   @Test
	public void test_DetermineFizzBuzz_3_multiples() {
      var fizzbuzz = new FizzBuzzApp();
      var result = fizzbuzz.process(3 * 3);
      assertEquals("fizz", result);
   }

   @Test
	public void test_DetermineFizzBuzz_with_other_numbers_return_as_strings() {
      var fizzbuzz = new FizzBuzzApp();
      var result = fizzbuzz.process(19);
      assertEquals("19", result);

      result = fizzbuzz.process(1);
      assertEquals("1", result);

      result = fizzbuzz.process(77);
      assertEquals("77", result);
   }
}