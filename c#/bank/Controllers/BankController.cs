using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using bank.Models;

namespace bank.Controllers {
    public class BankController : Controller {
        // GET: /Home/
        [HttpGet]
        [Route("/account")]
        public IActionResult Bank() {
            return View("Bank");
        }
    }
}
