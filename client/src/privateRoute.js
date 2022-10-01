import React from 'react';
import PropTypes from 'prop-types';
import { Route, Navigate } from 'react-router-dom';
import { verifySession } from "./api/services"
import { useNavigate } from 'react-router-dom';

const PublicRoute = ({ children }) => {
  const navigate = useNavigate();
  const authToken = localStorage.getItem("token");
  
  if (authToken == undefined || authToken == null || authToken == "") {
    return <Navigate to="/login" />
  }
  else {
    (async () => {
      var res = await verifySession(authToken)
      console.log(res.status)
      if (res.status == 401) {
        localStorage.removeItem("token")
        navigate("/login")
      }
    })();
  }
  return children
};

export default PublicRoute;