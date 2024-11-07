import json
import pandas as pd
from io import StringIO
import azure.functions as func

def main(req: func.HttpRequest, inputBlob: func.InputStream) -> func.HttpResponse:
    user_id = req.params.get('user_id')
    if not user_id:
        return func.HttpResponse(
            "Veuillez fournir un ID utilisateur.",
            status_code=400
        )
    
    # Charger les données depuis l’input binding
    data = inputBlob.read().decode('utf-8')
    df = pd.read_csv(StringIO(data))

    # Logique de recommandation
    recommendations = df[df['user_id'] == int(user_id)]['click_article_id'].head(5).tolist()

    return func.HttpResponse(json.dumps(recommendations), mimetype="application/json")
