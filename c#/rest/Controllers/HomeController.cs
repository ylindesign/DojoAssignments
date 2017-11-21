using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using rest.Models;
using System.Linq;

namespace rest.Controllers
{
    public class HomeController : Controller
    {
        private RestContext _context;
        public HomeController(RestContext context) {
            _context = context;
        }
        // GET: /Home/
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            // ViewBag.Message = TempData["message"];
            ViewBag.Errors = "";
            return View();
        }

        [Route("/reviews")]
        public IActionResult Reviews()
        {
            List<Review> AllReviews = _context.reviews.ToList();
            ViewBag.AllReviews = AllReviews;
            ViewBag.Message = TempData["message"];
            return View();
        }

        [HttpPost]
        [Route("/review")]
        public IActionResult Review(Review NewReview)
        {
            if(ModelState.IsValid) {
                _context.Add(NewReview);
                _context.SaveChanges();
                TempData["message"] = "You successfully made a review!";
                return RedirectToAction("Reviews");
            }
            // TempData["message"] = "You're missing some information!";
            else {
            // TempData["errors"] = ModelState.Values;
            // System.Console.WriteLine(ModelState.Values);
            ViewBag.Errors = ModelState.Values;
            }
            return View("Index");
            // return RedirectToAction("Index");
        }
    }
}
