---
layout: page
permalink: /noticias/
title: global.maisnoticias
---

<div  class="gallery">
    <div id="team" class="team">
        {% capture path %}/img/noticias/{% endcapture %}
        {% assign novidades = site.static_files | reverse  %}
        {% for file in novidades %}
            {% if file.path contains '/img/noticias/' %}
                {% unless file.path contains 'docs/' %}
                    <a href="{{ file.path }}" class="gallery-item expandable-box image-link">
                        <div class="expandable-box-top">
                            <img src="{{ file.path }}" /> 
                        </div>
                        <div class="expandable-box-bottom">
                            <span><svg class="icon icon-magnify"><use xlink:href="#icon-magnify"></use></svg></span>
                            <span>{% t global.click %}</span>
                        </div>
                    </a>
                {% endunless %}
            {% endif %}
        {% endfor %}
    </div>
</div>
