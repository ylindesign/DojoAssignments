using System.ComponentModel.DataAnnotations;
namespace bank.Models {
    public class RegisterViewModel : BaseEntity {
        [Required(ErrorMessage="First name needs to be at least 2 characters long.")]
        [MinLength(2)]
        [RegularExpression(@"^[a-zA-Z]+$")]
        public string first_name { get; set; }

        [Required(ErrorMessage="Last name needs to be at least 2 characters long.")]
        [MinLength(2)]
        [RegularExpression(@"^[a-zA-Z]+$")]
        public string last_name { get; set; }
 
        [Required(ErrorMessage="Email needs to be a valid email.")]
        [EmailAddress]
        public string email { get; set; }
 
        [Required(ErrorMessage="Password needs to be at least 8 characters long.")]
        [MinLength(8)]
        [DataType(DataType.Password)]
        public string password { get; set; }
 
        [Compare("password", ErrorMessage = "Passwords must match.")]
        public string pw_conf { get; set; }
    }
}