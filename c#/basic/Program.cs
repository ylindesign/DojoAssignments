using System;
using System.Collections.Generic;

namespace basic
{
    class Program
    {
        static void Main(string[] args)
        {
            // Print 1-255
            // Write a program (sets of instructions) that would print all the numbers from 1 to 255.
            // for (int i = 1; i <= 255; i++)
            // {
            //     System.Console.WriteLine(i);
            // }

            // Print odd numbers between 1-255
            // Write a program (sets of instructions) that would print all the odd numbers from 1 to 255.
            // for (int i = 1; i <= 255; i++)
            // {
            //     if (i%2 == 1)
            //     {
            //         System.Console.WriteLine(i);
            //     }
            // }

            // Print Sum
            // Write a program that would print the numbers from 0 to 255 but this time, it would also print the sum of the numbers that have been printed so far. For example, your output should be something like this:
            // New number: 0 Sum: 0
            // New number: 1 Sum: 1
            // int sum = 0;
            // for (int i = 0; i <= 255; i++)
            // {
            //     sum = sum + i;
            //     System.Console.WriteLine("New number: {0} Sum: {1}", i, sum);
            // }

            // Iterating through an Array
            // Given an array X, say [1,3,5,7,9,13], write a program that would iterate through each member of the array and print each value on the screen. Being able to loop through each member of the array is extremely important.
            // int[] thisArray = {1,3,5,7,9,13};
            // for (int i = 0; i < thisArray.Length; i++)
            // {
            //     System.Console.WriteLine(thisArray[i]);
            // }

            // Find Max
            // Write a program (sets of instructions) that takes any array and prints the maximum value in the array. Your program should also work with a given array that has all negative numbers (e.g. [-3, -5, -7]), or even a mix of positive numbers, negative numbers and zero.
            // int[] thisArray = {1,3,-5,7,9,-13};
            // int max = thisArray[0];
            // for (int i = 1; i < thisArray.Length; i++)
            // {
            //     if (thisArray[i] > max)
            //     {
            //         max = thisArray[i];
            //     }
            // }
            // System.Console.WriteLine(max);

            // Get Average
            // Write a program that takes an array, and prints the AVERAGE of the values in the array. For example for an array [2, 10, 3], your program should print an average of 5. Again, make sure you come up with a simple base case and write instructions to solve that base case first, then test your instructions for other complicated cases. You can use a count function with this assignment.
            // int[] thisArray = {2, 10, 3,2};
            // double sum = 0.0;
            // double avg = 0.0;
            // for (int i = 0; i < thisArray.Length; i++)
            // {
            //     sum = sum + thisArray[i];
            // }
            // avg = sum / thisArray.Length;
            // System.Console.WriteLine(avg);

            // Array with Odd Numbers
            // Write a program that creates an array 'y' that contains all the odd numbers between 1 to 255. When the program is done, 'y' should have the value of [1, 3, 5, 7, ... 255].
            // List<int> oddList = new List<int>();
            // for(int i = 1; i <= 255; i++) {
            //     if(i % 2 == 1) {
            //         oddList.Add(i);
            //     }
            // }
            // oddList.ToArray();

            // Greater than Y
            // Write a program that takes an array and returns the number of values in that array whose value is greater than a given value y. For example, if array = [1, 3, 5, 7] and y = 3. After your program is run it will print 2 (since there are two values in the array that are greater than 3).
            // int y = 3;
            // int num = 0;
            // int[] thisArray = {1, 3, 5, 7};
            // for (int i = 0; i < thisArray.Length; i++)
            // {
            //     if (thisArray[i] > y)
            //     {
            //         num = num + 1;
            //     }
            // }
            // System.Console.WriteLine(num);

            // Square the Values
            // Given any array x, say [1, 5, 10, -2], create an algorithm (sets of instructions) that multiplies each value in the array by itself. When the program is done, the array x should have values that have been squared, say [1, 25, 100, 4].
            // int[] thisArray = {1, 5, 10, -2};
            // for (int i = 0; i < thisArray.Length; i++)
            // {
            //     thisArray[i] = thisArray[i] * thisArray[i];
            //     System.Console.WriteLine(thisArray[i]);
            // }

            // Eliminate Negative Numbers
            // Given any array x, say [1, 5, 10, -2], create an algorithm that replaces any negative number with the value of 0. When the program is done, x should have no negative values, say [1, 5, 10, 0].
            // int[] thisArray = {1, 5, 10, -2};
            // for (int i = 0; i < thisArray.Length; i++)
            // {
            //     System.Console.WriteLine(thisArray[i]);
            //     if(thisArray[i] < 0)
            //     {
            //         thisArray[i] = 0;
            //     }
            // }

            // Min, Max, and Average
            // Given any array x, say [1, 5, 10, -2], create an algorithm that prints the maximum number in the array, the minimum value in the array, and the average of the values in the array.
            // int[] thisArray = {1, 5, 10, -2};
            // int max = thisArray[0];
            // int min = thisArray[0];
            // double sum = 0.0;
            // double avg = 0.0;
            // for (int i = 0; i < thisArray.Length; i++)
            // {
            //     if (thisArray[i] > max)
            //     {
            //         max = thisArray[i];
            //     }
            //     if (thisArray[i] < min)
            //     {
            //         min = thisArray[i];
            //     }
            //     sum = sum + thisArray[i];
            // }
            // avg = sum / thisArray.Length;
            // System.Console.WriteLine(min);
            // System.Console.WriteLine(max);
            // System.Console.WriteLine(avg);

            // Shifting the values in an array
            // Given any array x, say [1, 5, 10, 7, -2], create an algorithm that shifts each number by one to the front and adds '0' to the end. For example, when the program is done,  if the array [1, 5, 10, 7, -2] is passed to the function, it should become [5, 10, 7, -2, 0].
            // int[] thisArray = {1, 5, 10, 7, -2};
            // for (int i = 0; i < thisArray.Length - 1; i++)
            // {
            //     thisArray[i] = thisArray[i + 1];
            // }
            // thisArray[thisArray.Length-1] = 0;
            // for (int i = 0; i < thisArray.Length; i++)
            // {
            //     System.Console.WriteLine(thisArray[i]);
            // }

            // Number to String
            // Write a program that takes an array of numbers and replaces any negative number with the string 'Dojo'. For example, if array x is initially [-1, -3, 2] your function should return an array with values ['Dojo', 'Dojo', 2].
            int[] thisArray = {-1, -3, 2};
            List<object> newList = new List<object>();
            for (int i = 0; i < thisArray.Length; i++)
            {
                if (thisArray[i] < 0)
                {
                    newList.Add("Dojo");
                }
                else
                {
                    newList.Add(thisArray[i]);
                }
            }
            newList.ToArray();
            for (int i = 0; i < newList.Count; i++)
            {
                System.Console.WriteLine(newList[i]);
            }
        }
    }
}
