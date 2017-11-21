using System;
using System.Collections.Generic;


namespace kitty
{
    class Program
    {
        static void Main(string[] args)
        {
            // Once you match the bet & show, end the game
            // If a player has more money than current Bet AND less than the double of current Bet, then the player has option to Pass(End) or Show(Match & End).
            Deck thisDeck = new Deck();
            thisDeck.Shuffle();
            Player One = new Player("Yu");
            Player Two = new Player("Kausali");            
            Game thisGame = new Game();
            // One.Draw(thisDeck);
            // Two.Draw(thisDeck);
            // One.Draw(thisDeck);
            // Two.Draw(thisDeck);
            // One.Draw(thisDeck);
            // Two.Draw(thisDeck);
            
            One.Hand.Add(new Card("Ace", "Spade", 14));
            One.Hand.Add(new Card("Ace", "Heart", 14));
            One.Hand.Add(new Card("Ace", "Diamond", 14));
            Two.Hand.Add(new Card("Ace", "Spade", 14));
            Two.Hand.Add(new Card("King", "Heart", 13));
            Two.Hand.Add(new Card("Queen", "Diamond", 12));

            thisGame.Sort(One);
            thisGame.Sort(Two);
            thisGame.Set(One);
            thisGame.Set(Two);
            thisGame.Compare(One, Two);
            thisGame.Announce(thisGame.winner);
            // Triple > Run + Flush
            // Run + Flush > Run
            // Run > Flush
                // <<Check Values of Run in all cases>>
            // Flush > Double
            // Double > Single High Value (Everything is diff)
            // Single > 2/4/5
        }
    }
}
