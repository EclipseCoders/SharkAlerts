import { Navigate, useRoutes, useSearchParams, useNavigate } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import Home from './components/Home';
import PrivateRoute from './privateRoute';
import PublicRoute from './publicRoute';

export default function Router() {

  const routes = [
    {
      path: '/',
      children: [
        { path: '/', element: <PrivateRoute><Home /></PrivateRoute> },
        { path: '/login', element: <PublicRoute><Login /></PublicRoute>},
        { path: '/register', element: <PublicRoute><Register /></PublicRoute> },
      ],
    },
    { path: '*', element: <Navigate to="/login" replace /> },
  ]

  return useRoutes(routes);
}