from django.shortcuts import render, redirect
from .chatbot import Chatbot


def chat(request):

    if "chatbot" not in request.session:
        request.session["chatbot"] = {
            "current_question": 0,
            "requirements": {}
        }

    bot = Chatbot()

    # Restore chatbot state
    bot.current_question = request.session["chatbot"]["current_question"]
    bot.requirements = request.session["chatbot"]["requirements"]

    if request.method == "POST":

        answer = request.POST.get("answer")

        if request.POST.getlist("answers"):
            answer = request.POST.getlist("answers")

        result = bot.process_answer(answer)

        # Save state
        request.session["chatbot"]["current_question"] = bot.current_question
        request.session["chatbot"]["requirements"] = bot.requirements
        request.session.modified = True

        # Questions remaining
        if isinstance(result, dict) and "question" in result:

            return render(
                request,
                "chatbot/chat.html",
                {
                    "question": result,
                }
            )

        # Scout results
        return render(
            request,
            "chatbot/results.html",
            {
                "results": result,
            }
        )

    question = bot.get_current_question()

    return render(
        request,
        "chatbot/chat.html",
        {
            "question": question,
        }
    )

#scout result

def results(request):

    chatbot_data = request.session.get("chatbot")

    if not chatbot_data:
        return redirect("chatbot:chat")

    requirements = chatbot_data.get("requirements", {})

    scout = Scout()

    results = scout.find_publishers(requirements)

    return render(
        request,
        "chatbot/results.html",
        {
            "results": results,
            "requirements": requirements,
        }
    )