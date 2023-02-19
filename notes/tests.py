from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Notes

TEST_USER = {
    'username': 'testuser',
    'email': 'test@email.com',
    'password': 'secret!!!'
}
TEST_NOTE = {'title': "A Title", 'text': "Body Content"}


class NotesTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username=TEST_USER['username'],
            email=TEST_USER['email'],
            password=TEST_USER['password']
        )
        self.note = Notes.objects.create(
            title=TEST_NOTE['title'],
            text=TEST_NOTE['text'],
            user=self.user
        )

    def test_string_representation(self):
        dummy_title = 'Sample Title'
        note = Notes.objects.create(title=dummy_title, user=self.user)
        self.assertEqual(str(note), note.title)

    def test_note_content(self):
        self.assertEqual(str(self.note.title), TEST_NOTE['title'])
        self.assertEqual(str(self.note.text), TEST_NOTE['text'])
        self.assertEqual(self.note.user, self.user)

    def test_note_list_view(self):
        self.client.login(
            username=TEST_USER['username'], password=TEST_USER['password']
        )
        response = self.client.get(reverse('notes.list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, TEST_NOTE['title'])
        self.assertTemplateUsed(response, 'notes/notes_list.html')

    def test_note_detail_view(self):
        response = self.client.get('/quicknotes/note/1')
        no_response = self.client.get('/quicknotes/note/99999')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, TEST_NOTE['title'])
        self.assertTemplateUsed(response, 'notes/note.html')
