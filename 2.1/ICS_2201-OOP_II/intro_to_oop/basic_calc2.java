package intro_to_oop;
import java.util.Scanner;

public class basic_calc2 {
    /*
     * This is when i first have messy code
     * But now we'll learn to use input to get num1 and num2
     */
    public static void main(String[] args) {
        Scanner basic_calc2Scanner = new Scanner(System.in); 
        /*
         * Scanner: is a class provides methods for reading input of various types
         * scanner/basic_calc2Scanner: the name of the variable you are creating to reference the Scanner object
         * new Scanner(System.in): Specifies that the scanner should read input from the standard input
         */

        System.out.println("***************************");
        System.out.println("!Welcome to my calculator!");
        System.out.print("Enter the first number: ");
        int num1 = basic_calc2Scanner.nextInt();
        
        System.out.write('\n');
        System.out.print("Enter the second number: ");
        int num2 = basic_calc2Scanner.nextInt();
        
        System.out.write('\n');
        System.out.print("Enter the desired operation(*,/,+,-): ");
        String op = basic_calc2Scanner.next();
        
        System.out.write('\n');

        /*
         * next(): reads usually words. Stops reading when encountered with a white space
         * nextInt(): reads the next integer from input
         * nextLine(): reads the entire line of text until it encounters a newline character
         * nextDouble(): reads a double value 
         * nextLong(): reads the next long integer
         * nextFloat(): reads the next floating-point number
         * nextBoolean(): reads the next boolean value
         * nextByte(): reads the next byte value from input
         * nextShort(): reads the next short integer from input
         * Surprisingly we have to use next() and an if statement like the one below to get a char input
         */

        char operator;

        if(op.length() == 1){
             operator = op.charAt(0);
            /*
             * charAt()- is a method used to retrieve a specific character
             * at a given index within the string
             * it actually makes sense op.charAt(0)
             */
        }else{
            System.out.println("Please enter a single character!");
            return;
        }

        if(operator == '+'){
            System.out.println("The result is:");
            System.out.println(num1 + num2);
        }else if(operator == '-'){
            System.out.println("The result is:");
            System.out.println(num1 - num2);
        }else if(operator == '/'){ 
            if(num2 == 0){
                System.out.println("Division by zero!");
                return;
            }
            System.out.println(num1 / num2);
        }else if(operator == '*'){
            System.out.println("The result is:");
            System.out.println(num1 * num2);
        }else {
            System.out.println("The result is:");
            System.out.println("Invalid input");
        }

        System.out.println("Thanks for using our calculator");
        basic_calc2Scanner.close();
    }      
}
