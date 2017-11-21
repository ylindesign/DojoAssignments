using System.Collections.Generic;
using System.Linq;

namespace kitty
{
    public class Game
    {
        public int Pile { get;set; }
        public int Bet { get;set; }
        public Player winner { get;set; }
        
        public Game() {
        }
        public void Show() {

        }
        public List<Card> Sort(Player person) {
            person.Hand = person.Hand.OrderBy(card => card.Val).ToList();
            person.HighCard = person.Hand[2].Val;
            person.MidCard = person.Hand[1].Val;
            person.LowCard = person.Hand[0].Val;
            // for (int card = 0; card < person.Hand.Count; card ++) {
            //     System.Console.WriteLine(person.Hand[card].Val);
            // }
            return person.Hand;
        }
        public void Set(Player person) {
            if (person.Hand[0].Val == person.Hand[1].Val && person.Hand[0].Val == person.Hand[2].Val) {
                person.Set = "Triple";
            }
            else if (person.Hand[0].Val == person.Hand[1].Val || person.Hand[1].Val == person.Hand[2].Val) {
                person.Set = "Double";
            }
            else {
                person.Set = "Single";
            }

            if (person.Hand[0].Suit == person.Hand[1].Suit && person.Hand[0].Suit == person.Hand[2].Suit) {
                person.Flush = true;
            }

            if (person.Hand[0].Val+1 == person.Hand[1].Val && person.Hand[0].Val+2 == person.Hand[2].Val) {
                person.Run = true;
                person.Set = "Run";
            }
        }
        
        public void Compare(Player One, Player Two) { 
            // Triple VS Triple
            if (Two.Set == "Triple" && One.Set == "Triple") {
                if (One.HighCard > Two.HighCard) {
                    winner = One;
                } else {
                    winner = Two;
                }
            }
            // Flush VS Flush
            if (One.Flush == true && Two.Flush == true) {
                if (One.HighCard > Two.HighCard) {
                    winner = One;
                } else {
                    winner = Two;
                }
            }
            // Run VS Run
            if (One.Run == true && Two.Run == true) {
                if (One.HighCard > Two.HighCard) {
                    winner = One;
                } else {
                    winner = Two;
                }
            }
            // Flush/Run VS Flush/Run
            if (One.Flush == true && One.Run == true && Two.Flush == true && Two.Run == true) {
                if (One.HighCard > Two.HighCard) {
                    winner = One;
                } else {
                    winner = Two;
                }
            }
            // Double VS Double
            if (One.Set == "Double" && Two.Set == "Double") {
                if (One.MidCard > Two.MidCard) {
                    winner = One;
                } else if (One.MidCard < Two.MidCard) {
                    winner = Two;
                } else {
                    if (One.HighCard > Two.HighCard) {
                        winner = One;
                    } else if (One.HighCard < Two.HighCard) {
                        winner = Two;
                    }
                }
            }

            // Triple VS Anything
            if (One.Set == "Triple" && Two.Set != "Triple") { 
                winner = One;
            } else if (Two.Set == "Triple" && One.Set != "Triple") {
                winner = Two;
            }

            // Flush/Run VS Anything
            if (One.Flush == true && One.Run == true && Two.Set != "Triple") {
                winner = One;
            } else if (Two.Flush == true && Two.Run == true && One.Set != "Triple") {
                winner = Two;
            }

            // Run VS Anything (excluding Flush/Run & Triple)
            if (One.Run == true && Two.Run != true && Two.Flush != true && Two.Set != "Triple") {
                winner = One;
            } else if (Two.Run == true && One.Run != true && One.Flush != true && One.Set != "Triple") {
                winner = Two;
            }

            // Double VS Single
            if (One.Set == "Double" && Two.Set == "Single") {
                winner = One;
            } 
            else if (Two.Set == "Double" && One.Set == "Single") {
                winner = Two;
            } 

            // Single VS Single
            if (One.Set == "Single" && Two.Set == "Single") { 
                if (One.HighCard > Two.HighCard) {
                    winner = One;
                } else {
                    winner = Two;
                }
            }
            // return winner;
        }
        
        public string Announce(Player winner) {
            string win = winner.Name;
            System.Console.WriteLine("The winner is {0}!!!!!!!!!", win);
            return win;
        }
    }
}