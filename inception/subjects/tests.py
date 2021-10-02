from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Subject
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import Http404
from django.http import HttpRequest
from django.db.models import Max
from subjects.views import subject


# Create your tests here.

class UserViewTestCase(TestCase):
    def test_index_view(self):
        c = Client()
        user = User.objects.create(username='user4', password='1234', email='user1@example.com')
        c.force_login(user)
        response = c.get(reverse('subjects:index'))
        self.assertEqual(response.status_code, 200)

class ViewTestCase(TestCase):

    def setUp(self):

        self.user_ad = User.objects.create_user(username="user6", email="user6@test.com", password="user6")
        self.user = User.objects.create_user(username="user7", email="user7@test.com", password="user7")

        subject = Subject.objects.create(subject_name = 'calculus2',subject_code = 'MA214',limited_seat = 2,status = "free",seat =2)


    def test_subject(self):
        c = Client()
        s = Subject.objects.first()
        response = c.get(reverse('subjects:subject',args=(s.id,)), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_invalid_flight_page(self):

        max_id = Subject.objects.all().aggregate(Max("id"))['id__max']

        c = Client()
        response = c.get(reverse('subjects:subject', args=(max_id+1,)))
        self.assertEqual(response.status_code, 404)


    def test_Course_view(self):
        self.c = Client()
        self.c.login(username='user6', password='user6')
        response = self.c.get(reverse('subjects:Course'))
        self.assertEqual(response.status_code, 200)

    def test_Course_view_stu(self):
        self.c = Client()
        self.c.login(username='user7', password='user7')
        response = self.c.get(reverse('subjects:Course'))
        self.assertEqual(response.status_code, 200)
        
    def test_login_enroll(self):
        s1 = Subject.objects.first()
        u2 = Client()
        response = u2.get(reverse('subjects:enroll', args=(s1.id,)))

    def test_enroll(self):
        c = Client()
        c.login(username='user6', password='user6')
        s = Subject.objects.first()
        s.seat = 1
        s.save
        response = c.get(reverse('subjects:enroll',args=(s.id,)))
        self.assertEqual(s.limited_seat,s.studentInClass.count()+s.seat)

    def test_full(self):
        c = Client()
        c.login(username='user6', password='user6')
        subjectfull = Subject.objects.create(subject_name = 'calculus2',subject_code = 'MA214',limited_seat = 2,status = "free",seat =0)
        response = c.get(reverse('subjects:enroll',args=(subjectfull.id,)))

        
    def test_login(self):
        s2 = Subject.objects.first()
        u = Client()
        response = u.get(reverse('subjects:drop', args=(s2.id,)))

    def test_drop(self):
        c = Client()
        c.login(username='user6', password='user6')
        subjecttodrop = Subject.objects.first()
        response = c.get(reverse('subjects:enroll',args=(subjecttodrop.id,)))
        response = c.get(reverse('subjects:drop',args=(subjecttodrop.id,)))

    


class whatevertest(TestCase):

    def create_test(self,
            subject_name = 'DiscreteMath',
            subject_code = 'CN200',
            semester = '1',
            year = '2021'):

        return Subject.objects.create(subject_name=subject_name, subject_code=subject_code, semester=semester, year=year)



    def test_creation(self):
        w = self.create_test()
        self.assertTrue(isinstance(w, Subject))
        expected_object_name = f"{w.subject_code} : {w.subject_name}"
        self.assertEqual(w.__str__(), expected_object_name )








