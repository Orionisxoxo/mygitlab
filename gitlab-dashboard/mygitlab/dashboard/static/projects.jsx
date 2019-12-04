var ProjectsBox = React.createClass( {
  loadProjectsFromServer: function()  {
    var xhr = new XMLHttpRequest();
    xhr.open('get', this.props.url, true);
    xhr.withCredentials = true;
    xhr.onload = function()  {
      var data = JSON.parse(xhr.responseText);
      this.setState( { data: data } );
    } .bind(this);
    xhr.send();
  } ,

  getInitialState: function()  {
    return  {data: []} ;
  } ,

  componentDidMount: function()  {
    this.loadProjectsFromServer();
  } ,

  render: function()  {
    return (
      <div>
        <h2>Projects</h2>
        <Projects data= {this.state.data}  />
      </div>
    );
  }
} );

var Projects = React.createClass( {
  render: function()  {
    var projectNodes = this.props.data.map(function (project)  {
      return (
        <Project
          title= {project.title}
          type= {project.type}
        />
      );
    } );

    return (
      <div>
        {projectNodes}
      </div>
    );
  }
} );


var Project = React.createClass( {
  render: function()  {
    return (
      <div>{this.props.title} ({this.props.type})</div>
    );
  }
} );


window.ProjectsBox = ProjectsBox;