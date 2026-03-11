app.ml.model
============

.. py:module:: app.ml.model

.. autoapi-nested-parse::

   Advanced ML Processing & Modeling
   =================================

   This package contains high-performance weather prediction models.
   By refactoring this entire module, we are forcing AutoAPI to regenerate
   the index and diagrams.



Classes
-------

.. autoapisummary::

   app.ml.model.GlobalWeatherNet
   app.ml.model.HyperParameters


Module Contents
---------------

.. py:class:: GlobalWeatherNet(hparams: HyperParameters, model_name: str = 'GlobalNet-V2')

   A deep learning model architecture for global-scale weather forecasting.

   This class replaces the previous `WeatherPredictor` to test if
   AutoAPI correctly re-indexes the new class name and suppresses the old one.

   :param hparams: The hyperparameter configuration for the network.
   :type hparams: :py:class:`HyperParameters`
   :param model_name: Identifier for the model instance.
   :type model_name: :py:class:`str`, *default* ``"GlobalNet-V2"``

   .. attribute:: version

      The version string for the model logic.

      :type: :py:class:`str`


   .. py:method:: export_onnx(path: str)

      Exports the current model state to the ONNX format.

      :param path: File system path where the .onnx file will be saved.
      :type path: :py:class:`str`



   .. py:method:: train_step(data: Dict[str, Any]) -> float

      Executes a single training iteration.

      :param data: A dictionary containing 'features' and 'targets' tensors.
      :type data: :py:class:`Dict[str`, :py:class:`Any]`

      :returns: The loss value after the optimization step.
      :rtype: :py:class:`float`

      .. admonition:: Notes

         This method uses a mock stochastic gradient descent update.
         It is intended for testing AutoAPI's ability to render 'Notes' blocks.

      :Warns: **UserWarning** -- If the batch size in `data` differs from `hparams.batch_size`.



   .. py:attribute:: hparams


   .. py:attribute:: model_name
      :value: 'GlobalNet-V2'



   .. py:attribute:: version
      :value: '2.0.0'



.. py:class:: HyperParameters

   Configuration for model training.

   .. attribute:: epochs

      Number of full passes through the dataset.

      :type: :py:class:`int`

   .. attribute:: batch_size

      Number of samples per gradient update.

      :type: :py:class:`int`

   .. attribute:: layers

      Number of neurons in each hidden layer.

      :type: :py:class:`List[int]`


   .. py:attribute:: batch_size
      :type:  int
      :value: 64



   .. py:attribute:: epochs
      :type:  int
      :value: 100



   .. py:attribute:: layers
      :type:  Optional[List[int]]
      :value: None



