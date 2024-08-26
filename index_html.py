# Autogenerated file
def render(led_value):
    yield """
<!DOCTYPE html>
<html>
  <head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>MicroPython Webserver</title>
    <link rel=\"stylesheet\" href=\"static/css/entireframework.min.css\" />
    <link rel=\"stylesheet\" href=\"static/css/index.css\" />
  </head>
  <body>
    <nav class=\"nav\" tabindex=\"-1\" onclick=\"this.focus()\">
      <div class=\"container\">
        <a class=\"pagename current\" href=\"#\">www.donskytech.com</a>
        <a href=\"#\">One</a>
        <a href=\"#\">Two</a>
        <a href=\"#\">Three</a>
      </div>
    </nav>
    <button class=\"btn-close btn btn-sm\">×</button>
    <div class=\"container\">
      <div class=\"hero\">
        <h1 class=\"title\">MicroPython Webserver</h1>
        <div class=\"toggle-div\">
            <p class=\"label\">Toggle Switch</p>
            <input type=\"checkbox\" id=\"switch\" onclick=\"toggleButtonSwitch()\" """
    if led_value == 1:
        yield """ checked """
    yield """/><label for=\"switch\">Toggle</label>
        </div>
      </div>
      <div
          class=\"RadialProgress\"
          role=\"progressbar\"
          aria-valuenow=\"25\"
          aria-valuemin=\"0\"
          aria-valuemax=\"100\"
        >
        </div>
        <input type=\"range\" value=\"25\" min=\"0\" max=\"100\" />
    </div>
    
    <script src=\"static/js/index.js\"></script>
    
  </body>
</html>"""
