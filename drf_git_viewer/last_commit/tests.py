# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase


class LastCommitTests(APITestCase):
    url = '/last-commit/'

    def test_last_commit(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIsNotNone(response.data)

        self.assertIn('commit', response.data)
        self.assertIn('commit_date', response.data)
        self.assertIn('branch', response.data)
        self.assertIn('version', response.data)
        self.assertIn('started', response.data)
        self.assertIn('uptime_seconds', response.data)

        self.assertIsInstance(response.data['uptime_seconds'], int)
        for name in ['commit', 'commit_date', 'branch', 'version', 'started']:
            self.assertIsInstance(response.data[name], str)

    def test_last_commit_wrong_method(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
