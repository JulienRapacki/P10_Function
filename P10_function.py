import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    user_id = req.params.get('user_id')
    if not user_id:
        return func.HttpResponse(
            "Veuillez fournir un ID utilisateur.",
            status_code=400
        )
    
    # Placeholder: recommandation d'exemple
    recommandations = ["item_1", "item_2", "item_3", "item_4", "item_5"]

    return func.HttpResponse(json.dumps(recommandations), mimetype="application/json")