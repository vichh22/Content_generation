# AI Content Studio

An AI-powered content generation web application built using **Python, Flask, and Groq AI**. It transforms a single topic into multiple types of content through an automated workflow.

## Overview

AI Content Studio simplifies content creation by generating content ideas, writing a detailed article, summarizing the article, and creating a professional LinkedIn post. The application provides a web-based dashboard where users can enter a topic and view all generated content in one place.

## Features

- **Content Idea Generation:** Generates five creative content ideas based on the user's topic.
- **Article Generation:** Creates a structured article with an introduction, headings, examples, and conclusion.
- **Automatic Summarization:** Produces a concise summary of the generated article.
- **LinkedIn Post Creation:** Converts the summary into an engaging LinkedIn post with relevant hashtags.
- **Interactive Dashboard:** Displays the four stages of the content workflow by default.
- **Copy to Clipboard:** Allows users to copy generated content easily.
- **Responsive Design:** Provides a dark-themed interface suitable for desktop and mobile screens.
- **AI Integration:** Uses the Groq API to generate content.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application and API routes |
| Groq API | AI-powered content generation |
| HTML5 | Web page structure |
| CSS3 | Styling and responsive layout |
| JavaScript | User interactions and API requests |
| python-dotenv | Loading environment variables |

## Project Structure

```text
content_generation/
├── .venv/              # Local virtual environment (not uploaded)
├── .env                # API key configuration (not uploaded)
├── .gitignore          # Files excluded from Git
├── app.py              # Main Flask application and web UI
├── prompt.py           # Prompt definitions, if used
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Workflow

1. **Enter a Topic:** The user enters a topic such as Machine Learning or Cybersecurity.
2. **Generate Ideas:** The AI creates five relevant content ideas.
3. **Create an Article:** The AI writes a detailed article using the generated ideas.
4. **Summarize the Article:** The article is condensed into its main points.
5. **Generate a LinkedIn Post:** The summary is transformed into a professional social media post.
6. **Copy the Results:** The user can copy each output from the dashboard.

## Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version
- Git
- A Groq API key

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/content_generation.git
cd content_generation
```

Replace `YOUR_USERNAME` with your GitHub username and use your actual repository name if it differs.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you have not created `requirements.txt` yet, add:

```text
Flask
groq
python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
groq_api_key=YOUR_GROQ_API_KEY
```

Replace `YOUR_GROQ_API_KEY` with your actual API key.

**Security:** Never upload `.env` to GitHub or expose your API key in frontend JavaScript.

### 5. Run the Application

```bash
python app.py
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

Enter a topic and click **Generate Content** to create all four outputs.

## Deployment

The Flask application can be deployed to a compatible Python hosting platform, such as Vercel.

General deployment steps:

1. Push the project to GitHub.
2. Import the repository into your chosen hosting platform.
3. Configure the environment variable `groq_api_key` in the hosting platform's project settings.
4. Ensure the required dependencies are listed in `requirements.txt`.
5. Deploy and test the application.

Do not commit your `.env` file. The hosting platform should supply the API key through its environment-variable settings.

## Security Considerations

- Keep API keys in environment variables.
- Exclude `.env` and `.venv/` from Git using `.gitignore`.
- Never place secret API keys in HTML, CSS, or JavaScript.
- Avoid enabling Flask debug mode in production.
- Handle API errors without exposing sensitive configuration or secrets.

## Future Enhancements

- User authentication and saved content history.
- Export generated content to PDF or Markdown.
- More content formats, such as blogs, emails, and social media captions.
- Customizable writing tone and article length.
- Streaming responses and progress indicators.
- Improved error handling, rate limiting, and production monitoring.

## License

This project is available for educational and personal development purposes. Add a specific open-source license if you intend to distribute or reuse the project under formal licensing terms.

---

**Developed with Python, Flask, and Groq AI.**
