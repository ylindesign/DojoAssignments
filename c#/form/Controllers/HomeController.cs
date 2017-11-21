using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using DbConnection;
using form.Models;

namespace form.Controllers {
    public class HomeController : Controller {
        [HttpGet]
        [Route("")]
        public IActionResult Index() {
            return View();
        }

        [Route("success")]
        public IActionResult Success() {
            return View("Success");
        }

        [HttpPost]
        [Route("process")]
        public IActionResult Process(Users NewUser) {
            
            // TryValidateModel(NewUser);
            if(ModelState.IsValid)
            {
                DbConnector.Execute($"INSERT INTO form (first_name, last_name, age, email, password, created_at, updated_at) VALUES ('{NewUser.first_name}', '{NewUser.last_name}', {NewUser.age}, '{NewUser.email}', '{NewUser.password}', NOW(), NOW())");
                return RedirectToAction("Success");
            }
            ViewBag.Status = true;
            ViewBag.errors = ModelState.Values;
            return View("Index");
        }
    }
}
