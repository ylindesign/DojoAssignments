namespace kitty
{
    public class Card
    {
        public string StringVal { get;set; }
        public string Suit { get;set; }
        public int Val { get;set; }
        // 
        public Card(string strVal, string suit, int val) {
            StringVal = strVal; // Ace, 2, 3, Queen, King, etc
            Suit = suit; // Spade, Heart, etc
            Val = val; // 1, 2, 3, 12, 13, etc
        }
    }
}