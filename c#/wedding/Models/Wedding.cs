using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace wedding.Models
{
    public class Wedding : BaseEntity
    {
        public int id { get; set; }
        [Required(ErrorMessage="Wedder One needs a name")]
        [MinLength(2)]
        public string wed_one { get; set; }
        [Required(ErrorMessage="Wedder Two needs a name")]
        [MinLength(2)]
        public string wed_two { get; set; }
        [Required(ErrorMessage="This wedding needs an address")]
        [MinLength(2)]
        public string address { get; set; }
        [Required(ErrorMessage="Date can't be left blank")]
        // [MinLength(2)]
        public DateTime date { get; set; }
        public DateTime created_at { get; set; }
        public DateTime updated_at { get; set; }
        public int userId { get; set; }

        // public User User { get; set; }

        public List<Guest> Guests { get; set; }
        public Wedding() {
            Guests = new List<Guest>();
        }
    }
}