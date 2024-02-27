from openai import OpenAI, OpenAIError
import json
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from typing import List, Dict, Any
import time
import os

from .serializers import FileUploadSerializer
from .models import UploadedFile
from .custom_functions import resume_shortlisting_functions, extract_information_functions



api_key = os.getenv('OPENAI_API_KEY', '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')
client = OpenAI(api_key=api_key)

class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = [MultiPartParser]

class CandidateMatchingView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        data = request.data
        position = data.get('position')
        job_description = data.get('job_description')
        resumes: List[Dict[str, Any]] = data.get('resumes', [])

        if not all([position, job_description, resumes]):
            raise APIException("Missing required data")

        suitable_candidates: List[Dict[str, Any]] = []

        # Function to safely make OpenAI API call with retry logic
        def safe_openai_call(call, attempt=1):
            try:
               response = call()
               function_call = response.choices[0].message.function_call
               if function_call is None:
                  raise ValueError("Function call is missing in the response")
               return json.loads(function_call.arguments)
            except (OpenAIError, ValueError, json.JSONDecodeError) as e:
                print(f"OpenAI API call failed on attempt {attempt}: {str(e)}")
                if attempt < 3: 
                    time.sleep(2 ** attempt)  
                    return safe_openai_call(call, attempt + 1)
                else:
                    raise APIException("OpenAI API call failed after multiple attempts - please try again later!")
                

        # Task 1: Check if the resume is suitable for the job based on match_score
        for resume in resumes:
            match_score_response = safe_openai_call(lambda: client.chat.completions.create(
                    model='gpt-3.5-turbo',
                    messages=[{'role': 'user', 'content': f"Given the job description as {job_description} for position as {position} , Calculate the match score for this resume if candidate possesses required expertise for the role: {resume['text']}"}],
                    functions=resume_shortlisting_functions,
                    function_call='auto'
            ))

            match_score = match_score_response['match_score']
            
            # If match_score is greater than 70, then the candidate is suitable
            if int(match_score) > 70:
                suitable_candidate = {
                    "resume": resume,
                    "match_score": match_score
                }
                suitable_candidates.append(suitable_candidate)

        # Task 2: Extract data for suitable candidates
        for suitable_candidate in suitable_candidates:
            info_response = safe_openai_call(lambda: client.chat.completions.create(
                    model='gpt-3.5-turbo',
                    messages=[{'role': 'user', 'content': f"Extract name, projects, professional_experience and college for this resume: {suitable_candidate['resume']['text']}" + "Also the job description is: " + job_description}],
                    functions=extract_information_functions,
                    function_call='auto'
                ))

            suitable_candidate.update({
                'projects': info_response['projects'],
                'professional_experience': info_response['professional_experience'],
                'college': info_response['college'],
                'name': info_response['name']
            })

        return Response({"suitable_candidates": suitable_candidates})

