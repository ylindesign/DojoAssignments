using System;

namespace deck
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            deck myDeck = new deck();
            myDeck.Shuffle();
            Player PlayerOne = new Player();
            PlayerOne.Draw(myDeck);
            PlayerOne.Draw(myDeck);
            PlayerOne.Draw(myDeck);
            PlayerOne.Draw(myDeck);
            PlayerOne.Draw(myDeck);
        }
    }
}
