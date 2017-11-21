using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace bank.Models
{
    public class User : BaseEntity
    {
        public int id { get; set; }
        public string first_name { get; set; }
        public string last_name { get; set; }
        public string email { get; set; }
        public string password { get; set; }
        public int balance { get; set; }
        public DateTime created_at { get; set; }
        public DateTime updated_at { get; set; }

        public List<Bank> Tran { get; set; }
        public User() {
            Tran = new List<Bank>();
        }
    }
}