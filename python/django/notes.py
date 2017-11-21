# MODELS
>> app/first_app/models.py

from django.db import models
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# magic method
	def __str__(self):
		return self.first_name + " " + self.last_name
		# <User: Firstname Lastname> instead of 
		# <User: User object>

class Post(models.Model):
	title = models.CharField(max_length=45)
	message = models.TextField(max_length=1000)
	# Notice the association made with ForeignKey for a one-to-many relationship
		# There can be many posts to one User
	user_id = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

# CharField
	# Any text that a user may enter. This has one additional required parameter, max_length, that (unsurprisingly) is the maximum length of text that can be saved.

# TextField
	# Like a CharField, but with no maximum length. Your user could copy the entire text of Atlas Shrugged into the field, and it would save in the database correctly.

# IntegerField, BooleanField
	# Holds integers or booleans, respectively

# DateTimeField
	# Used for date and times, such as timestamps or when a flight is scheduled to depart. This field can take two very useful optional parameters, auto_now_add=True, which adds the current date/time when object is created, and auto_now=True, which automatically updates any time the object is modified.

# ForeignKey, ManyToManyField, OneToOneField
	# Used to indicate a relationship between models (anything that would require a JOIN statement in SQL). ForeignKey is for one-to-many relationships and goes in the model on the "many" side, just as the foreign key column goes in the SQL table on the "many" side.


>> app/first_app/views.py

from django.shortcuts import render
#look inside models.py for people class
from .models import People
def index(request):
	context = {
	"people" : People.objects.all()
	#select * from People
	}
	return render(request, "appname/index.html", context)

def show(request):
	People.objects.create(first_name=“Mike”,last_name=“Hannon”)
	people = People.objects.all()
	print people
	# From Form
	People.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
	return redirect("/")

# In HTML
{% for person in people %}
	{{person.first_name}}
	{{person.last_name}}
{% endfor %}



# QUERIES

# ID	First Name	Last Name	Age
# 1		John		Roberts		62
# 2		Anthony		Kennedy		80
# 3		Clarence	Thomas		68
# 4		Ruth Bader	Ginsburg	81
# 5		Stephen		Breyer		78
# 6		Samuel		Alito		67
# 7		Sonia		Sotomayor	62
# 8		Elena		Kagan		56
# 9		Neil		Gorsuch		49

# Get
	# returns the one object that matches a given condition.
user = User.objects.get(last_name="Thomas")
print("QUERY RESULT:", user)
# >> QUERY RESULT: Clarence Thomas

	# Only use .get if you know that there's exactly one matching item! For this reason, this method works best when used with ID numbers.
user = User.objects.get(id=6)
print("QUERY RESULT:", user)
# >> QUERY RESULT: Samuel Alito

# Filter
	# returns all of the records where a given condition is true.
user = User.objects.filter(last_name="Thomas")
print("QUERY RESULT:", user)
# >> QUERY RESULT: [<User: Clarens Thomas>]>

# The difference between .get and .filter in this case? Note that .get returns the object itself, while .filter returns a QuerySet (a type of object that contains a set of query objects).

# Exclude
	# the opposite of .filter: It returns all of the records where a given condition is false.
user = User.objects.exclude(last_name="Thomas")
print("QUERY RESULT:", user)
# >> QUERY RESULT: [<User: John Roberts>, <User: Anthony Kennedy>, <User:Ruth Bader	Ginsburg>, etc]>

# Conditions
user = User.objects.filter(first_name__startswith="S")
print("QUERY RESULT:", user)
# >> QUERY RESULT: [<User: Stephen Breyer>, <User: Samuel Alito>, <User: Sonia Sotomayor>]>
	# exclude(first_name__contains="E")
	# filter(age__gt=80)
	# filter(age__gte=80)
		# gte = greater than or equal (includes 80 yr)

# Combining Queries
# Diff queries
user = User.objects.filter(last_name__contains="o").exclude(first_name__contains="o")
print("QUERY RESULT:", user)

# Same query, diff arguments
user = User.objects.filter(age__lt=70, first_name__startswith="S")
print("QUERY RESULT:", user)

# This argument OR this argument, use |
user = User.objects.filter(age__lt=70)|User.objects.filter(first_name__startswith="S")
print("QUERY RESULT:", user)

# Displaying on Templates
...user_orm_example_project/apps/users/views.py

def index(request):
	users = User.objects.filter(age__lt=70)|User.objects.filter(first_name__startswith="S")
	context = {"users": users}
	return render(request, "users/index.html", context)

...user_orm_example_project/apps/templates/appname/index.html

<h1>Users</h1>
<table>
  <tr>
    <th>ID</th>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Age</th>
  </tr>
  {% for user in users %}
    <tr>
      <td>{{ user.id }}</td>
      <td>{{ user.first_name }}</td>
      <td>{{ user.last_name }}</td>
      <td>{{ user.age }}</td>
    </tr>
  {% endfor %}
