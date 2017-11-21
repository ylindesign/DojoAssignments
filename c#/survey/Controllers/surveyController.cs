using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace survey.Controllers {
    public class surveyController : Controller {
        [HttpGet]
        [Route("")]
        public IActionResult Index() {
            return View("index");
        }

        [Route("/results")]
        public IActionResult Results() {
            return View("results");
        }

        [HttpPost]
        [Route("/send")]
        public IActionResult Send(string Name, string Location, string Lang, string Comment) {
            ViewBag.Name = Name;
            ViewBag.Location = Location;
            ViewBag.Lang = Lang;
            ViewBag.Comment = Comment;
            return View("results");
        }
    }
}