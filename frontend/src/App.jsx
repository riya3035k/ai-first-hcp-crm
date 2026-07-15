import InteractionForm from "./components/InteractionForm";
import InteractionHistory from "./components/InteractionHistory";
import ChatInterface from "./components/ChatInterface";

function App() {
  return (
    <div>
      <h1>AI-First HCP CRM</h1>
      <p>Healthcare Professional Interaction Management</p>

      <InteractionForm />

      <ChatInterface />

      <InteractionHistory />
    </div>
  );
}

export default App;