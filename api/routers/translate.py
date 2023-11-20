from fastapi import APIRouter
from google.cloud import translate_v2

router = APIRouter()

client = translate_v2.Client.from_service_account_json(
    'app-deploy-hackathon-2023-b2e6f1b4ed11.json'
)


@router.get("/translate/{text}/{target_lang}")
async def translate(text: str, target_lang: str):
    result = client.translate(text, target_language=target_lang)
    # print(result)
    translated_text = result['translatedText']
    return {"input_text": text, "translated_text": translated_text}
