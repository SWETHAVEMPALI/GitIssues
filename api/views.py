from datetime import datetime, timedelta
from django.shortcuts import render
from github import Github, GithubException


def github(request):
    search_result = {}
    client = Github()
    if 'repolink' in request.GET:
        repo_link = request.GET['repolink']
        if repo_link:
            repoPath = repo_link.split('/')
            username, repositoryName = repoPath[-2], repoPath[-1]
            try:
                currentdatetime = datetime.now()
                open_issues_PRs = client.get_user(username).get_repo(repositoryName).get_issues(state='open')
                issues_PRs_updated_today = client.get_user(username).get_repo(repositoryName).get_issues(state='open', since=(currentdatetime - timedelta(hours=24)))
                issues_PRs_updated_this_week = client.get_user(username).get_repo(repositoryName).get_issues(state='open', since=(currentdatetime - timedelta(days=7)))

                open_issues = filter(lambda x: not x.pull_request, open_issues_PRs)
                issues_updated_today = filter(lambda x: not x.pull_request, issues_PRs_updated_today)
                issues_updated_this_week = filter(lambda x: not x.pull_request, issues_PRs_updated_this_week)

                total_open_issues = len(list(open_issues))
                total_issues_updated_today = len(list(issues_updated_today))
                total_issues_updated_this_week = len(list(issues_updated_this_week))
                issues_updated_earlier = total_open_issues - total_issues_updated_today - total_issues_updated_this_week

                search_result['repo_name'] = repositoryName
                search_result['total_open_issues'] = total_open_issues
                search_result['total_issues_updated_today'] = total_issues_updated_today
                search_result['total_issues_updated_this_week'] = total_issues_updated_this_week
                search_result['issues_updated_earlier'] = issues_updated_earlier
                search_result['success'] = True

            except GithubException as ge:
                search_result['message'] = ge.data['message']
                search_result['success'] = False

    return render(request, 'github.html', {'search_result': search_result})
