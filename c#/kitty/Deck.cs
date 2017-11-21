using System;
using System.Collections.Generic;

namespace kitty
{
    public class Deck
    {
        public List<Card> Cards { get;set; }
        public Deck() {
            Cards = new List<Card>();
            BuildDeck();
        }
        public void BuildDeck(){
            string[] Suits = {"Hearts", "Clubs", "Spades", "Diamonds"};
            string[] Values = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};
            for (int suit = 0; suit < Suits.Length; suit++) {
                for (int value = 0; value < Values.Length; value++) {
                    Cards.Add(new Card(Values[value], Suits[suit], value + 2));
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