using System.Collections.Generic;

namespace kitty {
    public class Player {
        public string Name;
        public List<Card> Hand { get;set; }
        public int Money { get;set; }
        public bool Flush { get;set; }
        public string Set { get;set; }
        public bool Run { get;set; }
        public int HighCard { get;set; }
        public int MidCard { get;set; }
        public int LowCard { get;set; }
        public Player(string name) {
            Name = name;
            Hand = new List<Card>();
            Money = 1000;
            Flush = false;
            Run = false;
        }
        public Card Draw(Deck Deck) {
            Card DrawnCard = Deck.Deal();
            Hand.Add(DrawnCard);
            return DrawnCard;
        }
        public bool Bet(Game Game, int Bet) {
            if (Bet >= Game.Bet) {
                Money -= Bet;
                Game.Pile += Bet;
                return true;
            } 
            return false;
        }
    }
}