import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class TestRunner {
   public static void main(String[] args) {
      var result = JUnitCore.runClasses(Main_Tests.class);
		
      for (var failure : result.getFailures()) {
         System.out.println("Main Tests failed:");   
         System.out.println(failure.toString());
      }
		
      System.out.println("Main Tests ran successfully.");

      result = JUnitCore.runClasses(FizzBuzzApp_Tests.class);
		
      for (var failure : result.getFailures()) {
         System.out.println("FizzBuzzApp Tests failed:");   
         System.out.println(failure.toString());
      }

      System.out.println("FizzBuzzApp Tests ran successfully.");

   }
}  