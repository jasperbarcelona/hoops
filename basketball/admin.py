from django.contrib import admin
from basketball.models import User, Team, UserTeam, Game, Court, UserGame, UserRating

admin.site.register(User)
admin.site.register(Team)
admin.site.register(UserTeam)
admin.site.register(Game)
admin.site.register(Court)
admin.site.register(UserGame)
admin.site.register(UserRating)
