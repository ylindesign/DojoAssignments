using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using wedding.Models;
using System.Linq;
using Microsoft.EntityFrameworkCore;

namespace wedding.Controllers {
    public class WeddingController : Controller {
        private WeddingContext _context;
        public WeddingController(WeddingContext context) {
            _context = context;
        }
        // GET: /Home/
        [HttpGet]
        [Route("wedding")]
        public IActionResult Wedding() {
            // Wedding AllWeddings = _context.wedding.All.ToList();
            if (HttpContext.Session.GetInt32("UserId") == 0 || HttpContext.Session.GetInt32("UserId") == null) {
                TempData["message"] = "You have to be logged in to see this page!";
                return RedirectToAction("Index", "User");
            }
            List<Wedding> AllWeddings = _context.wedding.Include(y => y.Guests).ToList();
            ViewBag.AllWeddings = AllWeddings;
            ViewBag.UserId = HttpContext.Session.GetInt32("UserId");
            ViewBag.Message = TempData["message"];
            return View("Wedding");
        }

        [Route("addpage")]
        public IActionResult AddPage()  {
            if (HttpContext.Session.GetInt32("UserId") == 0 || HttpContext.Session.GetInt32("UserId") == null) {
                TempData["message"] = "You have to be logged in to see this page!";
                return RedirectToAction("Index", "User");
            }
            ViewBag.Message = TempData["message"];
            return View("AddPage");
        }

        [Route("page/{WedId}")]
        public IActionResult Page(int WedId)  {
            if (HttpContext.Session.GetInt32("UserId") == 0 || HttpContext.Session.GetInt32("UserId") == null) {
                TempData["message"] = "You have to be logged in to see this page!";
                return RedirectToAction("Index", "User");
            }
            ViewBag.Wedding = _context.wedding.Where(x => x.id == WedId).SingleOrDefault();
            ViewBag.Guests = _context.guests.Where(g => g.weddingId == WedId).Include(u => u.User).ToList();
            // Where(y => y.weddingId == WedId)
            return View();
        }

        [HttpPost]
        [Route("/add")]
        public IActionResult Add(Wedding Wed) {
            if (Wed.date < DateTime.Now.Date) {
                TempData["message"] = "Date cant be in the past";
                System.Console.WriteLine("Date cant be in the past");
                System.Console.WriteLine("Date cant be in the past");
                System.Console.WriteLine("Date cant be in the past");
                System.Console.WriteLine("Date cant be in the past");
                System.Console.WriteLine("Date cant be in the past");
                return RedirectToAction("AddPage");
            }
            if(ModelState.IsValid) {
                Wed.created_at = DateTime.Now;
                Wed.updated_at = DateTime.Now;
                Wed.userId = (int)HttpContext.Session.GetInt32("UserId");
                _context.Add(Wed);
                _context.SaveChanges();
                TempData["message"] = "Sucessfully added a new wedding";
            } else {
                TempData["message"] = "Unsucessful in adding a new wedding";
            }
            return RedirectToAction("Wedding");
        }

        [Route("rsvp/{WedId}")]
        public IActionResult RSVP(int WedId) {
            if(ModelState.IsValid) {
                Guest Moca = new Guest();
                Moca.weddingId = WedId;
                Moca.userId = (int)HttpContext.Session.GetInt32("UserId");
                _context.Add(Moca);
                _context.SaveChanges();
                TempData["message"] = "Sucessfully RSVP'd to a wedding";
            } else {
                TempData["message"] = "Unsucessful in RSVPing";
            }
            return RedirectToAction("Wedding");
        }

        [Route("unrsvp/{WedId}")]
        public IActionResult UnRSVP(int WedId) {
            if(ModelState.IsValid) {
                int CurrId = (int)HttpContext.Session.GetInt32("UserId");
                Guest remove = _context.guests.Where(x => x.weddingId == WedId && x.userId == CurrId).SingleOrDefault();
                _context.guests.Remove(remove);
                _context.SaveChanges();
                // Guest Moca = new Guest();
                // Moca.weddingId = WedId;
                // _context.Add(Moca);
                // _context.SaveChanges();
                TempData["message"] = "Sucessfully un-RSVP'd to a wedding";
            } else {
                TempData["message"] = "Unsucessful in un-RSVPing";
            }
            return RedirectToAction("Wedding");
        }

        [Route("delete/{WedId}")]
        public IActionResult Delete(int WedId) {
            if(ModelState.IsValid) {
                Wedding remove = _context.wedding.Where(x => x.id == WedId).SingleOrDefault();
                List<Guest> guest = _context.guests.Where(g => g.weddingId == WedId).ToList();
                foreach (var persom in guest) {
                    _context.guests.Remove(persom);
                    _context.SaveChanges();
                }
                _context.wedding.Remove(remove);
                _context.SaveChanges();
                TempData["message"] = "Sucessfully deleted a wedding";
            } else {
                TempData["message"] = "Unsucessful in deleting";
            }
            return RedirectToAction("Wedding");
        }
    }
}
