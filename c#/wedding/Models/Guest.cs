using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace wedding.Models
{
    public class Guest : BaseEntity
    {
        public int id { get; set; }
        public int userId { get; set; }
        public int weddingId { get; set; }
        public User User { get; set; }


        public Wedding Wedding { get; set; }

    }
}