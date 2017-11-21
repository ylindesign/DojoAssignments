using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace userdash.Controllers {
    public class UserController : Controller {
        // GET: /Home/
        [HttpGet]
        [Route("")]
        public IActionResult Index() {
            return View();
        }

        [Route("signin")]
        public IActionResult Signin() {
            return View();
        }

        [Route("register")]
        public IActionResult Register() {
            return View();
        }

        [Route("users/new")]
        public IActionResult NewUser() {
            return View();
        }
    }
}
