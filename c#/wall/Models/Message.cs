using System.ComponentModel.DataAnnotations;
 
namespace wall.Models {
    public class Message : BaseEntity {
        [Required]
        // [MinLength(2)]
        // [RegularExpression(@"^[a-zA-Z''-'\s]{1,40}$")]
        public string message { get; set; }

        [Required]
        [RegularExpression(@"^\d+$")] //non negative number
        public int user_id { get; set; }
    }

    public class Comment : BaseEntity {
        [Required]
        // [MinLength(2)]
        // [RegularExpression(@"^[a-zA-Z''-'\s]{1,40}$")]
        public string comment { get; set; }

        [Required]
        [RegularExpression(@"^\d+$")] //non negative number
        public int user_id { get; set; }

        [Required]
        [RegularExpression(@"^\d+$")] //non negative number
        public int message_id { get; set; }
    }
}