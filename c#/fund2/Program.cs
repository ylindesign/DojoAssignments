using System;
using System.Collections.Generic;

namespace fund2
{
    class Program
    {
        static void Main(string[] args)
        {
            // int[] array1;
            // array1 = new int[] {0,1,2,3,4,5,6,7,8,9};

            string[] array2;
            array2 = new string[] {"Tim", "Martin", "Nikki", "Sara"};

            // bool[] array3;
            // array3 = new bool[] {true, false, true, false, true, false, true, false, true, false,};

            // int [,] multiTable = new int[10,10];
            // for (int i = 0; i < 10; i++)
            // {
            //     for (int j = 0; j < 10; j++)
            //     {
            //         multiTable[i, j] = (i+1)*(j+1);
            //         // Console.WriteLine(i*j);
            //     }
            // }
            // for (int x = 0; x < 10; x++)
            // {
            //     for (int y = 0; y < 10; y++)
            //     {
            //         Console.Write(multiTable[x,y]);
            //     }
            // }
            List<string> flavors = new List<string>();
            flavors.Add("Chocolate");
            flavors.Add("Vanilla");
            flavors.Add("Beans");
            flavors.Add("Berry");
            flavors.Add("Mystery");
            // System.Console.WriteLine(flavors.Count);
            // System.Console.WriteLine(flavors[3]);
            // flavors.RemoveAt(3);
            // System.Console.WriteLine(flavors.Count);
            Dictionary<string,string> profile = new Dictionary<string,string>();
            Random rand = new Random();
            foreach(string name in array2)
            {
                profile[name] = flavors[rand.Next(flavors.Count)];
            }
            Console.WriteLine("Users and their favor ice cream flavors:");
            foreach(KeyValuePair<string, string> info in profile)
            {
                Console.WriteLine(info.Key + " - " + info.Value);
            }
        }
    }
}
