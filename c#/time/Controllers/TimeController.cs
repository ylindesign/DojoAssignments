using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace time.Controllers
{
    public class TimeController : Controller
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