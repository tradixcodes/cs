package intro_to_oop;
public class examples {
    static int age = 19;
    /*
    * This age will be used through out the class
    * If a variable is declared and not assigned a value Java will automatically assign 0 to the variable
    * The main method can only use static data types, try using int age instead
    * This class thin is wierd but I'll get the hang of it
    */
    public static void main(String[] args) {
        /*
         * The are a few different types of print out functions like in c
         * Remember putchar(), puts(), and printf()
         * In Java, we have System.out.print(), System.out.println(), System.out.printf(),
         * System.out.format() and System.out.write()
         */
        System.out.print("Hello, World\n");
        // System.out.print() prints the text without a newline character.
        System.out.println("I am " + age + " years old.");
        //System.out.println() print the text with a newline character; Somehow similar to puts()
        System.out.printf("I am %d years old.\n", age);
        // System.out.printf() allows you to format the output using format specifiers, also no '\n'
        // Similar to printf()
        double price = 19.987;
        System.out.format("The price is $%.2f\n", price);
        //System.out.format() is used for formatted output. It actually rounds off to the specified format
        System.out.write('A');
        System.out.write('\n');
        System.out.write(65); //Thought it uses ASCII values like C
        // System.out.write() is exactly like putchar(). It prints out a single character

    }
}