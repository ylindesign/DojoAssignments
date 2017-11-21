using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace port.Controllers {
    public class PortController : Controller {
        // A GET method
        // [HttpGet]
        // [Route("index")]
        // public string Index() {
        //     return "Hello World!";
        // }
        
        // A POST method
        [HttpGet]
        [Route("")]
        // public JsonResult Example() {
        //     // The Json method convert the object passed to it into JSON
        //     return Json(SomeC#Object);
        // }
        public IActionResult Index() {
            
            return View("index");
        }
        [Route("/project")]
        public IActionResult Project() {
            return View("project");
        }
        [Route("/contact")]
        public IActionResult Contact() {
            return View("contact");
        }
        //     OR
        //     return View("Index");
        //     Both of these returns will render the same view (You only need one!)
        // }
    }
}