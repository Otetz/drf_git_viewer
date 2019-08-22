import datetime

from django.conf import settings
from git import Repo
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class LastCommitView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        repo = Repo(settings.GIT_ROOT)
        started = settings.STARTED
        content = {
            'commit': repo.head.commit.hexsha,
            'commit_date': repo.head.commit.committed_datetime.isoformat(timespec='seconds'),
            'branch': str(repo.active_branch),
            'started': started.isoformat(timespec='seconds'),
            'uptime_seconds': (datetime.datetime.utcnow() - started).total_seconds(),
        }
        return Response(content)
