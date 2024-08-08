import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import '../App.css'

/**
 * @summary - top navigation bar 
 */
function NavBarGlobal() {
  return (
      <Navbar fixed="top" expand="lg" className="navbar-custom">
        <Container className='ml-16 mt-2 mr-0'>
          {/* Home brand logo */}
          <div>
            <Navbar.Brand href="#home">
              <img
                src="att_logo.jpg"
                width="105"
                height="35"
                className="d-inline-block align-top"
                alt="React Bootstrap logo"
              />
            </Navbar.Brand>
          </div>
          {/* Navigation links */}
          <div className="mx-auto">
            <Nav >
              <Nav.Link href="#home" style={{ color: 'white' , fontSize:'20px', marginRight:'3rem', marginLeft:'13rem'}}>Home</Nav.Link>
              <Nav.Link href="#link" style={{ color: 'white' , fontSize:'20px', marginRight:'3rem'}}>Profile</Nav.Link>
              <Nav.Link href="#home" style={{ color: 'white' , fontSize:'20px', marginRight:'3rem'}}>Calls</Nav.Link>
              <Nav.Link href="#link" style={{ color: 'white' , fontSize:'20px', marginRight:'3rem'}}>Help</Nav.Link>
            </Nav>
          </div>          
        </Container>
      </Navbar>
  );
}
export default NavBarGlobal;