using System;
using DbConnection;

namespace connect
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            DbConnector.Execute("Some query with no expected return");
        }
    }
}
