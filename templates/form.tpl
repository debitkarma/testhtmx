<!doctype html>

<html lang="en">

<head>
  <meta charset="utf-8">
  <script src="https://unpkg.com/htmx.org@2.0.2"
    integrity="sha384-Y7hw+L/jvKeWIRRkqWYfPcvVxHzVzn5REgzbawhxAuQGwX1XWe70vji+VSeHOThJ"
    crossorigin="anonymous"></script>
  <title></title>

  <!--<link rel="stylesheet" href="css/styles.css?v=1.0">-->

</head>

<body>
  <script src="/static/js/htmx.js"></script>
  <div class="header">
    <h1>Test Page for HTMX</h1>
  </div>
  <div class="top">
    <h2>Testing Form Progress</h2>
    <p>Welcome <a href="/hello/{{name}}">{{name}}!!</a></p>
  </div>
  <div class="rendered-form">
    <form hx-post="/hello/{{name}}/running">
      <div class="formbuilder-text form-group field-input">
        <label for="input" class="formbuilder-text-label">Text
          <br>
        </label>
        <input type="text" placeholder="write something here" class="form-control" name="input" access="false"
          value="default_text_form" maxlength="20" id="input">
      </div>
      <div class="formbuilder-number form-group field-number_of_times">
        <label for="number_of_times" class="formbuilder-number-label">Number</label>
        <input type="number" class="form-control" name="number_of_times" access="false" value="3" min="1" max="10"
          step="1" id="number_of_times">
      </div>
      <div class="formbuilder-button form-group field-submit">
        <button type="submit" class="btn-default btn" name="submit" access="false" id="submit">Submit</button>
      </div>
    </form>
  </div>
  <div id="results">
    <p></p>
  </div>
  <div id="testing html">
    <p>
      <a href="/running">./running</a>
    </p>
    <p>
      <a href="/running">/running</a>
    </p>
    <p>
      <a href="running">running</a>
    </p>
    <p>
      <a href="{{name}}/running">{{name}}/running</a>
    </p>
  </div>
</body>

</html>