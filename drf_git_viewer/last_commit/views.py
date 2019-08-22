import datetime

from dateutil import tz
from django.conf import settings
from git import Repo
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class LastCommitView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    # noinspection PyUnusedLocal,PyShadowingBuiltins
    def get(self, request, format=None):
        repo = Repo(settings.GIT_ROOT)
        started = settings.STARTED
        tags = sorted(repo.tags, key=lambda tag: tag.name, reverse=True)
        commit_date_local = repo.head.commit.committed_datetime
        commit_date_utc = (commit_date_local + datetime.timedelta(seconds=repo.head.commit.committer_tz_offset)) \
            .replace(tzinfo=tz.UTC)

        content = {
            'commit': repo.head.commit.hexsha,
            'commit_date': commit_date_utc.isoformat(timespec='seconds').replace('+00:00', 'Z'),
            'branch': str(repo.active_branch),
            'version': tags[0].name,
            'started': started.isoformat(timespec='seconds') + 'Z',
            'uptime_seconds': int((datetime.datetime.utcnow() - started).total_seconds()),
        }
        return Response(content)
