from django.db import models
from django.core.validators import (MaxValueValidator,MinValueValidator)
class Player_Male(models.Model):
    id=models.AutoField(primary_key=True)
    sid=models.IntegerField(validators=[MaxValueValidator(21000000),MinValueValidator(17000000)])
    first_name=models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=40)
    sports=models.CharField(max_length=40)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.sports} {self.id}'

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
        return f'{self.first_name} {self.last_name} {self.sports} {self.id}'


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


class screening_cricket_male(models.Model):
    screening_cricket_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    qualified=models.CharField(max_length=40)

class screening_football_male(models.Model):
    screening_football_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    qualified=models.CharField(max_length=40)

class screening_basketball_male(models.Model):
    screening_basketball_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    qualified=models.CharField(max_length=40)

class screening_chess_male(models.Model):
    screening_chess_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    qualified=models.CharField(max_length=40)

class screening_table_tennis_male(models.Model):
    screening_table_tennis_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    qualified=models.CharField(max_length=40)

class screening_badminton_male(models.Model):
    screening_badminton_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    qualified=models.CharField(max_length=40)

class screening_athletics_male(models.Model):
    screening_athletics_male_id=models.OneToOneField(Player_Male,on_delete=models.CASCADE,primary_key=True)
    qualified=models.CharField(max_length=40)


class selection_cricket_male(models.Model):
    selection_cricket_male_id=models.OneToOneField(cricket_male,on_delete=models.CASCADE,primary_key=True)
    status=models.CharField(max_length=40)

class selection_football_male(models.Model):
    selection_football_male_id=models.OneToOneField(football_male,on_delete=models.CASCADE,primary_key=True)
    status=models.CharField(max_length=40)

class selection_basketball_male(models.Model):
    selection_basketball_male_id=models.OneToOneField(basketball_male,on_delete=models.CASCADE,primary_key=True)
    status=models.CharField(max_length=40)

class selection_chess_male(models.Model):
    selection_chess_male_id=models.OneToOneField(chess_male,on_delete=models.CASCADE,primary_key=True)
    status=models.CharField(max_length=40)

class selection_table_tennis_male(models.Model):
    selection_table_tennis_male_id=models.OneToOneField(table_tennis_male,on_delete=models.CASCADE,primary_key=True)
    status=models.CharField(max_length=40)

class selection_badminton_male(models.Model):
    selection_badminton_male_id=models.OneToOneField(badminton_male,on_delete=models.CASCADE,primary_key=True)
    status=models.CharField(max_length=40)

class selection_athletics_male(models.Model):
    selection_athletics_male_id=models.OneToOneField(athletics_male,on_delete=models.CASCADE,primary_key=True)
    status=models.CharField(max_length=40)

class selection_badminton_female(models.Model):
    selection_badminton_female_id=models.OneToOneField(badminton_female,on_delete=models.CASCADE,primary_key=True)
    status=models.CharField(max_length=40)

class selection_table_tennis_female(models.Model):
    selection_table_tennis_female_id=models.OneToOneField(table_tennis_female,on_delete=models.CASCADE,primary_key=True)
    status=models.CharField(max_length=40)

class selection_chess_female(models.Model):
    selection_chess_female_id=models.OneToOneField(chess_female,on_delete=models.CASCADE,primary_key=True)
    status=models.CharField(max_length=40)


class sports_equipments(models.Model):
    sports_equipments_id=models.AutoField(primary_key=True)
    sports_name=models.CharField(max_length=40)
    equipment_name=models.CharField(max_length=40)
    no_of_qty_available=models.CharField(max_length=40)
    no_of_qty_required = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.sports_name} {self.equipment_name}'