using System;
using System.ComponentModel.DataAnnotations;

namespace rest.Models
{
    public class Review
    {
        public int id { get; set; }
        
        [Required(ErrorMessage="Must have your name.")]
        public string user { get; set; }

        [Required(ErrorMessage="Must have a restaurant name.")]
        public string rest { get; set; }

        [Required(ErrorMessage="Must have a review.")]
        [MinLength(10)]
        public string review { get; set; }

        [Required(ErrorMessage="Must have a date.")]
        public DateTime date { get; set; }

        [Required(ErrorMessage="Must have a rating.")]        
        public int stars { get; set; }
        public DateTime created_at { get; set; }
        public DateTime updated_at { get; set; }
    }
}