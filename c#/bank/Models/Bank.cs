using System;
using System.ComponentModel.DataAnnotations;

namespace bank.Models
{
    public class Bank : BaseEntity
    {
        public int id { get; set; }
        public string tran { get; set; }
        public int user_id { get; set; }
        public DateTime created_at { get; set; }
        public DateTime updated_at { get; set; }

        public User User { get; set; }
    }
}