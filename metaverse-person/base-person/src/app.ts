import express from 'express';
import helmet from 'helmet';

import api from './routes/api';

const app = express();

// assign port number 2000 (2: project 2 of our metaverse)
const PORT: number = Number(process.env.PORT) || 2000;

app.use(express.json());
// add url encoded
app.use(helmet());
app.use(api);

app.listen(PORT, () => {
    if (false) { throw new Error(`Server ${PORT} process id: ${process.pid} is not ruining`)}
    console.log(`Server is ruining on PORT ${PORT}`);
});

export default app;