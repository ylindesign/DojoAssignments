using System;
using System.Collections.Generic;

namespace boxing
{
    class Program
    {
        static void Main(string[] args)
        {
            List<object> thing = new List<object>();
            thing.Add(7);
            thing.Add(28);
            thing.Add(-1);
            thing.Add(true);
            thing.Add("chair");
            int sum = 0;
            for (int i = 0; i < thing.Count; i++)
            {
                System.Console.WriteLine(thing[i]);
                if (thing[i] is int)
                {
                    // int add = thing[i] as int;
                    sum += (int)thing[i];
                }
            }
            System.Console.WriteLine(sum);
        }
    }
}
