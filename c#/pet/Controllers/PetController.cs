using System;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
 
namespace pet.Controllers {
    public static class SessionExtensions {
        // We can call ".SetObjectAsJson" just like our other session set methods, by passing a key and a value
        public static void SetObjectAsJson(this ISession session, string key, object value)
        {
            // This helper function simply serializes theobject to JSON and stores it as a string in session
            session.SetString(key, JsonConvert.SerializeObject(value));
        }
        
        // generic type T is a stand-in indicating that we need to specify the type on retrieval
        public static T GetObjectFromJson<T>(this ISession session, string key)
        {
            string value = session.GetString(key);
            // Upone retrieval the object is deserialized based on the type we specified
            return value == null ? default(T) : JsonConvert.DeserializeObject<T>(value);
        }
    }
    public class PetController : Controller {
        [HttpGet]
        [Route("")]
        public IActionResult Index() {
            ViewBag.Win = false;
            ViewBag.Lose = false;
            var current = HttpContext.Session.GetObjectFromJson<pet>("pet");
            if (HttpContext.Session.GetObjectFromJson<pet>("pet") == null) {
                var Pal = new pet();
                HttpContext.Session.SetObjectAsJson("pet", Pal);
            }
            if (HttpContext.Session.GetObjectFromJson<pet>("pet").Energy >= 100 && HttpContext.Session.GetObjectFromJson<pet>("pet").Full >= 100) {
                if (HttpContext.Session.GetObjectFromJson<pet>("pet").Happy >= 100) {
                    TempData["comment"] = "You win!";
                    ViewBag.Win = true;
                    return View("index");
                }
            }
            if (HttpContext.Session.GetObjectFromJson<pet>("pet").Full <= 0 || HttpContext.Session.GetObjectFromJson<pet>("pet").Happy <= 0) {
                TempData["comment"] = "It died!";
                ViewBag.Lose = true;
                return View("index");
            }
            ViewBag.Pal = HttpContext.Session.GetObjectFromJson<pet>("pet");
            ViewBag.Message = TempData["comment"];
            return View("index");
        }

        [HttpPost]
        [Route("feed")]
        public IActionResult Feed() {
            if (HttpContext.Session.GetObjectFromJson<pet>("pet").Meals <= 0) {
                TempData["comment"] = "You don't have enough food to feed!";
                return RedirectToAction("Index");
            }
            Random rand = new Random();
            int chance = rand.Next(1,5);            
            var update = HttpContext.Session.GetObjectFromJson<pet>("pet");
            if (chance == 1) {
                update.Meals -= 1;
                TempData["comment"] = "Oh no! Your pet didn't like that!";
            } else {
                int eating = rand.Next(5,11);
                update.Full += eating;
                update.Meals -= 1;
                TempData["comment"] = "You just fed your pet! They gained " + eating +  " Fullness!";
            }
            HttpContext.Session.SetObjectAsJson("pet", update);
            return RedirectToAction("Index");
        }

        [Route("play")]
        public IActionResult Play() {
            if (HttpContext.Session.GetObjectFromJson<pet>("pet").Energy <= 4) {
                TempData["comment"] = "You don't have enough energy to play!";
                return RedirectToAction("Index");
            }
            Random rand = new Random();
            int chance = rand.Next(1,5);
            var update = HttpContext.Session.GetObjectFromJson<pet>("pet");
            if (chance == 1) {
                update.Energy -= 5;
                TempData["comment"] = "Oh no! Your pet didn't like that!";
            } else {
                int playing = rand.Next(5,11);
                System.Console.WriteLine(update.Happy);
                update.Happy += playing;
                update.Energy -= 5;
                TempData["comment"] = "You just played with your pet! They gained " + playing + " happiness!";
            }
            HttpContext.Session.SetObjectAsJson("pet", update);
            return RedirectToAction("Index");
        }

        [Route("work")]
        public IActionResult Work() {
            if (HttpContext.Session.GetObjectFromJson<pet>("pet").Energy <= 4) {
                TempData["comment"] = "You don't have enough energy to work!";
                return RedirectToAction("Index");
            }
            Random rand = new Random();
            int working = rand.Next(1,4);
            var update = HttpContext.Session.GetObjectFromJson<pet>("pet");
            update.Meals += working;
            update.Energy -= 5;
            HttpContext.Session.SetObjectAsJson("pet", update);
            TempData["comment"] = "Your pet just worked and gained " + working + " meals!";
            return RedirectToAction("Index");
        }

        [Route("sleep")]
        public IActionResult Sleep() {
            // if (HttpContext.Session.GetObjectFromJson<pet>("pet").Full <= 4) {
            //     TempData["comment"] = "Your pet is too hungry to sleep!";
            //     return RedirectToAction("Index");
            // }
            // if (HttpContext.Session.GetObjectFromJson<pet>("pet").Happy <= 4) {
            //     TempData["comment"] = "Your pet is too angry to sleep!";
            //     return RedirectToAction("Index");
            // }
            // Random rand = new Random();
            // int eating = rand.Next(5,11);
            var update = HttpContext.Session.GetObjectFromJson<pet>("pet");
            update.Energy += 15;
            update.Full -= 5;
            update.Happy -= 5;
            HttpContext.Session.SetObjectAsJson("pet", update);
            TempData["comment"] = "Your pet just took a nap! It gained energy, but is now hungirer and angrier!";
            return RedirectToAction("Index");
        }

        [Route("reset")]
        public IActionResult Reset() {
            HttpContext.Session.Clear();
            return RedirectToAction("Index");
        }
    }
}