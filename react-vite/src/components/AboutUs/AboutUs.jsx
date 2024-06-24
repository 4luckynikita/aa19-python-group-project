import "./about.css";
import { FaGithub } from "react-icons/fa";

const About = () => {
  return (
    <div className="about">
      <h1>About Us</h1>
      <h2>Welcome To Our Team</h2>
      <h3>Click Our Links!</h3>
      <div className="links">
        <div className="git">
          <FaGithub className="icongit" />
          <a href="https://github.com/4luckynikita" target="#">
            Nikita
          </a>
        </div>
        <div className="git">
          <FaGithub className="icongit" />
          <a href="https://github.com/cecepot" target="#">
            Cece
          </a>
        </div>
        <div className="git">
          <FaGithub className="icongit" />
          <a href="https://github.com/ErikHervall11" target="#">
            Erik
          </a>
        </div>
      </div>
    </div>
  );
};

export default About;
