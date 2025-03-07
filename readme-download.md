# Blog Idea Generator - README

## Overview

The Blog Idea Generator is a web application that helps content creators quickly generate blog post ideas and outlines tailored to their specific niche. It uses language models through either Open WebUI or local Ollama to generate creative, structured content ideas.

## Features

- Generate customized blog post ideas based on your content niche
- Choose the number of ideas to generate (1, 3, 5, or 10)
- Select content tone (professional, casual, humorous, etc.)
- Include or exclude detailed outlines for each post idea
- Select from available language models
- Copy results to clipboard with one click
- Responsive design for desktop and mobile

## Prerequisites

- Python 3.8+
- FastAPI and its dependencies
- Access to Open WebUI (https://chat.ivislabs.in) and/or local Ollama installation

## Installation Steps

1. **Create Project Structure**
   - Create the project directory
   - Create subdirectories for templates and static files

2. **Install Dependencies**
   - Install FastAPI, Uvicorn, Jinja2, HTTPX, and other required packages

3. **Configure API Settings**
   - Update the API key for Open WebUI if needed
   - Configure local Ollama settings if using it as a fallback

4. **Start the Application**
   - Run the FastAPI application with Uvicorn
   - Access the application at http://localhost:8000

## Using the Application

### Step 1: Set Your Content Parameters
1. Enter your content niche (e.g., "sustainable gardening", "digital marketing")
2. Select the number of blog post ideas you want
3. Choose your preferred content tone
4. Decide whether to include detailed outlines
5. Select the language model to use

### Step 2: Generate Ideas
1. Click the "Generate Ideas" button
2. Wait for the ideas to be generated
3. View the results in the designated area

### Step 3: Use Your Ideas
1. Review the generated blog post ideas and outlines
2. Use the "Copy to Clipboard" button to save the ideas
3. Incorporate them into your content planning

## How It Works

1. **User Inputs Parameters**
   - The user fills out the form with their content needs

2. **Application Sends Request to LLM**
   - The application creates a prompt based on user inputs
   - It attempts to connect to Open WebUI first
   - Falls back to local Ollama if Open WebUI is unavailable

3. **LLM Generates Content**
   - The language model processes the prompt
   - Returns creative blog post ideas in the requested format

4. **Results Display**
   - The application formats the response with proper styling
   - Displays the content to the user

## Troubleshooting

### API Connection Issues
- Verify your API key is correct
- Check if Open WebUI is accessible from your network
- Review application logs for specific error messages

### No Models Available
- Verify that the API is working properly
- Check that you have models installed if using local Ollama
- The application will use a default list if it can't fetch models

### Generation Errors
- Try a different language model
- Simplify your request (fewer ideas, no outlines)
- Check if the prompt is properly formatted

## Customization Options

- Modify prompt templates for different types of content generation
- Adjust the UI styling to match your preferences
- Configure different LLM providers by updating API endpoints
- Add additional generation options based on your needs
