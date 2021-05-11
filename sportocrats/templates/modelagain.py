from django.db import models
class Player_Male(models.Model):
    id=models.AutoField(primary_key=True)
    sid=models.CharField(max_length=8)
    first_name=models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=40)
    sports=models.CharField(max_length=40)

    def __str__(self):
        return self.first_name

class cricket_male(models.Model):
    cricket_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class football_male(models.Model):
    football_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class basketball_male(models.Model):
    basketball_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class chess_male(models.Model):
    chess_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class table_tennis_male(models.Model):
    table_tennis_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class badminton_male(models.Model):
    badminton_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class athletics_male(models.Model):
    athletics_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class Player_female(models.Model):
    id = models.AutoField(primary_key=True)
    sid=models.CharField(max_length=8)
    first_name=models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=40)
    sports=models.CharField(max_length=40)

    def __str__(self):
        return self.first_name


class admin_sports(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=40)
    sports=models.CharField(max_length=40)
    post=models.CharField(max_length=40)

    def __str__(self):
        return self.first_name


class cricket_female(models.Model):
    cricket_female_id=models.OneToOneField(Player_female,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class football_female(models.Model):
    football_female_id=models.OneToOneField(Player_female,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class basketball_female(models.Model):
    basketball_female_id=models.OneToOneField(Player_female,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class chess_female(models.Model):
    chess_female_id=models.OneToOneField(Player_female,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class table_tennis_female(models.Model):
    table_tennis_female_id=models.OneToOneField(Player_female,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class badminton_female(models.Model):
    badminton_female_id=models.OneToOneField(Player_female,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)

class athletics_female(models.Model):
    athletics_female_id=models.OneToOneField(Player_female,on_delete=models.CASCADE,primary_key=True)
    team_no=models.IntegerField()
    result=models.CharField(max_length=40)
    performance=models.CharField(max_length=40)