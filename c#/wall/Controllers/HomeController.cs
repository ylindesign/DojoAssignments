using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using DbConnection;
using wall.Models;
using Newtonsoft.Json;

namespace wall.Controllers {
    public static class SessionExtensions {
        public static void SetObjectAsJson(this ISession session, string key, object value)
        {
            session.SetString(key, JsonConvert.SerializeObject(value));
        }
        
        public static T GetObjectFromJson<T>(this ISession session, string key)
        {
            string value = session.GetString(key);
            return value == null ? default(T) : JsonConvert.DeserializeObject<T>(value);
        }
    }
    public class HomeController : Controller {
        [HttpGet]
        [Route("")]
        public IActionResult Index() {
            if (HttpContext.Session.GetObjectFromJson<int>("user") > 0) {
                TempData["message"] = "You're already logged in, can't skip to Home Page";
                return RedirectToAction("Wall");
            }
            ViewBag.Messages = TempData["message"];
            return View("Index");
        }

        [Route("wall")]
        public IActionResult Wall() {
            if (HttpContext.Session.GetObjectFromJson<int>("user") > 0) {
                var AllMessages = DbConnector.Query($"SELECT messages.id AS messages_id, message, users.id AS users_id, first_name, messages.created_at AS created FROM messages JOIN users ON messages.user_id = users.id ");
                var AllComments = DbConnector.Query($"SELECT comments.id AS comments_id, comment, comments.message_id AS messages_id, comments.user_id, first_name, comments.created_at AS created FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON comments.user_id = users.id");                
                // var AllUsers = DbConnector.Query($"SELECT * FROM users");
                int id = HttpContext.Session.GetObjectFromJson<int>("user");
                var user = DbConnector.Query($"SELECT * FROM users WHERE id = {id}");
                string name = Convert.ToString(user[0]["first_name"]);
                ViewBag.Messages = TempData["message"];
                ViewBag.Name = name;
                ViewBag.AllMessages = AllMessages;
                ViewBag.AllComments = AllComments;
                // ViewBag.AllUsers = AllUsers;
                return View("Wall");
            } 
            TempData["message"] = "Can't skip Login/Registration!";
            return RedirectToAction("Index");
        }

        [HttpPost]
        [Route("register")]
        public IActionResult Register(User NewUser) {
            if (Request.Form["password"] != Request.Form["conf_pw"]) {
                TempData["message"] = "Passwords must match";
                return RedirectToAction("Index");
            }
            var user = DbConnector.Query($"SELECT * FROM users WHERE email = '{NewUser.email}'");
            if (user.Count > 0) {
                if (Request.Form["email"] == user[0]["email"]) {
                    TempData["message"] = "Email is taken!";
                    return RedirectToAction("Index");
                }
            }
            TryValidateModel(NewUser);
            if(ModelState.IsValid) {
                DbConnector.Execute($"INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES ('{NewUser.first_name}', '{NewUser.last_name}', '{NewUser.email}', '{NewUser.password}', NOW(), NOW())");
                // if (user.Count > 0) {
                    var current = DbConnector.Query($"SELECT * FROM users WHERE email = '{NewUser.email}'");
                    int id = Convert.ToInt32(current[0]["id"]);
                    HttpContext.Session.SetObjectAsJson("user", id);
                // }
                TempData["message"] = "You successfully registered!";
                return RedirectToAction("Wall");
            }
            ViewBag.Status = true;
            ViewBag.errors = ModelState.Values;
            return View("Index");
        }

        [Route("login")]
        public IActionResult Login(User NewUser) {
            var user = DbConnector.Query($"SELECT * FROM users WHERE email = '{NewUser.email}'");            
            if (user.Count > 0) {
                if (user[0]["password"] == Request.Form["pw"] && user[0]["email"] == Request.Form["email"]) {
                    // User current = HttpContext.Session.GetObjectFromJson<User>("user");
                    int id = Convert.ToInt32(user[0]["id"]);
                    HttpContext.Session.SetObjectAsJson("user", id);
                    // TempData["name"] = user[0]["first_name"];
                    TempData["message"] = "You're logged in!";
                    return RedirectToAction("Wall");
            }
            } else {
                TempData["message"] = "Invalid Username or Password";
            }
            return RedirectToAction("Index");
        }

        [Route("logout")]
        public IActionResult Logout() {
            HttpContext.Session.Clear();
            return RedirectToAction("Index");
        }

        [Route("message")]
        public IActionResult Message(string message) {
            // if (HttpContext.Session.GetObjectFromJson<int>("user") > 0) {
                int id = HttpContext.Session.GetObjectFromJson<int>("user");
                var user = DbConnector.Query($"SELECT * FROM users WHERE id = {id}");
                // int userId = Convert.ToInt32(user[0]["id"]);
                
                TryValidateModel(message);
                if(ModelState.IsValid) {
                    TempData["message"] = "You successfully posted a message!";
                    DbConnector.Execute($"INSERT INTO messages (message, user_id, created_at, updated_at) VALUES ('{message}', {id}, NOW(), NOW())");
                    // return RedirectToAction("Wall");
                }
            // }
            return RedirectToAction("Wall");
        }

        [Route("comment/{msg_id}")]
        public IActionResult Comment(string comment, int msg_id) {
            // if (HttpContext.Session.GetObjectFromJson<int>("user") > 0) {
                int id = HttpContext.Session.GetObjectFromJson<int>("user");
                var user = DbConnector.Query($"SELECT * FROM users WHERE id = {id}");
                int userId = Convert.ToInt32(user[0]["id"]);
                
                TryValidateModel(comment);
                if(ModelState.IsValid) {
                    TempData["message"] = "You successfully posted a comment!";
                    DbConnector.Execute($"INSERT INTO comments (comment, user_id, message_id, created_at, updated_at) VALUES ('{comment}', {userId}, {msg_id}, NOW(), NOW())");
                    // return RedirectToAction("Wall");
                }
            // }
            return RedirectToAction("Wall");

//             SELECT messages.id AS messages_id, message, users.id AS users_id, first_name, messages.created_at AS created, comments.id AS comment_id, comment
// FROM messages
// JOIN users ON messages.user_id = users.id 
// JOIN comments ON messages.id = comments.id
        }
    }
}
