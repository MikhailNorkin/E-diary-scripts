def create_commendation(child_name,Subject_name):
	from datacenter.models import Schoolkid
	from django.core.exceptions import ObjectDoesNotExist
	from django.core.exceptions import MultipleObjectsReturned
	import sys
	try:
		e = Schoolkid.objects.filter(full_name__contains=child_name).get()
	except ObjectDoesNotExist:
		print("Не найдено не одного ученика с таким именем")
		sys.exit(1)
	except MultipleObjectsReturned:
		return print("С таким именем слишком много учеников")
		sys.exit(1)
	child= Schoolkid.objects.filter(full_name__contains=child_name)[0]
	from datacenter.models import Subject
	Subject_year = Subject.objects.filter(title=Subject_name, year_of_study=child.year_of_study)[0]
	from datacenter.models import Lesson
	Lessons = Lesson.objects.filter(year_of_study = child.year_of_study, group_letter=child.group_letter, subject=Subject_year)
	Lesson_random = random.choice(Lessons)
	from datacenter.models import Commendation
	Commendation.objects.create(text="Хвалю", created=Lesson_random.date,schoolkid=child,subject=Lesson_random.subject,teacher=Lesson_random.teacher)