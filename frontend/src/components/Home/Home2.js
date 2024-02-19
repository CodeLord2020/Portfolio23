import React from "react";
import { Container, Row, Col } from "react-bootstrap";
// import myImg from "../../Assets/avatar.svg";
import myImg from "../../Assets/avatar.jpg";
import Tilt from "react-parallax-tilt";
import {
  AiFillGithub,
  AiOutlineFacebook,
  AiOutlineMail,
} from "react-icons/ai";
import { FaLinkedinIn } from "react-icons/fa";

function Home2() {
  return (
    <Container fluid className="home-about-section" id="about">
      <Container>
        <Row>
          <Col md={8} className="home-about-description">
            <h1 style={{ fontSize: "2.6em" }}>
              LET ME <span className="purple"> INTRODUCE </span> MYSELF
            </h1>
            <p className="home-about-body">
              I'm a Python developer passionate about crafting dynamic web experiences, extracting insights from data, and building innovative data-driven solutions.
              <br /><br />
     <h1 style={{ fontSize: "1.3em" }}>         
<span className="purple">Python</span> is my tool of choice to: </h1>

<b className="purple"> Weave web magic: </b> <br /><i>
Craft responsive web applications using frameworks like Django, Flask and FastAPI. <br />
Design interactive user interfaces that engage and delight. <br />
Build scalable backends that handle complex data flows securely.</i> <br />  <br />

           
              
                <b className="purple"> Uncover hidden truths in data: </b><br /><i>
                Explore and manipulate diverse datasets using libraries like NumPy, Pandas, and Matplotlib.<br />
Discover patterns, trends, and anomalies through rigorous analysis.<br />
Communicate findings effectively through clear visualizations.</i><br /><br />
              
              
              <b className="purple"> Empower with machine learning: </b>
              
              <br />
              
              <i>
              Develop intelligent algorithms for prediction, classification, and recommendation systems.<br />
Build models that learn from data and adapt to evolving needs.<br />
Drive decision-making and automation across industries.</i><br /><br />
        
              Whenever possible, I also apply my passion for developing products
              with
              <i>
                <b className="purple">
                  {" "}
                  Modern Python & Javascript Libraries and Frameworks
                </b>
              </i>
              &nbsp; like
              <i>
                <b className="purple">Django and React.js</b>
              </i>
            </p>
          </Col>
          <Col md={4} className="myAvtar">
            <Tilt>
              <img src={myImg} className="img-fluid" alt="avatar" />
            </Tilt>
          </Col>
        </Row>
        <Row>
          <Col md={12} className="home-about-social">
            <h1>FIND ME ON</h1>
            <p>
              Feel free to <span className="purple">connect </span>with me
            </p>
            <ul className="home-about-social-links">
              <li className="social-icons">
                <a
                  href="https://github.com/CodeLord2020"
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <AiFillGithub />
                </a>
              </li>
              <li className="social-icons">
                <a
                  href="https://www.facebook.com/adebayo.rasheed.752"
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <AiOutlineFacebook />
                </a>
              </li>
              <li className="social-icons">
                <a
                  href="https://www.linkedin.com/in/rasheedbabatunde-50133921a"
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <FaLinkedinIn />
                </a>
              </li>
              <li className="social-icons">
                <a
                  href="mailto:rasheedbabatunde76@gmail.com"
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour home-social-icons"
                >
                  <AiOutlineMail />
                </a>
              </li>
            </ul>
          </Col>
        </Row>
      </Container>
    </Container>
  );
}
export default Home2;
