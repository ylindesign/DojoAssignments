using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace userdash.Controllers {
    public class DashboardController : Controller {
        // GET: /Home/
        [HttpGet]
        [Route("dashboard")]
        public IActionResult Dashboard() {
            return View("Dashboard");
        }
    }
}
