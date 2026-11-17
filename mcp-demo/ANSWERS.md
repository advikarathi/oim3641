# In-class Activity 22: MCP and the Python SDK

## Screenshots

- Part 3: [screenshots/part3-predict-docs.png](screenshots/part3-predict-docs.png)
- Part 5: [screenshots/part5-client-classify.png](screenshots/part5-client-classify.png)
- Part 6: [screenshots/part6-probabilities.png](screenshots/part6-probabilities.png)

## Part 4

**Compare `classify_iris` in `mcp_server.py` with `predict` in `api.py`. Which one does the actual prediction? What does the MCP version add?**

`predict` in `api.py` does the actual prediction. It loads the trained model and calls `model.predict()`. `classify_iris` in `mcp_server.py` never touches the model. It just sends the four measurements to the `/predict` endpoint over HTTP and returns the answer. What the MCP version adds is a way for an AI app to find and use the model on its own. It gives the model a tool name, a plain-English description of what it does and a typed list of inputs. It also turns the result into a readable sentence ("Predicted species: virginica") instead of raw JSON.

## Part 5

**The client printed a tool name, a description and its inputs without reading your code. Where in `mcp_server.py` did each one come from?**

- **Name:** the function name, `def classify_iris`.
- **Description:** the function's docstring.
- **Inputs:** the function's parameter names and their `float` type hints. The SDK turned these into a JSON schema with four `number` fields.

The `@mcp.tool()` decorator registers the function so the server can share all of this when a client asks what tools it has.

**Both /docs and this output describe the same model. Who is each one written for?**

`/docs` is written for human developers. They read it, try requests in the browser and then write code that calls the API. The `client.py` output is written for an AI model. The LLM reads the tool name, description and inputs to decide on its own whether to call the tool and what values to pass.

**If the docstring were "Does a calculation." and a user asked "What kind of iris is this?", would you know to call this tool? What does that tell you about who the docstring is really for?**

No. "Does a calculation" says nothing about flowers or species, so an LLM would probably skip the tool or have to guess from the parameter names. This shows the docstring is really written for the LLM, not for programmers. In MCP the docstring works like a prompt: it's the main thing the model uses to decide when a tool is useful. A vague description makes a working tool effectively invisible.

## Part 6

**Try 6.0, 2.7, 5.1, 1.6. How sure is the model?**

Not very sure. It returned setosa 0.0, versicolor 0.68 and virginica 0.32. It leans toward versicolor, but there's about a one in three chance it's virginica, so this flower sits near the boundary between the two species. `classify_iris` would only have said "versicolor" and hidden that doubt. That's why I wrote the `iris_probabilities` docstring to tell the LLM to use it when the user asks how confident the model is, or when a flower might be borderline.

## Part 7

**Does your team's prototype need an MCP server? Why or why not?**

No, not for the prototype. Lark is an AI travel agent that users talk to directly through our own app. They tell it where they want to go, their dates and their budget, and it helps plan the trip. Our own code controls when the LLM is called and which travel data it gets, so we can wire those functions together directly. Building an MCP server would add another layer to run and maintain, and right now no outside AI app needs to call Lark.

Two things could make the answer yes. First, if we wanted Lark's features to work inside AI tools people already use, we would build an MCP server. For example, someone could ask Claude "plan me a 4-day trip to Lisbon under $1,500" and Claude would call tools like `search_flights`, `find_hotels` or `build_itinerary` on our server. Second, if Lark grew into an agent that picks between several tools on its own, like checking flights, comparing hotels, looking up weather and booking, MCP would give each tool a clear name and description so the model can choose the right one. A travel agent is actually a good fit for MCP once it gets there, because the model has to decide which tool fits the user's request. That's exactly what we saw in Part 6 with `classify_iris` and `iris_probabilities`. We might also use MCP the other way, as a client, by connecting Lark to existing MCP servers for flights or maps instead of writing every API integration ourselves.
