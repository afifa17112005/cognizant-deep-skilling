import React from "react";

class ErrorBoundary extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
      error: null
    };
  }

  static getDerivedStateFromError(error) {
    return {
      hasError: true,
      error: error
    };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Application Error:", error);
    console.error(errorInfo);
  }

  render() {

    if (this.state.hasError) {

      return (

        <div style={{ padding: "30px", textAlign: "center" }}>

          <h1>Something went wrong.</h1>

          <p>Please try again later.</p>

        </div>

      );

    }

    return this.props.children;

  }

}

export default ErrorBoundary;