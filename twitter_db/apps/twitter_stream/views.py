from django.views import generic

import models


class StatusView(generic.TemplateView):
    template_name = 'twitter_stream/status.html'

    def get_context_data(self, **kwargs):

        processes = models.StreamProcess.get_current_stream_processes()
        running = False
        for p in processes:
            if p.status == models.StreamProcess.STREAM_STATUS_RUNNING:
                running = True
                break

        result = {
            'running': running,
            'credentials': models.TwitterAPICredentials.objects.all(),
            'filter_terms': models.FilterTerm.objects.filter(enabled=True),
            'processes': processes,
            'tweet_count': models.Tweet.objects.count(),
        }

        return result

status_view = StatusView.as_view()