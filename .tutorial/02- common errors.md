# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## If You Don't Ask.....

👉 What's the problem here?


```python
from flask import Flask

app = Flask(__name__)

@app.route("/process", methods=["POST"])
```

<details> <summary> 👀 Answer </summary>

I forgot to import the `request` library. This will throw an internal server error with the text 'request is not defined' in there somewhere.

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/process", methods=["POST"])
```

</details>

## Inputs Anonymous

👉 What's the problem here?


```python
page = """<form method = "post" action="/process">
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
```

<details> <summary> 👀 Answer </summary>

I've not given each of my options the  `name` attribute. The data input doesn't get stored anywhere so it can't be passed on. This will throw a 'Bad Request'.

```python
page = """<form method = "post" action="/process">
    <p>Name: <input type="text" name="username" required> </p>
    <p>Email: <input type="Email" name="email"> </p>
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
```

</details>
