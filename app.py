
# ============================================================
# AI CONTENT STUDIO
# Flask + Groq AI + HTML + CSS + JavaScript
# ============================================================

# First create a virtual environment and activate it.
# Create a .env file to store the API key.
# Create a .gitignore file to prevent the .env file from
# being uploaded to GitHub.
# Install the required packages: Flask, python-dotenv, groq.
# Create this Python file to build the application.

# -------------------- IMPORT REQUIRED LIBRARIES --------------------

from dotenv import load_dotenv
import os
from groq import Groq
from flask import Flask, request, jsonify, render_template_string

# -------------------- LOAD ENVIRONMENT VARIABLES --------------------

load_dotenv()

api_key = os.getenv("groq_api_key")

# -------------------- GROQ CONFIGURATION --------------------

MODEL = "openai/gpt-oss-20b"

def ask_ai(prompt):
    """Send a prompt to Groq and return the AI-generated response."""

    if not api_key:
        raise ValueError(
            "Groq API key not found. Add groq_api_key to your .env file."
        )

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional AI content creation assistant. "
                    "Generate clear, accurate, useful, well-structured content. "
                    "Follow the user's instructions carefully."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()


# -------------------- GENERATE CONTENT IDEAS --------------------

def generate_ideas(topic):
    prompt = f"""
Generate 5 creative and useful content ideas about: {topic}

For each idea:
- Give a short, engaging title.
- Add one sentence explaining the idea.
- Number the ideas from 1 to 5.

Keep the output easy to read.
"""
    return ask_ai(prompt)


# -------------------- CREATE AN ARTICLE --------------------

def create_article(topic, ideas):
    prompt = f"""
Write a well-structured article about: {topic}

Use these content ideas as inspiration:
{ideas}

Requirements:
- Include an engaging title.
- Start with an introduction.
- Use clear section headings.
- Explain the topic in detail.
- Include practical examples where useful.
- End with a conclusion.
- Use professional, readable language.
"""
    return ask_ai(prompt)


# -------------------- CREATE A SUMMARY --------------------

def create_summary(article):
    prompt = f"""
Create a concise summary of the following article.

Preserve the main points and important information.
Use short paragraphs or bullet points.

ARTICLE:
{article}
"""
    return ask_ai(prompt)


# -------------------- CREATE A LINKEDIN POST --------------------

def create_linkedin_post(topic, summary):
    prompt = f"""
Create a professional LinkedIn post about: {topic}

Use this summary as the source material:
{summary}

Requirements:
- Start with an attention-grabbing opening.
- Use short, readable paragraphs.
- Provide a useful takeaway.
- End with a question or invitation to engage.
- Add 3 to 5 relevant hashtags.
- Keep the tone professional and engaging.
"""
    return ask_ai(prompt)


# -------------------- FLASK APPLICATION --------------------

app = Flask(__name__)


# -------------------- EMBEDDED HTML, CSS AND JAVASCRIPT --------------------

