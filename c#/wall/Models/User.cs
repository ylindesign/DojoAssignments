using System.ComponentModel.DataAnnotations;
 
namespace wall.Models {
    public class User : BaseEntity {
        [Required(ErrorMessage="First name needs to be at least 2 characters long.")]
        [MinLength(2)]
        [RegularExpression(@"^[a-zA-Z''-'\s]{1,40}$")]
        public string first_name { get; set; }

        [Required(ErrorMessage="Last name needs to be at least 2 characters long.")]
        [MinLength(2)]
        [RegularExpression(@"^[a-zA-Z''-'\s]{1,40}$")]
        public string last_name { get; set; }
 
        [Required]
        [EmailAddress]
        [RegularExpression(@"^(?("")("".+?""@)|(([0-9a-zA-Z]((\.(?!\.))|[-!#\$%&'\*\+/=\?\^`\{\}\|~\w])*)(?<=[0-9a-zA-Z])@))(?(\[)(\[(\d{1,3}\.){3}\d{1,3}\])|(([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,6}))$")]
        public string email { get; set; }
 
        [Required]
        [DataType(DataType.Password)]
        // [RegularExpression(@"(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{8,10})$")]
        public string password { get; set; }
    }
}