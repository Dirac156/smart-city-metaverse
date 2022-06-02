import express, { Request, Response, Router } from "express";

// the first version of our API 1.0.0
const api: Router = express.Router();

api.get("/", (req: Request, res: Response) => {
    if (process.env.NODE_ENV === "development") {
        return res.status(200).json({
            API_STATUS: true,
        })
    }
});

export default api;