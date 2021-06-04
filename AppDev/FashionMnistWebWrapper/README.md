<b>Deploying the ML model on Heroku</b>
<br>

Follow the fashion_mnist tutorial on tensorflow and add the line `tf.keras.models.save_model(model, 'recognition_model.hdf5')` after model.fit in your script

Then place the exported .hdf5 file in this repository and push to your github branch
After pushing, login on heroku and create a new pipeline by connecting to your branch

This should start an autodeploy process which uses the `shell` script as well as the `procfile` to run and create the model.
