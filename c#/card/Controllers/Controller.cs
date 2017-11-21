using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace card.Controllers
{
    // public class HelloController : Controller
    // {
    //     // [HttpGetAttribute]
    //     // public string Index()
    //     // {
    //     //     return "Hello World! Again!";
    //     // }
    //     [HttpGet]
    //     [Route("/{f_name}/{l_name}/{age}/{color}")]
    //     public JsonResult DisplayInt(string f_name, string l_name, int age, string color)
    //     {
    //         var AnonObject = new {
    //                             FirstName = f_name,
    //                             LastName = l_name,
    //                             Age = age,
    //                             Color = color
    //                         };
    //         return Json(AnonObject);
    //     }
    // }
    public class HelloController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
            //OR
            // return View("Index");
            //Both of these returns will render the same view (You only need one!)
        }
    }
}