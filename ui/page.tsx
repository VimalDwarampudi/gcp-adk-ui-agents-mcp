"use client";

import { CopilotChat } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";
import "./chat-theme.css";

export default function HomePage() {
  return (
    // Bright, energized background gradient
    <main className="flex h-screen w-screen bg-gradient-to-tr from-blue-50 via-white to-indigo-50 font-sans">

      {/* 1. Professional Light Sidebar */}
      <nav className="w-28 md:w-32 bg-white/70 backdrop-blur-md border-r border-slate-200 flex flex-col items-center py-8 shadow-sm">
        <div className="text-2xl font-black text-slate-800 mb-12 tracking-tighter">
          <span className="text-indigo-600">HR Agent</span>
        </div>

        <div className="flex-1 w-full px-2 space-y-6">
          <MenuBtn icon="🏠" label="Agent" color="text-indigo-600" active />
          <MenuBtn icon="📊" label="Policies" color="text-slate-600" />
          <MenuBtn icon="📁" label="Employees" color="text-slate-600" />
          <MenuBtn icon="🧬" label="Links" color="text-slate-600" />
        </div>


      </nav>

      {/* 2. Light Theme Chat Area */}
      <section className="flex-1 flex flex-col items-center justify-center p-6">
        <div className="w-full max-w-5xl h-[88vh] bg-white rounded-[2.5rem] shadow-[0_20px_50px_rgba(0,0,0,0.05)] overflow-hidden border border-slate-200">
          <CopilotChat
            className="copilot-light-theme h-full"
            labels={{
              title: "Assistant Console",
              initial: "Hello! I am your HR agent, here to help you with any HR related queries?",
            }}
          />
        </div>
      </section>
    </main>
  );
}

function MenuBtn({ icon, label, color, active = false }: { icon: string, label: string, color: string, active?: boolean }) {
  return (
    <button className={`w-full flex flex-col items-center py-3 rounded-2xl transition-all ${active ? 'bg-indigo-50' : 'hover:bg-slate-50'}`}>
      <span className={`text-2xl mb-1 ${active ? 'text-indigo-600' : color}`}>{icon}</span>
      <span className={`text-[10px] font-bold uppercase tracking-wider ${active ? 'text-indigo-600' : 'text-slate-400'}`}>{label}</span>
    </button>
  );
}