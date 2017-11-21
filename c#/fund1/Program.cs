using System;

namespace fund1
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i= 1; i<=255; i=i+1){
                Console.WriteLine(i);
            }
            for (int i= 1; i<=100; i=i+1){
                if (i%3 == 0 && i%5 !=0){
                    Console.WriteLine(i);
                }
                else if(i%5 == 0 && i%3 !=0){
                    Console.WriteLine(i);
                }
            }
             for (int i= 1; i<=100; i=i+1){
                if (i%3 == 0 && i%5 !=0){
                    Console.WriteLine("Fizz");
                }
                else if(i%5 == 0 && i%3 !=0){
                    Console.WriteLine("Buzz");
                }
                else if(i%5 == 0 && i%3 ==0){
                    Console.WriteLine("FizzBuzz");

               }
           }
        }
    }
}
