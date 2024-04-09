# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
from flask import Flask

app = Flask(__name__)

@app.route("/process", methods=["POST"])

def process():
  page = ""
  form = request.form

  if form["baldies"] == "david":
    page += f"You're alright {form['username']}"
  else:
    page += f"You've picked wrong {form['username']}"

  return page


@app.route('/')
def index():
  page = """<form method = "post" action="process">
    <p>Name: <input type="text" required> </p>
    <p>Email: <input type="Email"> </p>
    <input type="hidden" name="userID" value="232"> </p>

    <p>
      Fave Baldy: 
      <select name="baldies">
        <option>David</option>
        <option>Jean Luc Picard</option>
        <option>Yul Brynner</option>
      </select>
    </p>

    <button type="submit">Save Data</button>
  </form>
    
    
    """
  return page
  
app.run(host='0.0.0.0', port=81)

```
<details> <summary> 👀 Answer </summary>

```python
from flask import Flask, request ###### Didn't import 'request'

app = Flask(__name__)

@app.route("/process", methods=["POST"])

def process():
  page = ""
  form = request.form

  if form["baldies"] == "David":
    page += f"You're alright {form['username']}"
  else:
    page += f"You've picked wrong {form['username']}"

  return page


@app.route('/')
def index():
  page = """<form method = "post" action="/process"> ####### No / before the action. Well done if you spotted this
  
    <p>Name: <input type="text" name="username" required> </p>
    <p>Email: <input type="Email" name="email"> </p>
    ###### No 'name' attributes in the two options above
    <input type="hidden" name="userID" value="232"> </p>

    <p>
      Fave Baldy: 
      <select name="baldies">
        <option>David</option>
        <option>Jean Luc Picard</option>
        <option>Yul Brynner</option>
      </select>
    </p>

    <button type="submit">Save Data</button>
  </form>
    
    
    """
  return page
  
app.run(host='0.0.0.0', port=81)

```

</details>