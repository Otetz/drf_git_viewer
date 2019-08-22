from rest_framework import serializers

from drf_git_viewer.last_commit.models import LastCommit


class LastCommitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LastCommit
        fields = ['commit', 'commit_date', 'branch', 'version', 'started', 'uptime_seconds']
