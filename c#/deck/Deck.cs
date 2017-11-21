using System;
using System.Collections.Generic;

namespace deck
{
    class deck {
        public List<Card> Cards { get;set; }
        public deck() {
            Cards = new List<Card>();
            BuildDeck();
        }

        public void BuildDeck(){
            string[] Suits = {"Hearts", "Clubs", "Spades", "Diamonds"};
            string[] Values = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};
            for (int suit = 0; suit < Suits.Length; suit++) {
                for (int value = 0; value < Values.Length; value++) {
                    Cards.Add(new Card(Values[value], Suits[suit], value + 1));
                }
            }
        }

        public Card Deal() {
            Card Drawn = Cards[0];
            Cards.RemoveAt(0);
            return Drawn;
        }

        public void Reset() {
            Cards = new List<Card>();
            BuildDeck();
        }

        public void Shuffle() {
            Random rand = new Random();
            for (int idx = 0; idx < Cards.Count; idx++) {
                int randIdx = rand.Next(idx, Cards.Count);
                Card temp = Cards[randIdx];
                Cards[randIdx] = Cards[idx];
                Cards[idx] = temp;
            }
        }
    }
}
