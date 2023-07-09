def create_commendation(child_name,Subject_name):
	import sys
	from datacenter.models import Subject
	from datacenter.models import Lesson
	from datacenter.models import Commendation
	from datacenter.models import Schoolkid
	try:
		schoolkid_child = Schoolkid.objects.get(full_name__contains=child_name)
	except Schoolkid.DoesNotExist:
		print("Не найдено не одного ученика с таким именем")
		sys.exit(1)
	except Schoolkid.MultipleObjectsReturned:
		print("С таким именем слишком много учеников")
		sys.exit(1)
	subject = Subject.objects.filter(title=Subject_name, year_of_study=schoolkid_child.year_of_study).order_by("-year_of_study").first()
	lesson = Lesson.objects.filter(year_of_study=schoolkid_child.year_of_study, subject=subject, group_letter=schoolkid_child.group_letter).order_by("-date").first()
	Commendation.objects.create(text="Хвалю", created=lesson.date, schoolkid=schoolkid_child, subject=lesson.subject, teacher=lesson.teacher)
	

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