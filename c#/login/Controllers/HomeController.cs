using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using DbConnection;
using login.Models;

namespace login.Controllers
{
    public class HomeController : Controller
    {
        // GET: /Home/
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            ViewBag.Messages = TempData["comment"];
            return View();
        }

        [Route("success")]
        public IActionResult Success()
        {
            ViewBag.Messages = TempData["comment"];
            return View("success");
        }

        [HttpPost]
        [Route("register")]
        public IActionResult Register(User NewUser) {
            if (Request.Form["password"] != Request.Form["conf_pw"]) {
                TempData["comment"] = "Passwords must match";
                return RedirectToAction("Index");
            }
            TryValidateModel(NewUser);
            if(ModelState.IsValid)
            {
                DbConnector.Execute($"INSERT INTO login (first_name, last_name, email, password, created_at, updated_at) VALUES ('{NewUser.first_name}', '{NewUser.last_name}', '{NewUser.email}', '{NewUser.password}', NOW(), NOW())");
                return RedirectToAction("Success");
            }
            ViewBag.Status = true;
            ViewBag.errors = ModelState.Values;
            return View("Index");
        }

        [Route("login")]
        public IActionResult Login(User NewUser) {
            
            // TryValidateModel(NewUser);
            // if(ModelState.IsValid)
            // {
                var user = DbConnector.Query($"SELECT * FROM login WHERE email = '{NewUser.email}'");
                if (user[0]["password"] == Request.Form["pw"]) {
                    // System.Console.WriteLine("Passwords must match");
                    TempData["comment"] = "Youre logged in!";
                    return RedirectToAction("Success");
                } else {
                    TempData["comment"] = "Username or Password doesn't exist";
                }
                return RedirectToAction("Index");
            // }
            // ViewBag.Status = true;
            // ViewBag.errors = ModelState.Values;
            // return RedirectToAction("Index");
        }
    }
}
