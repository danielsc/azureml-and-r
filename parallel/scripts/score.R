#' Copyright(c) Microsoft Corporation.
#' Licensed under the MIT license.



init <- function()
{
  model_path <- Sys.getenv("AZUREML_MODEL_DIR")
  message(paste(list.files(path = model_path, recursive = TRUE), collapse=', '))
  
  model <- readRDS(file.path(model_path,"model.rds"))
  message("model is loaded")
  
  function(data)
  {
    prediction <- predict(model, data)
    #result <- as.character(prediction)
    prediction
  }
}


