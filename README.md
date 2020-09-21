
## README Action Template

### 🐾 What's this?

This is a repository with reference to [waka-readme-stats](https://github.com/anmol098/waka-readme-stats).
You can make `README Update Action` easily with this repository.

### 🐾 How to setup as coder? 

Firstly, you can fork this `readme-action` repository (Of course, you can copy!).
We call forked repository `FR` (Forked Repository) below.

In `FR` repository, you will have `insert_text.py`.
You can rewrite `insert_text.py`!

### 🐾 How to setup as user? 

If you finish `FR` repository's work (so, rewriting `insert_text.py`), 
you have to add `<!--START_SECTION:custom_action-->`, `<!--END_SECTION:custom_action-->` to your account's README.md.

And your readme profile repository, you have to make

`.github/workflows/action.yml` (action.yml's name is anything ok.)

```yaml
name: Action

on:
   schedule:
     - cron: "0 31 * * *"

jobs:
  update-readme:
    name: Update Readme with Metrics
    runs-on: ubuntu-latest
    steps:
      - uses: Ganariya/readme-action@master #Your FR's action
        with:
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
          USERNAME: "Ganariya"
```



