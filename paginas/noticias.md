---
layout: page
permalink: /noticias/
title: global.maisnoticias
---

<div  class="gallery">
    <div id="team" class="team">
        {% capture path %}/img/Noticias/{% endcapture %}
        {% assign novidades = site.static_files | reverse  %}
        {% for file in novidades %}
            {% if file.path contains '/img/Noticias/' and file.extname == '.jpg' %}
                {% unless file.path contains 'docs/' %}
                    <a href="{{ file.path }}" class="gallery-item expandable-box image-link">
                        <div class="expandable-box-top">
                            <img src="{{ file.path }}" /> 
                        </div>
                        <div class="expandable-box-bottom">
                            <span><svg class="icon icon-magnify"><use xlink:href="#icon-magnify"></use></svg></span>
                            <span><svg class="icon icon-pdf"><use xlink:href="#icon-pdf"></use></svg></span>
                        </div>
                    </a>
                {% endunless %}
            {% endif %}
        {% endfor %}
    </div>
</div>
