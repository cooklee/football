from django.db import models

class Teams(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    points = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'

class Games(models.Model):
    id = models.BigAutoField(primary_key=True)
    team_home = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_home', blank=True, null=True, related_name='team_home')
    team_home_goals = models.BigIntegerField(blank=True, null=True)
    team_away = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_away', blank=True, null=True, related_name='team_away')
    team_away_goals = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'



