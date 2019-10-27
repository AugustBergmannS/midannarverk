
{% extends "base.html" %}

{% block innihald %}
    <div class="wrapper">
        {%for i in oneco%}
            <p><a href="/company/{{i}}"  class="stodvar"><img src="/static/{{i}}.png"></a></p>
        {%endfor%}
    </div>
    <div class="upplysingar">
        <h1>Besta verðið</h1>
        <p>Ódýrasta bensínið: {{minbensin}} kr. er hjá {{bensinnafn}}, {{nafnbensinstodvar}}</p>
        <p>Ódýrasta díesel olían: {{mindiesel}} kr. er hjá {{dieselnafn}}, {{nafndieselstodvar}}</p>
        <p>Síðast uppfært: {{ 0 | getdate }}</p>
    </div>
{% endblock %}