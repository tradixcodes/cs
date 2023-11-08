package intro_to_oop;

public class basic_calculator {
    public static void main(String[] args) {
        double num1 = 20;
        int num2 = 19;

        System.out.println(num1 + num2);
        System.out.println(num1 - num2);
        System.out.println(num1 * num2);
        System.out.println(num1 / num2);

        String name = "Njoroge Kanyagia";
        
        for(int i = 0; i < name.length(); i++){
            char c = name.charAt(i);
            System.out.print(c);
        }
        /*
         * name.length()- return the length of the string
         * name.charAt(i)- retrieves the character of the current
         * index
         * So there is String data type in Java, but it's not 
         * primitive like in C++ neither can we use char ... []
         * like in c.
         * There is also no null termination in Java like there
         * is in C. The String data type is represented as objects
         * of the String class. So we'll be using .length(method)
         * most of the time to iterate through strings in Java.
         */
        System.out.write('\n');
        System.out.println("My name is "+ name + ".");
    }
}
