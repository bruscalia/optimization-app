# optimization-app

A white label repository for a streamlit numerical optimization web application.

To learn more about numerical optimization and operations research you can find more material in my [Online Course](https://www.udemy.com/course/numerical-optimization-and-operations-research-in-python/?referralCode=FC93E35606AC78F1A8C5), [Medium stories](https://medium.com/@bruscalia12), and [Github repository](https://github.com/bruscalia/optimization-demo-files).

## Usage

1) Fork or clone this repository
2) Modify the [model](./optimize/model.py) file to suit your problem
3) Modify the [app](./app.py) file to select input/output type and include new elements to your own interface.

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
