from jinja2 import Template
from starlite.applications import Starlite
from starlite.middleware import Middleware
from starlite.middleware.sessions import SessionMiddleware
from starlite.responses import PlainTextResponse, HTMLResponse
from starlite_wtf import StarliteForm, CSRFProtectMiddleware, csrf_protect
from wtforms import StringField
from wtforms.validators import DataRequired


class MyForm(StarliteForm):
    name = StringField("name", validators=[DataRequired()])


template = Template(
    """
<html>
  <body>
    <form method="post" novalidate>
      {{ form.csrf_token }}
      <div>
        {{ form.name(placeholder='Name') }}
        {% if form.name.errors -%}
        <span>{{ form.name.errors[0] }}</span>
        {%- endif %}
      </div>
      <button type="submit">Submit</button>
    </form>
  </body>
</html>
"""
)


app = Starlite(
    middleware=[
        Middleware(SessionMiddleware, secret_key="***REPLACEME1***"),  # noqa: S106
        Middleware(CSRFProtectMiddleware, csrf_secret="***REPLACEME2***"),  # noqa: S106
    ]
)


@app.route("/", methods=["GET", "POST"])
@csrf_protect
async def index(request):
    """GET|POST /: form handler"""
    form = await MyForm.from_formdata(request)

    if form.validate_on_submit():
        return PlainTextResponse("SUCCESS")

    html = template.render(form=form)
    return HTMLResponse(html)
