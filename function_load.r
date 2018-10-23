loadLibs = function (lista){
  # Run through the list with libs names
  for (x in lista){
    # If not in require, then install the lib
    if (!require(x, character.only = TRUE)){
      install.packages(x, dependencies = TRUE) 
      # Apply the value in require, for load the lib in R
      sapply(x, library, character.only = TRUE)
    } 
  }
}
