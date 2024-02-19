import React from "react";
import { Col, Row } from "react-bootstrap";
import {
  SiVisualstudiocode,
  SiSelenium,
  SiCookiecutter,
  SiRabbitmq,
  SiCelery,
  SiPostman,
} from "react-icons/si";

function Toolstack() {
  return (
    <Row style={{ justifyContent: "center", paddingBottom: "50px" }}>      
      <Col xs={4} md={2} className="tech-icons">
        <SiVisualstudiocode />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <SiPostman />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <SiSelenium />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <SiCookiecutter />
      </Col> <Col xs={4} md={2} className="tech-icons">
        <SiCelery />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <SiRabbitmq />
      </Col>

    </Row>
  );
}

export default Toolstack;
