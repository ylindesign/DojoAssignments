using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using DbConnection;
using System.Linq;

namespace quote.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }

        [Route("quotes")]
        public IActionResult Quotes()
        {
            // List<Dictionary<string, object>> AllQuotes = DbConnector.Query("SELECT * FROM quotes");
            ViewBag.Quotes = DbConnector.Query("SELECT * FROM quotes ORDER BY created_at DESC");
            return View("Quotes");
        }

        [Route("error")]
        public IActionResult Error()
        {
            
            return View("Error");
        }

        [HttpPost]
        [Route("quotes")]
        public IActionResult NewQuote()
        {
            string name, quote;
            name = Request.Form["name"];
            quote = Request.Form["quote"];
            if (name.Length < 3 || quote.Length < 5) {
                return RedirectToAction("Error");
            }
            DbConnector.Execute($"INSERT INTO quotes (name, quote, created_at, updated_at) VALUES ('{name}', '{quote}', NOW(), NOW())");
            return RedirectToAction("Index");
        }


    }
}
