{% extends "base.html" %}

{% block innihald %}
    <table>
        <tr>
          <th>Fyrirtæki</th>
          <th>Staður</th> 
        </tr>
        {%for i in stodvar%}
            <tr>
                <td><a href="/{{i["company"]}}/{{i["name"]}}">{{i["company"]}}</a></td>
                <td>{{i["name"]}}</td>
            </tr>
        {%endfor%}
    </table>
    <h3>Fjöldi stöðva: {{fjoldi}}</h3>
{% endblock %}