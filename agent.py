





from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.voice import VoicePipeline
from livekit.plugins import openai

async def entrypoint(ctx: JobContext):
    await ctx.connect()

    pipeline = VoicePipeline(
        vad=openai.VAD(),
        stt=openai.STT(),
        llm=openai.LLM(
            model="gpt-4o-mini",
            system_prompt=(
                "You are a polite recruitment assistant calling nurses. "
                "Speak clearly in English. Keep responses short and professional."
            ),
        ),
        tts=openai.TTS(
            voice="alloy"
        ),
    )

    pipeline.start(ctx.room)

    await pipeline.say(
        "Hello. This is an automated call regarding a nursing opportunity in Dubai. "
        "May I ask if you are currently looking for overseas work?",
        allow_interruptions=True,
    )

if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint
        )
    )

