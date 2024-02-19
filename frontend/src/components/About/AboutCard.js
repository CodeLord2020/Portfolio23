import React from "react";
import Card from "react-bootstrap/Card";
import { ImPointRight } from "react-icons/im";

function AboutCard() {
  return (
    <Card className="quote-card-view">
      <Card.Body>
        <blockquote className="blockquote mb-0">
          <p style={{ textAlign: "justify" }}>

            💼 About Me:<br />
            Experienced professional with a strong background in Python and JavaScript development. 🐍🌐
            <br /><br />
            🔹 Experience:<br />
            I have accumulated a wealth of experience working with Python, particularly in the context of web application development. My expertise includes working with frameworks such as Django and utilizing their powerful features to build robust and scalable applications. I am adept at utilizing the Django ORM, handling database interactions, and implementing complex business logic.
            <br />
            In addition to my Python experience, I have a solid foundation in JavaScript development. I have worked with modern frameworks and libraries such as React, enabling me to create dynamic and interactive user interfaces.
            <br />
            🔹 Team Player:<br />
            Collaboration and teamwork are essential to me. I thrive in a team environment, where I can contribute my skills and learn from fellow colleagues. I greatly value open communication, shared goals, and mutual support, which ultimately leads to successful project outcomes.
            <br /><br />
            🔹 Passionate Developer:<br />
            I am deeply passionate about software development and always strive to stay up to date with the latest industry trends and best practices. Whether it's exploring new frameworks, attending meetups and conferences, or actively participating in online tech communities, I am committed to continuous learning and growth.
            <br /><br />
            🔹 Problem-solving Approach:<br />
            I take a systematic and analytical approach to problem-solving. With my strong technical foundation and breadth of experience, I am adept at breaking down complex tasks into manageable components, identifying efficient solutions, and delivering high-quality results.
            <br />
            I am eager to leverage my skills, experience, and passion for software development to contribute to innovative projects and collaborate with talented teams.
            <br />
            If you're interested in discussing potential opportunities or have any questions, feel free to connect with me. Let's create great things together! 👨‍💻🚀

            <br />
            <br />
            Apart from coding, some other activities that I love to do!
          </p>
          <ul>
            <li className="about-activity">
              <ImPointRight /> Reading Books
            </li>
            <li className="about-activity">
              <ImPointRight /> Tennis
            </li>
            <li className="about-activity">
              <ImPointRight /> Music
            </li>
          </ul>

          <p style={{ color: "rgb(155 126 172)" }}>
            "Strive to build things that make a difference!"{" "}
          </p>
          <footer className="blockquote-footer"></footer>
        </blockquote>
      </Card.Body>
    </Card>
  );
}

export default AboutCard;
