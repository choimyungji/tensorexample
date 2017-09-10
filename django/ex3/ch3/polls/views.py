# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
{% if latest_question_list %}
	<ul>
	{% for question in latest_question_list %}
		<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
	{% endfor %}
	</ul>
{% else %}
	<p>No polls are available</p>
{% endif %}

