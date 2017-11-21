# WE USED VIEWS TO FIND THESE

1. ...all baseball leagues
context={
	"leagues": League.objects.filter(sport = "Baseball"),
}

2. ...all womens' leagues'
context={	
	"leagues": League.objects.filter(name__contains="Women"),
}

3. ...all leagues where sport is any type of hockey
"leagues": League.objects.filter(sport__contains="Hockey"),

4. ...all leagues where sport is something OTHER THAN football
context={	
	"leagues": League.objects.exclude(sport="Football"),
}

5. ...all leagues that call themselves "conferences"
context={	
	"leagues": League.objects.filter(name__contains="Conference"),
}

6. ...all leagues in the Atlantic region
context={	
	"leagues": League.objects.filter(name__contains="Atlantic"),
}

7. ...all teams based in Dallas
context={	
	"teams": Team.objects.filter(location__contains="Dallas"),
}

8. ...all teams named the Raptors
context={	
	"teams": Team.objects.filter(team_name__contains="Raptors"),
}

9. ...all teams whose location includes "City"
context={	
	"teams": Team.objects.filter(location__contains="city"),
}

10. ...all teams whose names begin with "T"
context={	
	"teams": Team.objects.filter(team_name__startswith="T"),
}

11. ...all teams, ordered alphabetically by location
context={	
	"teams": Team.objects.all().order_by("location"),
}

12. ...all teams, ordered by team name in reverse alphabetical order
context={	
	"teams": Team.objects.all().order_by("-team_name"),
}

13. ...every player with last name "Cooper"
context={	
	"players": Player.objects.filter(last_name="Cooper"),
}

14. ...every player with first name "Joshua"
context={	
	"players": Player.objects.filter(first_name="Joshua"),
}

15. ...every player with last name "Cooper" EXCEPT FOR Joshua
context={	
	"players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
}

16. ...all players with first name "Alexander" OR first name "Wyatt"
context={	
	"players": Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt"),
}



...all teams in the Atlantic Soccer Conference
		"teams": Team.objects.filter(league__name__contains="Atlantic Soccer")

...all (current) players on the Boston Penguins
"players": Player.objects.filter(curr_team__team_name__contains="Penguins"

...all (current) players in the International Collegiate Baseball Conference
	"players": Player.objects.filter(curr_team__league__name__contains="International Collegiate Baseball Conference")

...all (current) players in the American Conference of Amateur Football with last name "Lopez"
		"players": Player.objects.filter(curr_team__league__name__contains="American Conference of Amateur Football").filter(last_name="Lopez")

...all football players
"players": Player.objects.filter(curr_team__league__sport__contains="Football")

...all teams with a (current) player named "Sophia"
		"teams": Team.objects.filter(curr_players__first_name="Sophia")

...all leagues with a (current) player named "Sophia"
"leagues": League.objects.filter(teams__curr_players__first_name="Sophia"),

...everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
"players": Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders")


...all teams, past and present, that Samuel Evans has played with
		"teams": Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans")


...all players, past and present, with the Manitoba Tiger-Cats
		"players": Player.objects.filter(all_teams__team_name="Tiger-Cats")


...all players who were formerly (but aren't currently) with the Wichita Vikings
		"players": Player.objects.filter(all_teams__team_name="Vikings").exclude(curr_team__team_name="Vikings")

...every team that Jacob Gray played for before he joined the Oregon Colts
		"teams": Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(team_name="Colts"),


...everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
		"players": Player.objects.filter(first_name="Joshua").filter(all_teams__league__name__contains="Atlantic Federation of Amateur Baseball Players")


...all teams that have had 12 or more players, past and present. (HINT: Look up the Django annotate function.)
	"teams": Team.objects.annotate(num_teams=Count('all_players')).filter(num_teams__gte=12),

...all players, sorted by the number of teams they've played for
	"players": Player.objects.annotate(num_teams=Count('all_teams')).order_by('num_teams'),




