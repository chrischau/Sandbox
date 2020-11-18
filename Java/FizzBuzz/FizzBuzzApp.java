interface FizzBuzz {
  String process(Integer n);
}

public class FizzBuzzApp implements FizzBuzz {
  final static String fizz = "fizz";
  final static String buzz = "buzz";

  public String process(Integer value) {
    if (value % 15 == 0) {
      return fizz + buzz;
    }
    else if (value % 5 == 0) {
      return buzz;
    }
    else if (value % 3 == 0) {
      return fizz;
    }
    
    return Integer.toString(value);
  }
}
