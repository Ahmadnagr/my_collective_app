from flask import Flask, render_template_string

app = Flask(__name__)

# هنا بنحط بيانات مشاريعك وشغلك اللي عاوزه يظهر على الموقع
PROJECTS = [
    {
        "title": "Project Sovereign Engine",
        "description": "An offline fantasy world simulator and story-generation engine utilizing custom narrative logic and database management.",
        "tag": "Python & Simulation"
    },
    {
        "title": "Walk-In Logger Pro Edition",
        "description": "A comprehensive customer traffic and retail sales conversion tracking tool with automated Excel report exporting.",
        "tag": "Desktop App & Automation"
    },
    {
        "title": "Diamond Archive Application",
        "description": "A specialized inventory and certificate system integrated with SQLite for tracking serial numbers and managing storage labels.",
        "tag": "Database & Logistics"
    }
]

# تصميم الموقع بـ HTML و CSS مدمج عشان يشتغل معاك فوراً في ملف واحد
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            color: #333;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 2rem 1rem;
        }
        header h1 {
            margin: 0;
            font-size: 2.5rem;
        }
        header p {
            margin: 0.5rem 0 0 0;
            font-size: 1.1rem;
            color: #bdc3c7;
        }
        .container {
            max-width: 1000px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        .section-title {
            border-bottom: 2px solid #2c3e50;
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
            color: #2c3e50;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }
        .card {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card h3 {
            margin-top: 0;
            color: #2c3e50;
        }
        .card p {
            color: #555;
            line-height: 1.6;
        }
        .tag {
            display: inline-block;
            background-color: #e74c3c;
            color: white;
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: bold;
        }
        footer {
            text-align: center;
            padding: 2rem;
            color: #7f8c8d;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

    <header>
        <h1>Welcome to My Portfolio</h1>
        <p>A showcase of my latest projects, tools, and developer journey</p>
    </header>

    <div class="container">
        <h2 class="section-title">Featured Projects</h2>
        <div class="grid">
            {% for project in projects %}
            <div class="card">
                <span class="tag">{{ project.tag }}</span>
                <h3>{{ project.title }}</h3>
                <p>{{ project.description }}</p>
            </div>
            {% endfor %}
        </div>
    </div>

    <footer>
        <p>&copy; 2026 Developer Portfolio. Built entirely with Python & Flask.</p>
    </footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, projects=PROJECTS)

if __name__ == '__main__':
    # تشغيل السيرفر المحلي
    app.run(debug=True)