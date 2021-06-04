This code creates a web wrapper around a trained model and lets users input their image and run it through the trained model.

Steps to set it up:

1. Go to https://github.com/TAMGDrexel/Spotted_Lantern_Flies/tree/main/MLCode_Malik and download the two image repositories.

2. Add the line `tf.keras.models.save_model(model, 'recognition_model.hdf5')` after model.fit

3. Run and train the model by first running the preprocessing script and then the model script

4. A file with the trained exported model should be generated and will be named 'recognition_model.hdf5'

5. Copy and paste the model file into this directory and pip install pipenv

6. Execute the command `pipenv install`

7. Then `pipenv shell`

8. This should create a new bash instance inside your directory.

9. Execute `streamlit run web_app.py` to lauch the web app
