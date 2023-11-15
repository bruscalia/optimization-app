# optimization-app

A white label repository for a streamlit numerical optimization web application.

<p align="left">
  <img src="./assets/icon_tsp.png" width="200" title="icon tsp">
</p>

## Execution

### Python

To run locally, please install Python libraries included in the file `requirements.txt`

```pip install -r requirements.txt```

Then, exexcute streamlit via command line:

```streamlit run app.py```

### Docker

To build an image locally, make sure you have docker installed in your computer and run the following command:

```docker build -t my_app:latest .```

You can replace `my_app` by any image name you would like and `latest` by any version.

Then you can run your app by running

```docker run -p 8501:8501 my_app:latest```


## Contact

You can reach out to me at bruscalia12@gmail.com
