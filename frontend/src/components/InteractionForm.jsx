import {useState} from "react";
import {createInteraction} from "../services/api";
function InteractionForm() {
    const [formData, setFormData] = useState({
        hcp_id: "",
        interaction_type: "",
        interaction_date: "",
        topics_discussed: "",
        sentiment: "",
        summary: "",
        follow_up_date: ""
    });
    const [message, setMessage] = useState("");
    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const dataToSend = {
                ...formData,
                follow_up_date: formData.follow_up_date || null
            };
            await createInteraction(dataToSend);
            setMessage("Interaction created successfully!");
            setFormData({
                hcp_id: "",
                interaction_type: "",
                interaction_date: "",
                topics_discussed: "",
                sentiment: "",
                summary: "",
                follow_up_date: ""
            });
        } catch (error) {
            console.error(error);
            setMessage(error.response?.data?.detail || "Failed to log interaction.");
        }
    };
    return (
        <div>
            <h2>Log New Interaction</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="number"
                    name="hcp_id"
                    placeholder="HCP ID"
                    value={formData.hcp_id}
                    onChange={handleChange}
                    required
                />
                <select
                    name="interaction_type"
                    value={formData.interaction_type}
                    onChange={handleChange}
                    required
                >
                    <option value="">Select Interaction Type</option>
                    <option value="meeting">Meeting</option>
                    <option value="call">Call</option>
                    <option value="email">Email</option>
                </select>
                <input
                    type="date"
                    name="interaction_date"
                    value={formData.interaction_date}
                    onChange={handleChange}
                    required
                />
                <textarea
                    name="topics_discussed"
                    placeholder="Topics Discussed"
                    value={formData.topics_discussed}
                    onChange={handleChange}
                    required
                />
                <select
                    name="sentiment"
                    value={formData.sentiment}
                    onChange={handleChange}
                    required
                >
                    <option value="">Select Sentiment</option>
                    <option value="positive">Positive</option>
                    <option value="neutral">Neutral</option>
                    <option value="negative">Negative</option>
                </select>
                <textarea
                    name="summary"
                    placeholder="Interaction Summary"
                    value={formData.summary}
                    onChange={handleChange}
                    required
                />
                <label>Follow-up Date</label>
                <input
                    type="date"
                    name="follow_up_date"
                    value={formData.follow_up_date}
                    onChange={handleChange}
                />
                <button type="submit">Log Interaction</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
}
export default InteractionForm;