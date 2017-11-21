using System;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Collections to work with
            List<Artist> Artists = JsonToFile<Artist>.ReadJson();
            List<Group> Groups = JsonToFile<Group>.ReadJson();

            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?
            // List<Artist> MV = Artists.Where(home => home.Hometown == "Mount Vernon").ToList();
            // System.Console.WriteLine("The artist is {0} and they are {1} years old.", MV[0].ArtistName, MV[0].Age);

            //Who is the Oldest artist in our collection of artists?
            // List<Artist> Young = Artists.OrderBy(age => age.Age).ToList();
            // System.Console.WriteLine("The youngest artist is {0} and they are {1} years old.", Young[0].ArtistName, Young[0].Age);

            //Display all artists with 'William' somewhere in their real name
            // List<Artist> William = Artists.Where(name => name.RealName.Contains("William")).ToList();
            // for (int i = 0; i < William.Count; i++) {
            //     System.Console.WriteLine("{0} has 'William' in their real name.", William[i].RealName);
            // }
            
            //Display all groups with names less than 8 characters in length.
            // List<Group> Less8 = Groups.Where(name => name.GroupName.Length < 8).ToList();
            // for (int i = 0; i < Less8.Count; i++) {
            //     System.Console.WriteLine("{0} has 'Less8' in their real name.", Less8[i].GroupName);
            // }

            //Display the 3 oldest artist from Atlanta
            // List<Artist> Atlanta = Artists.Where(home => home.Hometown == "Atlanta").ToList();
            // List<Artist> Old = Atlanta.OrderByDescending(age => age.Age).ToList();

            // int Counter = 0;
            // List<Artist> Final = new List<Artist>();
            // for (int i = 0; i < Old.Count; i++) {
            //     // int age = Old[0].Age;
            //     if (Counter == 3) {
            //         break;
            //     }
            //     if (Old[i].Age == Old[i+1].Age) {
            //         // Counter--;
            //         Final.Add(Old[i]);
            //     }
            //     else {
            //         Final.Add(Old[i]);
            //         Counter++;
            //     }
            // }
            // for (int j = 0; j < Final.Count; j++) {
            //     System.Console.WriteLine("{0} is {1}.", Final[j].ArtistName, Final[j].Age);
            // }
            
            
            

            //(Optional) Display the Group Name of all groups that have members that are not from New York City

            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'
        }
    }
}
