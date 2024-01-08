### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
<!-- Python is used mostly for backend development, while Javascript is mostly used for frontend.-->

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
<!-- I could use a get method with a default value, or a try-except block. -->

- What is a unit test?
<!-- A unit test is a way of testing a single functionality separate from the rest of the application/system that is being developed. -->

- What is an integration test?
<!-- A test that makes sure that multiple functionalities or parts of an application work together as expected. -->

- What is the role of web application framework, like Flask?
<!-- Application frameworks are meant for creating a simplified structure for the development of an application. -->

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
<!-- I would weigh the pros and cons of each for my application. A URL query param would probably be more suited for an application that used a lot of filtering and sorting, while passing information as a param in a route URL would be something i would use for a simpler application.-->

- How do you collect data from a URL placeholder parameter using Flask?
<!-- You would use the route decorator and specify the parameter within the route pattern. -->

- How do you collect data from the query string using Flask?
<!-- By using the request object. -->

- How do you collect data from the body of the request using Flask?
<!-- By using the request object and putting a ".{get_json/data/form}" or whatever datatype you're looking for is at the end.-->

- What is a cookie and what kinds of things are they commonly used for?
<!-- A cookie is a small piece of data stored in a user's browser. They are commonly used for analytics, session managment, remembering inputs, and authentication. -->

- What is the session object in Flask?
<!-- Flask session is an object that allows you to store and access user-specific data across requests. -->

- What does Flask's `jsonify()` do?
<!-- It is a helper function that returns a JSON response. -->
