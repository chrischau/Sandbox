public class Main {
  final static String fizz = "fizz";
  final static String buzz = "buzz";

  public static void main(String[] args) {
    int maxIteration = ParseArgument(args);

    var fizzbuzz = new FizzBuzzApp();

    for(int iteration = 1; iteration <= maxIteration; iteration++) {
      System.out.println(fizzbuzz.process(iteration));      
    }
  }

  public static int ParseArgument(String[] args) {
    if (args.length > 0 && TryParseInt(args[0])) {
      int parsedValue = Integer.parseInt(args[0]);
      
      if (parsedValue > 1) { 
        return parsedValue; 
      }
    }

    return 100;
  }

  public static boolean TryParseInt(String value) {  
    try {  
        Integer.parseInt(value);  
        return true;  
     } catch (NumberFormatException e) {  
        return false;  
     }  
  }  
}
