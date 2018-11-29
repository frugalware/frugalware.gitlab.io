hook:
	cd .git && python /srv/ftp/pub/other/git-hooks/git-hooks.py post-receive
	python hooks/post-receive-news.py
	python hooks/post-receive-security.py
