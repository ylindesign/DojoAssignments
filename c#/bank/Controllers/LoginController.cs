using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using bank.Models;

namespace bank.Controllers {
    public class LoginController : Controller {
        private BankContext _context;
        public LoginController(BankContext context) {
            _context = context;
        }
        // GET: /Home/
        [HttpGet]
        [Route("")]
        public IActionResult Index() {
            return View();
        }

        [Route("login")]
        public IActionResult Login() {
            return View();
        }

        [HttpPost]
        [Route("register")]
        public IActionResult Register(RegisterViewModel model) {
            if(ModelState.IsValid) {
                User NewUser = new User {
                    first_name = model.first_name,
                    last_name = model.last_name,
                    email = model.email,
                    password = model.password
                };
            } else {
                ViewBag.Errors = ModelState.Values;
                return RedirectToAction("Index");
            }
            return View(model);
        }
    }
}
