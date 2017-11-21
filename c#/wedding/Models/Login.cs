using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace wedding.Models
{
    public class User : BaseEntity
    {
        public int id { get; set; }
        public string first_name { get; set; }
        public string last_name { get; set; }
        public string email { get; set; }
        public string password { get; set; }
        public DateTime created_at { get; set; }
        public DateTime updated_at { get; set; }

        public List<Guest> Guests { get; set; }

        public List<Wedding> Wedding { get; set; }
        public User() {
            Guests = new List<Guest>();
            Wedding = new List<Wedding>();
        }
    }
}