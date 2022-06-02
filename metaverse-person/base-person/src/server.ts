import http from 'http';

import app from './app';

// create new server for our application
http.createServer(app);
