This project is a part of the #djangogirls #bangkok #Thailand on 24th March 2018

Tutorial Git: https://github.com/ggcarrots/django-carrots.git
Tutorial Guideline: https://tutorial.djangogirls.org/en/django_admin/

Pythonanywhere
>> http://ammiiamm.pythonanywhere.com/
>> กรณีต้องการลบโปรเจ็คออก ให้ตามท้ายว่า --nuke : pa_autoconfigure_django.py https://github.com/ammiiamm/djangogirl.git —nuke
>> Login Console เข้าไปเพื่อ pull code และ reload code จากที่ Tab ของ Web

Git
- .gitignore สร้างไฟล์เพื่อ ignore ไฟล์ที่ไม่ต้องการเอาขึ้น
- git reset —hard HEAD เวลาเจอปัญหาไฟล์ conflict หนักๆ

Python Basic
- List เก็บเป็นลิสต์
- Dictionary เก็บเป็น Key กับ Value
- Python มีการ strict เรื่องของ Indent เพราะไม่มี semicolon 

Django
- Framework ที่ช่วยให้ขึ้นเว็บได้ง่ายขึ้น
- Django Route ใช้ Regular Expression
    * ^ for the beginning of the text
    * $ for the end of the text
    * \d for a digit
    * + to indicate that the previous item should be repeated at least once
    * () to capture part of the pattern
- Django View
    * {{ }} ไปดู Data
    * {% %} รันโปรแกรม
- Django Model
    * มีองค์ประกอบอะไร attribute
    * ทำอะไรได้บ้าง function
    * __str__ คล้าย .toString() ในจาวา ใช้โชว์ attribute กรณีมีการ lookup model

Key Commands
>>source myvenv/bin/activate
>>pip install django~=1.11.0
>>django-admin startproject mysite .
>>python manage.py migrate
>>python manage.py runserver
>>python manage.py startapp blog
>>python manage.py createsuperuser

Current Status:
This code has already covered all functions in the tutorial. In between, I've already added "delete" function for extending more about django.
