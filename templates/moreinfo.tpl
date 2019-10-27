{% extends "base.html" %}

{% block innihald %}
    <main class="upplysingar">
        <p>Söluaðili: {{soluadili}}</p>
        <p>Staður: {{nafn}}</p>
        <p>Verð á 1. lítra af Bensíni, 95 oktan: {{bensin}}</p>
        <p>Verð á 1. lítra af Dísel olíu: {{diesel}}</p>
        <p>Staðsetning bensínstöðvar: <a href="https://www.google.com/maps/@{{lat}},{{lon}},18z/">{{stadsetning}}Staðsetning á Google korti</a></p>
    </main>
{% endblock %}