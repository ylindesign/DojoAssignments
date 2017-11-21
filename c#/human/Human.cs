using System;

namespace human
{
    public class Human
    {
        public string Name;
        public int Strength;
        public int Intelligence;
        public int Dexterity;
        public int Health;
        public Human(string name)
        {
            Name = name;
            Strength = 3;
            Intelligence = 3;
            Dexterity = 3;
            Health = 100;
        }

        public Human(string name, int str, int intel, int dex, int hp){
            Name = name;
            Strength = str;
            Intelligence = intel;
            Dexterity = dex;
            Health = hp;
        }

        public void Attack(Human person){
            person.Health -= 5 * Strength;
        }
    }
}