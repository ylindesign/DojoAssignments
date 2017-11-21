using System.ComponentModel.DataAnnotations;
namespace wedding.Models {
    public class RegisterViewModel : BaseEntity {
        [Required(ErrorMessage="First name needs to be at least 2 characters long.")]
        [MinLength(2)]
        [RegularExpression(@"^[a-zA-Z]+$", ErrorMessage="First name must only contain letters.")]
        public string first_name { get; set; }

        [Required(ErrorMessage="Last name needs to be at least 2 characters long.")]
        [MinLength(2)]
        [RegularExpression(@"^[a-zA-Z]+$", ErrorMessage="Last name must only contain letters.")]
        public string last_name { get; set; }
 
        [Required(ErrorMessage="Email needs to be a valid email.")]
        [EmailAddress]
        public string email { get; set; }
 
        [Required]
        [MinLength(8, ErrorMessage="Password needs to be at least 8 characters long.")]
        [DataType(DataType.Password)]
        public string password { get; set; }
 
        [Compare("password", ErrorMessage = "Passwords must match.")]
        public string pw_conf { get; set; }
    }
}