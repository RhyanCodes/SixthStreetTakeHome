# SixthStreetTakeHome
## Discussion:
1. How would you approach versioning of this library?
I would approach versioning by embedding the version number at the top and add a configuration file for installing via pip commands.
2. How would we go about publishing this library?
   Update the configuration file for metadata and dependencies and upload it to Pypl
4. How would you design this if it was going to be a service rather than a library?
   I would wrap the logic in FastAPI and use Redis cachine to avoid rate limits
5. - Approximation of time spent on this exercise and any noteworthy assumptions made
to complete the case.
90 minutes. 
6. If LLMs were used, include a short description of your thought process in selecting and
querying the model.
I used copilot in VS code with Gemini 3 for auto complete
