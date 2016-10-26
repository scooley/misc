from stackapi import StackAPI

site = StackAPI('stackoverflow')
comments = site.fetch('comments')

print comments
