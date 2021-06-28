from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.views import status
from .models import Question

# Create your tests here.
class PostQuestionAPI(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('api-question-list', kwargs={'version': 'v1'})

    def test_create_post(self):
        self.assertEquals(
            Question.objects.count(),
            0
        )
        data = {
            'title': 'title',
            'body': 'body'
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            Question.objects.count(),
            1
        )
        post = Question.objects.first()
        self.assertEquals(
            post.title,
            data['title']
        )
        self.assertEquals(
            post.text,
            data['body']
        )

    


class QuestionDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        self.post = Question(title='title2', body='text2')
        self.post.save()
        self.url = reverse('api-question-details', kwargs={'version': 'v1', 'pk': self.post.pk})

    def test_get_question_details(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        self.assertEquals(
            data['pk'],
            str(self.post.pk)
        )
        self.assertEquals(
            data['title'],
            self.post.title
        )
        self.assertEquals(
            data['body'],
            self.post.text
        )

    def test_update_post(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        data['title'] = 'new_title'
        data['body'] = 'new_body'
        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.post.refresh_from_db()
        self.assertEquals(
            self.post.title,
            data['title']
        )
        self.assertEquals(
            self.post.text,
            data['body']
        )

    def test_delete_post(self):
        self.assertEquals(
            Question.objects.count(),
            1
        )
        response = self.client.delete(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEquals(
            Question.objects.count(),
            0
        )
