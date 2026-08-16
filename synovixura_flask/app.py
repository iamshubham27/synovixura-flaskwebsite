import os
from datetime import datetime, timezone

from flask import Flask, render_template, request, jsonify
from supabase import create_client, Client

try:
    # Optional: lets `python app.py` pick up a local .env file.
    # Not required in production if env vars are set another way
    # (e.g. PythonAnywhere's WSGI file or the Web tab's env vars UI).
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key-change-me")

VALID_STATUSES = ["new", "read", "replied", "archived"]

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# ---------------------------------------------------------------------------
# Page routes (mirrors the original site's pages, now server-rendered)
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/dashboard-1")
def dashboard1():
    return render_template("dashboard1.html")


@app.route("/dashboard-2")
def dashboard2():
    return render_template("dashboard2.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


# ---------------------------------------------------------------------------
# API routes — same contract as the original Express + Supabase backend,
# so the copied front-end JS (fetch('/api/contact'), fetch('/api/contacts'))
# works completely unmodified.
# ---------------------------------------------------------------------------

@app.route("/api/health")
def api_health():
    return jsonify(
        {
            "status": "OK",
            "message": "Server is running with Supabase",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    )


@app.route("/api/contacts")
def api_contacts():
    try:
        res = (
            supabase.table("contacts")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )
        data = res.data
        return jsonify({"success": True, "count": len(data), "data": data})
    except Exception as exc:
        return (
            jsonify({"success": False, "message": "Error fetching contacts", "error": str(exc)}),
            500,
        )


@app.route("/api/contacts/<int:contact_id>", methods=["GET"])
def api_contact_get(contact_id):
    try:
        res = (
            supabase.table("contacts")
            .select("*")
            .eq("id", contact_id)
            .maybe_single()
            .execute()
        )
        if res is None or res.data is None:
            return jsonify({"success": False, "message": "Contact not found"}), 404
        return jsonify({"success": True, "data": res.data})
    except Exception as exc:
        return (
            jsonify({"success": False, "message": "Error fetching contact", "error": str(exc)}),
            500,
        )


@app.route("/api/contact", methods=["POST"])
def api_contact_submit():
    payload = request.get_json(silent=True) or {}
    name = (payload.get("name") or "").strip()
    email = (payload.get("email") or "").strip()
    company = (payload.get("company") or "").strip()
    service = (payload.get("service") or "").strip()
    message = (payload.get("message") or "").strip()
    budget = (payload.get("budget") or "").strip()

    if not name or not email or not service or not message:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Please provide all required fields: name, email, service, message",
                }
            ),
            400,
        )

    ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.headers.get("User-Agent", "")

    try:
        res = (
            supabase.table("contacts")
            .insert(
                {
                    "name": name,
                    "email": email,
                    "company": company,
                    "service": service,
                    "message": message,
                    "budget": budget,
                    "ip_address": ip_address,
                    "user_agent": user_agent,
                    "status": "new",
                }
            )
            .execute()
        )
        return (
            jsonify(
                {
                    "success": True,
                    "message": "Contact form submitted successfully!",
                    "data": res.data[0],
                }
            ),
            201,
        )
    except Exception as exc:
        return (
            jsonify(
                {"success": False, "message": "Error submitting contact form", "error": str(exc)}
            ),
            500,
        )


@app.route("/api/contacts/<int:contact_id>", methods=["PATCH"])
def api_contact_update_status(contact_id):
    payload = request.get_json(silent=True) or {}
    status = payload.get("status")

    if status not in VALID_STATUSES:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Invalid status. Must be one of: "
                    + ", ".join(VALID_STATUSES),
                }
            ),
            400,
        )

    try:
        res = (
            supabase.table("contacts")
            .update({"status": status})
            .eq("id", contact_id)
            .execute()
        )
        if not res.data:
            return jsonify({"success": False, "message": "Contact not found"}), 404
        return jsonify(
            {"success": True, "message": "Contact status updated", "data": res.data[0]}
        )
    except Exception as exc:
        return (
            jsonify({"success": False, "message": "Error updating contact", "error": str(exc)}),
            500,
        )


@app.route("/api/contacts/<int:contact_id>", methods=["DELETE"])
def api_contact_delete(contact_id):
    try:
        res = supabase.table("contacts").delete().eq("id", contact_id).execute()
        if not res.data:
            return jsonify({"success": False, "message": "Contact not found"}), 404
        return jsonify(
            {
                "success": True,
                "message": "Contact deleted successfully",
                "data": res.data[0],
            }
        )
    except Exception as exc:
        return (
            jsonify({"success": False, "message": "Error deleting contact", "error": str(exc)}),
            500,
        )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
