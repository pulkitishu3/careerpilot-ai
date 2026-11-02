
import { useEffect, useState } from "react";
import API from "./services/api";
import "./App.css";

interface DashboardData {
  project: string;
  total_resumes: number;
  jobs_matched: number;
  skills_identified: number;
  interviews_completed: number;
}

function App() {
  const [data, setData] = useState<DashboardData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        const response = await API.get("/api/v1/dashboard");
        setData(response.data);
      } catch (err) {
        console.error(err);
        setError("Unable to connect to CareerPilot backend.");
      } finally {
        setLoading(false);
      }
    };

    fetchDashboard();
  }, []);

  if (loading) {
    return <div className="loading">Loading CareerPilot AI...</div>;
  }

  if (error || !data) {
    return <div className="error">{error || "No dashboard data found."}</div>;
  }

  const stats = [
    { label: "Resumes Analyzed", value: data.total_resumes },
    { label: "Jobs Matched", value: data.jobs_matched },
    { label: "Skills Identified", value: data.skills_identified },
    { label: "Interviews Completed", value: data.interviews_completed },
  ];

  return (
    <div className="app">
      <aside className="sidebar">
        <h2>CareerPilot AI</h2>

        <nav>
          <a className="active" href="/">Dashboard</a>
          <a href="#">Resume Analyzer</a>
          <a href="#">Job Matching</a>
          <a href="#">Skill Gap Analysis</a>
          <a href="#">Learning Roadmap</a>
          <a href="#">Mock Interviews</a>
        </nav>

        <div className="sidebar-footer">
          AI-powered career companion
        </div>
      </aside>

      <main className="main-content">
        <header className="topbar">
          <div>
            <h1>Dashboard</h1>
            <p>Welcome to your career intelligence workspace.</p>
          </div>
          <span className="status">● Backend Connected</span>
        </header>

        <section className="welcome">
          <h2>Build your future with CareerPilot AI.</h2>
          <p>
            Analyze your skills, discover opportunities, and prepare
            for your dream career.
          </p>
        </section>

        <section className="stats-grid">
          {stats.map((stat) => (
            <div className="stat-card" key={stat.label}>
              <p>{stat.label}</p>
              <h2>{stat.value}</h2>
            </div>
          ))}
        </section>

        <section className="activity">
          <h2>Getting Started</h2>
          <p>
            Your career journey begins here. Resume analysis,
            job matching and personalized learning are coming next.
          </p>
        </section>

        <footer>
          CareerPilot AI © 2026 | Your Career, Intelligently Guided
        </footer>
      </main>
    </div>
  );
}

export default App;
