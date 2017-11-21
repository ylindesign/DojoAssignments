using System;
using System.Collections.Generic;

namespace puzzle
{
    class Program
    {
        static void Main(string[] args)
        {
        // System.Console.WriteLine(TossCoin());
        // System.Console.WriteLine(TossMultipleCoins(10)); 
        // RandomArray();
        // int[] myArr = RandomArray();
        // System.Console.WriteLine(myArr.Min());
        // System.Console.WriteLine(myArr.Max());
        System.Console.WriteLine(Names());
    }
    static string[] Names(){
        string[] arrayNames = {"Todd", "Tiffany", "Charlie", "Geneva", "Sydney"};
        Random rand = new Random();
        int first = 0;
        int sec = 0;
        int times = rand.Next(5,10);
        int counter = 0;
        string temp = "";
        while (counter < times)
        {
            first = rand.Next(0,arrayNames.Length);
            sec = rand.Next(0,arrayNames.Length);
            if (first == sec)
            {
                counter = counter - 1;
            }
            else
            {
                temp = arrayNames[first];
                arrayNames[first] = arrayNames[sec];
                arrayNames[sec] = temp;
            }
            counter = counter + 1;
        }
        for (int i = 0; i < arrayNames.Length; i++)
        {
            System.Console.WriteLine(arrayNames[i]);
        }
        return arrayNames;

    }

    static string TossCoin(Random rand){
        // System.Console.WriteLine("Tossing a Coin!!");
        string Result = "Heads";
        // Random rand = new Random();
        if (rand.Next(0,2) == 0){
            Result = "Tails";
        }
        return Result;
    }

    static Double TossMultipleCoins(int num){
        int HeadCounter = 0;
        Random rand = new Random();
        for(int i = 0; i<num; i++){
            if(TossCoin(rand) == "Heads")  {
                HeadCounter++;
            }
        }
        return (Double)HeadCounter/num;
    }

    static int[] RandomArray(){
        int sum = 0;
        int[] newArr = new int[10];
        Random rand = new Random();
        for (int i = 0; i <10; i++){
            newArr[i] = rand.Next(5,26);
            System.Console.WriteLine(newArr[i]);
            sum += newArr[i];
        }
        System.Console.WriteLine(sum);
        
        return newArr;
    }
}
}
