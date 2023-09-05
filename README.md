# AI Role Play

## Requirements

Install python and set up a virtual env as usual.
The run:

```sh
pip install -e ".[dev,test]"
```

## Run the app

Set the OpenAI API key first:

```sh
export OPENAI_API_KEY="..."
```

Or create a `.env` file, which is loaded automatically by the app.

Then run the app with:

```sh
streamlit run app.py --server.runOnSave True
```
