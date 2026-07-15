import { useEffect, useState } from "react";
import { getInteractions } from "../services/api";

function InteractionHistory() {
  const [interactions, setInteractions] = useState([]);

  useEffect(() => {
    loadInteractions();
  }, []);

  const loadInteractions = async () => {
    try {
      const response = await getInteractions();
      setInteractions(response.data);
    } catch (error) {
      console.error("Failed to load interactions:", error);
    }
  };

  return (
    <div>
      <h2>Interaction History</h2>

      {interactions.length === 0 ? (
        <p>No interactions found.</p>
      ) : (
        <table border="1">
          <thead>
            <tr>
              <th>ID</th>
              <th>HCP ID</th>
              <th>Type</th>
              <th>Date</th>
              <th>Topics</th>
              <th>Sentiment</th>
              <th>Summary</th>
              <th>Follow-up Date</th>
            </tr>
          </thead>

          <tbody>
            {interactions.map((interaction) => (
              <tr key={interaction.id}>
                <td>{interaction.id}</td>
                <td>{interaction.hcp_id}</td>
                <td>{interaction.interaction_type}</td>
                <td>{interaction.interaction_date}</td>
                <td>{interaction.topics_discussed}</td>
                <td>{interaction.sentiment}</td>
                <td>{interaction.summary}</td>
                <td>{interaction.follow_up_date || "Not scheduled"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default InteractionHistory;