</table>

# Grabbing and Displaying Comment in Blog Ex
# in views.py
def comments(request,id):
	blog = Blog.objects.get(id=id)
	Comment.objects.create(comment=request.POST['comment'],blog=blog)
	return redirect('/')
		# putting form comment into table database

# in index.html

{% for comment in blog.comment_set.all() %}
	{{ comment.comment }}
{% endfor %}


# MODEL VALIDATIONS INTRO - USERMANAGER


>> app/first_app/models.py

from __future__ import unicode_literals
from django.db import models
#Our new manager!
#No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
	def login(self, postData):
		print "Running a login function!"
		print "If successful login occurs, maybe return {'theuser':user} where user is a user object?")
		print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"

def register(self, postData):
	print ("Register a user here")
	print ("If successful, maybe return {'theuser':user} where user is a user object?")
	print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] ")

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# *************************
	# Connect an instance of UserManager to our User model overwriting
	# the old hidden objects key with a new one with extra properties!!!
	objects = UserManager()
	# *************************

>> app/first_app/views.py

# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
from .models import User
def index(request):
	print("Running index method, calling out to User.")
	user = User.objects.login("speros@codingdojo.com","Speros")
	# DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
	print (type(user))
	if 'error' in user:
		pass
	if 'theuser' in user:
		pass
	return HttpResponse("Done running userManager method. Check your terminal console.")



Linking URL into HTML

action=" {% url = 'author:create' %}"
namespace > method


# MANY TO MANY RELATIONSHIPS
>> app/first_app/models.py

class Book(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Publisher(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name="publishers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


this_book = Book.objects.get(id=4)
this_publisher = Publisher.objects.get(id=2)
this_publisher.books.add(this_book)

# this_book.publishers.add(this_publisher) is the same as this_publisher.books.add(this_book), and this_book.publishers.all() will return all publishers of a given book.


# FOREIGN KEY RELATIONSHIPS
>> app/first_app/models.py

class Author(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(Author, related_name="books")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

# To create a record that has this foreign key relationship, you'd pass it into the create function, like with any other field:
my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))

# This code will find all of the books by the author with ID 2:
books = Book.objects.filter(author=Author.objects.get(id=2))

# You can also search by a field in the related object by using a double underscore:
books = Book.objects.filter(author__name="Louise May Alcott")
books = Book.objects.filter(author__name__startswith="Lou")

>> projname/apps/appname/views.py

def index(request):
	context = {"authors": Author.objects.all()}
	return render(request, "book/index.html", context)

>> projname/apps/appname/templates/books/index.html

<h1>Author List</h1>
<ul>
{% for author in authors %}
	<li>{{author.name}}
		<ul>
			{% for book in author.books.all %}
				<li><em>{{book.title}}</em></li>
			{% endfor %}
		</ul>
	</li>
{% endfor %}
</ul>


# NAMED ROUTES
>> projname/apps/appname/urls.py
from django.conf.urls import url
	from . import views
	urlpatterns = [
		url(r'^$', views.toindex, name = 'my_index'),
		url(r'^this_app/new$', views.new, name = 'my_new'),
		url(r'^this_app/(?P<id>\d+)/edit$', views.edit, name = 'my_edit'),
		url(r'^this_app/(?P<id>\d+)/delete$', views.delete, name = 'my_delete'),
		url(r'^this_app/(?P<id>\d+)$', views.show, name = 'my_show'),
	]

>> projname/apps/appname/templates/books/index.html
<a href="{% url 'my_new' %}"></a>
# <a href="/target/this_app/new"></a>

<form class="" action="{% url 'my_delete' id=5 %}" method="post">
	<input type="submit" value="Submit">
</form>
# <form class="" action="/target/this_app/5/delete" method="post">
_____________

>> projname/apps/appname/urls.py
urlpatterns = [
	url(r'^accounts/', include('apps.login_reg_app.urls', namespace='users')),
	url(r'^courses/', include('apps.courses_app.urls', namespace='courses')),
]

>> projname/apps/appname/templates/books/index.html
<a href="{% url 'courses:index' %}">This link will hit the index route in your courses_app</a>
<a href="{% url 'users:index' %}">And this link will hit the index route in your login_reg_app</a>

>> projname/apps/appname/views.py
return redirect(reverse('users:show', keywordarguments={'id': your_id_variable }))


# BCRYPT
(djangoenv)>python
>>> import bcrypt
>>> password = "magical unicorns"
>>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
>>> print hashed
>>> print len(hashed)
>>> password2 = "bananas"
>>> hashed2 = bcrypt.hashpw(password2, bcrypt.gensalt())
>>> print hashed2
>>> if hashed == hashed2:
...      print "the passwords match!"
...   else:
...      print "the passwords don't match!"
...
>>> exit()


















