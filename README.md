<h1 align="center"> Hackathon Inatel 2023 </h1>

<p align="center">Refers to the 2023 <a href='https://inatel.br/'>Inatel</a>'s app challenge Hackathon supported by <a href='https://www.viasat.com/'>ViaSat</a>.</p>

<div id='technology' align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/jvoliveirag/Hackathon-Inatel-2023)
![GitHub language count](https://img.shields.io/github/languages/count/jvoliveirag/Hackathon-Inatel-2023)
![GitHub open issues](https://img.shields.io/github/issues/jvoliveirag/Hackathon-Inatel-2023)
![Vercel](https://vercelbadge.vercel.app/api/jvoliveirag/Hackathon-Inatel-2023)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<a href='#flask'>![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)</a>
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

<a href='#TS'>![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)</a>
<a href='#react'>![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)</a>
<a href='#next'>![Next JS](https://img.shields.io/badge/Next-black?style=for-the-badge&logo=next.js&logoColor=white)</a>
<a href='#tailwind'>![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)</a>

You can run the application by clicking <b><u><a href='https://ntracker.vercel.app/'>here</a></u></b>.

<img align='center' src="logo.png" width="250">

</div>

<h2 id="footer" align="left">Authors ✏️</h2>

- [João Victor Oliveira](https://github.com/jvoliveirag)
- [Maycol Teles](https://github.com/MaycolTeles)

<div>
<h1> Summary 📋</h1>

- <a href="#intro">Introduction</a>
- <a href="#technology">Technologies</a>
- <a href="#app">Application Overview</a>
- <a href='#dev'>Development</a>
  - <a href='#front'>Front-end</a>
  - <a href='#back'>Back-end</a>
- <a href='#future'>Thinking Forward</a>
- <a href="#concl">Conclusion</a>
</div>

<h2 id="intro" align="left">Introduction 📌</h2>
The <u><b>nTracker</b></u> is an application to monitor your network traffic and show the data in a clear and efficient way. It was designed to be simple and user-friendly.

<h2 id="app" align="left">Application Overview 🔍</h2>

<img align='center' src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjNhMThlZjcyODQ5YjJhN2JhYjNkMjAyNmU3Y2NiMDBkZGJlNjQ3MCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/qlDZRtXiEqYeOzMTcm/giphy.gif" width="450">

<br>Here are some features of nTracker:

- Create alerts and receive notifications;
- Filters: by name, category (download, upload, speed);
- Interactive charts;
- Realtime display of the payload;
- Multiplatform: web (which also works on mobile devices), desktop.

And here is a short video (in PT-BR) explaining a little bit about the app and its development: <a href='https://drive.google.com/file/d/1WnmZ-0mR-ZlX6-6oapkfCf3AUl22lGUI/view?usp=sharing'>nTracker presentation - Hackathon Inatel 2023</a>

<h2 id="dev" align="left">Development ⚙️</h2>

<u><b>Obs.:</b></u> To see details like requirements, setup and install and how to use, please refer to the docs of the respective end by just clicking on their name below.

- <h3 id="front" align="left"><a href='https://github.com/jvoliveirag/Hackathon-Inatel-2023/blob/main/frontend/README.md'>Front-end</a></h3>
    For the web version we applied some of the most used technologies of the moment:

  - <a id='TS'><b><u>TypeScript</u></b>: allows type verification;</a>
  - <a id='react'><b><u>React</u></b>: hooks and components;</a>
  - <a id='next'><b><u>NextJs</u></b>: routes optimization and serverside rendering;</a>
  - <a id='tailwind'><b><u>TailwindCSS</u></b>: styling classes;</a>
  - <b><u>Axios</u></b>: requests optimization;
  - <b><u>Highcharts</u></b>: Interactive charts.

  With these we could built an application which is <b>responsive</b>, <b>simple</b>, <b>clean</b> and <b>efficient</b>;

- <h3 id="back" align="left"><a href='https://github.com/jvoliveirag/Hackathon-Inatel-2023/blob/main/backend/README.md'>Back-end</a></h3>

  - <b><u>Clean Archtecture</u></b>: By creating the application using the Clean Architecture approach, we're able to decouple our domain (entities, use_cases, etc.) from the "external world" (our UI, external libraries, databases, etc.). In our application, we can have our data displayed in the Tkinter library (for a desktop application) or returned from an API using Flask.
  - <b><u>Sockets</u></b>: To read the traffic data from the server (the code provided by ViaSat).
  - <b id='flask'><u>Flask</u></b>: To create our API endpoints to return the backend data.
  - <b><u>TkInter</u></b>: To run the application and display data locally (in a destkop application).

<h2 id="future" align="left">Thinking Forward 💡</h2>
    Since we did not have too much time to work on all our ideas we focused on the main goal which was building an application that works well with the given purpose of the challenge. However we thought some features that we want to keep registered for possible future implemmentation such as: 
    
 - Reports generation;
 - Network management:
    - Closing and optimizing apps automaticaly;
    - Usage of AIs;

<h2 id="concl" align="left">Conclusion ✅</h2>
The <u><b>nTracker</b></u> is a potencial powerful network traffic monitoring application because it provides real-time alerts, customizable filters, interactive charts besides of being multiplatform, with a responsive web version and desktop compatibility.

The technologies employed allow the app to have great performance on the most variable devices, as well as open up space to develop new features . The <u><b>nTracker</b></u> ensures efficient network monitoring and management for optimal performance and security.
