from django.test import TestCase

# Create your tests here.
from django.test.client import Client
from .models import Doctor
class ReceptionTestCase(TestCase):
    def _createDoctor(self):
        doctor = Doctor()
        doctor.fio = "Test"
        doctor.save()

    def test_create_new_reception(self):
        c = Client()
        self._createDoctor()

        response = c.post('/add_reception/',{'fio':'Иван Иванов','date':'2018-01-01','time':'12:00','doctor':'1'})
        self.assertEqual(response.json()['RESULT'],True)

    def test_create_two_reception(self):
        c = Client()
        self._createDoctor()

        response = c.post('/add_reception/',
                          {'fio': 'Иван Иванов', 'date': '2018-01-01', 'time': '12:00', 'doctor': '1'})
        self.assertEqual(response.json()['RESULT'], True)
        response = c.post('/add_reception/',
                          {'fio': 'Петр Петров', 'date': '2018-01-01', 'time': '12:00', 'doctor': '1'})
        self.assertEqual(response.json()['RESULT'], False)

    def test_create_new_reception_not_working(self):
        c = Client()
        self._createDoctor()

        response = c.post('/add_reception/',
                          {'fio': 'Иван Иванов', 'date': '2017-04-22', 'time': '12:00', 'doctor': '1'})

        self.assertEqual(response.json()['RESULT'], False)
        response = c.post('/add_reception/',
                          {'fio': 'Петр Петров', 'date': '2017-04-20', 'time': '19:00', 'doctor': '1'})
        self.assertEqual(response.json()['RESULT'], False)