using System.Collections.Generic;

namespace deck
{
    class Player
    {
        public List<Card> Hand { get;set; }

        public Player() {
            Hand = new List<Card>();
        }

        public Card Draw(deck deck) {
            Card DrawnCard = deck.Deal();
            Hand.Add(DrawnCard);
            return DrawnCard;
        }

        public Card Discard(int idx) {
            idx--;
            if (idx > Hand.Count) {
                System.Console.WriteLine("Don't have a card there!");
                return null;
            }
            Card Drop = Hand[idx];
            Hand.RemoveAt(idx);
            return Drop;
        }
    }
}
