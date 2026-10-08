from django.shortcuts import render, redirect

from .analyzer import IdeaAnalyzer


def idea(request):

    if "pitch_assistant" not in request.session:

        request.session["pitch_assistant"] = {
            "step": "game_idea",

            "messages": [
                {
                    "role": "assistant",
                    "content": (
                        "Hey! Let's turn your game idea into "
                        "a pitch publishers can understand and remember. "
                        "You don't need to write professionally. "
                        "Just tell me about your game naturally."
                    )
                },
                {
                    "role": "assistant",
                    "content": (
                        "First, tell me about your game. "
                        "What is it about?"
                    )
                }
            ],

            "data": {}
        }

    assistant = request.session["pitch_assistant"]


    # ------------------------------------------
    # HANDLE USER MESSAGE
    # ------------------------------------------

    if request.method == "POST":

        message = request.POST.get(
            "message",
            ""
        ).strip()

        if message:

            assistant["messages"].append({
                "role": "user",
                "content": message
            })


            if assistant["step"] == "game_idea":

                assistant["data"]["game_idea"] = message

                assistant["messages"].append({
                    "role": "assistant",
                    "content": (
                        "Got it. Now tell me what the player "
                        "actually does most of the time in your game."
                    )
                })

                assistant["step"] = "gameplay"


            elif assistant["step"] == "gameplay":

                assistant["data"]["gameplay"] = message

                assistant["messages"].append({
                    "role": "assistant",
                    "content": (
                        "That helps me understand the core gameplay. "
                        "Now, what makes your game different or "
                        "special compared with other games?"
                    )
                })

                assistant["step"] = "special"


            elif assistant["step"] == "special":

                assistant["data"]["special_feature"] = message

                assistant["messages"].append({
                    "role": "assistant",
                    "content": (
                        "Nice. I have enough information to analyze "
                        "the core idea of your game."
                    )
                })

                assistant["step"] = "ready"


            request.session["pitch_assistant"] = assistant
            request.session.modified = True

            return redirect(
                "pitch_assistant:idea"
            )


    return render(
        request,
        "pitch_assistant/idea.html",
        {
            "messages": assistant["messages"],
            "step": assistant["step"],
            "data": assistant["data"],
        }
    )


# ------------------------------------------
# ANALYZE IDEA
# ------------------------------------------

def analyze_idea(request):

    assistant = request.session.get(
        "pitch_assistant"
    )

    if not assistant:

        return redirect(
            "pitch_assistant:idea"
        )


    data = assistant.get(
        "data",
        {}
    )


    if not data.get("game_idea"):

        return redirect(
            "pitch_assistant:idea"
        )


    analyzer = IdeaAnalyzer()

    analysis = analyzer.analyze(
        data
    )


    assistant["analysis"] = analysis
    assistant["step"] = "analyzed"

    request.session["pitch_assistant"] = assistant
    request.session.modified = True


    return render(
        request,
        "pitch_assistant/analysis.html",
        {
            "analysis": analysis,
            "data": data,
        }
    )


# ------------------------------------------
# NEW PITCH
# ------------------------------------------

def new_pitch(request):

    request.session.pop(
        "pitch_assistant",
        None
    )

    return redirect(
        "pitch_assistant:idea"
    )