import sys

def find_schoolkid_child(child_name):
	from datacenter.models import Schoolkid
	try:
		schoolkid_child = Schoolkid.objects.get(full_name__contains=child_name)
		return schoolkid_child
	except Schoolkid.DoesNotExist:
		print("Не найдено не одного ученика с таким именем")
	except Schoolkid.MultipleObjectsReturned:
		print("С таким именем слишком много учеников")
	sys.exit(1)
	

def create_commendation(child_name,subject_name):
	from datacenter.models import Subject
	from datacenter.models import Lesson
	from datacenter.models import Commendation
	schoolkid_child = find_schoolkid_child(child_name)
	subject = Subject.objects.filter(title=subject_name, year_of_study=schoolkid_child.year_of_study).first()
	lesson = Lesson.objects.filter(year_of_study=schoolkid_child.year_of_study, subject=subject, group_letter=schoolkid_child.group_letter).order_by("-date").first()
	Commendation.objects.create(text="Хвалю", created=lesson.date, schoolkid=schoolkid_child, subject=lesson.subject, teacher=lesson.teacher)
	sys.exit(1)
	

def fix_marks(schoolkid):
	from datacenter.models import Mark
	marks_child_23 = Mark.objects.filter(schoolkid=schoolkid,points__in=[2,3])
	for mark in marks_child_23:
		mark.points = 5
		mark.save()


def remove_chastisements(schoolkid):
	from datacenter.models import Chastisement
	Chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
	Chastisements.delete()