HTML_PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>AI Content Studio</title>

    <style>
        :root {
            --bg: #0b1020;
            --panel: #141c30;
            --panel-light: #19243b;
            --border: #2b3652;
            --text: #f8fafc;
            --muted: #9aa8c7;
            --accent: #8b83ff;
            --accent-light: #b4adff;
            --green: #42d6a4;
            --red: #ff8585;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            background:
                radial-gradient(
                    circle at top right,
                    rgba(104, 88, 255, 0.12),
                    transparent 35%
                ),
                var(--bg);
            color: var(--text);
            font-family: Inter, "Segoe UI", Arial, sans-serif;
            line-height: 1.6;
        }

        button,
        input {
            font: inherit;
        }

        .app {
            width: min(1440px, 100%);
            margin: 0 auto;
            padding: 36px 30px 60px;
        }

        .topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            margin-bottom: 36px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        # .brand-icon {
        #     width: 46px;
        #     height: 46px;
        #     display: grid;
        #     place-items: center;
        #     border-radius: 14px;
        #     background: linear-gradient(135deg, #8b83ff, #5b55db);
        #     font-size: 23px;
        # }

        .brand h1 {
            font-size: 20px;
            letter-spacing: -0.4px;
        }

        .brand p {
            font-size: 13px;
            color: var(--muted);
        }

        .status-pill {
            display: flex;
            align-items: center;
            gap: 8px;
            border: 1px solid var(--border);
            border-radius: 30px;
            padding: 8px 13px;
            color: var(--muted);
            font-size: 12px;
            white-space: nowrap;
        }

        .status-dot {
            width: 8px;
            height: 8px;
            background: var(--green);
            border-radius: 50%;
        }

        .hero {
            margin-bottom: 30px;
        }

        .eyebrow {
            color: var(--accent-light);
            text-transform: uppercase;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1.6px;
            margin-bottom: 10px;
        }

        .hero h2 {
            font-size: clamp(28px, 4vw, 42px);
            line-height: 1.2;
            letter-spacing: -1.2px;
            max-width: 700px;
            margin-bottom: 14px;
        }

        .hero p {
            color: var(--muted);
            max-width: 650px;
            font-size: 15px;
        }

        .panel {
            background: rgba(20, 28, 48, 0.92);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 26px;
            margin-bottom: 28px;
        }

        .panel-heading {
            margin-bottom: 20px;
        }

        .panel-heading h3 {
            font-size: 18px;
            margin-bottom: 4px;
        }

        .panel-heading p {
            color: var(--muted);
            font-size: 13px;
        }

        .topic-label {
            display: block;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 9px;
        }

        .input-row {
            display: flex;
            gap: 12px;
        }

        .topic-input {
            flex: 1;
            min-width: 0;
            background: #0d1426;
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px 16px;
            color: var(--text);
            outline: none;
            transition: border-color 0.2s;
        }

        .topic-input:focus {
            border-color: var(--accent);
        }

        .topic-input::placeholder {
            color: #687693;
        }

        .generate-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 9px;
            background: linear-gradient(135deg, #8b83ff, #6961ed);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 13px 22px;
            font-weight: 700;
            cursor: pointer;
            transition: transform 0.2s, opacity 0.2s;
            white-space: nowrap;
        }

        .generate-btn:hover {
            transform: translateY(-1px);
        }

        .generate-btn:disabled {
            opacity: 0.65;
            cursor: wait;
            transform: none;
        }

        .helper {
            margin-top: 10px;
            color: var(--muted);
            font-size: 12px;
        }

        /* WORKFLOW: VISIBLE BY DEFAULT */

        .workflow-section {
            display: block;
            margin-top: 34px;
            margin-bottom: 34px;
        }

        .workspace-heading {
            margin-bottom: 20px;
        }

        .workspace-heading h2 {
            font-size: 27px;
            letter-spacing: -0.6px;
            margin-bottom: 5px;
        }

        .workspace-heading p {
            color: var(--muted);
            font-size: 14px;
        }

        .workflow-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 15px;
        }

        .workflow-card {
            min-height: 105px;
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 17px;
            padding: 18px 20px;
            transition:
                border-color 0.25s,
                background 0.25s,
                transform 0.25s;
        }

        .workflow-card:hover {
            border-color: #625ce0;
            transform: translateY(-2px);
        }

        .workflow-card.active {
            border-color: var(--accent);
            background: #1b2440;
        }

        .workflow-card.completed {
            border-color: rgba(66, 214, 164, 0.55);
        }

        .step-number {
            color: var(--accent-light);
            font-size: 12px;
            display: block;
            margin-bottom: 13px;
        }

        .workflow-card h3 {
            font-size: 15px;
            font-weight: 700;
        }

        .step-status {
            display: block;
            margin-top: 5px;
            color: var(--muted);
            font-size: 11px;
        }

        .workflow-card.completed .step-status {
            color: var(--green);
        }

        .message {
            display: none;
            padding: 13px 16px;
            margin: 20px 0;
            border-radius: 12px;
            font-size: 13px;
            overflow-wrap: anywhere;
        }

        .message.show {
            display: block;
        }

        .message.error {
            background: rgba(255, 100, 100, 0.08);
            border: 1px solid rgba(255, 100, 100, 0.3);
            color: var(--red);
        }

        .message.info {
            background: rgba(139, 131, 255, 0.08);
            border: 1px solid rgba(139, 131, 255, 0.3);
            color: var(--accent-light);
        }

        .results-section {
            margin-top: 36px;
        }

        .results-header {
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            gap: 15px;
            margin-bottom: 20px;
        }

        .results-header h2 {
            font-size: 25px;
            margin-bottom: 4px;
        }

        .results-header p {
            color: var(--muted);
            font-size: 13px;
        }

        .results-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 18px;
        }

        .result-card {
            min-width: 0;
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 17px;
            overflow: hidden;
        }

        .result-card-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            padding: 18px 20px;
            border-bottom: 1px solid var(--border);
        }

        .result-card-header h3 {
            font-size: 15px;
        }

        .copy-btn {
            color: var(--accent-light);
            background: transparent;
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 6px 10px;
            font-size: 11px;
            cursor: pointer;
        }

        .copy-btn:hover {
            background: var(--panel-light);
        }

        .result-content {
            padding: 20px;
            color: #d5dcef;
            font-size: 13px;
            white-space: pre-wrap;
            overflow-wrap: anywhere;
            max-height: 480px;
            overflow-y: auto;
        }

        .empty-state {
            padding: 34px 20px;
            color: var(--muted);
            text-align: center;
            font-size: 13px;
        }

        .empty-state span {
            display: block;
            font-size: 28px;
            margin-bottom: 8px;
        }

        .footer {
            margin-top: 42px;
            padding-top: 20px;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 12px;
            color: var(--muted);
            font-size: 12px;
        }

        @media (max-width: 900px) {
            .workflow-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }

        @media (max-width: 650px) {
            .app {
                padding: 24px 16px 40px;
            }

            .topbar {
                align-items: flex-start;
            }

            .status-pill {
                font-size: 0;
            }

            .input-row {
                flex-direction: column;
            }

            .generate-btn {
                width: 100%;
            }

            .panel {
                padding: 20px;
            }

            .results-grid {
                grid-template-columns: 1fr;
            }

            .workspace-heading h2 {
                font-size: 23px;
            }

            .workflow-card {
                padding: 16px;
            }

            .footer {
                flex-direction: column;
            }
        }

        @media (max-width: 380px) {
            .workflow-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>
<div class="app">

    <!-- HEADER -->

    <header class="topbar">
        <div class="brand">
            <div class="brand-icon"></div>
            <div>
                <h1>AI Content Studio</h1>
                <p>Your AI-powered writing workspace</p>
            </div>
        </div>

        <div class="status-pill">
            <span class="status-dot"></span>
            Groq AI Assistant
        </div>
    </header>


    <!-- INTRODUCTION -->

    <section class="hero">
        <div class="eyebrow">Create smarter content</div>

        <h2>Turn your ideas into impactful content.</h2>

        <p>
            Generate content ideas, write detailed articles, create concise
            summaries, and prepare professional LinkedIn posts in one place.
        </p>
    </section>


    <!-- TOPIC INPUT -->

    <section class="panel">
        <div class="panel-heading">
            <h3>Start creating</h3>
            <p>Enter a topic and let AI build your content pipeline.</p>
        </div>

        <form id="contentForm">
            <label class="topic-label" for="topicInput">
                What would you like to write about?
            </label>

            <div class="input-row">
                <input
                    id="topicInput"
                    class="topic-input"
                    type="text"
                    placeholder="e.g. Machine Learning, Cybersecurity..."
                    autocomplete="off"
                    required
                >

                <button
                    id="generateBtn"
                    class="generate-btn"
                    type="submit"
                >
                    <span id="buttonIcon"></span>
                    <span id="buttonText">Generate Content</span>
                </button>
            </div>

            <p class="helper">
                One topic. Four outputs. Powered by Groq AI.
            </p>
        </form>
    </section>


    <!-- WORKFLOW PIPELINE
         This section is outside the results container.
         Therefore, it is visible immediately when the page loads. -->

    <section class="workflow-section" id="workflow">
        <div class="workspace-heading">
            <h2>Your content workspace</h2>
            <p id="generatedFor">Ready to generate content</p>
        </div>

        <div class="workflow-grid">

            <div class="workflow-card" id="step-ideas">
                <span class="step-number">STEP 01</span>
                <h3>💡 Ideas</h3>
                <span class="step-status" id="status-ideas">
                    Waiting to start
                </span>
            </div>

            <div class="workflow-card" id="step-article">
                <span class="step-number">STEP 02</span>
                <h3>📝 Article</h3>
                <span class="step-status" id="status-article">
                    Waiting to start
                </span>
            </div>

            <div class="workflow-card" id="step-summary">
                <span class="step-number">STEP 03</span>
                <h3>📋 Summary</h3>
                <span class="step-status" id="status-summary">
                    Waiting to start
                </span>
            </div>

            <div class="workflow-card" id="step-linkedin">
                <span class="step-number">STEP 04</span>
                <h3>💼 LinkedIn</h3>
                <span class="step-status" id="status-linkedin">
                    Waiting to start
                </span>
            </div>

        </div>
    </section>


    <!-- STATUS / ERROR MESSAGE -->

    <div id="messageBox" class="message" role="status" aria-live="polite"></div>


    <!-- GENERATED CONTENT -->

    <section class="results-section" id="resultsSection">
        <div class="results-header">
            <div>
                <h2>Generated content</h2>
                <p>Your AI-generated results will appear here.</p>
            </div>
        </div>

        <div class="results-grid">

            <article class="result-card">
                <div class="result-card-header">
                    <h3>💡 Content Ideas</h3>
                    <button class="copy-btn" data-copy="ideas">Copy</button>
                </div>
                <div class="result-content" id="ideas">
                    <div class="empty-state">
                        <span>✦</span>
                        Your content ideas will appear here.
                    </div>
                </div>
            </article>

            <article class="result-card">
                <div class="result-card-header">
                    <h3>📝 Article</h3>
                    <button class="copy-btn" data-copy="article">Copy</button>
                </div>
                <div class="result-content" id="article">
                    <div class="empty-state">
                        <span>▤</span>
                        Your article will appear here.
                    </div>
                </div>
            </article>

            <article class="result-card">
                <div class="result-card-header">
                    <h3>📋 Summary</h3>
                    <button class="copy-btn" data-copy="summary">Copy</button>
                </div>
                <div class="result-content" id="summary">
                    <div class="empty-state">
                        <span>≡</span>
                        Your summary will appear here.
                    </div>
                </div>
            </article>

            <article class="result-card">
                <div class="result-card-header">
                    <h3>💼 LinkedIn Post</h3>
                    <button class="copy-btn" data-copy="linkedin">Copy</button>
                </div>
                <div class="result-content" id="linkedin">
                    <div class="empty-state">
                        <span>↗</span>
                        Your LinkedIn post will appear here.
                    </div>
                </div>
            </article>

        </div>
    </section>


    <!-- FOOTER -->

    <footer class="footer">
        <span>AI Content Studio</span>
        <span>Built with Python, Flask and Groq AI</span>
    </footer>

</div>


<script>
    const form = document.getElementById("contentForm");
    const topicInput = document.getElementById("topicInput");
    const generateBtn = document.getElementById("generateBtn");
    const buttonText = document.getElementById("buttonText");
    const buttonIcon = document.getElementById("buttonIcon");
    const generatedFor = document.getElementById("generatedFor");
    const messageBox = document.getElementById("messageBox");

    const steps = ["ideas", "article", "summary", "linkedin"];

    const labels = {
        ideas: "Ideas",
        article: "Article",
        summary: "Summary",
        linkedin: "LinkedIn"
    };

    function showMessage(message, type = "info") {
        messageBox.textContent = message;
        messageBox.className = "message show " + type;
    }

    function hideMessage() {
        messageBox.textContent = "";
        messageBox.className = "message";
    }

    function setStep(step, status) {
        const card = document.getElementById("step-" + step);
        const statusLabel = document.getElementById("status-" + step);

        card.classList.remove("active", "completed");

        if (status === "active") {
            card.classList.add("active");
            statusLabel.textContent = "In progress...";
        } else if (status === "completed") {
            card.classList.add("completed");
            statusLabel.textContent = "Completed";
        } else if (status === "error") {
            statusLabel.textContent = "Could not complete";
        } else {
            statusLabel.textContent = "Waiting to start";
        }
    }

    function resetWorkflow() {
        steps.forEach(step => setStep(step, "waiting"));
    }

    function setResult(id, content) {
        // textContent prevents generated text from being interpreted as HTML.
        document.getElementById(id).textContent = content;
    }

    function setLoading(isLoading) {
        generateBtn.disabled = isLoading;
        buttonText.textContent = isLoading
            ? "Generating..."
            : "Generate Content";

        buttonIcon.textContent = isLoading ? "◌" : "✦";
    }

    form.addEventListener("submit", async function(event) {
        event.preventDefault();

        const topic = topicInput.value.trim();

        if (!topic) {
            showMessage("Please enter a topic first.", "error");
            topicInput.focus();
            return;
        }

        hideMessage();
        setLoading(true);
        resetWorkflow();

        // The workflow remains visible during generation.
        generatedFor.textContent = "Generating content for: " + topic;

        steps.forEach(step => {
            setResult(step, "Waiting for generated content...");
        });

        try {
            const response = await fetch("/generate", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ topic: topic })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.error || "Unable to generate content."
                );
            }

            // Update workflow and results.
            steps.forEach(step => {
                setResult(step, data[step] || "No content returned.");
                setStep(step, "completed");
            });

            generatedFor.textContent = "Generated for: " + topic;

            showMessage(
                "All four content steps have been completed successfully.",
                "info"
            );

        } catch (error) {
            showMessage(
                error.message || "Something went wrong. Please try again.",
                "error"
            );

            generatedFor.textContent =
                "Generation failed. You can try again.";

        } finally {
            setLoading(false);
        }
    });


    // Copy an individual result.
    document.querySelectorAll("[data-copy]").forEach(button => {
        button.addEventListener("click", async function() {
            const targetId = button.dataset.copy;
            const target = document.getElementById(targetId);
            const text = target.innerText.trim();

            if (!text) {
                showMessage("There is no content to copy yet.", "error");
                return;
            }

            try {
                await navigator.clipboard.writeText(text);

                const originalText = button.textContent;
                button.textContent = "Copied!";

                setTimeout(() => {
                    button.textContent = originalText;
                }, 1500);

            } catch (error) {
                showMessage(
                    "Copy failed. Please select and copy the text manually.",
                    "error"
                );
            }
        });
    });
</script>

</body>
</html>
"""


# -------------------- HOME PAGE ROUTE --------------------

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)


# -------------------- GENERATE CONTENT ROUTE --------------------

@app.route("/generate", methods=["POST"])
def generate_content():
    data = request.get_json(silent=True) or {}
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({
            "error": "Please enter a topic."
        }), 400

    try:
        # STEP 01: Generate content ideas.
        ideas = generate_ideas(topic)

        # STEP 02: Create an article.
        article = create_article(topic, ideas)

        # STEP 03: Summarize the article.
        summary = create_summary(article)

        # STEP 04: Create a LinkedIn post.
        linkedin = create_linkedin_post(topic, summary)

        return jsonify({
            "topic": topic,
            "ideas": ideas,
            "article": article,
            "summary": summary,
            "linkedin": linkedin
        })

    except Exception as error:
        app.logger.exception("Content generation failed")

        return jsonify({
            "error": str(error)
        }), 500


# -------------------- RUN APPLICATION --------------------

if __name__ == "__main__":
    # Local development only.
    # For Vercel deployment, Vercel manages the application server.
    app.run(debug=True, port=5000)
